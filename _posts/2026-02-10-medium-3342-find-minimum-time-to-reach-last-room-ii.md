---
layout: post
title: "[Medium] 3342. Find Minimum Time to Reach Last Room II"
date: 2026-02-10 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dijkstra, grid]
permalink: /2026/02/10/medium-3342-find-minimum-time-to-reach-last-room-ii/
tags: [leetcode, medium, graph, shortest-path, dijkstra, grid]
---
There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **minimum** time in seconds **after** which the room opens and can be moved to. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent** room.

**Moving between adjacent rooms takes:**
*   **1 second** for the first move.
*   **2 seconds** for the second move.
*   **1 second** for the third move.
*   **2 seconds** for the fourth move.
*   ...and so on, alternating between 1 and 2 seconds.

Return the **minimum** time to reach the room `(n - 1, m - 1)`.

Two rooms are adjacent if they share a common wall (up/down/left/right).

## Examples

**Example 1**

```
Input: moveTime = [[0,4],[4,4]]
Output: 7
Explanation:
- At t=0, move to (1,0) (cost 1). Arrive at t=4 (wait for 4). Next move cost will be 2.
- At t=4, wait until t=4. Move to (1,0). Wait? No, arrive t=1 (cost) + max(0, 4) = 5?
  Let's trace carefully:
  - Start (0,0) at t=0.
  - Move to (0,1): moveTime[0][1]=4. Arrive at max(0, 4) + 1 = 5. Next cost 2.
  - Move to (1,1) from (0,1): moveTime[1][1]=4. Arrive max(5, 4) + 2 = 7.
  Alternatively:
  - Start (0,0) at t=0.
  - Move to (1,0): moveTime[1][0]=4. Arrive max(0, 4) + 1 = 5. Next cost 2.
  - Move to (1,1) from (1,0): moveTime[1][1]=4. Arrive max(5, 4) + 2 = 7.
```

**Example 2**

```
Input: moveTime = [[0,0,0,0],[0,0,0,0]]
Output: 6
Explanation:
- (0,0) -> (0,1): cost 1. Arrive t=1.
- (0,1) -> (0,2): cost 2. Arrive t=3.
- (0,2) -> (0,3): cost 1. Arrive t=4.
- (0,3) -> (1,3): cost 2. Arrive t=6.
```

**Example 3**

```
Input: moveTime = [[0,1],[1,2]]
Output: 4
```

## Constraints

- `2 <= n == moveTime.length <= 750`
- `2 <= m == moveTime[i].length <= 750`
- `0 <= moveTime[i][j] <= 10^9`

## Key Insight

This is a **shortest path problem** on a grid where the edge weights are dynamic but depend only on the *sequence* of moves (1, 2, 1, 2...).

Specifically, the cost of the $k$-th move is:
- $1$ if $k$ is odd (1st, 3rd, ...)
- $2$ if $k$ is even (2nd, 4th, ...)

This creates a state `(row, col, next_move_cost)`. Since the cost alternates between 1 and 2, `next_move_cost` is always either 1 or 2.

We can use **Dijkstra's Algorithm**. The state in the priority queue will be `{time, row, col, weight}`.
- `weight` is the cost to move *out* of the current cell to a neighbor.
- When moving from `(r, c)` to `(nr, nc)` with weight `w`:
  - `arrival_time = max(current_time, moveTime[nr][nc]) + w`
  - The next weight for `(nr, nc)` will be `3 - w` (swaps 1 $\to$ 2 and 2 $\to$ 1).

## Thinking Process

There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **minimum** time in seconds **after** which the room opens and can be moved to. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent** room.

- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.



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
| BFS / DFS traversal | $O(V+E)$ | $O(V)$ | Connectivity, flood fill |
| Dijkstra | $O((V+E)\log V)$ | $O(V)$ | Non-negative edge weights |
| **Union-Find (DSU)** *(this problem)* | $O(\alpha(n))$ | $O(n)$ | Dynamic connectivity |
| Topological sort | $O(V+E)$ | $O(V)$ | DAG ordering, cycle detection |

## Solution

{% raw %}
```cpp
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        const int n = (int)moveTime.size();
        const int m = (int)moveTime[0].size();

        // dist[i][j] stores the minimum time to reach (i, j).
        // Note: strictly speaking, we might arrive at (i, j) with 'next_cost=1' or 'next_cost=2'.
        // However, arriving earlier is always better regardless of the next move cost
        // because the wait time `max(t, moveTime)` dominates small differences in edge weights.
        // A simple 2D dist array is sufficient for this problem's constraints.
        vector<vector<long long>> dist(n, vector<long long>(m, LLONG_MAX));
        dist[0][0] = 0;

        // State: {time, r, c, next_move_cost}
        // next_move_cost is the cost to travel to the *next* neighbor.
        struct State {
            long long time;
            int r, c, w;
            bool operator>(const State& other) const { return time > other.time; }
        };
        
        priority_queue<State, vector<State>, greater<>> pq;
        pq.push({0, 0, 0, 1}); // Start at (0,0), time 0, next move costs 1

        const int dirs[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

        while (!pq.empty()) {
            auto [t, r, c, w] = pq.top();
            pq.pop();

            if (t > dist[r][c]) continue;
            if (r == n - 1 && c == m - 1) return (int)t;

            for (auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;

                // Calculate arrival time at neighbor
                // Must wait until moveTime[nr][nc], then add travel cost 'w'
                long long nt = max(t, (long long)moveTime[nr][nc]) + w;

                if (nt < dist[nr][nc]) {
                    dist[nr][nc] = nt;
                    pq.push({nt, nr, nc, 3 - w}); // Flip weight: 1->2, 2->1
                }
            }
        }
        return -1; // Should not reach here
    }
};
```

### Solution Explanation

**Approach:** Union-Find (DSU) (this problem)

**Key idea:** There is a dungeon with `n x m` rooms arranged as a grid.

**How the code works:**
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.
## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

- **Pattern:** Union-Find (DSU) (this problem)
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.

## References

- [LC 3342: Find Minimum Time to Reach Last Room II on LeetCode](https://www.leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/)
- [LeetCode Discuss — LC 3342: Find Minimum Time to Reach Last Room II](https://www.leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/editorial/) *(may require premium)*

## Template Reference

- [Graph Templates: Dijkstra](/posts/2025-10-29-leetcode-templates-graph/#dijkstra)
