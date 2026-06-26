---
layout: post
title: "Algorithm Templates: DFS"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates dfs graph
permalink: /posts/2025-11-24-leetcode-templates-dfs/
tags: [leetcode, templates, dfs, graph, traversal]
---
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

<svg viewBox="0 0 570 340" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="185" y="28" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">DFS flood fill on a grid</text>
  <text x="89" y="46" font-size="9" fill="#9A9792" text-anchor="middle">0</text>
  <text x="140" y="46" font-size="9" fill="#9A9792" text-anchor="middle">1</text>
  <text x="191" y="46" font-size="9" fill="#9A9792" text-anchor="middle">2</text>
  <text x="242" y="46" font-size="9" fill="#9A9792" text-anchor="middle">3</text>
  <text x="293" y="46" font-size="9" fill="#9A9792" text-anchor="middle">4</text>
  <!-- Row 0: 1* 1* 0 0 0 — island 1 being flood-filled -->
  <rect x="65" y="52" width="48" height="48" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="89" y="77" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <text x="89" y="93" font-size="9" fill="#5A5752" text-anchor="middle">①</text>
  <rect x="116" y="52" width="48" height="48" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="140" y="77" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <text x="140" y="93" font-size="9" fill="#5A5752" text-anchor="middle">②</text>
  <rect x="167" y="52" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="191" y="81" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="218" y="52" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="242" y="81" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="269" y="52" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="293" y="81" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <!-- Row 1: 0 1* 0 0 0 -->
  <rect x="65" y="103" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="89" y="132" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="116" y="103" width="48" height="48" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="140" y="128" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <text x="140" y="144" font-size="9" fill="#5A5752" text-anchor="middle">③</text>
  <rect x="167" y="103" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="191" y="132" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="218" y="103" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="242" y="132" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="269" y="103" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="293" y="132" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <!-- Row 2: 0 0 0 1 1 — island 2 (not yet explored) -->
  <rect x="65" y="154" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="89" y="183" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="116" y="154" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="140" y="183" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="167" y="154" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="191" y="183" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="218" y="154" width="48" height="48" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="242" y="183" font-size="13" fill="#3A3530" font-weight="600" text-anchor="middle">1</text>
  <rect x="269" y="154" width="48" height="48" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="293" y="183" font-size="13" fill="#3A3530" font-weight="600" text-anchor="middle">1</text>
  <!-- Row 3: 0 0 0 1 0 -->
  <rect x="65" y="205" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="89" y="234" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="116" y="205" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="140" y="234" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="167" y="205" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="191" y="234" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="218" y="205" width="48" height="48" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="242" y="234" font-size="13" fill="#3A3530" font-weight="600" text-anchor="middle">1</text>
  <rect x="269" y="205" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="293" y="234" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <!-- Row 4: 0 0 0 0 0 -->
  <rect x="65" y="256" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="89" y="285" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="116" y="256" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="140" y="285" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="167" y="256" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="191" y="285" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="218" y="256" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="242" y="285" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <rect x="269" y="256" width="48" height="48" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="293" y="285" font-size="13" fill="#B8B5B0" font-weight="600" text-anchor="middle">0</text>
  <!-- DFS exploration arrows -->
  <defs><marker id="dfs-arrow" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0,0 7,2.5 0,5" fill="#8B8680"/></marker></defs>
  <line x1="103" y1="76" x2="126" y2="76" stroke="#8B8680" stroke-width="2" marker-end="url(#dfs-arrow)"/>
  <line x1="140" y1="93" x2="140" y2="113" stroke="#8B8680" stroke-width="2" marker-end="url(#dfs-arrow)"/>
  <!-- Annotations -->
  <text x="370" y="72" font-size="11" fill="#5A5752" font-weight="600">DFS flood fill</text>
  <text x="370" y="90" font-size="10" fill="#7A7772">Start at (0,0), explore</text>
  <text x="370" y="104" font-size="10" fill="#7A7772">all connected 1s:</text>
  <text x="370" y="128" font-size="10" fill="#5A5752">① (0,0) → go right</text>
  <text x="370" y="144" font-size="10" fill="#5A5752">② (0,1) → go down</text>
  <text x="370" y="160" font-size="10" fill="#5A5752">③ (1,1) → no more 1s</text>
  <text x="370" y="176" font-size="10" fill="#7A7772" font-style="italic">Backtrack → island done!</text>
  <!-- Legend -->
  <rect x="370" y="206" width="14" height="14" rx="3" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="390" y="217" font-size="10" fill="#5A5752">Explored (flood fill)</text>
  <rect x="370" y="226" width="14" height="14" rx="3" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="390" y="237" font-size="10" fill="#5A5752">Land (not yet visited)</text>
  <rect x="370" y="246" width="14" height="14" rx="3" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1"/>
  <text x="390" y="257" font-size="10" fill="#5A5752">Water (0)</text>
  <text x="370" y="286" font-size="10" fill="#7A7772" font-style="italic">Grid has 2 islands.</text>
  <text x="370" y="300" font-size="10" fill="#7A7772" font-style="italic">DFS marks each connected</text>
  <text x="370" y="314" font-size="10" fill="#7A7772" font-style="italic">component of 1s.</text>
