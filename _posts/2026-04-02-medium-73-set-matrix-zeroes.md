---
layout: post
title: "[Medium] 73. Set Matrix Zeroes"
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
- **Follow-up**: Can you solve it with O(1) extra space?

## Thinking Process

The naive approach (modify while scanning) corrupts the matrix -- new zeros trigger more zeros than intended. We need to **record which rows and columns to zero out first**, then apply.

Three levels of space usage:
1. **O(m + n)**: Use separate sets/arrays for row and column markers
2. **O(1)**: Use the matrix's own first row and first column as markers

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Grid traversal</text>

  <rect x="50" y="40" width="28" height="28" fill="#D4D8E0" stroke="#8B8680"/><rect x="78" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="106" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="50" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="78" y="68" width="28" height="28" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="106" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="110" y="115" text-anchor="middle" font-size="11" fill="#6B6560">BFS/DFS flood from each cell</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Row/column traversal | O(nm) | O(1) | Simulation, spiral |
| BFS/DFS on grid | O(nm) | O(nm) | Islands, shortest path |
| **Matrix as graph** *(this problem)* | O(nm) | O(nm) | 4/8-directional neighbors |
| Transpose / rotate | O(nm) | O(1) | In-place rotation tricks |

## Solution

Scan for zeros, record their rows and columns, then zero out.
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

### Solution Explanation

**Approach:** Matrix as graph (this problem)

**Key idea:** The naive approach (modify while scanning) corrupts the matrix -- new zeros trigger more zeros than intended. We need to **record which rows and columns to zero out first**, then apply.

**How the code works:**
1. **O(m + n)**: Use separate sets/arrays for row and column markers
2. **O(1)**: Use the matrix's own first row and first column as markers

**Walkthrough** — input `[[1,1,1],[1,0,1],[1,1,1]]`, expected output `[[1,0,1],[0,0,0],[1,0,1]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Hash Sets | O(m · n) | O(m + n) | Simple and clear |
| In-Place Markers | O(m · n) | O(1) | Uses matrix itself; interview follow-up |

## Common Mistakes

- Zeroing out row 0 / column 0 before processing the interior (destroys marker data)
- Modifying the matrix during the scan pass (new zeros cascade incorrectly)
- Forgetting to separately handle row 0 and column 0 (they overlap at `matrix[0][0]`)

## Key Takeaways

- **"Mark then apply"** is the core pattern -- never modify and read from the same data simultaneously
- Using the matrix's own borders as storage is a classic O(1) space trick
- The order of operations is critical: scan → mark → apply interior → apply borders

## Related Problems

- [289. Game of Life](https://www.leetcode.com/problems/game-of-life/) -- in-place matrix update with encoding trick
- [48. Rotate Image](https://www.leetcode.com/problems/rotate-image/) -- in-place matrix manipulation
- [54. Spiral Matrix](https://www.leetcode.com/problems/spiral-matrix/) -- matrix traversal
- [59. Spiral Matrix II](https://www.leetcode.com/problems/spiral-matrix-ii/) -- matrix filling

## References

- [LC 73: Set Matrix Zeroes on LeetCode](https://www.leetcode.com/problems/set-matrix-zeroes/)
- [LeetCode Discuss — LC 73: Set Matrix Zeroes](https://www.leetcode.com/problems/set-matrix-zeroes/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/set-matrix-zeroes/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
