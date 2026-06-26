---
layout: post
title: "Algorithm Templates: Graph"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates graph
permalink: /posts/2025-10-29-leetcode-templates-graph/
tags: [leetcode, templates, graph]
---
Graph algorithms are among the most versatile tools in competitive programming and coding interviews. A graph is simply a collection of nodes (vertices) connected by edges, and nearly every "network," "grid," or "relationship" problem maps onto one. This page provides production-ready C++ templates for the most common graph patterns — from basic traversal to advanced connectivity — so you can focus on modeling the problem rather than re-deriving algorithms from scratch. All templates are 0-indexed unless noted.

> **New to Graphs?** A graph consists of **nodes** (things) connected by **edges** (relationships between things). Most graph problems on LeetCode reduce to one of three categories: **traversal** (BFS/DFS — explore or find shortest paths), **shortest paths** with weights (Dijkstra, Bellman-Ford), or **connectivity / ordering** (Union-Find, Topological Sort). If you can identify which category your problem falls into, you're halfway to the solution.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 370" style="max-width:720px;width:100%;height:auto;display:block;margin:1.5em auto;">
  <defs>
    <marker id="ah" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#B8B5B0"/>
    </marker>
  </defs>
  <!-- Start node -->
  <rect x="260" y="10" width="200" height="44" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="360" y="38" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#5A5752" font-weight="bold">Graph Problem?</text>
  <!-- Level 1 branches -->
  <line x1="300" y1="54" x2="160" y2="100" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="360" y1="54" x2="360" y2="100" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="420" y1="54" x2="520" y2="100" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <!-- Question nodes -->
  <rect x="50" y="100" width="220" height="40" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="160" y="125" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#5A5752">Unweighted edges?</text>
  <rect x="260" y="100" width="200" height="40" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="360" y="125" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#5A5752">Ordering with dependencies?</text>
  <rect x="470" y="100" width="200" height="40" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="570" y="125" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#5A5752">Connected components?</text>
  <!-- Arrows to answers -->
  <line x1="160" y1="140" x2="160" y2="186" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="320" y1="140" x2="280" y2="186" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="400" y1="140" x2="440" y2="186" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="570" y1="140" x2="570" y2="186" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <!-- Answer nodes row 1 -->
  <rect x="80" y="190" width="160" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="160" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">BFS</text>
  <rect x="200" y="190" width="160" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="280" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">Topological Sort</text>
  <rect x="490" y="190" width="160" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="570" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">DSU or DFS</text>
  <!-- Weighted branch from start -->
  <line x1="360" y1="140" x2="360" y2="252" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <rect x="260" y="256" width="200" height="40" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="360" y="281" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#5A5752">Weighted edges?</text>
  <!-- Weighted sub-branches -->
  <line x1="310" y1="296" x2="220" y2="326" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="410" y1="296" x2="500" y2="326" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <rect x="100" y="320" width="240" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="220" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">Dijkstra</text>
  <text x="220" y="355" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#5A5752">(non-negative)</text>
  <rect x="380" y="320" width="240" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="500" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">Bellman-Ford</text>
  <text x="500" y="355" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#5A5752">(negative allowed)</text>
  <!-- Answer node for topo -->
  <rect x="360" y="190" width="120" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="420" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#5A5752">↓ weighted?</text>
  <text x="420" y="224" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#5A5752">see below</text>
</svg>

## Contents

