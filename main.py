import re
import requests
import time
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from typing import List, Optional, Tuple
from dataclasses import dataclass, field

OUTPUT_FILE = "DocumentationUCZONE.md"
URLS_FILE = "urls.txt"
LLMS_URL = "https://uczone.gitbook.io/api-v2.0/llms.txt"

COMMON_NOISE = re.compile(
    r"For the complete documentation index, see .*?llms\.txt.*?\. Markdown versions of documentation pages are available by appending `?\.md`? to page URLs; this page is available as \[Markdown\]\(.*?\)\.",
    re.IGNORECASE | re.DOTALL
)

def strip_gitbook_noise(markdown_text: str) -> str:
    """Улучшенная чистка + удаление повторяющейся фразы."""
    if not markdown_text:
        return markdown_text

    # Удаляем основной шум
    cleaned = COMMON_NOISE.sub("", markdown_text)
    cleaned = re.sub(r"^\s*copy\s*$", "", cleaned, flags=re.IGNORECASE | re.MULTILINE)
    cleaned = re.sub(r"{%\s*hint.*?%}|{%\s*endhint\s*%}", "", cleaned, flags=re.IGNORECASE)

    lines = [line for line in cleaned.splitlines() if line.strip()]
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def fetch_llms_structure() -> List[Tuple[str, str]]:
    """Автоматический парсинг llms.txt → список (title, url)."""
    try:
        resp = requests.get(LLMS_URL, timeout=15)
        resp.raise_for_status()
        content = resp.text

        # Парсим Markdown-список: - [Title](url)
        pattern = r"-\s*\[([^\]]+)\]\((https?://[^\)]+)\)"
        matches = re.findall(pattern, content)
        print(f"✅ Извлечено {len(matches)} ссылок из llms.txt")
        return matches
    except Exception as e:
        print(f"⚠️ Ошибка загрузки llms.txt: {e}. Используем urls.txt")
        return []


def load_urls_from_file(filepath: str) -> List[str]:
    """Fallback."""
    path = Path(filepath)
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


@dataclass
class PageGroup:
    title: str
    match_pattern: str
    level: int
    urls: List[str] = field(default_factory=list)


# Более умная базовая структура (можно расширять)
STRUCTURE_DEFINITIONS = [
    PageGroup("Starting Guide", "getting-started", 1),
    PageGroup("Cheats Types and Callbacks", "cheats-types-and-callbacks", 1),
    PageGroup("Classes - Color", "classes/color", 2),
    PageGroup("Classes - Menu System", "classes/menu", 2),
    PageGroup("Classes - UI Widgets", "classes/widgets", 2),
    PageGroup("Classes - Math", "classes/math", 2),
    PageGroup("Game Components - Entity Lists", "game-components/lists", 1),
    PageGroup("Game Components - Core Objects", "game-components/core", 1),
    PageGroup("Game Engine", "game-components/game-engine", 1),
    PageGroup("Networking and APIs", "networking-and-apis", 1),
    PageGroup("Rendering and Visuals", "rendering-and-visuals", 1),
    PageGroup("Rendering - Panorama UI", "rendering-and-visuals/panorama", 2),
    PageGroup("Configuration and Utilities", "configuration-and-utilities", 1),
]


def distribute_urls(urls: List[str], groups: List[PageGroup]):
    """Улучшенное распределение (самое длинное совпадение + fallback)."""
    for url in urls:
        best_match = None
        max_len = -1
        for group in groups:
            if group.match_pattern in url:
                if len(group.match_pattern) > max_len:
                    max_len = len(group.match_pattern)
                    best_match = group
        if best_match:
            best_match.urls.append(url)
        else:
            print(f"⚠️ Нет группы для: {url}")
            groups[0].urls.append(url)  # fallback


def get_markdown_content(url: str) -> Optional[str]:
    """Получение .md + fallback."""
    try:
        md_url = url if url.endswith('.md') else f"{url}.md"
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(md_url, headers=headers, timeout=15)
        resp.raise_for_status()
        content = resp.text.strip()

        if content.startswith('<!DOCTYPE') or '<html' in content[:500]:
            # fallback to HTML
            return get_markdown_from_html(url)
        return strip_gitbook_noise(content)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return get_markdown_from_html(url)
        return None
    except Exception:
        return get_markdown_from_html(url)


def get_markdown_from_html(url: str) -> Optional[str]:
    """Fallback HTML → MD (без изменений)."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, 'html.parser')
        main = soup.find('main')
        if not main:
            return None
        for nav in main.find_all(['nav', 'footer']):
            nav.decompose()
        markdown_text = md(str(main), heading_style="ATX")
        return strip_gitbook_noise(markdown_text)
    except Exception as e:
        print(f"   ❌ Fallback error: {e}")
        return None


def generate_toc(groups: List[PageGroup]) -> str:
    """TOC (без изменений)."""
    toc = ["# Оглавление\n"]
    for group in groups:
        if not group.urls:
            continue
        indent = "  " * (group.level - 1)
        anchor = group.title.lower().replace(" ", "-").replace("_", "-")
        toc.append(f"{indent}- [{group.title}](#{anchor})")
    return "\n".join(toc) + "\n\n"


def main():
    # 1. Автоматический парсинг llms.txt
    structure = fetch_llms_structure()
    urls = [url for _, url in structure] if structure else load_urls_from_file(URLS_FILE)

    if not urls:
        print("❌ Нет URL.")
        return

    # 2. Распределение
    active_groups = [g for g in STRUCTURE_DEFINITIONS]
    for g in active_groups:
        g.urls = []
    distribute_urls(urls, active_groups)
    active_groups = [g for g in active_groups if g.urls]

    total = sum(len(g.urls) for g in active_groups)
    print(f"🚀 Парсинг {total} страниц...")

    common_intro = (
        "> **Полная документация**: [llms.txt](https://uczone.gitbook.io/api-v2.0/llms.txt)\n"
        "> Markdown-версии доступны путём добавления `.md` к URL.\n\n"
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# UCZONE API v2.0 - Полная документация\n\n")
        f.write(f"*Сгенерировано из {total} страниц GitBook*\n\n")
        f.write("---\n\n")
        f.write(common_intro)          # Одна общая фраза в начале
        f.write(generate_toc(active_groups))
        f.write("\n" + "=" * 80 + "\n\n")

        processed = 0
        for group in active_groups:
            heading = "#" * (group.level + 1)
            f.write(f"{heading} {group.title}\n\n")

            for url in group.urls:
                processed += 1
                print(f"[{processed}/{total}] {group.title}: {url}")
                content = get_markdown_content(url)
                if content:
                    f.write(f"<!-- Source: {url} -->\n\n")
                    f.write(content + "\n\n")
                else:
                    f.write(f"> ⚠️ Не удалось: {url}\n\n")
                time.sleep(0.3)

            f.write("\n" + "-" * 80 + "\n\n")

    print(f"✅ Готово: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
