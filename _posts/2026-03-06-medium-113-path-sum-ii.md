---
layout: post
title: "[Medium] 113. Path Sum II"
date: 2026-03-06
categories: [leetcode, medium, tree, dfs, backtracking]
tags: [leetcode, medium, tree, dfs, backtracking]
permalink: /2026/03/06/medium-113-path-sum-ii/
---

Given the `root` of a binary tree and an integer `targetSum`, return all **root-to-leaf** paths where the sum of the node values equals `targetSum`. Each path should be returned as a list of node values.

## Examples

**Example 1:**

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
          5
         / \
        4   8
       /   / \
      11  13  4
     / \     / \
    7   2   5   1
Output: [[5,4,11,2],[5,8,4,5]]
```

**Example 2:**

```
Input: root = [1,2,3], targetSum = 5
Output: []
```

**Example 3:**

```
Input: root = [1,2], targetSum = 1
Output: []
```

## Constraints

- The number of nodes is in `[0, 5000]`
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Thinking Process

This is [LC 112 Path Sum](/2026/03/06/easy-112-path-sum/) extended to **collect all valid paths** instead of just returning true/false.

### From LC 112 to LC 113

| LC 112 | LC 113 |
|---|---|
| Return `bool` | Return all matching paths |
| Can short-circuit on first match | Must explore the entire tree |
| No path tracking needed | Maintain a running path + backtrack |

### Backtracking Pattern

1. **Push** the current node's value onto the path
2. At a **leaf**, if remaining sum is `0`, copy the path to results
3. **Recurse** on children
4. **Pop** the current node (backtrack)

The push/pop ensures the path is always correct for the current branch.

## Approach: DFS + Backtracking -- $O(n^2)$

{% raw %}
```cpp
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> rtn;
        vector<int> pathNodes;
        traversePaths(root, targetSum, pathNodes, rtn);
        return rtn;
    }

private:
    void traversePaths(TreeNode* node, int remainingSum,
                       vector<int>& pathNodes, vector<vector<int>>& pathsList) {
        if (!node) return;

        remainingSum -= node->val;
        pathNodes.push_back(node->val);

        if (!node->left && !node->right && remainingSum == 0) {
            pathsList.push_back(pathNodes);
        } else {
            traversePaths(node->right, remainingSum, pathNodes, pathsList);
            traversePaths(node->left, remainingSum, pathNodes, pathsList);
        }

        pathNodes.pop_back();
    }
};
```
{% endraw %}

**Time**: $O(n^2)$ worst case -- visit $n$ nodes, each valid path copy is $O(n)$
**Space**: $O(h)$ recursion + path storage (excluding output)

## Common Mistakes

- Forgetting `pathNodes.pop_back()` after recursion (corrupts the path for sibling branches)
- Copying the path at every node instead of only at leaves
- Not handling the empty tree case (null root returns `[]`, not `[[]]`)

## Key Takeaways

- This is the **standard backtracking-on-tree** template: push → check/recurse → pop
- The transition from LC 112 → 113 is a common interview escalation: "now collect all answers"
- Same pattern applies to LC 257 (all root-to-leaf paths as strings)

## Related Problems

- [112. Path Sum](https://leetcode.com/problems/path-sum/) -- boolean version (does any path match?)
- [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/) -- path can start anywhere, prefix sum approach
- [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) -- collect all root-to-leaf paths

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
- [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/)
