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

## Solution: Recursive + Memoization -- $O(2^{n/2})$

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
{% endraw %}

**Time**: $O(2^{n/2})$ -- the number of full binary trees grows as Catalan numbers
**Space**: $O(n \cdot 2^{n/2})$ -- storing all trees in the memo

## Key Details

**Why `i += 2`?** Both subtrees must be full binary trees, so both must have an odd number of nodes. Starting at 1 and stepping by 2 ensures `i` and `n - 1 - i` are both odd.

**Why memoization helps**: `FBT(3)` might be needed as a left subtree for `FBT(7)` in multiple splits, and also as a right subtree. Caching avoids regenerating the same trees.

**Catalan numbers**: The count of full binary trees with $n$ nodes (where $n = 2k+1$) is the $k$-th Catalan number: $C_k = \frac{1}{k+1}\binom{2k}{k}$.

| n | Trees |
|---|---|
| 1 | 1 |
| 3 | 1 |
| 5 | 2 |
| 7 | 5 |
| 9 | 14 |
| 11 | 42 |

## Common Mistakes

- Not checking for even `n` (no full binary tree exists)
- Stepping `i` by 1 instead of 2 (generates invalid subtree sizes)
- Forgetting to create a **new root** for each `(l, r)` combination (sharing root nodes across trees corrupts the output)

## Key Takeaways

- **"Generate all structurally unique trees"** = recursive decomposition by subtree sizes + memoization
- The odd-only constraint and step-by-2 iteration are specific to full binary trees
- Same pattern as LC 95 (Unique BSTs II) -- split, recurse, combine all pairs

## Related Problems

- [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) -- generate all BSTs (similar recursive structure)
- [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) -- count Catalan numbers
- [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) -- recursive split + combine pattern
- [108. Convert Sorted Array to BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) -- tree construction

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
- [DP](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
