---
layout: post
title: "[Medium] 286. Walls and Gates"
date: 2025-12-14 00:00:00 -0800
categories: leetcode algorithm medium cpp array matrix bfs problem-solving
---
{% raw %}

You are given an `m x n` grid `rooms` initialized with these three possible values:

- `-1` A wall or an obstacle.
- `0` A gate.
- `INF` Infinity means an empty room. We use the value `2^31 - 1 = 2147483647` to represent `INF` as you may assume that the distance to a gate is less than `2147483647`.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should remain `INF`.

## Examples

**Example 1:**
```
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

**Example 2:**
```
Input: rooms = [[-1]]
Output: [[-1]]
```

**Example 3:**
```
Input: rooms = [[2147483647]]
Output: [[2147483647]]
```

## Constraints

- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 250`
- `rooms[i][j]` is `-1`, `0`, or `2^31 - 1`.

## Thinking Process

1. **Multi-source BFS**: Start from all gates simultaneously for efficiency

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

This solution uses BFS starting from all gates simultaneously. Since BFS guarantees shortest path in unweighted graphs, each empty room will be filled with the distance to its nearest gate.

```cpp
class Solution {
private:
    const int EMPTY = INT_MAX;
    const int GATE = 0;
    const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        const int ROWS = rooms.size(), COLS = rooms[0].size();
        if(ROWS == 0 || COLS == 0) return;    
        
        queue<pair<int, int>> q;
        
        // Add all gates to queue (multi-source BFS)
        for(int row = 0; row < ROWS; row++) {
            for(int col = 0; col < COLS; col++) {
                if(rooms[row][col] == GATE) {
                    q.push({row, col});
                }
            }
        }
        
        // BFS from all gates simultaneously
        while(!q.empty()) {
            auto [row, col] = q.front();
            q.pop();
            
            for(auto& dir: dirs) {
                int nrow = row + dir[0];
                int ncol = col + dir[1];
                
                // Skip if out of bounds, wall, or already visited (not EMPTY)
                if(nrow < 0 || nrow >= ROWS || ncol < 0 || ncol >= COLS || 
                   rooms[nrow][ncol] != EMPTY) {
                    continue;
                }
                
                // Update distance and add to queue
                rooms[nrow][ncol] = rooms[row][col] + 1;
                q.push({nrow, ncol});
            }
        }
    }
};
```

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** 1. **Multi-source BFS**: Start from all gates simultaneously for efficiency

**How the code works:**
1. **Multi-source BFS**: Start from all gates simultaneously for efficiency
- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.

**Walkthrough** — input `rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]`, expected output `[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Operation | Time | Space |
|-----------|------|-------|
| Find all gates | O(m×n) | O(1) |
| BFS traversal | O(m×n) | O(m×n) |
| **Overall** | **O(m×n)** | **O(m×n)** |

### How Solution 1 Works

1. **Initialization**: 
   - Find all gates (value 0) and add them to the queue
   - Gates are the starting points for BFS

2. **Multi-Source BFS**:
   - Process all gates simultaneously
   - For each gate's neighbor:
     - If it's an empty room (`EMPTY`), update its distance
     - Distance = current cell's distance + 1
     - Add to queue for further exploration

3. **Key Insight**:
   - BFS guarantees shortest path in unweighted graphs
   - By starting from all gates, each empty room gets the distance to its **nearest** gate
   - Walls (`-1`) are skipped, empty rooms are updated in-place

### Why Multi-Source BFS?

- **Single-source BFS** would require running BFS from each gate separately → O(k × m × n) where k is number of gates
- **Multi-source BFS** processes all gates together → O(m × n)
- Each cell is visited once, and the first visit (from nearest gate) sets the correct distance
## Example Walkthrough

**Input:** 
```
rooms = [
  [INF, -1,  0,  INF],
  [INF, INF, INF, -1 ],
  [INF, -1,  INF, -1 ],
  [0,   -1,  INF, INF]
]
```

### Solution 1 (Multi-Source BFS):

```
Step 1: Find all gates
  Gates at: (0,2) and (3,0)
  Queue: [(0,2), (3,0)]

