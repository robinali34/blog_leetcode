---
layout: post
title: "[Hard] 489. Robot Room Cleaner"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm hard cpp dfs backtracking problem-solving
permalink: /posts/2025-11-24-hard-489-robot-room-cleaner/
tags: [leetcode, hard, dfs, backtracking, robot, simulation]
---
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

```cpp
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is blocked and robot stays in the current cell.
  boolean move();

  // Robot will stay in the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
```

**Note:**

- The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must design the algorithm based only on the 4 given APIs and try it in the room first, then you may visualize the room layout.

## Examples

**Example 1:**
```
Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
```

## Constraints

- `m == room.length`
- `n == room[i].length`
- `1 <= m <= 100`
- `1 <= n <= 200`
- `room[i][j]` is either `0` or `1`.
- `0 <= row < m`
- `0 <= col < n`
- `room[row][col] == 1`
- All the empty cells can be visited from the starting position.

## Thinking Process

1. **Relative Directions**: Use `(d + i) % 4` to explore directions relative to current facing

- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 165" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Tree DFS (bottom-up)</text>

  <line x1="140" y1="42" x2="80" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="140" y1="42" x2="200" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="80" y1="88" x2="50" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="200" y1="88" x2="230" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <circle cx="140" cy="42" r="18" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="140" y="46" text-anchor="middle" font-size="12" fill="#3D3535">3</text>
  <circle cx="80" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="80" y="92" text-anchor="middle" font-size="11" fill="#3D3535">9</text>
  <circle cx="200" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="200" y="92" text-anchor="middle" font-size="11" fill="#3D3535">20</text>
  <circle cx="50" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="50" y="132" text-anchor="middle" font-size="10" fill="#3D3535">15</text>
  <circle cx="230" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="230" y="132" text-anchor="middle" font-size="10" fill="#3D3535">7</text>
  <text x="140" y="155" text-anchor="middle" font-size="11" fill="#6B6560">post-order: combine left + right + 1</text>

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

**Time Complexity:** O(N - O) where N is number of cells and O is number of obstacles  
**Space Complexity:** O(N - O) for visited set and recursion stack

This solution uses DFS backtracking with a visited set to track cleaned cells. The key insight is to always return the robot to its previous position after exploring a path.

### Solution: DFS with Backtracking

