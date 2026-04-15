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

## Thinking Process

Preorder traversal processes nodes in **root → left → right** order. Three standard implementations exist:

1. **Recursive** -- direct translation of the definition
2. **Iterative (stack)** -- simulate recursion with an explicit stack
3. **Morris traversal** -- $O(1)$ space using threaded tree

### Why Know All Three?

The recursive solution is trivial. Interviewers often follow up with "can you do it iteratively?" or "can you do it in O(1) space?" -- that's where the stack and Morris approaches matter.

## Approach 1: Recursive -- $O(n)$

{% raw %}
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
{% endraw %}

**Time**: $O(n)$
**Space**: $O(h)$ recursion stack, where $h$ is tree height ($O(\log n)$ balanced, $O(n)$ skewed)

## Approach 2: Iterative (Stack) -- $O(n)$

Push right child first, then left, so left is processed first (LIFO).

{% raw %}
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
{% endraw %}

**Time**: $O(n)$
**Space**: $O(h)$ for the stack

## Approach 3: Morris Traversal -- $O(n)$ time, $O(n)$ space

Use the tree's null pointers to thread back to ancestors, avoiding a stack entirely. For preorder: visit the node **before** following the thread.

{% raw %}
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
{% endraw %}

**Time**: $O(n)$ -- each edge traversed at most twice
**Space**: $O(n)$ for the output vector; $O(1)$ auxiliary

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Recursive | $O(n)$ | $O(h)$ | Simplest, may stack overflow on deep trees |
| Iterative Stack | $O(n)$ | $O(h)$ | Common interview follow-up |
| Morris | $O(n)$ | $O(n)$ | $O(1)$ auxiliary; modifies tree temporarily, restores it |

## Key Takeaways

- All three traversal orders (pre/in/post) share the same three implementation strategies
- **Iterative stack trick for preorder**: push right before left so left pops first
- **Morris**: useful when $O(1)$ space is required; temporarily modifies the tree but restores it

## Related Problems

- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) -- root between left and right
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) -- root after children
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) -- BFS approach

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
