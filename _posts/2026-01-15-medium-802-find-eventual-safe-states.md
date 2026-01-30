---
layout: post
title: "802. Find Eventual Safe States"
date: 2026-01-15 00:00:00 -0700
categories: [leetcode, medium, graph, dfs, cycle-detection]
permalink: /2026/01/15/medium-802-find-eventual-safe-states/
tags: [leetcode, medium, graph, dfs, cycle-detection, three-state-coloring]
---

# 802. Find Eventual Safe States

## Problem Statement

There is a directed graph of `n` nodes with each node labeled from `0` to `n - 1`. The graph is represented by a **0-indexed** 2D integer array `graph` where `graph[i]` is an integer array of nodes adjacent to node `i`, meaning there is an edge from node `i` to each node in `graph[i]`.

A node is a **terminal node** if there are no outgoing edges. A node is a **safe node** if every possible path starting from that node leads to a terminal node (or another safe node).

Return *an array containing all the **safe nodes** of the graph*. The answer should be sorted in **ascending order**.

## Examples

**Example 1:**
```
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The graph is shown above.
Nodes 5 and 6 are terminal nodes, and every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
```

**Example 2:**
```
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation: Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
```

## Constraints

- `n == graph.length`
- `1 <= n <= 10^4`
- `0 <= graph[i].length <= n`
- `0 <= graph[i][j] <= n - 1`
- `graph[i]` is sorted in ascending order.
- The graph may contain self-loops.
- The number of edges in the graph will be in the range `[0, n * (n - 1) / 2]`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Safe state definition**: What makes a node "safe"? (Assumption: A node is safe if all paths starting from it eventually lead to a terminal node - no cycles reachable)

2. **Terminal node**: What is a terminal node? (Assumption: A node with no outgoing edges - it's a sink node)

3. **Graph type**: Is the graph directed or undirected? (Assumption: Directed - edges have direction, represented as adjacency list)

4. **Self-loops**: Can nodes have self-loops? (Assumption: Yes - per constraints, graph may contain self-loops)

5. **Cycle handling**: How should we handle cycles? (Assumption: Nodes in cycles are not safe - they can never reach a terminal node)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For each node, check if it's part of a cycle by doing DFS starting from that node. If DFS encounters a node that's already in the current path (back edge), there's a cycle and the node is unsafe. This approach requires O(n × (V + E)) time as we check each node, which is too slow for large graphs.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use DFS with coloring: mark nodes as white (unvisited), gray (currently in path), or black (processed). If we encounter a gray node during DFS, we found a cycle. All nodes in the cycle and nodes that can reach the cycle are unsafe. However, identifying all unsafe nodes requires careful tracking of which nodes can reach cycles.

**Step 3: Optimized Solution (8 minutes)**

Use reverse graph + topological sort: reverse all edges, then nodes with no outgoing edges (sinks) in the original graph become sources in the reversed graph. Use topological sort starting from these sources. All nodes reachable from sources in the reversed graph are safe (they eventually reach a terminal node). Alternatively, use DFS with memoization: for each node, check if all paths lead to terminal nodes. Nodes that can reach cycles are unsafe. The reverse graph approach is cleaner: safe nodes are those that can reach terminal nodes, which is equivalent to being reachable from terminal nodes in the reversed graph.

## Solution Approach

This problem requires finding all nodes that do **not** lead to any cycle. A node is safe if all paths starting from it eventually reach a terminal node (a node with no outgoing edges).

### Key Insights:

1. **Safe Nodes**: Nodes that don't lead to cycles and eventually reach terminal nodes
2. **Terminal Nodes**: Nodes with no outgoing edges (empty `graph[i]`)
3. **Cycle Detection**: Nodes in cycles are unsafe
4. **Three-State Coloring**: Use `0=unvisited`, `1=visiting`, `2=safe` to track node states
5. **DFS Traversal**: Recursively check if all paths from a node lead to safe nodes

### Algorithm:

1. **Initialize Color Array**: All nodes start as unvisited (`0`)
2. **DFS from Each Node**: Check if node is safe
3. **State Transitions**:
   - If node is already visited (`color[x] > 0`), return whether it's safe (`color[x] == 2`)
   - Mark node as visiting (`color[x] = 1`)
   - Recursively check all neighbors
   - If any neighbor is unsafe, current node is unsafe
   - If all neighbors are safe, mark current node as safe (`color[x] = 2`)
4. **Collect Safe Nodes**: Return all nodes with `color[i] == 2`

## Solution

### **Solution: DFS with Three-State Coloring**

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        const int N = graph.size();
        vector<int> color(N);
        vector<int> rtn;
        for(int i = 0; i < N; i++) {
            if(safe(i, graph, color)) rtn.push_back(i);
        }
        return rtn;
    }
    
