---
layout: post
title: "LC 419: Battleships in a Board"
date: 2025-10-20 17:00:00 -0700
categories: leetcode medium array matrix
permalink: /posts/2025-10-20-medium-419-battleships-in-a-board/
tags: [leetcode, medium, array, matrix, dfs, battleship]
---

# LC 419: Battleships in a Board

**Difficulty:** Medium  
**Category:** Array, Matrix, DFS  
**Companies:** Amazon, Google, Microsoft

## Problem Statement

Given an `m x n` matrix `board` where each cell is either a battleship `'X'` or empty `'.'`, return the number of the battleships on `board`.

Battleships can only be placed horizontally or vertically on `board`. In other words, they can only be made of the shape `1 x k` (1 row, k columns) or `k x 1` (k rows, 1 column), where `k` can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

### Examples

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

### Constraints

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

### Approach 2: DFS with Visited Tracking

**Algorithm:**
1. Mark visited battleships to avoid double counting
2. Use DFS to explore each battleship completely
3. Count each battleship only once

**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n) for visited array

```cpp
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        int count = 0;
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == 'X' && !visited[i][j]) {
                    dfs(board, visited, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    
private:
    void dfs(vector<vector<char>>& board, vector<vector<bool>>& visited, int i, int j) {
        if(i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || 
           board[i][j] != 'X' || visited[i][j]) return;
        
        visited[i][j] = true;
        
        // Explore in all four directions
        dfs(board, visited, i + 1, j);
        dfs(board, visited, i - 1, j);
        dfs(board, visited, i, j + 1);
        dfs(board, visited, i, j - 1);
    }
};
```

### Approach 3: Union Find

**Algorithm:**
1. Use Union Find to group connected `'X'` cells
2. Count the number of distinct groups

**Time Complexity:** O(m × n × α(m × n)) where α is inverse Ackermann function  
**Space Complexity:** O(m × n)

```cpp
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        UnionFind uf(m * n);
        int count = 0;
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == 'X') {
                    int curr = i * n + j;
                    if(i > 0 && board[i - 1][j] == 'X') {
                        uf.unionSets(curr, (i - 1) * n + j);
                    }
                    if(j > 0 && board[i][j - 1] == 'X') {
                        uf.unionSets(curr, i * n + (j - 1));
                    }
                }
            }
        }
        
        unordered_set<int> roots;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == 'X') {
                    roots.insert(uf.find(i * n + j));
                }
            }
        }
        
        return roots.size();
    }
    
private:
    class UnionFind {
        vector<int> parent, rank;
        
    public:
        UnionFind(int n) : parent(n), rank(n, 0) {
            iota(parent.begin(), parent.end(), 0);
        }
        
        int find(int x) {
            if(parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        
        void unionSets(int x, int y) {
            int px = find(x), py = find(y);
            if(px != py) {
                if(rank[px] < rank[py]) swap(px, py);
                parent[py] = px;
                if(rank[px] == rank[py]) rank[px]++;
            }
        }
    };
};
```

## Algorithm Analysis

### Top-Left Corner Approach (Recommended)

**Why it works:**
- Each battleship has exactly one top-left corner
- By checking only top and left neighbors, we avoid double counting
- No extra space needed

**Key Conditions:**
```cpp
if(i > 0 && board[i - 1][j] == 'X') continue;  // Not top-left
if(j > 0 && board[i][j - 1] == 'X') continue;  // Not top-left
```

### Complexity Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Top-Left Corner | O(m×n) | O(1) | Optimal, simple | None |
| DFS | O(m×n) | O(m×n) | Clear logic | Extra space |
| Union Find | O(m×n×α) | O(m×n) | Handles complex shapes | Overkill for this problem |

## Key Insights

1. **Battleship Structure**: Each battleship is a connected component of `'X'` cells
2. **No Adjacent Ships**: Ships are separated by at least one empty cell
3. **Top-Left Corner**: Each battleship has exactly one top-left corner
4. **Single Pass**: Can count ships in one pass without modification

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

- [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [LC 695: Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [LC 130: Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

## Implementation Notes

1. **Boundary Checks**: Always check array bounds before accessing
2. **Type Casting**: Cast `board.size()` to `int` to avoid comparison warnings
3. **Early Continue**: Use `continue` to skip non-top-left corners
4. **Single Pass**: No need to modify the original board

---

*This problem demonstrates the power of identifying unique characteristics (top-left corners) to solve problems efficiently without extra space.*
