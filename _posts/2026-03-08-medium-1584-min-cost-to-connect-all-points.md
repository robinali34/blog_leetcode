---
layout: post
title: "[Medium] 1584. Min Cost to Connect All Points"
date: 2026-03-08
categories: [leetcode, medium, graph, mst, dsu]
tags: [leetcode, medium, graph, mst, kruskal, dsu]
permalink: /2026/03/08/medium-1584-min-cost-to-connect-all-points/
---

You are given an array `points` where `points[i] = [xi, yi]` represents a point on the 2D plane. The cost to connect two points is the **Manhattan distance**: `|xi - xj| + |yi - yj|`. Return the minimum cost to connect all points such that every pair of points has a path between them.

## Examples

**Example 1:**

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
```

**Example 2:**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## Constraints

- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`
- All pairs `(xi, yi)` are distinct

## Thinking Process

This is a **Minimum Spanning Tree (MST)** problem on a complete graph. Each point is a node, and the edge weight between any two points is their Manhattan distance.

### Kruskal's Algorithm

1. Generate all $\binom{n}{2}$ edges with their Manhattan distance weights
2. Sort edges by weight (ascending)
3. Greedily add edges using **DSU (Union-Find)** -- skip edges that would create a cycle
4. Stop after adding $n - 1$ edges (MST is complete)

### Why Kruskal?

For a complete graph with $n$ nodes, there are $O(n^2)$ edges. Kruskal's sorts them and processes greedily, giving $O(n^2 \log n)$ total. Prim's with a heap is also $O(n^2 \log n)$ here, but Kruskal + DSU is cleaner for complete graphs.

## Approach: Kruskal's MST + DSU -- $O(n^2 \log n)$

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
        if (x != parent[x]) parent[x] = find(parent[x]);
        return parent[x];
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
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<pair<int, pair<int, int>>> allEdges;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int weight = abs(points[i][0] - points[j][0]) +
                             abs(points[i][1] - points[j][1]);
                allEdges.push_back({weight, {i, j}});
            }
        }

        sort(allEdges.begin(), allEdges.end());

        DSU dsu(n);
        int mstCost = 0, edgesUsed = 0;

        for (int i = 0; i < (int)allEdges.size() && edgesUsed < n - 1; i++) {
            auto [node1, node2] = allEdges[i].second;
            int weight = allEdges[i].first;
            if (dsu.unite(node1, node2)) {
                mstCost += weight;
                edgesUsed++;
            }
        }

        return mstCost;
    }
};
```
{% endraw %}

**Time**: $O(n^2 \log n)$ -- $O(n^2)$ edges, sorting dominates
**Space**: $O(n^2)$ for the edge list

## Walk-Through

```
Points: [0,0], [2,2], [3,10], [5,2], [7,0]

Edges sorted by weight (first few):
  (0,1) w=4, (1,3) w=3, (0,3) w=7, (0,4) w=7, (3,4) w=4, ...

Process:
  (1,3) w=3  → unite 1,3  → cost=3,  edges=1
  (0,1) w=4  → unite 0,1  → cost=7,  edges=2
  (3,4) w=4  → unite 3,4  → cost=11, edges=3
  (0,2) w=13 → unite 0,2  → cost=20, edges=4 = n-1 → done!

MST cost = 20 ✓
```

## DSU (Union-Find) Recap

- **Path compression** (`find`): flattens the tree so future finds are nearly $O(1)$
- **Union by rank**: always attach the smaller tree under the larger root
- Combined: amortized $O(\alpha(n))$ per operation (practically constant)

## Common Mistakes

- Forgetting to stop after $n - 1$ edges (MST of $n$ nodes always has exactly $n - 1$ edges)
- Generating duplicate edges (only iterate `j = i + 1` to `n`, not all pairs)
- Using edge weight for rank in DSU (rank tracks tree height/size, not edge weight)

## Key Takeaways

- **Complete graph MST** = generate all edges + Kruskal's. Simple and effective for $n \leq 1000$
- **DSU** is the natural companion to Kruskal's -- it answers "are these connected?" in near-constant time
- For larger $n$, Prim's with adjacency list or geometric optimizations (e.g., only considering nearest neighbors) would be needed

## Related Problems

- [1135. Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) -- Kruskal on given edges
- [1168. Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) -- MST with virtual node
- [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) -- DSU for connectivity check

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
- [Data Structures (DSU)](/blog_leetcode/posts/2025-10-29-leetcode-templates-data-structures/)
