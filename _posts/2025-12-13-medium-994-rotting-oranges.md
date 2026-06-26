---
layout: post
title: "[Medium] 994. Rotting Oranges"
date: 2025-12-13 00:00:00 -0800
categories: leetcode algorithm medium cpp array matrix bfs problem-solving
---
{% raw %}

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

## Thinking Process

1. **Multi-source BFS**: Start from all rotten oranges simultaneously

- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Queue BFS** *(this problem)* | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| Level-order BFS | O(n) | O(w) | Process by depth/layer |

## Solution

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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** 1. **Multi-source BFS**: Start from all rotten oranges simultaneously

**How the code works:**
1. **Multi-source BFS**: Start from all rotten oranges simultaneously
- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.

**Walkthrough** — input `grid = [[2,1,1],[1,1,0],[0,1,1]]`, expected output `4`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Operation | Time | Space |
|-----------|------|-------|
| Initial scan | O(m×n) | O(1) |
| BFS traversal | O(m×n) | O(m×n) |
| **Overall** | **O(m×n)** | **O(m×n)** |

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

### Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Initial scan | O(m×n) | O(1) |
| BFS traversal | O(m×n) | O(m×n) |
| **Overall** | **O(m×n)** | **O(m×n)** |

## Common Mistakes

1. **No fresh oranges**: `[[0,2]]` → return 0
2. **Impossible to rot all**: Isolated fresh orange → return -1
3. **All rotten initially**: `[[2,2]]` → return 0
4. **All fresh initially**: No rotten oranges → return -1
5. **Empty grid**: Not possible per constraints

1. **Not counting initial fresh oranges**: Must count before BFS starts
2. **Wrong level tracking**: Forgetting to increment minutes at right time
3. **Boundary checks**: Not checking array bounds before accessing
4. **Visited tracking**: Not marking as rotten immediately (could process same cell twice)
5. **Return value**: Returning minutes when freshOranges > 0 (should return -1)

## Optimization Tips

1. **Early termination**: Can break early if `freshOranges == 0` during BFS
2. **Space optimization**: Solution 1 uses no extra space beyond queue
3. **Level tracking**: Marker approach is elegant but level-size approach is clearer

## Related Problems

- [286. Walls and Gates](https://www.leetcode.com/problems/walls-and-gates/) - Similar multi-source BFS
- [317. Shortest Distance from All Buildings](https://www.leetcode.com/problems/shortest-distance-from-all-buildings/) - Multi-source BFS with distance
- [200. Number of Islands](https://www.leetcode.com/problems/number-of-islands/) - Connected components
- [542. 01 Matrix](https://www.leetcode.com/problems/01-matrix/) - Distance from nearest 0
- [1162. As Far from Land as Possible](https://www.leetcode.com/problems/as-far-from-land-as-possible/) - Multi-source BFS

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

## References

- [LC 994: Rotting Oranges on LeetCode](https://www.leetcode.com/problems/rotting-oranges/)
- [LeetCode Discuss — LC 994: Rotting Oranges](https://www.leetcode.com/problems/rotting-oranges/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/rotting-oranges/editorial/) *(may require premium)*

## Key Takeaways

1. **Multi-source BFS**: Start from all rotten oranges simultaneously
2. **Level separation**: Need to track time/levels to know when all oranges at current level are processed
3. **Fresh count tracking**: Decrement count when rotting, check if zero at end
4. **Grid modification**: Mark as rotten immediately to avoid reprocessing
