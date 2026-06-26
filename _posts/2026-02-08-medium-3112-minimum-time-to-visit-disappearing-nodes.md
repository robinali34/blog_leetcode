---
layout: post
title: "[Medium] 3112. Minimum Time to Visit Disappearing Nodes"
date: 2026-02-08 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dijkstra]
permalink: /2026/02/08/medium-3112-minimum-time-to-visit-disappearing-nodes/
tags: [leetcode, medium, graph, shortest-path, dijkstra]
---
There exists an undirected tree with `n` nodes numbered `0` to `n-1`. You are given a 2D integer array `edges` of length `n-1`, where `edges[i] = [ui, vi, lengthi]` indicates that there is an undirected edge between nodes `ui` and `vi` with a traversal time of `lengthi` seconds.

You are also given a 0-indexed array `disappear`, where `disappear[i]` is the time when node `i` disappears.

Return an array `answer` of length `n`, where `answer[i]` is the **minimum time** in seconds it takes to reach node `i` from node `0` before it disappears. If it's impossible to reach node `i` before it disappears, return `-1`.

## Examples

**Example 1:**

```
Input: n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]
Output: [0,-1,4]
Explanation:
- Node 0: We start at node 0 at time 0, so answer[0] = 0.
- Node 1: We can reach node 1 at time 2, but disappear[1] = 1, so we cannot reach it in time. answer[1] = -1.
- Node 2: We can reach node 2 via path 0 -> 1 -> 2 at time 3, or directly via 0 -> 2 at time 4. Since disappear[2] = 5, we can reach it. The minimum time is 4, so answer[2] = 4.
```

**Example 2:**

```
Input: n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]
Output: [0,2,3]
Explanation:
- Node 0: We start at node 0 at time 0, so answer[0] = 0.
- Node 1: We can reach node 1 at time 2, and disappear[1] = 3, so we can reach it. answer[1] = 2.
- Node 2: We can reach node 2 via path 0 -> 1 -> 2 at time 3, and disappear[2] = 5, so we can reach it. answer[2] = 3.
```

**Example 3:**

```
Input: n = 2, edges = [[0,1,1]], disappear = [1,1]
Output: [0,-1]
Explanation:
- Node 0: We start at node 0 at time 0, so answer[0] = 0.
- Node 1: We can reach node 1 at time 1, but disappear[1] = 1, so we cannot reach it in time (must arrive strictly before disappear time). answer[1] = -1.
```

## Constraints

