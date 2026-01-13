---
layout: post
title: "51. N-Queens"
date: 2026-01-12 00:00:00 -0700
categories: [leetcode, hard, array, backtracking, recursion]
permalink: /2026/01/12/hard-51-n-queens/
tags: [leetcode, hard, array, backtracking, recursion, constraint-satisfaction]
---

# 51. N-Queens

## Problem Statement

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

## Examples

**Example 1:**
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

**Example 2:**
```
Input: n = 1
Output: [["Q"]]
```

## Constraints

- `1 <= n <= 9`

## Solution Approach

This is a classic **backtracking with constraint satisfaction** problem. The key insight is to place queens row by row, ensuring no two queens attack each other.

### Key Insights:

1. **Row-by-Row Placement**: Place one queen per row (guarantees no row conflicts)
2. **Constraint Checking**: Need to check:
   - **Column**: No other queen in same column
   - **Diagonal** (top-left to bottom-right): `row - col` is constant
   - **Anti-diagonal** (top-right to bottom-left): `row + col` is constant
3. **Optimization**: Use boolean arrays to track constraints instead of checking board each time
4. **Backtracking**: Try each column, place queen, recurse, then undo

### Algorithm:

1. **Initialize**: Create board, boolean arrays for columns, diagonals, anti-diagonals
2. **DFS**: For each row, try each column:
   - Check if position is valid (not in conflict)
   - Place queen and mark constraints
   - Recurse to next row
   - Remove queen and unmark constraints (backtrack)
3. **Base Case**: When `row == n`, add board configuration to result

## Solution

### **Solution: Backtracking with Optimized Constraint Checking**

```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        size = n;
        board.assign(n, string(n, '.'));
        col.assign(n, false);
        diag.assign(2 * n, false);
        anti.assign(2 * n, false);
        dfs(0);
        return rtn;
    }
private:
    int size;
    vector<string> board;
    vector<vector<string>> rtn;
    vector<bool> col, diag, anti;

    void dfs(int row) {
        if(row == size) {
            rtn.push_back(board);
            return;
        }
        for(int c = 0; c < size; c++) {
            int d = row - c + size;
            int a = row + c;
            if(col[c] || diag[d] || anti[a]) continue;
            col[c] = diag[d] = anti[a] = true;
            board[row][c] = 'Q';
            dfs(row + 1);
            board[row][c] = '.';
            col[c] = diag[d] = anti[a] = false; 
        }
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 4-9)**:
   - `size = n`: Store board size
   - `board`: `n × n` grid initialized with `'.'`
   - `col`: Boolean array of size `n` to track used columns
   - `diag`: Boolean array of size `2 * n` to track diagonals (top-left to bottom-right)
   - `anti`: Boolean array of size `2 * n` to track anti-diagonals (top-right to bottom-left)

2. **DFS Function (Lines 16-30)**:
   - **Base Case (Lines 17-20)**: If `row == size`, all queens placed successfully
     - Add current board configuration to result
     - Return
   - **Try Each Column (Lines 21-29)**:
     - **Calculate indices**:
       - `d = row - c + size`: Diagonal index (add `size` to avoid negative indices)
       - `a = row + c`: Anti-diagonal index
     - **Check Constraints (Line 23)**: If column, diagonal, or anti-diagonal is occupied, skip
     - **Place Queen (Lines 24-25)**: Mark constraints and place `'Q'`
     - **Recurse (Line 26)**: Try next row
     - **Backtrack (Lines 27-28)**: Remove queen and unmark constraints

### **Why This Works:**

- **Row-by-Row**: Placing one queen per row eliminates row conflicts automatically
- **Column Tracking**: `col[c]` ensures no two queens in same column
- **Diagonal Tracking**: 
  - Diagonal `\`: `row - col` is constant (shifted by `+size` to avoid negatives)
  - Anti-diagonal `/`: `row + col` is constant
- **Optimization**: Boolean arrays provide O(1) constraint checking vs O(n) board scanning
- **Backtracking**: Undoing choices allows exploring all valid configurations

### **Diagonal Index Calculation:**

For an `n × n` board:
- **Diagonal** (top-left to bottom-right): `row - col` ranges from `-(n-1)` to `(n-1)`
  - Add `n` to shift range to `[1, 2n-1]`
  - Use `row - col + n` as index
- **Anti-diagonal** (top-right to bottom-left): `row + col` ranges from `0` to `2(n-1)`
  - Use `row + col` directly as index

**Example for `n = 4`:**

```
Diagonal indices (row - col + 4):
    0  1  2  3
0   4  5  6  7
1   3  4  5  6
2   2  3  4  5
3   1  2  3  4

Anti-diagonal indices (row + col):
    0  1  2  3
