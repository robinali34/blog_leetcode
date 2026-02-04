---
layout: post
title: "743. Network Delay Time"
date: 2026-02-03 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dijkstra]
permalink: /2026/02/03/medium-743-network-delay-time/
tags: [leetcode, medium, graph, shortest-path, dijkstra]
---

# 743. Network Delay Time

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Graph properties**: What type of graph is this? (Assumption: Directed weighted graph - edges have direction and weights representing time)

2. **Node numbering**: How are nodes numbered? (Assumption: Nodes are numbered from 1 to n, but we'll use 0-indexed arrays internally)

3. **All nodes reachable**: What if not all nodes are reachable from node k? (Assumption: Return -1 if any node is unreachable)

4. **Minimum time definition**: What does "minimum time for all nodes to receive the signal" mean? (Assumption: The maximum shortest distance from node k to any node - the time when the last node receives the signal)

5. **Edge weights**: Can edge weights be negative? (Assumption: No - all weights are non-negative (0 <= wi <= 100), so we can use Dijkstra's algorithm)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Use BFS/DFS to explore all paths from node k, keeping track of minimum time to reach each node. This approach has exponential time complexity in worst case due to exploring all possible paths.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use Bellman-Ford algorithm to find shortest paths from node k to all other nodes. This works for any graph but has O(n*m) time complexity, where m is the number of edges.

**Step 3: Optimized Solution (8 minutes)**

Use Dijkstra's algorithm since all edge weights are non-negative. We can use either:
- Adjacency matrix with O(n²) time complexity
- Adjacency list with priority queue for O((n+m)log n) time complexity

The answer is the maximum shortest distance from node k to any node, or -1 if any node is unreachable.

## Solution Approach

This is a classic shortest path problem. We need to find the shortest distance from node k to all other nodes, then return the maximum of these distances.

### Key Insights:

1. **Shortest Path Problem**: Find shortest paths from a single source (node k) to all destinations
2. **Dijkstra's Algorithm**: Optimal choice since all edge weights are non-negative
3. **Maximum Distance**: The answer is the maximum shortest distance, representing when the last node receives the signal
4. **Unreachable Nodes**: If any node has distance LLONG_MAX, return -1

## Solution 1: Dijkstra's Algorithm with Adjacency Matrix

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

### Complexity Analysis:

- **Time Complexity**: O(n²) - For each of n nodes, we scan all n nodes to find minimum
- **Space Complexity**: O(n²) - Adjacency matrix

## Solution 2: Adjacency List - Version A: BFS (Without Dijkstra)

This solution uses BFS with a regular queue. While BFS doesn't guarantee shortest paths in general weighted graphs, **it works correctly for this problem** because:

1. **We update distances whenever a shorter path is found** - The key is the condition `if (d < dist[to])`
2. **We re-queue nodes when their distance improves** - This allows us to explore all possible paths
3. **Eventually converges** - Since we only update when finding shorter paths, the algorithm will eventually find all shortest paths, though it may process nodes multiple times

**Note:** This approach is less efficient than Dijkstra's algorithm but is simpler to implement and works correctly for this problem.

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto& t: times) adj[t[0] - 1].emplace_back(t[1] - 1, t[2]);

        vector<long long> dist(n, LLONG_MAX);
        dist[k - 1] = 0;
        queue<int> q;
        q.push(k - 1);
        while(!q.empty()) {
            int node = q.front();
            q.pop();
            for(auto& next: adj[node]) {
                int to = next.first;
                long long d = dist[node] + next.second;
                if (d < dist[to]) {
                    dist[to] = d;
                    q.emplace(to);
                }
            }
        }
        long long rtn = *max_element(dist.begin(), dist.end());
        return rtn == LLONG_MAX ? -1 : (int)rtn;
    }
};
```

### Why This Works:

- **Distance Update**: We only update `dist[to]` when we find a shorter path (`d < dist[to]`)
- **Re-queuing**: When a node's distance improves, we add it back to the queue to explore paths from it
- **Convergence**: Eventually, all shortest paths will be found, though nodes may be processed multiple times
- **Correctness**: Unlike standard BFS, this version continues until no more distance improvements are possible

### Complexity Analysis:

- **Time Complexity**: O(n*m) worst case - May process nodes multiple times (each edge can be relaxed multiple times)
- **Space Complexity**: O(n+m) - Adjacency list and queue

## Solution 3: Adjacency List - Version B: Dijkstra with Min-Heap (Optimal)

**This is the optimal implementation!** This solution uses Dijkstra's algorithm with a min-heap (priority queue with `greater<>` comparator) and is the best practical approach for this problem.

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto& t: times) adj[t[0] - 1].emplace_back(t[1] - 1, t[2]);

        vector<long long> dist(n, LLONG_MAX);
        dist[k - 1] = 0;
        // Min-heap: priority_queue with greater<> comparator
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> q;
        q.emplace(0, k - 1);
        while(!q.empty()) {
            auto node = q.top();
            q.pop();
            long long time = node.first;
            int x = node.second;
            if(dist[x] < time) continue; // Skip outdated entries (lazy deletion)
            for(auto& next: adj[x]) {
                int y = next.first;
                long long d = dist[x] + next.second;
                if(d < dist[y]) {
                    dist[y] = d;
                    q.emplace(d, y);
                }
            }
        }
        long long rtn = *max_element(dist.begin(), dist.end());
        return rtn == LLONG_MAX ? -1 : (int)rtn;
    }
};
```

