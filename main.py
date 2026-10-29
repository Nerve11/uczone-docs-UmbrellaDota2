import re
import time
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

OUTPUT_FILE = "DocumentationUCZONE.md"
URLS_FILE = "urls.txt"
LLMS_URL = "https://uczone.gitbook.io/api-v2.0/llms.txt"
BASE_DOCS_URL = "https://uczone.gitbook.io/api-v2.0"
ENUMS_MD_URL = f"{BASE_DOCS_URL}/cheats-types-and-callbacks/enums.md"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/markdown, text/plain;q=0.9, text/html;q=0.8, */*;q=0.5",
}

# Удаляет стандартную шапку GitBook (включая символ цитаты `>` в начале строки)
COMMON_NOISE = re.compile(
    r"^\s*>?\s*For the complete documentation index, see .*?llms\.txt.*?"
    r"Markdown versions of documentation pages are available by appending `?\.md`? to page URLs; "
    r"this page is available as \[Markdown\]\(.*?\)\.[ \t]*$",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)

# Директивы GitBook ({% hint %}, {% tabs %}, {% code %} и т.д.)
GITBOOK_DIRECTIVE_RE = re.compile(
    r"\{%\s*(?:end)?(?:hint|tabs|tab|code|embed|swagger|content-ref).*?%\}",
    re.IGNORECASE,
)

# Битые внутренние ссылки GitBook на страницу Enums (pages/VwVljl88Qnl7u9hhqRdw#enum.xxx)
BROKEN_ENUM_LINK_RE = re.compile(
    r"(?:https?://uczone\.gitbook\.io/api-v2\.0/[^)\s]*/|/api-v2\.0/[^)\s]*/)?pages/VwVljl88Qnl7u9hhqRdw(#enum\.[a-zA-Z0-9_]+)",
    re.IGNORECASE,
)

# Индексные страницы-каталоги из llms.txt, которые содержат только список ссылок на дочерние страницы
INDEX_ONLY_PATHS = {
    "cheats-types-and-callbacks/classes.md",
    "cheats-types-and-callbacks/classes/widgets.md",
    "cheats-types-and-callbacks/classes/math.md",
    "game-components/lists.md",
    "game-components/core.md",
    "game-components/game-engine.md",
    "game-components/networking-and-apis.md",
    "game-components/rendering-and-visuals.md",
    "game-components/rendering-and-visuals/panorama.md",
    "game-components/configuration-and-utilities.md",
}


@dataclass
class ParsedPage:
    url: str
    title: str
    raw_markdown: str
    formatted_markdown: str = ""
    section_number: str = ""
    heading_level: int = 3


@dataclass
class PageGroup:
    title: str
    match_pattern: str
    level: int
    urls: List[str] = field(default_factory=list)
    pages: List[ParsedPage] = field(default_factory=list)
    section_number: str = ""


# Иерархическая структура глав (level=1) и подглав (level=2)
STRUCTURE_DEFINITIONS: List[PageGroup] = [
    PageGroup("Starting Guide", "getting-started", 1),
    PageGroup("Cheats Types and Callbacks", "cheats-types-and-callbacks", 1),
    PageGroup("Classes - Color", "cheats-types-and-callbacks/classes/color", 2),
    PageGroup("Classes - Menu System", "cheats-types-and-callbacks/classes/menu", 2),
    PageGroup("Classes - UI Widgets", "cheats-types-and-callbacks/classes/widgets", 2),
    PageGroup("Classes - Math", "cheats-types-and-callbacks/classes/math", 2),
    PageGroup("Game Components - Entity Lists", "game-components/lists", 1),
    PageGroup("Game Components - Core Objects", "game-components/core", 1),
    PageGroup("Game Engine", "game-components/game-engine", 1),
    PageGroup("Networking and APIs", "game-components/networking-and-apis", 1),
    PageGroup("Rendering and Visuals", "game-components/rendering-and-visuals", 1),
    PageGroup("Rendering - Panorama UI", "game-components/rendering-and-visuals/panorama", 2),
    PageGroup("Configuration and Utilities", "game-components/configuration-and-utilities", 1),
]


