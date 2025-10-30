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
- [Tarjan SCC / Bridges & Articulation](#tarjan-scc--bridges--articulation)

## BFS / Shortest Path (unweighted)

```cpp
int bfsGrid(vector<string>& g, pair<int,int> s, pair<int,int> t){
    int m=g.size(), n=g[0].size();
    queue<pair<int,int>> q; vector<vector<int>> dist(m, vector<int>(n, -1));
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
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

| ID | Title | Link |
|---|---|---|
| 200 | Number of Islands | [Number of Islands](https://leetcode.com/problems/number-of-islands/) |
| 417 | [Pacific Atlantic Water Flow](https://robinali34.github.io/blog_leetcode/posts/2025-10-19-medium-417-pacific-atlantic-water-flow/) | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) |
| 542 | 01 Matrix | [01 Matrix](https://leetcode.com/problems/01-matrix/) |

## Multi-source BFS (grids/graphs)

```cpp
int multiSourceBfs(vector<string>& g, vector<pair<int,int>> sources){
    int m=g.size(), n=g[0].size();
    queue<pair<int,int>> q; vector<vector<int>> dist(m, vector<int>(n, -1));
    for(auto [x,y]: sources){ dist[x][y]=0; q.push({x,y}); }
    int dirs[4][2]={{1,0},{-1,0},{0,1},{0,-1}}; int best=0;
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

| ID | Title | Link |
|---|---|---|
| 994 | Rotting Oranges | https://leetcode.com/problems/rotting-oranges/ |
| 286 | Walls and Gates | https://leetcode.com/problems/walls-and-gates/ |

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

| ID | Title | Link |
|---|---|---|
| 864 | Shortest Path to Get All Keys | https://leetcode.com/problems/shortest-path-to-get-all-keys/ |
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |

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

| ID | Title | Link |
|---|---|---|
| 207 | Course Schedule | https://leetcode.com/problems/course-schedule/ |
| 210 | Course Schedule II | https://leetcode.com/problems/course-schedule-ii/ |
| 269 | Alien Dictionary | https://leetcode.com/problems/alien-dictionary/ |

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

| ID | Title | Link |
|---|---|---|
| 743 | Network Delay Time | https://leetcode.com/problems/network-delay-time/ |
| 1631 | Path With Minimum Effort | https://leetcode.com/problems/path-with-minimum-effort/ |

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

| ID | Title | Link |
|---|---|---|
| 1293 | Shortest Path in a Grid with Obstacles Elimination | https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/ |
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |

## Tarjan SCC / Bridges & Articulation

```cpp
int timer2; vector<int> tin2, low2; vector<pair<int,int>> bridges;
void dfsBr(int u,int p,const vector<vector<int>>& g){ tin2[u]=low2[u]=++timer2; int child=0; bool isAP=false;
    for(int v:g[u]) if(v!=p){ if(!tin2[v]){ ++child; dfsBr(v,u,g); low2[u]=min(low2[u], low2[v]); if(low2[v]>tin2[u]) bridges.push_back({u,v}); if(p!=-1 && low2[v]>=tin2[u]) isAP=true; }
        else low2[u]=min(low2[u], tin2[v]); }
    if(p==-1 && child>1) isAP=true;
}
```

| ID | Title | Link |
|---|---|---|
| 1192 | Critical Connections in a Network | https://leetcode.com/problems/critical-connections-in-a-network/ |
{% endraw %}