Step 2: BFS from gates
  Process (0,2):
    Neighbors: (1,2), (-1,2), (0,1), (0,3)
    Valid: (1,2), (0,3)
    Update: rooms[1][2] = 1, rooms[0][3] = 1
    Queue: [(3,0), (1,2), (0,3)]
  
  Process (3,0):
    Neighbors: (4,0), (2,0), (3,1), (3,-1)
    Valid: (2,0)
    Update: rooms[2][0] = 1
    Queue: [(1,2), (0,3), (2,0)]
  
  Process (1,2):
    Neighbors: (2,2), (0,2), (1,1), (1,3)
    Valid: (2,2), (1,1)
    Update: rooms[2][2] = 2, rooms[1][1] = 2
    Queue: [(0,3), (2,0), (2,2), (1,1)]
  
  Continue until queue is empty...

Final Result:
[
  [3, -1,  0,  1],
  [2,  2,  1, -1],
  [1, -1,  2, -1],
  [0, -1,  3,  4]
]
```

### Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Find all gates | O(m×n) | O(1) |
| BFS traversal | O(m×n) | O(m×n) |
| **Overall** | **O(m×n)** | **O(m×n)** |

## Common Mistakes

1. **No gates**: All rooms remain `INF`
2. **No empty rooms**: Only walls and gates
3. **Single cell**: `[[-1]]` or `[[0]]` or `[[INF]]`
4. **All gates**: Every cell is a gate
5. **Isolated rooms**: Rooms that cannot reach any gate remain `INF`

1. **Single-source BFS**: Running BFS from each gate separately (inefficient)
2. **Not checking bounds**: Forgetting to check array bounds before accessing
3. **Wrong condition**: Using `rooms[nrow][ncol] == EMPTY` instead of `!= EMPTY` for visited check
4. **Distance calculation**: Forgetting to add 1 when updating distance
5. **Modifying input**: Not handling the case where input is empty

## Optimization Tips

1. **Early termination**: Not applicable here (need to fill all rooms)
2. **Space optimization**: Solution 1 uses grid itself, no extra distance array
3. **Direction array**: Using constant array for directions is cleaner than nested loops

## Related Problems

- [994. Rotting Oranges](https://www.leetcode.com/problems/rotting-oranges/) - Similar multi-source BFS
- [317. Shortest Distance from All Buildings](https://www.leetcode.com/problems/shortest-distance-from-all-buildings/) - Multi-source BFS with obstacles
- [542. 01 Matrix](https://www.leetcode.com/problems/01-matrix/) - Distance from nearest 0
- [1162. As Far from Land as Possible](https://www.leetcode.com/problems/as-far-from-land-as-possible/) - Multi-source BFS on grid
- [200. Number of Islands](https://www.leetcode.com/problems/number-of-islands/) - Connected components

## Pattern Recognition

This problem demonstrates the **"Multi-Source BFS"** pattern:

```
1. Identify all starting points (gates)
2. Add all sources to queue
3. Process level by level (BFS)
4. Update distances in-place
5. Skip obstacles (walls)
```

Similar problems:
- Rotting Oranges
- 01 Matrix
- Shortest Distance from All Buildings
- As Far from Land as Possible

## Real-World Applications

1. **Navigation Systems**: Find nearest exit/entrance in a building
2. **Game Development**: Pathfinding from multiple spawn points
3. **Network Routing**: Find nearest gateway/router
4. **Emergency Evacuation**: Find nearest exit in emergency scenarios
5. **Facility Location**: Find optimal locations based on multiple sources

{% endraw %}

## References

- [LC 286: Walls and Gates on LeetCode](https://www.leetcode.com/problems/walls-and-gates/)
- [LeetCode Discuss — LC 286: Walls and Gates](https://www.leetcode.com/problems/walls-and-gates/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/walls-and-gates/editorial/) *(may require premium)*

## Key Takeaways

1. **Multi-source BFS**: Start from all gates simultaneously for efficiency
2. **In-place update**: Use the grid itself to track distances (no extra space needed)
3. **BFS guarantees shortest path**: First visit to a cell gives the shortest distance
4. **Walls are obstacles**: Skip walls (`-1`) during traversal
5. **Empty check**: Only process cells that are `EMPTY` (not yet visited)
