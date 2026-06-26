---
layout: post
title: "[Medium] 221. Maximal Square"
date: 2026-04-18
categories: [leetcode, medium, dynamic-programming]
tags: [leetcode, medium, dynamic-programming, matrix, dp]
permalink: /2026/04/18/medium-221-maximal-square/
---
Given an `m x n` binary matrix filled with `'0'`s and `'1'`s, find the largest square containing only `'1'`s and return its area.

## Examples

**Example 1:**

```
Input:
  1 0 1 0 0
  1 0 1 1 1
  1 1 1 1 1
  1 0 0 1 0

Output: 4   (a 2x2 square)
```

**Example 2:**

```
Input:
  0 1
  1 0

Output: 1   (a 1x1 square)
```

**Example 3:**

```
Input:
  0

Output: 0
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is `'0'` or `'1'`

## Thinking Process

### The DP Definition

Define `dp[i][j]` = **side length** of the largest square whose bottom-right corner is at `(i, j)`.

### The Transition

A square at `(i, j)` can only be as large as the smallest of its three neighbors plus one:

```
dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
```

Why? A square of side `k` at `(i, j)` requires:
- A square of side `k-1` ending at `(i-1, j)` (top)
- A square of side `k-1` ending at `(i, j-1)` (left)
- A square of side `k-1` ending at `(i-1, j-1)` (diagonal)

If any of these is smaller, it becomes the bottleneck.

```
  ┌──────────┐
  │ diag  top│
  │ left  cur│
  └──────────┘

dp[i-1][j-1]  dp[i-1][j]
dp[i][j-1]    dp[i][j] = 1 + min(top, left, diag)
```

### Complete Walk-through

```
Matrix:                    DP table:
1 0 1 0 0                 1 0 1 0 0
1 0 1 1 1                 1 0 1 1 1
1 1 1 1 1                 1 1 1 2 2
1 0 0 1 0                 1 0 0 1 0
```

Key cells:
- `dp[2][3]`: `min(top=1, left=1, diag=1) + 1 = 2` -- a 2x2 square forms
- `dp[2][4]`: `min(top=1, left=2, diag=1) + 1 = 2` -- another 2x2 square
- `dp[3][3]`: `min(top=2, left=0, diag=1) + 1 = 1` -- left is 0, so only 1x1

Max value = 2, so answer = $2^2 = 4$.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">1D DP recurrence</text>

  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

## Solution

{% raw %}
```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int rows = matrix.size();
        int cols = matrix[0].size();

        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        int maxSide = 0;

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (matrix[i][j] == '1') {
                    if (i == 0 || j == 0) {
                        dp[i][j] = 1;
                    } else {
                        dp[i][j] = 1 + min({
                            dp[i - 1][j],
                            dp[i][j - 1],
                            dp[i - 1][j - 1]
                        });
                    }
                    maxSide = max(maxSide, dp[i][j]);
                }
            }
        }
        return maxSide * maxSide;
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** ### The DP Definition

**How the code works:**
- A square of side `k-1` ending at `(i-1, j)` (top)
- A square of side `k-1` ending at `(i, j-1)` (left)
- A square of side `k-1` ending at `(i-1, j-1)` (diagonal)
- `dp[2][3]`: `min(top=1, left=1, diag=1) + 1 = 2` -- a 2x2 square forms
- `dp[2][4]`: `min(top=1, left=2, diag=1) + 1 = 2` -- another 2x2 square
- `dp[3][3]`: `min(top=2, left=0, diag=1) + 1 = 1` -- left is 0, so only 1x1

**Walkthrough** — input `1 0 1 0 0`, expected output `4   (a 2x2 square)`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- **Returning `maxSide` instead of `maxSide * maxSide`:** The problem asks for **area**, not side length
- **Treating `matrix[i][j]` as int:** The matrix contains `char` values (`'0'`/`'1'`), not integers
- **Forgetting to reset `dp[j] = 0` in 1D version:** When `matrix[i][j] == '0'`, the cell must be explicitly zeroed

## Key Takeaways

- Classic 2D DP pattern: define state at each cell, derive from neighbors
- The `min` of three neighbors is the core insight -- a square is only as large as its weakest constraint
- Space optimization from 2D to 1D is a standard technique: save the diagonal before overwriting
- Answer is $\text{maxSide}^2$ (area, not side length)

## Related Problems

- [85. Maximal Rectangle](https://www.leetcode.com/problems/maximal-rectangle/) -- harder generalization using histogram approach
- [1277. Count Square Submatrices with All Ones](https://www.leetcode.com/problems/count-square-submatrices-with-all-ones/) -- same DP, sum all `dp[i][j]` values
- [62. Unique Paths](https://www.leetcode.com/problems/unique-paths/) -- similar 2D DP grid pattern
- [64. Minimum Path Sum](https://www.leetcode.com/problems/minimum-path-sum/) -- 2D DP with neighbor transitions

## References

- [LC 221: Maximal Square on LeetCode](https://www.leetcode.com/problems/maximal-square/)
- [LeetCode Discuss — LC 221: Maximal Square](https://www.leetcode.com/problems/maximal-square/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/maximal-square/editorial/) *(may require premium)*

## Template Reference

- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
