---
layout: post
title: "79. Word Search"
date: 2026-01-12 00:00:00 -0700
categories: [leetcode, medium, array, backtracking, matrix, dfs]
permalink: /2026/01/12/medium-79-word-search/
tags: [leetcode, medium, array, backtracking, matrix, dfs, recursion]
---

# 79. Word Search

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Cell reuse**: Can we reuse the same cell multiple times in a path? (Assumption: No - each cell can be used at most once in a path)

2. **Movement directions**: In which directions can we move? (Assumption: Up, down, left, right - 4 directions, no diagonals)

3. **Case sensitivity**: Are character comparisons case-sensitive? (Assumption: Yes - 'A' and 'a' are different)

4. **Word matching**: Do we need exact match or can it be a subsequence? (Assumption: Exact match - contiguous path forming the exact word)

5. **Starting position**: Can we start from any cell? (Assumption: Yes - can start from any cell that matches the first character of word)

## Solution Approach

This is a classic **backtracking with DFS** problem on a 2D grid. The key insight is to explore all possible paths from each starting position, marking cells as visited during exploration and restoring them when backtracking.

### Key Insights:

1. **DFS Exploration**: Start from each cell and explore all 4 directions
2. **Visited Marking**: Mark current cell as visited (e.g., `'#'`) to avoid revisiting
3. **Backtracking**: Restore cell value after exploring all paths from it
4. **Early Termination**: Return `true` as soon as word is found
5. **Boundary Checking**: Check bounds and character match before recursing

### Algorithm:

1. **For each cell**: Try starting the word search from that cell
2. **DFS Function**:
   - Base case: If `idx == word.length()`, return `true`
   - Check bounds and character match
   - Mark cell as visited
   - Explore all 4 directions
   - Restore cell value (backtrack)
3. **Return**: `true` if word found, `false` otherwise

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

## Key Insights

1. **DFS with Backtracking**: Explore all paths, restore state after exploring
2. **In-Place Marking**: Use `'#'` to mark visited cells (no extra visited array needed)
3. **Early Termination**: Return `true` immediately when word is found
4. **Direction Array**: Clean iteration through 4 directions
5. **Boundary Checking**: Check bounds and character match before recursing

## Edge Cases

1. **Single character word**: `word = "A"` → return `true` if 'A' exists in board
2. **Word longer than board**: Impossible, but handled by bounds checking
3. **All cells same character**: `board = [["A","A"],["A","A"]]`, `word = "AAA"` → return `true`
4. **No matching path**: Return `false` after exploring all possibilities
5. **Word not found**: Return `false`

## Common Mistakes

1. **Not restoring cell value**: Forgetting to backtrack causes incorrect results
2. **Wrong visited marking**: Not marking before recursion or marking incorrectly
3. **Missing bounds check**: Accessing out-of-bounds indices
4. **Wrong character comparison**: Comparing before marking as visited
5. **Not checking all starting positions**: Only checking first cell

## Alternative Approaches

### **Approach 2: Using Visited Array**

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(dfs(board, word, i, j, 0, visited)) return true;
            }
        }
        return false;
    }
    
private:
    bool dfs(vector<vector<char>>& board, string& word, int i, int j, int idx, vector<vector<bool>>& visited) {
        if(idx == word.length()) return true;
        if(i < 0 || i >= board.size() || j < 0 || j >= board[0].size()) return false;
        if(visited[i][j] || board[i][j] != word[idx]) return false;
        
        visited[i][j] = true;
        vector<pair<int, int>> dirs = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
        for(auto& [dr, dc]: dirs) {
            if(dfs(board, word, i + dr, j + dc, idx + 1, visited)) return true;
        }
        visited[i][j] = false;
        return false;
    }
};
```

**Time Complexity:** O(m × n × 4^L)  
**Space Complexity:** O(m × n + L) (visited array + recursion stack)

**Comparison:**
- **In-place marking**: More space-efficient, modifies board
- **Visited array**: Preserves board, uses extra O(m × n) space

## Related Problems

- [LC 212: Word Search II](https://leetcode.com/problems/word-search-ii/) - Find multiple words (use Trie)
- [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) - Similar DFS pattern
- [LC 130: Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) - DFS with boundaries
- [LC 79: Word Search](https://leetcode.com/problems/word-search/) - This problem

---

*This problem demonstrates DFS backtracking on a 2D grid. The key is marking cells as visited during exploration and restoring them when backtracking, allowing the same cell to be used in different paths.*

