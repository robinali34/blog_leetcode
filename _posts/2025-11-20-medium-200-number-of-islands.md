---
layout: post
title: "[Medium] 200. Number of Islands"
date: 2025-11-20 00:00:00 -0800
categories: leetcode algorithm medium cpp dfs graph matrix problem-solving
permalink: /posts/2025-11-20-medium-200-number-of-islands/
tags: [leetcode, medium, dfs, graph, matrix, connected-components]
---

# [Medium] 200. Number of Islands

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

## Examples

**Example 1:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Island definition**: What is an island? (Assumption: Group of connected '1's - horizontally or vertically adjacent, not diagonally)

2. **Return value**: What should we return? (Assumption: Integer - count of islands in the grid)

3. **Connection rules**: How are cells connected? (Assumption: Horizontal or vertical adjacency - up, down, left, right)

4. **Grid modification**: Can we modify the grid? (Assumption: Yes - can mark visited cells to avoid revisiting)

5. **Empty grid**: What if grid is empty? (Assumption: Return 0 - no islands exist)

## Solution: DFS with In-Place Marking

**Time Complexity:** O(m × n) - Each cell is visited at most once  
**Space Complexity:** O(m × n) - Worst case recursion stack depth

This solution uses Depth-First Search to explore each island and marks visited cells by changing `'1'` to `'0'` to avoid revisiting.

### Solution: DFS In-Place Marking

```cpp
class Solution {
private:
    void dfs(vector<vector<char>>& grid, int row, int col) {
        if (row < 0 || col < 0 || row >= (int)grid.size() || col >= (int)grid[0].size()
            || grid[row][col] != '1') {
                return;
        }
        
        grid[row][col] = '0';
        
        dfs(grid, row - 1, col);
        dfs(grid, row, col - 1);
        dfs(grid, row + 1, col);
        dfs(grid, row, col + 1);
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0) return 0;
        
        int cnt = 0;
        
        for(int i = 0; i < (int)grid.size(); i++) {
            for(int j = 0; j < (int)grid[0].size(); j++) {
                if(grid[i][j] == '1') {
                    dfs(grid, i, j);
                    cnt++;
                }
            }
        }
        
        return cnt;
    }
};
```

## How the Algorithm Works

### Step-by-Step Example: `grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]`

```
Initial Grid:
  0 1 2 3 4
0 1 1 0 0 0
1 1 1 0 0 0
2 0 0 1 0 0
3 0 0 0 1 1

i=0, j=0: Found '1' → Start DFS
  DFS(0,0): Mark (0,0) as '0'
    DFS(-1,0): Out of bounds, return
    DFS(0,-1): Out of bounds, return
    DFS(1,0): Found '1' → Mark (1,0) as '0'
      DFS(0,0): Already '0', return
      DFS(1,-1): Out of bounds, return
      DFS(2,0): Found '0', return
      DFS(1,1): Found '1' → Mark (1,1) as '0'
        DFS(0,1): Found '1' → Mark (0,1) as '0'
          ... (explore all connected)
    DFS(0,1): Already '0', return
  cnt = 1

i=0, j=2: Found '0', skip
i=0, j=3: Found '0', skip
...
i=2, j=2: Found '1' → Start DFS
  DFS(2,2): Mark (2,2) as '0'
    ... (explore all connected)
  cnt = 2

i=3, j=3: Found '1' → Start DFS
  DFS(3,3): Mark (3,3) as '0'
    DFS(3,4): Found '1' → Mark (3,4) as '0'
      ... (explore all connected)
  cnt = 3

Result: 3 islands
```

### Visual Representation

```
Island 1:        Island 2:    Island 3:
  1 1             1            1 1
  1 1             0            0 0
  0 0             0            0 0
```

## Key Insights

1. **Connected Components**: Each island is a connected component of '1's
2. **In-Place Marking**: Change '1' to '0' to mark visited cells (no extra visited array needed)
3. **DFS Exploration**: Use DFS to explore all connected land cells
4. **4-Directional**: Only check up, down, left, right (not diagonals)
5. **Count on Discovery**: Increment count when finding a new '1' (start of new island)

