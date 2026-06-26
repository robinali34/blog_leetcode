---
layout: post
title: "Algorithm Templates: DFS"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates dfs graph
permalink: /posts/2025-11-24-leetcode-templates-dfs/
tags: [leetcode, templates, dfs, graph, traversal]
---

{% raw %}
**Depth-First Search (DFS)** is one of the most fundamental graph traversal algorithms. It works by starting at a node and exploring as far down each branch as possible before backtracking — making it ideal for problems involving reachability, connected components, paths, and tree structure. This page collects ready-to-use C++ templates for the most common DFS patterns you'll encounter on LeetCode. See also [Graph](/posts/2025-10-29-leetcode-templates-graph/) and [Backtracking](/posts/2025-11-24-leetcode-templates-backtracking/).

> **New to DFS?** DFS explores as deep as possible before backtracking. Think of it like exploring a maze — go straight until you hit a dead end, then back up and try the next turn.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 310" width="520" height="310" style="max-width:100%;">
  <style>
    .node{fill:#D4D8D0;stroke:#B8B5B0;stroke-width:2}
    .visited{fill:#E8D5D0;stroke:#B8B5B0;stroke-width:2}
    .current{fill:#D4D8E0;stroke:#B8B5B0;stroke-width:2.5}
    .edge{stroke:#B8B5B0;stroke-width:2;fill:none}
    .label{font:bold 14px sans-serif;fill:#3A3530;text-anchor:middle;dominant-baseline:central}
    .order{font:11px sans-serif;fill:#5A5752;text-anchor:middle}
    .title{font:bold 13px sans-serif;fill:#5A5752;text-anchor:middle}
    .stk{fill:#D4D8E0;stroke:#B8B5B0;stroke-width:1.5}
    .stklbl{font:12px monospace;fill:#3A3530;text-anchor:middle;dominant-baseline:central}
  </style>
  <!-- Title -->
  <text x="180" y="18" class="title">DFS Traversal Order</text>
  <!-- Edges -->
  <line x1="180" y1="55" x2="110" y2="115" class="edge"/>
  <line x1="180" y1="55" x2="250" y2="115" class="edge"/>
  <line x1="110" y1="135" x2="65" y2="195" class="edge"/>
  <line x1="110" y1="135" x2="155" y2="195" class="edge"/>
  <line x1="250" y1="135" x2="250" y2="195" class="edge"/>
  <!-- Nodes: visited=E8D5D0, current=D4D8E0 -->
  <circle cx="180" cy="45" r="20" class="visited"/>
  <text x="180" y="45" class="label">1</text>
  <text x="180" y="75" class="order">①</text>
  <circle cx="110" cy="125" r="20" class="visited"/>
  <text x="110" y="125" class="label">2</text>
  <text x="110" y="155" class="order">②</text>
  <circle cx="250" cy="125" r="20" class="node"/>
  <text x="250" y="125" class="label">3</text>
  <text x="250" y="155" class="order">⑤</text>
  <circle cx="65" cy="205" r="20" class="visited"/>
  <text x="65" y="205" class="label">4</text>
  <text x="65" y="235" class="order">③</text>
  <circle cx="155" cy="205" r="20" class="current"/>
  <text x="155" y="205" class="label">5</text>
  <text x="155" y="235" class="order">④</text>
  <circle cx="250" cy="205" r="20" class="node"/>
  <text x="250" y="205" class="label">6</text>
  <text x="250" y="235" class="order">⑥</text>
  <!-- Stack visualization -->
  <text x="420" y="18" class="title">Stack</text>
  <rect x="390" y="28" width="60" height="28" rx="4" class="stk"/>
  <text x="420" y="42" class="stklbl">3</text>
  <rect x="390" y="60" width="60" height="28" rx="4" class="stk"/>
  <text x="420" y="74" class="stklbl">5 ←</text>
  <text x="420" y="108" class="order">top of stack</text>
  <!-- Legend -->
  <rect x="360" y="145" width="16" height="16" rx="3" class="visited"/>
  <text x="385" y="155" style="font:12px sans-serif;fill:#5A5752" dominant-baseline="central">Visited</text>
  <rect x="360" y="170" width="16" height="16" rx="3" class="current"/>
  <text x="385" y="180" style="font:12px sans-serif;fill:#5A5752" dominant-baseline="central">Processing</text>
  <rect x="360" y="195" width="16" height="16" rx="3" class="node"/>
  <text x="385" y="205" style="font:12px sans-serif;fill:#5A5752" dominant-baseline="central">Unvisited</text>
  <!-- Arrow showing the "go deep" path -->
  <text x="420" y="260" class="order">DFS goes deep</text>
  <text x="420" y="278" class="order">before going wide</text>
</svg>
</div>

## Contents

- [Basic DFS](#basic-dfs)
- [DFS on Grid](#dfs-on-grid)
- [DFS on Tree](#dfs-on-tree)
- [DFS with Memoization](#dfs-with-memoization)
- [Iterative DFS](#iterative-dfs)

## Basic DFS

Depth-First Search explores as far as possible before backtracking.

**When to use:** Checking reachability between nodes, finding connected components, or exploring all paths in a general graph.

```cpp
// DFS on graph (adjacency list)
void dfs(vector<vector<int>>& graph, int node, vector<bool>& visited) {
    visited[node] = true;
    
    // Process node
    cout << node << " ";
    
    // Explore neighbors
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(graph, neighbor, visited);
        }
    }
}

// DFS with return value
bool dfs(vector<vector<int>>& graph, int node, int target, vector<bool>& visited) {
    if (node == target) return true;
    visited[node] = true;
    
    for (int neighbor : graph[node]) {
        if (!visited[neighbor] && dfs(graph, neighbor, target, visited)) {
            return true;
        }
    }
    
    return false;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 841 | Keys and Rooms | [Link](https://leetcode.com/problems/keys-and-rooms/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/12/medium-841-keys-and-rooms/) |

## DFS on Grid

DFS for 2D grid problems (connected components, paths).

**When to use:** Flood-fill problems, island counting, or any task where you explore connected cells in a 2D matrix.

```cpp
// DFS on 2D grid (4-directional)
void dfsGrid(vector<vector<char>>& grid, int i, int j) {
    int m = grid.size(), n = grid[0].size();
    
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1') {
        return;
    }
    
    grid[i][j] = '0'; // Mark as visited
    
    // Explore 4 directions
    dfsGrid(grid, i + 1, j);
    dfsGrid(grid, i - 1, j);
    dfsGrid(grid, i, j + 1);
    dfsGrid(grid, i, j - 1);
}

// Number of Islands using DFS
int numIslands(vector<vector<char>>& grid) {
    int m = grid.size(), n = grid[0].size();
    int count = 0;
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == '1') {
                count++;
                dfsGrid(grid, i, j);
            }
        }
    }
    
    return count;
}

// Word Search
bool dfsWordSearch(vector<vector<char>>& board, int i, int j, string& word, int idx) {
    if (idx == word.size()) return true;
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size()) return false;
    if (board[i][j] != word[idx]) return false;
    
    char temp = board[i][j];
    board[i][j] = '#'; // Mark as visited
    
    vector<pair<int, int>> dirs = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
    for (auto& [dx, dy] : dirs) {
        if (dfsWordSearch(board, i + dx, j + dy, word, idx + 1)) {
            return true;
        }
    }
    
    board[i][j] = temp; // Backtrack
    return false;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-20-medium-200-number-of-islands/) |
| 79 | Word Search | [Link](https://leetcode.com/problems/word-search/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/medium-79-word-search/) |
| 695 | Max Area of Island | [Link](https://leetcode.com/problems/max-area-of-island/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-695-max-area-of-island/) |
| 133 | Clone Graph | [Link](https://leetcode.com/problems/clone-graph/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-133-clone-graph/) |
| 417 | Pacific Atlantic Water Flow | [Link](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-417-pacific-atlantic-water-flow/) |
| 323 | Number of Connected Components | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-323-number-of-connected-components-in-an-undirected-graph/) |
| 547 | Number of Provinces | [Link](https://leetcode.com/problems/number-of-provinces/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-18-medium-547-number-of-provinces/) |

## DFS on Tree

DFS for tree problems (preorder, inorder, postorder).

**When to use:** Tree traversals, path-sum problems, computing tree height/diameter, or any recursive tree decomposition.

```cpp
// Preorder DFS
void preorder(TreeNode* root, vector<int>& result) {
    if (!root) return;
    result.push_back(root->val);
    preorder(root->left, result);
    preorder(root->right, result);
}

// Inorder DFS
void inorder(TreeNode* root, vector<int>& result) {
    if (!root) return;
    inorder(root->left, result);
    result.push_back(root->val);
    inorder(root->right, result);
}

// Postorder DFS
void postorder(TreeNode* root, vector<int>& result) {
    if (!root) return;
    postorder(root->left, result);
    postorder(root->right, result);
    result.push_back(root->val);
}

// Path Sum
bool hasPathSum(TreeNode* root, int targetSum) {
    if (!root) return false;
    if (!root->left && !root->right) {
        return root->val == targetSum;
    }
    return hasPathSum(root->left, targetSum - root->val) ||
           hasPathSum(root->right, targetSum - root->val);
}

// Sum Root to Leaf Numbers
int sumNumbers(TreeNode* root, int sum = 0) {
    if (!root) return 0;
    sum = sum * 10 + root->val;
    if (!root->left && !root->right) return sum;
    return sumNumbers(root->left, sum) + sumNumbers(root->right, sum);
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 100 | Same Tree | [Link](https://leetcode.com/problems/same-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-100-same-tree/) |
| 101 | Symmetric Tree | [Link](https://leetcode.com/problems/symmetric-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-101-symmetric-tree/) |
| 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-104-maximum-depth-of-binary-tree/) |
| 111 | Minimum Depth of Binary Tree | [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-111-minimum-depth-of-binary-tree/) |
| 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-112-path-sum/) |
| 129 | Sum Root to Leaf Numbers | [Link](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-129-sum-root-to-leaf-numbers/) |
| 226 | Invert Binary Tree | [Link](https://leetcode.com/problems/invert-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-226-invert-binary-tree/) |
| 236 | Lowest Common Ancestor | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/medium-236-lowest-common-ancestor-of-a-binary-tree/) |
| 437 | Path Sum III | [Link](https://leetcode.com/problems/path-sum-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-437-path-sum-iii/) |
| 690 | Employee Importance | [Link](https://leetcode.com/problems/employee-importance/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-16-medium-690-employee-importance/) |

## DFS with Memoization

DFS with caching to avoid recomputation.

**When to use:** Problems with overlapping subproblems on graphs or grids, such as longest increasing path or counting distinct paths.

```cpp
// DFS with memoization (e.g., Longest Increasing Path)
int dfsWithMemo(vector<vector<int>>& matrix, int i, int j, 
                vector<vector<int>>& memo, int prev) {
    int m = matrix.size(), n = matrix[0].size();
    
    if (i < 0 || i >= m || j < 0 || j >= n || matrix[i][j] <= prev) {
        return 0;
    }
    
    if (memo[i][j] != -1) {
        return memo[i][j];
    }
    
    int result = 1;
    vector<pair<int, int>> dirs = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
    
    for (auto& [dx, dy] : dirs) {
        result = max(result, 1 + dfsWithMemo(matrix, i + dx, j + dy, 
                                              memo, matrix[i][j]));
    }
    
    memo[i][j] = result;
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 329 | Longest Increasing Path in a Matrix | [Link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/18/hard-329-longest-increasing-path-in-a-matrix/) |

## Iterative DFS

DFS using stack instead of recursion.

**When to use:** When the recursion depth might cause a stack overflow, or when you need explicit control over the traversal order.

```cpp
// Iterative DFS on graph
void dfsIterative(vector<vector<int>>& graph, int start) {
    stack<int> st;
    vector<bool> visited(graph.size(), false);
    
    st.push(start);
    
    while (!st.empty()) {
        int node = st.top();
        st.pop();
        
        if (visited[node]) continue;
        visited[node] = true;
        
        // Process node
        cout << node << " ";
        
        // Push neighbors in reverse order to maintain order
        for (int i = graph[node].size() - 1; i >= 0; --i) {
            if (!visited[graph[node][i]]) {
                st.push(graph[node][i]);
            }
        }
    }
}

// Iterative DFS on tree
vector<int> preorderIterative(TreeNode* root) {
    vector<int> result;
    if (!root) return result;
    
    stack<TreeNode*> st;
    st.push(root);
    
    while (!st.empty()) {
        TreeNode* node = st.top();
        st.pop();
        result.push_back(node->val);
        
        if (node->right) st.push(node->right);
        if (node->left) st.push(node->left);
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 144 | Binary Tree Preorder Traversal | [Link](https://leetcode.com/problems/binary-tree-preorder-traversal/) | - |
| 94 | Binary Tree Inorder Traversal | [Link](https://leetcode.com/problems/binary-tree-inorder-traversal/) | - |

## Pattern Comparison

| Pattern | When to Use | Time | Space |
|---|---|---|---|
| Basic DFS | Reachability, connected components | O(V+E) | O(V) |
| Grid DFS | Flood fill, island counting | O(M×N) | O(M×N) |
| Tree DFS | All tree traversals, path problems | O(N) | O(H) |
| DFS + Memo | Overlapping subproblems on graphs/grids | O(States) | O(States) |
| Iterative | When recursion stack overflows | O(V+E) | O(V) |

## DFS vs BFS

> **When should you pick DFS over BFS (or vice versa)?**
>
> - **Use DFS** when you need to explore all paths, check connectivity, detect cycles, or solve problems that decompose recursively (e.g., tree shape, backtracking). DFS is also more memory-efficient on narrow/deep structures.
> - **Use BFS** when you need the **shortest path in an unweighted graph**, want to process nodes level by level, or need the minimum number of steps to reach a target.
> - **Rule of thumb:** If the problem says "shortest" or "minimum steps," reach for BFS. If it says "all paths," "connected," or "exists," DFS is usually the natural fit.

## More templates

- **Graph, Backtracking:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Backtracking](/posts/2025-11-24-leetcode-templates-backtracking/)
- **Data structures, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

