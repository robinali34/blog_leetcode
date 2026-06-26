---
layout: post
title: "[Medium] 348. Design Tic-Tac-Toe"
date: 2026-03-04
categories: [leetcode, medium, design, matrix]
tags: [leetcode, medium, design, matrix, simulation]
permalink: /2026/03/04/medium-348-design-tic-tac-toe/
---
Design a Tic-Tac-Toe game that is played on an `n x n` board between two players. A move is guaranteed to be valid and is placed on an empty block. Once a winning condition is reached, no more moves are allowed. A player wins if they place `n` marks in a row, column, diagonal, or anti-diagonal.

Implement the `TicTacToe` class:
- `TicTacToe(int n)` -- initializes the board of size `n x n`
- `int move(int row, int col, int player)` -- player `1` or `2` places a mark. Return the player number if they win, otherwise `0`

## Examples

**Example:**

```
Input: ["TicTacToe","move","move","move","move","move","move","move"]
       [[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]
Output: [null,0,0,0,0,0,0,1]

Explanation:
  . . .    1 . .    1 . 2    1 . 2    1 . 2    1 . 2    1 . 2    1 . 2
  . . . -> . . . -> . . . -> . . . -> . 2 . -> 2 2 . -> 2 2 . -> 2 2 .
  . . .    . . .    . . .    . . 1    . . 1    . . 1    . . 1    1 1 1  ← player 1 wins
```

## Constraints

- `2 <= n <= 100`
- `player` is `1` or `2`
- `0 <= row, col < n`
- Every call to `move` is on an empty cell
- At most `n²` calls to `move`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Row/column traversal** *(this problem)* | $O(nm)$ | $O(1)$ | Simulation, spiral |
| BFS/DFS on grid | $O(nm)$ | $O(nm)$ | Islands, shortest path |
| Matrix as graph | $O(nm)$ | $O(nm)$ | 4/8-directional neighbors |
| Transpose / rotate | $O(nm)$ | $O(1)$ | In-place rotation tricks |

## Thinking Process

### Brute Force

After each move, scan the entire row, column, and both diagonals to check for a winner. Each `move` costs $O(n)$.

### Key Insight: +1 / -1 Encoding

Instead of storing the full board, track the **sum** of each row, column, diagonal, and anti-diagonal:
- Player 1 contributes `+1`
- Player 2 contributes `-1`

If any sum reaches `+n`, player 1 wins. If any reaches `-n`, player 2 wins. This works because a sum of `±n` means all `n` cells in that line belong to the same player.

This makes each `move` $O(1)$ -- just update at most 4 counters and check their absolute values.

### Why +1 / -1?

Using `+1` and `-1` is cleaner than tracking two separate counts per line. Opposite players cancel each other out, so `|sum| == n` is a necessary and sufficient condition for a win.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Grid traversal</text>

  <rect x="50" y="40" width="28" height="28" fill="#D4D8E0" stroke="#8B8680"/><rect x="78" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="106" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="50" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="78" y="68" width="28" height="28" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="106" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="110" y="115" text-anchor="middle" font-size="11" fill="#6B6560">BFS/DFS flood from each cell</text>

</svg>

## Approach: Counter Tracking -- $O(1)$ per move

{% raw %}
```cpp
class TicTacToe {
public:
    TicTacToe(int n) : rows(n), cols(n), diagonal(0), antiDiagonal(0) {}

    int move(int row, int col, int player) {
        int curr = player == 1 ? 1 : -1;
        int n = rows.size();

        rows[row] += curr;
        cols[col] += curr;
        if (row == col) diagonal += curr;
        if (row == n - col - 1) antiDiagonal += curr;

        if (abs(rows[row]) == n || abs(cols[col]) == n ||
            abs(diagonal) == n || abs(antiDiagonal) == n)
            return player;
        return 0;
    }

private:
    vector<int> rows, cols;
    int diagonal, antiDiagonal;
};
```

### Solution Explanation

**Approach:** Row/column traversal (this problem)

**Key idea:** ### Brute Force

**How the code works:**
- Player 1 contributes `+1`
- Player 2 contributes `-1`
## Common Mistakes

- Using separate arrays for each player instead of the simpler `+1 / -1` encoding
- Forgetting the anti-diagonal condition (`row == n - col - 1`)
- Checking only diagonal when `row == col` but missing that some cells lie on **both** diagonals (e.g., the center of an odd-sized board)

## Key Takeaways

- **Reduce the board to counters** -- instead of storing an `n x n` grid, 2 arrays + 2 integers suffice
- The **+1 / -1 trick** turns a two-player game into simple summation, where `|sum| == n` detects a winner
- This pattern generalizes to any "check if a line is fully occupied by one player" problem

## Related Problems

- [794. Valid Tic-Tac-Toe State](https://www.leetcode.com/problems/valid-tic-tac-toe-state/) -- validate a board state
- [1275. Find Winner on a Tic Tac Toe Game](https://www.leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) -- determine winner from move list

## References

- [LC 348: Design Tic-Tac-Toe on LeetCode](https://www.leetcode.com/problems/design-tic-tac-toe/)
- [LeetCode Discuss — LC 348: Design Tic-Tac-Toe](https://www.leetcode.com/problems/design-tic-tac-toe/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/design-tic-tac-toe/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
