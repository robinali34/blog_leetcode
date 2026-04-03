---
layout: post
title: "LeetCode 73. Set Matrix Zeroes"
date: 2026-04-02
categories: [leetcode, medium, matrix, array]
tags: [leetcode, medium, matrix, array, in-place]
permalink: /2026/04/02/medium-73-set-matrix-zeroes/
---

Given an `m x n` integer matrix, if an element is `0`, set its **entire row and column** to `0`. You must do it **in place**.

## Examples

**Example 1:**

```
Input:  [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**

```
Input:  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Constraints

- `m == matrix.length`, `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`
- **Follow-up**: Can you solve it with $O(1)$ extra space?

## Thinking Process

The naive approach (modify while scanning) corrupts the matrix -- new zeros trigger more zeros than intended. We need to **record which rows and columns to zero out first**, then apply.

Three levels of space usage:
1. **$O(m + n)$**: Use separate sets/arrays for row and column markers
2. **$O(1)$**: Use the matrix's own first row and first column as markers

## Solution 1: Hash Sets -- $O(m \cdot n)$ time, $O(m + n)$ space

Scan for zeros, record their rows and columns, then zero out.

{% raw %}
```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int R = matrix.size();
        int C = matrix[0].size();
        set<int> rows;
        set<int> cols;

        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (matrix[i][j] == 0) {
                    rows.insert(i);
                    cols.insert(j);
                }
            }
        }

        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (rows.find(i) != rows.end() || cols.find(j) != cols.end()) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
};
```
{% endraw %}

**Time**: $O(m \cdot n)$
**Space**: $O(m + n)$

## Solution 2: In-Place Markers -- $O(m \cdot n)$ time, $O(1)$ space

Use the **first row** and **first column** of the matrix itself as marker arrays. Two boolean flags track whether row 0 and column 0 originally contained zeros.

### Algorithm

1. Check if row 0 or column 0 originally have any zeros (save in flags)
2. For cells `[1..R-1][1..C-1]`: if `matrix[i][j] == 0`, mark `matrix[i][0] = 0` and `matrix[0][j] = 0`
3. Zero out cells `[1..R-1][1..C-1]` based on markers in row 0 / column 0
4. Finally, zero out row 0 and column 0 if their flags are set

### Why Process Row 0 / Column 0 Last?

If we zero them out early, we lose the marker information stored there. The flags preserve the original state.

{% raw %}
```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int R = matrix.size();
        int C = matrix[0].size();

        bool firstRowZero = false;
        bool firstColZero = false;
        for (int j = 0; j < C; ++j)
            if (matrix[0][j] == 0) firstRowZero = true;
        for (int i = 0; i < R; ++i)
            if (matrix[i][0] == 0) firstColZero = true;

        for (int i = 1; i < R; ++i) {
            for (int j = 1; j < C; ++j) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < R; ++i) {
            for (int j = 1; j < C; ++j) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }

        if (firstRowZero)
            for (int j = 0; j < C; ++j)
                matrix[0][j] = 0;
        if (firstColZero)
            for (int i = 0; i < R; ++i)
                matrix[i][0] = 0;
    }
};
```
{% endraw %}

**Time**: $O(m \cdot n)$
**Space**: $O(1)$

### Walk-through

```
Input:
  [[0, 1, 2, 0],
   [3, 4, 5, 2],
   [1, 3, 1, 5]]

Step 1: firstRowZero = true (matrix[0][0]=0), firstColZero = true (matrix[0][0]=0)

Step 2: Scan [1..2][1..3] — no zeros found, markers unchanged

Step 3: Apply markers to [1..2][1..3] — no changes (no markers set beyond originals)

Step 4: firstRowZero → zero out row 0: [0,0,0,0]
        firstColZero → zero out col 0: all [i][0] = 0

Result:
  [[0, 0, 0, 0],
   [0, 4, 5, 2],
   [0, 3, 1, 5]]  ✓
```

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Hash Sets | $O(m \cdot n)$ | $O(m + n)$ | Simple and clear |
| In-Place Markers | $O(m \cdot n)$ | $O(1)$ | Uses matrix itself; interview follow-up |

## Common Mistakes

- Zeroing out row 0 / column 0 before processing the interior (destroys marker data)
- Modifying the matrix during the scan pass (new zeros cascade incorrectly)
- Forgetting to separately handle row 0 and column 0 (they overlap at `matrix[0][0]`)

## Key Takeaways

- **"Mark then apply"** is the core pattern -- never modify and read from the same data simultaneously
- Using the matrix's own borders as storage is a classic $O(1)$ space trick
- The order of operations is critical: scan → mark → apply interior → apply borders

## Related Problems

- [289. Game of Life](https://leetcode.com/problems/game-of-life/) -- in-place matrix update with encoding trick
- [48. Rotate Image](https://leetcode.com/problems/rotate-image/) -- in-place matrix manipulation
- [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) -- matrix traversal
- [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) -- matrix filling

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