private:
    bool safe(int x, vector<vector<int>>& graph, vector<int>& color) {
        if(color[x] > 0) {
            return color[x] == 2;
        }
        color[x] = 1;
        for(int y: graph[x]) {
            if(!safe(y, graph, color)) return false;
        }
        color[x] = 2;
        return true;
    }
};
```

### **Algorithm Explanation:**

1. **Initialization (Lines 4-5)**:
   - `color` array tracks state: `0=unvisited`, `1=visiting`, `2=safe`
   - `rtn` stores result (safe nodes)

2. **Main Loop (Lines 6-9)**:
   - For each node `i`, check if it's safe using DFS
   - If safe, add to result

3. **DFS Function `safe()` (Lines 12-22)**:
   - **Base Case (Lines 13-15)**: If node already visited, return whether it's safe
   - **Mark Visiting (Line 16)**: Set `color[x] = 1` to detect cycles
   - **Check Neighbors (Lines 17-19)**: 
     - Recursively check all neighbors
     - If any neighbor is unsafe (leads to cycle), return `false`
   - **Mark Safe (Line 20)**: If all neighbors are safe, mark current node as safe
   - **Return (Line 21)**: Return `true` if node is safe

### **How It Works:**

- **Cycle Detection**: If during DFS we encounter a node with `color[x] == 1` (visiting), it means we're in a cycle, so that path is unsafe
- **Memoization**: Once a node is marked as safe (`color[x] == 2`), we don't need to recompute it
- **Terminal Nodes**: Nodes with no outgoing edges are automatically safe (loop doesn't execute, node marked as safe)

### **Example Walkthrough:**

**Input:** `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`

```
Graph structure:
0 -> 1, 2
1 -> 2, 3
2 -> 5
3 -> 0
4 -> 5
5 -> [] (terminal)
6 -> [] (terminal)

DFS from node 0:
  color[0] = 1 (visiting)
  Check node 1:
    color[1] = 1
    Check node 2:
      color[2] = 1
      Check node 5:
        color[5] = 2 (safe, terminal)
      color[2] = 2 (safe)
    Check node 3:
      color[3] = 1
      Check node 0:
        color[0] == 1 → cycle detected!
        Return false
      Return false
    Return false
  Return false
  Node 0 is unsafe

DFS from node 2:
  color[2] = 1
  Check node 5:
    color[5] = 2 (safe)
  color[2] = 2 (safe)
  Node 2 is safe ✓

