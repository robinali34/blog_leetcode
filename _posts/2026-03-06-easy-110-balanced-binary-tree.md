---
layout: post
title: "LeetCode 110. Balanced Binary Tree"
date: 2026-03-06
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, dfs, recursion]
permalink: /2026/03/06/easy-110-balanced-binary-tree/
---

Given a binary tree, determine if it is **height-balanced**. A height-balanced binary tree is one in which the depth of the two subtrees of every node never differs by more than one.

## Examples

**Example 1:**

```
Input: root = [3,9,20,null,null,15,7]
      3
     / \
    9  20
      /  \
     15   7
Output: true
```

**Example 2:**

```
Input: root = [1,2,2,3,3,null,null,4,4]
        1
       / \
      2   2
     / \
    3   3
   / \
  4   4
Output: false
```

**Example 3:**

```
Input: root = []
Output: true
```

## Constraints

- The number of nodes is in `[0, 5000]`
- `-10^4 <= Node.val <= 10^4`

## Thinking Process

### Naive: Top-Down -- $O(n^2)$

For each node, compute the height of left and right subtrees separately, check the difference, then recurse on children. This recomputes heights repeatedly -- $O(n)$ per node, $O(n^2)$ total.

### Optimal: Bottom-Up with Early Termination -- $O(n)$

Compute height bottom-up and **return -1 as a sentinel** the moment an imbalance is detected. This way:
- Each node is visited exactly once
- An imbalance anywhere propagates up immediately, short-circuiting the rest of the tree

The key insight is combining two tasks into one recursive function: **compute height** and **detect imbalance**, using `-1` as the "not balanced" signal.

## Approach: Bottom-Up DFS -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return getHeight(root) != -1;
    }

private:
    int getHeight(TreeNode* node) {
        if (!node) return 0;

        int leftHeight = getHeight(node->left);
        if (leftHeight == -1) return -1;

        int rightHeight = getHeight(node->right);
        if (rightHeight == -1) return -1;

        if (abs(leftHeight - rightHeight) > 1) return -1;

        return max(leftHeight, rightHeight) + 1;
    }
};
```
{% endraw %}

**Time**: $O(n)$ -- each node visited once
**Space**: $O(h)$ recursion stack ($O(\log n)$ balanced, $O(n)$ skewed)

## Why -1 Works as a Sentinel

Normal heights are always $\geq 0$, so `-1` is an impossible height value. Once any subtree returns `-1`, every ancestor immediately returns `-1` without doing further work. This is the **early termination** that makes it $O(n)$.

## Common Mistakes

- Computing height and checking balance in separate passes (top-down $O(n^2)$)
- Forgetting to check `leftHeight == -1` **before** computing `rightHeight` (misses early termination)
- Confusing "balanced" with "perfect" or "complete" -- balanced only requires height difference $\leq 1$ at every node

## Key Takeaways

- **Sentinel return value** (-1) to encode both height and validity in a single function is a clean pattern
- **Bottom-up > top-down** when you can avoid redundant computation
- This pattern generalizes: any tree property that depends on subtree properties can use bottom-up DFS with early exit

## Related Problems

- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) -- height computation (base case for this problem)
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) -- same bottom-up pattern, track max path
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) -- bottom-up with global max

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
