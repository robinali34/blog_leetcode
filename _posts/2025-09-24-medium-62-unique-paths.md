---
layout: post
title: "[Medium] 62. Unique Paths"
date: 2025-09-24 23:30:00 -0000
categories: leetcode algorithm dynamic-programming data-structures grid combinatorics medium cpp unique-paths problem-solving
---

# [Medium] 62. Unique Paths

This is a classic dynamic programming problem that requires finding the number of unique paths from top-left to bottom-right of a grid. The key insight is recognizing the overlapping subproblems and using DP to avoid recalculating the same paths multiple times.

## Problem Description

There is a robot on an m x n grid. The robot is initially located at the top-left corner (grid[0][0]). The robot tries to move to the bottom-right corner (grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

### Examples

**Example 1:**
```
Input: m = 3, n = 7
Output: 28
```

**Example 2:**
```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

**Example 3:**
```
Input: m = 7, n = 3
Output: 28
```

**Example 4:**
```
Input: m = 3, n = 3
Output: 6
```

### Constraints
- 1 <= m, n <= 100
- It's guaranteed that the answer will be less than or equal to 2 * 10^9

## Approach

The solution uses dynamic programming with the following key insights:

1. **Base Case**: The first row and first column can only be reached in one way (moving right or down respectively)
2. **Recurrence Relation**: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
3. **Bottom-up DP**: Build the solution from smaller subproblems to larger ones

## Solution in C++

**Time Complexity:** O(m × n) - We fill each cell once  
**Space Complexity:** O(m × n) - For the DP table

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 1));
        for (int row = 1; row < m; row++) {
            for (int col = 1; col < n; col++) {
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col];
            }
        }
        return dp[m- 1][n -1];
    }
};
```

## Step-by-Step Example

Let's trace through the solution with m = 3, n = 3:

**Step 1:** Initialize DP table with all 1s
```
[1, 1, 1]
[1, 1, 1]
[1, 1, 1]
```

**Step 2:** Fill the DP table using recurrence relation
- dp[1][1] = dp[1][0] + dp[0][1] = 1 + 1 = 2
- dp[1][2] = dp[1][1] + dp[0][2] = 2 + 1 = 3
- dp[2][1] = dp[2][0] + dp[1][1] = 1 + 2 = 3
- dp[2][2] = dp[2][1] + dp[1][2] = 3 + 3 = 6

**Final DP table:**
```
[1, 1, 1]
[1, 2, 3]
[1, 3, 6]
```

**Result:** dp[2][2] = 6 unique paths

## Key Insights

1. **Mathematical Approach**: This is essentially a combination problem - we need to choose (m-1) down moves out of (m+n-2) total moves
2. **DP Optimization**: Avoids recalculating the same subproblems multiple times
3. **Space Optimization**: Can be optimized to O(min(m,n)) space using rolling array technique
4. **Base Cases**: First row and column are always 1 since there's only one way to reach them

## Alternative Approaches

### Mathematical Solution (Combinatorics)
```cpp
int uniquePaths(int m, int n) {
    long long result = 1;
    for (int i = 0; i < min(m-1, n-1); i++) {
        result = result * (m + n - 2 - i) / (i + 1);
    }
    return (int)result;
}
```

### Space-Optimized DP
```cpp
int uniquePaths(int m, int n) {
    vector<int> dp(n, 1);
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[j] += dp[j-1];
        }
    }
    return dp[n-1];
}
```

## Visual Representation

For a 3×3 grid, the unique paths are:
```
Start → → ↓
        ↓ ↓
        ↓ End

Start → ↓ ↓
        → ↓
        ↓ End

Start → ↓ ↓
        ↓ →
        ↓ End

Start ↓ → ↓
      → ↓
      ↓ End

Start ↓ → ↓
      ↓ →
      ↓ End

Start ↓ ↓ →
      ↓ ↓
      → End
```

## Common Mistakes

- **Off-by-one errors**: Confusing 0-indexed vs 1-indexed arrays
- **Integer overflow**: Not handling large numbers properly
- **Base case errors**: Not initializing first row and column correctly
- **Index confusion**: Mixing up row and column indices

## Related Problems

- **63. Unique Paths II** - With obstacles
- **64. Minimum Path Sum** - Find minimum cost path
- **120. Triangle** - Triangular grid paths
- **174. Dungeon Game** - Reverse DP approach

---
