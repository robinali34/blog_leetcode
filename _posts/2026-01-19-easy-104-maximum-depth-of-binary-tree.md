---
layout: post
title: "[Easy] 104. Maximum Depth of Binary Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-104-maximum-depth-of-binary-tree/
tags: [leetcode, easy, tree, dfs, bfs, recursion]
---
Given the `root` of a binary tree, return its **maximum depth** — the number of nodes along the longest path from the root down to the farthest leaf.

## Examples

**Example 1:**

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2
```

## Constraints

- The number of nodes is in `[0, 10^4]`
- `-100 <= Node.val <= 100`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | $O(n)$ | $O(h)$ stack | Natural for trees and graphs |
| Iterative DFS (stack) | $O(n)$ | $O(n)$ | Avoid recursion depth limits |
| DFS with memoization | $O(n)$ | $O(n)$ | Overlapping subproblems on graphs |
| Backtracking DFS | $O(2^n)$ typical | $O(n)$ | Enumerate choices with pruning |

## Thinking Process

Depth counts **nodes**, not edges. The tree is empty when `root` is null → depth 0.

**Bottom-up DFS** is the cleanest formulation:

- Base case: null node → 0
- Otherwise → `1 + max(left depth, right depth)`

Each subtree returns its own height; the parent adds one for the current node. BFS level counting also works but needs a queue.



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

## Solution — $O(n)$ time, $O(h)$ space

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** Depth counts **nodes**, not edges. The tree is empty when `root` is null → depth 0.

**How the code works:**
**Bottom-up DFS** is the cleanest formulation:
- Base case: null node → 0
- Otherwise → `1 + max(left depth, right depth)`

**Walkthrough** — input `root = [3,9,20,null,null,15,7]`, expected output `3`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

**Time:** $O(n) · **Space:** $O(h)
## Common Mistakes

- Returning `1` for null instead of `0` (off-by-one on empty tree)
- Counting edges instead of nodes
- Top-down depth tracking with a running max — works but more error-prone than bottom-up

## Related Problems

- [111. Minimum Depth of Binary Tree](https://www.leetcode.com/problems/minimum-depth-of-binary-tree/)
- [110. Balanced Binary Tree](https://www.leetcode.com/problems/balanced-binary-tree/)
- [543. Diameter of Binary Tree](https://www.leetcode.com/problems/diameter-of-binary-tree/)
- [102. Binary Tree Level Order Traversal](https://www.leetcode.com/problems/binary-tree-level-order-traversal/) — BFS alternative

## Key Takeaways

- **Post-order DFS** (`return 1 + max(left, right)`) is the standard tree depth/height template
- Depth from root (this problem) vs height from leaves — same recurrence, different framing
- First of many tree DFS problems — master this before LCA, diameter, and path sums

## References

- [LC 104: Maximum Depth of Binary Tree on LeetCode](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/)
- [LeetCode Discuss — LC 104: Maximum Depth of Binary Tree](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
