---
layout: post
title: "[Medium] 200. Number of Islands"
date: 2025-11-20 00:00:00 -0800
categories: leetcode algorithm medium cpp dfs graph matrix problem-solving
permalink: /posts/2025-11-20-medium-200-number-of-islands/
tags: [leetcode, medium, dfs, graph, matrix, connected-components]
---
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

## Thinking Process

1. **Connected Components**: Each island is a connected component of '1's

- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.



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
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Solution

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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **Connected Components**: Each island is a connected component of '1's

**How the code works:**
1. **Connected Components**: Each island is a connected component of '1's
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `grid = [`, expected output `1`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DFS In-Place** | O(m×n) | O(m×n) | Simple, intuitive | Recursion stack |
| **BFS** | O(m×n) | O(min(m,n)) | Iterative, better space | More verbose |
| **Union-Find** | O(m×n×α) | O(m×n) | Good for dynamic | Complex |
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

### Complexity
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

1. **Empty grid**: `[]` or `[[]]` → return `0`
2. **No islands**: All `'0'` → return `0`
3. **Single cell**: `[["1"]]` → return `1`
4. **Single row**: `[["1","1","0"]]` → return `1`
5. **Single column**: `[["1"],["1"],["0"]]` → return `1`
6. **All land**: Entire grid is `'1'` → return `1`

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

- [695. Max Area of Island](https://www.leetcode.com/problems/max-area-of-island/) - Find largest island area
- [130. Surrounded Regions](https://www.leetcode.com/problems/surrounded-regions/) - Mark surrounded regions
- [463. Island Perimeter](https://www.leetcode.com/problems/island-perimeter/) - Calculate island perimeter
- [305. Number of Islands II](https://www.leetcode.com/problems/number-of-islands-ii/) - Dynamic islands (Union-Find)
- [694. Number of Distinct Islands](https://www.leetcode.com/problems/number-of-distinct-islands/) - Count distinct island shapes

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

## Key Takeaways

1. **Connected Components**: Each island is a connected component of '1's
2. **In-Place Marking**: Change '1' to '0' to mark visited cells (no extra visited array needed)
3. **DFS Exploration**: Use DFS to explore all connected land cells
4. **4-Directional**: Only check up, down, left, right (not diagonals)
5. **Count on Discovery**: Increment count when finding a new '1' (start of new island)

## References

- [LC 200: Number of Islands on LeetCode](https://www.leetcode.com/problems/number-of-islands/)
- [LeetCode Discuss — LC 200: Number of Islands](https://www.leetcode.com/problems/number-of-islands/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/number-of-islands/editorial/) *(may require premium)*

## Template Reference

- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