## Algorithm Breakdown

```cpp
int numIslands(vector<vector<char>>& grid) {
    // Handle empty grid
    if (grid.size() == 0 || grid[0].size() == 0) return 0;
    
    int cnt = 0;
    
    // Scan entire grid
    for(int i = 0; i < grid.size(); i++) {
        for(int j = 0; j < grid[0].size(); j++) {
            // Found unvisited land cell
            if(grid[i][j] == '1') {
                // Explore entire island
                dfs(grid, i, j);
                // Count this island
                cnt++;
            }
        }
    }
    
    return cnt;
}

void dfs(vector<vector<char>>& grid, int row, int col) {
    // Base cases: out of bounds or water/visited
    if (row < 0 || col < 0 || 
        row >= grid.size() || col >= grid[0].size() ||
        grid[row][col] != '1') {
        return;
    }
    
    // Mark as visited by changing to '0'
    grid[row][col] = '0';
    
    // Explore all 4 directions
    dfs(grid, row - 1, col);  // Up
    dfs(grid, row, col - 1);   // Left
    dfs(grid, row + 1, col);   // Down
    dfs(grid, row, col + 1);   // Right
}
```

## Edge Cases

1. **Empty grid**: `[]` or `[[]]` → return `0`
2. **No islands**: All `'0'` → return `0`
3. **Single cell**: `[["1"]]` → return `1`
4. **Single row**: `[["1","1","0"]]` → return `1`
5. **Single column**: `[["1"],["1"],["0"]]` → return `1`
6. **All land**: Entire grid is `'1'` → return `1`

## Alternative Approaches

### Approach 2: BFS (Breadth-First Search)

**Time Complexity:** O(m × n)  
**Space Complexity:** O(min(m, n)) - Queue size

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size(), n = grid[0].size();
        int cnt = 0;
        vector<vector<int>> dirs = \{\{-1,0\}, \{1,0\}, \{0,-1\}, \{0,1\}\};
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == '1') {
                    cnt++;
                    queue<pair<int,int>> q;
                    q.push({i, j});
                    grid[i][j] = '0';
                    
                    while(!q.empty()) {
                        auto [r, c] = q.front();
                        q.pop();
                        
                        for(auto& dir : dirs) {
                            int nr = r + dir[0];
                            int nc = c + dir[1];
                            
                            if(nr >= 0 && nr < m && nc >= 0 && nc < n 
                               && grid[nr][nc] == '1') {
                                grid[nr][nc] = '0';
                                q.push({nr, nc});
                            }
                        }
                    }
                }
            }
        }
        
        return cnt;
    }
};
```

**Pros:**
- Iterative (no recursion stack)
- Better space complexity for wide islands

**Cons:**
- More verbose
- Requires queue data structure

### Approach 3: Union-Find (Disjoint Set)

**Time Complexity:** O(m × n × α(m × n)) where α is inverse Ackermann  
**Space Complexity:** O(m × n)

```cpp
class Solution {
private:
    vector<int> parent;
    int find(int x) {
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        parent[find(x)] = find(y);
    }
    
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size(), n = grid[0].size();
        parent.resize(m * n);
        iota(parent.begin(), parent.end(), 0);
        
