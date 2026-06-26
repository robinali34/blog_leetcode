---
layout: post
title: "Algorithm Templates: BFS"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates bfs graph
permalink: /posts/2025-11-24-leetcode-templates-bfs/
tags: [leetcode, templates, bfs, graph, traversal]
---

{% raw %}
Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes layer by layer, visiting all neighbors at the current depth before moving deeper. It's the go-to technique for finding shortest paths in unweighted graphs and grids, and it appears constantly in LeetCode Medium problems.

> **New to BFS?** The core idea is simple: **use a queue to explore nodes level by level -- process all nodes at distance 1, then distance 2, then distance 3, and so on.** The first time you reach a node is always the shortest path.

<svg viewBox="0 0 720 340" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- Title -->
  <text x="360" y="22" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">BFS explores a graph level by level</text>

  <!-- Graph nodes -->
  <circle cx="200" cy="70" r="22" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="2"/>
  <text x="200" y="76" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">A</text>

  <circle cx="120" cy="150" r="22" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="2"/>
  <text x="120" y="156" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">B</text>
  <circle cx="280" cy="150" r="22" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="2"/>
  <text x="280" y="156" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">C</text>

  <circle cx="80" cy="240" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="2"/>
  <text x="80" y="246" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">D</text>
  <circle cx="200" cy="240" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="2"/>
  <text x="200" y="246" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">E</text>

  <!-- Edges -->
  <line x1="186" y1="88" x2="134" y2="132" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="214" y1="88" x2="266" y2="132" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="108" y1="168" x2="92" y2="222" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="138" y1="166" x2="186" y2="224" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="264" y1="166" x2="214" y2="224" stroke="#B8B5B0" stroke-width="1.5"/>

  <!-- Level labels -->
  <text x="340" y="76" font-size="11" fill="#5A5752" font-weight="600">Level 0</text>
  <text x="340" y="156" font-size="11" fill="#5A5752" font-weight="600">Level 1</text>
  <text x="340" y="246" font-size="11" fill="#5A5752" font-weight="600">Level 2</text>

  <!-- Queue state boxes -->
  <rect x="430" y="50" width="270" height="44" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="445" y="68" font-size="10" fill="#5A5752" font-weight="600">Queue:</text>
  <text x="500" y="68" font-size="12" fill="#3A3530" font-family="monospace">[A]</text>
  <text x="445" y="84" font-size="10" fill="#5A5752">Process A → enqueue B, C</text>

  <rect x="430" y="110" width="270" height="56" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="445" y="128" font-size="10" fill="#5A5752" font-weight="600">Queue:</text>
  <text x="500" y="128" font-size="12" fill="#3A3530" font-family="monospace">[B, C]</text>
  <text x="445" y="144" font-size="10" fill="#5A5752">Process B → enqueue D, E</text>
  <text x="445" y="158" font-size="10" fill="#5A5752">Process C → E already visited</text>

  <rect x="430" y="180" width="270" height="44" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="445" y="198" font-size="10" fill="#5A5752" font-weight="600">Queue:</text>
  <text x="500" y="198" font-size="12" fill="#3A3530" font-family="monospace">[D, E]</text>
  <text x="445" y="214" font-size="10" fill="#5A5752">Process D, E → no new neighbors</text>

  <rect x="430" y="240" width="270" height="36" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="445" y="258" font-size="10" fill="#5A5752" font-weight="600">Queue:</text>
  <text x="500" y="258" font-size="12" fill="#3A3530" font-family="monospace">[]</text>
  <text x="540" y="258" font-size="10" fill="#5A5752">→ Done!</text>

  <!-- Legend -->
  <circle cx="445" cy="305" r="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="460" y="309" font-size="10" fill="#5A5752">Level 0 (start)</text>
  <circle cx="545" cy="305" r="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="560" y="309" font-size="10" fill="#5A5752">Level 1</text>
  <circle cx="625" cy="305" r="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="640" y="309" font-size="10" fill="#5A5752">Level 2</text>
</svg>

## Contents

