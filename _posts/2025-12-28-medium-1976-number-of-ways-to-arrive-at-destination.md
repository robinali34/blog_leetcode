---
layout: post
title: "[Medium] 1976. Number of Ways to Arrive at Destination"
date: 2025-12-28 14:30:00 -0700
categories: [leetcode, medium, dijkstra, shortest-path, graph, dynamic-programming]
permalink: /2025/12/28/medium-1976-number-of-ways-to-arrive-at-destination/
---
You are in a city that consists of `n` intersections numbered from `0` to `n - 1` with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is **at most one** road between any two intersections.

You are given an integer `n` and an array `roads` where `roads[i] = [ui, vi, timei]` means that there is a road between intersections `ui` and `vi` that takes `timei` minutes to travel. You want to know how many ways you can travel from intersection `0` to intersection `n - 1` in the **shortest amount of time**.

Return *the **number of ways** you can arrive at your destination in the **shortest amount of time***. Since the answer may be large, return it **modulo** `10^9 + 7`.

## Thinking Process

You are in a city that consists of `n` intersections numbered from `0` to `n - 1` with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is **at most one** road between any two intersections.

You are given an integer `n` and an array `roads` where `roads[i] = [ui, vi, timei]` means that there is a road between intersections `ui` and `vi` that takes `timei` minutes to travel. You want to know how many ways you can travel from intersection `0` to intersection `n - 1` in the **shortest amount of time**.

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

## Examples

**Example 1:**
```
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➜ 1 ➜ 2 ➜ 5 ➜ 6
- 0 ➜ 1 ➜ 3 ➜ 5 ➜ 6
- 0 ➜ 4 ➜ 6
- 0 ➜ 6
```

**Example 2:**
```
Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
```

## Constraints

- `1 <= n <= 200`
- `n - 1 <= roads.length <= n * (n - 1) / 2`
- `roads[i].length == 3`
- `0 <= ui, vi <= n - 1`
- `1 <= timei <= 10^9`
- `ui != vi`
- There is at most one road connecting any two intersections.
- You can reach any intersection from any other intersection.

## Dijkstra's Template

Here's the general template for Dijkstra's algorithm with path counting:

```cpp
int countShortestPaths(int n, vector<vector<pair<int, int>>>& adjList, int start, int end) {
    const int MOD = 1e9 + 7;
    const long long INF = LLONG_MAX;
    
    // Distance and path count arrays
    vector<long long> dist(n, INF);
    vector<int> pathCount(n, 0);
    
    // Priority queue: (distance, node)
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    
    // Initialize start node
    dist[start] = 0;
    pathCount[start] = 1;
    pq.emplace(0, start);
    
    while (!pq.empty()) {
        auto [currDist, currNode] = pq.top();
        pq.pop();
        
        // Skip if outdated (already found shorter path)
        if (currDist > dist[currNode]) continue;
        
        // Explore neighbors
        for (auto& [neighbor, weight] : adjList[currNode]) {
            long long newDist = currDist + weight;
            
            // Found shorter path: update distance and reset count
            if (newDist < dist[neighbor]) {
                dist[neighbor] = newDist;
                pathCount[neighbor] = pathCount[currNode];
                pq.emplace(newDist, neighbor);
            }
            // Found equal path: add to count
            else if (newDist == dist[neighbor]) {
                pathCount[neighbor] = (pathCount[neighbor] + pathCount[currNode]) % MOD;
            }
        }
    }
    
    return pathCount[end];
}
```

### **Key Template Components:**

1. **Data Structures**:
   - `dist[i]`: Shortest distance to node `i`
   - `pathCount[i]`: Number of shortest paths to node `i`
   - Priority queue: Min-heap for Dijkstra's

2. **Initialization**:
   - Start node: `dist[start] = 0`, `pathCount[start] = 1`
   - All other nodes: `dist[i] = INF`, `pathCount[i] = 0`

3. **Main Loop**:
   - Extract minimum distance node
   - Skip outdated entries
   - Update neighbors:
     - **Shorter**: Update distance, reset count
     - **Equal**: Accumulate count

4. **Modulo**: Apply `MOD` to prevent overflow

### Complexity
### **Time Complexity:** O((V + E) log V)
- **Priority queue operations**: O(E log V) - each edge processed once
- **Graph traversal**: O(V + E) - visit all nodes and edges
- **Total**: O((V + E) log V) where V = n, E = number of roads

### **Space Complexity:** O(V + E)
- **Adjacency list**: O(E) - store all edges
- **Distance array**: O(V) - store distances for all nodes
- **Path count array**: O(V) - store counts for all nodes
- **Priority queue**: O(V) - at most V nodes in queue
- **Total**: O(V + E)

## Key Points

1. **Dijkstra's Algorithm**: Finds shortest paths in weighted graphs with non-negative edges
2. **Path Counting**: Track number of ways to reach each node with shortest distance
3. **Multiple Paths**: When multiple paths have same distance, accumulate counts
4. **Modulo Arithmetic**: Handle large numbers with `10^9 + 7`
5. **Bidirectional Graph**: Roads are undirected (both directions)
6. **Outdated Skip**: Skip nodes with outdated distances in priority queue

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [743. Network Delay Time](https://www.leetcode.com/problems/network-delay-time/) - Dijkstra's basic application
- [1631. Path With Minimum Effort](https://www.leetcode.com/problems/path-with-minimum-effort/) - Dijkstra's on grid
- [1514. Path with Maximum Probability](https://www.leetcode.com/problems/path-with-maximum-probability/) - Modified Dijkstra's
- [787. Cheapest Flights Within K Stops](https://www.leetcode.com/problems/cheapest-flights-within-k-stops/) - Dijkstra's with constraints

## Tags

`Dijkstra's Algorithm`, `Shortest Path`, `Graph`, `Dynamic Programming`, `Path Counting`, `Medium`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 1976: Number of Ways to Arrive at Destination on LeetCode](https://www.leetcode.com/problems/number-of-ways-to-arrive-at-destination/)
- [LeetCode Discuss — LC 1976: Number of Ways to Arrive at Destination](https://www.leetcode.com/problems/number-of-ways-to-arrive-at-destination/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/number-of-ways-to-arrive-at-destination/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