</svg>

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

<svg viewBox="0 0 660 290" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="160" y="22" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">DFS with memoization — Longest Increasing Path</text>
  <!-- Column labels -->
  <text x="95" y="50" font-size="9" fill="#9A9792" text-anchor="middle">col 0</text>
  <text x="170" y="50" font-size="9" fill="#9A9792" text-anchor="middle">col 1</text>
  <text x="245" y="50" font-size="9" fill="#9A9792" text-anchor="middle">col 2</text>
  <!-- Row 0: 9 9 4 | memo: 1 1 2 -->
  <rect x="60" y="60" width="70" height="52" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="95" y="84" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">9</text>
  <text x="95" y="104" font-size="9" fill="#5A5752" text-anchor="middle">memo=1</text>
  <rect x="135" y="60" width="70" height="52" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="170" y="84" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">9</text>
  <text x="170" y="104" font-size="9" fill="#7A7772" text-anchor="middle">memo=1</text>
  <rect x="210" y="60" width="70" height="52" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="245" y="84" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">4</text>
  <text x="245" y="104" font-size="9" fill="#7A7772" text-anchor="middle">memo=2</text>
  <!-- Row 1: 6 6 8 | memo: 2 2 1 -->
  <rect x="60" y="117" width="70" height="52" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="95" y="141" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">6</text>
  <text x="95" y="161" font-size="9" fill="#5A5752" text-anchor="middle">memo=2</text>
  <rect x="135" y="117" width="70" height="52" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="170" y="141" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">6</text>
  <text x="170" y="161" font-size="9" fill="#7A7772" text-anchor="middle">memo=2</text>
  <rect x="210" y="117" width="70" height="52" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="245" y="141" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">8</text>
  <text x="245" y="161" font-size="9" fill="#7A7772" text-anchor="middle">memo=1</text>
  <!-- Row 2: 2 1 1 | memo: 3 4 2 -->
  <rect x="60" y="174" width="70" height="52" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="95" y="198" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">2</text>
  <text x="95" y="218" font-size="9" fill="#5A5752" text-anchor="middle">memo=3</text>
  <rect x="135" y="174" width="70" height="52" rx="5" fill="#D4D8E0" stroke="#8B8680" stroke-width="2.5"/>
  <text x="170" y="198" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <text x="170" y="218" font-size="9" fill="#3A3530" font-weight="600" text-anchor="middle">memo=4 ★</text>
  <rect x="210" y="174" width="70" height="52" rx="5" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="245" y="198" font-size="16" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <text x="245" y="218" font-size="9" fill="#7A7772" text-anchor="middle">memo=2</text>
  <!-- Path arrows: (2,1)→(2,0)→(1,0)→(0,0) -->
  <defs><marker id="memo-arrow" markerWidth="7" markerHeight="5" refX="6" refY="2.5" orient="auto"><polygon points="0,0 7,2.5 0,5" fill="#8B8680"/></marker></defs>
  <line x1="145" y1="200" x2="135" y2="200" stroke="#8B8680" stroke-width="2.5" marker-end="url(#memo-arrow)"/>
  <line x1="95" y1="178" x2="95" y2="172" stroke="#8B8680" stroke-width="2.5" marker-end="url(#memo-arrow)"/>
  <line x1="95" y1="122" x2="95" y2="116" stroke="#8B8680" stroke-width="2.5" marker-end="url(#memo-arrow)"/>
  <!-- Explanation -->
  <text x="330" y="72" font-size="11" fill="#5A5752" font-weight="600">Longest increasing path</text>
  <text x="330" y="92" font-size="11" fill="#3A3530" font-weight="700">1 → 2 → 6 → 9</text>
  <text x="330" y="108" font-size="10" fill="#7A7772">(length 4, shown with arrows)</text>
  <text x="330" y="138" font-size="10" fill="#5A5752" font-weight="600">How memo works:</text>
  <text x="330" y="156" font-size="10" fill="#7A7772">memo[r][c] = length of the</text>
  <text x="330" y="170" font-size="10" fill="#7A7772">longest path starting from (r,c)</text>
  <text x="330" y="196" font-size="10" fill="#5A5752">DFS from cell 1 at (2,1):</text>
  <text x="330" y="212" font-size="10" fill="#7A7772">→ can go to 2: 1+memo[2][0]</text>
  <text x="330" y="226" font-size="10" fill="#7A7772">→ memo[2][0]=3 (2→6→9)</text>
  <text x="330" y="240" font-size="10" fill="#7A7772">→ so memo[2][1] = 1+3 = 4</text>
  <!-- Legend -->
  <rect x="330" y="258" width="14" height="14" rx="3" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="350" y="269" font-size="10" fill="#5A5752">On longest path</text>
  <rect x="460" y="258" width="14" height="14" rx="3" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="480" y="269" font-size="10" fill="#5A5752">Path start (max memo)</text>
</svg>

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

