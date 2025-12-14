---
layout: post
title: "[Medium] 994. Rotting Oranges"
date: 2025-12-13 00:00:00 -0800
categories: leetcode algorithm medium cpp array matrix bfs problem-solving
---

{% raw %}
# [Medium] 994. Rotting Oranges

You are given an `m x n` grid where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If this is impossible, return `-1`.

## Examples

**Example 1:**
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**
```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**
```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are no fresh oranges at minute 0, the answer is just 0.
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

## Solution 1: Multi-Source BFS with Level Marker (Recommended)

**Time Complexity:** O(m × n) - Each cell is visited at most once  
**Space Complexity:** O(m × n) - For the queue

This solution uses BFS starting from all rotten oranges simultaneously. A special marker `{-1, -1}` is used to separate levels (minutes).

```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> cache;
        int freshOranges = 0;
        const int ROWS = grid.size(), COLS = grid[0].size();

        // Find all rotten oranges and count fresh oranges
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if(grid[r][c] == 2) {
                    cache.push({r, c});
                } else if(grid[r][c] == 1) {
                    freshOranges++;
                }
            }
        }
        // Add level separator
        cache.push({-1, -1});

        int minutesElapsed = -1;
        int dirs[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

        while(!cache.empty()) {
            auto [row, col] = cache.front();
            cache.pop();
            
            if(row == -1) {
                // Level separator encountered
                minutesElapsed++;
                if(!cache.empty()) {
                    // Add separator for next level
                    cache.push({-1, -1});
                }
            } else {
                // Process current rotten orange
                for(auto& d: dirs) {
                    int nr = row + d[0];
                    int nc = col + d[1];
                    if(nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;  // Mark as rotten
                        freshOranges--;
                        cache.push({nr, nc});
                    }
                }
            }
        }
        
        return freshOranges == 0 ? minutesElapsed : -1;
    }
};
```

### How Solution 1 Works

1. **Initialization**: 
   - Find all rotten oranges (value 2) and add them to queue
   - Count all fresh oranges (value 1)
   - Add level separator `{-1, -1}` after initial rotten oranges

2. **BFS Processing**:
   - When encountering `{-1, -1}`, increment minutes and add separator for next level
   - For each rotten orange, check 4 neighbors
   - If neighbor is fresh, mark it as rotten, decrement fresh count, and add to queue

3. **Result**: 
   - If all fresh oranges are rotten (`freshOranges == 0`), return minutes elapsed
   - Otherwise, return -1 (impossible to rot all oranges)

### Key Insight

The `{-1, -1}` marker acts as a level separator:
- All oranges at the same level (same minute) are processed together
- When we encounter the marker, we know we've finished one minute
- This allows us to track time without maintaining a separate distance/time array

## Solution 2: Multi-Source BFS with Level-by-Level Processing

**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n)

This approach processes each level explicitly by tracking queue size.

```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int freshOranges = 0;
        const int ROWS = grid.size(), COLS = grid[0].size();
        int dirs[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

        // Find all rotten oranges and count fresh oranges
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if(grid[r][c] == 2) {
                    q.push({r, c});
                } else if(grid[r][c] == 1) {
                    freshOranges++;
                }
            }
        }

        int minutes = 0;
        while(!q.empty() && freshOranges > 0) {
            int levelSize = q.size();
            for(int i = 0; i < levelSize; i++) {
                auto [row, col] = q.front();
                q.pop();
                
                for(auto& d: dirs) {
                    int nr = row + d[0];
                    int nc = col + d[1];
                    if(nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        freshOranges--;
                        q.push({nr, nc});
                    }
                }
            }
            if(freshOranges > 0) minutes++;
        }
        
        return freshOranges == 0 ? minutes : -1;
    }
};
```

### How Solution 2 Works

1. **Level-by-level processing**: Process all nodes at current level before moving to next
2. **Queue size tracking**: `levelSize = q.size()` captures all nodes at current minute
3. **Increment minutes**: Only increment after processing a level (if fresh oranges remain)

## Solution 3: BFS with Distance Array

**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n)

This approach maintains a separate distance/time array to track when each orange rots.

```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        const int ROWS = grid.size(), COLS = grid[0].size();
        queue<pair<int, int>> q;
        vector<vector<int>> time(ROWS, vector<int>(COLS, -1));
        int freshOranges = 0;
        int dirs[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

        // Initialize: add rotten oranges to queue
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if(grid[r][c] == 2) {
                    q.push({r, c});
                    time[r][c] = 0;
                } else if(grid[r][c] == 1) {
                    freshOranges++;
                }
            }
        }

        int maxTime = 0;
        while(!q.empty()) {
            auto [row, col] = q.front();
            q.pop();
            
            for(auto& d: dirs) {
                int nr = row + d[0];
                int nc = col + d[1];
                if(nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && 
                   grid[nr][nc] == 1 && time[nr][nc] == -1) {
                    time[nr][nc] = time[row][col] + 1;
                    maxTime = max(maxTime, time[nr][nc]);
                    grid[nr][nc] = 2;
                    freshOranges--;
                    q.push({nr, nc});
                }
            }
        }
        
        return freshOranges == 0 ? maxTime : -1;
    }
};
```

