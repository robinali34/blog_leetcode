---
layout: post
title: "LeetCode 145. Binary Tree Postorder Traversal"
date: 2026-03-06
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, dfs, stack]
permalink: /2026/03/06/easy-145-binary-tree-postorder-traversal/
---

Given the `root` of a binary tree, return the **postorder** traversal of its nodes' values. Postorder visits: **left → right → root**.

## Examples

**Example 1:**

```
Input: root = [1,null,2,3]
    1
     \
      2
     /
    3
Output: [3,2,1]
```

**Example 2:**

```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,null,9]
Output: [4,6,7,5,2,9,8,3,1]
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

Postorder visits **left → right → root**. The tricky part is the iterative version -- we must visit both children before the parent.

### Iterative Trick: Modified Preorder + Reverse

Preorder is **root → left → right**. If we change it to **root → right → left** (push left before right), then reverse the result, we get **left → right → root** = postorder.

This avoids the complexity of tracking "has the right child been visited?"

### Two-Stack / Prev-Pointer Alternative

A more direct iterative approach uses a `prev` pointer to track whether we're returning from the right child, but the reverse trick is simpler to implement.

## Approach 1: Recursive -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> rtn;
        postorder(root, rtn);
        return rtn;
    }

private:
    void postorder(TreeNode* node, vector<int>& rtn) {
        if (!node) return;
        postorder(node->left, rtn);
        postorder(node->right, rtn);
        rtn.push_back(node->val);
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ for the output; $O(h)$ recursion stack

## Approach 2: Iterative (Modified Preorder + Reverse) -- $O(n)$

Do **root → right → left** traversal, then reverse the result to get **left → right → root**.

{% raw %}
```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> rtn;
        stack<TreeNode*> st;
        st.push(root);

        while (!st.empty()) {
            TreeNode* node = st.top(); st.pop();
            rtn.push_back(node->val);
            if (node->left) st.push(node->left);
            if (node->right) st.push(node->right);
        }

        reverse(rtn.begin(), rtn.end());
        return rtn;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ for the output; $O(h)$ for the stack

## Approach 3: Iterative (Prev Pointer) -- $O(n)$

Track the previously visited node. Only visit the current node when its right child is null or was just visited.

{% raw %}
```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> rtn;
        stack<TreeNode*> st;
        TreeNode* cur = root;
        TreeNode* prev = nullptr;

        while (cur || !st.empty()) {
            while (cur) {
                st.push(cur);
                cur = cur->left;
            }
            cur = st.top();
            if (!cur->right || cur->right == prev) {
                rtn.push_back(cur->val);
                st.pop();
                prev = cur;
                cur = nullptr;
            } else {
                cur = cur->right;
            }
        }

        return rtn;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ for the output; $O(h)$ for the stack

## Comparison Across All Three Traversal Orders

| Order | Visit when | Iterative stack trick |
|---|---|---|
| **Preorder** (root→L→R) | First encounter | Push right then left |
| **Inorder** (L→root→R) | After left subtree done | Go left, pop, visit, go right |
| **Postorder** (L→R→root) | After both children done | Reverse of (root→R→L), or use prev pointer |

## Key Takeaways

- **Reverse trick** turns postorder into a simple modification of preorder -- swap push order and reverse output
- **Prev pointer** approach is the "true" iterative postorder -- no reversal needed, but harder to get right
- All three traversal orders share the same $O(n)$ time and $O(h)$ auxiliary space structure

## Related Problems

- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) -- root before children
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) -- root between children
- [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) -- generalized to N-ary

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
