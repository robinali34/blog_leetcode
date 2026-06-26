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



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | $O(n)$ | $O(h)$ stack | Natural for trees and graphs |
| Iterative DFS (stack) | $O(n)$ | $O(n)$ | Avoid recursion depth limits |
| DFS with memoization | $O(n)$ | $O(n)$ | Overlapping subproblems on graphs |
| Backtracking DFS | $O(2^n)$ typical | $O(n)$ | Enumerate choices with pruning |

## Solution

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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** A node is "good" if `node->val >= max value on the path from root to this node`. So we need to carry the **running maximum** as we traverse downward.

**How the code works:**
1. Start DFS from root with `maxVal = INT_MIN` (or `root->val`)
2. At each node: if `node->val >= maxVal`, it's good -- increment count
3. Update `maxVal = max(maxVal, node->val)` and recurse on children

**Walkthrough** — input `root = [3,1,4,3,null,1,5]`, expected output `4`:

Good nodes: 3 (root), 3 (left-left), 4, 5.
Node 1 is not good because 3 > 1 on its path.
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

- [112. Path Sum](https://www.leetcode.com/problems/path-sum/) -- top-down DFS carrying remaining sum
- [113. Path Sum II](https://www.leetcode.com/problems/path-sum-ii/) -- top-down DFS with path tracking
- [1376. Time Needed to Inform All Employees](https://www.leetcode.com/problems/time-needed-to-inform-all-employees/) -- DFS with accumulated state
- [124. Binary Tree Maximum Path Sum](https://www.leetcode.com/problems/binary-tree-maximum-path-sum/) -- path value tracking

## References

- [LC 1448: Count Good Nodes in Binary Tree on LeetCode](https://www.leetcode.com/problems/count-good-nodes-in-binary-tree/)
- [LeetCode Discuss — LC 1448: Count Good Nodes in Binary Tree](https://www.leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/count-good-nodes-in-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
