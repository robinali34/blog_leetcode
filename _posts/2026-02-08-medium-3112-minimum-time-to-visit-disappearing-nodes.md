---
layout: post
title: "3112. Minimum Time to Visit Disappearing Nodes"
date: 2026-02-08 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dijkstra]
permalink: /2026/02/08/medium-3112-minimum-time-to-visit-disappearing-nodes/
tags: [leetcode, medium, graph, shortest-path, dijkstra]
---

# 3112. Minimum Time to Visit Disappearing Nodes

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Disappear time interpretation**: What does "disappear" mean? (Assumption: A node can only be visited if we arrive **strictly before** its disappear time. If we arrive at time `t` and `disappear[i] = t`, we cannot visit it)

2. **Starting node**: Can node 0 disappear immediately? (Assumption: If `disappear[0] == 0`, we cannot start, so all nodes are unreachable. Return array of all -1)

3. **Graph type**: Is this always a tree? (Assumption: Yes, `edges.length == n - 1` guarantees it's a tree, meaning there's exactly one path between any two nodes)

4. **Edge weights**: Are edge weights always positive? (Assumption: Yes, `1 <= lengthi <= 10^5`, so we can use Dijkstra's algorithm)

5. **Multiple paths**: Since it's a tree, is there only one path between nodes? (Assumption: Yes, but we still need to find the minimum time, which Dijkstra handles efficiently)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Use BFS/DFS to explore all paths from node 0, keeping track of minimum time to reach each node while checking disappear constraints. However, since it's a tree, there's only one path between nodes, so this is actually O(n) but doesn't handle the time constraint optimally.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use BFS level-by-level, but this doesn't work well for weighted graphs. We need to consider edge weights, not just hop count.

**Step 3: Optimized Solution (8 minutes)**

Use Dijkstra's algorithm with a modification: when relaxing an edge (u, v), only update `dist[v]` if `dist[u] + weight < disappear[v]`. This ensures we only consider paths that arrive before nodes disappear.

## Solution Approach

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

## Complexity Analysis

**Time Complexity:** O((V + E) log V)
- Building adjacency list: O(E)
- Dijkstra's algorithm: O((V + E) log V) with priority queue
- Total: O((V + E) log V)

**Space Complexity:** O(V + E)
- Adjacency list: O(E)
- Distance array: O(V)
- Priority queue: O(V)
- Total: O(V + E)

## Edge Cases

1. **Node 0 disappears immediately**: If `disappear[0] == 0`, return all `-1`
2. **Node disappears exactly when we arrive**: If `arrival_time == disappear[i]`, return `-1` (must arrive strictly before)
3. **Unreachable nodes**: Nodes with no path from node 0 return `-1`
4. **Large edge weights**: Edge weights can be up to 10^5, but total path length is bounded by disappear times

## Related Problems

- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) - Standard Dijkstra
- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Shortest path with edge count constraint
- [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) - Shortest path variant
- [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) - Shortest path with different optimization

## Template Reference

See [Graph Templates: Dijkstra](/posts/2025-10-29-leetcode-templates-graph/#dijkstra) for the standard Dijkstra template and variant with node disappearance constraints.
