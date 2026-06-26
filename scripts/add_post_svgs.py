#!/usr/bin/env python3
"""Insert pattern SVG diagrams into problem posts."""

import re
import sys
from pathlib import Path

from post_svg_library import pick_svg

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"

SKIP = ("template", "guide", "question-list", "cheatsheet", "categories-and")


def is_problem_post(path: Path) -> bool:
    return bool(re.search(r"\d{3,4}", path.name)) and not any(
        s in path.name for s in SKIP
    )


def parse_filename(path: Path) -> tuple[int, str] | None:
    m = re.search(r"(?:easy|medium|hard)-(?:lcr)?(\d+)-(.+)\.md$", path.name, re.I)
    if m:
        return int(m.group(1)), m.group(2)
    m = re.search(r"(?:easy|medium|hard)-(.+)\.md$", path.name, re.I)
    if m:
        return 0, m.group(1)
    return None


def parse_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("---", 3)
    if end == -1:
        return "", text
    return text[: end + 3], text[end + 3:]


def extract_tags(fm: str) -> list[str]:
    tags: list[str] = []
    m = re.search(r"tags:\s*\[([^\]]+)\]", fm)
    if m:
        tags.extend(re.findall(r"[\w-]+", m.group(1)))
    m = re.search(r"categories:\s*\[([^\]]+)\]", fm)
    if m:
        tags.extend(re.findall(r"[\w-]+", m.group(1)))
    elif re.search(r"^categories:\s*([^\n]+)", fm, re.M):
        cats = re.search(r"^categories:\s*([^\n]+)", fm, re.M).group(1)
        tags.extend(re.findall(r"[\w-]+", cats))
    return tags


def insert_svg_after_section(body: str, svg: str, headers: tuple[str, ...]) -> str:
    for header in headers:
        m = re.search(
            rf"^## {re.escape(header)}\s*\n+(.*?)(?=^## |\Z)",
            body,
            flags=re.MULTILINE | re.DOTALL,
        )
        if m:
            pos = m.end()
            return body[:pos] + "\n\n" + svg + "\n\n" + body[pos:]
    m = re.search(r"^## Solution", body, flags=re.M)
    if m:
        return body[: m.start()] + svg + "\n\n" + body[m.start():]
    return body.rstrip() + "\n\n" + svg + "\n"


def add_svg_to_body(body: str, problem_num: int, tags: list[str], slug: str) -> str:
    if "<svg" in body.lower():
        return body
    svg = pick_svg(problem_num, tags, slug)
    if not svg:
        return body
    return insert_svg_after_section(
        body,
        svg,
        ("Thinking Process", "Common Approaches", "Examples", "Constraints"),
    )


def process_file(path: Path, dry_run: bool = False) -> bool:
    parsed = parse_filename(path)
    if not parsed:
        return False
    num, slug = parsed
    text = path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(text)
    tags = extract_tags(fm)
    new_body = add_svg_to_body(body, num, tags, slug)
    if new_body.strip() == body.strip():
        return False
    new_text = (fm + "\n" if fm else "") + new_body.strip() + "\n"
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def main():
    dry_run = "--dry-run" in sys.argv
    count = 0
    for path in sorted(POSTS.glob("*.md")):
        if not is_problem_post(path):
            continue
        if process_file(path, dry_run=dry_run):
            count += 1
            if dry_run:
                print(f"would add svg: {path.name}")
    print(f"{'Would update' if dry_run else 'Updated'} {count} posts with SVG")


if __name__ == "__main__":
    main()
