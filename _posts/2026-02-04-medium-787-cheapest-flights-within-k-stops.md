---
layout: post
title: "[Medium] 787. Cheapest Flights Within K Stops"
date: 2026-02-04 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dynamic-programming, bellman-ford]
permalink: /2026/02/04/medium-787-cheapest-flights-within-k-stops/
tags: [leetcode, medium, graph, shortest-path, dynamic-programming, bellman-ford]
---
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight from city `fromi` to city `toi` with cost `pricei`.

You are also given three integers `src`, `dst`, and `k`, return **the cheapest price** from `src` to `dst` with **at most** `k` stops. If there is no such route, return `-1`.

## Examples

**Example 1:**

```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```

**Example 2:**

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
```

**Example 3:**

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 has cost 500.
```

## Constraints

- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= fromi, toi < n`
- `fromi != toi`
- `1 <= pricei <= 104`
- There will not be any multiple flights between two cities.
- `0 <= src, dst < n`
- `src != dst`
- `0 <= k < n`

## Thinking Process

1. **Stop Constraint**: k stops means at most k+1 edges (k intermediate cities + destination)

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

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
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

## Solution

```cpp
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto& e: flights) adj[e[0]].push_back({e[1], e[2]});
        vector<long long> prices(n, LONG_LONG_MAX);
        queue<pair<int, int>> q;
        q.push({src, 0});
        int stop = 0;
        while(stop <= k && !q.empty()) {
            int sz = q.size();
            while(sz--) {
                auto [node, price] = q.front();
                q.pop();
                for(auto [neighbor, currPrice]: adj[node]) {
                    long long newPrice = price + currPrice;
                    if(newPrice >= prices[neighbor]) continue;
                    prices[neighbor] = newPrice;
                    q.push({neighbor, newPrice});
                }
            }
            stop++;
        }
        return prices[dst] == LONG_LONG_MAX? -1: prices[dst];
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **Stop Constraint**: k stops means at most k+1 edges (k intermediate cities + destination)

**How the code works:**
1. **Stop Constraint**: k stops means at most k+1 edges (k intermediate cities + destination)
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1`, expected output `700`:

The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

### Algorithm Breakdown:

1. **Build Adjacency List**: Create graph representation
2. **Initialize**: Set `prices[src] = 0`, push `(src, 0)` to queue
3. **BFS Level-by-Level**: For each stop level (0 to k):
   - Process all nodes at current level
   - For each node, explore neighbors and update prices if cheaper
   - Only add to queue if price improved (pruning)
4. **Result**: Return `prices[dst]` or -1 if unreachable

### Why This Works:

- **Level-by-Level Processing**: Ensures we process all nodes reachable in exactly `stop` stops before moving to `stop+1`
- **Price Update**: Only update if `newPrice < prices[neighbor]`, ensuring we find the cheapest path
- **Stop Limit**: The outer loop `while(stop <= k)` ensures we don't exceed k stops

### Solution 1 (BFS Level-by-Level):
- **Time Complexity**: O(n * m * k) - Process each edge up to k+1 times
- **Space Complexity**: O(n + m) - Adjacency list and queue

### Solution 2 (Bellman-Ford):
- **Time Complexity**: O(k * m) - k+1 iterations, each processing all m edges
- **Space Complexity**: O(n) - Distance arrays

### Solution 3 (Dijkstra with Stops):
- **Time Complexity**: O(m * log(m)) - Each edge may be processed multiple times
- **Space Complexity**: O(n + m) - Adjacency list and priority queue
## Related Problems

- [743. Network Delay Time](https://www.leetcode.com/problems/network-delay-time/) - Shortest path without stop constraint
- [1514. Path with Maximum Probability](https://www.leetcode.com/problems/path-with-maximum-probability/) - Maximum probability path
- [1631. Path With Minimum Effort](https://www.leetcode.com/problems/path-with-minimum-effort/) - Minimum effort path
- [1928. Minimum Cost to Reach Destination in Time](https://www.leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) - Shortest path with time constraint

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Stop Constraint**: k stops means at most k+1 edges (k intermediate cities + destination)
2. **Bellman-Ford Advantage**: Naturally handles edge count constraints - perfect for this problem
3. **BFS Level-by-Level**: Ensures we process nodes in order of number of stops
4. **Dijkstra with Stops**: Track both distance and stops, skip paths that exceed limit or use more stops
5. **Temporary Array**: In Bellman-Ford, using `tmp` prevents using updated distances in the same iteration

## References

- [LC 787: Cheapest Flights Within K Stops on LeetCode](https://www.leetcode.com/problems/cheapest-flights-within-k-stops/)
- [LeetCode Discuss — LC 787: Cheapest Flights Within K Stops](https://www.leetcode.com/problems/cheapest-flights-within-k-stops/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/cheapest-flights-within-k-stops/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