### Algorithm Breakdown:

1. **Build Adjacency List**: Create list of neighbors for each node with edge weights
2. **Initialize**: Set `dist[k-1] = 0`, push `(0, k-1)` to min-heap
3. **Dijkstra's Algorithm**: While heap is not empty:
   - Pop node `x` with minimum distance
   - Skip if already processed (distance outdated - lazy deletion)
   - Relax edges: For each neighbor `y`, update distance if shorter path found
4. **Result**: Return maximum distance, or -1 if any node is unreachable

### Why This Works:

- **Min-Heap (Priority Queue)**: `priority_queue` with `greater<>` comparator creates a min-heap, efficiently finding the node with minimum distance in O(log n) time
- **Lazy Deletion**: Skip outdated entries with `if(dist[x] < time) continue` - this avoids expensive heap updates
- **Adjacency List**: More space-efficient for sparse graphs
- **Optimal Implementation**: This is already the optimal practical implementation for Dijkstra's algorithm

### Complexity Analysis:

- **Time Complexity**: O((n+m)log n) - Each edge is processed once, min-heap operations (insert/extract-min) are O(log n)
- **Space Complexity**: O(n+m) - Adjacency list and min-heap

### Further Optimization Notes:

- **Theoretical Optimization**: Fibonacci heap can achieve O(n log n + m) time complexity, but it's not practical due to high constant factors and complexity
- **Current Implementation**: The binary min-heap (priority_queue) is already optimal for practical purposes
- **Lazy Deletion**: The `if(dist[x] < time) continue` check is crucial - it allows us to avoid expensive decrease-key operations by simply adding duplicate entries and skipping outdated ones

### Sample Test Case Run:

**Input:** `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2`

**Solution 3 Execution:**

```
Initial: dist = [LLONG_MAX, 0, LLONG_MAX, LLONG_MAX], q = [(0, 1)]

Iteration 1:
  Pop: (0, 1) - node 2 (0-indexed: node 1)
  dist[1] = 0
  Neighbors of node 2:
    - Node 1 (0-indexed: node 0): dist[0] = min(LLONG_MAX, 0+1) = 1, push (1, 0)
    - Node 3 (0-indexed: node 2): dist[2] = min(LLONG_MAX, 0+1) = 1, push (1, 2)
  q = [(1, 0), (1, 2)]
  dist = [1, 0, 1, LLONG_MAX]

Iteration 2:
  Pop: (1, 0) - node 1
  dist[0] = 1
  Neighbors of node 1: None
  q = [(1, 2)]
  dist = [1, 0, 1, LLONG_MAX]

Iteration 3:
  Pop: (1, 2) - node 3
  dist[2] = 1
  Neighbors of node 3:
    - Node 4 (0-indexed: node 3): dist[3] = min(LLONG_MAX, 1+1) = 2, push (2, 3)
  q = [(2, 3)]
  dist = [1, 0, 1, 2]

Iteration 4:
  Pop: (2, 3) - node 4
  dist[3] = 2
  Neighbors of node 4: None
  q = []
  dist = [1, 0, 1, 2]

Result: max(dist) = max(1, 0, 1, 2) = 2
Return: 2 ✓
```

