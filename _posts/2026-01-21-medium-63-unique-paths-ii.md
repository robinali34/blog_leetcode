---
layout: post
title: "63. Unique Paths II"
date: 2026-01-21 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming, matrix]
permalink: /2026/01/21/medium-63-unique-paths-ii/
tags: [leetcode, medium, array, dynamic-programming, matrix, grid, obstacles]
---

# 63. Unique Paths II

## Problem Statement

You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` and `0` respectively in `grid`. A path that the robot takes cannot include **any square that is an obstacle**.

Return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

## Examples

**Example 1:**
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

**Example 2:**
```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

**Example 3:**
```
Input: obstacleGrid = [[1,0]]
Output: 0
Explanation: The starting cell is blocked, so no path exists.
```

## Constraints

- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`

## Solution Approach

This is a **2D dynamic programming** problem similar to Unique Paths (LC 62), but with obstacles blocking certain cells. The key insight is that if a cell contains an obstacle, there are 0 ways to reach it.

### Key Insights:

1. **DP State**: `dp[i][j]` = number of unique paths to reach cell `(i, j)`
2. **Base Cases**: 
   - If `obstacleGrid[0][0] == 1`, return 0 (starting cell blocked)
   - `dp[0][0] = 1` if no obstacle
   - First row: can only come from left, but if obstacle encountered, all subsequent cells are 0
   - First column: can only come from top, but if obstacle encountered, all subsequent cells are 0
3. **Recurrence**: 
   - If `obstacleGrid[i][j] == 1`: `dp[i][j] = 0`
   - Otherwise: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
4. **Answer**: `dp[m-1][n-1]` (bottom-right corner)

### Space Optimization:

We can optimize space from O(m×n) to O(n) by using a 1D array since we only need the previous row.

## Solution

### **Solution 1: Space-Optimized DP (O(n) space)**

```cpp
class Solution {
public:
    /*
        f(i, j) = 0 if obstacleGrid[i][j] == 1
        f(i, j) = f(i-1, j) + f(i, j-1), if obstacleGrid[i][j] == 0
    */
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        const int N = obstacleGrid.size(), M = obstacleGrid[0].size();
        vector<int> dp(M, 0);
        dp[0] = (obstacleGrid[0][0] == 0) ? 1 : 0;
        
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                }
                else if(j > 0) {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp.back();
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 8-9)**:
   - Get dimensions `N` (rows) and `M` (columns)
   - Initialize `dp` array of size `M` (columns) with zeros
   - Set `dp[0] = 1` if starting cell has no obstacle, else `0`

2. **Process Each Row (Lines 11-19)**:
   - For each row `i` from `0` to `N-1`:
     - For each column `j` from `0` to `M-1`:
       - **If obstacle (Line 13)**: Set `dp[j] = 0` (no paths through obstacle)
       - **Else if not first column (Line 15)**: `dp[j] += dp[j-1]`
         - This accumulates paths from left (`dp[j-1]`) with paths from top (already in `dp[j]`)

3. **Return (Line 20)**: `dp.back()` = `dp[M-1]` (number of paths to bottom-right)

### **Why This Works:**

- **Space Optimization**: Using 1D array `dp[j]` stores paths to current row
  - Before update: `dp[j]` = paths from top (previous row)
  - After `dp[j] += dp[j-1]`: `dp[j]` = paths from top + paths from left
- **Obstacle Handling**: When obstacle encountered, set `dp[j] = 0`, blocking all paths through that cell
- **Base Case**: `dp[0]` initialized based on starting cell
- **Row-by-Row Processing**: Each row processes left-to-right, accumulating paths correctly

### **Example Walkthrough:**

**For `obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]`:**

```
Initial: dp = [1, 0, 0]  (starting at (0,0))

Row 0 (i=0):
  j=0: obstacleGrid[0][0]=0, dp[0] stays 1
  j=1: obstacleGrid[0][1]=0, dp[1] += dp[0] → dp[1] = 1
  j=2: obstacleGrid[0][2]=0, dp[2] += dp[1] → dp[2] = 1
  dp = [1, 1, 1]

Row 1 (i=1):
  j=0: obstacleGrid[1][0]=0, dp[0] stays 1 (from top)
  j=1: obstacleGrid[1][1]=1, dp[1] = 0 (obstacle!)
  j=2: obstacleGrid[1][2]=0, dp[2] += dp[1] → dp[2] = 1 + 0 = 1
  dp = [1, 0, 1]

Row 2 (i=2):
  j=0: obstacleGrid[2][0]=0, dp[0] stays 1
  j=1: obstacleGrid[2][1]=0, dp[1] += dp[0] → dp[1] = 0 + 1 = 1
  j=2: obstacleGrid[2][2]=0, dp[2] += dp[1] → dp[2] = 1 + 1 = 2
  dp = [1, 1, 2]

Result: 2 paths
```

### **Solution 2: 2D DP (O(m×n) space)**

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Base case: starting cell
        if (obstacleGrid[0][0] == 0) {
            dp[0][0] = 1;
        }
        
        // Fill first row
        for (int j = 1; j < n; j++) {
            if (obstacleGrid[0][j] == 0) {
                dp[0][j] = dp[0][j-1];
            }
        }
        
        // Fill first column
        for (int i = 1; i < m; i++) {
            if (obstacleGrid[i][0] == 0) {
                dp[i][0] = dp[i-1][0];
            }
        }
        
        // Fill remaining cells
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 0) {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        
        return dp[m-1][n-1];
    }
};
```

### **Complexity Analysis:**

**Solution 1 (Space-Optimized):**
- **Time Complexity:** O(m × n) - Visit each cell once
- **Space Complexity:** O(n) - Single array of size `n` (number of columns)

**Solution 2 (2D DP):**
- **Time Complexity:** O(m × n) - Visit each cell once
- **Space Complexity:** O(m × n) - Full DP table

### **Key Differences from LC 62:**

1. **Obstacle Handling**: Check if cell is obstacle before calculating paths
2. **Base Case**: Starting cell might be blocked (return 0)
3. **Edge Cases**: First row/column can have obstacles blocking subsequent cells

### **Edge Cases:**

1. **Starting cell blocked**: `obstacleGrid[0][0] == 1` → return 0
2. **Ending cell blocked**: `obstacleGrid[m-1][n-1] == 1` → return 0
3. **Single cell**: `m == 1 && n == 1` → return 1 if no obstacle, else 0
4. **Entire row/column blocked**: Some paths become impossible

### **Common Mistakes:**

1. **Forgetting to check starting cell**: Must initialize `dp[0]` based on `obstacleGrid[0][0]`
2. **Not resetting obstacle cells**: When obstacle found, must set `dp[j] = 0` explicitly
3. **Incorrect space optimization**: In 1D version, must handle first column separately (no `j > 0` check for `dp[0]`)

### **Related Problems:**

- [LC 62: Unique Paths](https://leetcode.com/problems/unique-paths/) - Same problem without obstacles
- [LC 64: Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) - Find minimum cost path
- [LC 980: Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) - Must visit all empty cells exactly once
