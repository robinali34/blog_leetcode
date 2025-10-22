---
layout: post
title: "LC 348: Design Tic-Tac-Toe"
date: 2025-10-20 17:30:00 -0700
categories: leetcode medium design array
permalink: /posts/2025-10-20-medium-348-design-tic-tac-toe/
tags: [leetcode, medium, design, array, matrix, optimization]
---

# LC 348: Design Tic-Tac-Toe

**Difficulty:** Medium  
**Category:** Design, Array, Matrix  
**Companies:** Amazon, Google, Microsoft, Facebook

## Problem Statement

Design a Tic-tac-toe game that is played between two players on an `n x n` grid.

A move is guaranteed to be valid and is placed on an empty block. Once a winning condition is reached, no more moves are allowed. A player who succeeds in placing `n` of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the `TicTacToe` class:

- `TicTacToe(int n)` Initializes the object the size of the board `n`.
- `int move(int row, int col, int player)` Indicates that the player with id `player` plays at the cell `(row, col)` of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Returns:
  - `0` if there is no winner yet
  - `1` if player 1 wins
  - `2` if player 2 wins

### Examples

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

### Constraints

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

### Approach 2: Optimized with Counters (Recommended)

**Key Insight:** Instead of checking the entire board, maintain counters for each row, column, and diagonal. Use `+1` for player 1 and `-1` for player 2.

**Algorithm:**
1. Maintain arrays for row counts, column counts, and diagonal counts
2. For each move, update relevant counters
3. Check if any counter reaches `±n` (absolute value equals n)

**Time Complexity:** O(1) per move  
**Space Complexity:** O(n)

```cpp
class TicTacToe {
public:
    TicTacToe(int n): rows(n), cols(n), diagonal(0), antiDiagonal(0) {
    }
    
    int move(int row, int col, int player) {
        int curr = player == 1 ? 1 : -1;
        int n = rows.size();

        rows[row] += curr;
        cols[col] += curr;
        if(row == col) diagonal += curr;
        if(row == n - col - 1) antiDiagonal += curr;

        if(abs(rows[row]) == n || abs(cols[col]) == n ||
           abs(diagonal) == n || abs(antiDiagonal) == n)
           return player;
        return 0;
    }
    
private:
    vector<int> rows, cols;
    int diagonal, antiDiagonal;
};
```

## Algorithm Analysis

### Naive vs Optimized Approach

| Aspect | Naive | Optimized |
|--------|-------|-----------|
| Time per move | O(n) | O(1) |
| Space | O(n²) | O(n) |
| Implementation | Simple | Slightly complex |
| Scalability | Poor | Excellent |

### Key Optimizations

1. **Counter-Based Tracking**: Instead of scanning the board, maintain running counts
2. **Player Encoding**: Use `+1` and `-1` to distinguish players
3. **Diagonal Detection**: Check if `row == col` (main diagonal) and `row == n - col - 1` (anti-diagonal)
4. **Absolute Value Check**: `abs(count) == n` indicates a win

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

## Related Problems

- [LC 794: Valid Tic-Tac-Toe State](https://leetcode.com/problems/valid-tic-tac-toe-state/)
- [LC 1275: Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)
- [LC 348: Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/)

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

---

*This problem demonstrates the importance of optimizing data structures and algorithms for repeated operations, showing how mathematical insights can lead to significant performance improvements.*
