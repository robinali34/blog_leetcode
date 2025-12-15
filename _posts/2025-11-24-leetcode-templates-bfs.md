---
layout: post
title: "LeetCode Templates: BFS"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates bfs graph
permalink: /posts/2025-11-24-leetcode-templates-bfs/
tags: [leetcode, templates, bfs, graph, traversal]
---

{% raw %}
## Contents

- [Basic BFS](#basic-bfs)
- [BFS on Grid](#bfs-on-grid)
- [Multi-source BFS](#multi-source-bfs)
- [BFS for Shortest Path](#bfs-for-shortest-path)
- [Level-order Traversal](#level-order-traversal)
- [BFS with State](#bfs-with-state)

## Basic BFS

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

## BFS on Grid

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

Start BFS from multiple sources simultaneously.

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

BFS finds shortest path in unweighted graphs.

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

## Level-order Traversal

BFS for tree level-order traversal.

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
| 102 | Binary Tree Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | - |
| 103 | Binary Tree Zigzag Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | - |
| 314 | Binary Tree Vertical Order Traversal | [Link](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-314-binary-tree-vertical-order-traversal/) |

## BFS with State

BFS when state includes more than just position.

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
{% endraw %}

