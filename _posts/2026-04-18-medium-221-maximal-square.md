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

## Solution 1: 2D DP -- $O(mn)$ time, $O(mn)$ space

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
{% endraw %}

The first row and first column are base cases: if `matrix[i][j] == '1'`, then `dp[i][j] = 1` (a 1x1 square at most).

## Solution 2: Space-Optimized 1D DP -- $O(mn)$ time, $O(n)$ space

Since each row only depends on the current and previous row, we can use a single 1D array.

{% raw %}
```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        int rows = matrix.size();
        int cols = matrix[0].size();

        vector<int> dp(cols, 0);
        int maxSide = 0;
        int prev = 0;

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                int temp = dp[j];
                if (matrix[i][j] == '1') {
                    if (i == 0 || j == 0) {
                        dp[j] = 1;
                    } else {
                        dp[j] = 1 + min({dp[j], dp[j - 1], prev});
                    }
                    maxSide = max(maxSide, dp[j]);
                } else {
                    dp[j] = 0;
                }
                prev = temp;
            }
        }
        return maxSide * maxSide;
    }
};
```
{% endraw %}

### Variable Mapping

| 1D variable | Equivalent in 2D |
|---|---|
| `dp[j]` (before update) | `dp[i-1][j]` (top) |
| `dp[j-1]` (already updated) | `dp[i][j-1]` (left) |
| `prev` (saved before overwriting) | `dp[i-1][j-1]` (diagonal) |

The trick is saving `dp[j]` into `prev` **before** overwriting it, so the diagonal value from the previous row isn't lost.

## Why `min` of Three Neighbors?

Consider why we can't just check one or two neighbors:

```
Case: top=3, left=3, diag=1

    . . . .
    . 1 1 .
    . 1 1 .      ← diag is the bottleneck
    . . 1 ?

Even though top and left support a 3x3,
the diagonal gap limits us to a 2x2.
```

All three must agree for a larger square to exist. The minimum captures the tightest constraint.

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

- [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) -- harder generalization using histogram approach
- [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) -- same DP, sum all `dp[i][j]` values
- [62. Unique Paths](https://leetcode.com/problems/unique-paths/) -- similar 2D DP grid pattern
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) -- 2D DP with neighbor transitions

## Template Reference

- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
