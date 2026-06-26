---
layout: post
title: "[Medium] 103. Binary Tree Zigzag Level Order Traversal"
date: 2026-01-06 00:00:00 -0700
categories: [leetcode, medium, tree, bfs, binary-tree]
permalink: /2026/01/06/medium-103-binary-tree-zigzag-level-order-traversal/
tags: [leetcode, medium, tree, bfs, level-order-traversal, deque, binary-tree]
---
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

## Thinking Process

1. **BFS Structure**: Maintains level-by-level traversal

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

### Solution Explanation

**Approach:** Level-order BFS (this problem)

**Key idea:** 1. **BFS Structure**: Maintains level-by-level traversal

**How the code works:**
1. **BFS Structure**: Maintains level-by-level traversal
- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

**Walkthrough** — input `root = [3,9,20,null,null,15,7]`, expected output `[[3],[20,9],[15,7]]`:

Level 0: [3] (left to right)
Level 1: [20,9] (right to left)
Level 2: [15,7] (left to right)

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
## Related Problems

- [LC 102: Binary Tree Level Order Traversal](https://www.leetcode.com/problems/binary-tree-level-order-traversal/) - Standard level order
- [LC 107: Binary Tree Level Order Traversal II](https://www.leetcode.com/problems/binary-tree-level-order-traversal-ii/) - Reverse level order
- [LC 314: Binary Tree Vertical Order Traversal](https://www.leetcode.com/problems/binary-tree-vertical-order-traversal/) - Vertical traversal
- [LC 199: Binary Tree Right Side View](https://www.leetcode.com/problems/binary-tree-right-side-view/) - Right side view

## Implementation Notes

1. **Deque vs Queue**: Deque allows efficient insertion at both ends
2. **Insert Performance**: `insert(begin())` is O(n) per level, but acceptable for this problem
3. **Direction Flag**: Simple boolean toggle is cleaner than using level number % 2
4. **Null Check**: Always check for null root before processing

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **BFS Structure**: Maintains level-by-level traversal
2. **Direction Toggle**: Simple boolean flag to alternate direction
3. **Insertion Strategy**: Choose insertion method based on direction
4. **Children Order**: Always process left then right to maintain level structure

## References

- [LC 103: Binary Tree Zigzag Level Order Traversal on LeetCode](https://www.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
- [LeetCode Discuss — LC 103: Binary Tree Zigzag Level Order Traversal](https://www.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
