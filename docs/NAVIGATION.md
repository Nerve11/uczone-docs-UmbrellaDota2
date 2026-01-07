# Навигация по документации UCZONE

Этот репозиторий содержит собранную (склеенную) документацию **UCZONE API v2.0** для написания Lua 5.4 скриптов под Umbrella Dota 2. 

- Главный файл документации: [DocumentationUCZONE.md](../DocumentationUCZONE.md)
- Исходный GitBook (оригинальная структура): https://uczone.gitbook.io/api-v2.0

## Быстрые ссылки (внутри DocumentationUCZONE.md)

| Раздел | Что внутри | Ссылка |
|---|---|---|
| Starting Guide | Запуск скрипта, коллбэки, примеры | [→ Starting Guide](../DocumentationUCZONE.md#starting-guide) |
| Callbacks | Все события, сигнатуры, примеры | [→ Callbacks](../DocumentationUCZONE.md#callbacks) |
| Enums | Таблицы перечислений | [→ Enums](../DocumentationUCZONE.md#enums) |
| Rendering | Отрисовка, Panorama UI | [→ Rendering and Visuals](../DocumentationUCZONE.md#rendering-and-visuals) |
| Game Components | Entity/NPC/Ability и списки | [→ Game Components - Core Objects](../DocumentationUCZONE.md#game-components---core-objects) |

## Соглашения в тексте

- Типы в документе часто подсвечены HTML-тегами из GitBook (например, `<mark style="color:purple;">`). Это нормально: GitHub отобразит как HTML. 
- Обозначение **`[?]`** рядом с полем/параметром означает, что оно опционально (может быть `nil`).
- Если рядом указано `(default: nil)` — значение по умолчанию `nil`.

## Как быстро находить нужное

- Используйте поиск по странице (Ctrl+F) по имени функции/типа: `OnUpdate`, `Entity.GetIndex`, `Enum.ModifierState`.
- Для больших таблиц Enums рекомендуется искать по ключу перечисления: `MODIFIER_STATE_STUNNED`, `DOTA_UNIT_ORDER_ATTACK_TARGET`.
