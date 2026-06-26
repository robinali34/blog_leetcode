---
layout: post
title: "[Medium] 79. Word Search"
date: 2026-01-12 00:00:00 -0700
categories: [leetcode, medium, array, backtracking, matrix, dfs]
permalink: /2026/01/12/medium-79-word-search/
tags: [leetcode, medium, array, backtracking, matrix, dfs, recursion]
---
Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Examples

**Example 1:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## Constraints

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

## Thinking Process

1. **DFS with Backtracking**: Explore all paths, restore state after exploring

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
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Solution

### **Solution: Backtracking with DFS**

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        rows = board.size();
        cols = board[0].size();
        for(int r = 0; r < rows; r++) {
            for(int c = 0; c < cols; c++) {
                if(backtrack(board, word, r, c, 0)) return true;
            }
        }
        return false;
    }
private:
    int rows, cols;
    const vector<pair<int, int>> dirs = \{\{0, 1\}, \{0, -1\}, \{1, 0\}, \{-1, 0\}\};

    bool backtrack(vector<vector<char>>& board, const string& word, int row, int col, int idx) {
        if(idx == word.length()) return true;
        if(row < 0 || row >= rows || col < 0 || col >= cols || board[row][col] != word[idx]) {
            return false;
        }

        board[row][col] = '#';
        for(auto& [dr, dc]: dirs) {
            if(backtrack(board, word, row + dr, col + dc, idx + 1)) return true;
        }
        board[row][col] = word[idx];
        return false;
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **DFS with Backtracking**: Explore all paths, restore state after exploring

**How the code works:**
1. **DFS with Backtracking**: Explore all paths, restore state after exploring
- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.

**Walkthrough** — input `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"`, expected output `true`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

### **Algorithm Explanation:**

1. **Main Function (Lines 3-12)**:
   - Store `rows` and `cols` dimensions
   - **For each cell `(r, c)`**: Try starting word search from that cell
   - If any starting position finds the word, return `true`
   - Otherwise, return `false`

2. **Backtrack Function (Lines 17-28)**:
   - **Base Case (Line 18)**: If `idx == word.length()`, we've matched entire word → return `true`
   - **Validation (Lines 19-21)**:
     - Check bounds: `row` and `col` within grid
     - Check character match: `board[row][col] == word[idx]`
     - If invalid, return `false`
   - **Mark as Visited (Line 23)**: Set `board[row][col] = '#'` to prevent revisiting
   - **Explore Directions (Lines 24-26)**:
     - Try all 4 directions: right, left, down, up
     - If any direction finds the word, return `true` immediately
   - **Backtrack (Line 27)**: Restore original character `board[row][col] = word[idx]`
   - **Return (Line 28)**: Return `false` if no path found

### **Why This Works:**

- **DFS Exploration**: Explores all possible paths from each starting position
- **Visited Marking**: Using `'#'` prevents revisiting the same cell in current path
- **Backtracking**: Restoring cell value allows exploring other paths that might use this cell
- **Early Termination**: Returns `true` as soon as word is found (no need to explore further)
- **Direction Array**: Clean way to iterate through 4 directions

### **Example Walkthrough:**

**For `board = [["A","B","C"],["S","F","C"]], word = "ABCCED"`:**

```
Starting from (0,0) with word "ABCCED":

backtrack(0, 0, 0):
  idx=0, board[0][0]='A' == word[0]='A' ✓
  Mark: board[0][0]='#'
  
  Try direction (0,1): backtrack(0, 1, 1)
    idx=1, board[0][1]='B' == word[1]='B' ✓
    Mark: board[0][1]='#'
    
    Try direction (0,2): backtrack(0, 2, 2)
      idx=2, board[0][2]='C' == word[2]='C' ✓
      Mark: board[0][2]='#'
      
      Try direction (1,2): backtrack(1, 2, 3)
        idx=3, board[1][2]='C' == word[3]='C' ✓
        Mark: board[1][2]='#'
        
        Try direction (1,1): backtrack(1, 1, 4)
          idx=4, board[1][1]='F' != word[4]='E' ✗
        Try direction (0,2): board[0][2]='#' ✗ (visited)
        Try direction (2,2): Out of bounds ✗
        Try direction (1,0): backtrack(1, 0, 4)
          idx=4, board[1][0]='S' != word[4]='E' ✗
        Backtrack: board[1][2]='C'
        
      Try direction (1,1): backtrack(1, 1, 3)
        idx=3, board[1][1]='F' != word[3]='C' ✗
      Try direction (0,1): board[0][1]='#' ✗ (visited)
      Try direction (1,3): Out of bounds ✗
      Backtrack: board[0][2]='C'
    
    Try direction (1,1): backtrack(1, 1, 2)
      idx=2, board[1][1]='F' != word[2]='C' ✗
    Try direction (0,0): board[0][0]='#' ✗ (visited)
    Try direction (1,2): backtrack(1, 2, 2)
      idx=2, board[1][2]='C' == word[2]='C' ✓
      Mark: board[1][2]='#'
      
      Try direction (1,3): Out of bounds ✗
      Try direction (1,1): backtrack(1, 1, 3)
        idx=3, board[1][1]='F' != word[3]='C' ✗
      Try direction (2,2): Out of bounds ✗
      Try direction (0,2): backtrack(0, 2, 3)
        idx=3, board[0][2]='C' == word[3]='C' ✓
        Mark: board[0][2]='#'
        
        Try direction (0,3): Out of bounds ✗
        Try direction (0,1): board[0][1]='#' ✗ (visited)
        Try direction (1,2): board[1][2]='#' ✗ (visited)
        Try direction (-1,2): Out of bounds ✗
        Backtrack: board[0][2]='C'
      Backtrack: board[1][2]='C'
    Backtrack: board[0][1]='B'
  Backtrack: board[0][0]='A'

No path found from (0,0). Try other starting positions...
```

**Note**: The actual path for "ABCCED" might not exist in this small example. The algorithm correctly explores all possibilities.

### **Complexity Analysis:**

- **Time Complexity:** O(m × n × 4^L) where L is word length
  - For each of `m × n` starting positions
  - Explore up to `4^L` paths (4 directions, L depth)
  - With pruning (character mismatch), actual complexity is better
- **Space Complexity:** O(L)
  - Recursion stack depth: at most `L` (word length)
  - No additional data structures (modifies board in-place)
## Common Mistakes

1. **Single character word**: `word = "A"` → return `true` if 'A' exists in board
2. **Word longer than board**: Impossible, but handled by bounds checking
3. **All cells same character**: `board = [["A","A"],["A","A"]]`, `word = "AAA"` → return `true`
4. **No matching path**: Return `false` after exploring all possibilities
5. **Word not found**: Return `false`

1. **Not restoring cell value**: Forgetting to backtrack causes incorrect results
2. **Wrong visited marking**: Not marking before recursion or marking incorrectly
3. **Missing bounds check**: Accessing out-of-bounds indices
4. **Wrong character comparison**: Comparing before marking as visited
5. **Not checking all starting positions**: Only checking first cell

## Related Problems

- [LC 212: Word Search II](https://www.leetcode.com/problems/word-search-ii/) - Find multiple words (use Trie)
- [LC 200: Number of Islands](https://www.leetcode.com/problems/number-of-islands/) - Similar DFS pattern
- [LC 130: Surrounded Regions](https://www.leetcode.com/problems/surrounded-regions/) - DFS with boundaries
- [LC 79: Word Search](https://www.leetcode.com/problems/word-search/) - This problem

## Key Takeaways

1. **DFS with Backtracking**: Explore all paths, restore state after exploring
2. **In-Place Marking**: Use `'#'` to mark visited cells (no extra visited array needed)
3. **Early Termination**: Return `true` immediately when word is found
4. **Direction Array**: Clean iteration through 4 directions
5. **Boundary Checking**: Check bounds and character match before recursing

## References

- [LC 79: Word Search on LeetCode](https://www.leetcode.com/problems/word-search/)
- [LeetCode Discuss — LC 79: Word Search](https://www.leetcode.com/problems/word-search/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/word-search/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
