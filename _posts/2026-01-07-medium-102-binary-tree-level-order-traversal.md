---
layout: post
title: "[Medium] 102. Binary Tree Level Order Traversal"
date: 2026-01-07 00:00:00 -0700
categories: [leetcode, medium, tree, bfs, binary-tree]
permalink: /2026/01/07/medium-102-binary-tree-level-order-traversal/
tags: [leetcode, medium, tree, bfs, level-order-traversal, binary-tree]
---
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

## Thinking Process

1. **BFS Structure**: Queue naturally maintains level-by-level order

- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Queue BFS | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| **Level-order BFS** *(this problem)* | O(n) | O(w) | Process by depth/layer |

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

### Solution Explanation

**Approach:** Level-order BFS (this problem)

**Key idea:** 1. **BFS Structure**: Queue naturally maintains level-by-level order

**How the code works:**
1. **BFS Structure**: Queue naturally maintains level-by-level order
- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

**Walkthrough** — input `root = [3,9,20,null,null,15,7]`, expected output `[[3],[9,20],[15,7]]`:

Level 0: [3]
Level 1: [9, 20]
Level 2: [15, 7]

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
## Related Problems

- [LC 103: Binary Tree Zigzag Level Order Traversal](https://www.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) - Alternate direction at each level
- [LC 107: Binary Tree Level Order Traversal II](https://www.leetcode.com/problems/binary-tree-level-order-traversal-ii/) - Reverse level order
- [LC 314: Binary Tree Vertical Order Traversal](https://www.leetcode.com/problems/binary-tree-vertical-order-traversal/) - Vertical traversal
- [LC 199: Binary Tree Right Side View](https://www.leetcode.com/problems/binary-tree-right-side-view/) - Right side view

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **BFS Structure**: Queue naturally maintains level-by-level order
2. **Level Size Tracking**: Critical to know when we've finished processing a level
3. **Pre-allocation**: Using `reserve()` avoids vector reallocation overhead
4. **Children Order**: Always add left then right to maintain left-to-right traversal

## References

- [LC 102: Binary Tree Level Order Traversal on LeetCode](https://www.leetcode.com/problems/binary-tree-level-order-traversal/)
- [LeetCode Discuss — LC 102: Binary Tree Level Order Traversal](https://www.leetcode.com/problems/binary-tree-level-order-traversal/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/binary-tree-level-order-traversal/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
