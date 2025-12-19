import requests
import time
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass

OUTPUT_FILE = "DocumentationUCZONE.md"

@dataclass
class PageGroup:
    """Группа страниц с общей темой"""
    title: str
    urls: List[str]
    level: int  # Уровень вложенности (1 = основной раздел, 2 = подраздел)

# Умная иерархическая структура разделов
PAGE_GROUPS = [
    PageGroup("Starting Guide", [
        "https://uczone.gitbook.io/api-v2.0"
    ], level=1),
    
    PageGroup("Cheats Types and Callbacks", [
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/callbacks",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums"
    ], level=1),
    
    PageGroup("Classes - Color", [
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color"
    ], level=2),
    
    PageGroup("Classes - Menu System", [
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup"
    ], level=2),
    
    PageGroup("Classes - UI Widgets", [
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuswitch",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderfloat",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenusliderint",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubutton",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpicker",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucolorpickerattachment",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenucombobox",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenugearattachment",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenuinputbox",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumulticombobox",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenumultiselect",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind"
    ], level=2),
    
    PageGroup("Classes - Math", [
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2",
        "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex"
    ], level=2),
    
    PageGroup("Game Components - Entity Lists", [
        "https://uczone.gitbook.io/api-v2.0/game-components/lists",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/abilities",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/couriers",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/customentities",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/entities",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/heroes",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/npcs",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/camps",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/players",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/runes",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/temptrees",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/towers",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/trees",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/physicalitems",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/modifiers",
        "https://uczone.gitbook.io/api-v2.0/game-components/lists/linearprojectiles"
    ], level=1),
    
    PageGroup("Game Components - Core Objects", [
        "https://uczone.gitbook.io/api-v2.0/game-components/core",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/player",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/modifier",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/entity",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/npc",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/hero",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/ability",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/item",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/rune",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/tower",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/tree",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/vambrace",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/camp",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/bottle",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/courier",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/drunkenbrawler",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/physicalitem",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/powertreads",
        "https://uczone.gitbook.io/api-v2.0/game-components/core/tiertoken"
    ], level=1),
    
    PageGroup("Game Engine", [
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/engine",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gamerules",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/globalvars",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gridnav",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/input",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/world",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/fogofwar",
        "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar"
    ], level=1),
    
    PageGroup("Networking and APIs", [
        "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis",
        "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/chatapi",
        "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/http",
        "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/steamapi",
        "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/netchannel",
        "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/gc"
    ], level=1),
    
    PageGroup("Rendering and Visuals", [
        "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals",
        "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/particle",
        "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv1",
        "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv2",
        "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/minimap"
    ], level=1),
    
    PageGroup("Rendering - Panorama UI", [
        "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama",
        "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/panorama",
        "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel"
    ], level=2),
    
    PageGroup("Configuration and Utilities", [
        "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities",
        "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/config",
        "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/humanizer",
        "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/log",
        "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/localizer",
        "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/gamelocalizer"
    ], level=1)
]


def get_clean_content(url: str) -> Optional[str]:
    """Извлекает чистый Markdown-контент из GitBook страницы"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Основной контент в <main>
        main_content = soup.find('main')
        if not main_content:
            return None

        # Удаляем навигацию и мусор
        for element in main_content.find_all(['nav', 'footer']):
            element.decompose()
        for link in main_content.find_all('a', class_=lambda x: x and 'pagination' in str(x)):
            link.decompose()
        
        # Конвертация в Markdown
        markdown_text = md(str(main_content), heading_style="ATX")
        return markdown_text.strip()

    except Exception as e:
        print(f"❌ Ошибка при обработке {url}: {e}")
        return None


def generate_toc(groups: List[PageGroup]) -> str:
    """Генерирует оглавление"""
    toc_lines = ["# Оглавление\n"]
    
    for group in groups:
        indent = "  " * (group.level - 1)
        anchor = group.title.lower().replace(" ", "-").replace("_", "-")
        toc_lines.append(f"{indent}- [{group.title}](#{anchor})")
    
    return "\n".join(toc_lines) + "\n\n"


def main():
    total_pages = sum(len(group.urls) for group in PAGE_GROUPS)
    print(f"🚀 Начинаем парсинг {total_pages} страниц в {len(PAGE_GROUPS)} групп...")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # Заголовок документа
        f.write("# UCZONE API v2.0 - Полная документация\n\n")
        f.write(f"*Сгенерировано из {total_pages} страниц GitBook*\n\n")
        f.write("---\n\n")
        
        # Оглавление
        f.write(generate_toc(PAGE_GROUPS))
        f.write("\n" + "="*80 + "\n\n")
        
        # Обрабатываем группы
        processed = 0
        for group_idx, group in enumerate(PAGE_GROUPS, 1):
            # Заголовок группы
            heading_level = "#" * (group.level + 1)
            f.write(f"{heading_level} {group.title}\n\n")
            
            # Обрабатываем страницы в группе
            for url_idx, url in enumerate(group.urls, 1):
                processed += 1
                print(f"[{processed}/{total_pages}] Группа '{group.title}' ({url_idx}/{len(group.urls)}): {url}")
                
                content = get_clean_content(url)
                
                if content:
                    # Добавляем якорь источника
                    f.write(f"<!-- Source: {url} -->\n\n")
                    f.write(content)
                    f.write("\n\n")
                else:
                    f.write(f"> ⚠️ Не удалось загрузить: {url}\n\n")
                
                time.sleep(0.3)  # Защита от блокировки
            
            # Разделитель между группами
            if group_idx < len(PAGE_GROUPS):
                f.write("\n" + "-"*80 + "\n\n")

    print(f"\n✅ Готово! Файл сохранён: {OUTPUT_FILE}")
    print(f"📊 Обработано групп: {len(PAGE_GROUPS)}")
    print(f"📄 Обработано страниц: {total_pages}")


if __name__ == "__main__":
    main()
