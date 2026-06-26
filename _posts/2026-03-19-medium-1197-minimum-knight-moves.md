---
layout: post
title: "[Medium] 1197. Minimum Knight Moves"
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

Knight moves are symmetric across both axes. If `(x, y)` is reachable in k moves, so is `(-x, y)`, `(x, -y)`, and `(-x, -y)`. So we can fold the target into the **first quadrant** with `x = abs(x)`, `y = abs(y)` and only explore that region.

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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** ### Why BFS?

**How the code works:**
1. Fold target to first quadrant: `x = abs(x)`, `y = abs(y)`
2. BFS from `(0,0)` with all 8 knight moves
3. Prune: only enqueue positions with `nx >= -1` and `ny >= -1`
4. Track visited states to avoid revisits
5. Return steps when we reach `(x, y)`

**Walkthrough** — input `x = 2, y = 1`, expected output `1`:

(0,0) → (2,1)
## Common Mistakes

- Not using `abs(x)`, `abs(y)` to exploit symmetry -- BFS explores 4x the area unnecessarily
- Restricting to `nx >= 0, ny >= 0` -- misses paths that need to briefly dip into negative coordinates
- Using an `unordered_set` on `pair` directly (C++ doesn't provide a default hash for `pair`)

## Key Takeaways

- **"Minimum moves on a grid with special movement rules"** = BFS
- **Symmetry pruning** (fold to first quadrant) dramatically reduces the search space
- Allowing `-1` boundary is a subtle but critical detail for correctness near the origin

## Related Problems

- [433. Minimum Genetic Mutation](https://www.leetcode.com/problems/minimum-genetic-mutation/) -- BFS shortest path with transformations
- [1091. Shortest Path in Binary Matrix](https://www.leetcode.com/problems/shortest-path-in-binary-matrix/) -- BFS on grid
- [752. Open the Lock](https://www.leetcode.com/problems/open-the-lock/) -- BFS with state transitions
- [286. Walls and Gates](https://www.leetcode.com/problems/walls-and-gates/) -- multi-source BFS

## References

- [LC 1197: Minimum Knight Moves on LeetCode](https://www.leetcode.com/problems/minimum-knight-moves/)
- [LeetCode Discuss — LC 1197: Minimum Knight Moves](https://www.leetcode.com/problems/minimum-knight-moves/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-knight-moves/editorial/) *(may require premium)*

## Template Reference

- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