**Verification:**
- Node 2 receives signal at time 0 ✓
- Nodes 1 and 3 receive signal at time 1 ✓
- Node 4 receives signal at time 2 ✓
- Maximum time = 2 ✓

**Output:** `2` ✓

---

**Another Example:** `times = [[1,2,1]]`, `n = 2`, `k = 2`

```
Initial: dist = [LLONG_MAX, LLONG_MAX], q = [(0, 1)] (node 2, 0-indexed: node 1)

Iteration 1:
  Pop: (0, 1) - node 2
  dist[1] = 0
  Neighbors of node 2: None
  q = []
  dist = [LLONG_MAX, 0]

Result: max(dist) = max(LLONG_MAX, 0) = LLONG_MAX
Return: -1 ✓
```

**Verification:**
- Node 2 receives signal at time 0 ✓
- Node 1 is unreachable from node 2 ✗
- Return -1 ✓

**Output:** `-1` ✓

## Complexity Analysis

### Solution 1 (Adjacency Matrix):
- **Time Complexity**: O(n²) - For each of n nodes, scan all n nodes to find minimum
- **Space Complexity**: O(n²) - Adjacency matrix

### Solution 2 (Adjacency List + BFS):
- **Time Complexity**: O(n*m) worst case - May process nodes multiple times
- **Space Complexity**: O(n+m) - Adjacency list and queue

### Solution 3 (Adjacency List + Min-Heap):
- **Time Complexity**: O((n+m)log n) - Each edge processed once, min-heap operations are O(log n)
- **Space Complexity**: O(n+m) - Adjacency list and min-heap

## Key Insights

1. **Dijkstra's Algorithm**: Optimal for single-source shortest paths with non-negative weights
2. **Data Structure Choice**: 
   - Adjacency matrix: Better for dense graphs (O(n²) time)
   - Adjacency list + min-heap: Better for sparse graphs (O((n+m)log n) time) - **This is already optimal!**
3. **Maximum Distance**: The answer is the maximum shortest distance, not the sum
4. **Unreachable Detection**: Check if any distance remains LLONG_MAX
5. **Lazy Deletion**: In min-heap version, skip outdated entries (`if(dist[x] < time) continue`) - this avoids expensive decrease-key operations
6. **BFS Limitation**: BFS with a regular queue does NOT work correctly for weighted graphs - always use Dijkstra's algorithm for shortest paths with weights
7. **Min-Heap Implementation**: `priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>>` creates a min-heap where the smallest distance is at the top

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Correctness | Best For |
|----------|----------------|------------------|-------------|----------|
| Adjacency Matrix | O(n²) | O(n²) | ✓ Correct | Dense graphs (many edges) |
| Adjacency List + BFS | O(n*m) | O(n+m) | ✓ Correct | Simple implementation, works but less efficient |
| Adjacency List + Min-Heap | O((n+m)log n) | O(n+m) | ✓ Correct | Sparse graphs (few edges) - **Optimal!** |

**Note:** The "Adjacency List + Min-Heap" approach (Solution 3) is the optimal practical implementation. While Fibonacci heap theoretically achieves O(n log n + m), the binary min-heap (priority_queue) is faster in practice due to lower constant factors.

## Related Problems

- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Shortest path with constraints
- [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) - Maximum probability path
- [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) - Minimum effort path
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) - Shortest paths with threshold