0   0  1  2  3
1   1  2  3  4
2   2  3  4  5
3   3  4  5  6
```

### **Example Walkthrough:**

**For `n = 4`:**

```
Initial: row=0, board=[[".",".",".","."], ...], all constraints false

Row 0:
  Try col 0:
    d = 0 - 0 + 4 = 4, a = 0 + 0 = 0
    Check: col[0]=false, diag[4]=false, anti[0]=false ✓
    Place Q at (0,0), mark constraints
    Recurse to row 1

  Row 1:
    Try col 0: col[0]=true ✗
    Try col 1:
      d = 1 - 1 + 4 = 4, a = 1 + 1 = 2
      Check: col[1]=false, diag[4]=true ✗ (conflict with (0,0))
    Try col 2:
      d = 1 - 2 + 4 = 3, a = 1 + 2 = 3
      Check: col[2]=false, diag[3]=false, anti[3]=false ✓
      Place Q at (1,2), mark constraints
      Recurse to row 2

    Row 2:
      Try col 0: col[0]=true ✗
      Try col 1:
        d = 2 - 1 + 4 = 5, a = 2 + 1 = 3
        Check: col[1]=false, diag[5]=false, anti[3]=true ✗
      Try col 2: col[2]=true ✗
      Try col 3:
        d = 2 - 3 + 4 = 3, a = 2 + 3 = 5
        Check: col[3]=false, diag[3]=true ✗
      Backtrack: Remove Q from (1,2)

    Try col 3:
      d = 1 - 3 + 4 = 2, a = 1 + 3 = 4
      Check: col[3]=false, diag[2]=false, anti[4]=false ✓
      Place Q at (1,3), mark constraints
      Recurse to row 2
      ... (continue until solution found)

Final: When row=4, add board to result
```

### **Complexity Analysis:**

- **Time Complexity:** O(n!)
  - For each row, we try at most `n` columns
  - With pruning, actual complexity is better but still exponential
  - In worst case: O(n!) (factorial)
- **Space Complexity:** O(n²)
  - `board`: O(n²) for storing board state
  - `col`, `diag`, `anti`: O(n) each
  - Recursion stack: O(n) depth
  - Result: O(n! × n²) for storing all solutions

## Key Insights

1. **Row-by-Row Placement**: Eliminates row conflicts automatically
2. **Optimized Constraint Checking**: Boolean arrays provide O(1) checking vs O(n) scanning
3. **Diagonal Indexing**: 
   - Diagonal: `row - col + n` (shifted to avoid negatives)
   - Anti-diagonal: `row + col`
4. **Backtracking Pattern**: Place → Recurse → Undo

## Edge Cases

1. **n = 1**: Return `[["Q"]]`
2. **n = 2, 3**: No solutions (impossible to place n queens)
3. **n = 4**: 2 solutions
4. **n = 8**: 92 solutions (classic 8-queens problem)

## Common Mistakes

1. **Wrong diagonal indexing**: Not shifting `row - col` correctly
2. **Missing backtrack**: Forgetting to unmark constraints after recursion
3. **Array bounds**: Diagonal array size should be `2 * n` (not `n`)
4. **Board initialization**: Not initializing board with `'.'` characters
5. **Constraint checking order**: Should check all three constraints before placing

## Alternative Approaches

### **Approach 2: Check Board Each Time (Less Efficient)**

```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        vector<vector<string>> result;
        dfs(board, 0, n, result);
        return result;
    }
    
private:
    void dfs(vector<string>& board, int row, int n, vector<vector<string>>& result) {
        if(row == n) {
            result.push_back(board);
            return;
        }
        for(int col = 0; col < n; col++) {
            if(isValid(board, row, col, n)) {
                board[row][col] = 'Q';
                dfs(board, row + 1, n, result);
                board[row][col] = '.';
            }
        }
    }
    
    bool isValid(vector<string>& board, int row, int col, int n) {
        // Check column above
        for(int i = 0; i < row; i++) {
            if(board[i][col] == 'Q') return false;
        }
        // Check diagonal \
        for(int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if(board[i][j] == 'Q') return false;
        }
        // Check diagonal /
        for(int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if(board[i][j] == 'Q') return false;
        }
        return true;
    }
};
```

**Time Complexity:** O(n! × n) (slower due to O(n) validation)  
**Space Complexity:** O(n²)

## Related Problems

- [LC 52: N-Queens II](https://leetcode.com/problems/n-queens-ii/) - Count number of solutions (same problem, just count)
- [LC 37: Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) - Similar constraint satisfaction
- [LC 51: N-Queens](https://leetcode.com/problems/n-queens/) - This problem

---

*This problem demonstrates backtracking with constraint satisfaction. The key optimization is using boolean arrays for O(1) constraint checking instead of scanning the board each time, which reduces time complexity significantly.*

