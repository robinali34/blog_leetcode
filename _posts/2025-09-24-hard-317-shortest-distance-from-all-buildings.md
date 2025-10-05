---
layout: post
title: "[Hard] 317. Shortest Distance from All Buildings"
date: 2025-09-24 19:00:00 -0000
categories: leetcode algorithm bfs graph data-structures matrix shortest-path hard cpp shortest-distance buildings problem-solving
---

# [Hard] 317. Shortest Distance from All Buildings

<!-- Fixed Liquid syntax error -->

This is a graph traversal problem that requires finding the optimal location to build a new building such that the total distance to all existing buildings is minimized. The key insight is using BFS from each building to calculate distances and finding the spot with minimum total distance.

## Problem Description

Given a 2D grid where:
- `0` represents empty land
- `1` represents a building  
- `2` represents an obstacle

Find the shortest distance from all buildings to a single empty land cell. Return -1 if it's impossible.

### Examples

**Example 1:**
```
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: The optimal location is (1,2) with total distance 7.
```

**Example 2:**
```
Input: grid = [[1,0]]
Output: 1
```

**Example 3:**
```
Input: grid = [[1]]
Output: -1
```

### Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0, 1, or 2
- There will be at least one building in the grid

## Approach

There are three main approaches to solve this problem:

1. **BFS from Each Empty Land**: For each empty land, BFS to all buildings
2. **BFS from Each Building**: For each building, BFS to all empty lands and accumulate distances
3. **Optimized BFS with Grid Modification**: Use grid values to track reachability

## Solution 1: BFS from Each Empty Land

**Time Complexity:** O(m²n²) - For each empty land, BFS to all buildings  
**Space Complexity:** O(mn) - For visited array and queue

```cpp
class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {
        const int rows = grid.size();
        const int cols = grid[0].size();

        int totalHouses = 0;
        for (const auto& row : grid) {
            for (const auto& cell : row) {
                if (cell == 1) totalHouses++;
            }
        }

        int minDistance = INT_MAX;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 0) {
                    minDistance = std::min(minDistance, bfs(grid, r, c, totalHouses));
                }
            }
        }

        return (minDistance == INT_MAX) ? -1 : minDistance;
    }

private:
    int bfs(vector<vector<int>>& grid, int startRow, int startCol, int totalHouses) {
        constexpr array<pair<int, int>, 4> directions\{\{
            \{1, 0\}, \{-1, 0\}, \{0, 1\}, \{0, -1\}
        \}\};

        const int rows = grid.size();
        const int cols = grid[0].size();

        int distanceSum = 0;
        int housesReached = 0;
        int steps = 0;

        queue<pair<int, int>> q;
        q.emplace(startRow, startCol);

        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        visited[startRow][startCol] = true;

        while (!q.empty() && housesReached != totalHouses) {
            const int levelSize = q.size();

            for (int i = 0; i < levelSize; ++i) {
                auto [r, c] = q.front();
                q.pop();

                if (grid[r][c] == 1) {
                    distanceSum += steps;
                    ++housesReached;
                    continue;
                }

                for (const auto& [dr, dc] : directions) {
                    int nr = r + dr;
                    int nc = c + dc;

                    if (nr >= 0 && nc >= 0 && nr < rows && nc < cols &&
                        !visited[nr][nc] && grid[nr][nc] != 2) {
                        visited[nr][nc] = true;
                        q.emplace(nr, nc);
                    }
                }
            }
            steps++;
        }

        if (housesReached != totalHouses) {
            for (int r = 0; r < rows; ++r) {
                for (int c = 0; c < cols; ++c) {
                    if (grid[r][c] == 0 && visited[r][c]) {
                        grid[r][c] = 2;  // Mark as unreachable
                    }
                }
            }
            return INT_MAX;
        }

        return distanceSum;
    }
};
```

## Solution 2: BFS from Each Building

**Time Complexity:** O(m²n²) - For each building, BFS to all empty lands  
**Space Complexity:** O(mn) - For distance tracking and visited array

