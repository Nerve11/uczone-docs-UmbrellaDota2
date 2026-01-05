import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_URL = "https://uczone.gitbook.io/api-v2.0"
OUTPUT_FILE = "DocumentationUCZONE.md"
OUTPUT_DIR = Path("docs_md")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36",
}


@dataclass
class MenuNode:
    title: str
    url: str
    children: List["MenuNode"] = field(default_factory=list)


# ----------------------------
# URL + text helpers
# ----------------------------

def normalize_url(url: str) -> str:
    url = url.strip()
    url = url.split("#", 1)[0]
    url = url.rstrip("/")
    return url


def is_internal_doc_url(url: str) -> bool:
    url = normalize_url(url)
    return url.startswith(BASE_URL)


def slugify_anchor(text: str) -> str:
    t = text.strip().lower()
    t = re.sub(r"[^a-z0-9\u0400-\u04ff\s_-]", "", t)
    t = t.replace("_", "-")
    t = re.sub(r"\s+", "-", t)
    t = re.sub(r"-+", "-", t)
    return t.strip("-")


def url_to_local_md_path(url: str) -> Path:
    """Maps https://uczone.gitbook.io/api-v2.0/a/b -> docs_md/a/b.md"""
    path = urlparse(normalize_url(url)).path
    if path.startswith("/api-v2.0"):
        rel = path[len("/api-v2.0") :].lstrip("/")
    else:
        rel = path.lstrip("/")

    if not rel:
        rel = "index"

    # keep URL path segments; just make sure it is a safe path
    rel = rel.replace("..", "")
    return OUTPUT_DIR / f"{rel}.md"


# ----------------------------
# Fetch + parse
# ----------------------------

def fetch_html(url: str) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=25)
    resp.raise_for_status()
    return resp.text


