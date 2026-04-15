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
{% endraw %}

**Time**: $O(n)$ -- each node visited once
**Space**: $O(h)$ recursion stack ($O(\log n)$ balanced, $O(n)$ skewed)

## Common Mistakes

- Returning `0` for null instead of `-1` (off-by-one: counts nodes instead of edges)
- Forgetting the diameter may not pass through the root -- must track the global max across all nodes
- Returning the diameter from the recursive function instead of the single-side depth (the function returns depth, but updates diameter as a side effect)

## Key Takeaways

- **Bottom-up DFS with global max** is a recurring tree pattern: compute a per-node value bottom-up, update a global answer at each node
- Same structure as LC 110 (sentinel) and LC 124 (max path sum) -- learn one, get all three
- The `return -1` for null trick cleanly handles edge counting

## Related Problems

- [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) -- bottom-up height with sentinel
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) -- same pattern with values instead of edges
- [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) -- diameter variant with value constraint

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
