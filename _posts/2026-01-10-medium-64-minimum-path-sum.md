---
layout: post
title: "64. Minimum Path Sum"
date: 2026-01-10 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming, matrix]
permalink: /2026/01/10/medium-64-minimum-path-sum/
tags: [leetcode, medium, array, dynamic-programming, matrix, grid]
---

# 64. Minimum Path Sum

## Problem Statement

Given a `m x n` `grid` filled with non-negative numbers, find a path from top-left to bottom-right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Movement direction**: In which directions can we move? (Assumption: Only right and down - typical grid path problem constraint)

2. **Starting/ending cells**: Where do we start and end? (Assumption: Start at top-left (0,0), end at bottom-right (m-1, n-1))

3. **Path sum**: What should we include in the path sum? (Assumption: Sum includes both starting and ending cells - all cells along the path)

4. **Grid boundaries**: Can we move outside the grid? (Assumption: No - must stay within grid bounds)

5. **Negative values**: Can grid values be negative? (Assumption: Based on constraints, values are >= 0, but should clarify if negative values are possible)

## Solution Approach

This is a classic **2D dynamic programming** problem. The key insight is that to reach cell `(i, j)`, we can only come from `(i-1, j)` (top) or `(i, j-1)` (left). We choose the path with minimum cost.

### Key Insights:

1. **DP State**: `dp[i][j]` = minimum path sum to reach cell `(i, j)`
2. **Base Cases**: 
   - `dp[0][0] = grid[0][0]` (starting cell)
   - First row: can only come from left
   - First column: can only come from top
3. **Recurrence**: `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`
4. **Answer**: `dp[m-1][n-1]` (bottom-right corner)

### Algorithm:

1. **Initialize**: `dp = grid` (copy grid to dp)
2. **Fill first row**: `dp[0][j] += dp[0][j-1]` for `j > 0`
3. **Fill first column**: `dp[i][0] += dp[i-1][0]` for `i > 0`
4. **Fill remaining cells**: `dp[i][j] += min(dp[i-1][j], dp[i][j-1])`
5. **Return**: `dp[m-1][n-1]`

## Solution

