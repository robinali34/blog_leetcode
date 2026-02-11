---
layout: post
title: "Algorithm Templates: Graph"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates graph
permalink: /posts/2025-10-29-leetcode-templates-graph/
tags: [leetcode, templates, graph]
---

{% raw %}
Minimal, copy-paste C++ for graph traversal, shortest paths, and topological sort. 0-indexed unless noted.

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

Grid: 4-directional. Use for shortest path when all edges have weight 1.

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

| ID | Title | Link |
|----|--------|------|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) |
| 542 | 01 Matrix | [Link](https://leetcode.com/problems/01-matrix/) |

---

## Multi-source BFS

Start from multiple nodes (distance 0). Same as BFS with initial queue containing all sources.

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

| ID | Title | Link |
|----|--------|------|
| 994 | Rotting Oranges | [Link](https://leetcode.com/problems/rotting-oranges/) |
| 286 | Walls and Gates | [Link](https://leetcode.com/problems/walls-and-gates/) |

---

## BFS with state (bitmask)

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

Indegree-based. Edge (u, v) means u before v. Returns order or empty if cycle.

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

Nonnegative weights. Adjacency list: g[u] = [(v, w), ...]. Returns distances from source s.

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

---

## 0-1 BFS

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

Path compression + rank. See [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/#union-find-dsu) for full template.

| ID | Title | Link |
|----|--------|------|
| 684 | Redundant Connection | [Link](https://leetcode.com/problems/redundant-connection/) |
| 721 | Accounts Merge | [Link](https://leetcode.com/problems/accounts-merge/) |
| 323 | Number of Connected Components | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) |
| 399 | Evaluate Division | [Link](https://leetcode.com/problems/evaluate-division/) (weighted DSU) |

---

## More templates

- **Data structures (DSU, segment tree, etc.):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Binary search, rotated array, 2D:** [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
