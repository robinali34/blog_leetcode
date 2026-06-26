---
layout: post
title: "[Medium] 3341. Find Minimum Time to Reach Last Room I"
date: 2026-02-10 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dijkstra, grid]
permalink: /2026/02/10/medium-3341-find-minimum-time-to-reach-last-room-i/
tags: [leetcode, medium, graph, shortest-path, dijkstra, grid]
---
There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **minimum** time in seconds **after** which the room opens and can be moved to. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent** room. Moving between adjacent rooms takes **exactly 1 second**.

Return the **minimum** time to reach the room `(n - 1, m - 1)`.

Two rooms are adjacent if they share a common wall (up/down/left/right).

## Examples

**Example 1**

```
Input: moveTime = [[0,4],[4,4]]
Output: 6
Explanation:
- Wait until t=4, move to (1,0) (arrive t=5)
- Move to (1,1) (arrive t=6)
```

**Example 2**

```
Input: moveTime = [[0,0,0],[0,0,0]]
Output: 3
```

**Example 3**

```
Input: moveTime = [[0,1],[1,2]]
Output: 3
```

## Constraints

- `2 <= n == moveTime.length <= 50`
- `2 <= m == moveTime[i].length <= 50`
- `0 <= moveTime[i][j] <= 10^9`

## Key Insight

This is a shortest path problem, but the “edge cost” depends on time because a room may not be enterable yet.

If we are at time `t` in room `(i, j)` and want to move into `(ni, nj)`, then:

\[
\text{nextTime} = \max(t,\ \text{moveTime}[ni][nj]) + 1
\]

That’s “wait until the neighbor is open, then spend 1 second to move”.

Since this transition cost is nonnegative and depends only on the current best time, we can use **Dijkstra** over grid states.

## Thinking Process

There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **minimum** time in seconds **after** which the room opens and can be moved to. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent** room. Moving between adjacent rooms takes **exactly 1 second**.

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
| BFS / DFS traversal | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| **Union-Find (DSU)** *(this problem)* | O(α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |

## Solution

{% raw %}
```cpp
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        const int n = (int)moveTime.size();
        const int m = (int)moveTime[0].size();

        vector<vector<long long>> dist(n, vector<long long>(m, LLONG_MAX));
        dist[0][0] = 0;

        using State = pair<long long, pair<int,int>>; // (time, (i,j))
        priority_queue<State, vector<State>, greater<>> pq;
        pq.emplace(0, make_pair(0, 0));

        const int dirs[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!pq.empty()) {
            auto [t, pos] = pq.top();
            pq.pop();
            auto [i, j] = pos;
            if (t != dist[i][j]) continue;
            if (i == n - 1 && j == m - 1) return (int)t;

            for (auto& d : dirs) {
                int ni = i + d[0], nj = j + d[1];
                if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
                long long nt = max(t, (long long)moveTime[ni][nj]) + 1;
                if (nt < dist[ni][nj]) {
                    dist[ni][nj] = nt;
                    pq.emplace(nt, make_pair(ni, nj));
                }
            }
        }
        return (int)dist[n - 1][m - 1];
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

- [LC 3341: Find Minimum Time to Reach Last Room I on LeetCode](https://www.leetcode.com/problems/find-minimum-time-to-reach-last-room-i/)
- [LeetCode Discuss — LC 3341: Find Minimum Time to Reach Last Room I](https://www.leetcode.com/problems/find-minimum-time-to-reach-last-room-i/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-minimum-time-to-reach-last-room-i/editorial/) *(may require premium)*

## Template Reference

- [Graph Templates: Dijkstra](/posts/2025-10-29-leetcode-templates-graph/#dijkstra)
