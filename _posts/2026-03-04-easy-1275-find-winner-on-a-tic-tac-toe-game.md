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

## Thinking Process

This uses the exact same `+1 / -1` counter trick as [LC 348 Design Tic-Tac-Toe](/2026/03/04/medium-348-design-tic-tac-toe/):

- Player A (even-indexed moves) contributes `+1`
- Player B (odd-indexed moves) contributes `-1`
- Track sums for each row, column, diagonal, and anti-diagonal
- If any sum reaches `+3`, A wins; if `-3`, B wins

After replaying all moves, if no winner:
- All 9 cells filled = `"Draw"`
- Otherwise = `"Pending"`

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
{% endraw %}

**Time**: $O(m)$ where $m$ is the number of moves (at most 9)
**Space**: $O(1)$ -- fixed-size arrays for a 3x3 board

## Common Mistakes

- Forgetting `"Pending"` as a possible outcome
- Using `abs()` for both players instead of checking `+3` and `-3` separately (works but less clear about *which* player won)
- Checking win condition only after all moves instead of after each move

## Key Takeaways

- Same `+1 / -1` counter pattern as [LC 348](/2026/03/04/medium-348-design-tic-tac-toe/) -- the only difference is replaying moves from an array vs receiving them one at a time
- The fixed `3 x 3` grid means everything is $O(1)$ in practice
- Check for a winner **after each move** to correctly identify the winning player

## Related Problems

- [348. Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) -- same counter trick in a design context
- [794. Valid Tic-Tac-Toe State](https://leetcode.com/problems/valid-tic-tac-toe-state/) -- validate a given board state

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
