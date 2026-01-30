---
layout: post
title: "102. Binary Tree Level Order Traversal"
date: 2026-01-07 00:00:00 -0700
categories: [leetcode, medium, tree, bfs, binary-tree]
permalink: /2026/01/07/medium-102-binary-tree-level-order-traversal/
tags: [leetcode, medium, tree, bfs, level-order-traversal, binary-tree]
---

# 102. Binary Tree Level Order Traversal

## Problem Statement

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Explanation:
Level 0: [3]
Level 1: [9, 20]
Level 2: [15, 7]
```

**Example 2:**
```
Input: root = [1]
Output: [[1]]
```

**Example 3:**
```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Level definition**: How are levels defined? (Assumption: Level 0 is root, level 1 is root's children, etc. - BFS levels)

2. **Output format**: How should we represent the result? (Assumption: List of lists - each inner list represents one level, nodes in left-to-right order)

3. **Empty tree**: What should we return for an empty tree? (Assumption: Return empty list [])

4. **Traversal order**: Should nodes at the same level be in any specific order? (Assumption: Left to right - process left child before right child)

5. **Tree modification**: Should we modify the tree or just traverse it? (Assumption: Just traverse - no modification needed)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to traverse tree level by level. Let me use DFS and track levels."

**Naive Solution**: Use DFS with level tracking. Store nodes by level in map, then convert to result.

**Complexity**: O(n) time, O(n) space

**Issues**:
- DFS doesn't naturally maintain level order
- Need to sort levels or use map
- Doesn't leverage BFS naturally
- Can be optimized

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "BFS naturally processes nodes level by level."

**Improved Solution**: Use BFS (queue). Process nodes level by level. For each level, process all nodes at that level, add to result.

**Complexity**: O(n) time, O(n) space

**Improvements**:
- BFS naturally maintains level order
- O(n) time is optimal
- Clean and intuitive
- Handles all cases correctly

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "BFS approach is optimal. Track level size to process level by level."

**Best Solution**: BFS approach is optimal. Use queue, track level size, process all nodes at current level before moving to next level.

**Complexity**: O(n) time, O(n) space

**Key Realizations**:
1. BFS is perfect for level-order traversal
2. O(n) time is optimal - visit each node once
3. Level size tracking enables level-by-level processing
4. O(n) space for queue is necessary

## Solution Approach

This is a classic **BFS (Breadth-First Search)** problem. The key insight is to:
1. Use a queue to traverse the tree level by level
2. Process all nodes at the current level before moving to the next
3. Track the level size to know when we've processed all nodes at a level

### Key Insights:

1. **Level-by-Level Processing**: Process all nodes at the current level before moving to the next
2. **Queue for BFS**: Use a queue to maintain the order of nodes to be processed
3. **Level Size Tracking**: Store the queue size before processing a level to know how many nodes belong to that level
4. **Children Order**: Always add left child first, then right child to maintain left-to-right order

### Algorithm:

1. **Initialize**: Create result vector and queue, push root if it exists
2. **For each level**:
   - Get current level size (number of nodes at this level)
   - Process all nodes at current level
   - Add their values to the level vector
   - Add their children to the queue for next level
3. **Return**: Result vector containing all levels

## Solution

### **Solution: BFS with Queue**

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> rtn;
        if(!root) return rtn;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()) {
            int levelSize = q.size();
            vector<int> level;
            level.reserve(levelSize);
            for(int i = 0; i < levelSize; i++) {
                TreeNode* curr = q.front();
                q.pop();
                level.push_back(curr->val);
                if(curr->left) q.push(curr->left);
                if(curr->right) q.push(curr->right);
            }
            rtn.push_back(level);
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 3-5)**:
   - Create empty result vector
   - Return empty result if root is null
   - Initialize queue and push root node

2. **Level Processing (Lines 6-18)**:
   - **For each level**:
     - **Get level size** (Line 7): Store `q.size()` before processing - this is the number of nodes at current level
     - **Create level vector** (Line 8): Pre-allocate space with `reserve()` for efficiency
     - **Process each node at current level** (Lines 9-15):
       - Remove node from front of queue
       - Add node value to level vector
       - Add left child to queue if it exists
       - Add right child to queue if it exists
     - **Add completed level** (Line 17): Push level vector to result

3. **Return (Line 19)**: Return the level order traversal

### **Why This Works:**

- **Queue maintains order**: FIFO ensures nodes are processed level by level
- **Level size tracking**: By storing `q.size()` before the loop, we know exactly how many nodes belong to the current level
- **Children added for next level**: Children are added to the queue but won't be processed until the next iteration
- **Left-to-right order**: Always adding left child before right child maintains the correct order

### **Example Walkthrough:**

**For `root = [3,9,20,null,null,15,7]`:**

```
Tree structure:
    3
   / \
  9   20
     /  \
    15   7

Initial: q = [3], rtn = []

Level 0:
  levelSize = 1
  Process: [3]
    - curr = 3, add 3 to level
    - Add 9 (left) and 20 (right) to queue
  level = [3]
  q = [9, 20]
  rtn = [[3]]

Level 1:
  levelSize = 2
  Process: [9, 20]
    - curr = 9, add 9 to level, no children
    - curr = 20, add 20 to level, add 15 (left) and 7 (right) to queue
  level = [9, 20]
  q = [15, 7]
  rtn = [[3], [9, 20]]

Level 2:
  levelSize = 2
  Process: [15, 7]
    - curr = 15, add 15 to level, no children
    - curr = 7, add 7 to level, no children
  level = [15, 7]
  q = []
  rtn = [[3], [9, 20], [15, 7]]

Queue empty, return result
```

### **Complexity Analysis:**

- **Time Complexity:** O(n) where n is the number of nodes
  - Each node is visited exactly once
  - Each node is enqueued and dequeued once
- **Space Complexity:** O(n) for the result and O(w) for the queue where w is maximum width
  - Result stores all n node values
  - Queue stores at most one level of nodes (maximum width of tree)

## Key Insights

1. **BFS Structure**: Queue naturally maintains level-by-level order
2. **Level Size Tracking**: Critical to know when we've finished processing a level
3. **Pre-allocation**: Using `reserve()` avoids vector reallocation overhead
4. **Children Order**: Always add left then right to maintain left-to-right traversal

## Related Problems

- [LC 103: Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) - Alternate direction at each level
- [LC 107: Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) - Reverse level order
- [LC 314: Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) - Vertical traversal
- [LC 199: Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) - Right side view

---

*This problem demonstrates the fundamental BFS pattern for tree traversal, which is essential for many tree problems.*