- `2 <= n <= 5 * 10^4`
- `edges.length == n - 1`
- `edges[i].length == 3`
- `0 <= ui < vi < n`
- `1 <= lengthi <= 10^5`
- `disappear.length == n`
- `1 <= disappear[i] <= 10^5`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **BFS / DFS traversal** *(this problem)* | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| Union-Find (DSU) | O(α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |

## Thinking Process

This is a shortest path problem with time constraints. We need to find the minimum time to reach each node from node 0, but nodes disappear at specific times.

### Key Insights:

1. **Dijkstra's Algorithm**: Perfect choice since all edge weights are positive
2. **Disappear Constraint**: Check `dist[u] + weight < disappear[v]` when relaxing edges
3. **Early Termination**: If we pop a node with `dist[u] >= disappear[u]`, skip processing its neighbors
4. **Return Format**: Use `-1` to indicate unreachable nodes or nodes that disappear before we can reach them

### Algorithm:

1. Build adjacency list from edges (undirected graph)
2. Initialize `dist[0] = 0`, all others as `-1` (or `INF`)
3. Use priority queue to process nodes in order of minimum distance
4. For each popped node `u`:
   - If `dist[u] >= disappear[u]`, skip (cannot visit)
   - For each neighbor `v`:
     - Calculate `newDist = dist[u] + weight`
     - If `newDist < disappear[v]` and `newDist < dist[v]` (or `dist[v] == -1`), update and push

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

## Solution Code

### Solution 1: Using long long with LLONG_MAX

```cpp
class Solution {
public:
    vector<int> minimumTime(int n, vector<vector<int>>& edges, vector<int>& disappear) {
        if(disappear[0] == 0) return vector<int>(n, -1);

        vector<vector<pair<int, int>>> adjs(n);
        for(auto e: edges) {
            int u = e[0], v = e[1], d = e[2];
            adjs[u].emplace_back(v, d);
            adjs[v].emplace_back(u, d);
        }
        
        vector<long long> dist(n, LLONG_MAX);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
        dist[0] = 0;
        pq.emplace({0, 0});
        while(!pq.empty()) {
            auto [t, u] = pq.top(); pq.pop();
            if(t > dist[u]) continue;
            if(t >= disappear[u]) continue;
            for(auto& [v, w]: adjs[u]) {
                long long nt = t + w;
                if(dist[v] > nt && nt < disappear[v]) {
                    dist[v] = nt;
                    pq.emplace({dist[v], v});
                }
            }
        }

        vector<int> rtn(n, -1);
        for(int i = 0; i < n; i++) {
            if(dist[i] != LLONG_MAX) rtn[i] = dist[i];
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** BFS / DFS traversal (this problem)

**Key idea:** This is a shortest path problem with time constraints. We need to find the minimum time to reach each node from node 0, but nodes disappear at specific times.

**How the code works:**
1. **Dijkstra's Algorithm**: Perfect choice since all edge weights are positive
2. **Disappear Constraint**: Check `dist[u] + weight < disappear[v]` when relaxing edges
3. **Early Termination**: If we pop a node with `dist[u] >= disappear[u]`, skip processing its neighbors
4. **Return Format**: Use `-1` to indicate unreachable nodes or nodes that disappear before we can reach them
1. Build adjacency list from edges (undirected graph)
2. Initialize `dist[0] = 0`, all others as `-1` (or `INF`)

**Walkthrough** — input `n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]`, expected output `[0,-1,4]`:

- Node 0: We start at node 0 at time 0, so answer[0] = 0.
- Node 1: We can reach node 1 at time 2, but disappear[1] = 1, so we cannot reach it in time. answer[1] = -1.
- Node 2: We can reach node 2 via path 0 -> 1 -> 2 at time 3, or directly via 0 -> 2 at time 4. Since disappear[2] = 5, we can reach it. The minimum time is 4, so answer[2] = 4.

**Time Complexity:** O((V + E) log V)
- Building adjacency list: O(E)
- Dijkstra's algorithm: O((V + E) log V) with priority queue
- Total: O((V + E) log V)

**Space Complexity:** O(V + E)
- Adjacency list: O(E)
- Distance array: O(V)
- Priority queue: O(V)
- Total: O(V + E)

**Key Points:**
- Uses `long long` to handle large distances
- Checks `t >= disappear[u]` after popping to skip nodes that already disappeared
- Checks `nt < disappear[v]` when relaxing edges
- Converts `LLONG_MAX` to `-1` in final result

### Solution 2: Using int with -1 (Cleaner)

```cpp
class Solution {
public:
    vector<int> minimumTime(int n, vector<vector<int>>& edges, vector<int>& disappear) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto& e: edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].emplace_back(v, w);
            adj[v].emplace_back(u, w);
        }
        vector<int> dis(n, -1);
        dis[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.emplace(0, 0);
        while(!pq.empty()) {
            auto [du, u] = pq.top();
            pq.pop();
            if(dis[u] != -1 && du > dis[u]) continue;
            for(auto& [v, w]: adj[u]) {
                int nd = du + w;
                if(nd < disappear[v] && (dis[v] == -1 || nd < dis[v])) {
                    dis[v] = nd;
                    pq.emplace(nd, v);
                }
            }
        }
        return dis;
    }
};
```

**Key Points:**
- Uses `int` since constraints guarantee values fit in int
- Uses `-1` directly to represent unreachable nodes
- Checks `nd < disappear[v]` when relaxing edges
- Simpler and more readable
## Edge Cases

1. **Node 0 disappears immediately**: If `disappear[0] == 0`, return all `-1`
2. **Node disappears exactly when we arrive**: If `arrival_time == disappear[i]`, return `-1` (must arrive strictly before)
3. **Unreachable nodes**: Nodes with no path from node 0 return `-1`
4. **Large edge weights**: Edge weights can be up to 10^5, but total path length is bounded by disappear times

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [743. Network Delay Time](https://www.leetcode.com/problems/network-delay-time/) - Standard Dijkstra
- [787. Cheapest Flights Within K Stops](https://www.leetcode.com/problems/cheapest-flights-within-k-stops/) - Shortest path with edge count constraint
- [1514. Path with Maximum Probability](https://www.leetcode.com/problems/path-with-maximum-probability/) - Shortest path variant
- [1631. Path With Minimum Effort](https://www.leetcode.com/problems/path-with-minimum-effort/) - Shortest path with different optimization

## Key Takeaways

- If `dist[u] >= disappear[u]`, skip (cannot visit)
- For each neighbor `v`:
- Calculate `newDist = dist[u] + weight`

## References

- [LC 3112: Minimum Time to Visit Disappearing Nodes on LeetCode](https://www.leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/)
- [LeetCode Discuss — LC 3112: Minimum Time to Visit Disappearing Nodes](https://www.leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/editorial/) *(may require premium)*

## Template Reference

See [Graph Templates: Dijkstra](/posts/2025-10-29-leetcode-templates-graph/#dijkstra) for the standard Dijkstra template and variant with node disappearance constraints.
