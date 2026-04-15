---
layout: post
title: "[Easy] 94. Binary Tree Inorder Traversal"
date: 2026-03-06
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, dfs, stack, morris]
permalink: /2026/03/06/easy-94-binary-tree-inorder-traversal/
---

Given the `root` of a binary tree, return the **inorder** traversal of its nodes' values. Inorder visits: **left → root → right**.

## Examples

**Example 1:**

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [1,3,2]
```

**Example 2:**

```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,null,9]
Output: [4,2,6,5,7,1,3,8,9]
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

Inorder traversal processes nodes in **left → root → right** order. For a BST, this produces sorted output.

Three standard implementations:

1. **Recursive** -- direct translation
2. **Iterative (stack)** -- go as far left as possible, then process and go right
3. **Morris traversal** -- $O(1)$ auxiliary space using threaded tree

### Iterative Key Insight

Unlike preorder where we can simply push right then left, inorder requires us to **defer** visiting a node until its entire left subtree is processed. The pattern is: push all left children onto the stack, pop and visit, then move to the right child.

## Approach 1: Recursive -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> rtn;
        inorder(root, rtn);
        return rtn;
    }

private:
    void inorder(TreeNode* node, vector<int>& rtn) {
        if (!node) return;
        inorder(node->left, rtn);
        rtn.push_back(node->val);
        inorder(node->right, rtn);
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ for the output; $O(h)$ recursion stack

## Approach 2: Iterative (Stack) -- $O(n)$

Push all left children first. When there's nothing left to go, pop, visit, and move right.

{% raw %}
```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> rtn;
        stack<TreeNode*> st;
        TreeNode* cur = root;

        while (cur || !st.empty()) {
            while (cur) {
                st.push(cur);
                cur = cur->left;
            }
            cur = st.top(); st.pop();
            rtn.push_back(cur->val);
            cur = cur->right;
        }

        return rtn;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ for the output; $O(h)$ for the stack

## Approach 3: Morris Traversal -- $O(n)$

Thread the rightmost node of the left subtree back to the current node. Visit the node **after** returning via the thread (between left and right).

{% raw %}
```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
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
                    pred->right = cur;
                    cur = cur->left;
                } else {
                    pred->right = nullptr;
                    rtn.push_back(cur->val);
                    cur = cur->right;
                }
            }
        }

        return rtn;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ for the output; $O(1)$ auxiliary

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Recursive | $O(n)$ | $O(h)$ aux | Simplest |
| Iterative Stack | $O(n)$ | $O(h)$ aux | "Go left, pop, go right" pattern |
| Morris | $O(n)$ | $O(1)$ aux | Modifies tree temporarily, restores it |

## Preorder vs Inorder: Key Difference

The Morris and iterative templates are almost identical across traversal orders. The only difference is **when** you record the node's value:

| Order | Record when... |
|---|---|
| Preorder | **Before** going left (first visit) |
| Inorder | **After** returning from left (second visit / thread return) |

## Key Takeaways

- **Iterative inorder** = "go left as far as possible, pop, visit, go right" -- this is the most commonly tested iterative pattern
- **Morris inorder** visits the node when it encounters the thread for the **second time** (thread already exists), unlike preorder which visits on the first encounter
- For a BST, inorder traversal yields sorted order -- useful for validation and kth-element problems

## Related Problems

- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) -- root before children
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) -- root after children
- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) -- inorder + early stop
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) -- inorder must be strictly increasing

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
