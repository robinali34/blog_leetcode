---
layout: post
title: "LeetCode 1197. Minimum Knight Moves"
date: 2026-03-19
categories: [leetcode, medium, bfs]
tags: [leetcode, medium, bfs, chess, shortest-path]
permalink: /2026/03/19/medium-1197-minimum-knight-moves/
---

In an infinite chess board with coordinates from `-infinity` to `+infinity`, a knight starts at `(0, 0)`. Return the **minimum number of moves** to reach `(x, y)`.

A knight moves in an "L" shape: 2 squares in one direction and 1 square perpendicular (8 possible moves).

## Examples

**Example 1:**

```
Input: x = 2, y = 1
Output: 1
Explanation: (0,0) → (2,1)
```

**Example 2:**

```
Input: x = 5, y = 5
Output: 4
Explanation: (0,0) → (2,1) → (4,2) → (3,4) → (5,5)
```

## Constraints

- `-300 <= x, y <= 300`

## Thinking Process

### Why BFS?

We need the **minimum number of moves** from `(0,0)` to `(x,y)` on an unweighted graph where each cell connects to 8 neighbors via knight moves. This is classic BFS shortest path.

### Symmetry Optimization

Knight moves are symmetric across both axes. If `(x, y)` is reachable in $k$ moves, so is `(-x, y)`, `(x, -y)`, and `(-x, -y)`. So we can fold the target into the **first quadrant** with `x = abs(x)`, `y = abs(y)` and only explore that region.

### Why Allow `nx >= -1` and `ny >= -1`?

For small targets like `(1,0)`, the knight must briefly step into negative coordinates to reach them:

```
(0,0) → (1,-2) → (-1,-1) → ... or more typically:
(0,0) → (-1,2) → (1,1) → ... → (1,0)
```

Allowing coordinates down to `-1` (not `-2` or beyond) is sufficient because after folding to the first quadrant, we never need to go further than one step past the origin.

### Algorithm

1. Fold target to first quadrant: `x = abs(x)`, `y = abs(y)`
2. BFS from `(0,0)` with all 8 knight moves
3. Prune: only enqueue positions with `nx >= -1` and `ny >= -1`
4. Track visited states to avoid revisits
5. Return steps when we reach `(x, y)`

## Solution: BFS -- $O(|x| \cdot |y|)$

{% raw %}
```cpp
class Solution {
public:
    int minKnightMoves(int x, int y) {
        x = abs(x);
        y = abs(y);
        vector<pair<int, int>> dirs = {{2, 1}, {1, 2}, {-1, 2}, {-2, 1},
                                        {-2, -1}, {-1, -2}, {1, -2}, {2, -1}};
        queue<pair<int, int>> q;
        q.push({0, 0});
        map<pair<int, int>, int> visited;
        visited[{0, 0}] = 0;

        while (!q.empty()) {
            auto [curX, curY] = q.front();
            q.pop();
            int steps = visited[{curX, curY}];
            if (curX == x && curY == y) return steps;

            for (auto& [dx, dy] : dirs) {
                int nx = curX + dx;
                int ny = curY + dy;
                if (nx >= -1 && ny >= -1 && visited.find({nx, ny}) == visited.end()) {
                    visited[{nx, ny}] = steps + 1;
                    q.push({nx, ny});
                }
            }
        }
        return -1;
    }
};
```
{% endraw %}

**Time**: $O(|x| \cdot |y|)$ -- BFS explores a bounded region around the target
**Space**: $O(|x| \cdot |y|)$ -- visited map

## Key Details

**Why `map<pair<int,int>, int>` instead of a 2D array?**
The board is infinite, so we can't pre-allocate a fixed grid. A map handles arbitrary coordinates. For better performance, an `unordered_map` with a custom hash or an offset-based 2D array (since coordinates are bounded by ~300) would work.

**Why not check goal when generating instead of when dequeuing?**
Either works. Checking at dequeue is simpler since `steps` is already stored in the visited map. Checking at generation would short-circuit one BFS level earlier.

## Common Mistakes

- Not using `abs(x)`, `abs(y)` to exploit symmetry -- BFS explores 4x the area unnecessarily
- Restricting to `nx >= 0, ny >= 0` -- misses paths that need to briefly dip into negative coordinates
- Using an `unordered_set` on `pair` directly (C++ doesn't provide a default hash for `pair`)

## Key Takeaways

- **"Minimum moves on a grid with special movement rules"** = BFS
- **Symmetry pruning** (fold to first quadrant) dramatically reduces the search space
- Allowing `-1` boundary is a subtle but critical detail for correctness near the origin

## Related Problems

- [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/) -- BFS shortest path with transformations
- [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) -- BFS on grid
- [752. Open the Lock](https://leetcode.com/problems/open-the-lock/) -- BFS with state transitions
- [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/) -- multi-source BFS

## Template Reference

- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