        int islands = 0;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == '1') {
                    islands++;
                    int idx = i * n + j;
                    
                    if(i > 0 && grid[i-1][j] == '1') {
                        int up = (i-1) * n + j;
                        if(find(idx) != find(up)) {
                            unite(idx, up);
                            islands--;
                        }
                    }
                    if(j > 0 && grid[i][j-1] == '1') {
                        int left = i * n + (j-1);
                        if(find(idx) != find(left)) {
                            unite(idx, left);
                            islands--;
                        }
                    }
                }
            }
        }
        
        return islands;
    }
};
```

**Pros:**
- Useful for dynamic island problems
- Can handle online queries

**Cons:**
- More complex implementation
- Overkill for this problem

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DFS In-Place** | O(m×n) | O(m×n) | Simple, intuitive | Recursion stack |
| **BFS** | O(m×n) | O(min(m,n)) | Iterative, better space | More verbose |
| **Union-Find** | O(m×n×α) | O(m×n) | Good for dynamic | Complex |

## Implementation Details

### Boundary Checking

```cpp
if (row < 0 || col < 0 || 
    row >= (int)grid.size() || col >= (int)grid[0].size() ||
    grid[row][col] != '1') {
    return;
}
```

**Why cast to `int`?**
- Prevents comparison warnings between `int` and `size_t`
- Ensures correct comparison behavior

### In-Place Marking

```cpp
grid[row][col] = '0';
```

**Why change to '0'?**
- Marks cell as visited without extra memory
- Prevents revisiting same cell
- Simplifies code (no separate visited array)

### Direction Exploration Order

```cpp
dfs(grid, row - 1, col);  // Up
dfs(grid, row, col - 1);  // Left
dfs(grid, row + 1, col);  // Down
dfs(grid, row, col + 1);  // Right
```

Order doesn't matter - all 4 directions must be explored.

## Common Mistakes

1. **Missing boundary checks**: Accessing `grid[-1][0]` or `grid[m][n]`
2. **Not marking visited**: Infinite recursion if cells aren't marked
3. **Wrong character comparison**: Using `1` instead of `'1'` (char vs int)
4. **Empty grid handling**: Not checking for empty grid
5. **Diagonal connections**: Checking 8 directions instead of 4

## Optimization Tips

1. **Early Exit**: Can add early exit if all cells processed
2. **Direction Array**: Use array for cleaner code:
   ```cpp
   vector<vector<int>> dirs = \{\{-1,0\}, \{1,0\}, \{0,-1\}, \{0,1\}\};
   for(auto& dir : dirs) {
       dfs(grid, row + dir[0], col + dir[1]);
   }
   ```
3. **BFS for Wide Islands**: Use BFS if islands are very wide (less stack depth)

## Related Problems

- [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) - Find largest island area
- [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) - Mark surrounded regions
- [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/) - Calculate island perimeter
- [305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) - Dynamic islands (Union-Find)
- [694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/) - Count distinct island shapes

## Real-World Applications

1. **Image Processing**: Connected component labeling
2. **Computer Vision**: Object detection and segmentation
3. **Geographic Information Systems**: Counting landmasses
4. **Network Analysis**: Finding connected network clusters
5. **Game Development**: Flood fill algorithms

## Pattern Recognition

This problem demonstrates the **"Connected Components"** pattern:

```
1. Scan grid for unvisited components
2. Use DFS/BFS to explore entire component
3. Mark visited to avoid revisiting
4. Count each component found
```

Similar problems:
- Max Area of Island
- Surrounded Regions
- Island Perimeter
- Number of Provinces

## DFS vs BFS Choice

### When to Use DFS

- **Pros**: 
  - Simpler recursive implementation
  - Natural for tree-like exploration
  - Less code
  
- **Cons**:
  - O(m×n) recursion stack in worst case
  - Stack overflow risk for very large grids

### When to Use BFS

- **Pros**:
  - O(min(m,n)) space for queue
  - No stack overflow risk
  - Better for wide islands
  
- **Cons**:
  - More verbose code
  - Requires queue data structure

**Recommendation**: DFS is preferred for this problem due to simplicity, unless dealing with very large grids.

## Why In-Place Marking Works

1. **No Extra Memory**: Saves O(m×n) space
2. **Simple Check**: `grid[i][j] != '1'` handles both water and visited
3. **Permanent Marking**: Once marked, never needs to be revisited
4. **Grid Modification**: Problem allows modifying input grid

---

*This problem is a classic introduction to graph traversal algorithms, demonstrating how DFS can efficiently solve connected component problems.*

