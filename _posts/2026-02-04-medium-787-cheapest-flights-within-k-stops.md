---
layout: post
title: "787. Cheapest Flights Within K Stops"
date: 2026-02-04 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dynamic-programming, bellman-ford]
permalink: /2026/02/04/medium-787-cheapest-flights-within-k-stops/
tags: [leetcode, medium, graph, shortest-path, dynamic-programming, bellman-ford]
---

# 787. Cheapest Flights Within K Stops

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Stops definition**: What counts as a "stop"? (Assumption: A stop is an intermediate city visited between src and dst. The destination itself is not counted as a stop, so k stops means at most k intermediate cities)

2. **Direct flight**: Can we have a direct flight from src to dst? (Assumption: Yes, if a direct flight exists, it's valid with 0 stops)

3. **Negative cycles**: Can there be negative edge weights or cycles? (Assumption: No, all prices are positive (1 <= pricei <= 10^4), so no negative cycles)

4. **Multiple paths**: Can there be multiple paths with the same number of stops? (Assumption: Yes, we need to find the cheapest one among all paths with at most k stops)

5. **Unreachable destination**: What if dst is unreachable within k stops? (Assumption: Return -1 if no valid path exists)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Use DFS/BFS to explore all possible paths from src to dst with at most k stops, keeping track of the minimum cost. This has exponential time complexity.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use BFS level-by-level to process all nodes reachable in exactly i stops, updating minimum prices. This ensures we explore paths in order of number of stops.

**Step 3: Optimized Solution (8 minutes)**

Use Bellman-Ford algorithm with k+1 iterations (since k stops means k+1 edges), or use Dijkstra's algorithm with stops tracking. Both approaches efficiently handle the constraint on number of stops.

## Solution Approach

This is a shortest path problem with a constraint on the number of stops (edges). We need to find the cheapest path from src to dst using at most k+1 edges.

### Key Insights:

1. **Stop Constraint**: k stops means at most k+1 edges (k intermediate cities + destination)
2. **Bellman-Ford**: Perfect for this problem since it can handle edge count constraints
3. **BFS Level-by-Level**: Process nodes level by level to ensure we respect the stop limit
4. **Dijkstra with Stops**: Track both distance and number of stops in the priority queue

## Solution 1: BFS Level-by-Level

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

### Complexity Analysis:

- **Time Complexity**: O(n * m * k) worst case - May process each edge multiple times across k+1 levels
- **Space Complexity**: O(n + m) - Adjacency list and queue

## Solution 2: Bellman-Ford Algorithm

```cpp
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> dist(n, INT_MAX);
        dist[src] = 0;
        for(int i = 0; i <= k; i++) {
            vector<int> tmp(dist);
            for(auto& flight: flights) {
                if(dist[flight[0]] != INT_MAX) {
                    tmp[flight[1]] = min(tmp[flight[1]], dist[flight[0]] + flight[2]);
                }
            }
            dist = tmp;
        }
        return dist[dst] == INT_MAX ? -1: dist[dst];
    }
};
```

### Algorithm Breakdown:

1. **Initialize**: Set `dist[src] = 0`, all others to `INT_MAX`
2. **Bellman-Ford Iterations**: For k+1 iterations (k stops = k+1 edges):
   - Create temporary array `tmp` to store new distances
   - For each edge `(u, v, w)`, relax: `tmp[v] = min(tmp[v], dist[u] + w)`
   - Update `dist = tmp` after each iteration
3. **Result**: Return `dist[dst]` or -1 if unreachable

### Why This Works:

- **Bellman-Ford Property**: After i iterations, `dist[v]` contains the shortest distance from src to v using at most i edges
- **Temporary Array**: Using `tmp` prevents using updated distances in the same iteration (ensures at most i edges)
- **k+1 Iterations**: k stops means k+1 edges, so we need k+1 iterations

### Complexity Analysis:

- **Time Complexity**: O(k * m) - k+1 iterations, each processing all m edges
- **Space Complexity**: O(n) - Distance arrays

## Solution 3: Dijkstra's Algorithm with Stops Tracking

```cpp
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto& e: flights) adj[e[0]].push_back({e[1], e[2]});
        vector<int> stops(n, INT_MAX);
        priority_queue<vector<int>, vector<vector<int>>, greater<>> pq;
        pq.push({0, src, 0}); // dist node stops
        while(!pq.empty()) {
            auto tmp = pq.top();
            pq.pop();
            int dist = tmp[0], node = tmp[1], steps = tmp[2];
            if(steps >= stops[node] || steps > k + 1) continue;
            stops[node] = steps;
            if(node == dst) return dist;
            for(auto& [neighbor, price]: adj[node]) {
                pq.push({dist + price, neighbor, steps + 1});
            }
        }
        return -1;
    }
};
```

### Algorithm Breakdown:

1. **Build Adjacency List**: Create graph representation
2. **Initialize**: Push `(0, src, 0)` to priority queue (distance, node, stops)
3. **Dijkstra's Algorithm**: While queue is not empty:
   - Pop node with minimum distance
   - Skip if already visited with fewer or equal stops, or if steps > k+1
   - Update `stops[node] = steps`
   - If reached destination, return distance
   - Relax edges: Push neighbors with updated distance and steps
4. **Result**: Return -1 if destination not reached

### Why This Works:

- **Priority Queue**: Always processes node with minimum distance first
- **Stops Tracking**: `stops[node]` stores minimum stops to reach node, skip if current path uses more stops
- **Early Termination**: Return immediately when destination is reached
- **Constraint Check**: `steps > k + 1` ensures we don't exceed the stop limit

### Complexity Analysis:

- **Time Complexity**: O(m * log(m)) - Each edge may be processed multiple times, priority queue operations
- **Space Complexity**: O(n + m) - Adjacency list and priority queue

### Sample Test Case Run:

**Input:** `n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]`, `src = 0`, `dst = 3`, `k = 1`

**Solution 1 Execution (BFS):**

```
Initial: prices = [0, LONG_LONG_MAX, LONG_LONG_MAX, LONG_LONG_MAX], q = [(0, 0)], stop = 0

Stop 0:
  Process node 0:
    - Neighbor 1: newPrice = 0 + 100 = 100 < LONG_LONG_MAX, update prices[1] = 100, push (1, 100)
  q = [(1, 100)]
  prices = [0, 100, LONG_LONG_MAX, LONG_LONG_MAX]

Stop 1:
  Process node 1:
    - Neighbor 2: newPrice = 100 + 100 = 200 < LONG_LONG_MAX, update prices[2] = 200, push (2, 200)
    - Neighbor 3: newPrice = 100 + 600 = 700 < LONG_LONG_MAX, update prices[3] = 700, push (3, 700)
  q = [(2, 200), (3, 700)]
  prices = [0, 100, 200, 700]

Result: prices[3] = 700
Return: 700 ✓
```

**Verification:**
- Path: 0 -> 1 -> 3 (1 stop, cost = 100 + 600 = 700) ✓
- Path 0 -> 1 -> 2 -> 3 (2 stops) is invalid (exceeds k=1) ✗

**Output:** `700` ✓

---

**Solution 2 Execution (Bellman-Ford):**

```
Initial: dist = [0, INT_MAX, INT_MAX, INT_MAX]

Iteration 0 (0 edges):
  tmp = [0, INT_MAX, INT_MAX, INT_MAX]
  Process flights:
    - [0,1,100]: dist[0] != INT_MAX, tmp[1] = min(INT_MAX, 0+100) = 100
  dist = [0, 100, INT_MAX, INT_MAX]

Iteration 1 (1 edge, k=1 stops):
  tmp = [0, 100, INT_MAX, INT_MAX]
  Process flights:
    - [0,1,100]: tmp[1] = min(100, 0+100) = 100 (no change)
    - [1,2,100]: dist[1] != INT_MAX, tmp[2] = min(INT_MAX, 100+100) = 200
    - [1,3,600]: dist[1] != INT_MAX, tmp[3] = min(INT_MAX, 100+600) = 700
    - [2,0,100]: dist[2] != INT_MAX, tmp[0] = min(0, 200+100) = 0 (no change)
    - [2,3,200]: dist[2] != INT_MAX, tmp[3] = min(700, 200+200) = 400 (but this path has 2 stops, invalid)
  dist = [0, 100, 200, 700]

Result: dist[3] = 700
Return: 700 ✓
```

**Note:** In iteration 1, we can reach node 3 via 0->1->3 (1 stop, cost 700) or 0->1->2->3 (2 stops, cost 400), but the second path is invalid because it exceeds k=1. The algorithm correctly finds 700.

**Output:** `700` ✓

---

**Solution 3 Execution (Dijkstra with Stops):**

```
Initial: stops = [INT_MAX, INT_MAX, INT_MAX, INT_MAX], pq = [[0, 0, 0]]

Iteration 1:
  Pop: [0, 0, 0] - node 0, dist=0, steps=0
  steps (0) < stops[0] (INT_MAX), update stops[0] = 0
  node != dst, continue
  Neighbors of 0:
    - [1, 100]: push [0+100, 1, 0+1] = [100, 1, 1]
  pq = [[100, 1, 1]]
  stops = [0, INT_MAX, INT_MAX, INT_MAX]

Iteration 2:
  Pop: [100, 1, 1] - node 1, dist=100, steps=1
  steps (1) < stops[1] (INT_MAX), update stops[1] = 1
  node != dst, continue
  Neighbors of 1:
    - [2, 100]: push [100+100, 2, 1+1] = [200, 2, 2]
    - [3, 600]: push [100+600, 3, 1+1] = [700, 3, 2]
  pq = [[200, 2, 2], [700, 3, 2]]
  stops = [0, 1, INT_MAX, INT_MAX]

Iteration 3:
  Pop: [200, 2, 2] - node 2, dist=200, steps=2
  steps (2) < stops[2] (INT_MAX), update stops[2] = 2
  node != dst, continue
  steps (2) <= k+1 (2), continue
  Neighbors of 2:
    - [0, 100]: push [200+100, 0, 2+1] = [300, 0, 3], but steps (3) > k+1 (2), skip
    - [3, 200]: push [200+200, 3, 2+1] = [400, 3, 3], but steps (3) > k+1 (2), skip
  pq = [[700, 3, 2]]
  stops = [0, 1, 2, INT_MAX]

Iteration 4:
  Pop: [700, 3, 2] - node 3, dist=700, steps=2
  steps (2) < stops[3] (INT_MAX), update stops[3] = 2
  node == dst, return 700 ✓
```

**Verification:**
- Found path: 0 -> 1 -> 3 (1 stop, cost 700) ✓
- Steps = 2 (which is k+1 = 2) ✓

**Output:** `700` ✓

## Complexity Analysis

### Solution 1 (BFS Level-by-Level):
- **Time Complexity**: O(n * m * k) - Process each edge up to k+1 times
- **Space Complexity**: O(n + m) - Adjacency list and queue

### Solution 2 (Bellman-Ford):
- **Time Complexity**: O(k * m) - k+1 iterations, each processing all m edges
- **Space Complexity**: O(n) - Distance arrays

### Solution 3 (Dijkstra with Stops):
- **Time Complexity**: O(m * log(m)) - Each edge may be processed multiple times
- **Space Complexity**: O(n + m) - Adjacency list and priority queue

## Key Insights

1. **Stop Constraint**: k stops means at most k+1 edges (k intermediate cities + destination)
2. **Bellman-Ford Advantage**: Naturally handles edge count constraints - perfect for this problem
3. **BFS Level-by-Level**: Ensures we process nodes in order of number of stops
4. **Dijkstra with Stops**: Track both distance and stops, skip paths that exceed limit or use more stops
5. **Temporary Array**: In Bellman-Ford, using `tmp` prevents using updated distances in the same iteration

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Best For |
|----------|----------------|------------------|----------|
| BFS Level-by-Level | O(n * m * k) | O(n + m) | Simple implementation, easy to understand |
| Bellman-Ford | O(k * m) | O(n) | **Optimal for this problem** - handles edge constraints naturally |
| Dijkstra with Stops | O(m * log(m)) | O(n + m) | When k is large, may be more efficient |

**Note:** Bellman-Ford (Solution 2) is typically the best choice for this problem because it naturally handles the edge count constraint and has better time complexity when k is small.

## Related Problems

- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) - Shortest path without stop constraint
- [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) - Maximum probability path
- [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) - Minimum effort path
- [1928. Minimum Cost to Reach Destination in Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) - Shortest path with time constraint
