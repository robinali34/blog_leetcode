---
layout: post
title: "[Easy] 111. Minimum Depth of Binary Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-111-minimum-depth-of-binary-tree/
tags: [leetcode, easy, tree, dfs, bfs, recursion]
---
Given a binary tree, find its **minimum depth**.

The minimum depth is the number of nodes along the **shortest path** from the root node down to the nearest **leaf node**.

**Note:** A leaf is a node with no children.

## Thinking Process

Given a binary tree, find its **minimum depth**.

The minimum depth is the number of nodes along the **shortest path** from the root node down to the nearest **leaf node**.

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
Input: root = [3,9,20,null,null,15,7]
Output: 2
Explanation: The minimum depth is 2, which is the path: 3 → 9.
```

**Example 2:**
```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
Explanation: The minimum depth is 5, which is the path: 2 → 3 → 4 → 5 → 6.
```

## Constraints

- The number of nodes in the tree is in the range `[0, 10^5]`.
- `-1000 <= Node.val <= 1000`

## Key Differences from Maximum Depth

| Aspect | Maximum Depth | Minimum Depth |
|--------|---------------|---------------|
| **Formula** | `1 + max(left, right)` | `1 + min(left, right)` |
| **Null Handling** | Can use `max(0, depth)` | Must skip null children |
| **Single Child** | Works with `max(0, child)` | Must only consider non-null child |
| **Early Termination** | No early exit possible | BFS can stop at first leaf |

## Common Mistakes

1. **Empty tree**: `root = null` → return `0`
2. **Single node**: `root = [1]` → return `1`
3. **Skewed tree**: `[2,null,3,null,4]` → return `3` (must follow the only path)
4. **Balanced tree**: `[3,9,20,null,null,15,7]` → return `2` (shortest path: 3 → 9)
5. **One child only**: `[1,2,null]` → return `2` (can't use null as depth 0)

1. **Wrong null handling**: Using `min(minDepth(left), minDepth(right))` when one is null
   ```cpp
   // WRONG:
   return 1 + min(minDepth(root->left), minDepth(root->right));
   // If left is null, minDepth(left) = 0, min(0, right) = 0 ❌
   ```

2. **Not checking leaf**: Forgetting to return 1 for leaf nodes
3. **Base case error**: Returning wrong value for null node
4. **Off-by-one**: Counting edges instead of nodes
5. **Missing single-child check**: Not handling nodes with only one child

## Related Problems

- [LC 104: Maximum Depth of Binary Tree](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/) - Find maximum depth (similar problem)
- [LC 110: Balanced Binary Tree](https://www.leetcode.com/problems/balanced-binary-tree/) - Check if tree is balanced
- [LC 112: Path Sum](https://www.leetcode.com/problems/path-sum/) - Check if path sum exists
- [LC 111: Minimum Depth of Binary Tree](https://www.leetcode.com/problems/minimum-depth-of-binary-tree/) - This problem
- [LC 559: Maximum Depth of N-ary Tree](https://www.leetcode.com/problems/maximum-depth-of-n-ary-tree/) - Extension to N-ary tree

## Key Takeaways

- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

## References

- [LC 111: Minimum Depth of Binary Tree on LeetCode](https://www.leetcode.com/problems/minimum-depth-of-binary-tree/)
- [LeetCode Discuss — LC 111: Minimum Depth of Binary Tree](https://www.leetcode.com/problems/minimum-depth-of-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-depth-of-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
