#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Патчер для DocumentationUCZONE.md.

Задача:
- Очень аккуратно добавить навигационный блок (docs/_doc_header.md) в начало большого файла
- Ничего не удалять

По умолчанию НЕ перезаписывает исходник: пишет результат в DocumentationUCZONE.enhanced.md.

Использование:
  python tools/patch_documentation.py

При необходимости можно включить inplace=True в main().
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "DocumentationUCZONE.md"
HEADER = ROOT / "docs" / "_doc_header.md"
OUT = ROOT / "DocumentationUCZONE.enhanced.md"


def insert_after_first_h1(text: str, block: str) -> str:
    """Вставляет block после первой строки заголовка уровня # ...\n
    Если # не найден, вставляет в самое начало.
    """
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "".join(lines[: i + 1]) + "\n" + block.strip() + "\n\n" + "".join(lines[i + 1 :])
    return block.strip() + "\n\n" + text


def main(inplace: bool = False) -> None:
    if not DOC.exists():
        raise SystemExit(f"Не найден файл: {DOC}")
    if not HEADER.exists():
        raise SystemExit(f"Не найден файл: {HEADER}")

    original = DOC.read_text(encoding="utf-8", errors="replace")
    header_block = HEADER.read_text(encoding="utf-8", errors="replace")

    # Защита от повторной вставки
    marker = "## 📌 Как пользоваться этим файлом"
    if marker in original:
        raise SystemExit("Похоже, навигационный блок уже вставлен (маркер найден).")

    patched = insert_after_first_h1(original, header_block)

    if inplace:
        DOC.write_text(patched, encoding="utf-8")
        print(f"OK: обновлён {DOC.name}")
    else:
        OUT.write_text(patched, encoding="utf-8")
        print(f"OK: записан {OUT.name} (исходник не тронут)")


if __name__ == "__main__":
    main(inplace=False)