<svg viewBox="0 0 700 270" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- DFS side -->
  <text x="170" y="22" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">DFS — Goes deep first</text>
  <!-- DFS highlighted path A→B→D -->
  <line x1="170" y1="58" x2="110" y2="118" stroke="#E8D5D0" stroke-width="8" stroke-linecap="round"/>
  <line x1="110" y1="128" x2="75" y2="188" stroke="#E8D5D0" stroke-width="8" stroke-linecap="round"/>
  <!-- DFS edges -->
  <line x1="170" y1="55" x2="110" y2="120" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="170" y1="55" x2="230" y2="120" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="110" y1="130" x2="75" y2="190" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="110" y1="130" x2="145" y2="190" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="230" y1="130" x2="230" y2="190" stroke="#B8B5B0" stroke-width="2"/>
  <!-- DFS nodes -->
  <circle cx="170" cy="50" r="18" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="170" y="55" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">A</text>
  <circle cx="110" cy="125" r="18" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="110" y="130" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">B</text>
  <circle cx="230" cy="125" r="18" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="230" y="130" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">C</text>
  <circle cx="75" cy="195" r="18" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="75" y="200" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">D</text>
  <circle cx="145" cy="195" r="18" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="145" y="200" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">E</text>
  <circle cx="230" cy="195" r="18" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="230" y="200" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">F</text>
  <!-- DFS visit order -->
  <text x="192" y="44" font-size="9" fill="#5A5752">①</text>
  <text x="132" y="118" font-size="9" fill="#5A5752">②</text>
  <text x="97" y="188" font-size="9" fill="#5A5752">③</text>
  <text x="167" y="188" font-size="9" fill="#7A7772">④</text>
  <text x="252" y="118" font-size="9" fill="#7A7772">⑤</text>
  <text x="252" y="188" font-size="9" fill="#7A7772">⑥</text>
  <!-- DFS deep arrow -->
  <path d="M 30 60 L 30 200" fill="none" stroke="#8B8680" stroke-width="1.5" stroke-dasharray="4,3"/>
  <polygon points="26,198 34,198 30,208" fill="#8B8680"/>
  <text x="30" y="228" font-size="10" fill="#5A5752" text-anchor="middle" font-style="italic">deep</text>
  <!-- Separator -->
  <line x1="345" y1="15" x2="345" y2="250" stroke="#E8E3D8" stroke-width="1.5" stroke-dasharray="5,4"/>
  <text x="345" y="260" font-size="10" fill="#9A9792" text-anchor="middle">vs</text>
  <!-- BFS side -->
  <text x="530" y="22" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">BFS — Goes wide first</text>
  <!-- BFS level highlight band -->
  <rect x="435" y="107" width="190" height="38" rx="8" fill="#D4D8E0" fill-opacity="0.4"/>
  <text x="640" y="130" font-size="9" fill="#5A5752" font-style="italic">level 1</text>
  <!-- BFS edges -->
  <line x1="530" y1="55" x2="470" y2="120" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="530" y1="55" x2="590" y2="120" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="470" y1="130" x2="435" y2="190" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="470" y1="130" x2="505" y2="190" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="590" y1="130" x2="590" y2="190" stroke="#B8B5B0" stroke-width="2"/>
  <!-- BFS nodes -->
  <circle cx="530" cy="50" r="18" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="530" y="55" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">A</text>
  <circle cx="470" cy="125" r="18" fill="#D4D8E0" stroke="#8B8680" stroke-width="2"/>
  <text x="470" y="130" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">B</text>
  <circle cx="590" cy="125" r="18" fill="#D4D8E0" stroke="#8B8680" stroke-width="2"/>
  <text x="590" y="130" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">C</text>
  <circle cx="435" cy="195" r="18" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="435" y="200" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">D</text>
  <circle cx="505" cy="195" r="18" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="505" y="200" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">E</text>
  <circle cx="590" cy="195" r="18" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="590" y="200" font-size="13" fill="#3A3530" font-weight="700" text-anchor="middle">F</text>
  <!-- BFS visit order -->
  <text x="552" y="44" font-size="9" fill="#5A5752">①</text>
  <text x="492" y="118" font-size="9" fill="#5A5752">②</text>
  <text x="612" y="118" font-size="9" fill="#5A5752">③</text>
  <text x="457" y="188" font-size="9" fill="#7A7772">④</text>
  <text x="527" y="188" font-size="9" fill="#7A7772">⑤</text>
  <text x="612" y="188" font-size="9" fill="#7A7772">⑥</text>
  <!-- BFS wide arrow -->
  <path d="M 420 240 L 630 240" fill="none" stroke="#8B8680" stroke-width="1.5" stroke-dasharray="4,3"/>
  <polygon points="628,236 628,244 638,240" fill="#8B8680"/>
  <text x="530" y="258" font-size="10" fill="#5A5752" text-anchor="middle" font-style="italic">wide</text>
</svg>

## More templates

- **Graph, Backtracking:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Backtracking](/posts/2025-11-24-leetcode-templates-backtracking/)
- **Data structures, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
