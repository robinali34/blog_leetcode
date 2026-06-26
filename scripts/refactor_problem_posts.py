#!/usr/bin/env python3
"""Normalize LeetCode problem posts to the readable template format."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"

SKIP_SUBSTRINGS = (
    "template",
    "guide",
    "question-list",
    "cheatsheet",
    "categories-and",
)

SECTIONS_DROP_PREFIXES = (
    "clarification questions",
    "interview deduction",
    "alternative approaches",
    "comparison of approaches",
    "when to use each approach",
)

SECTIONS_DROP_IF_ALTERNATIVES_REMOVED = ("comparison",)

TAG_TO_TEMPLATE = {
    "tree": "/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/",
    "bst": "/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/",
    "dfs": "/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/",
    "bfs": "/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/",
    "linked-list": "/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/",
    "stack": "/blog_leetcode/posts/2025-11-13-leetcode-templates-stack/",
    "heap": "/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/",
    "greedy": "/blog_leetcode/posts/2025-12-14-leetcode-templates-greedy/",
    "backtracking": "/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/",
    "graph": "/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/",
    "dp": "/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/",
    "binary-search": "/blog_leetcode/posts/2026-01-20-leetcode-templates-search/",
    "search": "/blog_leetcode/posts/2026-01-20-leetcode-templates-search/",
    "two-pointers": "/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/",
    "sliding-window": "/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/",
    "array": "/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/",
    "matrix": "/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/",
    "string": "/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/",
    "design": "/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/",
    "bit-manipulation": "/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/",
    "math": "/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/",
    "queue": "/blog_leetcode/posts/2025-11-24-leetcode-templates-queue/",
}

TEMPLATE_LABELS = {
    "tree": "Trees",
    "bst": "Trees",
    "dfs": "DFS",
    "bfs": "BFS",
    "linked-list": "Linked List",
    "stack": "Stack",
    "heap": "Heap",
    "greedy": "Greedy",
    "backtracking": "Backtracking",
    "graph": "Graph",
    "dp": "Dynamic Programming",
    "binary-search": "Search",
    "search": "Search",
    "two-pointers": "Arrays & Strings",
    "sliding-window": "Arrays & Strings",
    "array": "Array & Matrix",
    "matrix": "Array & Matrix",
    "string": "String Processing",
    "design": "Data Structure Design",
    "bit-manipulation": "Math & Bit Manipulation",
    "math": "Math & Bit Manipulation",
    "queue": "Queue",
}


def is_problem_post(path: Path) -> bool:
    if not re.search(r"\d{3,4}", path.name):
        return False
    return not any(s in path.name for s in SKIP_SUBSTRINGS)


def parse_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("---", 3)
    if end == -1:
        return "", text
    return text[: end + 3], text[end + 3:]


def split_sections(body: str) -> list[tuple[str | None, str]]:
    parts = re.split(r"^(## .+)$", body.strip(), flags=re.MULTILINE)
    if not parts:
        return [(None, body)]
    sections = [(None, parts[0])]
    i = 1
    while i < len(parts):
        header = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append((header, content))
        i += 2
    return sections


def header_key(header: str) -> str:
    key = re.sub(r"^##\s+", "", header).strip().lower()
    key = re.sub(r"\s*\([^)]*\)\s*$", "", key).strip()
    return key


def should_drop_section(key: str) -> bool:
    return any(key == p or key.startswith(p) for p in SECTIONS_DROP_PREFIXES)


def is_solution_header(key: str) -> bool:
    if key in ("solution", "c++ solution"):
        return True
    if key.startswith("approach:"):
        return True
    if key.startswith("solution:"):
        return True
    if re.match(r"^solution\s+\d", key):
        return True
    return False


def has_solution_section(sections: list[tuple[str | None, str]]) -> bool:
    return any(h and is_solution_header(header_key(h)) for h, _ in sections)


def extract_cpp_blocks(text: str) -> list[str]:
    return re.findall(r"```cpp\n.*?```", text, flags=re.DOTALL)


def clean_preamble(text: str) -> str:
    lines = text.strip().splitlines()
    out = []
    skip_problem_statement_body = False
    for line in lines:
        if re.match(r"^#\s+\d+\.", line) or re.match(r"^#\s+LC\s+\d+", line, re.I):
            continue
        if re.match(r"^## Problem Statement\s*$", line):
            skip_problem_statement_body = True
            continue
        if skip_problem_statement_body and line.startswith("## "):
            skip_problem_statement_body = False
        if skip_problem_statement_body:
            out.append(line)
            continue
        out.append(line)
    text = "\n".join(out).strip()
    text = re.sub(
        r"\n---\s*\n\*This problem demonstrates.*?\*\s*$",
        "",
        text,
        flags=re.DOTALL,
    )
    return text


def trim_solution_content(content: str) -> str:
    code_blocks = extract_cpp_blocks(content)
    sub_drop = {
        "example walkthrough",
        "walk-through",
        "walkthrough",
        "step-by-step",
    }
    parts = re.split(r"^(### .+)$", content, flags=re.MULTILINE)
    if len(parts) <= 1:
        return content.strip()
    kept = [parts[0]]
    i = 1
    while i < len(parts):
        sub_h = parts[i].strip()
        sub_c = parts[i + 1] if i + 1 < len(parts) else ""
        sub_key = re.sub(r"^###\s+", "", sub_h).strip().lower()
        sub_key = sub_key.rstrip(":")
        if sub_key not in sub_drop:
            kept.append(sub_h)
            kept.append(sub_c)
        i += 2
    result = "".join(kept).strip()
    if code_blocks and not extract_cpp_blocks(result):
        result = (result + "\n\n" + code_blocks[0]).strip()
    return result


def merge_key_sections(
    sections: list[tuple[str | None, str]],
) -> list[tuple[str | None, str]]:
    out: list[tuple[str | None, str]] = []
    insights = ""
    has_thinking = any(h and header_key(h) == "thinking process" for h, _ in sections)
    has_solution = has_solution_section(sections)

    for header, content in sections:
        if header is None:
            out.append((header, content))
            continue
        key = header_key(header)
        if key == "key insights":
            insights = content.strip()
            continue
        if key == "approach" and not has_thinking:
            out.append(("## Thinking Process", content))
            has_thinking = True
            continue
        if key == "solution approach":
            if not has_solution and not has_thinking:
                out.append(("## Thinking Process", content))
                has_thinking = True
            continue
        if key == "edge cases":
            for i, (h, c) in enumerate(out):
                if h and header_key(h) == "common mistakes":
                    merged = (c.strip() + "\n\n" + content.strip()).strip()
                    out[i] = (h, "\n" + merged + "\n")
                    break
            else:
                out.append((header, content))
            continue
        out.append((header, content))

    if insights:
        for i, (h, c) in enumerate(out):
            if h and header_key(h) == "key takeaways":
                merged = (insights + "\n\n" + c.strip()).strip()
                out[i] = (h, "\n" + merged + "\n")
                break
        else:
            out.append(("## Key Takeaways", "\n" + insights + "\n"))
    return out


def infer_template_from_front_matter(fm: str) -> tuple[str, str] | None:
    tags_match = re.search(r"tags:\s*\[([^\]]+)\]", fm)
    cats_match = re.search(r"categories:\s*\[([^\]]+)\]", fm)
    candidates = []
    if tags_match:
        candidates.extend(re.findall(r"[\w-]+", tags_match.group(1)))
    if cats_match:
        candidates.extend(re.findall(r"[\w-]+", cats_match.group(1)))
    for c in candidates:
        if c in TAG_TO_TEMPLATE:
            return TEMPLATE_LABELS[c], TAG_TO_TEMPLATE[c]
    return None


def add_template_reference(
    sections: list[tuple[str | None, str]], fm: str
) -> list[tuple[str | None, str]]:
    if any(h and header_key(h) == "template reference" for h, _ in sections):
        return sections
    tpl = infer_template_from_front_matter(fm)
    if not tpl:
        return sections
    label, url = tpl
    sections.append(
        (
            "## Template Reference",
            f"\n- [{label}]({url})\n",
        )
    )
    return sections


def refactor_body(body: str, fm: str) -> tuple[str, bool]:
    original = body.strip()
    body = clean_preamble(body)
    sections = split_sections(body)
    if not sections:
        return body, False

    removed_alternatives = False
    solution_kept = False
    thinking_from_approach = ""
    new_sections: list[tuple[str | None, str]] = []

    for header, content in sections:
        if header is None:
            new_sections.append((header, content))
            continue
        key = header_key(header)
        if key == "solution approach":
            thinking_from_approach = content.strip()
            continue
        if should_drop_section(key):
            if key.startswith("alternative approaches"):
                removed_alternatives = True
            continue
        if removed_alternatives and any(
            key == p or key.startswith(p) for p in SECTIONS_DROP_IF_ALTERNATIVES_REMOVED
        ):
            continue
        if is_solution_header(key):
            if solution_kept:
                continue
            content = trim_solution_content(content)
            if key == "c++ solution" or not key.startswith("approach:"):
                header = "## Solution"
            solution_kept = True
        new_sections.append((header, content))

    new_sections = merge_key_sections(new_sections)

    # Merge Edge Cases into Common Mistakes when both exist
    edge_i = None
    mistakes_i = None
    for i, (h, _) in enumerate(new_sections):
        if h and header_key(h) == "edge cases":
            edge_i = i
        if h and header_key(h) == "common mistakes":
            mistakes_i = i
    if edge_i is not None and mistakes_i is not None and edge_i < mistakes_i:
        _, edge_c = new_sections[edge_i]
        h, mistakes_c = new_sections[mistakes_i]
        new_sections[mistakes_i] = (
            h,
            "\n" + edge_c.strip() + "\n\n" + mistakes_c.strip() + "\n",
        )
        new_sections.pop(edge_i)

    if thinking_from_approach:
        insight = thinking_from_approach
        if "### key insights" in thinking_from_approach.lower():
            m = re.search(
                r"###\s*Key Insights:?\s*(.*)",
                thinking_from_approach,
                flags=re.I | re.DOTALL,
            )
            if m:
                insight = m.group(1).strip()
        for i, (h, c) in enumerate(new_sections):
            if h and header_key(h) == "thinking process":
                merged = (c.strip() + "\n\n" + insight).strip()
                new_sections[i] = (h, "\n" + merged + "\n")
                break
        else:
            new_sections.insert(
                1,
                ("## Thinking Process", "\n" + insight + "\n"),
            )

    filtered: list[tuple[str | None, str]] = []
    for header, content in new_sections:
        if header and header_key(header) == "complexity" and solution_kept:
            continue
        filtered.append((header, content))

    new_sections = add_template_reference(filtered, fm)

    parts = []
    for header, content in new_sections:
        if header is None:
            parts.append(content.strip())
        else:
            parts.append(header)
            parts.append(content.strip())
    result = "\n\n".join(p for p in parts if p).strip() + "\n"

    # Safety: never ship a post that lost all solution code
    if extract_cpp_blocks(original) and not extract_cpp_blocks(result):
        return original + "\n", False

    changed = result != original + "\n"
    return result, changed


def refactor_file(path: Path, dry_run: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(text)
    new_body, changed = refactor_body(body, fm)
    if not changed:
        return False
    new_text = (fm + "\n" if fm else "") + new_body
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def main():
    dry_run = "--dry-run" in sys.argv
    count = 0
    for path in sorted(POSTS.glob("*.md")):
        if not is_problem_post(path):
            continue
        if refactor_file(path, dry_run=dry_run):
            count += 1
            if dry_run:
                print(f"would update: {path.name}")
    print(f"{'Would update' if dry_run else 'Updated'} {count} posts")


if __name__ == "__main__":
    main()
