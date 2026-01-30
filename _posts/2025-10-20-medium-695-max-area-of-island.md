---
layout: post
title: "695. Max Area of Island"
date: 2025-10-20 13:35:00 -0700
categories: leetcode algorithm medium dfs graph matrix
permalink: /2025/10/20/medium-695-max-area-of-island/
---

# 695. Max Area of Island

**Difficulty:** Medium  
**Category:** DFS, Graph, Matrix

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Island definition**: What is an island? (Assumption: Group of connected 1s - horizontally or vertically adjacent, not diagonally)

2. **Area calculation**: How is area calculated? (Assumption: Number of 1s in the island - count of connected land cells)

3. **Optimization goal**: What are we optimizing for? (Assumption: Maximum area among all islands)

4. **Return value**: What should we return? (Assumption: Integer - maximum area of an island, 0 if no islands)

5. **Empty grid**: What if grid is empty? (Assumption: Return 0 - no islands exist)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to find max island area. Let me check all cells and count connected 1s."

**Naive Solution**: For each cell, if it's 1, try to count connected 1s by checking neighbors recursively without tracking visited.

**Complexity**: O(m × n × (m × n)) worst case, O(m × n) space

**Issues**:
- Revisits cells multiple times
- Very inefficient
- Doesn't track visited cells
- Can be optimized

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use DFS/BFS to explore each island, mark visited cells to avoid revisiting."

**Improved Solution**: Use DFS/BFS to explore each island. Mark visited cells (set to 0 or use visited array). Count cells in each island, track maximum.

**Complexity**: O(m × n) time, O(m × n) space

**Improvements**:
- Visited tracking prevents revisiting
- O(m × n) time is optimal
- DFS/BFS explores islands correctly
- Handles all cases correctly

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "DFS with grid modification is optimal. Modify grid in-place to mark visited."

**Best Solution**: DFS approach is optimal. For each unvisited 1, perform DFS to count island size. Mark visited cells by setting to 0 (modify grid in-place) to avoid revisiting.

**Complexity**: O(m × n) time, O(m × n) space (recursion stack)

**Key Realizations**:
1. DFS/BFS is natural for connected components
2. In-place modification saves space
3. O(m × n) time is optimal - visit each cell once
4. O(m × n) space for recursion stack is necessary

## Approach

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

## Complexity Analysis

**Time Complexity:** O(m × n) where m and n are the dimensions of the grid
- Each cell is visited at most once
- DFS visits each cell in an island exactly once

**Space Complexity:** O(m × n) for the recursion stack
- In worst case, the entire grid could be one large island
- Maximum recursion depth equals the number of cells in the largest island

## Key Insights

1. **In-place Marking:** Using the input grid to mark visited cells saves space
2. **4-directional Connectivity:** Only horizontal and vertical connections count
3. **DFS Pattern:** Classic connected components problem with area calculation
4. **Boundary Checking:** Always check bounds before accessing grid cells
5. **Max Tracking:** Compare each island's area with the current maximum

## Alternative Approaches

### BFS Approach:
```cpp
int bfs(vector<vector<int>>& grid, int r, int c) {
    queue<pair<int,int>> q;
    q.push({r, c});
    grid[r][c] = 0;
    int area = 0;
    
    while(!q.empty()) {
        auto [row, col] = q.front();
        q.pop();
        area++;
        
        for(auto& dir: dirs) {
            int newR = row + dir[0], newC = col + dir[1];
            if(newR >= 0 && newR < grid.size() && 
               newC >= 0 && newC < grid[0].size() && 
               grid[newR][newC] == 1) {
                grid[newR][newC] = 0;
                q.push({newR, newC});
            }
        }
    }
    return area;
}
```

This problem demonstrates the fundamental pattern for finding connected components in a 2D grid using DFS or BFS.
