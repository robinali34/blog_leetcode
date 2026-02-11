---
layout: post
title: "3341. Find Minimum Time to Reach Last Room I"
date: 2026-02-10 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dijkstra, grid]
permalink: /2026/02/10/medium-3341-find-minimum-time-to-reach-last-room-i/
tags: [leetcode, medium, graph, shortest-path, dijkstra, grid]
---

## Problem Statement

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

## Solution (Dijkstra on Grid)

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
{% endraw %}

## Complexity

- **Time**: \(O(nm \log(nm))\)
- **Space**: \(O(nm)\)

## Template Reference

- [Graph Templates: Dijkstra](/posts/2025-10-29-leetcode-templates-graph/#dijkstra)
