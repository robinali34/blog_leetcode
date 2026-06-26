---
layout: post
title: "[Easy] 110. Balanced Binary Tree"
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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Thinking Process

### Naive: Top-Down -- O(n^2)

For each node, compute the height of left and right subtrees separately, check the difference, then recurse on children. This recomputes heights repeatedly -- O(n) per node, O(n^2) total.

### Optimal: Bottom-Up with Early Termination -- O(n)

Compute height bottom-up and **return -1 as a sentinel** the moment an imbalance is detected. This way:
- Each node is visited exactly once
- An imbalance anywhere propagates up immediately, short-circuiting the rest of the tree

The key insight is combining two tasks into one recursive function: **compute height** and **detect imbalance**, using `-1` as the "not balanced" signal.



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

## Approach: Bottom-Up DFS -- O(n)

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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** ### Naive: Top-Down -- O(n^2)

**How the code works:**
- Each node is visited exactly once
- An imbalance anywhere propagates up immediately, short-circuiting the rest of the tree

**Walkthrough** — input `root = [3,9,20,null,null,15,7]`, expected output `true`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Why -1 Works as a Sentinel

Normal heights are always ≥ 0, so `-1` is an impossible height value. Once any subtree returns `-1`, every ancestor immediately returns `-1` without doing further work. This is the **early termination** that makes it O(n).

## Common Mistakes

- Computing height and checking balance in separate passes (top-down O(n^2))
- Forgetting to check `leftHeight == -1` **before** computing `rightHeight` (misses early termination)
- Confusing "balanced" with "perfect" or "complete" -- balanced only requires height difference ≤ 1 at every node

## Key Takeaways

- **Sentinel return value** (-1) to encode both height and validity in a single function is a clean pattern
- **Bottom-up > top-down** when you can avoid redundant computation
- This pattern generalizes: any tree property that depends on subtree properties can use bottom-up DFS with early exit

## Related Problems

- [104. Maximum Depth of Binary Tree](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/) -- height computation (base case for this problem)
- [543. Diameter of Binary Tree](https://www.leetcode.com/problems/diameter-of-binary-tree/) -- same bottom-up pattern, track max path
- [124. Binary Tree Maximum Path Sum](https://www.leetcode.com/problems/binary-tree-maximum-path-sum/) -- bottom-up with global max

## References

- [LC 110: Balanced Binary Tree on LeetCode](https://www.leetcode.com/problems/balanced-binary-tree/)
- [LeetCode Discuss — LC 110: Balanced Binary Tree](https://www.leetcode.com/problems/balanced-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/balanced-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
