---
layout: post
title: "[Easy] 101. Symmetric Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-101-symmetric-tree/
tags: [leetcode, easy, tree, dfs, recursion]
---
Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Thinking Process

1. **Mirror Comparison**: Compare left subtree with right subtree as mirrors
- `a->left` ↔ `b->right` (outer nodes)
- `a->right` ↔ `b->left` (inner nodes)

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
Input: root = [1,2,2,3,4,4,3]
Output: true

Tree structure:
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```

**Example 2:**
```
Input: root = [1,2,2,null,3,null,3]
Output: false

Tree structure:
      1
     / \
    2   2
     \   \
      3   3
```

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

## Common Mistakes

1. **Empty tree**: `root = []` → return `true`
2. **Single node**: `root = [1]` → return `true`
3. **Symmetric tree**: `[1,2,2,3,4,4,3]` → return `true`
4. **Asymmetric structure**: `[1,2,2,null,3,null,3]` → return `false`
5. **Asymmetric values**: `[1,2,2,3,4,5,3]` → return `false`
6. **One child**: `[1,2,null]` → return `false`

1. **Wrong comparison order**: Comparing `a->left` with `b->left` instead of `b->right`
   ```cpp
   // WRONG:
   return isMirror(a->left, b->left) && isMirror(a->right, b->right);
   // ❌ This checks if trees are identical, not mirrors
   ```

2. **Not handling null correctly**: Accessing values before null check
3. **Wrong logic operator**: Using OR instead of AND
4. **Missing value check**: Only checking structure, not values
5. **Comparing same side**: Forgetting to cross-compare (left with right)

## Related Problems

- [LC 101: Symmetric Tree](https://www.leetcode.com/problems/symmetric-tree/) - This problem
- [LC 100: Same Tree](https://www.leetcode.com/problems/same-tree/) - Check if two trees are identical
- [LC 226: Invert Binary Tree](https://www.leetcode.com/problems/invert-binary-tree/) - Mirror a binary tree
- [LC 572: Subtree of Another Tree](https://www.leetcode.com/problems/subtree-of-another-tree/) - Check if subtree exists
- [LC 104: Maximum Depth of Binary Tree](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/) - Find maximum depth
- [LC 110: Balanced Binary Tree](https://www.leetcode.com/problems/balanced-binary-tree/) - Check if tree is balanced

## Key Takeaways

1. **Mirror Comparison**: Compare left subtree with right subtree as mirrors
2. **Cross Comparison**: 
   - `a->left` ↔ `b->right` (outer nodes)
   - `a->right` ↔ `b->left` (inner nodes)
3. **Three Base Cases**: Both null, one null, or value mismatch
4. **AND Logic**: Both comparisons must succeed for symmetry
5. **Empty Tree**: Empty tree is symmetric

## References

- [LC 101: Symmetric Tree on LeetCode](https://www.leetcode.com/problems/symmetric-tree/)
- [LeetCode Discuss — LC 101: Symmetric Tree](https://www.leetcode.com/problems/symmetric-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/symmetric-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
