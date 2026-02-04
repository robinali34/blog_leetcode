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
4. **Unreachable Nodes**: If any node has distance INT_MAX, return -1

## Solution 1: Dijkstra's Algorithm with Adjacency Matrix

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<int>> adj(n, vector<int>(n, INT_MAX));
        for(auto& t: times) adj[t[0] - 1][t[1] - 1] = t[2];

        vector<long long> dist(n, INT_MAX);
        dist[k - 1] = 0;
        vector<bool> used(n, false);
        for(int i = 0; i < n; i++) {
            int x = -1;
            for(int y = 0; y < n; y++) {
                if(!used[y] && (x == -1 || dist[y] < dist[x])) {
                    x = y;
                }
            }
            used[x] = true;
            for(int y = 0; y < n; y++) {
                dist[y] = min(dist[y], dist[x] + adj[x][y]);
            }
        }
        int rtn = *max_element(dist.begin(), dist.end());
        return rtn == INT_MAX ? -1: (int)rtn;
    }
};
```

### Algorithm Breakdown:

1. **Build Adjacency Matrix**: Create `n×n` matrix where `adj[i][j]` represents edge weight from node i to node j
2. **Initialize**: Set `dist[k-1] = 0` (source node), all others to `INT_MAX`
3. **Dijkstra's Algorithm**: For n iterations:
   - Find unvisited node `x` with minimum distance
   - Mark `x` as visited
   - Relax edges: Update distances to all neighbors of `x`
4. **Result**: Return maximum distance, or -1 if any node is unreachable

### Why This Works:

- **Dijkstra's Property**: Always processes the node with minimum distance first
- **Greedy Choice**: Once a node is processed, its distance is final (non-negative weights guarantee this)
- **Relaxation**: Updates distances to neighbors if a shorter path is found

### Complexity Analysis:

- **Time Complexity**: O(n²) - For each of n nodes, we scan all n nodes to find minimum
- **Space Complexity**: O(n²) - Adjacency matrix

## Solution 3: BFS with Queue (Incorrect for Weighted Graphs)

**Note:** This solution uses BFS with a regular queue, which does **not** guarantee shortest paths in weighted graphs. It may work for some test cases but is incorrect in general. Dijkstra's algorithm (Solutions 1 and 2) is the correct approach.

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto& t: times) adj[t[0] - 1].emplace_back(t[1] - 1, t[2]);

        vector<long long> dist(n, INT_MAX);
        dist[k - 1] = 0;
        queue<int> q;
        q.push(k - 1);
        while(!q.empty()) {
            int node = q.front();
            q.pop();
            for(auto& next: adj[node]) {
                int to = next.first, d = dist[node] + next.second;
                if (d < dist[to]) {
                    dist[to] = d;
                    q.emplace(to);
                }
            }
        }
        int rtn = *max_element(dist.begin(), dist.end());
        return rtn == INT_MAX ? -1 : rtn;
    }
};
```

### Why This Is Incorrect:

- **BFS Property**: BFS processes nodes level by level, which works for unweighted graphs
- **Weighted Graphs**: With weights, the first path found may not be the shortest
- **Example**: If we have edges `A->B (weight 3)` and `A->C->B (weight 1+1=2)`, BFS might process `A->B` first and set `dist[B]=3`, then later find the shorter path `A->C->B` with `dist[B]=2`, but it may not update correctly
- **Correct Approach**: Use Dijkstra's algorithm (priority queue) to always process the node with minimum distance first

### Complexity Analysis:

- **Time Complexity**: O(n*m) worst case - May process nodes multiple times
- **Space Complexity**: O(n+m) - Adjacency list and queue

