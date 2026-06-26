---
layout: post
title: "[Easy] 543. Diameter of Binary Tree"
date: 2026-03-06
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, dfs, recursion]
permalink: /2026/03/06/easy-543-diameter-of-binary-tree/
---
Given the `root` of a binary tree, return the length of the **diameter** of the tree. The diameter is the length of the longest path between any two nodes (measured in number of **edges**). This path may or may not pass through the root.

## Examples

**Example 1:**

```
Input: root = [1,2,3,4,5]
      1
     / \
    2   3
   / \
  4   5
Output: 3
Explanation: The longest path is [4,2,1,3] or [5,2,1,3], both length 3.
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

## Constraints

- The number of nodes is in `[1, 10^4]`
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

### Key Observation

The diameter passing through a node = **left depth + right depth + 2** (counting edges). The overall diameter is the maximum of this across all nodes.

### Why Bottom-Up?

We need the depth of every subtree. Computing depth top-down would recompute subtrees repeatedly ($O(n^2)$). Instead, compute depth bottom-up and update a global maximum at each node -- same pattern as [LC 110 Balanced Binary Tree](/2026/03/06/easy-110-balanced-binary-tree/).

### Edge Count vs Node Count

Returning `-1` for a null node means a leaf has depth `0`, and the path through a node with left depth `L` and right depth `R` has `L + R + 2` edges. This correctly counts edges rather than nodes.

### Walk-Through

```
      1
     / \
    2   3
   / \
  4   5

Node 4: left=-1, right=-1 → diameter candidate = -1+-1+2 = 0, return 0
Node 5: left=-1, right=-1 → diameter candidate = 0, return 0
Node 2: left=0,  right=0  → diameter candidate = 0+0+2 = 2, return 1
Node 3: left=-1, right=-1 → diameter candidate = 0, return 0
Node 1: left=1,  right=0  → diameter candidate = 1+0+2 = 3, return 2

Max diameter = 3 ✓
```



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

## Approach: Bottom-Up DFS -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        getLongestPath(root, diameter);
        return diameter;
    }

private:
    int getLongestPath(TreeNode* node, int& diameter) {
        if (!node) return -1;
        int leftPath = getLongestPath(node->left, diameter);
        int rightPath = getLongestPath(node->right, diameter);
        diameter = max(diameter, leftPath + rightPath + 2);
        return max(leftPath, rightPath) + 1;
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** ### Key Observation

**Walkthrough** — input `root = [1,2,3,4,5]`, expected output `3`:

The longest path is [4,2,1,3] or [5,2,1,3], both length 3.
## Common Mistakes

- Returning `0` for null instead of `-1` (off-by-one: counts nodes instead of edges)
- Forgetting the diameter may not pass through the root -- must track the global max across all nodes
- Returning the diameter from the recursive function instead of the single-side depth (the function returns depth, but updates diameter as a side effect)

## Key Takeaways

- **Bottom-up DFS with global max** is a recurring tree pattern: compute a per-node value bottom-up, update a global answer at each node
- Same structure as LC 110 (sentinel) and LC 124 (max path sum) -- learn one, get all three
- The `return -1` for null trick cleanly handles edge counting

## Related Problems

- [110. Balanced Binary Tree](https://www.leetcode.com/problems/balanced-binary-tree/) -- bottom-up height with sentinel
- [124. Binary Tree Maximum Path Sum](https://www.leetcode.com/problems/binary-tree-maximum-path-sum/) -- same pattern with values instead of edges
- [687. Longest Univalue Path](https://www.leetcode.com/problems/longest-univalue-path/) -- diameter variant with value constraint

## References

- [LC 543: Diameter of Binary Tree on LeetCode](https://www.leetcode.com/problems/diameter-of-binary-tree/)
- [LeetCode Discuss — LC 543: Diameter of Binary Tree](https://www.leetcode.com/problems/diameter-of-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/diameter-of-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
