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

## Solution 1: DSU (Union-Find) -- $O(n \cdot \alpha(n))$

Union each edge. If both endpoints already share the same root, we've found a cycle.

{% raw %}
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
{% endraw %}

**Time**: $O(n \cdot \alpha(n)) \approx O(n)$ -- nearly linear with path compression
**Space**: $O(n)$

## Solution 2: DFS (Cycle Detection) -- $O(n)$

Build an adjacency list and DFS from node 0. Track the parent to avoid false cycle detection on the edge we came from. If we revisit a node via a different path, it's a cycle. After DFS, check all nodes were visited (connected).

{% raw %}
```cpp
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n - 1) return false;
        vector<vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        vector<bool> visited(n, false);
        if (!dfs(0, -1, graph, visited)) return false;
        for (bool v : visited) {
            if (!v) return false;
        }
        return true;
    }

private:
    bool dfs(int node, int parent, vector<vector<int>>& graph, vector<bool>& visited) {
        visited[node] = true;
        for (int nei : graph[node]) {
            if (!visited[nei]) {
                if (!dfs(nei, node, graph, visited)) return false;
            } else if (nei != parent) {
                return false;
            }
        }
        return true;
    }
};
```
{% endraw %}

**Time**: $O(n)$ -- visit each node and edge once
**Space**: $O(n)$ -- adjacency list + recursion stack

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
| DSU | $O(n \cdot \alpha(n))$ | $O(n)$ | No graph construction needed |
| DFS | $O(n)$ | $O(n)$ | Checks connectivity + acyclicity in one pass |

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

- [323. Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) -- DSU connectivity
- [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) -- DSU + edge counting
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) -- cycle detection in directed graph
- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) -- find the cycle-causing edge with DSU

## Template Reference

- [Graph — DSU](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