### How Solution 3 Works

1. **Distance array**: `time[r][c]` stores when orange at `(r, c)` becomes rotten
2. **Track maximum time**: Keep track of maximum time needed
3. **Visited check**: Use `time[nr][nc] == -1` to check if not yet processed

## Comparison of Approaches

| Aspect | Solution 1 (Marker) | Solution 2 (Level Size) | Solution 3 (Distance) |
|--------|---------------------|------------------------|----------------------|
| **Time Complexity** | O(m×n) | O(m×n) | O(m×n) |
| **Space Complexity** | O(m×n) | O(m×n) | O(m×n) |
| **Extra Space** | None | None | Distance array |
| **Code Clarity** | Good | Excellent | Good |
| **Level Tracking** | Marker-based | Size-based | Distance-based |

## Example Walkthrough

**Input:** `grid = [[2,1,1],[1,1,0],[0,1,1]]`

### Solution 1 (Marker-based):
```
Initial:
  Rotten: (0,0)
  Fresh: 5 oranges
  Queue: [(0,0), (-1,-1)]

Minute 0:
  Process (0,0): Rot (0,1) and (1,0)
  Queue: [(-1,-1), (0,1), (1,0)]
  Fresh: 3

Minute 1:
  Process (0,1): Rot (0,2)
  Process (1,0): Rot (1,1)
  Queue: [(-1,-1), (0,2), (1,1)]
  Fresh: 1

Minute 2:
  Process (0,2): No new rots
  Process (1,1): Rot (2,1)
  Queue: [(-1,-1), (2,1)]
  Fresh: 0

Minute 3:
  Process (2,1): Rot (2,2)
  Queue: [(-1,-1), (2,2)]
  Fresh: 0

Minute 4:
  Process (2,2): No new rots
  Queue: [(-1,-1)]
  Fresh: 0

Result: 4 minutes
```

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Initial scan | O(m×n) | O(1) |
| BFS traversal | O(m×n) | O(m×n) |
| **Overall** | **O(m×n)** | **O(m×n)** |

## Edge Cases

1. **No fresh oranges**: `[[0,2]]` → return 0
2. **Impossible to rot all**: Isolated fresh orange → return -1
3. **All rotten initially**: `[[2,2]]` → return 0
4. **All fresh initially**: No rotten oranges → return -1
5. **Empty grid**: Not possible per constraints

## Common Mistakes

1. **Not counting initial fresh oranges**: Must count before BFS starts
2. **Wrong level tracking**: Forgetting to increment minutes at right time
3. **Boundary checks**: Not checking array bounds before accessing
4. **Visited tracking**: Not marking as rotten immediately (could process same cell twice)
5. **Return value**: Returning minutes when freshOranges > 0 (should return -1)

## Key Insights

1. **Multi-source BFS**: Start from all rotten oranges simultaneously
2. **Level separation**: Need to track time/levels to know when all oranges at current level are processed
3. **Fresh count tracking**: Decrement count when rotting, check if zero at end
4. **Grid modification**: Mark as rotten immediately to avoid reprocessing

## Optimization Tips

1. **Early termination**: Can break early if `freshOranges == 0` during BFS
2. **Space optimization**: Solution 1 uses no extra space beyond queue
3. **Level tracking**: Marker approach is elegant but level-size approach is clearer

## Related Problems

- [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/) - Similar multi-source BFS
- [317. Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/) - Multi-source BFS with distance
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) - Connected components
- [542. 01 Matrix](https://leetcode.com/problems/01-matrix/) - Distance from nearest 0
- [1162. As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) - Multi-source BFS

## Pattern Recognition

This problem demonstrates the **"Multi-Source BFS"** pattern:

```
1. Find all starting points (sources)
2. Add all sources to queue
3. Process level by level
4. Track time/distance from sources
5. Check if all targets are reached
```

Similar problems:
- Walls and Gates
- Shortest Distance from All Buildings
- 01 Matrix
- As Far from Land as Possible

## Real-World Applications

1. **Disease Spread**: Model how disease spreads from multiple sources
2. **Network Broadcasting**: Broadcast message from multiple nodes
3. **Fire Spread**: Simulate fire spreading from multiple ignition points
4. **Virus Propagation**: Model computer virus spreading in network
5. **Information Diffusion**: Track information spread in social networks

{% endraw %}