### **Solution: 2D Dynamic Programming**

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        //dp: min sum to reach i, j grid
        // dp[0][0] = grid[0][0]
        // dp[i][0] = grid[i][0] + dp[i - 1][0]
        // dp[0][j] = grid[0][j] + dp[0][j - 1]
        // dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        const int N = grid.size(), M = grid[0].size();
        if(N == 0 || M == 0) return 0;
        vector<vector<int>> dp = grid;

        for(int i = 1; i < N; i++) {
            dp[i][0] += dp[i - 1][0];
        }
        for(int j = 1; j < M; j++) {
            dp[0][j] += dp[0][j - 1];
        }

        for(int i = 1; i < N; i++) {
            for(int j = 1; j < M; j++) {
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[N - 1][M - 1];
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 9-10)**:
   - Get dimensions `N` (rows) and `M` (columns)
   - Handle edge case: empty grid returns 0
   - Copy `grid` to `dp` (we'll modify `dp` in-place)

2. **Fill First Column (Lines 12-14)**:
   - For each row `i > 0`: `dp[i][0] += dp[i-1][0]`
   - First column cells can only be reached from above
   - Accumulate the sum going down

3. **Fill First Row (Lines 15-17)**:
   - For each column `j > 0`: `dp[0][j] += dp[0][j-1]`
   - First row cells can only be reached from left
   - Accumulate the sum going right

4. **Fill Remaining Cells (Lines 19-23)**:
   - For each cell `(i, j)` where `i > 0` and `j > 0`:
     - `dp[i][j] += min(dp[i-1][j], dp[i][j-1])`
     - Choose the minimum cost path (from top or left)
     - Add current cell's value

5. **Return (Line 24)**: `dp[N-1][M-1]` (minimum path sum to bottom-right)

### **Why This Works:**

- **Optimal Substructure**: Minimum path to `(i, j)` = current cost + minimum of paths from `(i-1, j)` or `(i, j-1)`
- **Base Cases**: First row and column have only one path, so we accumulate sums
- **Greedy Choice**: At each cell, choose the path with minimum cost so far
- **Bottom-Up DP**: Build solution from smaller subproblems (top-left) to larger (bottom-right)

### **Example Walkthrough:**

**For `grid = [[1,3,1],[1,5,1],[4,2,1]]`:**

```
Initial grid:
[1, 3, 1]
[1, 5, 1]
[4, 2, 1]

Step 1: Initialize dp = grid
dp = [[1, 3, 1],
      [1, 5, 1],
      [4, 2, 1]]

Step 2: Fill first column (i=1,2)
i=1: dp[1][0] += dp[0][0] → dp[1][0] = 1 + 1 = 2
i=2: dp[2][0] += dp[1][0] → dp[2][0] = 4 + 2 = 6
dp = [[1, 3, 1],
      [2, 5, 1],
      [6, 2, 1]]

Step 3: Fill first row (j=1,2)
j=1: dp[0][1] += dp[0][0] → dp[0][1] = 3 + 1 = 4
j=2: dp[0][2] += dp[0][1] → dp[0][2] = 1 + 4 = 5
dp = [[1, 4, 5],
      [2, 5, 1],
      [6, 2, 1]]

Step 4: Fill remaining cells
i=1, j=1: dp[1][1] += min(dp[0][1], dp[1][0])
          = 5 + min(4, 2) = 5 + 2 = 7
i=1, j=2: dp[1][2] += min(dp[0][2], dp[1][1])
          = 1 + min(5, 7) = 1 + 5 = 6
i=2, j=1: dp[2][1] += min(dp[1][1], dp[2][0])
          = 2 + min(7, 6) = 2 + 6 = 8
i=2, j=2: dp[2][2] += min(dp[1][2], dp[2][1])
          = 1 + min(6, 8) = 1 + 6 = 7

Final dp:
[[1, 4, 5],
 [2, 7, 6],
 [6, 8, 7]]

Result: dp[2][2] = 7

Path: 1 → 3 → 1 → 1 → 1 (sum = 7)
```

### **Complexity Analysis:**

- **Time Complexity:** O(m × n)
  - Visit each cell exactly once
  - Constant time operations per cell
  - Total: O(m × n)
- **Space Complexity:** O(m × n)
  - `dp` array of size `m × n`
  - Can be optimized to O(min(m, n)) using rolling array

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

## Key Insights

1. **2D DP Pattern**: Classic grid DP problem with optimal substructure
2. **Base Cases**: First row and column have only one path
3. **Recurrence**: Choose minimum of top or left neighbor
4. **Space Optimization**: Can reduce to O(min(m, n)) using rolling array

## Edge Cases

1. **Single cell**: `grid = [[5]]` → return `5`
2. **Single row**: `grid = [[1,2,3]]` → return `6` (sum of row)
3. **Single column**: `grid = [[1],[2],[3]]` → return `6` (sum of column)
4. **All zeros**: `grid = [[0,0],[0,0]]` → return `0`

## Common Mistakes

1. **Wrong initialization**: Not handling first row/column separately
2. **Index errors**: Off-by-one errors in loops
3. **Wrong recurrence**: Using `max` instead of `min`
4. **Base case errors**: Not initializing `dp[0][0]` correctly
5. **Empty grid**: Not handling empty grid case

## Related Problems

- [LC 62: Unique Paths](https://leetcode.com/problems/unique-paths/) - Count paths (similar structure)
- [LC 63: Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) - With obstacles
- [LC 120: Triangle](https://leetcode.com/problems/triangle/) - Triangular grid minimum path
- [LC 174: Dungeon Game](https://leetcode.com/problems/dungeon-game/) - Reverse DP approach
- [LC 931: Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) - 3-directional moves

---

*This problem demonstrates the classic 2D DP pattern for grid path problems. The key is recognizing the optimal substructure and building the solution bottom-up from base cases.*

