---
layout: post
title: "[Easy] 1275. Find Winner on a Tic Tac Toe Game"
date: 2026-03-04
categories: [leetcode, easy, simulation, matrix]
tags: [leetcode, easy, simulation, matrix, design]
permalink: /2026/03/04/easy-1275-find-winner-on-a-tic-tac-toe-game/
---
Tic-tac-toe is played on a `3 x 3` grid by two players A and B. Player A always plays first. Given an array `moves` where `moves[i] = [row, col]` indicates a move, return:
- `"A"` if player A wins
- `"B"` if player B wins
- `"Draw"` if all 9 cells are filled with no winner
- `"Pending"` if the game is not yet over

## Examples

**Example 1:**

```
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins with the diagonal.
```

**Example 2:**

```
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins with the first column.
```

**Example 3:**

```
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
```

## Constraints

- `1 <= moves.length <= 9`
- `moves[i].length == 2`
- `0 <= moves[i][j] <= 2`
- All moves are unique and valid
- The grid is always `3 x 3`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Row/column traversal** *(this problem)* | $O(nm)$ | $O(1)$ | Simulation, spiral |
| BFS/DFS on grid | $O(nm)$ | $O(nm)$ | Islands, shortest path |
| Matrix as graph | $O(nm)$ | $O(nm)$ | 4/8-directional neighbors |
| Transpose / rotate | $O(nm)$ | $O(1)$ | In-place rotation tricks |

## Thinking Process

This uses the exact same `+1 / -1` counter trick as [LC 348 Design Tic-Tac-Toe](/2026/03/04/medium-348-design-tic-tac-toe/):

- Player A (even-indexed moves) contributes `+1`
- Player B (odd-indexed moves) contributes `-1`
- Track sums for each row, column, diagonal, and anti-diagonal
- If any sum reaches `+3`, A wins; if `-3`, B wins

After replaying all moves, if no winner:
- All 9 cells filled = `"Draw"`
- Otherwise = `"Pending"`



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Grid traversal</text>

  <rect x="50" y="40" width="28" height="28" fill="#D4D8E0" stroke="#8B8680"/><rect x="78" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="106" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="50" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="78" y="68" width="28" height="28" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="106" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="110" y="115" text-anchor="middle" font-size="11" fill="#6B6560">BFS/DFS flood from each cell</text>

</svg>

## Approach: Counter Tracking -- $O(m)$

{% raw %}
```cpp
class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        const int GRID_SIZE = 3;
        vector<int> rows(GRID_SIZE, 0), cols(GRID_SIZE, 0);
        int diag = 0, antiDiag = 0;

        for (int i = 0; i < (int)moves.size(); i++) {
            int row = moves[i][0], col = moves[i][1];

            int player = (i % 2 == 0) ? 1 : -1;
            rows[row] += player;
            cols[col] += player;

            if (row == col) diag += player;
            if (row == GRID_SIZE - 1 - col) antiDiag += player;

            if (rows[row] == GRID_SIZE || cols[col] == GRID_SIZE ||
                diag == GRID_SIZE || antiDiag == GRID_SIZE)
                return "A";
            else if (rows[row] == -GRID_SIZE || cols[col] == -GRID_SIZE ||
                     diag == -GRID_SIZE || antiDiag == -GRID_SIZE)
                return "B";
        }

        return moves.size() == GRID_SIZE * GRID_SIZE ? "Draw" : "Pending";
    }
};
```

### Solution Explanation

**Approach:** Row/column traversal (this problem)

**Key idea:** This uses the exact same `+1 / -1` counter trick as [LC 348 Design Tic-Tac-Toe](/2026/03/04/medium-348-design-tic-tac-toe/):

**How the code works:**
- Player A (even-indexed moves) contributes `+1`
- Player B (odd-indexed moves) contributes `-1`
- Track sums for each row, column, diagonal, and anti-diagonal
- If any sum reaches `+3`, A wins; if `-3`, B wins
- All 9 cells filled = `"Draw"`
- Otherwise = `"Pending"`

**Walkthrough** — input `moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]`, expected output `"A"`:

A wins with the diagonal.
## Common Mistakes

- Forgetting `"Pending"` as a possible outcome
- Using `abs()` for both players instead of checking `+3` and `-3` separately (works but less clear about *which* player won)
- Checking win condition only after all moves instead of after each move

## Key Takeaways

- Same `+1 / -1` counter pattern as [LC 348](/2026/03/04/medium-348-design-tic-tac-toe/) -- the only difference is replaying moves from an array vs receiving them one at a time
- The fixed `3 x 3` grid means everything is $O(1)$ in practice
- Check for a winner **after each move** to correctly identify the winning player

## Related Problems

- [348. Design Tic-Tac-Toe](https://www.leetcode.com/problems/design-tic-tac-toe/) -- same counter trick in a design context
- [794. Valid Tic-Tac-Toe State](https://www.leetcode.com/problems/valid-tic-tac-toe-state/) -- validate a given board state

## References

- [LC 1275: Find Winner on a Tic Tac Toe Game on LeetCode](https://www.leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)
- [LeetCode Discuss — LC 1275: Find Winner on a Tic Tac Toe Game](https://www.leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
