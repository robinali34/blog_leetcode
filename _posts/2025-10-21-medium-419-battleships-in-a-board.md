---
layout: post
title: "[Medium] 419. Battleships in a Board"
date: 2025-10-21 17:00:00 -0700
categories: leetcode medium array matrix
permalink: /posts/2025-10-21-medium-419-battleships-in-a-board/
tags: [leetcode, medium, array, matrix, dfs, battleship]
---
**Difficulty:** Medium  
**Category:** Array, Matrix, DFS  
**Companies:** Amazon, Google, Microsoft


Given an `m x n` matrix `board` where each cell is either a battleship `'X'` or empty `'.'`, return the number of the battleships on `board`.

Battleships can only be placed horizontally or vertically on `board`. In other words, they can only be made of the shape `1 x k` (1 row, k columns) or `k x 1` (k rows, 1 column), where `k` can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

## Examples
**Example 1:**
```
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
```

**Example 2:**
```
Input: board = [["."]]
Output: 0
```

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is either `'.'` or `'X'`

## Solution Approaches

### Approach 1: Count Top-Left Corners (Optimal)

**Key Insight:** Only count the top-left corner of each battleship. A cell is the top-left corner if:
1. It contains `'X'`
2. The cell above it (if exists) is not `'X'`
3. The cell to the left (if exists) is not `'X'`

**Time Complexity:** O(m × n)  
**Space Complexity:** O(1)

```cpp
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int count = 0;
        for(int i = 0; i < (int)board.size(); i++) {
            for(int j = 0; j < (int)board[0].size(); j++) {
                if(board[i][j] == 'X') {
                    if(i > 0 && board[i - 1][j] == 'X') continue;
                    if(j > 0 && board[i][j - 1] == 'X') continue;
                    count++;
                }
            }
        }
        return count;
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **Battleship Structure**: Each battleship is a connected component of `'X'` cells

**How the code works:**
1. **Battleship Structure**: Each battleship is a connected component of `'X'` cells
- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.

**Walkthrough** — input `board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]`, expected output `2`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Edge Cases

1. **Empty Board**: Return 0
2. **Single Cell**: `[["X"]]` → 1 battleship
3. **No Battleships**: `[["."]]` → 0 battleships
4. **Large Battleships**: Vertical or horizontal ships of any length

## Follow-up Questions

- What if battleships could be L-shaped or T-shaped?
- How would you find the size of each battleship?
- What if the board could be modified (mark visited ships)?

## Related Problems

- [LC 200: Number of Islands](https://www.leetcode.com/problems/number-of-islands/)
- [LC 695: Max Area of Island](https://www.leetcode.com/problems/max-area-of-island/)
- [LC 130: Surrounded Regions](https://www.leetcode.com/problems/surrounded-regions/)

## Implementation Notes

1. **Boundary Checks**: Always check array bounds before accessing
2. **Type Casting**: Cast `board.size()` to `int` to avoid comparison warnings
3. **Early Continue**: Use `continue` to skip non-top-left corners
4. **Single Pass**: No need to modify the original board

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Battleship Structure**: Each battleship is a connected component of `'X'` cells
2. **No Adjacent Ships**: Ships are separated by at least one empty cell
3. **Top-Left Corner**: Each battleship has exactly one top-left corner
4. **Single Pass**: Can count ships in one pass without modification

## References

- [LC 419: Battleships in a Board on LeetCode](https://www.leetcode.com/problems/battleships-in-a-board/)
- [LeetCode Discuss — LC 419: Battleships in a Board](https://www.leetcode.com/problems/battleships-in-a-board/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/battleships-in-a-board/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)

## Thinking Process

1. **Battleship Structure**: Each battleship is a connected component of `'X'` cells

- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.



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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | $O(n)$ | $O(h)$ stack | Natural for trees and graphs |
| Iterative DFS (stack) | $O(n)$ | $O(n)$ | Avoid recursion depth limits |
| DFS with memoization | $O(n)$ | $O(n)$ | Overlapping subproblems on graphs |
| Backtracking DFS | $O(2^n)$ typical | $O(n)$ | Enumerate choices with pruning |
