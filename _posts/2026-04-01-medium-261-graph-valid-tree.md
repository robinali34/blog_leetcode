---
layout: post
title: "[Medium] 261. Graph Valid Tree"
date: 2026-04-01
categories: [leetcode, medium, graph, dsu, dfs]
tags: [leetcode, medium, graph, dsu, dfs, tree, cycle-detection]
permalink: /2026/04/01/medium-261-graph-valid-tree/
---
Given `n` nodes labeled `0` to `n-1` and a list of undirected `edges`, determine if these edges form a **valid tree**.

A valid tree has exactly two properties:
1. **Connected** -- all nodes are reachable from any node
2. **Acyclic** -- no cycles

## Examples

**Example 1:**

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
Explanation: Cycle exists: 1→2→3→1
```

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= edges[i][0], edges[i][1] < n`
- No duplicate edges

## Thinking Process

### Key Observation

A graph with `n` nodes is a valid tree if and only if:
1. It has exactly `n - 1` edges
2. It is connected (or equivalently, acyclic -- with exactly `n - 1` edges, one implies the other)

**Early exit**: if `edges.size() != n - 1`, immediately return false. Too few edges means disconnected; too many means a cycle exists.

After this check, we only need to verify **one** of: connected or acyclic.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Solution

Union each edge. If both endpoints already share the same root, we've found a cycle.
```cpp
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n - 1) return false;
        parent.resize(n);
        for (int i = 0; i < n; ++i) parent[i] = i;
        for (auto& e : edges) {
            int pu = find(e[0]), pv = find(e[1]);
            if (pu == pv) return false;
            parent[pu] = pv;
        }
        return true;
    }

private:
    vector<int> parent;
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** ### Key Observation

**How the code works:**
1. It has exactly `n - 1` edges
2. It is connected (or equivalently, acyclic -- with exactly `n - 1` edges, one implies the other)
**Early exit**: if `edges.size() != n - 1`, immediately return false. Too few edges means disconnected; too many means a cycle exists.

**Walkthrough** — input `n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]`, expected output `true`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Why `nei != parent` in DFS?

In an undirected graph, edge `(u, v)` appears in both adjacency lists. When DFS goes from `u` to `v`, looking back at `v`'s neighbors will see `u` again. Without the parent check, this would falsely report a cycle.

```
0 — 1 — 2

DFS: 0 → 1 → sees 0 (parent, skip) → 2 → sees 1 (parent, skip)
No cycle ✓
```

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| DSU | O(n · α(n)) | O(n) | No graph construction needed |
| DFS | O(n) | O(n) | Checks connectivity + acyclicity in one pass |

Both are optimal. DSU is more concise; DFS is more intuitive for graph problems.

## Common Mistakes

- Forgetting the `edges.size() != n - 1` early check (without it, DSU alone doesn't catch disconnected components)
- In DFS: not tracking parent, causing false cycle detection on undirected edges
- Assuming the graph is connected just because there are no cycles (need `n - 1` edges too)

## Key Takeaways

- **Valid tree = exactly `n - 1` edges + connected (or acyclic)**
- The edge count check is a powerful early exit that simplifies both DSU and DFS approaches
- DSU naturally detects cycles during union; DFS naturally checks connectivity during traversal

## Related Problems

- [323. Number of Connected Components](https://www.leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) -- DSU connectivity
- [1319. Number of Operations to Make Network Connected](https://www.leetcode.com/problems/number-of-operations-to-make-network-connected/) -- DSU + edge counting
- [207. Course Schedule](https://www.leetcode.com/problems/course-schedule/) -- cycle detection in directed graph
- [684. Redundant Connection](https://www.leetcode.com/problems/redundant-connection/) -- find the cycle-causing edge with DSU

## References

- [LC 261: Graph Valid Tree on LeetCode](https://www.leetcode.com/problems/graph-valid-tree/)
- [LeetCode Discuss — LC 261: Graph Valid Tree](https://www.leetcode.com/problems/graph-valid-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/graph-valid-tree/editorial/) *(may require premium)*

## Template Reference

- [Graph — DSU](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
