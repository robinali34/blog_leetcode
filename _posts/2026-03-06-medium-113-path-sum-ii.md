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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

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

## Approach: DFS + Backtracking -- O(n^2)
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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** This is [LC 112 Path Sum](/2026/03/06/easy-112-path-sum/) extended to **collect all valid paths** instead of just returning true/false.

**How the code works:**
1. **Push** the current node's value onto the path
2. At a **leaf**, if remaining sum is `0`, copy the path to results
3. **Recurse** on children
4. **Pop** the current node (backtrack)

**Walkthrough** — input `root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22`, expected output `[[5,4,11,2],[5,8,4,5]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- Forgetting `pathNodes.pop_back()` after recursion (corrupts the path for sibling branches)
- Copying the path at every node instead of only at leaves
- Not handling the empty tree case (null root returns `[]`, not `[[]]`)

## Key Takeaways

- This is the **standard backtracking-on-tree** template: push → check/recurse → pop
- The transition from LC 112 → 113 is a common interview escalation: "now collect all answers"
- Same pattern applies to LC 257 (all root-to-leaf paths as strings)

## Related Problems

- [112. Path Sum](https://www.leetcode.com/problems/path-sum/) -- boolean version (does any path match?)
- [437. Path Sum III](https://www.leetcode.com/problems/path-sum-iii/) -- path can start anywhere, prefix sum approach
- [257. Binary Tree Paths](https://www.leetcode.com/problems/binary-tree-paths/) -- collect all root-to-leaf paths

## References

- [LC 113: Path Sum II on LeetCode](https://www.leetcode.com/problems/path-sum-ii/)
- [LeetCode Discuss — LC 113: Path Sum II](https://www.leetcode.com/problems/path-sum-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/path-sum-ii/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
- [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/)
