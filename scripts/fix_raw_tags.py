#!/usr/bin/env python3
"""Normalize {% raw %}/{% endraw %} — wrap only code blocks that contain Liquid syntax."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"

RAW = "{% raw %}"
ENDRAW = "{% endraw %}"
FENCE = re.compile(r"(```[^\n]*\n[\s\S]*?\n```)")


def strip_raw_tags(text: str) -> str:
    text = re.sub(r"\s*\{% raw %\}\s*\n?", "\n", text)
    text = re.sub(r"\s*\{% endraw %\}\s*\n?", "\n", text)
    return text


def needs_raw(block: str) -> bool:
    return "{{" in block or "{%" in block


def wrap_code_blocks(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        block = match.group(1)
        if needs_raw(block):
            return f"{RAW}\n{block}\n{ENDRAW}\n"
        return block + "\n"

    return FENCE.sub(repl, text)


def normalize(text: str) -> str:
    text = strip_raw_tags(text)
    text = wrap_code_blocks(text)
    # Collapse excessive blank lines introduced by stripping.
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


def fix_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = normalize(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    bad = []
    for path in sorted(POSTS.glob("*.md")):
        if fix_file(path):
            changed += 1
        text = path.read_text(encoding="utf-8")
        r, e = text.count(RAW), text.count(ENDRAW)
        if r != e:
            bad.append((path.name, r, e))
    print(f"done — {changed} file(s) updated")
    if bad:
        print("still unbalanced:")
        for name, r, e in bad:
            print(f"  {name}: raw={r} endraw={e}")


if __name__ == "__main__":
    main()
