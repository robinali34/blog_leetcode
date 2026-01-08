---
layout: post
title: "LeetCode Templates: Graph"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates graph
permalink: /posts/2025-10-29-leetcode-templates-graph/
tags: [leetcode, templates, graph]
---

{% raw %}
## Contents

- [BFS / Shortest Path](#bfs--shortest-path-unweighted)
- [Multi-source BFS](#multi-source-bfs-gridsgraphs)
- [BFS on Bitmask State](#bfs-on-bitmask-state-visit-all-keys)
- [Topological Sort (Kahn)](#topological-sort-kahn)
- [Dijkstra](#dijkstra-weights--0)
- [0-1 BFS](#0-1-bfs-weights-0-or-1)
- [Disjoint Set Union (DSU)](#disjoint-set-union-dsu)
- [Tarjan SCC / Bridges & Articulation](#tarjan-scc--bridges--articulation)

## BFS / Shortest Path (unweighted)

```cpp
int bfsGrid(vector<string>& g, pair<int,int> s, pair<int,int> t){
    int m=g.size(), n=g[0].size();
    queue<pair<int,int>> q; vector<vector<int>> dist(m, vector<int>(n, -1));
    int dirs[4][2] = \{\{1,0\},\{-1,0\},\{0,1\},\{0,-1\}\};
    q.push(s); dist[s.first][s.second] = 0;
    while(!q.empty()){
        auto [x,y] = q.front(); q.pop();
        if (make_pair(x,y) == t) return dist[x][y];
        for (auto& d: dirs){
            int nx=x+d[0], ny=y+d[1];
            if (nx>=0&&nx<m&&ny>=0&&ny<n && g[nx][ny] != '#' && dist[nx][ny]==-1){
                dist[nx][ny] = dist[x][y] + 1; q.push({nx,ny});
            }
        }
    }
    return -1;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) | - |
| 417 | Pacific Atlantic Water Flow | [Link](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-417-pacific-atlantic-water-flow/) |
| 542 | 01 Matrix | [Link](https://leetcode.com/problems/01-matrix/) | - |

## Multi-source BFS (grids/graphs)

```cpp
int multiSourceBfs(vector<string>& g, vector<pair<int,int>> sources){
    int m=g.size(), n=g[0].size();
    queue<pair<int,int>> q; vector<vector<int>> dist(m, vector<int>(n, -1));
    for(auto [x,y]: sources){ dist[x][y]=0; q.push({x,y}); }
    int dirs[4][2]=\{\{1,0\},\{-1,0\},\{0,1\},\{0,-1\}\}; int best=0;
    while(!q.empty()){
        auto [x,y]=q.front(); q.pop();
        for(auto& d: dirs){ int nx=x+d[0], ny=y+d[1];
            if(nx>=0&&nx<m&&ny>=0&&ny<n && g[nx][ny] != '#' && dist[nx][ny]==-1){
                dist[nx][ny]=dist[x][y]+1; best=max(best, dist[nx][ny]); q.push({nx,ny});
            }
        }
    }
    return best;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 994 | Rotting Oranges | [Link](https://leetcode.com/problems/rotting-oranges/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-13-medium-994-rotting-oranges/) |
| 286 | Walls and Gates | [Link](https://leetcode.com/problems/walls-and-gates/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-14-medium-286-walls-and-gates/) |

## BFS on Bitmask State (visit all keys)

```cpp
struct State{int u,mask};
int bfsMask(const vector<vector<int>>& g, int start){
    int n=g.size(); int full=(1<<n)-1; queue<State> q; vector vis(n, vector<bool>(1<<n,false));
    q.push({start, 1<<start}); vis[start][1<<start]=true; int d=0;
    while(!q.empty()){
        int sz=q.size();
        while(sz--){ auto [u,mask]=q.front(); q.pop(); if(mask==full) return d;
            for(int v: g[u]){ int m2=mask|(1<<v); if(!vis[v][m2]){ vis[v][m2]=true; q.push({v,m2}); } }
        }
        ++d;
    }
    return -1;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 864 | Shortest Path to Get All Keys | [Link](https://leetcode.com/problems/shortest-path-to-get-all-keys/) | - |
| 847 | Shortest Path Visiting All Nodes | [Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | - |

## Topological Sort (Kahn)

```cpp
vector<int> topoKahn(int n, const vector<vector<int>>& g){
    vector<int> indeg(n); for(int u=0;u<n;++u) for(int v:g[u]) ++indeg[v];
    queue<int> q; for(int i=0;i<n;++i) if(!indeg[i]) q.push(i);
    vector<int> order;
    while(!q.empty()){ int u=q.front(); q.pop(); order.push_back(u);
        for(int v:g[u]) if(--indeg[v]==0) q.push(v);
    }
    if ((int)order.size()!=n) order.clear();
    return order;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 207 | Course Schedule | [Link](https://leetcode.com/problems/course-schedule/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-207-course-schedule/) |
| 210 | Course Schedule II | [Link](https://leetcode.com/problems/course-schedule-ii/) | - |
| 269 | Alien Dictionary | [Link](https://leetcode.com/problems/alien-dictionary/) | - |

## Dijkstra (weights ≥ 0)

```cpp
vector<long long> dijkstra(int n, const vector<vector<pair<int,int>>>& g, int s){
    const long long INF = (1LL<<60);
    vector<long long> dist(n, INF); dist[s]=0;
    using P=pair<long long,int>; priority_queue<P, vector<P>, greater<P>> pq; pq.push({0,s});
    while(!pq.empty()){
        auto [d,u]=pq.top(); pq.pop(); if(d!=dist[u]) continue;
        for(auto [v,w]: g[u]) if(dist[v]>d+w){ dist[v]=d+w; pq.push({dist[v],v}); }
    }
    return dist;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 743 | Network Delay Time | [Link](https://leetcode.com/problems/network-delay-time/) | - |
| 1631 | Path With Minimum Effort | [Link](https://leetcode.com/problems/path-with-minimum-effort/) | - |
| 1976 | Number of Ways to Arrive at Destination | [Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/28/medium-1976-number-of-ways-to-arrive-at-destination/) |

## 0-1 BFS (weights 0 or 1)

```cpp
deque<int> dq; vector<int> dist(n, 1e9); dist[s]=0; dq.push_front(s);
while(!dq.empty()){
    int u=dq.front(); dq.pop_front();
    for(auto [v,w]: g[u]){
        int nd = dist[u] + w; // w in {0,1}
        if (nd < dist[v]){
            dist[v]=nd; if (w==0) dq.push_front(v); else dq.push_back(v);
        }
    }
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1293 | Shortest Path in a Grid with Obstacles Elimination | [Link](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | - |
| 847 | Shortest Path Visiting All Nodes | [Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | - |

## Tarjan SCC / Bridges & Articulation

```cpp
int timer2; vector<int> tin2, low2; vector<pair<int,int>> bridges;
void dfsBr(int u,int p,const vector<vector<int>>& g){ tin2[u]=low2[u]=++timer2; int child=0; bool isAP=false;
    for(int v:g[u]) if(v!=p){ if(!tin2[v]){ ++child; dfsBr(v,u,g); low2[u]=min(low2[u], low2[v]); if(low2[v]>tin2[u]) bridges.push_back({u,v}); if(p!=-1 && low2[v]>=tin2[u]) isAP=true; }
        else low2[u]=min(low2[u], tin2[v]); }
    if(p==-1 && child>1) isAP=true;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1192 | Critical Connections in a Network | [Link](https://leetcode.com/problems/critical-connections-in-a-network/) | - |

## Disjoint Set Union (DSU)

Disjoint Set Union (DSU), also known as Union-Find, tracks connected components efficiently.

### Basic Disjoint Set

```cpp
class UnionFind {
    vector<int> parent;
public:
    UnionFind(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
    }
    
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};
```

### Disjoint Set with Union by Rank

Union by rank keeps tree balanced for better performance.

```cpp
class UnionFind {
    vector<int> parent, rank;
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px == py) return;
        
        // Union by rank: attach smaller tree to larger tree
        if (rank[px] < rank[py]) {
            parent[px] = py;
        } else if (rank[px] > rank[py]) {
            parent[py] = px;
        } else {
            parent[py] = px;
            rank[px]++;
        }
    }
    
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
    
    int countComponents() {
        unordered_set<int> roots;
        for (int i = 0; i < parent.size(); ++i) {
            roots.insert(find(i));
        }
        return roots.size();
    }
};
```

### Weighted Disjoint Set

For problems requiring maintaining weights/ratios (e.g., Evaluate Division).

```cpp
class WeightedUnionFind {
    unordered_map<string, pair<string, double>> weights;
    
    pair<string, double> find(const string& node) {
        if(!weights.contains(node)) {
            weights[node] = {node, 1.0};
        }
        auto entry = weights[node];
        if(entry.first != node) {
            auto parentEntry = find(entry.first);
            weights[node] = {
                parentEntry.first,
                entry.second * parentEntry.second
            };
        }
        return weights[node];
    }
    
    void unite(const string& dividend, const string& divisor, double value) {
        auto dividendEntry = find(dividend);
        auto divisorEntry = find(divisor);
        
        string dividendRoot = dividendEntry.first;
        string divisorRoot = divisorEntry.first;
        
        if(dividendRoot != divisorRoot) {
            weights[dividendRoot] = {
                divisorRoot,
                divisorEntry.second * value / dividendEntry.second
            };
        }
    }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 323 | Number of Connected Components in an Undirected Graph | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-323-number-of-connected-components-in-an-undirected-graph/) |
| 547 | Number of Provinces | [Link](https://leetcode.com/problems/number-of-provinces/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-18-medium-547-number-of-provinces/) |
| 684 | Redundant Connection | [Link](https://leetcode.com/problems/redundant-connection/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/29/medium-684-redundant-connection/) |
| 685 | Redundant Connection II | [Link](https://leetcode.com/problems/redundant-connection-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/hard-685-redundant-connection-ii/) |
| 721 | Accounts Merge | [Link](https://leetcode.com/problems/accounts-merge/) | - |
| 990 | Satisfiability of Equality Equations | [Link](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/04/medium-990-satisfiability-of-equality-equations/) |
| 399 | Evaluate Division | [Link](https://leetcode.com/problems/evaluate-division/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-17-medium-399-evaluate-division/) |
| 1319 | Number of Operations to Make Network Connected | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | - |

### References

- [LeetCode Disjoint Set LeetBook](https://leetcode.cn/leetbook/detail/disjoint-set/) - Comprehensive guide to Disjoint Set Union (DSU) with LeetCode problems

{% endraw %}
