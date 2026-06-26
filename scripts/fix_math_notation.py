#!/usr/bin/env python3
"""Replace $...$ inline math with plain-text complexity notation for Jekyll/kramdown."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LATEX_REPLACEMENTS = [
    ("\\log", "log"),
    ("\\leq", "≤"),
    ("\\geq", "≥"),
    ("\\times", "×"),
    ("\\cdot", "·"),
    ("\\infty", "∞"),
    ("\\alpha", "α"),
    ("\\beta", "β"),
    ("\\sum", "sum"),
    ("\\min", "min"),
    ("\\max", "max"),
]

INLINE_MATH = re.compile(r"\$([^$]+)\$")


def normalize_inline_math(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        for latex, plain in LATEX_REPLACEMENTS:
            inner = inner.replace(latex, plain)
        inner = re.sub(r"\\([a-zA-Z]+)", r"\1", inner)
        return inner

    return INLINE_MATH.sub(repl, text)


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = normalize_inline_math(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    targets = [
        ROOT / "_posts",
        ROOT / "_templates",
        ROOT / "scripts" / "enrich_problem_posts.py",
    ]
    changed = 0
    for target in targets:
        if target.is_file():
            if process_file(target):
                changed += 1
                print(f"updated {target.relative_to(ROOT)}")
            continue
        for path in sorted(target.rglob("*.md")):
            if process_file(path):
                changed += 1
                print(f"updated {path.relative_to(ROOT)}")
    print(f"done — {changed} file(s) changed")


if __name__ == "__main__":
    main()
