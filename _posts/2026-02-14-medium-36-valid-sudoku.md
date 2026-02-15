---
layout: post
title: "LeetCode 36. Valid Sudoku"
date: 2026-02-14
categories: [leetcode, medium, math, bit-manipulation]
tags: [leetcode, medium, bitmask, grid, hash]
permalink: /2026/02/14/medium-36-valid-sudoku/
---

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each **row** must contain the digits `1-9` without repetition.
2. Each **column** must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes must contain the digits `1-9` without repetition.

**Note:** We are NOT solving Sudoku. Just validating the current board. Empty cells are represented by `'.'`.

## Examples

**Example 1:**

```
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:**

```
Input: board = (same as above but with board[0][0] changed to "8")
Output: false
Explanation: Two 8's in the top-left 3x3 sub-box.
```

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`

## Thinking Process

**Fixed size 9x9** -- maximum 81 cells, so time complexity is essentially constant. This problem is not about performance; it's about **clean constraint modeling**.

We need to detect duplicates across **27 constraint groups**:
- 9 rows
- 9 columns
- 9 sub-boxes (3x3 blocks)

### Why Bitmask?

Instead of using `set` or `unordered_set`, use an integer bitmask per group:
- Faster -- no hash overhead
- Cleaner -- single integer per group
- Classic bit manipulation trick

### Encoding

For digit `d` (character `'1'` to `'9'`):

```
num = d - '1'       // 0..8
mask = 1 << num     // one-hot bit
```

Each row/col/box maintains an integer. If the bit is already set, we found a duplicate.

### Box Index: Why `(i/3)*3 + (j/3)` Works

The 9 sub-boxes are indexed as:

```
0 1 2
3 4 5
6 7 8
```

- `(i / 3)` gives the block row (0, 1, or 2)
- `(j / 3)` gives the block column (0, 1, or 2)
- Combined: `(i / 3) * 3 + (j / 3)` maps to 0..8

Common wrong formula: `(i % 3) * 3 + (j % 3)` -- this gives position *within* a box, not the box index.

## Approach

Single pass over all 81 cells. For each filled cell:
1. Compute `num = board[i][j] - '1'` and `mask = 1 << num`
2. Compute `boxIndex = (i / 3) * 3 + (j / 3)`
3. Check if `mask` already exists in `row[i]`, `col[j]`, or `box[boxIndex]`
4. If yes, return `false`. Otherwise, set the bit.

**Time Complexity**: $O(81)$ = $O(1)$
**Space Complexity**: $O(1)$ (27 integers)

## Solution

{% raw %}
```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int row[9] = {0};
        int col[9] = {0};
        int box[9] = {0};

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;

                int num = board[i][j] - '1';   // 0..8
                int mask = 1 << num;
                int boxIndex = (i / 3) * 3 + (j / 3);

                if (row[i] & mask) return false;
                if (col[j] & mask) return false;
                if (box[boxIndex] & mask) return false;

                row[i] |= mask;
                col[j] |= mask;
                box[boxIndex] |= mask;
            }
        }
        return true;
    }
};
```
{% endraw %}

## Common Mistakes

- Using `unordered_set` inside loops -- slower and messier than bitmask
- Forgetting to skip `'.'` cells
- Wrong box index formula (`(i % 3) * 3 + (j % 3)` is position within a box, not the box index)

## Key Takeaways

This problem tests:
- **Constraint modeling** -- 27 groups validated in one pass
- **Bitmask usage** -- one integer per constraint group
- **Grid indexing mapping** -- the `(i/3)*3 + (j/3)` trick
- **Clean $O(1)$ structure design** -- no containers, just arrays

## Related Problems

- [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) -- backtracking extension

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
