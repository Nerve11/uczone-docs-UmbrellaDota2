import requests
import time
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Имя итогового файла
OUTPUT_FILE = "DocumentationUCZONE.md"

# Полный список ссылок (порядок важен — так они будут идти в файле)
URLS = [
    "https://uczone.gitbook.io/api-v2.0",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/callbacks",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/enums",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/color",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/ctabsection",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cfirsttab",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/csecondtab",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cthirdtab",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/menu/cmenugroup",
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
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/widgets/cmenubind",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vector",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/angle",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vec2",
    "https://uczone.gitbook.io/api-v2.0/cheats-types-and-callbacks/classes/math/vertex",
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
    "https://uczone.gitbook.io/api-v2.0/game-components/lists/linearprojectiles",
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
    "https://uczone.gitbook.io/api-v2.0/game-components/core/tiertoken",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/engine",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/event",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gamerules",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/globalvars",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/gridnav",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/input",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/world",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/fogofwar",
    "https://uczone.gitbook.io/api-v2.0/game-components/game-engine/convar",
    "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis",
    "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/chatapi",
    "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/http",
    "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/steamapi",
    "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/netchannel",
    "https://uczone.gitbook.io/api-v2.0/game-components/networking-and-apis/gc",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/particle",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv1",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv1#setdrawcolor",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/renderv2",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/minimap",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/panorama",
    "https://uczone.gitbook.io/api-v2.0/game-components/rendering-and-visuals/panorama/uipanel",
    "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities",
    "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/config",
    "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/humanizer",
    "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/log",
    "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/localizer",
    "https://uczone.gitbook.io/api-v2.0/game-components/configuration-and-utilities/gamelocalizer"
]

def get_clean_content(url):
    """Скачивает страницу и возвращает Markdown контент только из основной части."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # В GitBook контент лежит в <main>
        main_content = soup.find('main')
        if not main_content:
            return None

        # Удаляем навигацию внизу (Previous / Next), чтобы не засорять файл
        for nav in main_content.find_all('a', class_=lambda x: x and 'pagination' in x):
            nav.decompose()
        
        # Конвертация в MD
        text = md(str(main_content), heading_style="ATX")
        return text.strip()

    except Exception as e:
        print(f"Ошибка при обработке {url}: {e}")
        return None

def main():
    print(f"Начинаем сборку {len(URLS)} страниц в один файл '{OUTPUT_FILE}'...")
    
    # Открываем файл на запись (перезаписываем, если был)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # Добавляем главный заголовок
        f.write("# UCZONE API v2.0 Documentation\n\n")
        f.write(f"Generated from {len(URLS)} pages.\n\n")

        for i, url in enumerate(URLS):
            print(f"[{i+1}/{len(URLS)}] Обработка: {url}")
            
            content = get_clean_content(url)
            
            if content:
                # Разделитель между страницами
                f.write("\n\n" + "="*80 + "\n")
                f.write(f"Original URL: {url}\n")
                f.write("="*80 + "\n\n")
                
                # Записываем контент
                f.write(content)
                
                # Дополнительный отступ после главы
                f.write("\n\n")
            else:
                f.write(f"\n\n> Failed to fetch content for: {url}\n\n")

            # Небольшая задержка, чтобы сервер не заблокировал
            time.sleep(0.2)

    print(f"\nГотово! Всё сохранено в файл: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()