---
layout: post
title: "LeetCode 1319. Number of Operations to Make Network Connected"
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

## Thinking Process

### Key Insight 1: Minimum Cables

To connect `n` nodes, we need at least `n - 1` edges. If `connections.size() < n - 1`, it's impossible -- return `-1`.

### Key Insight 2: Connected Components

If we have enough cables, any redundant cable (within an already-connected component) can be repositioned to bridge two disconnected components.

The answer is simply:

$$\text{operations} = \text{components} - 1$$

Each operation connects one more component to the rest.

### Why DSU?

Every connection merges two computers. Start with `n` components, and each successful union reduces the count by one. After processing all connections, the remaining component count gives the answer directly.

## Approach: DSU -- $O(n + m)$

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
{% endraw %}

**Time**: $O(n + m \cdot \alpha(n))$ -- effectively $O(n + m)$ since $\alpha$ is near-constant
**Space**: $O(n)$ for DSU

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

- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) -- count connected components (DSU or DFS)
- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) -- find the extra edge
- [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) -- MST with DSU

## Template Reference

- [Graph (DSU)](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
- [Data Structures (DSU)](/blog_leetcode/posts/2025-10-29-leetcode-templates-data-structures/)
