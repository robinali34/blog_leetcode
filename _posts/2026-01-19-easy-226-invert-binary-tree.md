---
layout: post
title: "[Easy] 226. Invert Binary Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-226-invert-binary-tree/
tags: [leetcode, easy, tree, dfs, recursion]
---
Given the `root` of a binary tree, invert the tree, and return *its root*.

## Thinking Process

1. **Post-order Traversal**: Process children before parent (or swap then recurse)

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
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Before inversion:
      4
     / \
    2   7
   / \ / \
  1  3 6  9

After inversion:
      4
     / \
    7   2
   / \ / \
  9  6 3  1
```

**Example 2:**
```
Input: root = [2,1,3]
Output: [2,3,1]

Before inversion:
    2
   / \
  1   3

After inversion:
    2
   / \
  3   1
```

**Example 3:**
```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Common Mistakes

1. **Empty tree**: `root = null` → return `null`
2. **Single node**: `root = [1]` → return `[1]` (no change)
3. **Skewed tree**: `[1,2,null]` → becomes `[1,null,2]`
4. **Balanced tree**: Works correctly for any balanced tree
5. **Large tree**: Handles up to 100 nodes efficiently

1. **Not handling null**: Forgetting to check for empty node
   ```cpp
   // WRONG:
   TreeNode* tmp = root->left; // ❌ Crashes if root is null
   ```

2. **Wrong traversal order**: Processing parent before children (pre-order)
3. **Creating new nodes**: Unnecessarily creating new tree instead of modifying in-place
4. **Not returning root**: Forgetting to return the modified root
5. **Swapping before recursion**: Should swap after or during recursion

## Related Problems

- [LC 226: Invert Binary Tree](https://www.leetcode.com/problems/invert-binary-tree/) - This problem
- [LC 100: Same Tree](https://www.leetcode.com/problems/same-tree/) - Check if two trees are identical
- [LC 101: Symmetric Tree](https://www.leetcode.com/problems/symmetric-tree/) - Check if tree is symmetric
- [LC 104: Maximum Depth of Binary Tree](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/) - Find maximum depth
- [LC 111: Minimum Depth of Binary Tree](https://www.leetcode.com/problems/minimum-depth-of-binary-tree/) - Find minimum depth
- [LC 617: Merge Two Binary Trees](https://www.leetcode.com/problems/merge-two-binary-trees/) - Merge two trees

## Key Takeaways

1. **Post-order Traversal**: Process children before parent (or swap then recurse)
2. **In-Place Modification**: Modify tree structure directly, no need for new tree
3. **Symmetric Operation**: Swapping is symmetric - order doesn't matter
4. **Base Case**: Empty node requires no action
5. **Return Root**: Always return the root node after modification

## References

- [LC 226: Invert Binary Tree on LeetCode](https://www.leetcode.com/problems/invert-binary-tree/)
- [LeetCode Discuss — LC 226: Invert Binary Tree](https://www.leetcode.com/problems/invert-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/invert-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
