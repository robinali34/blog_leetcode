"""Reusable inline SVG diagrams for LeetCode problem posts."""

SVG_STYLE = (
    "max-width:100%;height:auto;display:block;margin:1.5em auto;"
    "font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
)

def wrap_svg(viewbox: str, body: str, title: str = "") -> str:
    t = f"<text x=\"50%\" y=\"18\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"600\" fill=\"#5A5752\">{title}</text>" if title else ""
    return (
        f"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"{viewbox}\" style=\"{SVG_STYLE}\">\n"
        f"{t}\n{body}\n</svg>"
    )


def svg_binary_search() -> str:
    inner = """
  <rect x="40" y="40" width="48" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="64" y="58" text-anchor="middle" font-size="12" fill="#3A3530">lo</text>
  <rect x="108" y="40" width="48" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="132" y="58" text-anchor="middle" font-size="12" fill="#3A3530">mid</text>
  <rect x="196" y="40" width="48" height="32" rx="4" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="220" y="58" text-anchor="middle" font-size="12" fill="#3A3530">hi</text>
  <rect x="60" y="90" width="160" height="28" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="140" y="108" text-anchor="middle" font-size="11" fill="#6B6560">discard half each step → O(log n)</text>
  <path d="M132 72v12M220 72v12" stroke="#9A9792" stroke-width="1.5" marker-end="url(#a)"/>
"""
    return wrap_svg("0 0 280 130", inner, "Binary search: shrink [lo … hi]")


def svg_rotated_array() -> str:
    inner = """
  <text x="20" y="35" font-size="11" fill="#6B6560">sorted half</text>
  <rect x="20" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="38" y="60" text-anchor="middle" font-size="11">4</text>
  <rect x="46" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="64" y="60" text-anchor="middle" font-size="11">5</text>
  <rect x="82" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="60" text-anchor="middle" font-size="11">6</text>
  <rect x="118" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="136" y="60" text-anchor="middle" font-size="11">7</text>
  <text x="160" y="35" font-size="11" fill="#A08888">pivot</text>
  <rect x="154" y="42" width="36" height="28" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/><text x="172" y="60" text-anchor="middle" font-size="11">0</text>
  <rect x="190" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="208" y="60" text-anchor="middle" font-size="11">1</text>
  <rect x="226" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="244" y="60" text-anchor="middle" font-size="11">2</text>
  <text x="140" y="95" text-anchor="middle" font-size="11" fill="#5A5752">One half is always sorted → BS on that half</text>
"""
    return wrap_svg("0 0 280 110", inner, "Rotated sorted array")


def svg_tree_dfs() -> str:
    inner = """
  <line x1="140" y1="42" x2="80" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="140" y1="42" x2="200" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="80" y1="88" x2="50" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="200" y1="88" x2="230" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <circle cx="140" cy="42" r="18" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="140" y="46" text-anchor="middle" font-size="12" fill="#3D3535">3</text>
  <circle cx="80" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="80" y="92" text-anchor="middle" font-size="11" fill="#3D3535">9</text>
  <circle cx="200" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="200" y="92" text-anchor="middle" font-size="11" fill="#3D3535">20</text>
  <circle cx="50" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="50" y="132" text-anchor="middle" font-size="10" fill="#3D3535">15</text>
  <circle cx="230" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="230" y="132" text-anchor="middle" font-size="10" fill="#3D3535">7</text>
  <text x="140" y="155" text-anchor="middle" font-size="11" fill="#6B6560">post-order: combine left + right + 1</text>
"""
    return wrap_svg("0 0 280 165", inner, "Tree DFS (bottom-up)")