- [BFS (unweighted)](#bfs-unweighted)
- [Multi-source BFS](#multi-source-bfs)
- [BFS with state (bitmask)](#bfs-with-state-bitmask)
- [Topological sort (Kahn)](#topological-sort-kahn)
- [Topological sort (DFS)](#topological-sort-dfs)
- [Dijkstra](#dijkstra)
- [0-1 BFS](#0-1-bfs)
- [Bellman-Ford (k edges)](#bellman-ford-k-edges)
- [Tarjan (SCC / bridges)](#tarjan-scc--bridges)
- [DSU](#dsu)

---

## BFS (unweighted)

**When to use:** "shortest path" or "minimum steps" on a grid or unweighted graph; "nearest exit"; "level-order traversal."

Grid: 4-directional. Use for shortest path when all edges have weight 1.

{% raw %}
```cpp
int bfs_grid(const vector<string>& g, int si, int sj, int ti, int tj) {
    int m = g.size(), n = g[0].size();
    vector<vector<int>> dist(m, vector<int>(n, -1));
    queue<pair<int,int>> q;
    q.push({si, sj});
    dist[si][sj] = 0;
    const int dirs[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    while (!q.empty()) {
        auto [i, j] = q.front();
        q.pop();
        if (i == ti && j == tj) return dist[i][j];
        for (auto& d : dirs) {
            int ni = i + d[0], nj = j + d[1];
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && g[ni][nj] != '#' && dist[ni][nj] == -1) {
                dist[ni][nj] = dist[i][j] + 1;
                q.push({ni, nj});
            }
        }
    }
    return -1;
}
```
{% endraw %}

| ID | Title | Link |
|----|--------|------|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) |
| 542 | 01 Matrix | [Link](https://leetcode.com/problems/01-matrix/) |

---

## Multi-source BFS

**When to use:** "distance from nearest X"; "spread from multiple starting points simultaneously"; "rotting oranges" or "fire spreading" patterns.

Start from multiple nodes (distance 0). Same as BFS with initial queue containing all sources.

{% raw %}
```cpp
int multi_bfs(const vector<string>& g, const vector<pair<int,int>>& sources) {
    int m = g.size(), n = g[0].size();
    vector<vector<int>> dist(m, vector<int>(n, -1));
    queue<pair<int,int>> q;
    for (auto [i, j] : sources) {
        dist[i][j] = 0;
        q.push({i, j});
    }
    const int dirs[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    int best = 0;
    while (!q.empty()) {
        auto [i, j] = q.front();
        q.pop();
        for (auto& d : dirs) {
            int ni = i + d[0], nj = j + d[1];
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && g[ni][nj] != '#' && dist[ni][nj] == -1) {
                dist[ni][nj] = dist[i][j] + 1;
                best = max(best, dist[ni][nj]);
                q.push({ni, nj});
            }
        }
    }
    return best;
}
```
{% endraw %}

| ID | Title | Link |
|----|--------|------|
| 994 | Rotting Oranges | [Link](https://leetcode.com/problems/rotting-oranges/) |
| 286 | Walls and Gates | [Link](https://leetcode.com/problems/walls-and-gates/) |

---

## BFS with state (bitmask)

**When to use:** "visit all nodes/keys"; "shortest path visiting a subset"; state changes at each step (e.g., collecting keys unlocks doors).

State = (node, mask). Use when “visit all keys” or “visit all nodes” is part of the goal.

```cpp
int bfs_mask(int n, const vector<vector<int>>& g, int start) {
    int full = (1 << n) - 1;
    vector<vector<bool>> vis(n, vector<bool>(1 << n, false));
    queue<pair<int,int>> q;
    q.push({start, 1 << start});
    vis[start][1 << start] = true;
    for (int d = 0; !q.empty(); d++) {
        int sz = q.size();
        while (sz--) {
            auto [u, mask] = q.front();
            q.pop();
            if (mask == full) return d;
            for (int v : g[u]) {
                int m2 = mask | (1 << v);
                if (!vis[v][m2]) {
                    vis[v][m2] = true;
                    q.push({v, m2});
                }
            }
        }
    }
    return -1;
}
```

| ID | Title | Link |
|----|--------|------|
| 847 | Shortest Path Visiting All Nodes | [Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |
| 864 | Shortest Path to Get All Keys | [Link](https://leetcode.com/problems/shortest-path-to-get-all-keys/) |

---

## Topological sort (Kahn)

**When to use:** "course prerequisites"; "build order"; "can I finish all tasks?"; finding a valid ordering of a DAG; cycle detection in directed graphs.

Indegree-based. Edge (u, v) means u before v. Returns order or empty if cycle.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 290" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="ka" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#8B8680"/>
    </marker>
  </defs>
  <!-- Step titles -->
  <text x="115" y="22" text-anchor="middle" font-size="12" fill="#3A3530" font-weight="bold">① Compute indegrees</text>
  <text x="360" y="22" text-anchor="middle" font-size="12" fill="#3A3530" font-weight="bold">② Process A, B</text>
  <text x="605" y="22" text-anchor="middle" font-size="12" fill="#3A3530" font-weight="bold">③ Process C, D</text>
  <!-- Panel dividers -->
  <line x1="234" y1="8" x2="234" y2="282" stroke="#E8E3D8" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="486" y1="8" x2="486" y2="282" stroke="#E8E3D8" stroke-width="1" stroke-dasharray="4,3"/>
  <!-- ===== PANEL 1: Initial indegrees ===== -->
  <!-- Edges (drawn first, behind nodes) -->
  <line x1="70" y1="100" x2="120" y2="121" stroke="#8B8680" stroke-width="1.5" marker-end="url(#ka)"/>
  <line x1="70" y1="155" x2="120" y2="135" stroke="#8B8680" stroke-width="1.5" marker-end="url(#ka)"/>
  <line x1="158" y1="128" x2="178" y2="128" stroke="#8B8680" stroke-width="1.5" marker-end="url(#ka)"/>
  <!-- Node A (indegree 0) — enqueued -->
  <circle cx="52" cy="92" r="20" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="52" y="97" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">A</text>
  <rect x="68" y="74" width="20" height="15" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1"/>
  <text x="78" y="85" text-anchor="middle" font-size="9" fill="#3A3530" font-weight="bold">0</text>
  <!-- Node B (indegree 0) — enqueued -->
  <circle cx="52" cy="163" r="20" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="52" y="168" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">B</text>
  <rect x="68" y="145" width="20" height="15" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1"/>
  <text x="78" y="156" text-anchor="middle" font-size="9" fill="#3A3530" font-weight="bold">0</text>
  <!-- Node C (indegree 2) -->
  <circle cx="138" cy="128" r="20" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="138" y="133" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">C</text>
  <rect x="154" y="110" width="20" height="15" rx="3" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="164" y="121" text-anchor="middle" font-size="9" fill="#5A5752">2</text>
  <!-- Node D (indegree 1) -->
  <circle cx="200" cy="128" r="20" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="200" y="133" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">D</text>
  <rect x="216" y="110" width="20" height="15" rx="3" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="226" y="121" text-anchor="middle" font-size="9" fill="#5A5752">1</text>
  <!-- Queue -->
  <rect x="15" y="210" width="205" height="32" rx="5" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <text x="26" y="230" font-size="11" fill="#5A5752">Queue:</text>
  <rect x="75" y="215" width="26" height="22" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1"/>
  <text x="88" y="230" text-anchor="middle" font-size="11" fill="#3A3530" font-weight="bold">A</text>
  <rect x="105" y="215" width="26" height="22" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1"/>
  <text x="118" y="230" text-anchor="middle" font-size="11" fill="#3A3530" font-weight="bold">B</text>
  <text x="26" y="265" font-size="11" fill="#7A7772">Output: [ ]</text>
  <!-- ===== PANEL 2: Process A, B ===== -->
  <!-- Faded edges -->
  <line x1="312" y1="100" x2="357" y2="121" stroke="#D4D8E0" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="312" y1="155" x2="357" y2="135" stroke="#D4D8E0" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="398" y1="128" x2="418" y2="128" stroke="#8B8680" stroke-width="1.5" marker-end="url(#ka)"/>
  <!-- A — processed -->
  <circle cx="294" cy="92" r="20" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="294" y="97" text-anchor="middle" font-size="14" fill="#9A9792">A</text>
  <text x="294" y="76" text-anchor="middle" font-size="10" fill="#9A9792">✓</text>
  <!-- B — processed -->
  <circle cx="294" cy="163" r="20" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="294" y="168" text-anchor="middle" font-size="14" fill="#9A9792">B</text>
  <text x="294" y="147" text-anchor="middle" font-size="10" fill="#9A9792">✓</text>
  <!-- C (indegree 2→0) — now enqueued -->
  <circle cx="380" cy="128" r="20" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="380" y="133" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">C</text>
  <rect x="396" y="110" width="32" height="15" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1"/>
  <text x="412" y="121" text-anchor="middle" font-size="8" fill="#3A3530" font-weight="bold">2→0</text>
  <!-- D (indegree 1) -->
  <circle cx="440" cy="128" r="20" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="440" y="133" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">D</text>
  <rect x="456" y="110" width="20" height="15" rx="3" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="466" y="121" text-anchor="middle" font-size="9" fill="#5A5752">1</text>
  <!-- Queue -->
  <rect x="257" y="210" width="205" height="32" rx="5" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <text x="268" y="230" font-size="11" fill="#5A5752">Queue:</text>
  <rect x="320" y="215" width="26" height="22" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1"/>
  <text x="333" y="230" text-anchor="middle" font-size="11" fill="#3A3530" font-weight="bold">C</text>
  <text x="268" y="265" font-size="11" fill="#7A7772">Output: [A, B]</text>
  <!-- ===== PANEL 3: Process C, D — done ===== -->
  <!-- All edges faded -->
  <line x1="554" y1="100" x2="597" y2="121" stroke="#D4D8E0" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="554" y1="155" x2="597" y2="135" stroke="#D4D8E0" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="640" y1="128" x2="655" y2="128" stroke="#D4D8E0" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- All nodes processed -->
  <circle cx="536" cy="92" r="20" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="536" y="97" text-anchor="middle" font-size="14" fill="#9A9792">A</text>
  <circle cx="536" cy="163" r="20" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="536" y="168" text-anchor="middle" font-size="14" fill="#9A9792">B</text>
  <circle cx="619" cy="128" r="20" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="619" y="133" text-anchor="middle" font-size="14" fill="#9A9792">C</text>
  <circle cx="677" cy="128" r="20" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="677" y="133" text-anchor="middle" font-size="14" fill="#9A9792">D</text>
  <!-- Queue (empty) -->
  <rect x="500" y="210" width="205" height="32" rx="5" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <text x="511" y="230" font-size="11" fill="#9A9792">Queue: (empty)</text>
  <!-- Final output -->
  <rect x="500" y="255" width="205" height="28" rx="5" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="602" y="274" text-anchor="middle" font-size="12" fill="#3A3530" font-weight="bold">Output: [A, B, C, D] ✓</text>
</svg>

```cpp
vector<int> topo_kahn(int n, const vector<vector<int>>& g) {
    vector<int> indeg(n);
    for (int u = 0; u < n; u++)
        for (int v : g[u]) indeg[v]++;
    queue<int> q;
    for (int i = 0; i < n; i++)
        if (indeg[i] == 0) q.push(i);
    vector<int> order;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);
        for (int v : g[u])
            if (--indeg[v] == 0) q.push(v);
    }
    return (int)order.size() == n ? order : vector<int>{};
}
```

| ID | Title | Link |
|----|--------|------|
| 207 | Course Schedule | [Link](https://leetcode.com/problems/course-schedule/) |
| 210 | Course Schedule II | [Link](https://leetcode.com/problems/course-schedule-ii/) |
| 269 | Alien Dictionary | [Link](https://leetcode.com/problems/alien-dictionary/) |

---

## Topological sort (DFS)

**When to use:** Same as Kahn's, but preferred when you also need cycle detection via back-edges; "find all safe states"; problems where DFS post-order gives useful structure.

Three colors: 0 unvisited, 1 visiting, 2 done. Push to order when finishing. Reverse = topo order. Back edge (neighbor color 1) = cycle.

```cpp
vector<int> topo_dfs(int n, const vector<vector<int>>& g) {
    vector<int> color(n, 0), order;
    bool ok = true;
    function<void(int)> dfs = [&](int u) {
        color[u] = 1;
        for (int v : g[u]) {
            if (color[v] == 0) dfs(v);
            else if (color[v] == 1) ok = false;
        }
        color[u] = 2;
        order.push_back(u);
    };
    for (int i = 0; i < n; i++)
        if (color[i] == 0) dfs(i);
    if (!ok) return {};
    reverse(order.begin(), order.end());
    return order;
}
```

| ID | Title | Link |
|----|--------|------|
| 802 | Find Eventual Safe States | [Link](https://leetcode.com/problems/find-eventual-safe-states/) |

---

## Dijkstra

**When to use:** "shortest path" with non-negative weights; "minimum cost to reach destination"; "network delay time"; any weighted graph where all weights ≥ 0.

Nonnegative weights. Adjacency list: g[u] = [(v, w), ...]. Returns distances from source s.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="da" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#8B8680"/>
    </marker>
  </defs>
  <!-- ======== WEIGHTED GRAPH ======== -->
  <!-- Edges with weight labels -->
  <line x1="121" y1="85" x2="259" y2="53" stroke="#8B8680" stroke-width="1.5" marker-end="url(#da)"/>
  <line x1="121" y1="95" x2="259" y2="127" stroke="#8B8680" stroke-width="1.5" marker-end="url(#da)"/>
  <line x1="280" y1="110" x2="280" y2="70" stroke="#8B8680" stroke-width="1.5" marker-end="url(#da)"/>
  <line x1="301" y1="53" x2="439" y2="85" stroke="#8B8680" stroke-width="1.5" marker-end="url(#da)"/>
  <line x1="301" y1="127" x2="439" y2="95" stroke="#8B8680" stroke-width="1.5" marker-end="url(#da)"/>
  <!-- Weight labels -->
  <rect x="178" y="57" width="18" height="16" rx="3" fill="#FAF8F5" stroke="none"/>
  <text x="187" y="69" text-anchor="middle" font-size="11" fill="#5A5752" font-weight="bold">4</text>
  <rect x="178" y="105" width="18" height="16" rx="3" fill="#FAF8F5" stroke="none"/>
  <text x="187" y="117" text-anchor="middle" font-size="11" fill="#5A5752" font-weight="bold">1</text>
  <rect x="286" y="82" width="18" height="16" rx="3" fill="#FAF8F5" stroke="none"/>
  <text x="295" y="94" text-anchor="middle" font-size="11" fill="#5A5752" font-weight="bold">2</text>
  <rect x="362" y="57" width="18" height="16" rx="3" fill="#FAF8F5" stroke="none"/>
  <text x="371" y="69" text-anchor="middle" font-size="11" fill="#5A5752" font-weight="bold">3</text>
  <rect x="362" y="105" width="18" height="16" rx="3" fill="#FAF8F5" stroke="none"/>
  <text x="371" y="117" text-anchor="middle" font-size="11" fill="#5A5752" font-weight="bold">7</text>
  <!-- Nodes (on top of edges) -->
  <circle cx="100" cy="90" r="22" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="100" y="95" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">S</text>
  <text x="100" y="125" text-anchor="middle" font-size="10" fill="#5A5752">dist: 0</text>
  <circle cx="280" cy="48" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="280" y="53" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">A</text>
  <text x="280" y="24" text-anchor="middle" font-size="10" fill="#5A5752">dist: ∞</text>
  <circle cx="280" cy="132" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="280" y="137" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">B</text>
  <text x="280" y="167" text-anchor="middle" font-size="10" fill="#5A5752">dist: ∞</text>
  <circle cx="460" cy="90" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="460" y="95" text-anchor="middle" font-size="14" fill="#3A3530" font-weight="bold">C</text>
  <text x="460" y="125" text-anchor="middle" font-size="10" fill="#5A5752">dist: ∞</text>
  <!-- Graph label -->
  <text x="540" y="52" font-size="10" fill="#7A7772">Edges: S→A(4), S→B(1),</text>
  <text x="540" y="66" font-size="10" fill="#7A7772">B→A(2), A→C(3), B→C(7)</text>
  <!-- ======== STEP BOXES ======== -->
  <!-- Step 1: Process S -->
  <rect x="15" y="183" width="215" height="110" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <rect x="15" y="183" width="215" height="24" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="122" y="199" text-anchor="middle" font-size="11" fill="#3A3530" font-weight="bold">Process S (dist 0)</text>
  <text x="28" y="224" font-size="10" fill="#5A5752">Relax S→A: dist[A] = 0+4 = 4</text>
  <text x="28" y="240" font-size="10" fill="#5A5752">Relax S→B: dist[B] = 0+1 = 1</text>
  <text x="28" y="262" font-size="10" fill="#7A7772">PQ: {(1, B), (4, A)}</text>
  <text x="28" y="280" font-size="10" fill="#7A7772">dist: [S=0, A=4, B=1]</text>
  <!-- Step 2: Process B — RELAXATION -->
  <rect x="243" y="183" width="215" height="110" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <rect x="243" y="183" width="215" height="24" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="350" y="199" text-anchor="middle" font-size="11" fill="#3A3530" font-weight="bold">Process B (dist 1)</text>
  <text x="256" y="224" font-size="10" fill="#3A3530" font-weight="bold">★ B→A: 1+2=3 &lt; 4 — relaxed!</text>
  <text x="256" y="240" font-size="10" fill="#5A5752">Relax B→C: dist[C] = 1+7 = 8</text>
  <text x="256" y="262" font-size="10" fill="#7A7772">PQ: {(3, A), (8, C)}</text>
  <text x="256" y="280" font-size="10" fill="#7A7772">dist: [S=0, B=1, A=3, C=8]</text>
  <!-- Step 3: Process A — RELAXATION -->
  <rect x="471" y="183" width="215" height="110" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <rect x="471" y="183" width="215" height="24" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="578" y="199" text-anchor="middle" font-size="11" fill="#3A3530" font-weight="bold">Process A (dist 3)</text>
  <text x="484" y="224" font-size="10" fill="#3A3530" font-weight="bold">★ A→C: 3+3=6 &lt; 8 — relaxed!</text>
  <text x="484" y="248" font-size="10" fill="#7A7772">PQ: {(6, C)}</text>
  <rect x="484" y="264" width="190" height="22" rx="4" fill="#D4D8D0" stroke="#8B8680" stroke-width="1"/>
  <text x="579" y="280" text-anchor="middle" font-size="10" fill="#3A3530" font-weight="bold">Final: S=0, B=1, A=3, C=6</text>
</svg>

```cpp
vector<long long> dijkstra(int n, const vector<vector<pair<int,int>>>& g, int s) {
    const long long INF = 1LL << 60;
    vector<long long> dist(n, INF);
    dist[s] = 0;
    using P = pair<long long, int>;
    priority_queue<P, vector<P>, greater<P>> pq;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d != dist[u]) continue;
        for (auto [v, w] : g[u]) {
            if (dist[v] > d + w) {
                dist[v] = d + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```

| ID | Title | Link |
|----|--------|------|
| 743 | Network Delay Time | [Link](https://leetcode.com/problems/network-delay-time/) |
| 1976 | Number of Ways to Arrive at Destination | [Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) |
| 3112 | Minimum Time to Visit Disappearing Nodes | [Link](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/) |
| 3341 | Find Minimum Time to Reach Last Room I | [Link](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/) |
| 3342 | Find Minimum Time to Reach Last Room II | [Link](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/) |

**Variant: nodes disappear at given times (3112).** Only relax edge \((u,v)\) if `dist[u] + w < disappear[v]`.

```cpp
vector<int> dijkstra_disappear(int n, const vector<vector<pair<int,int>>>& g,
                               const vector<int>& disappear) {
    vector<int> dist(n, -1);
    dist[0] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (dist[u] != -1 && d > dist[u]) continue;
        for (auto [v, w] : g[u]) {
            int nd = d + w;
            if (nd < disappear[v] && (dist[v] == -1 || nd < dist[v])) {
                dist[v] = nd;
                pq.push({nd, v});
            }
        }
    }
    return dist;
}
```

**Variant: grid with earliest-entry times (3341).** Moving costs 1, but you may need to wait to enter the next cell:
\[
\text{nextTime} = \max(\text{curTime},\ \text{open}[ni][nj]) + 1
\]

{% raw %}
```cpp
long long dijkstra_grid_open(const vector<vector<int>>& open) {
    int n = open.size(), m = open[0].size();
    const long long INF = 1LL << 60;
    vector<vector<long long>> dist(n, vector<long long>(m, INF));
    dist[0][0] = 0;
    using S = pair<long long, pair<int,int>>; // (time, (i,j))
    priority_queue<S, vector<S>, greater<>> pq;
    pq.push({0, {0, 0}});
    const int dirs[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    while (!pq.empty()) {
        auto [t, pos] = pq.top();
        pq.pop();
        auto [i, j] = pos;
        if (t != dist[i][j]) continue;
        if (i == n - 1 && j == m - 1) return t;
        for (auto& d : dirs) {
            int ni = i + d[0], nj = j + d[1];
            if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
            long long nt = max(t, (long long)open[ni][nj]) + 1;
            if (nt < dist[ni][nj]) {
                dist[ni][nj] = nt;
                pq.push({nt, {ni, nj}});
            }
        }
    }
    return dist[n - 1][m - 1];
}
```
{% endraw %}

---

## 0-1 BFS

**When to use:** Edge weights are only 0 or 1; "minimum flips/changes to reach target"; grid problems where some moves are free and others cost 1.

Weights 0 or 1. Deque: push front for 0, back for 1. O(V + E).

```cpp
vector<int> bfs01(int n, const vector<vector<pair<int,int>>>& g, int s) {
    vector<int> dist(n, 1e9);
    dist[s] = 0;
    deque<int> dq;
    dq.push_front(s);
    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();
        for (auto [v, w] : g[u]) {
            int nd = dist[u] + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                if (w == 0) dq.push_front(v);
                else dq.push_back(v);
            }
        }
    }
    return dist;
}
```

---

## Bellman-Ford (k edges)

**When to use:** "cheapest flight within K stops"; shortest path with a constraint on number of edges; negative edge weights allowed; detecting negative cycles.

Relax all edges up to k times. Use when path length (number of edges) is limited.

```cpp
vector<long long> bellman_ford_k(int n, const vector<array<int,3>>& edges, int src, int k) {
    const long long INF = 1LL << 60;
    vector<long long> dist(n, INF);
    dist[src] = 0;
    for (int i = 0; i <= k; i++) {
        vector<long long> ndist = dist;
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            if (dist[u] != INF && dist[u] + w < ndist[v])
                ndist[v] = dist[u] + w;
        }
        dist = move(ndist);
    }
    return dist;
}
```

| ID | Title | Link |
|----|--------|------|
| 787 | Cheapest Flights Within K Stops | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |

---

## Tarjan (SCC / bridges)

**When to use:** "critical connections"; "articulation points"; "strongly connected components"; finding bridges whose removal disconnects the graph.

SCC: same low-link = same component. Bridges: edge (u,v) is bridge iff low[v] > tin[u].

```cpp
struct Tarjan {
    int n, timer = 0;
    vector<vector<int>> g;
    vector<int> tin, low, comp, st;
    vector<char> in;
    int ncomp = 0;

    Tarjan(int n) : n(n), g(n), tin(n, -1), low(n), comp(n, -1), in(n, 0) {}
    void add(int u, int v) { g[u].push_back(v); }

    void dfs(int u) {
        tin[u] = low[u] = timer++;
        st.push_back(u);
        in[u] = 1;
        for (int v : g[u]) {
            if (tin[v] == -1) {
                dfs(v);
                low[u] = min(low[u], low[v]);
            } else if (in[v])
                low[u] = min(low[u], tin[v]);
        }
        if (low[u] == tin[u]) {
            while (true) {
                int v = st.back();
                st.pop_back();
                in[v] = 0;
                comp[v] = ncomp;
                if (v == u) break;
            }
            ncomp++;
        }
    }
    int run() {
        for (int i = 0; i < n; i++)
            if (tin[i] == -1) dfs(i);
        return ncomp;
    }
};

// Bridges: during dfs, if (low[v] > tin[u]) then (u,v) is bridge
vector<pair<int,int>> bridges(int n, const vector<vector<int>>& g) {
    int timer = 0;
    vector<int> tin(n, -1), low(n);
    vector<pair<int,int>> out;
    function<void(int,int)> dfs = [&](int u, int p) {
        tin[u] = low[u] = timer++;
        for (int v : g[u]) {
            if (tin[v] == -1) {
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > tin[u]) out.push_back({u, v});
            } else if (v != p)
                low[u] = min(low[u], tin[v]);
        }
    };
    for (int i = 0; i < n; i++)
        if (tin[i] == -1) dfs(i, -1);
    return out;
}
```

| ID | Title | Link |
|----|--------|------|
| 1192 | Critical Connections in a Network | [Link](https://leetcode.com/problems/critical-connections-in-a-network/) |

---

## DSU

**When to use:** "number of connected components"; "are two nodes in the same group?"; "redundant connection" (cycle detection in undirected graph); dynamic connectivity as edges are added.

Path compression + rank. See [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/#union-find-dsu) for full template.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 210" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="ua" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#8B8680"/>
    </marker>
    <marker id="ua2" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#B8B5B0"/>
    </marker>
  </defs>
  <!-- Panel titles -->
  <text x="110" y="18" text-anchor="middle" font-size="12" fill="#3A3530" font-weight="bold">① Initial (6 sets)</text>
  <text x="345" y="18" text-anchor="middle" font-size="12" fill="#3A3530" font-weight="bold">② After 3 unions</text>
  <text x="590" y="18" text-anchor="middle" font-size="12" fill="#3A3530" font-weight="bold">③ Path compression</text>
  <!-- Dividers -->
  <line x1="225" y1="6" x2="225" y2="204" stroke="#E8E3D8" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="465" y1="6" x2="465" y2="204" stroke="#E8E3D8" stroke-width="1" stroke-dasharray="4,3"/>
  <!-- ===== PANEL 1: 6 separate nodes ===== -->
  <circle cx="45" cy="75" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="45" y="80" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">0</text>
  <circle cx="110" cy="75" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="110" y="80" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">1</text>
  <circle cx="175" cy="75" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="175" y="80" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">2</text>
  <circle cx="45" cy="140" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="45" y="145" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">3</text>
  <circle cx="110" cy="140" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="110" y="145" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">4</text>
  <circle cx="175" cy="140" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="175" y="145" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">5</text>
  <text x="110" y="186" text-anchor="middle" font-size="10" fill="#7A7772">Each node is its own root</text>
  <!-- ===== PANEL 2: After union(0,1), union(2,3), union(4,5) ===== -->
  <!-- Tree 0←1 -->
  <line x1="280" y1="124" x2="280" y2="94" stroke="#8B8680" stroke-width="1.5" marker-end="url(#ua)"/>
  <circle cx="280" cy="72" r="16" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="280" y="77" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">0</text>
  <circle cx="280" cy="140" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="280" y="145" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">1</text>
  <!-- Tree 2←3 -->
  <line x1="345" y1="124" x2="345" y2="94" stroke="#8B8680" stroke-width="1.5" marker-end="url(#ua)"/>
  <circle cx="345" cy="72" r="16" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="345" y="77" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">2</text>
  <circle cx="345" cy="140" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="345" y="145" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">3</text>
  <!-- Tree 4←5 -->
  <line x1="410" y1="124" x2="410" y2="94" stroke="#8B8680" stroke-width="1.5" marker-end="url(#ua)"/>
  <circle cx="410" cy="72" r="16" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="410" y="77" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">4</text>
  <circle cx="410" cy="140" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="410" y="145" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">5</text>
  <text x="345" y="186" text-anchor="middle" font-size="10" fill="#7A7772">union(0,1) union(2,3) union(4,5)</text>
  <!-- ===== PANEL 3: Path compression ===== -->
  <!-- BEFORE find(3): tree 0←1, 0←2←3 -->
  <text x="527" y="36" text-anchor="middle" font-size="10" fill="#7A7772">Before find(3)</text>
  <!-- Edge 1→0 -->
  <line x1="505" y1="96" x2="522" y2="70" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ua2)"/>
  <!-- Edge 2→0 (highlighted path) -->
  <line x1="549" y1="96" x2="535" y2="70" stroke="#8B8680" stroke-width="2" marker-end="url(#ua)"/>
  <!-- Edge 3→2 (highlighted path) -->
  <line x1="556" y1="138" x2="556" y2="118" stroke="#8B8680" stroke-width="2" marker-end="url(#ua)"/>
  <!-- Nodes -->
  <circle cx="527" cy="54" r="16" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="527" y="59" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">0</text>
  <circle cx="496" cy="105" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="496" y="110" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">1</text>
  <circle cx="556" cy="105" r="16" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="556" y="110" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">2</text>
  <circle cx="556" cy="155" r="16" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="556" y="160" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">3</text>
  <!-- Arrow between before/after -->
  <text x="596" y="105" text-anchor="middle" font-size="18" fill="#8B8680">→</text>
  <!-- AFTER find(3): tree 0←1, 0←2, 0←3 (all direct children) -->
  <text x="660" y="36" text-anchor="middle" font-size="10" fill="#7A7772">After find(3)</text>
  <!-- Edge 1→0 -->
  <line x1="633" y1="96" x2="650" y2="70" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ua2)"/>
  <!-- Edge 2→0 -->
  <line x1="660" y1="89" x2="660" y2="72" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ua2)"/>
  <!-- Edge 3→0 (highlighted — new direct link) -->
  <line x1="685" y1="96" x2="669" y2="70" stroke="#8B8680" stroke-width="2" marker-end="url(#ua)"/>
  <!-- Nodes -->
  <circle cx="660" cy="54" r="16" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="660" y="59" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">0</text>
  <circle cx="624" cy="105" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="624" y="110" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">1</text>
  <circle cx="660" cy="105" r="16" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="660" y="110" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">2</text>
  <circle cx="696" cy="105" r="16" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="696" y="110" text-anchor="middle" font-size="13" fill="#3A3530" font-weight="bold">3</text>
  <text x="590" y="186" text-anchor="middle" font-size="10" fill="#7A7772">3 now points directly to root 0</text>
</svg>

| ID | Title | Link | Solution |
|----|--------|------|----------|
| 684 | Redundant Connection | [Link](https://leetcode.com/problems/redundant-connection/) | - |
| 721 | Accounts Merge | [Link](https://leetcode.com/problems/accounts-merge/) | - |
| 323 | Number of Connected Components | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | - |
| 399 | Evaluate Division | [Link](https://leetcode.com/problems/evaluate-division/) | - |
| 1202 | Smallest String With Swaps | [Link](https://leetcode.com/problems/smallest-string-with-swaps/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/09/medium-1202-smallest-string-with-swaps/) |
| 1319 | Number of Operations to Make Network Connected | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/10/medium-1319-number-of-operations-to-make-network-connected/) |
| 1584 | Min Cost to Connect All Points | [Link](https://leetcode.com/problems/min-cost-to-connect-all-points/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/08/medium-1584-min-cost-to-connect-all-points/) |
| 261 | Graph Valid Tree | [Link](https://leetcode.com/problems/graph-valid-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/01/medium-261-graph-valid-tree/) |

---

## Algorithm Summary

| Algorithm | When to Use | Time | Space |
|---|---|---|---|
| BFS | Shortest path, unweighted | O(V+E) | O(V) |
| Dijkstra | Shortest path, non-negative weights | O((V+E) log V) | O(V) |
| Bellman-Ford | Shortest path, negative weights, k edges | O(VE) | O(V) |
| Topological Sort | DAG ordering, prerequisites | O(V+E) | O(V) |
| DSU (Union-Find) | Connected components, cycle detection | O(α(n)) per op | O(V) |
| Tarjan | SCC, bridges, articulation points | O(V+E) | O(V) |

---

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures (DSU, segment tree, etc.):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Binary search, rotated array, 2D:** [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
