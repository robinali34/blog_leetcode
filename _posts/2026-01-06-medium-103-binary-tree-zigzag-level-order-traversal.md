---
layout: post
title: "103. Binary Tree Zigzag Level Order Traversal"
date: 2026-01-06 00:00:00 -0700
categories: [leetcode, medium, tree, bfs, binary-tree]
permalink: /2026/01/06/medium-103-binary-tree-zigzag-level-order-traversal/
tags: [leetcode, medium, tree, bfs, level-order-traversal, deque, binary-tree]
---

# 103. Binary Tree Zigzag Level Order Traversal

## Problem Statement

Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Explanation:
Level 0: [3] (left to right)
Level 1: [20,9] (right to left)
Level 2: [15,7] (left to right)
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
- `-100 <= Node.val <= 100`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Zigzag pattern**: What is the zigzag pattern? (Assumption: Level 0 left-to-right, level 1 right-to-left, level 2 left-to-right, alternating)

2. **Level definition**: How are levels numbered? (Assumption: Level 0 is root, level 1 is root's children, etc.)

3. **Output format**: How should we represent the result? (Assumption: List of lists - each inner list represents one level in zigzag order)

4. **Empty tree**: What should we return for an empty tree? (Assumption: Return empty list [])

5. **Starting direction**: Which direction should level 0 use? (Assumption: Left-to-right - even levels go left-to-right, odd levels go right-to-left)

## Solution Approach

This problem is a variation of **level-order traversal** (BFS) where we alternate the direction of traversal at each level. The key insight is to:
1. Use BFS to traverse level by level
2. Alternate the direction of adding values to each level
3. Use a deque for efficient insertion at both ends

### Key Insights:

1. **Level-by-Level Processing**: Process all nodes at the current level before moving to the next
2. **Direction Alternation**: Toggle between left-to-right and right-to-left at each level
3. **Deque for Efficiency**: Use `deque` to efficiently insert at the beginning when going right-to-left
4. **Standard BFS**: Always add children in the same order (left, then right) to maintain level structure

### Algorithm:

1. **Initialize**: Use a deque for BFS, start with root, set `leftToRight = true`
2. **For each level**:
   - Process all nodes at current level
   - Add values to level vector based on direction
   - Toggle direction for next level
3. **Add children**: Always add left child first, then right child (maintains level order)

## Solution

### **Solution: BFS with Deque and Direction Toggle**

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> rtn;
        if(root == nullptr) return rtn;

        deque<TreeNode*> queue;
        queue.push_back(root);
        bool leftToRight = true;

        while(!queue.empty()) {
            int size = queue.size();
            vector<int> level;
            for(int i = 0; i < size; i++) {
                TreeNode* curr = queue.front();
                queue.pop_front();
                if(leftToRight) {
                    level.push_back(curr->val);
                } else {
                    level.insert(level.begin(), curr->val);
                }
                if(curr->left) queue.push_back(curr->left);
                if(curr->right) queue.push_back(curr->right);
            }
            rtn.push_back(level);
            leftToRight = !leftToRight;
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 4-6)**:
   - Create empty result vector
   - Return empty result if root is null
   - Initialize deque with root node
   - Set `leftToRight = true` for first level

2. **Level Processing (Lines 8-25)**:
   - **For each level**:
     - Get current level size (number of nodes at this level)
     - Create empty level vector
     - **Process each node at current level**:
       - Remove node from front of deque
       - **Add value based on direction**:
         - If `leftToRight`: append to end of level vector
         - If `rightToLeft`: insert at beginning of level vector
       - **Add children**: Always add left child first, then right child to back of deque
     - Add completed level to result
     - **Toggle direction**: `leftToRight = !leftToRight`

3. **Return (Line 26)**: Return the zigzag level order traversal

### **Why This Works:**

- **Deque for BFS**: `deque` allows efficient removal from front and insertion at back
- **Direction Toggle**: Alternates between left-to-right and right-to-left
- **Insertion Strategy**: 
  - Left-to-right: `push_back()` - natural order
  - Right-to-left: `insert(begin())` - reverse order
- **Children Order**: Always add left then right to maintain level structure

### **Example Walkthrough:**

**For `root = [3,9,20,null,null,15,7]`:**

```
Tree structure:
    3
   / \
  9   20
     /  \
    15   7

Level 0 (leftToRight = true):
  Process: [3]
  Add: level = [3]
  Children: [9, 20]
  Result: [[3]]

Level 1 (leftToRight = false):
  Process: [9, 20]
  Add: level.insert(9) → [9], then level.insert(20) → [20, 9]
  Children: [15, 7]
  Result: [[3], [20, 9]]

Level 2 (leftToRight = true):
  Process: [15, 7]
  Add: level.push_back(15) → [15], then level.push_back(7) → [15, 7]
  Children: []
  Result: [[3], [20, 9], [15, 7]]
```

### **Complexity Analysis:**

- **Time Complexity:** O(n) where n is the number of nodes
  - Each node is visited exactly once
  - `insert()` at beginning is O(n) per level, but amortized over all levels is still O(n)
- **Space Complexity:** O(n) for the result and O(w) for the deque where w is maximum width
  - Result stores all n node values
  - Deque stores at most one level of nodes (maximum width)

## Alternative Approaches

### **Approach 2: Using Index Calculation**

Instead of inserting at the beginning, we can pre-allocate the level vector and calculate the index:

```cpp
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

**Advantages:**
- More efficient: O(1) index assignment vs O(n) insertion
- Pre-allocated vector avoids reallocation

**Trade-off:**
- Slightly more complex index calculation

## Key Insights

1. **BFS Structure**: Maintains level-by-level traversal
2. **Direction Toggle**: Simple boolean flag to alternate direction
3. **Insertion Strategy**: Choose insertion method based on direction
4. **Children Order**: Always process left then right to maintain level structure

## Related Problems

- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Standard level order
- [LC 107: Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) - Reverse level order
- [LC 314: Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) - Vertical traversal
- [LC 199: Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) - Right side view

## Implementation Notes

1. **Deque vs Queue**: Deque allows efficient insertion at both ends
2. **Insert Performance**: `insert(begin())` is O(n) per level, but acceptable for this problem
3. **Direction Flag**: Simple boolean toggle is cleaner than using level number % 2
4. **Null Check**: Always check for null root before processing

---

*This problem demonstrates how to modify standard BFS to achieve zigzag traversal by alternating the insertion direction at each level.*

