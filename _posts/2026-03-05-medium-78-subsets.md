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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | $O(n)$ | $O(h)$ stack | Natural for trees and graphs |
| Iterative DFS (stack) | $O(n)$ | $O(n)$ | Avoid recursion depth limits |
| DFS with memoization | $O(n)$ | $O(n)$ | Overlapping subproblems on graphs |
| Backtracking DFS | $O(2^n)$ typical | $O(n)$ | Enumerate choices with pruning |

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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** Every element has two choices: **include** or **exclude**. With `n` elements, there are $2^n$ subsets total.

**Walkthrough** — input `nums = [1,2,3]`, expected output `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
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

- [90. Subsets II](https://www.leetcode.com/problems/subsets-ii/) -- duplicates allowed, add skip logic
- [46. Permutations](https://www.leetcode.com/problems/permutations/) -- order matters, use visited array
- [77. Combinations](https://www.leetcode.com/problems/combinations/) -- fixed-size subsets
- [39. Combination Sum](https://www.leetcode.com/problems/combination-sum/) -- subsets with target sum

## References

- [LC 78: Subsets on LeetCode](https://www.leetcode.com/problems/subsets/)
- [LeetCode Discuss — LC 78: Subsets](https://www.leetcode.com/problems/subsets/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/subsets/editorial/) *(may require premium)*

## Template Reference

- [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/)
