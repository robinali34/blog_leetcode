---
layout: post
title: "[Medium] 78. Subsets"
date: 2026-03-05
categories: [leetcode, medium, backtracking]
tags: [leetcode, medium, backtracking, dfs, bit-manipulation]
permalink: /2026/03/05/medium-78-subsets/
---

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set). The solution must not contain duplicate subsets.

## Examples

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All elements are **unique**

## Thinking Process

Every element has two choices: **include** or **exclude**. With `n` elements, there are $2^n$ subsets total.

### Backtracking Approach

Use DFS with a `start` index to avoid duplicates. At each level, we first record the current path as a valid subset, then try adding each remaining element and recurse.

### Walk-Through: `nums = [1, 2, 3]`

```
dfs(start=0, path=[])        → record []
├─ add 1 → dfs(start=1, path=[1])    → record [1]
│  ├─ add 2 → dfs(start=2, path=[1,2])  → record [1,2]
│  │  └─ add 3 → dfs(start=3, path=[1,2,3]) → record [1,2,3]
│  └─ add 3 → dfs(start=3, path=[1,3])  → record [1,3]
├─ add 2 → dfs(start=2, path=[2])    → record [2]
│  └─ add 3 → dfs(start=3, path=[2,3])  → record [2,3]
└─ add 3 → dfs(start=3, path=[3])    → record [3]
```

The `start` parameter ensures we only pick elements after the current index, preventing duplicate subsets like `[2,1]` when `[1,2]` already exists.

## Approach 1: Backtracking -- $O(n \cdot 2^n)$

{% raw %}
```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> rtn;
        vector<int> path;
        dfs(nums, 0, path, rtn);
        return rtn;
    }

private:
    void dfs(const vector<int>& nums, int start,
             vector<int>& path, vector<vector<int>>& rtn) {
        rtn.push_back(path);
        for (int i = start; i < (int)nums.size(); i++) {
            path.push_back(nums[i]);
            dfs(nums, i + 1, path, rtn);
            path.pop_back();
        }
    }
};
```
{% endraw %}

**Time**: $O(n \cdot 2^n)$ -- $2^n$ subsets, each up to $O(n)$ to copy
**Space**: $O(n)$ recursion depth (excluding output)

## Approach 2: Bitmask Enumeration -- $O(n \cdot 2^n)$

Each integer from `0` to `2^n - 1` represents a subset: bit `j` is set means include `nums[j]`.

{% raw %}
```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> rtn;

        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> subset;
            for (int j = 0; j < n; j++) {
                if (mask & (1 << j))
                    subset.push_back(nums[j]);
            }
            rtn.push_back(subset);
        }

        return rtn;
    }
};
```
{% endraw %}

**Time**: $O(n \cdot 2^n)$
**Space**: $O(n)$ per subset (excluding output)

## Common Mistakes

- Forgetting `path.pop_back()` after the recursive call (breaks backtracking)
- Using `i` instead of `i + 1` in the recursive call (generates permutations, not subsets)
- Not recording the path at the **start** of each call (misses the empty subset and partial subsets)

## Key Takeaways

- **Backtracking template**: push → recurse → pop. The `start` index prevents revisiting earlier elements
- **Bitmask alternative**: natural for small `n` ($\leq 20$), iterative and easy to reason about
- This is the foundation for LC 90 (Subsets II with duplicates) -- just add a sort + skip condition

## Related Problems

- [90. Subsets II](https://leetcode.com/problems/subsets-ii/) -- duplicates allowed, add skip logic
- [46. Permutations](https://leetcode.com/problems/permutations/) -- order matters, use visited array
- [77. Combinations](https://leetcode.com/problems/combinations/) -- fixed-size subsets
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/) -- subsets with target sum

## Template Reference

- [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/)
