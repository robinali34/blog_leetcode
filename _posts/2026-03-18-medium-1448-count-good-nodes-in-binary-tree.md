---
layout: post
title: "[Medium] 1448. Count Good Nodes in Binary Tree"
date: 2026-03-18
categories: [leetcode, medium, tree, dfs, bfs]
tags: [leetcode, medium, tree, dfs, bfs]
permalink: /2026/03/18/medium-1448-count-good-nodes-in-binary-tree/
---

Given a binary tree, a node `X` is **good** if there is no node with a value greater than `X` on the path from root to `X`. Return the number of good nodes in the tree. The root is always a good node.

## Examples

**Example 1:**

```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Good nodes: 3 (root), 3 (left-left), 4, 5.
Node 1 is not good because 3 > 1 on its path.
```

**Example 2:**

```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Good nodes: 3 (root), 3, 4.
```

**Example 3:**

```
Input: root = [1]
Output: 1
```

## Constraints

- Number of nodes in the tree is in the range `[1, 10^5]`
- `-10^4 <= Node.val <= 10^4`

## Thinking Process

A node is "good" if `node->val >= max value on the path from root to this node`. So we need to carry the **running maximum** as we traverse downward.

This is a classic **top-down DFS with state** pattern: pass extra information (the path maximum) from parent to child.

### Algorithm

1. Start DFS from root with `maxVal = INT_MIN` (or `root->val`)
2. At each node: if `node->val >= maxVal`, it's good -- increment count
3. Update `maxVal = max(maxVal, node->val)` and recurse on children

## Solution 1: Recursive DFS -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    int goodNodes(TreeNode* root) {
        cnt = 0;
        dfs(root, INT_MIN);
        return cnt;
    }

private:
    int cnt;
    void dfs(TreeNode* node, int maxVal) {
        if (!node) return;
        if (node->val >= maxVal) {
            cnt++;
            maxVal = node->val;
        }
        dfs(node->left, maxVal);
        dfs(node->right, maxVal);
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(h)$ -- recursion stack, $O(n)$ worst case for skewed tree

## Solution 2: Iterative DFS (Stack) -- $O(n)$

Carry `maxVal` alongside each node in the stack.

{% raw %}
```cpp
class Solution {
public:
    int goodNodes(TreeNode* root) {
        if (!root) return 0;
        int count = 0;
        stack<pair<TreeNode*, int>> stk;
        stk.push({root, root->val});

        while (!stk.empty()) {
            auto [node, maxVal] = stk.top();
            stk.pop();
            if (node->val >= maxVal) count++;
            int newMax = max(maxVal, node->val);
            if (node->right) stk.push({node->right, newMax});
            if (node->left) stk.push({node->left, newMax});
        }

        return count;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(h)$

## Solution 3: BFS (Queue) -- $O(n)$

Same idea, but level-by-level with a queue. Each entry carries its path maximum.

{% raw %}
```cpp
class Solution {
public:
    int goodNodes(TreeNode* root) {
        if (!root) return 0;
        int count = 0;
        queue<pair<TreeNode*, int>> q;
        q.push({root, root->val});

        while (!q.empty()) {
            auto [node, maxVal] = q.front();
            q.pop();
            if (node->val >= maxVal) count++;
            int newMax = max(maxVal, node->val);
            if (node->left) q.push({node->left, newMax});
            if (node->right) q.push({node->right, newMax});
        }

        return count;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(w)$ where $w$ is the maximum width of the tree

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Recursive DFS | $O(n)$ | $O(h)$ | Cleanest, natural top-down |
| Iterative DFS | $O(n)$ | $O(h)$ | Avoids stack overflow |
| BFS | $O(n)$ | $O(w)$ | Level-order, wider space for balanced trees |

## Common Mistakes

- Forgetting that the root is always good (initializing `maxVal` too high)
- Not updating `maxVal` when the current node is good
- Using `>` instead of `>=` (a node equal to the path max is still good)

## Key Takeaways

- **"Check property along root-to-node path"** = top-down DFS carrying state
- The pattern of passing a running aggregate (max, sum, etc.) downward appears in many tree problems
- All three traversal styles (recursive DFS, iterative DFS, BFS) work here since we only need to visit every node once with its path context

## Related Problems

- [112. Path Sum](https://leetcode.com/problems/path-sum/) -- top-down DFS carrying remaining sum
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/) -- top-down DFS with path tracking
- [1376. Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) -- DFS with accumulated state
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) -- path value tracking

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