def pick_best_nav_container(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Pick nav/aside container with max number of internal doc links."""
    candidates = []

    for tag_name in ("nav", "aside"):
        for el in soup.find_all(tag_name):
            links = el.select("a[href]")
            cnt = 0
            for a in links:
                href = a.get("href", "").strip()
                if not href:
                    continue
                full = normalize_url(urljoin(BASE_URL, href))
                if is_internal_doc_url(full):
                    cnt += 1
            candidates.append((cnt, el))

    # fallback: any element that looks like sidebar
    for el in soup.find_all(["div", "section"]):
        cls = " ".join(el.get("class", [])).lower()
        if not cls:
            continue
        if any(k in cls for k in ("sidebar", "navigation", "toc")):
            links = el.select("a[href]")
            cnt = 0
            for a in links:
                href = a.get("href", "").strip()
                full = normalize_url(urljoin(BASE_URL, href))
                if is_internal_doc_url(full):
                    cnt += 1
            candidates.append((cnt, el))

    if not candidates:
        return None

    candidates.sort(key=lambda x: x[0], reverse=True)
    best_cnt, best_el = candidates[0]
    return best_el if best_cnt > 0 else None


def parse_menu_tree_from_ul(container: BeautifulSoup, page_url: str) -> Optional[List[MenuNode]]:
    ul = container.find("ul")
    if not ul:
        return None

    def parse_ul(ul_tag) -> List[MenuNode]:
        nodes: List[MenuNode] = []
        for li in ul_tag.find_all("li", recursive=False):
            a = li.find("a", href=True)
            if not a:
                continue
            title = " ".join(a.get_text(" ", strip=True).split())
            href = a.get("href", "")
            full = normalize_url(urljoin(page_url, href))
            if not title or not is_internal_doc_url(full):
                continue

            child_ul = li.find("ul")
            children = parse_ul(child_ul) if child_ul else []
            nodes.append(MenuNode(title=title, url=full, children=children))
        return nodes

    tree = parse_ul(ul)
    return tree if tree else None


def parse_menu_tree_from_aria(container: BeautifulSoup, page_url: str) -> Optional[List[MenuNode]]:
    """Parse menu from aria-level treeitems (common in SPA sidebars)."""
    items = container.select("[aria-level] a[href]")
    if not items:
        # some layouts put aria-level directly on clickable node
        items = container.select("a[aria-level][href]")

    rows: List[Tuple[int, str, str]] = []
    for a in items:
        try:
            lvl_raw = a.get("aria-level") or (a.find_parent(attrs={"aria-level": True}) or {}).get("aria-level")
            lvl = int(lvl_raw) if lvl_raw else 1
        except Exception:
            lvl = 1

        title = " ".join(a.get_text(" ", strip=True).split())
        href = a.get("href", "").strip()
        full = normalize_url(urljoin(page_url, href))
        if not title or not is_internal_doc_url(full):
            continue

        rows.append((lvl, title, full))

    if not rows:
        return None

    # Build tree using stack
    root: List[MenuNode] = []
    stack: List[Tuple[int, MenuNode]] = []

    for lvl, title, full in rows:
        node = MenuNode(title=title, url=full)

        while stack and stack[-1][0] >= lvl:
            stack.pop()

        if not stack:
            root.append(node)
        else:
            stack[-1][1].children.append(node)

        stack.append((lvl, node))

    return root if root else None


def parse_menu_tree_fallback_flat(container: BeautifulSoup, page_url: str) -> List[MenuNode]:
    seen = set()
    out: List[MenuNode] = []
    for a in container.select("a[href]"):
        href = a.get("href", "").strip()
        if not href:
            continue
        if href.startswith(("mailto:", "tel:", "javascript:")):
            continue
        full = normalize_url(urljoin(page_url, href))
        if not is_internal_doc_url(full):
            continue
        if full in seen:
            continue
        title = " ".join(a.get_text(" ", strip=True).split())
        if not title:
            continue
        seen.add(full)
        out.append(MenuNode(title=title, url=full))
    return out


def discover_menu_tree() -> List[MenuNode]:
    """Discover menu structure from GitBook sidebar."""
    html = fetch_html(BASE_URL)
    soup = BeautifulSoup(html, "html.parser")

    container = pick_best_nav_container(soup)
    if not container:
        raise RuntimeError("Не удалось найти контейнер меню (nav/aside) на стартовой странице")

    # Try multiple strategies
    tree = (
        parse_menu_tree_from_aria(container, BASE_URL)
        or parse_menu_tree_from_ul(container, BASE_URL)
        or parse_menu_tree_fallback_flat(container, BASE_URL)
    )

    # Ensure root page is included
    if not any(normalize_url(n.url) == normalize_url(BASE_URL) for n in tree):
        tree.insert(0, MenuNode(title="Starting Guide", url=normalize_url(BASE_URL)))

    return tree


# ----------------------------
# Markdown fetching
# ----------------------------

def get_markdown_from_html(url: str) -> Optional[str]:
    try:
        response = requests.get(url, headers=HEADERS, timeout=25)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        main_content = soup.find("main")
        if not main_content:
            return None

        for element in main_content.find_all(["nav", "footer", "aside"]):
            element.decompose()

        markdown_text = md(str(main_content), heading_style="ATX")
        return markdown_text.strip()

    except Exception as e:
        print(f"   ❌ HTML fallback ошибка: {e}")
        return None


def get_markdown_content(url: str) -> Optional[str]:
    """Prefer direct .md, fallback to HTML->MD."""
    url = normalize_url(url)
    try:
        markdown_url = url if url.endswith(".md") else f"{url}.md"
        response = requests.get(markdown_url, headers=HEADERS, timeout=25)
        response.raise_for_status()
        content = response.text.strip()

        if content.startswith("<!DOCTYPE") or content.startswith("<html"):
            return get_markdown_from_html(url)

        return content

    except requests.exceptions.HTTPError as e:
        if getattr(e.response, "status_code", None) == 404:
            return get_markdown_from_html(url)
        print(f"   ❌ HTTP ошибка при .md: {e}")
        return None
    except Exception as e:
        print(f"   ⚠️  Ошибка при .md доступе: {e}")
        return get_markdown_from_html(url)


# ----------------------------
# Cleaning + formatting
# ----------------------------

def strip_gitbook_noise(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    out: List[str] = []

    # very conservative filters
    noise_patterns = [
        re.compile(r"^\s*last\s+updated\b", re.IGNORECASE),
        re.compile(r"^\s*(previous|next)\s*$", re.IGNORECASE),
        re.compile(r"^\s*\[(previous|next)\]\s*\(.*\)\s*$", re.IGNORECASE),
    ]

    for line in lines:
        s = line.strip()
        if not s:
            out.append(line)
            continue
        if any(p.search(s) for p in noise_patterns):
            continue
        out.append(line)

    # collapse multiple blank lines
    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip() + "\n"


def shift_headings(markdown_text: str, shift: int) -> str:
    if shift <= 0:
        return markdown_text

    out_lines = []
    for line in markdown_text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if not m:
            out_lines.append(line)
            continue
        lvl = len(m.group(1))
        new_lvl = min(6, lvl + shift)
        out_lines.append("#" * new_lvl + " " + m.group(2))
    return "\n".join(out_lines).strip() + "\n"


def drop_leading_h1(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    if lines and re.match(r"^#\s+", lines[0]):
        return "\n".join(lines[1:]).lstrip() + "\n"
    return markdown_text


def generate_toc_from_tree(tree: List[MenuNode]) -> str:
    lines = ["# Оглавление", ""]

    def walk(nodes: List[MenuNode], depth: int):
        for n in nodes:
            indent = "  " * depth
            anchor = slugify_anchor(n.title)
            lines.append(f"{indent}- [{n.title}](#{anchor})")
            if n.children:
                walk(n.children, depth + 1)

    walk(tree, 0)
    return "\n".join(lines).strip() + "\n\n"


# ----------------------------
# Export
# ----------------------------

def export_page_md(url: str, title: str) -> Optional[Path]:
    content = get_markdown_content(url)
    if not content:
        return None

    content = strip_gitbook_noise(content)

    path = url_to_local_md_path(url)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"<!-- Source: {normalize_url(url)} -->\n")
        f.write(f"<!-- Title: {title} -->\n\n")
        f.write(content)

    return path


def build_single_markdown(tree: List[MenuNode]) -> None:
    # First: export every page as separate md (also builds a url->path map)
    url_to_path = {}

    def walk_export(nodes: List[MenuNode]):
        for n in nodes:
            print(f"🧾 Экспорт страницы: {n.title} -> {n.url}")
            p = export_page_md(n.url, n.title)
            if p:
                url_to_path[normalize_url(n.url)] = p
                print(f"   ✅ сохранено: {p}")
            else:
                print("   ❌ не удалось скачать")
            time.sleep(0.25)
            if n.children:
                walk_export(n.children)

    walk_export(tree)

    # Second: build combined documentation following menu order
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# UCZONE API v2.0 - Полная документация\n\n")
        f.write(f"*Source: {BASE_URL}*\n\n")
        f.write("---\n\n")
        f.write(generate_toc_from_tree(tree))
        f.write("---\n\n")

        def walk_write(nodes: List[MenuNode], depth: int):
            for n in nodes:
                heading_level = min(6, 2 + depth)  # root items => ##
                f.write("#" * heading_level + f" {n.title}\n\n")
                f.write(f"<!-- Source: {normalize_url(n.url)} -->\n\n")

                page_md = get_markdown_content(n.url)
                if page_md:
                    page_md = strip_gitbook_noise(page_md)
                    page_md = drop_leading_h1(page_md)
                    # shift headings so that in-page H2 becomes deeper than section header
                    page_md = shift_headings(page_md, heading_level - 1)
                    f.write(page_md)
                    f.write("\n")
                else:
                    f.write(f"> ⚠️ Не удалось загрузить: {n.url}\n\n")

                if n.children:
                    walk_write(n.children, depth + 1)

        walk_write(tree, 0)

    print(f"\n✅ Готово: {OUTPUT_FILE}")
    print(f"📁 Отдельные страницы сохранены в: {OUTPUT_DIR}")


def main():
    print("🚀 Старт")
    print(f"🔎 Строим структуру меню GitBook из: {BASE_URL}")
    tree = discover_menu_tree()
    print("✅ Меню получено, начинаем экспорт страниц...")
    build_single_markdown(tree)


if __name__ == "__main__":
    main()
