---
layout: post
title: "[Medium] 286. Walls and Gates"
date: 2025-12-14 00:00:00 -0800
categories: leetcode algorithm medium cpp array matrix bfs problem-solving
---

{% raw %}
# [Medium] 286. Walls and Gates

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

## Solution 1: Multi-Source BFS (Recommended)

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

## Solution 2: DFS (Alternative - Less Efficient)

**Time Complexity:** O((m × n)^2) in worst case  
**Space Complexity:** O(m × n) - Recursion stack

DFS approach starting from each gate. Less efficient because it may revisit cells multiple times.

```cpp
class Solution {
private:
    const int EMPTY = INT_MAX;
    const int GATE = 0;
    const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    void dfs(vector<vector<int>>& rooms, int row, int col, int distance) {
        if(row < 0 || row >= rooms.size() || col < 0 || col >= rooms[0].size() ||
           rooms[row][col] < distance) {
            return;
        }
        
        rooms[row][col] = distance;
        
        for(auto& dir: dirs) {
            dfs(rooms, row + dir[0], col + dir[1], distance + 1);
        }
    }
    
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        const int ROWS = rooms.size(), COLS = rooms[0].size();
        if(ROWS == 0 || COLS == 0) return;
        
        // Start DFS from each gate
        for(int row = 0; row < ROWS; row++) {
            for(int col = 0; col < COLS; col++) {
                if(rooms[row][col] == GATE) {
                    dfs(rooms, row, col, 0);
                }
            }
        }
    }
};
```

### How Solution 2 Works

1. **DFS from each gate**: Start DFS from every gate with distance 0
2. **Pruning**: If current distance >= existing distance in cell, skip (already found shorter path)
3. **Update**: Set cell to current distance and continue DFS

### Why BFS is Better

- **BFS**: Guarantees shortest path, each cell visited once
- **DFS**: May revisit cells, requires pruning check, less efficient

## Comparison of Approaches

| Aspect | Multi-Source BFS | DFS |
|--------|------------------|-----|
| **Time Complexity** | O(m×n) | O((m×n)²) worst case |
| **Space Complexity** | O(m×n) | O(m×n) |
| **Optimality** | Guaranteed shortest path | Requires pruning |
| **Code Simplicity** | Excellent | Good |
| **Efficiency** | Better | Less efficient |

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

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Find all gates | O(m×n) | O(1) |
| BFS traversal | O(m×n) | O(m×n) |
| **Overall** | **O(m×n)** | **O(m×n)** |

## Edge Cases

1. **No gates**: All rooms remain `INF`
2. **No empty rooms**: Only walls and gates
3. **Single cell**: `[[-1]]` or `[[0]]` or `[[INF]]`
4. **All gates**: Every cell is a gate
5. **Isolated rooms**: Rooms that cannot reach any gate remain `INF`

## Common Mistakes

1. **Single-source BFS**: Running BFS from each gate separately (inefficient)
2. **Not checking bounds**: Forgetting to check array bounds before accessing
3. **Wrong condition**: Using `rooms[nrow][ncol] == EMPTY` instead of `!= EMPTY` for visited check
4. **Distance calculation**: Forgetting to add 1 when updating distance
5. **Modifying input**: Not handling the case where input is empty

## Key Insights

1. **Multi-source BFS**: Start from all gates simultaneously for efficiency
2. **In-place update**: Use the grid itself to track distances (no extra space needed)
3. **BFS guarantees shortest path**: First visit to a cell gives the shortest distance
4. **Walls are obstacles**: Skip walls (`-1`) during traversal
5. **Empty check**: Only process cells that are `EMPTY` (not yet visited)

## Optimization Tips

1. **Early termination**: Not applicable here (need to fill all rooms)
2. **Space optimization**: Solution 1 uses grid itself, no extra distance array
3. **Direction array**: Using constant array for directions is cleaner than nested loops

## Related Problems

- [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) - Similar multi-source BFS
- [317. Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/) - Multi-source BFS with obstacles
- [542. 01 Matrix](https://leetcode.com/problems/01-matrix/) - Distance from nearest 0
- [1162. As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) - Multi-source BFS on grid
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) - Connected components

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