```cpp
class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {
        const int cols = grid[0].size(), rows = grid.size();
        int minDisatnce = INT_MAX, totalHouses = 0;
        vector<vector<array<int, 2>>> distances(rows, vector<array<int, 2>> (cols, {0, 0}));
        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(grid[row][col] == 1) {
                    totalHouses++;
                    bfs(grid, distances, row, col);
                }
            }
        }
        for (int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(distances[row][col][1] == totalHouses) {
                    minDisatnce = min(minDisatnce, distances[row][col][0]);
                }
            }
        }
        return minDisatnce == INT_MAX ? -1: minDisatnce;
    }

private:
    void bfs(vector<vector<int>>& grid, vector<vector<array<int, 2>>>& distance, int row, int col) {
        constexpr array<pair<int, int>, 4> dirs = \{\{\{1, 0\}, \{-1, 0\}, \{0, 1\}, \{0, -1\}\}\};
        const int rows = grid.size(), cols = grid[0].size();
        queue<pair<int, int>> q;
        q.emplace(row, col);
        vector<vector<bool>> vis (rows, vector<bool>(cols, false));
        vis[row][col] = true;
        int steps = 0;
        while(!q.empty()) {
            for (int i = q.size(); i > 0; i--) {
                auto cur = q.front();
                q.pop();
                row = cur.first;
                col = cur.second;
                if(grid[row][col] == 0) {
                    distance[row][col][0] += steps;
                    distance[row][col][1] += 1;
                }
                for(auto& [dr, dc]: dirs) {
                    int nextRow = row + dr;
                    int nextCol = col + dc;
                    if (nextRow >= 0 && nextCol >= 0 && nextRow < rows && nextCol < cols) {
                        if(!vis[nextRow][nextCol] && grid[nextRow][nextCol] == 0) {
                            vis[nextRow][nextCol] = true;
                            q.emplace(nextRow, nextCol);
                        }
                    }
                }
            }
            steps++;
        }
    }
};
```

## Solution 3: Optimized BFS with Grid Modification

**Time Complexity:** O(m²n²) - For each building, BFS to all reachable empty lands  
**Space Complexity:** O(mn) - For total distance tracking

```cpp
class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {
        const int rows = grid.size(), cols = grid[0].size();
        constexpr array<pair<int, int>, 4> dirs = \{\{\{1, 0\}, \{-1, 0\}, \{0, 1\}, \{0, -1\}\}\};
        int emptyLandValue =0, minDist = INT_MAX;
        vector<vector<int>> total(rows, vector<int> (cols, 0));
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if(grid[row][col] == 1) {
                    minDist = INT_MAX;
                    queue<pair<int, int>> q;
                    q.emplace(row, col);
                    int steps = 0;
                    while(!q.empty()) {
                        steps++;
                        for(int level = q.size(); level > 0; level--) {
                            auto cur = q.front();
                            q.pop();
                            for (auto& [dr, dc]: dirs) {
                                int nextRow = cur.first + dr;
                                int nextCol = cur.second + dc;
                                if(nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols
                                && grid[nextRow][nextCol] == emptyLandValue){
                                    grid[nextRow][nextCol]--;
                                    total[nextRow][nextCol] += steps;
                                    q.emplace(nextRow, nextCol);
                                    minDist = min(minDist, total[nextRow][nextCol]);
                                }
                            }
                        }
                    }
                    emptyLandValue--;
                }
            }
        }
        return minDist == INT_MAX ? -1 : minDist;
    }
};
```

## Step-by-Step Example

Let's trace through Solution 2 with grid = `[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]`:

**Step 1:** Count total houses = 3

**Step 2:** BFS from each building
- Building at (0,0): Updates distances to all reachable empty lands
- Building at (0,4): Updates distances to all reachable empty lands  
- Building at (2,2): Updates distances to all reachable empty lands

**Step 3:** Check each empty land
- Only empty lands reachable by all 3 buildings are considered
- Find minimum total distance among valid positions

**Result:** Position (1,2) with total distance 7

## Key Insights

1. **BFS Level Processing**: Process each level of BFS to calculate distances correctly
2. **Reachability Check**: Ensure all buildings can reach the chosen empty land
3. **Distance Accumulation**: Sum distances from all buildings to each empty land
4. **Grid Optimization**: Use grid modification to track reachability efficiently

## Approach Comparison

| Approach | Pros | Cons |
|----------|------|------|
| **Solution 1** | Simple logic, easy to understand | Less efficient, modifies original grid |
| **Solution 2** | Clean separation, tracks reachability | Uses extra space for distance tracking |
| **Solution 3** | Most efficient, reuses grid space | Complex logic, harder to debug |

## Common Mistakes

- **Incorrect Distance Calculation**: Not using level-by-level BFS
- **Reachability Issues**: Not checking if all buildings can reach empty land
- **Grid Modification**: Modifying original grid without proper restoration
- **Boundary Conditions**: Not handling edge cases properly

---
