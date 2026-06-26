---
layout: post
title: "[Medium] 894. All Possible Full Binary Trees"
date: 2026-04-12
categories: [leetcode, medium, tree, recursion, memoization]
tags: [leetcode, medium, tree, recursion, memoization, dp]
permalink: /2026/04/12/medium-894-all-possible-full-binary-trees/
---
Given an integer `n`, return a list of all possible **full binary trees** with `n` nodes. Each node has value `0`. A full binary tree is a tree where every node has either 0 or 2 children.

## Examples

**Example 1:**

```
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],
         [0,0,0,null,null,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,null,null,null,null,0,0],
         [0,0,0,0,0,null,null,0,0]]
(5 distinct full binary trees)
```

**Example 2:**

```
Input: n = 3
Output: [[0,0,0]]
(Only one: root with two leaves)
```

## Constraints

- `1 <= n <= 20`

## Thinking Process

### Key Observation

A full binary tree has the property: every internal node has exactly 2 children. This means:
- `n` must be **odd** (each subtree adds 2 nodes at a time, plus the root)
- If `n` is even, no full binary tree exists

### Recursive Structure

A full binary tree with `n` nodes has:
- 1 root node
- `i` nodes in the left subtree
- `n - 1 - i` nodes in the right subtree

where `i` is odd and ranges over `1, 3, 5, ..., n-2`.

For each split, recursively generate all left trees and all right trees, then combine every pair.

### Memoization

The same subproblem `allPossibleFBT(k)` may be called multiple times (e.g., both left and right subtrees can have the same size). Caching results avoids redundant computation.

### Walk-through (n=5)

```
n=5: root + split remaining 4 nodes
  i=1: left=FBT(1)=[leaf], right=FBT(3)=[root+2leaves]
    → 1 tree
  i=3: left=FBT(3)=[root+2leaves], right=FBT(1)=[leaf]
    → 1 tree

Total: 2 full binary trees with 5 nodes
```



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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

## Solution

{% raw %}
```cpp
class Solution {
public:
    vector<TreeNode*> allPossibleFBT(int n) {
        if (n % 2 == 0) return {};
        if (n == 1) return {new TreeNode(0)};
        if (memo.contains(n)) return memo[n];

        vector<TreeNode*> rtn;
        for (int i = 1; i < n; i += 2) {
            auto leftTree = allPossibleFBT(i);
            auto rightTree = allPossibleFBT(n - 1 - i);
            for (auto l : leftTree) {
                for (auto r : rightTree) {
                    TreeNode* root = new TreeNode(0);
                    root->left = l;
                    root->right = r;
                    rtn.push_back(root);
                }
            }
        }
        return memo[n] = rtn;
    }

private:
    unordered_map<int, vector<TreeNode*>> memo;
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** ### Key Observation

**How the code works:**
- `n` must be **odd** (each subtree adds 2 nodes at a time, plus the root)
- If `n` is even, no full binary tree exists
- 1 root node
- `i` nodes in the left subtree
- `n - 1 - i` nodes in the right subtree

**Walkthrough** — input `n = 7`, expected output `[[0,0,0,null,null,0,0,null,null,0,0],`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- Not checking for even `n` (no full binary tree exists)
- Stepping `i` by 1 instead of 2 (generates invalid subtree sizes)
- Forgetting to create a **new root** for each `(l, r)` combination (sharing root nodes across trees corrupts the output)

## Key Takeaways

- **"Generate all structurally unique trees"** = recursive decomposition by subtree sizes + memoization
- The odd-only constraint and step-by-2 iteration are specific to full binary trees
- Same pattern as LC 95 (Unique BSTs II) -- split, recurse, combine all pairs

## Related Problems

- [95. Unique Binary Search Trees II](https://www.leetcode.com/problems/unique-binary-search-trees-ii/) -- generate all BSTs (similar recursive structure)
- [96. Unique Binary Search Trees](https://www.leetcode.com/problems/unique-binary-search-trees/) -- count Catalan numbers
- [241. Different Ways to Add Parentheses](https://www.leetcode.com/problems/different-ways-to-add-parentheses/) -- recursive split + combine pattern
- [108. Convert Sorted Array to BST](https://www.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) -- tree construction

## References

- [LC 894: All Possible Full Binary Trees on LeetCode](https://www.leetcode.com/problems/all-possible-full-binary-trees/)
- [LeetCode Discuss — LC 894: All Possible Full Binary Trees](https://www.leetcode.com/problems/all-possible-full-binary-trees/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/all-possible-full-binary-trees/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
- [DP](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