- [Basic BFS](#basic-bfs)
- [BFS on Grid](#bfs-on-grid)
- [Multi-source BFS](#multi-source-bfs)
- [BFS for Shortest Path](#bfs-for-shortest-path)
- [Level-order Traversal](#level-order-traversal)
- [BFS with State](#bfs-with-state)

## Basic BFS

**When to use:** The problem says "shortest path" or "minimum steps" in an unweighted graph, or asks you to explore all reachable nodes. Look for phrases like "fewest moves," "minimum number of operations," or "can you reach."

Breadth-First Search explores nodes level by level using a queue.

```cpp
// BFS on graph (adjacency list)
void bfs(vector<vector<int>>& graph, int start) {
    queue<int> q;
    vector<bool> visited(graph.size(), false);
    
    q.push(start);
    visited[start] = true;
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        
        // Process node
        cout << node << " ";
        
        // Explore neighbors
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 841 | Keys and Rooms | [Link](https://leetcode.com/problems/keys-and-rooms/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/12/medium-841-keys-and-rooms/) |

## BFS on Grid

**When to use:** The problem gives you a 2D matrix/grid and asks for shortest distance between cells, number of connected components (islands), or nearest cell of a certain type. Look for "grid," "matrix," "4-directional," or "adjacent cells."

BFS for 2D grid problems (4-directional or 8-directional).

```cpp
// BFS on 2D grid (4-directional)
int bfsGrid(vector<vector<char>>& grid, pair<int, int> start, pair<int, int> target) {
    int m = grid.size(), n = grid[0].size();
    queue<pair<int, int>> q;
    vector<vector<int>> dist(m, vector<int>(n, -1));
    vector<pair<int, int>> dirs = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
    
    q.push(start);
    dist[start.first][start.second] = 0;
    
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        
        if (make_pair(x, y) == target) {
            return dist[x][y];
        }
        
        for (auto& [dx, dy] : dirs) {
            int nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && 
                grid[nx][ny] != '#' && dist[nx][ny] == -1) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    return -1;
}

// Count connected components (Number of Islands)
int numIslands(vector<vector<char>>& grid) {
    int m = grid.size(), n = grid[0].size();
    int count = 0;
    vector<pair<int, int>> dirs = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == '1') {
                count++;
                queue<pair<int, int>> q;
                q.push({i, j});
                grid[i][j] = '0';
                
                while (!q.empty()) {
                    auto [x, y] = q.front();
                    q.pop();
                    
                    for (auto& [dx, dy] : dirs) {
                        int nx = x + dx, ny = y + dy;
                        if (nx >= 0 && nx < m && ny >= 0 && ny < n && 
                            grid[nx][ny] == '1') {
                            grid[nx][ny] = '0';
                            q.push({nx, ny});
                        }
                    }
                }
            }
        }
    }
    
    return count;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-20-medium-200-number-of-islands/) |
| 695 | Max Area of Island | [Link](https://leetcode.com/problems/max-area-of-island/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-695-max-area-of-island/) |

## Multi-source BFS

**When to use:** The problem asks for the distance from ANY source (not one specific source). Classic signals: "distance to nearest 0," "rotting spreads from all rotten oranges simultaneously," or "fill from all gates at once."

Start BFS from multiple sources simultaneously -- enqueue all starting points before the loop begins.

```cpp
// Multi-source BFS (e.g., 01 Matrix)
vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
    int m = mat.size(), n = mat[0].size();
    queue<pair<int, int>> q;
    vector<vector<int>> dist(m, vector<int>(n, -1));
    vector<pair<int, int>> dirs = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
    
    // Add all zeros as starting points
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] == 0) {
                q.push({i, j});
                dist[i][j] = 0;
            }
        }
    }
    
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        
        for (auto& [dx, dy] : dirs) {
            int nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && dist[nx][ny] == -1) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    return dist;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 286 | Walls and Gates | [Link](https://leetcode.com/problems/walls-and-gates/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-14-medium-286-walls-and-gates/) |
| 542 | 01 Matrix | [Link](https://leetcode.com/problems/01-matrix/) | - |
| 317 | Shortest Distance from All Buildings | [Link](https://leetcode.com/problems/shortest-distance-from-all-buildings/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/hard-317-shortest-distance-from-all-buildings/) |
| 994 | Rotting Oranges | [Link](https://leetcode.com/problems/rotting-oranges/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-13-medium-994-rotting-oranges/) |

## BFS for Shortest Path

**When to use:** You need the shortest path and all edges have equal weight (or cost = 1 per step). Look for "minimum number of steps," "shortest transformation sequence," or "fewest moves to reach target."

BFS finds shortest path in unweighted graphs -- the first time you reach a node is guaranteed to be via the shortest path.

```cpp
// Shortest path in unweighted graph
int shortestPath(vector<vector<int>>& graph, int start, int target) {
    queue<int> q;
    vector<int> dist(graph.size(), -1);
    
    q.push(start);
    dist[start] = 0;
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        
        if (node == target) {
            return dist[node];
        }
        
        for (int neighbor : graph[node]) {
            if (dist[neighbor] == -1) {
                dist[neighbor] = dist[node] + 1;
                q.push(neighbor);
            }
        }
    }
    
    return -1;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1091 | Shortest Path in Binary Matrix | [Link](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/11/medium-1091-shortest-path-in-binary-matrix/) |
| 127 | Word Ladder | [Link](https://leetcode.com/problems/word-ladder/) | - |
| 433 | Minimum Genetic Mutation | [Link](https://leetcode.com/problems/minimum-genetic-mutation/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/15/medium-433-minimum-genetic-mutation/) |
| 1197 | Minimum Knight Moves | [Link](https://leetcode.com/problems/minimum-knight-moves/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/19/medium-1197-minimum-knight-moves/) |

## Level-order Traversal

**When to use:** The problem asks you to process a tree level by level. Look for "level order," "zigzag order," "vertical order," "right side view," or "cousins in a binary tree."

BFS for tree level-order traversal -- use `q.size()` to process one complete level per iteration.

```cpp
// Binary Tree Level Order Traversal
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int size = q.size();
        vector<int> level;
        
        for (int i = 0; i < size; ++i) {
            TreeNode* node = q.front();
            q.pop();
            level.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        
        result.push_back(level);
    }
    
    return result;
}

// Zigzag Level Order Traversal
vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    bool leftToRight = true;
    
    while (!q.empty()) {
        int size = q.size();
        vector<int> level(size);
        
        for (int i = 0; i < size; ++i) {
            TreeNode* node = q.front();
            q.pop();
            
            int index = leftToRight ? i : size - 1 - i;
            level[index] = node->val;
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        
        result.push_back(level);
        leftToRight = !leftToRight;
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 102 | Binary Tree Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-102-binary-tree-level-order-traversal/) |
| 103 | Binary Tree Zigzag Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/06/medium-103-binary-tree-zigzag-level-order-traversal/) |
| 314 | Binary Tree Vertical Order Traversal | [Link](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-314-binary-tree-vertical-order-traversal/) |
| 429 | N-ary Tree Level Order Traversal | [Link](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-429-n-ary-tree-level-order-traversal/) |
| 993 | Cousins in Binary Tree | [Link](https://leetcode.com/problems/cousins-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/easy-993-cousins-in-binary-tree/) |
| 863 | All Nodes Distance K in Binary Tree | [Link](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-25-medium-863-all-nodes-distance-k-in-binary-tree/) |

## BFS with State

**When to use:** The shortest path depends on more than just position -- you also need to track keys collected, obstacles eliminated, a bitmask of visited nodes, or other extra dimensions. Look for "at most k obstacles," "collect all keys," or "visit all nodes."

BFS when state includes more than just position -- expand the visited array to cover all state dimensions.

```cpp
// BFS with state (e.g., Shortest Path with Obstacle Elimination)
int shortestPath(vector<vector<int>>& grid, int k) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<vector<bool>>> visited(m, vector<vector<bool>>(n, vector<bool>(k + 1, false)));
    queue<vector<int>> q; // {x, y, obstacles_eliminated, steps}
    
    q.push({0, 0, 0, 0});
    visited[0][0][0] = true;
    vector<pair<int, int>> dirs = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
    
    while (!q.empty()) {
        auto state = q.front();
        q.pop();
        int x = state[0], y = state[1], obstacles = state[2], steps = state[3];
        
        if (x == m - 1 && y == n - 1) {
            return steps;
        }
        
        for (auto& [dx, dy] : dirs) {
            int nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
                int newObstacles = obstacles + grid[nx][ny];
                if (newObstacles <= k && !visited[nx][ny][newObstacles]) {
                    visited[nx][ny][newObstacles] = true;
                    q.push({nx, ny, newObstacles, steps + 1});
                }
            }
        }
    }
    
    return -1;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1293 | Shortest Path in a Grid with Obstacles Elimination | [Link](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | - |
| 847 | Shortest Path Visiting All Nodes | [Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | - |

---

## Summary: When to Use Each BFS Pattern

| Pattern | When to Use | Time | Space |
|---|---|---|---|
| **Basic BFS** | Shortest path (unweighted), level-order | $O(V+E)$ | $O(V)$ |
| **Grid BFS** | Grid shortest path, nearest cell | $O(M \times N)$ | $O(M \times N)$ |
| **Multi-source** | Distance from ANY source | $O(M \times N)$ | $O(M \times N)$ |
| **Level-order** | Tree level processing | $O(N)$ | $O(N)$ |
| **BFS + State** | Multiple dimensions (keys, masks) | $O(\text{States})$ | $O(\text{States})$ |

## More templates

- **Graph (Dijkstra, 0-1 BFS, topo):** [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Data structures, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