def svg_bst_catalan() -> str:
    inner = """
  <text x="70" y="38" text-anchor="middle" font-size="11" fill="#6B6560">root = 2</text>
  <circle cx="70" cy="55" r="14" fill="#E0D8E4" stroke="#8E9AAF" stroke-width="2"/>
  <text x="70" y="59" text-anchor="middle" font-size="11">2</text>
  <circle cx="40" cy="95" r="12" fill="#D4D8E0" stroke="#8B8680"/><text x="40" y="99" text-anchor="middle" font-size="10">1</text>
  <circle cx="100" cy="95" r="12" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="99" text-anchor="middle" font-size="10">3</text>
  <line x1="70" y1="69" x2="40" y2="83" stroke="#8E9AAF" stroke-width="1.5"/>
  <line x1="70" y1="69" x2="100" y2="83" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="25" y="115" font-size="9" fill="#7A8EA0">C(1)</text>
  <text x="95" y="115" font-size="9" fill="#7A8EA0">C(1)</text>
  <text x="200" y="70" font-size="11" fill="#5A5752">C(n) = Σ C(j-1)·C(n-j)</text>
  <text x="200" y="88" font-size="10" fill="#9A9792">pick root j, multiply subtrees</text>
"""
    return wrap_svg("0 0 320 125", inner, "BST count: split at root")


def svg_linked_list() -> str:
    inner = """
  <rect x="30" y="50" width="44" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="52" y="68" text-anchor="middle" font-size="12">1</text>
  <path d="M74 66h16" stroke="#8B8680" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="90" y="50" width="44" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="112" y="68" text-anchor="middle" font-size="12">2</text>
  <path d="M134 66h16" stroke="#8B8680" stroke-width="2"/>
  <rect x="150" y="50" width="44" height="32" rx="4" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="172" y="68" text-anchor="middle" font-size="12">3</text>
  <text x="130" y="105" text-anchor="middle" font-size="11" fill="#6B6560">slow → → fast (2x speed)</text>
  <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>
"""
    return wrap_svg("0 0 260 115", inner, "Linked list: pointer walk")


def svg_graph_bfs() -> str:
    inner = """
  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>
"""
    return wrap_svg("0 0 280 135", inner, "Graph BFS layers")


def svg_sliding_window() -> str:
    inner = """
  <rect x="20" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="36" y="63" text-anchor="middle" font-size="11">a</text>
  <rect x="52" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="68" y="63" text-anchor="middle" font-size="11">b</text>
  <rect x="84" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="63" text-anchor="middle" font-size="11">c</text>
  <rect x="116" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="132" y="63" text-anchor="middle" font-size="11">d</text>
  <rect x="148" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="164" y="63" text-anchor="middle" font-size="11">e</text>
  <rect x="52" y="38" width="64" height="42" rx="4" fill="none" stroke="#C4956A" stroke-width="2" stroke-dasharray="4"/>
  <text x="84" y="32" text-anchor="middle" font-size="10" fill="#C4956A" font-weight="600">window</text>
  <text x="110" y="105" text-anchor="middle" font-size="11" fill="#6B6560">expand right, shrink left when invalid</text>
"""
    return wrap_svg("0 0 220 115", inner, "Sliding window")


def svg_two_pointers() -> str:
    inner = """
  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>
"""
    return wrap_svg("0 0 230 110", inner, "Two pointers")


def svg_stack() -> str:
    inner = """
  <rect x="100" y="30" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="46" text-anchor="middle" font-size="10">top</text>
  <rect x="100" y="54" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="100" y="78" width="80" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="200" y="70" font-size="11" fill="#6B6560">push / pop</text>
  <path d="M90 42v60" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="115" text-anchor="middle" font-size="11" fill="#6B6560">LIFO — monotonic stack scans array</text>
"""
    return wrap_svg("0 0 280 125", inner, "Stack")