## Solution 2: Dijkstra's Algorithm with Adjacency List and Priority Queue

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n);
        for(auto& t: times) adj[t[0] - 1].emplace_back(t[1] - 1, t[2]);

        vector<long long> dist(n, INT_MAX);
        dist[k - 1] = 0;
        // use priority queue to find min distance point
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> q;
        q.emplace(0, k - 1);
        while(!q.empty()) {
            auto node = q.top();
            q.pop();
            int time = node.first, x = node.second;
            if(dist[x] < time) continue;
            for(auto& next: adj[x]) {
                int y = next.first, d = dist[x] + next.second;
                if(d < dist[y]) {
                    dist[y] = d;
                    q.emplace(d, y);
                }
            }
        }
        int rtn = *max_element(dist.begin(), dist.end());
        return rtn == INT_MAX ? -1: (int)rtn;
    }
};
```

### Algorithm Breakdown:

1. **Build Adjacency List**: Create list of neighbors for each node with edge weights
2. **Initialize**: Set `dist[k-1] = 0`, push `(0, k-1)` to priority queue
3. **Dijkstra's Algorithm**: While queue is not empty:
   - Pop node `x` with minimum distance
   - Skip if already processed (distance outdated)
   - Relax edges: For each neighbor `y`, update distance if shorter path found
4. **Result**: Return maximum distance, or -1 if any node is unreachable

### Why This Works:

- **Priority Queue**: Efficiently finds node with minimum distance in O(log n) time
- **Lazy Deletion**: Skip outdated entries with `if(dist[x] < time) continue`
- **Adjacency List**: More space-efficient for sparse graphs

### Complexity Analysis:

- **Time Complexity**: O((n+m)log n) - Each edge is processed once, priority queue operations are O(log n)
- **Space Complexity**: O(n+m) - Adjacency list and priority queue

### Sample Test Case Run:

**Input:** `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2`

**Solution 2 Execution:**

```
Initial: dist = [INT_MAX, 0, INT_MAX, INT_MAX], q = [(0, 1)]

Iteration 1:
  Pop: (0, 1) - node 2 (0-indexed: node 1)
  dist[1] = 0
  Neighbors of node 2:
    - Node 1 (0-indexed: node 0): dist[0] = min(INT_MAX, 0+1) = 1, push (1, 0)
    - Node 3 (0-indexed: node 2): dist[2] = min(INT_MAX, 0+1) = 1, push (1, 2)
  q = [(1, 0), (1, 2)]
  dist = [1, 0, 1, INT_MAX]

Iteration 2:
  Pop: (1, 0) - node 1
  dist[0] = 1
  Neighbors of node 1: None
  q = [(1, 2)]
  dist = [1, 0, 1, INT_MAX]

Iteration 3:
  Pop: (1, 2) - node 3
  dist[2] = 1
  Neighbors of node 3:
    - Node 4 (0-indexed: node 3): dist[3] = min(INT_MAX, 1+1) = 2, push (2, 3)
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
Initial: dist = [INT_MAX, INT_MAX], q = [(0, 1)] (node 2, 0-indexed: node 1)

Iteration 1:
  Pop: (0, 1) - node 2
  dist[1] = 0
  Neighbors of node 2: None
  q = []
  dist = [INT_MAX, 0]

Result: max(dist) = max(INT_MAX, 0) = INT_MAX
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

### Solution 2 (Adjacency List + Priority Queue):
- **Time Complexity**: O((n+m)log n) - Each edge processed once, priority queue operations
- **Space Complexity**: O(n+m) - Adjacency list and priority queue

## Key Insights

1. **Dijkstra's Algorithm**: Optimal for single-source shortest paths with non-negative weights
2. **Data Structure Choice**: 
   - Adjacency matrix: Better for dense graphs (O(n²) time)
   - Adjacency list + priority queue: Better for sparse graphs (O((n+m)log n) time)
3. **Maximum Distance**: The answer is the maximum shortest distance, not the sum
4. **Unreachable Detection**: Check if any distance remains INT_MAX
5. **Lazy Deletion**: In priority queue version, skip outdated entries for efficiency
6. **BFS Limitation**: BFS with a regular queue does NOT work correctly for weighted graphs - always use Dijkstra's algorithm for shortest paths with weights

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Correctness | Best For |
|----------|----------------|------------------|-------------|----------|
| Adjacency Matrix | O(n²) | O(n²) | ✓ Correct | Dense graphs (many edges) |
| Adjacency List + PQ | O((n+m)log n) | O(n+m) | ✓ Correct | Sparse graphs (few edges) |
| BFS with Queue | O(n*m) | O(n+m) | ✗ Incorrect | **Not recommended** - Use Dijkstra instead |

## Related Problems

- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Shortest path with constraints
- [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) - Maximum probability path
- [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) - Minimum effort path
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) - Shortest paths with threshold
