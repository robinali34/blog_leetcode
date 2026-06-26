---
layout: post
title: "[Medium] 348. Design Tic-Tac-Toe"
date: 2025-10-21 17:30:00 -0700
categories: leetcode medium design array
permalink: /posts/2025-10-21-medium-348-design-tic-tac-toe/
tags: [leetcode, medium, design, array, matrix, optimization]
---
**Difficulty:** Medium  
**Category:** Design, Array, Matrix  
**Companies:** Amazon, Google, Microsoft, Facebook


Design a Tic-tac-toe game that is played between two players on an `n x n` grid.

A move is guaranteed to be valid and is placed on an empty block. Once a winning condition is reached, no more moves are allowed. A player who succeeds in placing `n` of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the `TicTacToe` class:

- `TicTacToe(int n)` Initializes the object the size of the board `n`.
- `int move(int row, int col, int player)` Indicates that the player with id `player` plays at the cell `(row, col)` of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Returns:
  - `0` if there is no winner yet
  - `1` if player 1 wins
  - `2` if player 2 wins

## Examples
**Example 1:**
```
Input:
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output:
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation:
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
```

## Constraints
- `2 <= n <= 100`
- player is `1` or `2`
- `0 <= row, col < n`
- At most `n^2` calls will be made to `move`

## Solution Approaches

### Approach 1: Naive Implementation

**Algorithm:**
1. Store the entire board as a 2D array
2. For each move, check all rows, columns, and diagonals
3. Return winner if any line is complete

**Time Complexity:** O(n) per move  
**Space Complexity:** O(n²)

```cpp
class TicTacToe {
public:
    TicTacToe(int n) {
        board.resize(n, vector<int>(n));
    }
    
    int move(int row, int col, int player) {
        if(player == 1)
            board[row][col] = 'X';
        else
            board[row][col] = 'O';
        if(win(player)) return player;
        return 0;
    }
    
private:
    vector<vector<int>> board;

    bool win(int player){
        char ch;
        if(player == 1) ch = 'X';
        else ch = 'O';
        int n = board.size();

        // Check rows
        for(int i = 0; i < n; i++) {
            int cnt = 0;
            for(int j = 0; j < n; j++) {
                if(board[i][j] == ch) cnt++;
            }
            if(cnt == n) return true;
        }

        // Check columns
        for(int i = 0; i < n; i++) {
            int cnt = 0;
            for(int j = 0; j < n; j++) {
                if(board[j][i] == ch) cnt++;
            }
            if(cnt == n) return true;
        }

        // Check main diagonal
        int cnt = 0;
        for(int i = 0; i < n; i++) {
            if(board[i][i] == ch) cnt++;
        }
        if(cnt == n) return true;

        // Check anti-diagonal
        cnt = 0;
        for(int i = 0; i < n; i++) {
            if(board[i][n - i - 1] == ch) cnt++;
        }
        if(cnt == n) return true;
        
        return false;
    }
};
```

### Solution Explanation

**Approach:** Row/column traversal (this problem)

**Key idea:** Difficulty:** Medium

**How the code works:**
**Difficulty:** Medium
**Category:** Design, Array, Matrix
- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.
- Boundary checks on every neighbor expansion.

**Walkthrough** — input `["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]`, expected output `[null, 0, 0, 0, 0, 0, 0, 1]`:

TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

**Time:** O(1) vs O(n) per move · **Space:** see analysis
## Implementation Details

### Counter Update Logic
```cpp
int curr = player == 1 ? 1 : -1;  // Player encoding
rows[row] += curr;                 // Update row count
cols[col] += curr;                 // Update column count
if(row == col) diagonal += curr;   // Main diagonal
if(row == n - col - 1) antiDiagonal += curr;  // Anti-diagonal
```

### Win Condition Check
```cpp
if(abs(rows[row]) == n || abs(cols[col]) == n ||
   abs(diagonal) == n || abs(antiDiagonal) == n)
   return player;
```

## Edge Cases

1. **First Move**: No winner yet
2. **Diagonal Win**: Both main and anti-diagonal can win simultaneously
3. **Last Move**: Game ends immediately when someone wins
4. **Large Board**: Optimized approach scales better

## Follow-up Questions

- What if the board could be larger (n > 100)?
- How would you handle more than 2 players?
- What if you needed to detect draws?
- How would you implement undo functionality?

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [LC 794: Valid Tic-Tac-Toe State](https://www.leetcode.com/problems/valid-tic-tac-toe-state/)
- [LC 1275: Find Winner on a Tic Tac Toe Game](https://www.leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)
- [LC 348: Design Tic-Tac-Toe](https://www.leetcode.com/problems/design-tic-tac-toe/)

## Design Patterns

1. **State Tracking**: Maintain game state efficiently
2. **Counter Optimization**: Use mathematical properties to avoid full scans
3. **Space-Time Trade-off**: Trade space for time efficiency
4. **Incremental Updates**: Update only affected counters

## Performance Considerations

- **Memory Usage**: Optimized approach uses O(n) vs O(n²) space
- **Time Complexity**: O(1) vs O(n) per move
- **Scalability**: Optimized approach handles large boards efficiently
- **Cache Efficiency**: Linear arrays have better cache performance than 2D arrays

## Key Takeaways

- **Pattern:** Row/column traversal (this problem)
- Difficulty:** Medium
- Category:** Design, Array, Matrix

## References

- [LC 348: Design Tic-Tac-Toe on LeetCode](https://www.leetcode.com/problems/design-tic-tac-toe/)
- [LeetCode Discuss — LC 348: Design Tic-Tac-Toe](https://www.leetcode.com/problems/design-tic-tac-toe/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/design-tic-tac-toe/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)

## Thinking Process

**Difficulty:** Medium

**Category:** Design, Array, Matrix

- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.
- Boundary checks on every neighbor expansion.



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
| **Row/column traversal** *(this problem)* | O(nm) | O(1) | Simulation, spiral |
| BFS/DFS on grid | O(nm) | O(nm) | Islands, shortest path |
| Matrix as graph | O(nm) | O(nm) | 4/8-directional neighbors |
| Transpose / rotate | O(nm) | O(1) | In-place rotation tricks |
