---
layout: post
title: "[Hard] 51. N-Queens"
date: 2026-01-12 00:00:00 -0700
categories: [leetcode, hard, array, backtracking, recursion]
permalink: /2026/01/12/hard-51-n-queens/
tags: [leetcode, hard, array, backtracking, recursion, constraint-satisfaction]
---
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

## Thinking Process

1. **Row-by-Row Placement**: Eliminates row conflicts automatically
- Diagonal: `row - col + n` (shifted to avoid negatives)
- Anti-diagonal: `row + col`

- Build solution incrementally; undo (backtrack) when constraints fail.
- Prune branches early to avoid exploring invalid partial states.
- Sort input to skip duplicate combinations efficiently.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Backtracking tree</text>

  <circle cx="140" cy="30" r="12" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="34" text-anchor="middle" font-size="9">start</text>
  <line x1="140" y1="42" x2="90" y2="65" stroke="#9A9792"/><line x1="140" y1="42" x2="190" y2="65" stroke="#9A9792"/>
  <circle cx="90" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/><circle cx="190" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/>
  <line x1="90" y1="82" x2="60" y2="100" stroke="#9A9792" stroke-dasharray="3"/><line x1="190" y1="82" x2="220" y2="100" stroke="#9A9792" stroke-dasharray="3"/>
  <text x="140" y="118" text-anchor="middle" font-size="11" fill="#6B6560">choose → explore → undo (prune)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Choose / explore / unchoose** *(this problem)* | O(2^n) | O(n) | Subsets, combinations |
| Constraint pruning | Reduced search | O(n) | Early exit on invalid partial |
| Sort + skip duplicates | O(2^n) | O(n) | Combination sum II style |
| Path recording | O(n!) worst | O(n) | Permutations |

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

### Solution Explanation

**Approach:** Choose / explore / unchoose (this problem)

**Key idea:** 1. **Row-by-Row Placement**: Eliminates row conflicts automatically

**How the code works:**
1. **Row-by-Row Placement**: Eliminates row conflicts automatically
- Diagonal: `row - col + n` (shifted to avoid negatives)
- Anti-diagonal: `row + col`
- Build solution incrementally; undo (backtrack) when constraints fail.
- Prune branches early to avoid exploring invalid partial states.
- Sort input to skip duplicate combinations efficiently.

**Walkthrough** — input `n = 4`, expected output `[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]`:

There exist two distinct solutions to the 4-queens puzzle as shown above.

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
## Common Mistakes

1. **n = 1**: Return `[["Q"]]`
2. **n = 2, 3**: No solutions (impossible to place n queens)
3. **n = 4**: 2 solutions
4. **n = 8**: 92 solutions (classic 8-queens problem)

1. **Wrong diagonal indexing**: Not shifting `row - col` correctly
2. **Missing backtrack**: Forgetting to unmark constraints after recursion
3. **Array bounds**: Diagonal array size should be `2 * n` (not `n`)
4. **Board initialization**: Not initializing board with `'.'` characters
5. **Constraint checking order**: Should check all three constraints before placing

## Related Problems

- [LC 52: N-Queens II](https://www.leetcode.com/problems/n-queens-ii/) - Count number of solutions (same problem, just count)
- [LC 37: Sudoku Solver](https://www.leetcode.com/problems/sudoku-solver/) - Similar constraint satisfaction
- [LC 51: N-Queens](https://www.leetcode.com/problems/n-queens/) - This problem

## Key Takeaways

1. **Row-by-Row Placement**: Eliminates row conflicts automatically
2. **Optimized Constraint Checking**: Boolean arrays provide O(1) checking vs O(n) scanning
3. **Diagonal Indexing**: 
   - Diagonal: `row - col + n` (shifted to avoid negatives)
   - Anti-diagonal: `row + col`
4. **Backtracking Pattern**: Place → Recurse → Undo

## References

- [LC 51: N-Queens on LeetCode](https://www.leetcode.com/problems/n-queens/)
- [LeetCode Discuss — LC 51: N-Queens](https://www.leetcode.com/problems/n-queens/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/n-queens/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
