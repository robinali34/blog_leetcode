---
layout: post
title: "[Easy] 144. Binary Tree Preorder Traversal"
date: 2026-03-06
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, dfs, stack, morris]
permalink: /2026/03/06/easy-144-binary-tree-preorder-traversal/
---
Given the `root` of a binary tree, return the **preorder** traversal of its nodes' values. Preorder visits: **root → left → right**.

## Examples

**Example 1:**

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1,2,3]
```

**Example 2:**

```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,null,9]
Output: [1,2,4,5,6,7,3,8,9]
```

**Example 3:**

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes is in `[0, 100]`
- `-100 <= Node.val <= 100`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Thinking Process

Preorder traversal processes nodes in **root → left → right** order. Three standard implementations exist:

1. **Recursive** -- direct translation of the definition
2. **Iterative (stack)** -- simulate recursion with an explicit stack
3. **Morris traversal** -- O(1) space using threaded tree

### Why Know All Three?

The recursive solution is trivial. Interviewers often follow up with "can you do it iteratively?" or "can you do it in O(1) space?" -- that's where the stack and Morris approaches matter.

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

## Approach 1: Recursive -- O(n)
```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> rtn;
        preorder(root, rtn);
        return rtn;
    }

private:
    void preorder(TreeNode* node, vector<int>& rtn) {
        if (!node) return;
        rtn.push_back(node->val);
        preorder(node->left, rtn);
        preorder(node->right, rtn);
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** Preorder traversal processes nodes in **root → left → right** order. Three standard implementations exist:

**How the code works:**
1. **Recursive** -- direct translation of the definition
2. **Iterative (stack)** -- simulate recursion with an explicit stack
3. **Morris traversal** -- O(1) space using threaded tree

**Walkthrough** — input `root = [1,null,2,3]`, expected output `[1,2,3]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Approach 2: Iterative (Stack) -- O(n)

Push right child first, then left, so left is processed first (LIFO).
```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> rtn;
        stack<TreeNode*> st;
        st.push(root);

        while (!st.empty()) {
            TreeNode* node = st.top(); st.pop();
            rtn.push_back(node->val);
            if (node->right) st.push(node->right);
            if (node->left) st.push(node->left);
        }

        return rtn;
    }
};
```

**Time**: O(n)
**Space**: O(h) for the stack

## Approach 3: Morris Traversal -- O(n) time, O(n) space

Use the tree's null pointers to thread back to ancestors, avoiding a stack entirely. For preorder: visit the node **before** following the thread.
```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> rtn;
        TreeNode* cur = root;

        while (cur) {
            if (!cur->left) {
                rtn.push_back(cur->val);
                cur = cur->right;
            } else {
                TreeNode* pred = cur->left;
                while (pred->right && pred->right != cur)
                    pred = pred->right;

                if (!pred->right) {
                    rtn.push_back(cur->val);
                    pred->right = cur;
                    cur = cur->left;
                } else {
                    pred->right = nullptr;
                    cur = cur->right;
                }
            }
        }

        return rtn;
    }
};
```

**Time**: O(n) -- each edge traversed at most twice
**Space**: O(n) for the output vector; O(1) auxiliary

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Recursive | O(n) | O(h) | Simplest, may stack overflow on deep trees |
| Iterative Stack | O(n) | O(h) | Common interview follow-up |
| Morris | O(n) | O(n) | O(1) auxiliary; modifies tree temporarily, restores it |

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

- All three traversal orders (pre/in/post) share the same three implementation strategies
- **Iterative stack trick for preorder**: push right before left so left pops first
- **Morris**: useful when O(1) space is required; temporarily modifies the tree but restores it

## Related Problems

- [94. Binary Tree Inorder Traversal](https://www.leetcode.com/problems/binary-tree-inorder-traversal/) -- root between left and right
- [145. Binary Tree Postorder Traversal](https://www.leetcode.com/problems/binary-tree-postorder-traversal/) -- root after children
- [102. Binary Tree Level Order Traversal](https://www.leetcode.com/problems/binary-tree-level-order-traversal/) -- BFS approach

## References

- [LC 144: Binary Tree Preorder Traversal on LeetCode](https://www.leetcode.com/problems/binary-tree-preorder-traversal/)
- [LeetCode Discuss — LC 144: Binary Tree Preorder Traversal](https://www.leetcode.com/problems/binary-tree-preorder-traversal/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/binary-tree-preorder-traversal/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
