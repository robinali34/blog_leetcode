---
layout: post
title: "[Medium] 1319. Number of Operations to Make Network Connected"
date: 2026-03-10
categories: [leetcode, medium, graph, dsu]
tags: [leetcode, medium, graph, dsu, union-find, connectivity]
permalink: /2026/03/10/medium-1319-number-of-operations-to-make-network-connected/
---
There are `n` computers numbered `0` to `n-1` connected by cables. `connections[i] = [a, b]` means a cable connects computers `a` and `b`. You can remove an existing cable and place it between any pair of disconnected computers. Return the **minimum number** of such operations to make all computers connected, or `-1` if impossible.

## Examples

**Example 1:**

```
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation:
  0             0
  |\      →     |
  1-2    3     1-2-3
  Redundant cable (1,2) can connect node 3.
```

**Example 2:**

```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
```

**Example 3:**

```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: Not enough cables (need at least 5 for 6 computers).
```

## Constraints

- `1 <= n <= 10^5`
- `1 <= connections.length <= min(n*(n-1)/2, 10^5)`
- `connections[i].length == 2`
- `0 <= connections[i][0], connections[i][1] < n`
- No repeated connections, no self-loops

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **BFS / DFS traversal** *(this problem)* | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| Union-Find (DSU) | O(α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |

## Thinking Process

### Key Insight 1: Minimum Cables

To connect `n` nodes, we need at least `n - 1` edges. If `connections.size() < n - 1`, it's impossible -- return `-1`.

### Key Insight 2: Connected Components

If we have enough cables, any redundant cable (within an already-connected component) can be repositioned to bridge two disconnected components.

The answer is simply:

$text{operations} = text{components} - 1

Each operation connects one more component to the rest.

### Why DSU?

Every connection merges two computers. Start with `n` components, and each successful union reduces the count by one. After processing all connections, the remaining component count gives the answer directly.



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

## Approach: DSU -- O(n + m)$

{% raw %}
```cpp
class DSU {
public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank[px] < rank[py]) swap(px, py);
        parent[py] = px;
        rank[px] += rank[py];
        return true;
    }

private:
    vector<int> parent, rank;
};

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        if ((int)connections.size() < n - 1) return -1;

        DSU dsu(n);
        int components = n;
        for (auto& c : connections) {
            if (dsu.unite(c[0], c[1])) components--;
        }
        return components - 1;
    }
};
```

### Solution Explanation

**Approach:** BFS / DFS traversal (this problem)

**Key idea:** ### Key Insight 1: Minimum Cables

**Walkthrough** — input `n = 4, connections = [[0,1],[0,2],[1,2]]`, expected output `1`:

0             0
  |\      →     |
  1-2    3     1-2-3
  Redundant cable (1,2) can connect node 3.
## Walk-Through: n=4, connections=[[0,1],[0,2],[1,2]]

```
Start: components = 4  (each node is its own component)

unite(0,1) → success → components = 3
unite(0,2) → success → components = 2
unite(1,2) → 1 and 2 already connected → skip (redundant cable)

components - 1 = 2 - 1 = 1 ✓
```

## Common Mistakes

- Forgetting the `n - 1` edge check upfront (without enough cables, no amount of rearranging helps)
- Counting redundant edges instead of components (the answer is `components - 1`, not the number of extra cables)

## Key Takeaways

- **"Enough cables?"** check: `m >= n - 1` is necessary and sufficient (given we can reposition)
- **Components - 1** is the universal formula for "minimum operations to connect all components"
- DSU naturally tracks component count: start at `n`, decrement on each successful union

## Related Problems

- [547. Number of Provinces](https://www.leetcode.com/problems/number-of-provinces/) -- count connected components (DSU or DFS)
- [684. Redundant Connection](https://www.leetcode.com/problems/redundant-connection/) -- find the extra edge
- [1584. Min Cost to Connect All Points](https://www.leetcode.com/problems/min-cost-to-connect-all-points/) -- MST with DSU

## References

- [LC 1319: Number of Operations to Make Network Connected on LeetCode](https://www.leetcode.com/problems/number-of-operations-to-make-network-connected/)
- [LeetCode Discuss — LC 1319: Number of Operations to Make Network Connected](https://www.leetcode.com/problems/number-of-operations-to-make-network-connected/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/number-of-operations-to-make-network-connected/editorial/) *(may require premium)*

## Template Reference

- [Graph (DSU)](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
- [Data Structures (DSU)](/blog_leetcode/posts/2025-10-29-leetcode-templates-data-structures/)