def svg_heap() -> str:
    inner = """
  <circle cx="140" cy="35" r="16" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="39" text-anchor="middle" font-size="11">1</text>
  <circle cx="90" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="90" y="79" text-anchor="middle" font-size="10">3</text>
  <circle cx="190" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="190" y="79" text-anchor="middle" font-size="10">2</text>
  <line x1="140" y1="51" x2="90" y2="61" stroke="#9A9792"/><line x1="140" y1="51" x2="190" y2="61" stroke="#9A9792"/>
  <text x="140" y="110" text-anchor="middle" font-size="11" fill="#6B6560">parent ≤ children (min-heap)</text>
"""
    return wrap_svg("0 0 280 120", inner, "Binary heap")


def svg_dp_table() -> str:
    inner = """
  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>
"""
    return wrap_svg("0 0 220 105", inner, "1D DP recurrence")


def svg_dp_grid() -> str:
    inner = """
  <rect x="40" y="40" width="32" height="28" rx="2" fill="#D4D8E0" stroke="#8B8680"/><text x="56" y="56" text-anchor="middle" font-size="10">1</text>
  <rect x="72" y="40" width="32" height="28" rx="2" fill="#E8E3D8" stroke="#B8B5B0"/><text x="88" y="56" text-anchor="middle" font-size="10">1</text>
  <rect x="104" y="40" width="32" height="28" rx="2" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="56" text-anchor="middle" font-size="10">1</text>
  <rect x="40" y="68" width="32" height="28" rx="2" fill="#E8E3D8" stroke="#B8B5B0"/><text x="56" y="84" text-anchor="middle" font-size="10">1</text>
  <rect x="72" y="68" width="32" height="28" rx="2" fill="#E0D8E4" stroke="#A098A8"/><text x="88" y="84" text-anchor="middle" font-size="10">2</text>
  <rect x="104" y="68" width="32" height="28" rx="2" fill="#E8D5D0" stroke="#B8A5A0"/><text x="120" y="84" text-anchor="middle" font-size="10">3</text>
  <text x="140" y="65" font-size="10" fill="#C4956A">← + ↑</text>
  <text x="90" y="115" text-anchor="middle" font-size="11" fill="#6B6560">cell from top + left neighbors</text>
"""
    return wrap_svg("0 0 200 125", inner, "2D DP on grid")


def svg_intervals() -> str:
    inner = """
  <line x1="30" y1="60" x2="250" y2="60" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="50" y="48" width="60" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="100" y="48" width="50" height="24" rx="3" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="160" y="48" width="70" height="24" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="95" text-anchor="middle" font-size="11" fill="#6B6560">sort by start → scan overlaps</text>
"""
    return wrap_svg("0 0 280 105", inner, "Intervals on timeline")


def svg_backtracking() -> str:
    inner = """
  <circle cx="140" cy="30" r="12" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="34" text-anchor="middle" font-size="9">start</text>
  <line x1="140" y1="42" x2="90" y2="65" stroke="#9A9792"/><line x1="140" y1="42" x2="190" y2="65" stroke="#9A9792"/>
  <circle cx="90" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/><circle cx="190" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/>
  <line x1="90" y1="82" x2="60" y2="100" stroke="#9A9792" stroke-dasharray="3"/><line x1="190" y1="82" x2="220" y2="100" stroke="#9A9792" stroke-dasharray="3"/>
  <text x="140" y="118" text-anchor="middle" font-size="11" fill="#6B6560">choose → explore → undo (prune)</text>
"""
    return wrap_svg("0 0 280 125", inner, "Backtracking tree")


def svg_matrix_grid() -> str:
    inner = """
  <rect x="50" y="40" width="28" height="28" fill="#D4D8E0" stroke="#8B8680"/><rect x="78" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="106" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="50" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="78" y="68" width="28" height="28" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="106" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="110" y="115" text-anchor="middle" font-size="11" fill="#6B6560">BFS/DFS flood from each cell</text>
"""
    return wrap_svg("0 0 220 125", inner, "Grid traversal")


def svg_greedy() -> str:
    inner = """
  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>
"""
    return wrap_svg("0 0 280 100", inner, "Greedy choice")