```cpp
/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
private:
    vector<vector<int>> dirs = \{\{-1, 0\}, \{0, 1\}, \{1, 0\}, \{0, -1\}\};
    set<pair<int, int>> visited;

    void goBack(Robot& robot) {
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }

    void backtrack(Robot& robot, int x, int y, int d) {
        visited.insert({x, y});
        robot.clean();

        for(int i = 0; i < 4; i++) {
            int new_d = (d + i) % 4;
            int nx = x + dirs[new_d][0];
            int ny = y + dirs[new_d][1];

            if(!visited.count({nx, ny}) && robot.move()) {
                backtrack(robot, nx, ny, new_d);
                goBack(robot);
            }
            robot.turnRight();
        }
    }

public:
    void cleanRoom(Robot& robot) {
        backtrack(robot, 0, 0, 0);
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **Relative Directions**: Use `(d + i) % 4` to explore directions relative to current facing

**How the code works:**
1. **Relative Directions**: Use `(d + i) % 4` to explore directions relative to current facing
- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.

**Walkthrough** — input `room = [`:

All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DFS Backtracking** | O(N-O) | O(N-O) | Simple, intuitive | Requires backtracking logic |
| **Explicit Tracking** | O(N-O) | O(N-O) | Clear direction handling | Same complexity |
## Algorithm Breakdown

### Direction Management

```cpp
vector<vector<int>> dirs = \{\{-1, 0\}, \{0, 1\}, \{1, 0\}, \{0, -1\}\};
// Index: 0=up, 1=right, 2=down, 3=left

int new_d = (d + i) % 4;  // Relative direction
int nx = x + dirs[new_d][0];
int ny = y + dirs[new_d][1];
```

**Why relative directions?**
- Robot maintains its facing direction
- `(d + i) % 4` rotates relative to current facing
- `i=0`: same direction, `i=1`: right turn, `i=2`: 180°, `i=3`: left turn

### Backtracking Function

```cpp
void backtrack(Robot& robot, int x, int y, int d) {
    // Mark current cell as visited and clean
    visited.insert({x, y});
    robot.clean();

    // Try all 4 directions
    for(int i = 0; i < 4; i++) {
        int new_d = (d + i) % 4;
        int nx = x + dirs[new_d][0];
        int ny = y + dirs[new_d][1];

        // If not visited and can move
        if(!visited.count({nx, ny}) && robot.move()) {
            // Explore recursively
            backtrack(robot, nx, ny, new_d);
            // Return to current position
            goBack(robot);
        }
        // Turn right to try next direction
        robot.turnRight();
    }
}
```

### goBack Function

```cpp
void goBack(Robot& robot) {
    robot.turnRight();  // Turn 90° right
    robot.turnRight();  // Turn 90° right (total 180°)
    robot.move();       // Move back to previous cell
    robot.turnRight();  // Turn 90° right
    robot.turnRight();  // Turn 90° right (total 180°, restore original facing)
}
```

**Why this works:**
- After `backtrack` returns, robot is facing away from previous cell
- Turn 180° to face previous cell
- Move back
- Turn 180° to restore original facing direction

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DFS Backtracking** | O(N-O) | O(N-O) | Simple, intuitive | Requires backtracking logic |
| **Explicit Tracking** | O(N-O) | O(N-O) | Clear direction handling | Same complexity |

## Implementation Details

### Direction Array

```cpp
vector<vector<int>> dirs = \{\{-1, 0\}, \{0, 1\}, \{1, 0\}, \{0, -1\}\};
//                    Index:   0        1       2        3
//                  Meaning:  up     right   down     left
```

**Why this order?**
- Matches clockwise rotation: up → right → down → left
- `turnRight()` increments direction index
- `(d + i) % 4` rotates relative to current facing

### Visited Set

```cpp
set<pair<int, int>> visited;
```

**Why use set?**
- O(log n) lookup and insertion
- Prevents revisiting cleaned cells
- Tracks all cleaned positions

### Relative Direction Calculation

```cpp
int new_d = (d + i) % 4;
```

**How it works:**
- `d`: Current facing direction (0=up, 1=right, 2=down, 3=left)
- `i`: Offset (0=same, 1=right turn, 2=180°, 3=left turn)
- `(d + i) % 4`: New direction after turning right `i` times

## Common Mistakes

1. **Single cell room**: Only one accessible cell → clean and return
2. **All directions blocked**: Clean current cell, no recursion
3. **Dead ends**: Backtrack correctly handles dead ends
4. **Circular paths**: Visited set prevents infinite loops
5. **Large room**: DFS handles any size room efficiently

1. **Forgetting goBack**: Not returning robot to previous position
2. **Wrong direction calculation**: Not using relative directions
3. **Not tracking visited**: Infinite recursion or revisiting cells
4. **Wrong turn sequence**: Incorrect goBack implementation
5. **Not cleaning current cell**: Forgetting to call `robot.clean()`

## Optimization Tips

1. **Use unordered_set**: Can use `unordered_set<pair<int,int>>` with hash for O(1) lookup
2. **Direction optimization**: Pre-compute direction offsets
3. **Early termination**: Can optimize if we know room size (not applicable here)

## Related Problems

- [200. Number of Islands](https://www.leetcode.com/problems/number-of-islands/) - Similar DFS pattern
- [695. Max Area of Island](https://www.leetcode.com/problems/max-area-of-island/) - DFS exploration
- [130. Surrounded Regions](https://www.leetcode.com/problems/surrounded-regions/) - DFS with boundaries
- [79. Word Search](https://www.leetcode.com/problems/word-search/) - DFS backtracking

## Real-World Applications

1. **Vacuum Robots**: Roomba-like cleaning robots
2. **Exploration Robots**: Mars rovers, underwater robots
3. **Game AI**: Pathfinding in games
4. **Maze Solving**: Robot navigation algorithms
5. **Search and Rescue**: Autonomous exploration

## Pattern Recognition

This problem demonstrates the **"DFS Backtracking with State Restoration"** pattern:

```
1. Mark current state (visited, clean)
2. Explore all possible next states
3. Recursively process each valid next state
4. Restore previous state (goBack)
5. Continue with next option
```

Similar problems:
- Word Search
- N-Queens
- Sudoku Solver
- Robot navigation problems

## Why Backtracking is Necessary

1. **Robot State**: Robot maintains position and facing direction
2. **API Constraints**: Can only move forward, must turn to change direction
3. **Exploration Order**: Need to try all directions from each cell
4. **State Restoration**: Must return robot to previous position after exploring

## goBack Function Explanation

```cpp
void goBack(Robot& robot) {
    robot.turnRight();  // 1st turn: 90° right
    robot.turnRight();  // 2nd turn: 90° right (total 180°)
    robot.move();       // Move back to previous cell
    robot.turnRight();  // 3rd turn: 90° right
    robot.turnRight();  // 4th turn: 90° right (total 180°, restore facing)
}
```

**Step-by-step:**
1. After recursive call returns, robot faces away from previous cell
2. Turn 180° to face previous cell
3. Move back to previous cell
4. Turn 180° to restore original facing direction

## Direction Index Mapping

```
Direction Index → Movement Offset
0 (up)    → (-1, 0)
1 (right) → (0, 1)
2 (down)  → (1, 0)
3 (left)  → (0, -1)

Turning right increments index: (d + 1) % 4
Turning left decrements index: (d + 3) % 4
```

## Coordinate System

- **Origin (0,0)**: Starting position of robot
- **Relative coordinates**: All positions relative to start
- **No absolute grid**: We don't know room boundaries
- **Visited tracking**: Only way to know what's been explored

---

*This problem is an excellent example of DFS backtracking with state management, demonstrating how to handle robot navigation and exploration algorithms.*

## Key Takeaways

1. **Relative Directions**: Use `(d + i) % 4` to explore directions relative to current facing
2. **Visited Set**: Track cleaned cells to avoid revisiting
3. **Backtracking**: Always return robot to previous position after exploring
4. **goBack Function**: Turn 180°, move, turn 180° to return to previous cell
5. **Direction Array**: `dirs = \{\{-1,0\}, \{0,1\}, \{1,0\}, \{0,-1\}\}` represents [up, right, down, left]

## References

- [LC 489: Robot Room Cleaner on LeetCode](https://www.leetcode.com/problems/robot-room-cleaner/)
- [LeetCode Discuss — LC 489: Robot Room Cleaner](https://www.leetcode.com/problems/robot-room-cleaner/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/robot-room-cleaner/editorial/) *(may require premium)*

## Template Reference

- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