def create_http_session() -> requests.Session:
    """Создаёт HTTP-сессию с автоматическими повторами при временных сбоях сети."""
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET", "HEAD"),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(HEADERS)
    return session


def normalize_md_url(url: str) -> str:
    """Нормализует ссылку так, чтобы она гарантированно вела напрямую на .md файл."""
    cleaned = url.strip()
    if not cleaned:
        return ""
    # Извлекаем URL, если строка записана в формате Markdown-ссылки: - [Title](url)
    md_link_match = re.search(r"\((https?://[^\s\)]+)\)", cleaned)
    if md_link_match:
        cleaned = md_link_match.group(1).strip()

    # Убираем якоря и query-параметры
    cleaned = cleaned.split("#")[0].split("?")[0].strip().rstrip("/")
    if not cleaned.endswith(".md"):
        cleaned = f"{cleaned}.md"
    return cleaned


def get_html_url(url: str) -> str:
    """Возвращает HTML-версию ссылки (без суффикса .md) для резервного парсинга."""
    cleaned = normalize_md_url(url)
    if cleaned.endswith(".md"):
        return cleaned[:-3]
    return cleaned


def get_relative_doc_path(url: str) -> str:
    """Извлекает относительный путь документа после /api-v2.0/."""
    cleaned = normalize_md_url(url)
    marker = "/api-v2.0/"
    if marker in cleaned:
        return cleaned.split(marker, 1)[1]
    return cleaned


def make_markdown_anchor(heading_text: str) -> str:
    """Генерирует GitHub-совместимый Markdown-якорь для оглавления."""
    text = heading_text.strip().lower()
    # Удаляем символы кроме букв, цифр, пробелов и дефисов (сохраняя пробелы и дефисы)
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = text.replace(" ", "-")
    return text


def clean_inline_gitbook_line(line: str) -> str:
    """Очищает строку вне блока кода от HTML-шума GitBook и лишнего экранирования."""
    # Заменяем конструкцию `&#x20;**` на `** ` (чтобы пробел выносился за закрывающие `**`),
    # а оставшиеся HTML-сущности пробела `&#x20;` заменяем на обычный пробел
    line = line.replace("&#x20;**", "** ")
    line = line.replace("&#x20;", " ")

    # Удаляем теги <mark ...> и </mark>, сохраняя их внутренний текст
    line = re.sub(r"</?mark[^>]*>", "", line, flags=re.IGNORECASE)

    # Удаляем теги <sub> и </sub>
    line = re.sub(r"</?sub>", "", line, flags=re.IGNORECASE)

    # Починка битых внутренних ссылок GitBook на страницу Enums
    line = BROKEN_ENUM_LINK_RE.sub(f"{ENUMS_MD_URL}\\1", line)

    # Преобразование относительных ссылок /api-v2.0/... в полные ссылки
    line = re.sub(r"\]\(/api-v2\.0/([^\)]+)\)", f"]({BASE_DOCS_URL}/\\1)", line)

    # Удаляем висячий обратный слеш переноса строки в конце обычного текста
    line = re.sub(r"\\\s*$", "", line)

    # Снимаем избыточное экранирование Markdown-символов GitBook (`\_`, `\*`, `` \` ``, `\[`, `\]`),
    # но НЕ трогаем `\|` внутри таблиц, чтобы не ломать ячейки с объединением типов (`CEntity \| nil`)
    line = line.replace(r"\`", "`")
    line = line.replace(r"\*", "*")
    line = line.replace(r"\_", "_")
    line = line.replace(r"\[", "[")
    line = line.replace(r"\]", "]")

    return line.rstrip()


