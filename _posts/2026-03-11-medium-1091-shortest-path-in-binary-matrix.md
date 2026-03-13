---
layout: post
title: "LeetCode 1091. Shortest Path in Binary Matrix"
date: 2026-03-11
categories: [leetcode, medium, graph, bfs]
tags: [leetcode, medium, graph, bfs, grid, shortest-path]
permalink: /2026/03/11/medium-1091-shortest-path-in-binary-matrix/
---

Given an `n x n` binary matrix `grid`, return the length of the shortest **clear path** from top-left `(0,0)` to bottom-right `(n-1,n-1)`. A clear path consists of cells with value `0`, and you can move in **8 directions** (including diagonals). The path length is the number of cells visited. Return `-1` if no such path exists.

## Examples

**Example 1:**

```
Input: grid = [[0,1],[1,0]]
Output: 2
Explanation: Path (0,0) → (1,1), length = 2
```

**Example 2:**

```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Explanation: Path (0,0) → (0,1) → (0,2) → (1,2) → (2,2), but
             shorter: (0,0) → (0,1) → (1,2) → (2,2), length = 4
```

**Example 3:**

```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
Explanation: Starting cell is blocked.
```

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`

## Thinking Process

### Why BFS?

This is an unweighted shortest path problem on a grid. BFS explores all cells at distance `d` before any cell at distance `d+1`, guaranteeing the first time we reach the destination is the shortest path.

### 8-Directional Movement

Unlike typical grid BFS (4 directions), this problem allows diagonal movement. This means 8 neighbors per cell.

### Edge Cases

- Start or end cell is `1` (blocked) → return `-1` immediately
- Grid is `1x1` with `grid[0][0] = 0` → return `1`

## Approach: BFS -- $O(n^2)$

{% raw %}
```cpp
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        const int n = grid.size();
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) return -1;

        queue<tuple<int, int, int>> q;
        q.emplace(0, 0, 1);
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        visited[0][0] = true;

        while (!q.empty()) {
            auto [row, col, dist] = q.front();
            q.pop();

            if (row == n - 1 && col == n - 1) return dist;

            for (const auto& [newRow, newCol] : getNeighbors(row, col, grid)) {
                if (visited[newRow][newCol]) continue;
                visited[newRow][newCol] = true;
                q.emplace(newRow, newCol, dist + 1);
            }
        }
        return -1;
    }

private:
    vector<pair<int, int>> dirs = {
        {-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}
    };

    vector<pair<int, int>> getNeighbors(int row, int col,
                                         const vector<vector<int>>& grid) {
        vector<pair<int, int>> neighbours;
        for (auto& [dr, dc] : dirs) {
            int nr = row + dr, nc = col + dc;
            if (nr < 0 || nr >= (int)grid.size() ||
                nc < 0 || nc >= (int)grid[0].size() ||
                grid[nr][nc] != 0)
                continue;
            neighbours.emplace_back(nr, nc);
        }
        return neighbours;
    }
};
```
{% endraw %}

**Time**: $O(n^2)$ -- each cell visited at most once
**Space**: $O(n^2)$ for the visited array and queue

## Common Mistakes

- Forgetting to check both start **and** end cells (either being blocked means no path)
- Using DFS instead of BFS (DFS doesn't guarantee shortest path in unweighted graphs)
- Marking visited **when popping** instead of **when pushing** (causes duplicate entries and TLE)
- Only checking 4 directions instead of 8

## Key Takeaways

- **BFS on grid = shortest path** when all moves have equal cost
- Mark cells as visited **when enqueueing**, not when dequeuing -- this prevents the same cell from being added multiple times
- The path length counts **cells visited** (not edges), so start at distance `1`

## Related Problems

- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) -- BFS/DFS grid traversal
- [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) -- multi-source BFS on grid
- [542. 01 Matrix](https://leetcode.com/problems/01-matrix/) -- BFS from all zeros simultaneously
- [127. Word Ladder](https://leetcode.com/problems/word-ladder/) -- BFS shortest path on implicit graph

## Template Reference

- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
