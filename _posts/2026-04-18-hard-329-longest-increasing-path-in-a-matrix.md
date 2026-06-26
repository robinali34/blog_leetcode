---
layout: post
title: "[Hard] 329. Longest Increasing Path in a Matrix"
date: 2026-04-18
categories: [leetcode, hard, dynamic-programming, dfs]
tags: [leetcode, hard, dfs, memoization, topological-sort, bfs, matrix]
permalink: /2026/04/18/hard-329-longest-increasing-path-in-a-matrix/
---
Given an `m x n` integers matrix, return the length of the **longest strictly increasing path**.

From each cell, you can move in four directions: up, down, left, or right. You may not move diagonally or outside the boundary.

## Examples

**Example 1:**

```
Input:
  9  9  4
  6  6  8
  2  1  1

Output: 4

One longest path: 1 → 2 → 6 → 9
```

**Example 2:**

```
Input:
  3  4  5
  3  2  6
  2  2  1

Output: 4

One longest path: 3 → 4 → 5 → 6
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`

## Thinking Process

### Why Brute Force Fails

Starting DFS from every cell without caching repeats enormous amounts of work. A cell deep in the matrix gets re-explored from every path that leads to it.

### DFS + Memoization

Define `dp[i][j]` = length of the longest increasing path **starting from** `(i, j)`.

From `(i, j)`, try all 4 neighbors `(nr, nc)` where `matrix[nr][nc] > matrix[i][j]`:

```
dp[i][j] = 1 + max(dp[nr][nc]) for all valid strictly-greater neighbors
```

If no neighbor is strictly greater, `dp[i][j] = 1`.

Since values are **strictly increasing**, there are no cycles. Each cell is computed exactly once, then cached.

### Alternative: Topological Sort (BFS)

Think of the grid as a **DAG**: draw an edge `u → v` whenever `matrix[v] > matrix[u]`. Then the longest increasing path = longest path in this DAG, which we can find via topological sort (Kahn's algorithm):

1. Compute **indegree** of each cell (number of strictly-smaller neighbors)
2. Start BFS from all cells with indegree 0 (local minima)
3. Process layer by layer; each layer = one step in the path
4. Number of BFS layers = answer



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Grid traversal</text>

  <rect x="50" y="40" width="28" height="28" fill="#D4D8E0" stroke="#8B8680"/><rect x="78" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="106" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="50" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="78" y="68" width="28" height="28" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="106" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="110" y="115" text-anchor="middle" font-size="11" fill="#6B6560">BFS/DFS flood from each cell</text>

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

{% raw %}
```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty()) return 0;
        int rows = matrix.size();
        int cols = matrix[0].size();
        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        int result = 0;

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                result = max(result, dfs(matrix, dp, i, j));
            }
        }
        return result;
    }

private:
    int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    int dfs(vector<vector<int>>& matrix, vector<vector<int>>& dp, int r, int c) {
        if (dp[r][c] != 0) return dp[r][c];
        int rows = matrix.size();
        int cols = matrix[0].size();
        int maxLen = 1;

        for (auto& d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                matrix[nr][nc] > matrix[r][c]) {
                maxLen = max(maxLen, 1 + dfs(matrix, dp, nr, nc));
            }
        }
        dp[r][c] = maxLen;
        return maxLen;
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** ### Why Brute Force Fails

**How the code works:**
1. Compute **indegree** of each cell (number of strictly-smaller neighbors)
2. Start BFS from all cells with indegree 0 (local minima)
3. Process layer by layer; each layer = one step in the path
4. Number of BFS layers = answer

**Walkthrough** — input `9  9  4`, expected output `4`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Comparison

| Aspect | DFS + Memoization | Topological Sort (BFS) |
|---|---|---|
| Approach | Top-down recursion with cache | Bottom-up layer-by-layer |
| Recursion | Yes (stack depth up to mn) | No (iterative) |
| Space | O(mn) dp + recursion stack | O(mn) indegree + queue |
| When to prefer | Simpler to write, natural for path problems | Avoids stack overflow on large inputs |
| Key insight | Strictly increasing = no cycles = safe to memo | Grid as DAG, longest path via topo sort |

## Common Mistakes

- **Forgetting the strictly-greater check:** Using `>=` instead of `>` creates cycles and infinite recursion
- **Using a visited array:** Unnecessary here and would actually prevent correct memoization (a cell should be reachable from multiple starting points)
- **Returning 0 for base case:** A single cell is a path of length **1**, not 0

## Key Takeaways

- **DFS + memoization on grid** is a core pattern: define `dp[i][j]` as the answer starting from `(i, j)`, recurse on valid neighbors, cache results
- **Strictly increasing** guarantees a DAG -- no cycles means memoization is safe and topological sort applies
- The BFS approach reveals the problem's structure: it's just **longest path in a DAG** disguised as a grid problem
- Both solutions are O(mn) -- choose based on whether you prefer recursive or iterative style

## Related Problems

- [200. Number of Islands](https://www.leetcode.com/problems/number-of-islands/) -- grid DFS without memoization
- [417. Pacific Atlantic Water Flow](https://www.leetcode.com/problems/pacific-atlantic-water-flow/) -- grid DFS with multi-source
- [1091. Shortest Path in Binary Matrix](https://www.leetcode.com/problems/shortest-path-in-binary-matrix/) -- grid BFS
- [221. Maximal Square](https://www.leetcode.com/problems/maximal-square/) -- grid DP with neighbor transitions
- [207. Course Schedule](https://www.leetcode.com/problems/course-schedule/) -- topological sort on explicit DAG

## References

- [LC 329: Longest Increasing Path in a Matrix on LeetCode](https://www.leetcode.com/problems/longest-increasing-path-in-a-matrix/)
- [LeetCode Discuss — LC 329: Longest Increasing Path in a Matrix](https://www.leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/longest-increasing-path-in-a-matrix/editorial/) *(may require premium)*

## Template Reference

- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
