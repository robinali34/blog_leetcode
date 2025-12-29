---
layout: post
title: "1976. Number of Ways to Arrive at Destination"
date: 2025-12-28 14:30:00 -0700
categories: [leetcode, medium, dijkstra, shortest-path, graph, dynamic-programming]
permalink: /2025/12/28/medium-1976-number-of-ways-to-arrive-at-destination/
---

# 1976. Number of Ways to Arrive at Destination

## Problem Statement

You are in a city that consists of `n` intersections numbered from `0` to `n - 1` with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is **at most one** road between any two intersections.

You are given an integer `n` and an array `roads` where `roads[i] = [ui, vi, timei]` means that there is a road between intersections `ui` and `vi` that takes `timei` minutes to travel. You want to know how many ways you can travel from intersection `0` to intersection `n - 1` in the **shortest amount of time**.

Return *the **number of ways** you can arrive at your destination in the **shortest amount of time***. Since the answer may be large, return it **modulo** `10^9 + 7`.

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

## Solution Approach

This problem requires finding the **number of shortest paths** from node `0` to node `n-1` in a weighted, undirected graph. This is a classic application of **Dijkstra's algorithm** combined with **dynamic programming** to count paths.

### Key Insights:

1. **Dijkstra's Algorithm**: Find shortest distances from source (node 0) to all nodes
2. **Path Counting**: Count number of ways to reach each node with shortest distance
3. **Multiple Paths**: When multiple paths have the same shortest distance, accumulate the count
4. **Modulo Arithmetic**: Handle large numbers with `10^9 + 7`

### Algorithm:

1. **Build adjacency list**: Create graph representation from roads
2. **Dijkstra's Algorithm**: Use priority queue to find shortest paths
3. **Path Counting**: 
   - If shorter path found: update distance and reset count
   - If equal path found: add to count
4. **Return**: Number of shortest paths to destination

## Solution

### **Solution: Dijkstra's Algorithm with Path Counting**

```cpp
class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        const int MOD = 1e9 + 7;
        vector<vector<pair<int, int>>> adjList(n);
        for(auto& road: roads) {
            int startNode = road[0], endNode = road[1], travelTime = road[2];
            adjList[startNode].emplace_back(endNode, travelTime);
            adjList[endNode].emplace_back(startNode, travelTime);
        }
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> minHeap;
        vector<long long> shortestTime(n, LLONG_MAX);
        vector<int> pathCount(n, 0);
        shortestTime[0] = 0;
        pathCount[0] = 1;
        minHeap.emplace(0, 0);
        while(!minHeap.empty()) {
            auto [currTime, currNode] = minHeap.top();
            minHeap.pop();

            if(currTime > shortestTime[currNode]) continue;
            for(auto& [neighborNode, roadTime]: adjList[currNode]) {
                if(currTime + roadTime < shortestTime[neighborNode]) {
                    shortestTime[neighborNode] = currTime + roadTime;
                    pathCount[neighborNode] = pathCount[currNode];
                    minHeap.emplace(shortestTime[neighborNode], neighborNode);
                }
                else if (currTime + roadTime == shortestTime[neighborNode]) {
                    pathCount[neighborNode] = (pathCount[neighborNode] + pathCount[currNode]) % MOD;
                }
            }
        }
        return pathCount[n - 1];
    }
};
```

### **Algorithm Explanation:**

1. **Graph Construction (Lines 5-9)**:
   - Build bidirectional adjacency list
   - Each edge stores `(neighbor, weight)`

2. **Initialization (Lines 10-15)**:
   - `shortestTime[i]`: Shortest time to reach node `i` (initialized to `LLONG_MAX`)
   - `pathCount[i]`: Number of shortest paths to node `i` (initialized to 0)
   - Start node: `shortestTime[0] = 0`, `pathCount[0] = 1`
   - Priority queue: `(time, node)` pairs, min-heap

3. **Dijkstra's Algorithm (Lines 16-30)**:
   - Extract node with minimum time
   - Skip if outdated (already found shorter path)
   - For each neighbor:
     - **Shorter path found**: Update distance and reset count
     - **Equal path found**: Add to count (modulo)

4. **Result**: Return `pathCount[n-1]` - number of shortest paths to destination

### **Example Walkthrough:**

**For `n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]`:**

```
Graph:
0 --2-- 1 --3-- 2
|       |       |
7       3       1
|       |       |
6 --1-- 5 --1-- 3
|       |
2       1
|
4

Dijkstra's Execution:

Step 1: Start at node 0
- shortestTime[0] = 0, pathCount[0] = 1
- Explore: 0→1 (time=2), 0→4 (time=5), 0→6 (time=7)

Step 2: Process node 1 (time=2)
- shortestTime[1] = 2, pathCount[1] = 1
- Explore: 1→2 (time=2+3=5), 1→3 (time=2+3=5)

Step 3: Process node 4 (time=5)
- shortestTime[4] = 5, pathCount[4] = 1
- Explore: 4→6 (time=5+2=7)

Step 4: Process node 2 (time=5)
- shortestTime[2] = 5, pathCount[2] = 1
- Explore: 2→5 (time=5+1=6)

Step 5: Process node 3 (time=5)
- shortestTime[3] = 5, pathCount[3] = 1
- Explore: 3→5 (time=5+1=6), 3→6 (time=5+3=8)

Step 6: Process node 5 (time=6)
- shortestTime[5] = 6, pathCount[5] = 2 (from node 2 and 3)
- Explore: 5→6 (time=6+1=7)

Step 7: Process node 6 (time=7)
- Found paths with time=7:
  - 0→6 (direct): pathCount = 1
  - 0→4→6: pathCount = 1
  - 0→1→2→5→6: pathCount = 1
  - 0→1→3→5→6: pathCount = 1
- pathCount[6] = 1 + 1 + 1 + 1 = 4

Result: 4 ways to reach node 6 with shortest time 7
```

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

## Complexity Analysis

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

## Alternative Approaches

### **Approach 1: Dijkstra + DP (Current Solution)**
- **Time**: O((V + E) log V)
- **Space**: O(V + E)
- **Best for**: General graphs with non-negative weights

### **Approach 2: BFS (Unweighted Graphs Only)**
- **Time**: O(V + E)
- **Space**: O(V + E)
- **Limitation**: Only works for unweighted graphs

### **Approach 3: Floyd-Warshall (All Pairs)**
- **Time**: O(V³)
- **Space**: O(V²)
- **Use case**: Need shortest paths between all pairs

## Related Problems

- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) - Dijkstra's basic application
- [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) - Dijkstra's on grid
- [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) - Modified Dijkstra's
- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Dijkstra's with constraints

## Tags

`Dijkstra's Algorithm`, `Shortest Path`, `Graph`, `Dynamic Programming`, `Path Counting`, `Medium`

