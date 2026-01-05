import re
import requests
import time
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass, field

OUTPUT_FILE = "DocumentationUCZONE.md"
URLS_FILE = "urls.txt"

def strip_gitbook_noise(markdown_text: str) -> str:
    """Чистка мусора, который GitBook/markdownify иногда добавляют в MD."""
    if not markdown_text:
        return markdown_text

    lines = markdown_text.splitlines()
    out: List[str] = []

    noise_patterns = [
        re.compile(r"^\s*copy\s*$", re.IGNORECASE),
        re.compile(r"^\s*{%\s*hint\s+style=\"info\"\s*%}\s*$"),
        re.compile(r"^\s*{%\s*endhint\s*%}\s*$"),
    ]

    for line in lines:
        s = line.strip()
        if s and any(p.search(s) for p in noise_patterns):
            continue
        out.append(line)

    cleaned = "\n".join(out)
    cleaned = cleaned.replace('{% hint style="info" %}', "")
    cleaned = cleaned.replace("{% endhint %}", "")
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()

@dataclass
class PageGroup:
    """Группа страниц с общей темой"""
    title: str
    match_pattern: str  # Подстрока URL, определяющая принадлежность к группе
    level: int  # Уровень вложенности (1 = основной раздел, 2 = подраздел)
    urls: List[str] = field(default_factory=list)

# Определение структуры документации
# Порядок в списке определяет порядок в итоговом файле.
# URL будет добавлен в группу с самым длинным совпадающим match_pattern.
STRUCTURE_DEFINITIONS = [
    PageGroup("Starting Guide", "api-v2.0", 1), # Fallback for root
    
    # Cheats Types
    PageGroup("Cheats Types and Callbacks", "cheats-types-and-callbacks", 1),
    PageGroup("Classes - Color", "cheats-types-and-callbacks/classes/color", 2),
    PageGroup("Classes - Menu System", "cheats-types-and-callbacks/classes/menu", 2),
    PageGroup("Classes - UI Widgets", "cheats-types-and-callbacks/classes/widgets", 2),
    PageGroup("Classes - Math", "cheats-types-and-callbacks/classes/math", 2),
    
    # Game Components
    PageGroup("Game Components - Entity Lists", "game-components/lists", 1),
    PageGroup("Game Components - Core Objects", "game-components/core", 1),
    PageGroup("Game Engine", "game-components/game-engine", 1),
    PageGroup("Networking and APIs", "game-components/networking-and-apis", 1),
    
    # Rendering
    PageGroup("Rendering and Visuals", "game-components/rendering-and-visuals", 1),
    PageGroup("Rendering - Panorama UI", "game-components/rendering-and-visuals/panorama", 2),
    
    # Config
    PageGroup("Configuration and Utilities", "game-components/configuration-and-utilities", 1),
]

def load_urls_from_file(filepath: str) -> List[str]:
    """Загружает список URL из файла."""
    path = Path(filepath)
    if not path.exists():
        print(f"⚠️ Файл {filepath} не найден!")
        return []
    
    with open(path, "r", encoding="utf-8") as f:
        # Фильтруем пустые строки и комментарии
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def distribute_urls(urls: List[str], groups: List[PageGroup]):
    """Распределяет URL по группам на основе match_pattern."""
    # Сортируем группы по длине паттерна (от длинных к коротким) для точного сопоставления
    # Но сохраняем исходный порядок для итогового вывода
    
    for url in urls:
        best_match_group = None
        max_len = -1
        
        for group in groups:
            if group.match_pattern in url:
                if len(group.match_pattern) > max_len:
                    max_len = len(group.match_pattern)
                    best_match_group = group
        
        if best_match_group:
            best_match_group.urls.append(url)
        else:
            # Если не найдено совпадений, добавляем в первую группу (Starting Guide) или создаем Misc
            print(f"⚠️ Не найдена группа для URL: {url}")
            groups[0].urls.append(url)

def get_markdown_from_html(url: str) -> Optional[str]:
    """Fallback-метод: парсит HTML и конвертирует в Markdown."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        main_content = soup.find('main')
        if not main_content:
            return None

        for element in main_content.find_all(['nav', 'footer']):
            element.decompose()
        for link in main_content.find_all('a', class_=lambda x: x and 'pagination' in str(x)):
            link.decompose()

        markdown_text = md(str(main_content), heading_style="ATX")
        return strip_gitbook_noise(markdown_text)
    except Exception as e:
        print(f"   ❌ Fallback ошибка: {e}")
        return None

def get_markdown_content(url: str) -> Optional[str]:
    """Получает чистый Markdown напрямую из GitBook."""
    try:
        markdown_url = url if url.endswith('.md') else f"{url}.md"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        
        response = requests.get(markdown_url, headers=headers, timeout=15)
        response.raise_for_status()
        content = response.text.strip()

        if content.startswith('<!DOCTYPE') or content.startswith('<html'):
            print(f"   🔄 .md вернул HTML, используем fallback...")
            return get_markdown_from_html(url)

        return strip_gitbook_noise(content)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"   🔄 .md недоступен (404), используем fallback...")
            return get_markdown_from_html(url)
        return None
    except Exception as e:
        print(f"   ⚠️  Ошибка: {e}")
        return get_markdown_from_html(url)

def generate_toc(groups: List[PageGroup]) -> str:
    """Генерирует оглавление."""
    toc_lines = ["# Оглавление\n"]
    for group in groups:
        if not group.urls: continue
        indent = "  " * (group.level - 1)
        anchor = group.title.lower().replace(" ", "-").replace("_", "-")
        toc_lines.append(f"{indent}- [{group.title}](#{anchor})")
    return "\n".join(toc_lines) + "\n\n"

def main():
    # 1. Загрузка URL
    urls = load_urls_from_file(URLS_FILE)
    if not urls:
        print("❌ Нет URL для обработки.")
        return

    # 2. Распределение по группам
    # Создаем копии групп, чтобы очистить старые данные если они были
    active_groups = [g for g in STRUCTURE_DEFINITIONS] 
    for g in active_groups: g.urls = []
    
    distribute_urls(urls, active_groups)
    
    # Фильтруем пустые группы
    active_groups = [g for g in active_groups if g.urls]

    total_pages = sum(len(group.urls) for group in active_groups)
    print(f"🚀 Начинаем парсинг {total_pages} страниц в {len(active_groups)} групп...")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# UCZONE API v2.0 - Полная документация\n\n")
        f.write(f"*Сгенерировано из {total_pages} страниц GitBook*\n\n")
        f.write("---\n\n")
        f.write(generate_toc(active_groups))
        f.write("\n" + "=" * 80 + "\n\n")

        processed = 0
        success_count = 0

        for group_idx, group in enumerate(active_groups, 1):
            heading_level = "#" * (group.level + 1)
            f.write(f"{heading_level} {group.title}\n\n")

            for url_idx, url in enumerate(group.urls, 1):
                processed += 1
                print(f"[{processed}/{total_pages}] {group.title} ({url_idx}/{len(group.urls)}): {url}")
                
                content = get_markdown_content(url)
                
                if content:
                    f.write(f"<!-- Source: {url} -->\n\n")
                    f.write(content)
                    f.write("\n\n")
                    success_count += 1
                    print(f"   ✅ Успешно ({len(content)} символов)")
                else:
                    f.write(f"> ⚠️ Не удалось загрузить: {url}\n\n")
                    print(f"   ❌ Ошибка загрузки")

                time.sleep(0.3)

            if group_idx < len(active_groups):
                f.write("\n" + "-" * 80 + "\n\n")

    print(f"\n✅ Готово! Файл сохранён: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()