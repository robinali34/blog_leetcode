---
layout: post
title: "[Medium] 64. Minimum Path Sum"
date: 2026-01-10 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming, matrix]
permalink: /2026/01/10/medium-64-minimum-path-sum/
tags: [leetcode, medium, array, dynamic-programming, matrix, grid]
---
Given a `m x n` `grid` filled with non-negative numbers, find a path from top-left to bottom-right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

## Thinking Process

1. **2D DP Pattern**: Classic grid DP problem with optimal substructure

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">2D DP on grid</text>

  <rect x="40" y="40" width="32" height="28" rx="2" fill="#D4D8E0" stroke="#8B8680"/><text x="56" y="56" text-anchor="middle" font-size="10">1</text>
  <rect x="72" y="40" width="32" height="28" rx="2" fill="#E8E3D8" stroke="#B8B5B0"/><text x="88" y="56" text-anchor="middle" font-size="10">1</text>
  <rect x="104" y="40" width="32" height="28" rx="2" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="56" text-anchor="middle" font-size="10">1</text>
  <rect x="40" y="68" width="32" height="28" rx="2" fill="#E8E3D8" stroke="#B8B5B0"/><text x="56" y="84" text-anchor="middle" font-size="10">1</text>
  <rect x="72" y="68" width="32" height="28" rx="2" fill="#E0D8E4" stroke="#A098A8"/><text x="88" y="84" text-anchor="middle" font-size="10">2</text>
  <rect x="104" y="68" width="32" height="28" rx="2" fill="#E8D5D0" stroke="#B8A5A0"/><text x="120" y="84" text-anchor="middle" font-size="10">3</text>
  <text x="140" y="65" font-size="10" fill="#C4956A">← + ↑</text>
  <text x="90" y="115" text-anchor="middle" font-size="11" fill="#6B6560">cell from top + left neighbors</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

## Examples

**Example 1:**
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
```

**Example 2:**
```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
Explanation: The path is 1 → 2 → 3 → 6.
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

## Space Optimization

We can optimize space to O(min(m, n)) by using a 1D array:

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        const int N = grid.size(), M = grid[0].size();
        vector<int> dp(M);
        
        // Initialize first row
        dp[0] = grid[0][0];
        for(int j = 1; j < M; j++) {
            dp[j] = dp[j-1] + grid[0][j];
        }
        
        // Process remaining rows
        for(int i = 1; i < N; i++) {
            dp[0] += grid[i][0];  // First column
            for(int j = 1; j < M; j++) {
                dp[j] = grid[i][j] + min(dp[j], dp[j-1]);
            }
        }
        
        return dp[M-1];
    }
};
```

**Key Insight**: We only need the previous row to compute the current row, so we can use a 1D array and update it row by row.

## Common Mistakes

1. **Single cell**: `grid = [[5]]` → return `5`
2. **Single row**: `grid = [[1,2,3]]` → return `6` (sum of row)
3. **Single column**: `grid = [[1],[2],[3]]` → return `6` (sum of column)
4. **All zeros**: `grid = [[0,0],[0,0]]` → return `0`

1. **Wrong initialization**: Not handling first row/column separately
2. **Index errors**: Off-by-one errors in loops
3. **Wrong recurrence**: Using `max` instead of `min`
4. **Base case errors**: Not initializing `dp[0][0]` correctly
5. **Empty grid**: Not handling empty grid case

## Related Problems

- [LC 62: Unique Paths](https://www.leetcode.com/problems/unique-paths/) - Count paths (similar structure)
- [LC 63: Unique Paths II](https://www.leetcode.com/problems/unique-paths-ii/) - With obstacles
- [LC 120: Triangle](https://www.leetcode.com/problems/triangle/) - Triangular grid minimum path
- [LC 174: Dungeon Game](https://www.leetcode.com/problems/dungeon-game/) - Reverse DP approach
- [LC 931: Minimum Falling Path Sum](https://www.leetcode.com/problems/minimum-falling-path-sum/) - 3-directional moves

## Key Takeaways

1. **2D DP Pattern**: Classic grid DP problem with optimal substructure
2. **Base Cases**: First row and column have only one path
3. **Recurrence**: Choose minimum of top or left neighbor
4. **Space Optimization**: Can reduce to O(min(m, n)) using rolling array

## References

- [LC 64: Minimum Path Sum on LeetCode](https://www.leetcode.com/problems/minimum-path-sum/)
- [LeetCode Discuss — LC 64: Minimum Path Sum](https://www.leetcode.com/problems/minimum-path-sum/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-path-sum/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
