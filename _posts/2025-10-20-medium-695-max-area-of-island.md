---
layout: post
title: "[Medium] 695. Max Area of Island"
date: 2025-10-20 13:35:00 -0700
categories: leetcode algorithm medium dfs graph matrix
permalink: /2025/10/20/medium-695-max-area-of-island/
---
**Difficulty:** Medium  
**Category:** DFS, Graph, Matrix


You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value of `1` in the island.

Return the **maximum area** of an island in `grid`. If there is no island, return `0`.

## Examples

### Example 1:
```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

### Example 2:
```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`

## Thinking Process

This is a classic **Connected Components** problem that can be solved using **Depth-First Search (DFS)**. The key insight is to:

1. **Traverse the entire grid** to find all islands
2. **Use DFS to explore each island** and calculate its area
3. **Mark visited cells** to avoid counting them multiple times
4. **Keep track of the maximum area** found

### Algorithm:
1. Iterate through each cell in the grid
2. When we find a land cell (`1`), start DFS from that cell
3. During DFS, mark visited cells as `0` (water) to avoid revisiting
4. Count all connected land cells and return the area
5. Update the maximum area if current island is larger



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
| **Recursive DFS** *(this problem)* | $O(n)$ | $O(h)$ stack | Natural for trees and graphs |
| Iterative DFS (stack) | $O(n)$ | $O(n)$ | Avoid recursion depth limits |
| DFS with memoization | $O(n)$ | $O(n)$ | Overlapping subproblems on graphs |
| Backtracking DFS | $O(2^n)$ typical | $O(n)$ | Enumerate choices with pruning |

## Solution

```cpp
class Solution {
private:
    vector<vector<int>> dirs = {&#123;0, -1&#125;, &#123;0, 1&#125;, &#123;1, 0&#125;, &#123;-1, 0&#125;};

    int dfs(vector<vector<int>>& grid, int r, int c) {
        if(r < 0 || r >= (int)grid.size() || c < 0 || c >= (int)grid[0].size()
           || grid[r][c] == 0) return 0;
        grid[r][c] = 0;
        int rtn = 1;
        for(auto& dir: dirs) {
            rtn += dfs(grid, r + dir[0], c + dir[1]);
        }
        return rtn;
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rtn = 0;
        for(int r = 0; r < (int)grid.size(); r++) {
            for(int c = 0; c < (int)grid[0].size(); c++) {
                rtn = max(rtn, dfs(grid, r, c));
            }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** This is a classic **Connected Components** problem that can be solved using **Depth-First Search (DFS)**. The key insight is to:

**How the code works:**
1. **Traverse the entire grid** to find all islands
2. **Use DFS to explore each island** and calculate its area
3. **Mark visited cells** to avoid counting them multiple times
4. **Keep track of the maximum area** found
1. Iterate through each cell in the grid
2. When we find a land cell (`1`), start DFS from that cell

**Time Complexity:** O(m × n) where m and n are the dimensions of the grid
- Each cell is visited at most once
- DFS visits each cell in an island exactly once

**Space Complexity:** O(m × n) for the recursion stack
- In worst case, the entire grid could be one large island
- Maximum recursion depth equals the number of cells in the largest island
## Explanation

### Step-by-Step Process:

1. **Direction Array:** `dirs` defines the 4 possible directions (up, down, left, right)
2. **DFS Function:** 
   - **Base Cases:** Return 0 if out of bounds or cell is water (`0`)
   - **Mark Visited:** Set current cell to `0` to mark as visited
   - **Count Current Cell:** Start with area = 1
   - **Recursive Calls:** Explore all 4 directions and sum their areas
3. **Main Function:**
   - **Grid Traversal:** Check every cell in the grid
   - **Island Detection:** When we find land (`1`), start DFS
   - **Max Tracking:** Keep track of the largest island found

### Example Walkthrough:
For a simple grid `[[1,1],[1,0]]`:

- **Cell (0,0):** Start DFS, area = 1 + DFS(0,1) + DFS(1,0) + DFS(-1,0) + DFS(0,-1)
- **DFS(0,1):** Area = 1 + DFS(0,2) + DFS(1,1) + DFS(-1,1) + DFS(0,0)
- **DFS(1,0):** Area = 1 + DFS(1,1) + DFS(2,0) + DFS(0,0) + DFS(1,-1)
- **DFS(1,1):** Returns 0 (water cell)
- **Total Area:** 3 (all connected land cells)

### Complexity
**Time Complexity:** O(m × n) where m and n are the dimensions of the grid
- Each cell is visited at most once
- DFS visits each cell in an island exactly once

**Space Complexity:** O(m × n) for the recursion stack
- In worst case, the entire grid could be one large island
- Maximum recursion depth equals the number of cells in the largest island

## References

- [LC 695: Max Area of Island on LeetCode](https://www.leetcode.com/problems/max-area-of-island/)
- [LeetCode Discuss — LC 695: Max Area of Island](https://www.leetcode.com/problems/max-area-of-island/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/max-area-of-island/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **In-place Marking:** Using the input grid to mark visited cells saves space
2. **4-directional Connectivity:** Only horizontal and vertical connections count
3. **DFS Pattern:** Classic connected components problem with area calculation
4. **Boundary Checking:** Always check bounds before accessing grid cells
5. **Max Tracking:** Compare each island's area with the current maximum
