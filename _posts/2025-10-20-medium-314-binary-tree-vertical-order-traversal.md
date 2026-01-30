---
layout: post
title: "314. Binary Tree Vertical Order Traversal"
date: 2025-10-20 15:00:00 -0700
categories: [leetcode, medium, tree, bfs, vertical-order]
permalink: /2025/10/20/medium-314-binary-tree-vertical-order-traversal/
---

# 314. Binary Tree Vertical Order Traversal

## Problem Statement

Given the root of a binary tree, return the **vertical order traversal** of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from **left to right**.

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9
Column  0: Nodes 3 and 15
Column  1: Only node 20
Column  2: Only node 7
```

**Example 2:**
```
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
```

**Example 3:**
```
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Vertical order definition**: What is vertical order? (Assumption: Nodes at same horizontal distance from root are in same column - left is negative, right is positive)

2. **Column ordering**: How should columns be ordered? (Assumption: From leftmost to rightmost - negative to positive column indices)

3. **Same column ordering**: How should nodes in same column be ordered? (Assumption: Top to bottom - level order within same column)

4. **Return format**: What should we return? (Assumption: List of lists - each inner list contains nodes in one column, ordered left to right)

5. **Empty tree**: What if tree is empty? (Assumption: Return empty list - no nodes to traverse)

## Solution Approach

This problem requires traversing a binary tree in **vertical order** (column by column from left to right). The key insight is to assign **column indices** to nodes and group them accordingly.

### Key Insights:

1. **Column assignment**: Root gets column 0, left child gets `column - 1`, right child gets `column + 1`
2. **Level order**: Use BFS to maintain top-to-bottom order within each column
3. **Grouping**: Use a map to group nodes by their column index
4. **Ordering**: Process columns from left to right (sorted by column index)

### Algorithm:

1. **BFS with column tracking**: Use queue to store `(node, column)` pairs
2. **Column mapping**: Use `map<int, vector<int>>` to group nodes by column
3. **Level-by-level**: Process nodes level by level to maintain top-to-bottom order
4. **Result construction**: Convert map to result vector in column order

## Solution

### **Solution: BFS with Column Tracking**

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> rtn;
        if(!root) return rtn;
        map<int, vector<int>> map;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        while(!q.empty()) {
            int size = q.size();
            for(int i = 0; i < (int)q.size(); i++) {
                TreeNode* curr = q.front().first;
                int dir = q.front().second;
                q.pop();
                map[dir].push_back(curr->val);
                if(curr->left) q.push({curr->left, dir - 1});
                if(curr->right) q.push({curr->right, dir + 1});
            }
        }
        for(auto& [node, vals]: map) {
            rtn.push_back(vals);
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize**: Create empty result vector and map for column grouping
2. **BFS setup**: Start with root at column 0
3. **Level processing**: For each level, process all nodes at that level
4. **Column assignment**: 
   - Left child: `column - 1`
   - Right child: `column + 1`
5. **Grouping**: Add node values to their respective columns
6. **Result construction**: Convert map to result vector in sorted column order

### **Example Walkthrough:**

**For `root = [3,9,20,null,null,15,7]`:**

```
Tree structure:
    3
   / \
  9   20
     /  \
    15   7

Column assignment:
    3 (col=0)
   / \
  9   20
(col=-1) (col=1)
     /  \
    15   7
(col=0) (col=2)

BFS Process:
Level 0: [(3,0)] → map[0] = [3]
Level 1: [(9,-1), (20,1)] → map[-1] = [9], map[1] = [20]
Level 2: [(15,0), (7,2)] → map[0] = [3,15], map[2] = [7]

Final map: {-1: [9], 0: [3,15], 1: [20], 2: [7]}
Result: [[9], [3,15], [20], [7]]
```

## Complexity Analysis

### **Time Complexity:** O(n log n)
- **BFS traversal**: O(n) - visit each node once
- **Map operations**: O(log n) per insertion (map is sorted)
- **Total**: O(n log n)

### **Space Complexity:** O(n)
- **Queue**: O(n) - maximum width of tree
- **Map**: O(n) - stores all node values
- **Result**: O(n) - output vector
- **Total**: O(n)

## Key Points

1. **BFS for level order**: Maintains top-to-bottom order within columns
2. **Column tracking**: Use integer column indices for grouping
3. **Map for grouping**: Automatically sorts columns from left to right
4. **Level-by-level processing**: Ensures proper ordering within columns
5. **Edge case handling**: Return empty vector for null root

## Alternative Approaches

### **DFS Approach (Not Recommended)**
```cpp
class Solution {
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        map<int, vector<pair<int, int>>> map; // column -> [(row, val)]
        dfs(root, 0, 0, map);
        
        vector<vector<int>> result;
        for(auto& [col, nodes] : map) {
            sort(nodes.begin(), nodes.end()); // Sort by row, then by val
            vector<int> vals;
            for(auto& [row, val] : nodes) {
                vals.push_back(val);
            }
            result.push_back(vals);
        }
        return result;
    }
    
private:
    void dfs(TreeNode* node, int row, int col, map<int, vector<pair<int, int>>>& map) {
        if(!node) return;
        map[col].push_back({row, node->val});
        dfs(node->left, row + 1, col - 1, map);
        dfs(node->right, row + 1, col + 1, map);
    }
};
```

**Why BFS is better:**
- **Natural ordering**: BFS maintains level order automatically
- **Simpler code**: No need to sort by row
- **Better performance**: O(n log n) vs O(n log n + sorting)

## Related Problems

- [987. Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) - More complex ordering rules
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Level order traversal
- [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) - Right view traversal

## Tags

`Tree`, `BFS`, `Vertical Order`, `Level Order`, `Medium`