def strip_gitbook_noise(markdown_text: str) -> str:
    """Очищает прямой .md текст из GitBook, сохраняя структуру таблиц, блоков кода и абзацев."""
    if not markdown_text:
        return ""

    # 1. Удаляем стандартную шапку GitBook и директивы {% ... %}
    cleaned = COMMON_NOISE.sub("", markdown_text)
    cleaned = GITBOOK_DIRECTIVE_RE.sub("", cleaned)

    # 2. Построчная обработка с защитой содержимого блоков кода ``` ... ```
    raw_lines = cleaned.splitlines()
    processed_lines: List[str] = []
    in_code_block = False

    for line in raw_lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            processed_lines.append(line.rstrip())
            continue

        if in_code_block:
            processed_lines.append(line.rstrip("\r"))
            continue

        # Пропускаем мусорные строки "copy" и пустые цитаты ">" (остатки от шапки GitBook)
        if re.match(r"^\s*copy\s*$", stripped, flags=re.IGNORECASE):
            continue
        if re.match(r"^\s*>\s*$", stripped):
            continue

        processed_lines.append(clean_inline_gitbook_line(line))

    # 3. Нормализация пустых строк вокруг заголовков, таблиц, <details> и блоков кода,
    #    чтобы таблицы и списки никогда не слипались с соседним текстом
    spaced_lines = ensure_markdown_block_spacing(processed_lines)
    result = "\n".join(spaced_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


def ensure_markdown_block_spacing(lines: List[str]) -> List[str]:
    """Гарантирует корректные пустые строки вокруг заголовков, таблиц, блоков кода и <details>."""
    out: List[str] = []
    in_code_block = False
    in_table = False

    def add_blank_if_needed():
        if out and out[-1].strip() != "":
            out.append("")

    for line in lines:
        stripped = line.strip()

        # Обработка границ блока кода ```
        if stripped.startswith("```"):
            if not in_code_block:
                add_blank_if_needed()
                out.append(line)
                in_code_block = True
                in_table = False
            else:
                out.append(line)
                out.append("")
                in_code_block = False
            continue

        if in_code_block:
            out.append(line)
            continue

        is_table_row = stripped.startswith("|") and stripped.endswith("|")
        is_heading = bool(re.match(r"^#{1,6}\s+", stripped))
        is_hr = bool(re.match(r"^(?:\*\*\*+|---+|___+)\s*$", stripped))

        # Если таблица закончилась, перед следующим непустым текстом нужна пустая строка
        if in_table and not is_table_row:
            add_blank_if_needed()
            in_table = False

        # Если таблица начинается, перед ней нужна пустая строка
        if is_table_row and not in_table:
            add_blank_if_needed()
            in_table = True

        if is_heading or is_hr:
            add_blank_if_needed()
            out.append(line)
            out.append("")
            continue

        if stripped.startswith("<details") or stripped == "</details>":
            add_blank_if_needed()
            out.append(line)
            out.append("")
            continue

        if stripped.startswith("<summary>") and stripped.endswith("</summary>"):
            out.append(line)
            out.append("")
            continue

        out.append(line)

    return out


def extract_page_title(markdown_text: str, fallback_url: str = "") -> str:
    """Извлекает заголовок первого уровня (# Title) из .md текста страницы."""
    in_code_block = False
    for line in markdown_text.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if not in_code_block:
            match = re.match(r"^#\s+(.+)$", line.strip())
            if match:
                return match.group(1).strip()

    if fallback_url:
        stem = Path(normalize_md_url(fallback_url)).stem
        return stem.replace("_", " ").replace("-", " ").title()
    return "Untitled"


def qualify_method_heading(
    raw_heading: str,
    page_title: str,
    following_lines: List[str],
    is_overloaded: bool = False,
) -> str:
    """
    Формирует полное квалифицированное имя метода/функции (например, `Hero.GetCurrentXP` или `CMenuSwitch:Get`),
    чтобы ИИ и поиск по заголовкам безошибочно определяли принадлежность метода к классу/таблице.
    Для перегруженных методов на одной странице добавляет сигнатуру параметров.
    """
    clean_name = raw_heading.strip()
    if clean_name.startswith("Enum."):
        return clean_name

    # Ищем строку сигнатуры в следующих нескольких строках (например: `Hero.GetCurrentXP(hero):` или `:Get():`)
    signature_line = ""
    for candidate in following_lines[:6]:
        s = candidate.strip()
        if not s:
            continue
        if s.startswith("#") or s.startswith("|"):
            break
        if s.startswith("`"):
            signature_line = s
            break

    if signature_line and "`" in signature_line:
        code_span = signature_line.split("`")[1].strip().rstrip(":")
        callee = code_span.split("(")[0].strip() if "(" in code_span else code_span
        params_part = "(" + code_span.split("(", 1)[1] if "(" in code_span else ""

        if callee.startswith(":"):
            base_qual = f"{page_title}{callee}"
        elif "." in callee or ":" in callee:
            base_qual = callee
        elif callee == page_title:
            return f"{page_title} ({code_span})"
        else:
            base_qual = f"{page_title}.{callee}"

        if is_overloaded and params_part:
            return f"{base_qual}{params_part}"
        return base_qual

    return clean_name


def format_page_for_chapter(
    markdown_text: str,
    url: str,
    section_number: str,
    page_heading_level: int,
    breadcrumb: str,
) -> Tuple[str, str]:
    """
    Форматирует .md страницу для встраивания в главу/подглаву:
    - Извлекает заголовок страницы и делает его подглавой нужного уровня (`###` или `####`) с номером раздела.
    - Добавляет блок метаданных (Глава, Раздел, Источник) для точного поиска ИИ.
    - Выравнивает все внутренние заголовки методов/полей/примеров строго глубже заголовка страницы.
    """
    page_title = extract_page_title(markdown_text, url)
    lines = markdown_text.splitlines()

    # Проверяем, содержит ли страница методы API (строки вида `Class.Method(...)` или `:Method(...)`)
    has_api_signatures = any(
        re.match(r"^`(?::[A-Za-z0-9_]+|[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)?)\([^\n`]*\):`", l.strip())
        for l in lines
    )

    # Подсчитываем заголовки 2-го уровня на странице, чтобы выявлять перегруженные методы
    h2_counts: Counter = Counter()
    in_code_scan = False
    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            in_code_scan = not in_code_scan
            continue
        if not in_code_scan:
            m2 = re.match(r"^##\s+(.+)$", s)
            if m2:
                h2_counts[m2.group(1).strip()] += 1

    body_lines: List[str] = []
    in_code_block = False
    first_h1_skipped = False
    method_level = min(page_heading_level + 1, 6)
    sub_method_level = min(page_heading_level + 2, 6)

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            body_lines.append(line)
            continue

        if in_code_block:
            body_lines.append(line)
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading_match:
            hashes, h_text = heading_match.group(1), heading_match.group(2).strip()
            orig_level = len(hashes)

            # Пропускаем первый заголовок # PageTitle, так как мы создаём нумерованный заголовок подглавы
            if orig_level == 1 and not first_h1_skipped:
                first_h1_skipped = True
                continue

            if orig_level == 2:
                if has_api_signatures:
                    qualified = qualify_method_heading(
                        raw_heading=h_text,
                        page_title=page_title,
                        following_lines=lines[idx + 1 :],
                        is_overloaded=(h2_counts[h_text] > 1),
                    )
                    body_lines.append(f"{'#' * method_level} {qualified}")
                else:
                    body_lines.append(f"{'#' * method_level} {h_text}")
            elif orig_level == 3 and h_text.lower() == "fields":
                body_lines.append(f"{'#' * method_level} {page_title} - Fields")
            else:
                body_lines.append(f"{'#' * sub_method_level} {h_text}")
            continue

        body_lines.append(line)

    spaced_body = "\n".join(ensure_markdown_block_spacing(body_lines))
    spaced_body = re.sub(r"\n{3,}", "\n\n", spaced_body).strip()

    page_hashes = "#" * page_heading_level
    filename = Path(normalize_md_url(url)).name
    header_block = (
        f"{page_hashes} {section_number}. {page_title}\n\n"
        f"<!-- Source: {url} -->\n"
        f"> **Навигация:** {breadcrumb} → `{page_title}` | **Источник:** [{filename}]({url})\n\n"
    )

    return page_title, header_block + spaced_body


def load_urls_from_file(filepath: str = URLS_FILE) -> List[str]:
    """Загружает и нормализует список прямых ссылок на .md файлы из urls.txt."""
    path = Path(filepath)
    if not path.exists():
        return []

    urls: List[str] = []
    seen = set()
    with open(path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            norm_url = normalize_md_url(line)
            if norm_url and norm_url not in seen:
                seen.add(norm_url)
                urls.append(norm_url)

    print(f"✅ Загружено {len(urls)} .md ссылок из {filepath}")
    return urls


def fetch_llms_structure(session: Optional[requests.Session] = None) -> List[Tuple[str, str]]:
    """Резервный автоматический парсинг llms.txt → список (title, md_url)."""
    http = session or create_http_session()
    try:
        resp = http.get(LLMS_URL, timeout=15)
        resp.raise_for_status()
        resp.encoding = "utf-8"
        content = resp.text

        pattern = r"-\s*\[([^\]]+)\]\((https?://[^\)]+)\)"
        raw_matches = re.findall(pattern, content)
        results: List[Tuple[str, str]] = []
        seen = set()
        for title, url in raw_matches:
            md_url = normalize_md_url(url)
            rel_path = get_relative_doc_path(md_url)
            if rel_path in INDEX_ONLY_PATHS or md_url in seen:
                continue
            seen.add(md_url)
            results.append((title.strip(), md_url))

        print(f"✅ Извлечено {len(results)} .md ссылок из llms.txt")
        return results
    except Exception as e:
        print(f"⚠️ Ошибка загрузки llms.txt: {e}")
        return []


def distribute_urls(urls: List[str], groups: List[PageGroup]) -> None:
    """
    Распределяет .md ссылки по главам и подглавам.
    Использует относительный путь после /api-v2.0/ и выбирает наиболее специфичную подглаву
    (с наибольшим уровнем вложенности, количеством сегментов пути и длиной совпадения).
    """
    for url in urls:
        norm_url = normalize_md_url(url)
        rel_path = get_relative_doc_path(norm_url)

        best_match: Optional[PageGroup] = None
        best_score: Tuple[int, int, int] = (-1, -1, -1)

        for group in groups:
            pattern = group.match_pattern.strip("/")
            # Проверяем совпадение по префиксу относительного пути или вхождению сегмента
            if (
                rel_path.startswith(pattern + "/")
                or rel_path == f"{pattern}.md"
                or f"/{pattern}/" in f"/{rel_path}"
                or f"/{pattern}.md" in f"/{rel_path}"
            ):
                score = (group.level, pattern.count("/") + 1, len(pattern))
                if score > best_score:
                    best_score = score
                    best_match = group

        if best_match is not None:
            best_match.urls.append(norm_url)
        else:
            print(f"⚠️ Нет подходящей главы для: {norm_url}, добавлено в '{groups[0].title}'")
            groups[0].urls.append(norm_url)


def get_markdown_content(url: str, session: Optional[requests.Session] = None) -> Optional[str]:
    """Напрямую скачивает и очищает .md файл по ссылке (с fallback на HTML при необходимости)."""
    http = session or create_http_session()
    md_url = normalize_md_url(url)
    html_url = get_html_url(url)

    try:
        resp = http.get(md_url, timeout=15)
        resp.raise_for_status()
        resp.encoding = "utf-8"
        content = resp.text.strip()

        # Если сервер вернул HTML-страницу вместо Markdown, используем резервный HTML-парсер
        if content.startswith("<!DOCTYPE") or "<html" in content[:500].lower():
            return get_markdown_from_html(html_url, session=http)

        cleaned = strip_gitbook_noise(content)
        return cleaned if cleaned else None
    except requests.exceptions.HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            return get_markdown_from_html(html_url, session=http)
        print(f"   ⚠️ HTTP ошибка при загрузке {md_url}: {e}")
        return get_markdown_from_html(html_url, session=http)
    except Exception as e:
        print(f"   ⚠️ Ошибка при загрузке {md_url}: {e}")
        return get_markdown_from_html(html_url, session=http)


def get_markdown_from_html(url: str, session: Optional[requests.Session] = None) -> Optional[str]:
    """Резервный парсинг HTML → Markdown (используется только если .md недоступен)."""
    http = session or create_http_session()
    html_url = get_html_url(url)
    try:
        resp = http.get(html_url, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "html.parser")
        main_tag = soup.find("main")
        if not main_tag:
            return None
        for nav in main_tag.find_all(["nav", "footer"]):
            nav.decompose()
        markdown_text = md(str(main_tag), heading_style="ATX")
        return strip_gitbook_noise(markdown_text)
    except Exception as e:
        print(f"   ❌ Ошибка резервного HTML-парсинга ({html_url}): {e}")
        return None


def assign_hierarchy_numbers(active_groups: List[PageGroup]) -> None:
    """
    Присваивает сквозную иерархическую нумерацию главам (1, 2, ...),
    подглавам (2.3, 2.4, ...) и отдельным страницам/модулям (2.1, 2.4.1, ...).
    """
    chapter_idx = 0
    sub_idx = 0

    for group in active_groups:
        if group.level == 1:
            chapter_idx += 1
            sub_idx = 0
            group.section_number = str(chapter_idx)
        else:
            if chapter_idx == 0:
                chapter_idx = 1
            sub_idx += 1
            group.section_number = f"{chapter_idx}.{sub_idx}"


def generate_toc(active_groups: List[PageGroup]) -> str:
    """
    Генерирует полное иерархическое оглавление по главам, подглавам и всем страницам API,
    чтобы ИИ и разработчики могли быстро находить нужный раздел.
    """
    toc: List[str] = ["## Оглавление\n"]

    for group in active_groups:
        if not group.pages:
            continue

        group_heading_text = f"{group.section_number}. {group.title}"
        group_anchor = make_markdown_anchor(group_heading_text)
        group_indent = "  " * (group.level - 1)
        toc.append(f"{group_indent}- [{group_heading_text}](#{group_anchor})")

        page_indent = "  " * group.level
        for page in group.pages:
            page_heading_text = f"{page.section_number}. {page.title}"
            page_anchor = make_markdown_anchor(page_heading_text)
            toc.append(f"{page_indent}- [{page_heading_text}](#{page_anchor})")

    return "\n".join(toc) + "\n\n"


def build_documentation(
    urls: List[str],
    content_fetcher=get_markdown_content,
    request_delay: float = 0.2,
) -> str:
    """
    Собирает полную документацию из списка .md ссылок с разделением на главы, подглавы и модули.
    Возвращает итоговый Markdown-текст документа.
    """
    # 1. Инициализация и распределение ссылок по главам и подглавам
    groups = [
        PageGroup(g.title, g.match_pattern, g.level)
        for g in STRUCTURE_DEFINITIONS
    ]
    distribute_urls(urls, groups)
    active_groups = [g for g in groups if g.urls]
    assign_hierarchy_numbers(active_groups)

    total = sum(len(g.urls) for g in active_groups)
    print(f"🚀 Парсинг {total} .md страниц в {len(active_groups)} главах/подглавах...")

    # 2. Скачивание и форматирование каждой страницы с учётом иерархии глав и подглав
    processed = 0
    current_chapter_title = ""
    current_chapter_num = "0"
    current_chapter_sub_counter = 0

    for group in active_groups:
        if group.level == 1:
            current_chapter_title = f"{group.section_number}. {group.title}"
            current_chapter_num = group.section_number
            current_chapter_sub_counter = 0
            breadcrumb = current_chapter_title
            page_heading_level = 3
        else:
            # group.section_number уже имеет вид "{chapter_idx}.{sub_idx}", синхронизируем счётчик
            parts = group.section_number.split(".")
            if len(parts) == 2 and parts[1].isdigit():
                current_chapter_sub_counter = int(parts[1])
            breadcrumb = f"{current_chapter_title} → {group.section_number}. {group.title}"
            page_heading_level = 4

        page_counter_in_subchapter = 0

        for url in group.urls:
            processed += 1
            print(f"[{processed}/{total}] {group.section_number}. {group.title}: {url}")
            raw_md = content_fetcher(url)

            if group.level == 1:
                current_chapter_sub_counter += 1
                page_sec_num = f"{current_chapter_num}.{current_chapter_sub_counter}"
            else:
                page_counter_in_subchapter += 1
                page_sec_num = f"{group.section_number}.{page_counter_in_subchapter}"

            if raw_md:
                page_title, formatted_md = format_page_for_chapter(
                    markdown_text=raw_md,
                    url=url,
                    section_number=page_sec_num,
                    page_heading_level=page_heading_level,
                    breadcrumb=breadcrumb,
                )
            else:
                page_title = extract_page_title("", url)
                page_hashes = "#" * page_heading_level
                formatted_md = (
                    f"{page_hashes} {page_sec_num}. {page_title}\n\n"
                    f"<!-- Source: {url} -->\n"
                    f"> ⚠️ Не удалось загрузить страницу: {url}"
                )

            group.pages.append(
                ParsedPage(
                    url=url,
                    title=page_title,
                    raw_markdown=raw_md or "",
                    formatted_markdown=formatted_md,
                    section_number=page_sec_num,
                    heading_level=page_heading_level,
                )
            )

            if request_delay > 0:
                time.sleep(request_delay)

        # Если после прямых страниц главы level=1 идут подглавы level=2, обновляем их номера,
        # чтобы нумерация внутри главы (например, 2.1, 2.2 -> 2.3, 2.4, 2.5, 2.6) шла без коллизий
        if group.level == 1 and current_chapter_sub_counter > 0:
            next_sub_idx = current_chapter_sub_counter
            for subsequent in active_groups[active_groups.index(group) + 1 :]:
                if subsequent.level == 1:
                    break
                next_sub_idx += 1
                subsequent.section_number = f"{current_chapter_num}.{next_sub_idx}"

    # 3. Сборка итогового документа с оглавлением и чёткими границами глав/подглав
    doc_parts: List[str] = [
        "# UCZONE API v2.0 - Полная документация\n\n",
        f"*Сгенерировано из {total} Markdown-страниц документации (`urls.txt`)*\n\n",
        "> **Полная документация**: [llms.txt](https://uczone.gitbook.io/api-v2.0/llms.txt)\n",
        "> Документ структурирован по главам, подглавам и модулям API для удобного чтения и быстрого поиска ИИ.\n\n",
        "---\n\n",
        generate_toc(active_groups),
        "---\n\n",
    ]

    for group in active_groups:
        if not group.pages:
            continue

        group_hashes = "#" * (group.level + 1)
        doc_parts.append(f"{group_hashes} {group.section_number}. {group.title}\n\n")

        for page in group.pages:
            doc_parts.append(page.formatted_markdown.strip() + "\n\n")

        doc_parts.append("---\n\n")

    return "".join(doc_parts).strip() + "\n"


def main() -> None:
    session = create_http_session()

    # 1. Приоритетная загрузка прямых .md ссылок из urls.txt (fallback на llms.txt)
    urls = load_urls_from_file(URLS_FILE)
    if not urls:
        print(f"⚠️ Файл {URLS_FILE} пуст или не найден, пробуем загрузить структуру из llms.txt...")
        structure = fetch_llms_structure(session=session)
        urls = [url for _, url in structure]

    if not urls:
        print("❌ Не найдено ссылок для парсинга.")
        return

    # 2. Сборка и сохранение документации
    full_markdown = build_documentation(
        urls=urls,
        content_fetcher=lambda u: get_markdown_content(u, session=session),
        request_delay=0.3,
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(full_markdown)

    print(f"✅ Готово: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
