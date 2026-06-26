#!/usr/bin/env python3
"""Add References (www), Common Approaches, Thinking Process, and rich explanations."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "_posts"

SKIP = ("template", "guide", "question-list", "cheatsheet", "categories-and")

MIN_EXPLANATION_CHARS = 220

THINKING_HINTS: dict[str, str] = {
    "binary-search": (
        "- The search space must shrink monotonically each step.\n"
        "- Decide which half still satisfies the predicate, discard the other.\n"
        "- Use `mid = left + (right - left) / 2` to avoid overflow."
    ),
    "dynamic-programming": (
        "- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?\n"
        "- Recurrence: how does the answer build from smaller indices?\n"
        "- Base cases first; optimize space if only prior row/layer is needed."
    ),
    "dfs": (
        "- DFS explores one branch fully before backtracking.\n"
        "- Mark visited nodes to avoid cycles on graphs.\n"
        "- Return aggregated results from children to the parent."
    ),
    "bfs": (
        "- BFS visits nodes in non-decreasing distance from the source.\n"
        "- Queue guarantees shortest path in unweighted graphs.\n"
        "- Process level by level when counting layers or distances."
    ),
    "graph": (
        "- Model entities as nodes and relationships as edges.\n"
        "- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.\n"
        "- Union-Find helps when connectivity updates are frequent."
    ),
    "tree": (
        "- Trees have no cycles — recursion is natural.\n"
        "- Combine results from left and right subtrees at each node.\n"
        "- Base case is usually `null`; height drives stack space."
    ),
    "linked-list": (
        "- Draw pointers before rewriting links.\n"
        "- Dummy head simplifies insert/delete at the head.\n"
        "- Slow/fast pointers find middle or detect cycles in one pass."
    ),
    "stack": (
        "- Stack matches nested or LIFO structure (parentheses, monotonic scans).\n"
        "- Push on open / larger; pop when the current element resolves pending work.\n"
        "- Monotonic stack finds next greater/smaller in O(n)."
    ),
    "heap": (
        "- Heap gives fast access to min/max without full sorting.\n"
        "- Size-k heap handles Top-K in O(n log k).\n"
        "- Lazy deletion when elements leave the heap before removal."
    ),
    "greedy": (
        "- Greedy works when local optimal choices lead to global optimum.\n"
        "- Often sort first to make the greedy choice obvious.\n"
        "- Prove or sanity-check: would swapping two choices ever help?"
    ),
    "backtracking": (
        "- Build solution incrementally; undo (backtrack) when constraints fail.\n"
        "- Prune branches early to avoid exploring invalid partial states.\n"
        "- Sort input to skip duplicate combinations efficiently."
    ),
    "two-pointers": (
        "- Two indices move toward each other or in the same direction.\n"
        "- Works on sorted arrays or when in-place modification is required.\n"
        "- Loop invariant: all indices outside `[left, right]` are already resolved."
    ),
    "sliding-window": (
        "- Maintain a window `[left, right]` satisfying a constraint.\n"
        "- Expand `right` to grow; shrink `left` when invalid.\n"
        "- Fixed window: slide both pointers together."
    ),
    "string": (
        "- Strings often need frequency maps or two-pointer scans.\n"
        "- Watch index bounds and empty-string edge cases.\n"
        "- Stack helps with nested or repeated patterns."
    ),
    "array": (
        "- Clarify if the array is sorted, has negatives, or allows duplicates.\n"
        "- Prefix sums answer range queries; hash maps answer pair/count queries.\n"
        "- In-place tricks use swap/write index instead of extra arrays."
    ),
    "matrix": (
        "- Treat the grid as a graph with 4- or 8-directional neighbors.\n"
        "- Row-major vs column-major traversal affects cache and logic.\n"
        "- Boundary checks on every neighbor expansion."
    ),
    "design": (
        "- Identify required operations and their frequency (get/put/insert).\n"
        "- Combine data structures: hash map + list, heap + map, trie + DFS.\n"
        "- Amortized O(1) often needs lazy cleanup or doubly-linked lists."
    ),
    "bit-manipulation": (
        "- XOR cancels duplicates; AND/SHIFT test or clear bits.\n"
        "- Bit masks enumerate subsets of a small set.\n"
        "- Watch signed vs unsigned when shifting."
    ),
}
THINKING_HINTS["dp"] = THINKING_HINTS["dynamic-programming"]

SLUG_PRIMARY_KEYWORDS: dict[str, str] = {
    "rotated": "rotated",
    "binary-search": "binary search",
    "subarray": "subarray",
    "substring": "substring",
    "palindrome": "palindrome",
    "linked-list": "linked",
    "tree": "tree",
    "graph": "graph",
    "interval": "interval",
    "meeting": "interval",
    "top-k": "heap",
    "k-closest": "heap",
    "unique-paths": "2d dp",
    "minimum-path": "2d dp",
    "word-search": "backtracking",
    "permutation": "backtracking",
    "combination": "backtracking",
}

TAG_APPROACHES: dict[str, str] = {
    "binary-search": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Standard binary search | O(log n) | O(1) | Sorted array, `left <= right` |
| Lower / upper bound | O(log n) | O(1) | First/last position, insert index |
| Binary search on rotated array | O(log n) | O(1) | Identify sorted half, discard other |
| Binary search on answer | O(n log M) | O(1) | Monotonic predicate over search space |
""",
    "dfs": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Recursive DFS | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |
""",
    "bfs": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Queue BFS | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| Level-order BFS | O(n) | O(w) | Process by depth/layer |
""",
    "dynamic-programming": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| 1D DP | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |
""",
    "dp": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| 1D DP | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |
""",
    "two-pointers": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Opposite ends | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |
""",
    "sliding-window": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Fixed-size window | O(n) | O(1) | Window size known upfront |
| Variable-size window | O(n) | O(1) | Expand/shrink until valid |
| Window + hash map | O(n) | O(k) | Track character/count frequencies |
| Deque window max | O(n) | O(k) | Monotonic deque for max/min in window |
""",
    "stack": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Monotonic stack | O(n) | O(n) | Next greater/smaller element |
| Parentheses matching | O(n) | O(n) | Push open, pop on close |
| Expression evaluation | O(n) | O(n) | Operand + operator stacks |
| Stack simulation | O(n) | O(n) | Process in LIFO order |
""",
    "heap": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Min/max heap | O(n log k) | O(k) | Top-K, streaming median |
| Two heaps | O(n log n) | O(n) | Median from data stream |
| Heap + lazy deletion | O(n log n) | O(n) | Delayed removal |
| Priority-driven search | O(n log n) | O(n) | Dijkstra, best-first expansion |
""",
    "greedy": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + greedy | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |
""",
    "graph": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| BFS / DFS traversal | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| Union-Find (DSU) | O(\α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |
""",
    "tree": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Recursive DFS | O(n) | O(h) | Depth, path sum, subtree queries |
| BFS level-order | O(n) | O(w) | Level traversal, zigzag |
| Inorder on BST | O(n) | O(h) | Sorted order, successor |
| Divide & conquer on tree | O(n) | O(h) | Diameter, max path |
""",
    "linked-list": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Iterative pointer walk | O(n) | O(1) | Traversal, insertion |
| Dummy head node | O(n) | O(1) | Simplify head-edge cases |
| Reversal (3-pointer) | O(n) | O(1) | Reverse sublist or full list |
| Slow/fast pointers | O(n) | O(1) | Middle, cycle, merge lists |
""",
    "backtracking": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Choose / explore / unchoose | O(2^n) | O(n) | Subsets, combinations |
| Constraint pruning | Reduced search | O(n) | Early exit on invalid partial |
| Sort + skip duplicates | O(2^n) | O(n) | Combination sum II style |
| Path recording | O(n!) worst | O(n) | Permutations |
""",
    "string": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Two pointers on string | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |
""",
    "array": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Prefix sum | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| Hash map counting | O(n) | O(n) | Frequency, two-sum variants |
