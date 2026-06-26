---
layout: post
title: "[Easy] 100. Same Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-100-same-tree/
tags: [leetcode, easy, tree, dfs, recursion]
---
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are **structurally identical**, and the nodes have the **same value**.

## Thinking Process

1. **Three Base Cases**: Both null, one null, or value mismatch

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
| **Recursive DFS** *(this problem)* | $O(n)$ | $O(h)$ stack | Natural for trees and graphs |
| Iterative DFS (stack) | $O(n)$ | $O(n)$ | Avoid recursion depth limits |
| DFS with memoization | $O(n)$ | $O(n)$ | Overlapping subproblems on graphs |
| Backtracking DFS | $O(2^n)$ typical | $O(n)$ | Enumerate choices with pruning |

## Examples

**Example 1:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true

Tree p:        Tree q:
    1              1
   / \            / \
  2   3          2   3
```

**Example 2:**
```
Input: p = [1,2], q = [1,null,2]
Output: false

Tree p:        Tree q:
    1              1
   /                 \
  2                   2
```

**Example 3:**
```
Input: p = [1,2,1], q = [1,1,2]
Output: false

Tree p:        Tree q:
    1              1
   / \            / \
  2   1          1   2
```

## Constraints

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Common Mistakes

1. **Both empty**: `p = []`, `q = []` → return `true`
2. **One empty**: `p = []`, `q = [1]` → return `false`
3. **Single node match**: `p = [1]`, `q = [1]` → return `true`
4. **Single node mismatch**: `p = [1]`, `q = [2]` → return `false`
5. **Same structure, different values**: `p = [1,2]`, `q = [1,3]` → return `false`
6. **Different structure**: `p = [1,2]`, `q = [1,null,2]` → return `false`

1. **Not checking both nulls first**: Accessing values before null check
   ```cpp
   // WRONG:
   if (p->val != q->val) return false; // ❌ Crashes if p or q is null
   ```

2. **Wrong logic operator**: Using OR instead of AND
   ```cpp
   // WRONG:
   return isSameTree(p->left, q->left) || isSameTree(p->right, q->right);
   // ❌ Returns true if only one subtree matches
   ```

3. **Not handling null correctly**: Forgetting that one tree can be null while the other isn't
4. **Comparing references**: Comparing node pointers instead of values
5. **Missing value check**: Only checking structure, not values

## Related Problems

- [LC 100: Same Tree](https://www.leetcode.com/problems/same-tree/) - This problem
- [LC 101: Symmetric Tree](https://www.leetcode.com/problems/symmetric-tree/) - Check if tree is symmetric
- [LC 226: Invert Binary Tree](https://www.leetcode.com/problems/invert-binary-tree/) - Mirror a binary tree
- [LC 572: Subtree of Another Tree](https://www.leetcode.com/problems/subtree-of-another-tree/) - Check if subtree exists
- [LC 104: Maximum Depth of Binary Tree](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/) - Find maximum depth
- [LC 110: Balanced Binary Tree](https://www.leetcode.com/problems/balanced-binary-tree/) - Check if tree is balanced

## Key Takeaways

1. **Three Base Cases**: Both null, one null, or value mismatch
2. **Symmetric Comparison**: Compare corresponding nodes in both trees
3. **AND Logic**: Both subtrees must match for trees to be identical
4. **Early Termination**: Return false immediately when mismatch found
5. **Pre-order Traversal**: Check current node before recursing

## References

- [LC 100: Same Tree on LeetCode](https://www.leetcode.com/problems/same-tree/)
- [LeetCode Discuss — LC 100: Same Tree](https://www.leetcode.com/problems/same-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/same-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
