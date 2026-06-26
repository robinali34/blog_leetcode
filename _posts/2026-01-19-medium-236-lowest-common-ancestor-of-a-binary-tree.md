---
layout: post
title: "[Medium] 236. Lowest Common Ancestor of a Binary Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, medium, tree, dfs]
permalink: /2026/01/19/medium-236-lowest-common-ancestor-of-a-binary-tree/
tags: [leetcode, medium, tree, dfs, recursion, lca]
---
Given a binary tree, find the **lowest common ancestor (LCA)** of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**)."

## Thinking Process

1. **Post-order Traversal**: Process children before parent to find LCA bottom-up
- Return node if it matches target
- Return current node if both subtrees found targets
- Otherwise, propagate the found result upward

- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 165" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Tree DFS (bottom-up)</text>

  <line x1="140" y1="42" x2="80" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="140" y1="42" x2="200" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="80" y1="88" x2="50" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="200" y1="88" x2="230" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <circle cx="140" cy="42" r="18" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="140" y="46" text-anchor="middle" font-size="12" fill="#3D3535">3</text>
  <circle cx="80" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="80" y="92" text-anchor="middle" font-size="11" fill="#3D3535">9</text>
  <circle cx="200" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="200" y="92" text-anchor="middle" font-size="11" fill="#3D3535">20</text>
  <circle cx="50" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="50" y="132" text-anchor="middle" font-size="10" fill="#3D3535">15</text>
  <circle cx="230" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="230" y="132" text-anchor="middle" font-size="10" fill="#3D3535">7</text>
  <text x="140" y="155" text-anchor="middle" font-size="11" fill="#6B6560">post-order: combine left + right + 1</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Examples

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Tree structure:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

**Example 2:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 1 is 5 (a node can be a descendant of itself).

Tree structure:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

**Example 3:**
```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

## Common Mistakes

1. **One node is ancestor of other**: `p = 5`, `q = 4` → return `5`
2. **Root is LCA**: `p` and `q` in different subtrees → return root
3. **Both nodes in same subtree**: LCA is deeper in that subtree
4. **Root equals one target**: Return root
5. **Skewed tree**: Works correctly but O(n) space

1. **Wrong traversal order**: Using pre-order instead of post-order
   ```cpp
   // WRONG:
   if (node == p || node == q) return node; // Check before recursion
   // ❌ May return too early
   ```

2. **Not handling self as descendant**: Forgetting that a node can be its own descendant
3. **Wrong return logic**: Returning null when one subtree found a match
   ```cpp
   // WRONG:
   if (left && right) return node;
   return nullptr; // ❌ Should return left or right
   ```

4. **Comparing values instead of nodes**: Using `node->val` instead of `node == p`
5. **Not propagating results**: Not returning the found node from subtrees

## Related Problems

- [LC 236: Lowest Common Ancestor of a Binary Tree](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) - This problem
- [LC 235: Lowest Common Ancestor of a Binary Search Tree](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) - BST version (easier)
- [LC 1644: Lowest Common Ancestor of a Binary Tree II](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/) - Nodes may not exist
- [LC 1650: Lowest Common Ancestor of a Binary Tree III](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) - Nodes have parent pointers
- [LC 1123: Lowest Common Ancestor of Deepest Leaves](https://www.leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) - LCA of deepest leaves
- [LC 102: Binary Tree Level Order Traversal](https://www.leetcode.com/problems/binary-tree-level-order-traversal/) - Level-order traversal

## Key Takeaways

1. **Post-order Traversal**: Process children before parent to find LCA bottom-up
2. **Return Strategy**: 
   - Return node if it matches target
   - Return current node if both subtrees found targets
   - Otherwise, propagate the found result upward
3. **Self as Descendant**: If `p` is ancestor of `q`, return `p` (and vice versa)
4. **Single Pass**: Can find LCA in one traversal without storing paths

## References

- [LC 236: Lowest Common Ancestor of a Binary Tree on LeetCode](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [LeetCode Discuss — LC 236: Lowest Common Ancestor of a Binary Tree](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