""",
    "matrix": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Row/column traversal | O(nm) | O(1) | Simulation, spiral |
| BFS/DFS on grid | O(nm) | O(nm) | Islands, shortest path |
| Matrix as graph | O(nm) | O(nm) | 4/8-directional neighbors |
| Transpose / rotate | O(nm) | O(1) | In-place rotation tricks |
""",
    "design": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash map + list | O(1) avg | O(n) | LRU cache pattern |
| Heap + hash map | O(log n) | O(n) | LFU, time-based store |
| Trie (prefix tree) | O(m) | O(nm) | Word search, autocomplete |
| Deque / circular buffer | O(1) | O(n) | Queue with fixed capacity |
""",
    "bit-manipulation": """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| XOR tricks | O(n) | O(1) | Single number, swap without temp |
| Bit masks | O(2^n) | O(n) | Subset enumeration |
| Brian Kernighan | O(log n) | O(1) | Count set bits |
| Shift operations | O(n) | O(1) | Power of two, divide by 2 |
""",
}


def is_problem_post(path: Path) -> bool:
    return bool(re.search(r"\d{3,4}", path.name)) and not any(
        s in path.name for s in SKIP
    )


def parse_filename(path: Path) -> tuple[int, str] | None:
    m = re.search(
        r"(?:easy|medium|hard)-(?:lcr)?(\d+)-(.+)\.md",
        path.name,
        re.I,
    )
    if m:
        return int(m.group(1)), m.group(2)
    m = re.search(r"(?:easy|medium|hard)-(.+)\.md", path.name, re.I)
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


def extract_title(fm: str) -> str:
    m = re.search(r"title:\s*[\"']?\[?(?:Easy|Medium|Hard)\]?\s*\d+\.\s*([^\"'\n]+)", fm, re.I)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return ""


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


def pick_approaches_table(tags: list[str]) -> str:
    priority = (
        "binary-search",
        "dynamic-programming",
        "dp",
        "bfs",
        "graph",
        "dfs",
        "tree",
        "linked-list",
        "stack",
        "heap",
        "greedy",
        "backtracking",
        "sliding-window",
        "two-pointers",
        "string",
        "matrix",
        "array",
        "design",
        "bit-manipulation",
    )
    for tag in priority:
        if tag in tags and tag in TAG_APPROACHES:
            return TAG_APPROACHES[tag].strip()
    for tag in tags:
        if tag in TAG_APPROACHES:
            return TAG_APPROACHES[tag].strip()
    return DEFAULT_APPROACHES.strip()


DEFAULT_APPROACHES = """
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | Often O(n^2) or O(2^n) | O(n) | Baseline; clarifies the optimization target |
| Sort + scan | O(n log n) | O(1) | Pairs, intervals, greedy ordering |
| Hash map / set | O(n) | O(n) | Frequency, membership, two-sum style |
| Single-pass linear | O(n) | O(1) | Two pointers, sliding window, Kadane |
"""


def build_references(num: int, title: str, slug: str) -> str:
    if num:
        label = f"LC {num}: {title}" if title else f"LC {num}"
        discuss = f"LeetCode Discuss — {label}"
    else:
        label = title if title else slug.replace("-", " ")
        discuss = f"LeetCode Discuss — {label}"
    return (
        f"## References\n\n"
        f"- [{label} on LeetCode](https://www.leetcode.com/problems/{slug}/)\n"
        f"- [{discuss}](https://www.leetcode.com/problems/{slug}/discuss/)\n"
        f"- [LeetCode Editorial](https://www.leetcode.com/problems/{slug}/editorial/) *(may require premium)*\n"
    )


def normalize_old_format(body: str) -> str:
    body = re.sub(r"^#\s+\[(?:Easy|Medium|Hard)\]\s+\d+\..*n?", "", body, flags=re.M)
    body = re.sub(r"^#s+LCs+d+:.*\n?", "", body, flags=re.M | re.I)
    body = re.sub(r"^#\s+\d+\.\s+.*n?", "", body, count=1, flags=re.M)

    body = re.sub(
        r"^## Problem Descriptions*n+",
        "",
        body,
        flags=re.M,
    )
    body = re.sub(
        r"^## Solution in C\+\+s*",
        "## Solution",
        body,
        flags=re.M,
    )
    body = re.sub(
        r"^## Template in C\+\+.*?(?=^## |\Z)",
        "",
        body,
        flags=re.M | re.DOTALL,
    )
    body = re.sub(
        r"^## Algorithm Explanation\s*",
        "### Solution Explanation",
        body,
        flags=re.M,
    )
    body = re.sub(
        r"^## How the Algorithm Workss*",
        "### Solution Explanation",
        body,
        flags=re.M,
    )
    body = re.sub(
        r"^## Time Complexity\s*",
        "### Complexity",
        body,
        flags=re.M,
    )
    body = re.sub(
        r"^## Complexity Analysiss*",
        "### Complexity",
        body,
        flags=re.M,
    )
    body = re.sub(r"^### Examples\s*", "## Examples", body, flags=re.M)
    body = re.sub(r"^### Constraintss*", "## Constraints", body, flags=re.M)
    return body


def extract_thinking_summary(body: str) -> str:
    m = re.search(
        r"^## Thinking Process\s*\n+(.*?)(?=^## |\Z)",
        body,
        flags=re.M | re.DOTALL,
    )
    if not m:
        return ""
    text = m.group(1).strip()
    # First paragraph or first few bullet lines
    lines = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            if lines:
                break
            continue
        if s.startswith("#"):
            break
        lines.append(line)
        if len(lines) >= 4:
            break
    return "\n".join(lines).strip()


def has_explanation_after_solution(body: str) -> bool:
    m = re.search(r"^## Solution.*?(?=^## |\Z)", body, flags=re.M | re.DOTALL)
    if not m:
        return False
    section = m.group(0)
    after_code = re.split(r"```cpp\n.*?```", section, flags=re.DOTALL)
    tail = after_code[-1] if len(after_code) > 1 else section
    if re.search(
        r"^###\s+(\*\*)?(Solution Explanation|Algorithm|How|Complexity|Why|Walkthrough)",
        tail,
        flags=re.M | re.I,
    ):
        return True
    if re.search(r"^###\s+.*Solution\s+\d", tail, flags=re.M | re.I):
        return True
    if re.search(r"Algorithm Breakdown", tail, flags=re.I):
        return True
    return len(tail.strip()) > 200


def ensure_solution_explanation(body: str) -> str:
    if has_explanation_after_solution(body):
        return body
    m = re.search(
        r"(^## (?:Solution|Approach)[^\n]*\n)(.*?)(?=^## |\Z)",
        body,
        flags=re.M | re.DOTALL,
    )
    if not m:
        return body
    header = m.group(1)
    section = m.group(2)
    if not re.search(r"```cpp", section):
        return body
    parts = re.split(r"(```cpp\n.*?```)", section, flags=re.DOTALL)
    if len(parts) < 2:
        return body
    before = parts[0]
    code = parts[1]
    after = "".join(parts[2:]).strip()
    summary = extract_thinking_summary(body)
    expl = "### Solution Explanation\n\n"
    if summary:
        expl += summary + "\n\n"
    else:
        expl += "Walk through the solution line by line and trace one example input.\n\n"
    if after and len(after) < 120:
        expl += after + "\n"
    elif not after:
        expl += "See **Complexity** below for time and space analysis.\n"
    new_section = before + code + "\n\n" + expl.strip() + "\n"
    if after and len(after) >= 120:
        new_section += "\n" + after.strip() + "\n"
    return body[: m.start()] + header + new_section + body[m.end():]


def ensure_thinking_process(body: str) -> str:
    if re.search(r"^## Thinking Process\s*", body, flags=re.M):
        return body
    if re.search(r"^## Approachs*", body, flags=re.M):
        return re.sub(r"^## Approach\s*", "## Thinking Process", body, flags=re.M)
    if re.search(r"^## Key Ideas*", body, flags=re.M):
        return re.sub(r"^## Key Idea\s*", "## Thinking Process", body, flags=re.M)
    return body


def pick_thinking_hint(tags: list[str]) -> str:
    priority = (
        "binary-search", "dynamic-programming", "dp", "graph", "tree",
        "linked-list", "bfs", "dfs", "stack", "heap", "greedy",
        "backtracking", "sliding-window", "two-pointers", "string",
        "matrix", "array", "design", "bit-manipulation",
    )
    for tag in priority:
        if tag in tags and tag in THINKING_HINTS:
            return THINKING_HINTS[tag]
    for tag in tags:
        if tag in THINKING_HINTS:
            return THINKING_HINTS[tag]
    return (
        "- Identify the pattern from constraints (sorted? graph? optimal substructure?).n"
        "- Write brute force first mentally, then optimize the bottleneck.n"
        "- Verify edge cases: empty input, single element, duplicates."
    )


def extract_preamble(body: str) -> str:
    m = re.search(r"^## ", body, flags=re.M)
    text = body[: m.start()].strip() if m else body.strip()
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return "nn".join(lines[:2]) if lines else ""


def extract_section(body: str, header: str) -> str:
    m = re.search(
        rf"^## {re.escape(header)}s*n+(.*?)(?=^## |Z)",
        body,
        flags=re.M | re.DOTALL,
    )
    return m.group(1).strip() if m else ""


def extract_key_takeaway_bullets(body: str, max_items: int = 4) -> str:
    section = extract_section(body, "Key Takeaways")
    if not section:
        return ""
    bullets = []
    for line in section.splitlines():
        s = line.strip()
        if s.startswith(("-", "*", "1.")):
            bullets.append(s)
        if len(bullets) >= max_items:
            break
    return "n".join(bullets)


def extract_full_thinking(body: str) -> str:
    return extract_section(body, "Thinking Process")


def extract_example_trace(body: str) -> str:
    m = re.search(
        r"\*\*Example 1:\*\*(.*?)(?=\*\*Example 2:|n## )",
        body,
        flags=re.I | re.DOTALL,
    )
    if not m:
        return ""
    block = m.group(1)
    input_m = re.search(r"Input:s*(.+)", block)
    output_m = re.search(r"Output:s*(.+)", block)
    expl_m = re.search(r"Explanation:s*(.+?)(?=nn|n```|Z)", block, re.S | re.I)
    if not input_m:
        return ""
    inp = input_m.group(1).strip()
    out = output_m.group(1).strip() if output_m else ""
    trace = f"**Walkthrough** — input `{inp}`"
    if out:
        trace += f", expected output `{out}`"
    trace += ":nn"
    if expl_m:
        trace += expl_m.group(1).strip() + "n"
    else:
        trace += (
            "1. Initialize variables from the problem setup.n"
            "2. Apply the main loop / recursion until the condition is met.n"
            "3. Confirm the result matches the expected output.n"
        )
    return trace


def extract_complexity_line(body: str) -> str:
    m = re.search(r"^## Solution[^n]*\O\(([^)]+)\)[^\n]*\O\(([^)]+)\)", body, re.M)
    if m:
        return f"**Time:** O({m.group(1)}) · **Space:** O({m.group(2)})"
    m = re.search(r"\*\*Time:\*\*.*", body)
    if m:
        line = m.group(0).strip()
        if "Space" not in line:
            sm = re.search(r"\*\*Space[^\*].*", body)
            if sm:
                line += " · " + sm.group(0).strip()
        return line
    m = re.search(
        r"^### Complexitys*n+(.*?)(?=^### |^## |Z)",
        body,
        flags=re.M | re.DOTALL,
    )
    if m:
        return m.group(1).strip()
    m = re.search(
        r"\*\*Time Complexity\*\*:?s*([^n]+)",
        body,
        re.I,
    )
    if m:
        sm = re.search(r"\*\*Space Complexity\*\*:?s*([^n]+)", body, re.I)
        space = sm.group(1).strip() if sm else "see analysis"
        return f"**Time:** {m.group(1).strip()} · **Space:** {space}"
    return ""


def extract_primary_approach_name(body: str, slug: str) -> str:
    section = extract_section(body, "Common Approaches")
    if not section:
        return ""
    for line in section.splitlines():
        if "|" not in line or line.strip().startswith("|---"):
            continue
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 3:
            continue
        name = cols[1]
        if "Approach" in name or not name:
            continue
        if "this problem" in line.lower() or "**" in name:
            return re.sub(r"\*+", "", name).strip()
    slug_lower = slug.lower()
    for line in section.splitlines():
        if "|" not in line or line.strip().startswith("|---"):
            continue
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 2:
            continue
        name = cols[1]
        if "Approach" in name:
            continue
        name_lower = name.lower()
        for kw in slug_lower.split("-"):
            if len(kw) > 3 and kw in name_lower:
                return re.sub(r"\*+", "", name).strip()
    return ""


def fix_table_pipe_spacing(body: str) -> str:
    return re.sub(
        r"\|\*\*([^*|]+)\*\*s*\*\(this problem\)\*s*\|",
        r"| **\1** *(this problem)* |",
        body,
    )


def pick_primary_row_index(table: str, slug: str, tags: list[str]) -> int | None:
    lines = [ln for ln in table.splitlines() if "|" in ln and "---" not in ln]
    data_rows = []
    for i, line in enumerate(lines):
        cols = [c.strip() for c in line.split("|")]
        if len(cols) >= 3 and cols[1] and "Approach" not in cols[1]:
            data_rows.append((i, line, cols[1].lower()))
    slug_parts = slug.lower().split("-")
    keywords = [p for p in slug_parts if len(p) > 3]
    for key, hint in SLUG_PRIMARY_KEYWORDS.items():
        if key in slug.lower():
            keywords.append(hint)
    if "grid" in tags or "matrix" in tags or "unique-paths" in slug:
        keywords.append("2d")
    for i, line, name_lower in data_rows:
        for kw in keywords:
            if kw in name_lower:
                return i
    return 0 if data_rows else None


def highlight_primary_approach_row(body: str, slug: str, tags: list[str]) -> str:
    m = re.search(
        r"^(## Common Approachess*n+(?:Typical techniques for this pattern:s*n+)?)(.*?)(?=^## |Z)",
        body,
        flags=re.M | re.DOTALL,
    )
    if not m:
        return body
    prefix, table = m.group(1), m.group(2)
    if "this problem" in table.lower():
        return fix_table_pipe_spacing(body)
    lines = table.splitlines()
    data_line_indices = [
        i for i, ln in enumerate(lines)
        if "|" in ln and "---" not in ln and "Approach" not in ln
    ]
    pick = pick_primary_row_index(table, slug, tags)
    if pick is not None and pick < len(data_line_indices):
        idx = data_line_indices[pick]
        cols = lines[idx].split("|")
        if len(cols) >= 2:
            name = re.sub(r"\*+", "", cols[1]).strip()
            cols[1] = f" **{name}** *(this problem)* "
            lines[idx] = "|".join(cols)
        table = "n".join(lines)
    return body[: m.start()] + prefix + table + body[m.end():]


def explanation_score(body: str) -> int:
    m = re.search(
        r"### Solution Explanations*n+(.*?)(?=^### |^## |Z)",
        body,
        flags=re.M | re.DOTALL | re.I,
    )
    if m:
        return len(m.group(1).strip())
    m = re.search(r"^## Solution.*?(?=^## |Z)", body, flags=re.M | re.DOTALL)
    if not m:
        return 0
    parts = re.split(r"```cppn.*?```", m.group(0), flags=re.DOTALL)
    if len(parts) < 2:
        return 0
    return len(parts[-1].strip())


def build_rich_explanation(body: str, tags: list[str], slug: str) -> str:
    parts = ["### Solution Explanationnn"]
    primary = extract_primary_approach_name(body, slug)
    if primary:
        parts.append(f"**Approach:** {primary}nn")
    thinking = extract_full_thinking(body)
    if thinking:
        first = thinking.splitlines()[0].strip()
        if first:
            parts.append(f"**Key idea:** {first.lstrip('- ').lstrip('* ')}nn")
        numbered = [
            ln.strip()
            for ln in thinking.splitlines()
            if re.match(r"^(d+\.|-|\*)", ln.strip())
        ]
        if numbered:
            parts.append("**How the code works:**n")
            parts.append("n".join(numbered[:6]) + "nn")
    trace = extract_example_trace(body)
    if trace:
        parts.append(trace + "n")
    comp = extract_complexity_line(body)
    if comp:
        parts.append(comp + "n")
    return "".join(parts).strip() + "n"


def inject_rich_explanation(body: str, tags: list[str], slug: str) -> str:
    if "### Solution Explanation" in body:
        if re.search(r"###s+.*Solutions+2", body, flags=re.I):
            if explanation_score(body) >= MIN_EXPLANATION_CHARS + 80:
                return body
        if explanation_score(body) >= MIN_EXPLANATION_CHARS and "Walkthrough" in body:
            return body
    rich = build_rich_explanation(body, tags, slug)
    m = re.search(
        r"(^## (?:Solution|Approach)[^n]*n)(.*?)(?=^## |Z)",
        body,
        flags=re.M | re.DOTALL,
    )
    if not m:
        return body
    header, section = m.group(1), m.group(2)
    if not re.search(r"```cpp", section):
        return body
    parts = re.split(r"(```cppn.*?```)", section, flags=re.DOTALL)
    if len(parts) < 2:
        return body
    before, code = parts[0], parts[1]
    after = "".join(parts[2:])
    after = re.sub(
        r"### Solution Explanations*n.*?(?=^### |^## |Z)",
        "",
        after,
        flags=re.M | re.DOTALL | re.I,
    )
    after = re.sub(
        r"### Complexitys*n.*?(?=^### |^## |Z)",
        "",
        after,
        flags=re.M | re.DOTALL,
    )
    new_section = before + code + "nn" + rich
    preserved = after.strip()
    if preserved and not re.match(r"^### Solution Explanation", preserved, re.I):
        if len(preserved) > 150 or re.search(r"^## ", preserved, re.M):
            if not preserved.startswith("n"):
                new_section += "n"
            new_section += preserved + "n"
    return body[: m.start()] + header + new_section + body[m.end():]


def ensure_thinking_process_generated(body: str, tags: list[str]) -> str:
    if re.search(r"^## Thinking Processs*", body, flags=re.M):
        return body
    content = extract_full_thinking(body)
    if not content:
        content = extract_key_takeaway_bullets(body)
    if not content:
        content = extract_preamble(body)
    if not content:
        content = pick_thinking_hint(tags)
    elif not content.strip().startswith("-"):
        hint = pick_thinking_hint(tags)
        content = content + "\n\n" + hint
    section = "## Thinking Process\n\n" + content.strip()
    return insert_section_before(
        body,
        section,
        ("Common Approaches", "Solution", "Examples", "Constraints"),
    )


def ensure_key_takeaways(body: str) -> str:
    if re.search(r"^## Key Takeaways\s*", body, flags=re.M):
        return body
    thinking = extract_full_thinking(body)
    primary = ""
    m = re.search(r"\*\*Approach:\*\*s*(.+)", body)
    if m:
        primary = m.group(1).strip()
    bullets = []
    if primary:
        bullets.append(f"- **Pattern:** {primary}")
    if thinking:
        for ln in thinking.splitlines():
            s = ln.strip()
            if s.startswith(("-", "*")):
                bullets.append(s if s.startswith("-") else f"- {s.lstrip('* ')}")
            if len(bullets) >= 3:
                break
    if not bullets:
        bullets = [
            "- Reuse the template for similar problems in this pattern family.",
            "- Trace Example 1 by hand before coding.",
        ]
    section = "## Key Takeawaysnn" + "n".join(bullets[:4])
    return insert_section_before(
        body,
        section,
        ("References", "Template Reference", "Related Problems"),
    )


def ensure_common_mistakes(body: str) -> str:
    if re.search(r"^## Common Mistakess*", body, flags=re.M):
        return body
    section = (
        "## Common Mistakes\n\n"
        "- Skipping edge cases (empty input, single element, boundaries).\n"
        "- Off-by-one errors in loops and index ranges.\n"
        "- Forgetting to handle the case when no valid answer exists.\n"
    )
    return insert_section_before(
        body,
        section,
        ("Key Takeaways", "Related Problems", "References"),
    )


def deep_enrich(body: str, tags: list[str], slug: str) -> str:
    body = ensure_thinking_process_generated(body, tags)
    body = highlight_primary_approach_row(body, slug, tags)
    body = inject_rich_explanation(body, tags, slug)
    body = ensure_common_mistakes(body)
    body = ensure_key_takeaways(body)
    return body


def insert_section_before(body: str, section_md: str, before_headers: tuple[str, ...]) -> str:
    for header in before_headers:
        pat = f"^## {re.escape(header)}\\s*"
        m = re.search(pat, body, flags=re.M | re.I)
        if m:
            return body[: m.start()] + section_md + "nn" + body[m.start():]
    return body.rstrip() + "nn" + section_md + "n"


def enrich_body(body: str, num: int, title: str, slug: str, tags: list[str]) -> str:
    body = normalize_old_format(body)
    body = ensure_thinking_process(body)

    if re.search(r"^## Common Approachess*", body, flags=re.M):
        # Upgrade generic table to tag-specific when possible
        m = re.search(
            r"^## Common Approaches\s*\n+(.*?)(?=^## |\Z)",
            body,
            flags=re.M | re.DOTALL,
        )
        if m and "Brute force" in m.group(1) and "Baseline" in m.group(1):
            table = pick_approaches_table(tags)
            if "Brute force | Often" not in table:
                new_block = (
                    "## Common Approaches\n\nTypical techniques for this pattern:\n\n"
                    + table
                )
                body = body[: m.start()] + new_block + "\n\n" + body[m.end():]
    else:
        table = pick_approaches_table(tags)
        section = "## Common Approaches\n\nTypical techniques for this pattern:\n\n" + table
        body = insert_section_before(
            body,
            section,
            ("Solution", "Thinking Process", "Examples", "Constraints"),
        )

    body = ensure_solution_explanation(body)
    body = deep_enrich(body, tags, slug)

    if not re.search(r"^## References\s*$", body, flags=re.M):
        refs = build_references(num, title, slug)
        body = insert_section_before(
            body,
            refs.strip(),
            ("Template Reference", "Key Takeaways", "Related Problems"),
        )

    # Normalize leetcode.com → www.leetcode.com site-wide in post body
    body = re.sub(
        r"https://leetcode\.com/",
        "https://www.leetcode.com/",
        body,
    )
    body = fix_table_pipe_spacing(body)

    return body.strip() + "\n"


def enrich_file(path: Path, dry_run: bool = False) -> bool:
    parsed = parse_filename(path)
    if not parsed:
        return False
    num, slug = parsed
    text = path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(text)
    title = extract_title(fm)
    tags = extract_tags(fm)
    new_body = enrich_body(body, num, title, slug, tags)
    if new_body == body.strip() + "\n":
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
        if enrich_file(path, dry_run=dry_run):
            count += 1
            if dry_run:
                print(f"would update: {path.name}")
    print(f"{'Would update' if dry_run else 'Updated'} {count} posts")


if __name__ == "__main__":
    main()