def svg_design() -> str:
    inner = """
  <rect x="40" y="45" width="70" height="36" rx="4" fill="#D4D8E0" stroke="#8B8680"/><text x="75" y="67" text-anchor="middle" font-size="10">API</text>
  <rect x="150" y="45" width="90" height="36" rx="4" fill="#E0D8E4" stroke="#A098A8"/><text x="195" y="67" text-anchor="middle" font-size="10">hash + list</text>
  <path d="M110 63h36" stroke="#8B8680" stroke-width="2" marker-end="url(#arr2)"/>
  <defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>
  <text x="140" y="105" text-anchor="middle" font-size="11" fill="#6B6560">compose data structures for operations</text>
"""
    return wrap_svg("0 0 280 115", inner, "Design pattern")


def svg_bit() -> str:
    inner = """
  <text x="40" y="50" font-family="monospace" font-size="14" fill="#3A3530">1 0 1 1 0 1 0</text>
  <text x="40" y="75" font-size="11" fill="#6B6560">XOR pairs · masks · shifts</text>
"""
    return wrap_svg("0 0 220 90", inner, "Bit manipulation")


def svg_array_hash() -> str:
    inner = """
  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>
"""
    return wrap_svg("0 0 230 110", inner, "Array + hash map")


PATTERN_SVG: dict[str, callable] = {
    "binary-search": svg_binary_search,
    "tree": svg_tree_dfs,
    "bst": svg_bst_catalan,
    "linked-list": svg_linked_list,
    "graph": svg_graph_bfs,
    "bfs": svg_graph_bfs,
    "dfs": svg_tree_dfs,
    "stack": svg_stack,
    "heap": svg_heap,
    "sliding-window": svg_sliding_window,
    "two-pointers": svg_two_pointers,
    "dynamic-programming": svg_dp_table,
    "dp": svg_dp_table,
    "backtracking": svg_backtracking,
    "greedy": svg_greedy,
    "matrix": svg_matrix_grid,
    "array": svg_array_hash,
    "string": svg_two_pointers,
    "design": svg_design,
    "bit-manipulation": svg_bit,
    "intervals": svg_intervals,
    "sorting": svg_intervals,
}

PROBLEM_SVG: dict[int, callable] = {
    33: svg_rotated_array,
    81: svg_rotated_array,
    96: svg_bst_catalan,
    104: svg_tree_dfs,
    111: svg_tree_dfs,
    200: svg_matrix_grid,
    206: svg_linked_list,
    876: svg_linked_list,
    3: svg_sliding_window,
    56: svg_intervals,
    253: svg_intervals,
    62: svg_dp_grid,
    64: svg_dp_grid,
    70: svg_dp_table,
    198: svg_dp_table,
    739: svg_stack,
    84: svg_stack,
}


def pick_svg(problem_num: int, tags: list[str], slug: str) -> str | None:
    if problem_num in PROBLEM_SVG:
        return PROBLEM_SVG[problem_num]()
    priority = (
        "binary-search", "sliding-window", "two-pointers", "linked-list",
        "graph", "bfs", "tree", "bst", "dfs", "stack", "heap",
        "dynamic-programming", "dp", "backtracking", "greedy",
        "matrix", "intervals", "design", "bit-manipulation", "array", "string",
    )
    slug_lower = slug.lower()
    if "rotated" in slug_lower or "search-in-rotated" in slug_lower:
        return svg_rotated_array()
    if "interval" in slug_lower or "meeting" in slug_lower:
        return svg_intervals()
    if "unique-path" in slug_lower or "minimum-path" in slug_lower:
        return svg_dp_grid()
    if "island" in slug_lower or "matrix" in slug_lower and "spiral" not in slug_lower:
        return svg_matrix_grid()
    for tag in priority:
        if tag in tags and tag in PATTERN_SVG:
            return PATTERN_SVG[tag]()
    for tag in tags:
        if tag in PATTERN_SVG:
            return PATTERN_SVG[tag]()
    return svg_array_hash()