Result: [2, 4, 5, 6]
```

### **Complexity Analysis:**

- **Time Complexity:** O(V + E)
  - Each node is visited at most once
  - Each edge is traversed at most once
  - Overall: O(V + E) where V = number of nodes, E = number of edges

- **Space Complexity:** O(V)
  - `color` array: O(V)
  - Recursion stack: O(V) in worst case
  - Result array: O(V)
  - Overall: O(V)

## Key Insights

1. **Safe Nodes**: Nodes that don't lead to cycles and eventually reach terminal nodes
2. **Three-State Coloring**: Efficient way to detect cycles and memoize safe nodes
3. **Terminal Nodes**: Automatically safe (no outgoing edges)
4. **Cycle Detection**: If we encounter a "visiting" node during DFS, cycle exists
5. **Memoization**: Once a node is determined safe, reuse the result

## Edge Cases

1. **All terminal nodes**: `graph = [[],[],[]]` → return `[0,1,2]`
2. **All nodes in cycle**: `graph = [[1],[0]]` → return `[]`
3. **Single node**: `graph = [[]]` → return `[0]`
4. **Disconnected components**: Some safe, some unsafe
5. **Self-loops**: Node pointing to itself is unsafe

## Common Mistakes

1. **Not detecting cycles correctly**: Forgetting to check if node is "visiting"
2. **Incorrect state transitions**: Not marking node as safe after checking neighbors
3. **Not handling terminal nodes**: Terminal nodes should be automatically safe
4. **Wrong return condition**: Returning `false` when encountering visiting node
5. **Not sorting result**: Result should be sorted in ascending order

## Alternative Approaches

### **Approach 2: Reverse Graph + Topological Sort (BFS - Kahn's Algorithm)**

Reverse the graph and use topological sort (Kahn's algorithm) starting from terminal nodes. This approach works backwards: terminal nodes are safe, and nodes that only lead to safe nodes become safe.

```cpp
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        const int N = graph.size();

        // Reverse graph: edge v -> u means u can reach v in original graph
        vector<vector<int>> reverseGraph(N);
        vector<int> outDegree(N);
        for(int u = 0; u < N; u++) {
            for(int v: graph[u]) {
                reverseGraph[v].emplace_back(u);
            }
            outDegree[u]= graph[u].size();
        }

        // Start with terminal nodes (outDegree == 0)
        queue<int> q;
        for(int i = 0; i < N; i++) {
            if(outDegree[i] == 0) {
                q.push(i);
            }
        }

        // Kahn's algorithm on reverse graph
        while(!q.empty()) {
            int safe = q.front();
            q.pop();
            for(int prev: reverseGraph[safe]) {
                if(--outDegree[prev] == 0) {
                    q.push(prev);
                }
            }
        }

        // Nodes with outDegree == 0 are eventually safe
        vector<int> rtn;
        for(int i = 0; i < N; i++) {
            if(outDegree[i] == 0) {
                rtn.emplace_back(i);
            }
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Build Reverse Graph (Lines 6-13)**:
   - Create `reverseGraph` where `reverseGraph[v]` contains all nodes `u` that have an edge `u -> v` in the original graph
   - Count `outDegree[u]` = number of outgoing edges from node `u` in original graph
   - This allows us to traverse backwards from terminal nodes

2. **Initialize Queue (Lines 15-20)**:
   - Start with all terminal nodes (nodes with `outDegree == 0`)
   - These are automatically safe since they have no outgoing edges

3. **Kahn's Algorithm (Lines 22-30)**:
   - Process each safe node from the queue
   - For each predecessor `prev` in the reverse graph:
     - Decrement `outDegree[prev]` (removing the edge to the safe node)
     - If `outDegree[prev] == 0`, all paths from `prev` lead to safe nodes, so `prev` becomes safe
     - Add `prev` to queue for further processing

4. **Collect Safe Nodes (Lines 32-37)**:
   - After processing, all nodes with `outDegree == 0` are eventually safe
   - Nodes in cycles will have `outDegree > 0` (they can't reach terminal nodes)

### **How It Works:**

- **Terminal Nodes**: Start with nodes that have no outgoing edges (automatically safe)
- **Propagation**: If all outgoing edges from a node lead to safe nodes, that node becomes safe
- **Cycle Detection**: Nodes in cycles will never have their `outDegree` reduced to 0, so they remain unsafe
- **Reverse Graph**: Allows us to efficiently find predecessors and propagate safety backwards

### **Example Walkthrough:**

**Input:** `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`

```
Original graph:
0 -> 1, 2
1 -> 2, 3
2 -> 5
3 -> 0
4 -> 5
5 -> [] (terminal)
6 -> [] (terminal)

Reverse graph:
0 -> 3
1 -> 0
2 -> 0, 1
3 -> 1
5 -> 2, 4
6 -> [] (no incoming edges)

outDegree = [2, 2, 1, 1, 1, 0, 0]

Step 1: Initialize queue with terminal nodes
  q = [5, 6]
  outDegree = [2, 2, 1, 1, 1, 0, 0]

Step 2: Process node 5
  Predecessors: [2, 4]
  outDegree[2] = 1 - 1 = 0 → q.push(2)
  outDegree[4] = 1 - 1 = 0 → q.push(4)
  outDegree = [2, 2, 0, 1, 0, 0, 0]
  q = [6, 2, 4]

Step 3: Process node 6
  No predecessors
  outDegree = [2, 2, 0, 1, 0, 0, 0]
  q = [2, 4]

Step 4: Process node 2
  Predecessors: [0, 1]
  outDegree[0] = 2 - 1 = 1
  outDegree[1] = 2 - 1 = 1
  outDegree = [1, 1, 0, 1, 0, 0, 0]
  q = [4]

Step 5: Process node 4
  Predecessors: [] (none in reverse graph)
  outDegree = [1, 1, 0, 1, 0, 0, 0]
  q = []

Final: outDegree == 0 → [2, 4, 5, 6] are safe
```

### **Complexity Analysis:**

- **Time Complexity:** O(V + E)
  - Building reverse graph: O(V + E)
  - BFS traversal: O(V + E)
  - Collecting result: O(V)
  - Overall: O(V + E)

- **Space Complexity:** O(V + E)
  - Reverse graph: O(V + E)
  - `outDegree` array: O(V)
  - Queue: O(V)
  - Result: O(V)
  - Overall: O(V + E)

### **Comparison: DFS vs BFS Approach**

| Aspect | DFS (Three-State Coloring) | BFS (Reverse Graph) |
|--------|----------------------------|---------------------|
| **Intuition** | Directly detects cycles via state tracking | Works backwards from terminal nodes |
| **Recursion** | Uses recursion stack (O(V) space) | Iterative, no recursion |
| **Memory** | O(V) for color array + recursion | O(V + E) for reverse graph |
| **Cycle Detection** | Explicit via "visiting" state | Implicit: nodes in cycles never reach outDegree 0 |
| **Implementation** | More concise, recursive | More verbose, iterative |
| **Stack Overflow Risk** | Possible on deep graphs | No recursion, more stable |
| **Best For** | When you want direct cycle detection | When you prefer iterative approach or have deep graphs |

Both approaches are valid and have the same time complexity. Choose based on preference and constraints.

## Related Problems

- [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) - Cycle detection in directed graph
- [LC 210: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Topological sort ordering
- [LCR 113: Course Schedule II (CN)](https://robinali34.github.io/blog_leetcode/2026/01/14/medium-lcr113-course-schedule-ii/) - DFS with three-state coloring
- [LC 310: Minimum Height Trees](https://robinali34.github.io/blog_leetcode/2026/01/14/medium-310-minimum-height-trees/) - Graph traversal, BFS/DFS
- [LC 269: Alien Dictionary](https://robinali34.github.io/blog_leetcode/2026/01/14/hard-269-alien-dictionary/) - Topological sort

---

*This problem demonstrates the **Three-State Coloring** pattern for cycle detection in directed graphs. The key insight is that safe nodes are those that don't lead to cycles and eventually reach terminal nodes.*

