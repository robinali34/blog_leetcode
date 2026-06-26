---
layout: post
title: "[Medium] 743. Network Delay Time"
date: 2026-02-03 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dijkstra]
permalink: /2026/02/03/medium-743-network-delay-time/
tags: [leetcode, medium, graph, shortest-path, dijkstra]
---
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the **minimum time** it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

## Examples

**Example 1:**

```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation: The signal starts at node 2. At time 0, node 2 receives the signal.
At time 1, nodes 1 and 3 receive the signal.
At time 2, node 4 receives the signal.
So the minimum time for all nodes to receive the signal is 2.
```

**Example 2:**

```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Explanation: The signal starts at node 1. At time 1, node 2 receives the signal.
So the minimum time for all nodes to receive the signal is 1.
```

**Example 3:**

```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
Explanation: Node 2 cannot send a signal to node 1, so it's impossible for all nodes to receive the signal.
```

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `0 <= wi <= 100`
- There will not be any multiple edges (i.e., no duplicate edges).

## Thinking Process

1. **Dijkstra's Algorithm**: Optimal for single-source shortest paths with non-negative weights
- Adjacency matrix: Better for dense graphs (O(n²) time)
- Adjacency list + min-heap: Better for sparse graphs (O((n+m)log n) time) - **This is already optimal!**

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
| **BFS / DFS traversal** *(this problem)* | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| Union-Find (DSU) | O(α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |

## Solution

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Build adjacency matrix
        // Initialize with "infinity" (LLONG_MAX)
        vector<vector<long long>> adj(n, vector<long long>(n, LLONG_MAX));
        for(auto &t : times) {
            int u = t[0]-1, v = t[1]-1, w = t[2];
            adj[u][v] = w;  // edge from u to v
        }

        // Distance array
        vector<long long> dist(n, LLONG_MAX);
        dist[k-1] = 0;

        // Visited array
        vector<bool> visited(n, false);

        // Dijkstra main loop (without priority queue)
        for(int i = 0; i < n; i++) {
            // Pick the unvisited node with the smallest distance
            long long minDist = LLONG_MAX;
            int u = -1;
            for(int j = 0; j < n; j++) {
                if(!visited[j] && dist[j] < minDist) {
                    minDist = dist[j];
                    u = j;
                }
            }

            if(u == -1) break; // all remaining nodes are unreachable
            visited[u] = true;

            // Relax neighbors
            for(int v = 0; v < n; v++) {
                if(adj[u][v] != LLONG_MAX && dist[u] + adj[u][v] < dist[v]) {
                    dist[v] = dist[u] + adj[u][v];
                }
            }
        }

        // Get the maximum distance
        long long ans = *max_element(dist.begin(), dist.end());
        return ans == LLONG_MAX ? -1 : (int)ans;
    }
};
```

### Solution Explanation

**Approach:** BFS / DFS traversal (this problem)

**Key idea:** 1. **Dijkstra's Algorithm**: Optimal for single-source shortest paths with non-negative weights

**How the code works:**
1. **Dijkstra's Algorithm**: Optimal for single-source shortest paths with non-negative weights
- Adjacency matrix: Better for dense graphs (O(n²) time)
- Adjacency list + min-heap: Better for sparse graphs (O((n+m)log n) time) - **This is already optimal!**
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2`, expected output `2`:

The signal starts at node 2. At time 0, node 2 receives the signal.
At time 1, nodes 1 and 3 receive the signal.
At time 2, node 4 receives the signal.
So the minimum time for all nodes to receive the signal is 2.

### Algorithm Breakdown:

1. **Build Adjacency Matrix**: Create `n×n` matrix where `adj[i][j]` represents edge weight from node i to node j, initialized with `LLONG_MAX`
2. **Initialize**: Set `dist[k-1] = 0` (source node), all others to `LLONG_MAX`
3. **Dijkstra's Algorithm**: For n iterations:
   - Find unvisited node `u` with minimum distance (linear scan)
   - Mark `u` as visited
   - Relax edges: Update distances to all neighbors of `u` if a shorter path is found
4. **Result**: Return maximum distance, or -1 if any node is unreachable

### Why This Works:

- **Dijkstra's Property**: Always processes the node with minimum distance first
- **Greedy Choice**: Once a node is processed, its distance is final (non-negative weights guarantee this)
- **Relaxation**: Updates distances to neighbors if a shorter path is found
- **Early Termination**: If `u == -1`, all remaining nodes are unreachable, so we can break early

### Solution 1 (Adjacency Matrix):
- **Time Complexity**: O(n²) - For each of n nodes, scan all n nodes to find minimum
- **Space Complexity**: O(n²) - Adjacency matrix

### Solution 2 (Adjacency List + BFS):
- **Time Complexity**: O(n*m) worst case - May process nodes multiple times
- **Space Complexity**: O(n+m) - Adjacency list and queue

### Solution 3 (Adjacency List + Min-Heap):
- **Time Complexity**: O((n+m)log n) - Each edge processed once, min-heap operations are O(log n)
- **Space Complexity**: O(n+m) - Adjacency list and min-heap
## Related Problems

- [787. Cheapest Flights Within K Stops](https://www.leetcode.com/problems/cheapest-flights-within-k-stops/) - Shortest path with constraints
- [1514. Path with Maximum Probability](https://www.leetcode.com/problems/path-with-maximum-probability/) - Maximum probability path
- [1631. Path With Minimum Effort](https://www.leetcode.com/problems/path-with-minimum-effort/) - Minimum effort path
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://www.leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) - Shortest paths with threshold

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Dijkstra's Algorithm**: Optimal for single-source shortest paths with non-negative weights
2. **Data Structure Choice**: 
   - Adjacency matrix: Better for dense graphs (O(n²) time)
   - Adjacency list + min-heap: Better for sparse graphs (O((n+m)log n) time) - **This is already optimal!**
3. **Maximum Distance**: The answer is the maximum shortest distance, not the sum
4. **Unreachable Detection**: Check if any distance remains LLONG_MAX
5. **Lazy Deletion**: In min-heap version, skip outdated entries (`if(dist[x] < time) continue`) - this avoids expensive decrease-key operations
6. **BFS Limitation**: BFS with a regular queue does NOT work correctly for weighted graphs - always use Dijkstra's algorithm for shortest paths with weights
7. **Min-Heap Implementation**: `priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>>` creates a min-heap where the smallest distance is at the top

## References

- [LC 743: Network Delay Time on LeetCode](https://www.leetcode.com/problems/network-delay-time/)
- [LeetCode Discuss — LC 743: Network Delay Time](https://www.leetcode.com/problems/network-delay-time/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/network-delay-time/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
