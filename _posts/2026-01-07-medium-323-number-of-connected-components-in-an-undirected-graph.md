---
layout: post
title: "323. Number of Connected Components in an Undirected Graph"
date: 2026-01-07 00:00:00 -0700
categories: [leetcode, medium, graph, bfs, dfs, union-find]
permalink: /2026/01/07/medium-323-number-of-connected-components-in-an-undirected-graph/
tags: [leetcode, medium, graph, bfs, connected-components, undirected-graph]
---

# 323. Number of Connected Components in an Undirected Graph

## Problem Statement

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return *the number of connected components in the graph*.

## Examples

**Example 1:**
```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation:
0 - 1 - 2  (component 1)
3 - 4      (component 2)
```

**Example 2:**
```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
Explanation:
0 - 1 - 2 - 3 - 4  (single component)
```

## Constraints

- `1 <= n <= 2000`
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai <= bi < n`
- `ai != bi`
- There are no repeated edges.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Graph type**: Is the graph directed or undirected? (Assumption: Undirected - edges have no direction, represented as bidirectional)

2. **Connected component definition**: What defines a connected component? (Assumption: A set of nodes where every pair of nodes is connected by a path)

3. **Isolated nodes**: Are isolated nodes (no edges) considered components? (Assumption: Yes - each isolated node is its own component)

4. **Node range**: What is the range of node labels? (Assumption: Nodes are labeled 0 to n-1, where n is number of nodes)

5. **Return value**: What should we return - count or list of components? (Assumption: Return count - integer representing number of connected components)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Use DFS or BFS to traverse the graph. Start from an unvisited node, mark all reachable nodes as visited. Count how many times we need to start a new traversal (one for each connected component). This approach has O(V + E) time, which is actually optimal, but we can optimize the implementation.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use Union-Find (Disjoint Set Union): initialize each node as its own component. For each edge, union the two nodes if they're in different components. The number of components equals the number of distinct roots. This achieves O(V + E × α(V)) time where α is the inverse Ackermann function, which is nearly constant.

**Step 3: Optimized Solution (8 minutes)**

Use Union-Find with path compression and union by rank: maintain a DSU data structure. Initialize with V components (one per node). For each edge, if the two nodes are in different components, union them and decrement component count. After processing all edges, return the component count. This achieves O(V + E × α(V)) ≈ O(V + E) amortized time, which is optimal. The key insight is that Union-Find efficiently tracks connected components as edges are added, and we can maintain the count incrementally.

## Solution Approach

This problem requires counting the number of **connected components** in an undirected graph. A connected component is a maximal set of nodes where every pair of nodes is connected by a path.

### Key Insights:

1. **Connected Components**: Groups of nodes that are reachable from each other
2. **Graph Traversal**: Use BFS or DFS to explore all nodes in a component
3. **Visited Tracking**: Mark visited nodes to avoid revisiting and to identify new components
4. **Component Counting**: Each unvisited node starts a new component

### Algorithm:

1. **Build adjacency list**: Create graph representation from edges
2. **Initialize visited array**: Track which nodes have been explored
3. **For each unvisited node**:
   - Start BFS/DFS from that node
   - Mark all reachable nodes as visited
   - Increment component count
4. **Return**: Total number of components

## Solutions

### **Solution 1: BFS (Breadth-First Search)**

```cpp
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for(auto& edge: edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        int rtn = 0;
        vector<bool> visited(n);
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                bfs(adj, i, visited);
                rtn++;
            }
        }
        return rtn;
    }
private:
    void bfs(vector<vector<int>>& adj, int u, vector<bool>& visited) {
        queue<int> q;
        q.push(u);
        visited[u] = true;
        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            for(int successor: adj[curr]) {
                if(!visited[successor]) {
                    q.push(successor);
                    visited[successor] = true;
                }
            }
        }
    }
};
```

### **Algorithm Explanation:**

1. **Build Graph (Lines 4-8)**:
   - Create adjacency list of size `n`
   - For each edge `[ai, bi]`, add bidirectional connections
   - Since graph is undirected, add both `adj[ai].push_back(bi)` and `adj[bi].push_back(ai)`

2. **Component Counting (Lines 9-15)**:
   - Initialize visited array and component counter
   - **For each node** from 0 to n-1:
     - If node is unvisited, it starts a new component
     - Call BFS to explore all nodes in this component
     - Mark all reachable nodes as visited
     - Increment component counter

3. **BFS Traversal (Lines 17-28)**:
   - **Initialize**: Create queue, push starting node, mark as visited
   - **While queue not empty**:
     - Remove node from front
     - **For each neighbor**:
       - If neighbor is unvisited, add to queue and mark as visited
   - This explores all nodes reachable from the starting node

### **Why This Works:**

- **BFS explores entire component**: Starting from any node in a component, BFS visits all nodes in that component
- **Visited tracking**: Prevents revisiting nodes and ensures each component is counted once
- **Unvisited nodes = new components**: Each unvisited node must belong to a new component
- **Bidirectional edges**: Adding both directions ensures we can traverse the undirected graph correctly

### **Example Walkthrough:**

**For `n = 5, edges = [[0,1],[1,2],[3,4]]`:**

```
Graph structure:
0 - 1 - 2  (component 1)
3 - 4      (component 2)

Initial: visited = [false, false, false, false, false], rtn = 0

Node 0 (unvisited):
  BFS from 0:
    Queue: [0]
    Process 0: visited[0] = true, neighbors [1]
    Queue: [1]
    Process 1: visited[1] = true, neighbors [0, 2]
    Queue: [2] (0 already visited)
    Process 2: visited[2] = true, neighbors [1] (already visited)
    Queue: []
  visited = [true, true, true, false, false]
  rtn = 1

Node 1 (visited): skip

Node 2 (visited): skip

Node 3 (unvisited):
  BFS from 3:
    Queue: [3]
    Process 3: visited[3] = true, neighbors [4]
    Queue: [4]
    Process 4: visited[4] = true, neighbors [3] (already visited)
    Queue: []
  visited = [true, true, true, true, true]
  rtn = 2

Node 4 (visited): skip

Result: 2 components
```

### **Complexity Analysis:**

- **Time Complexity:** O(n + m) where n is number of nodes and m is number of edges
  - Building adjacency list: O(m)
  - BFS visits each node once: O(n)
  - BFS processes each edge once: O(m)
  - Total: O(n + m)
- **Space Complexity:** O(n + m)
  - Adjacency list: O(n + m)
  - Visited array: O(n)
  - Queue: O(n) worst case (one level of nodes)
  - Total: O(n + m)

### **Solution 2: DFS (Depth-First Search)**

```cpp
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for(auto& edge: edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        int rtn = 0;
        vector<bool> visited(n);
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                dfs(adj, i, visited);
                rtn++;
            }
        }
        return rtn;
    }
private:
    void dfs(vector<vector<int>>& adj, int u, vector<bool>& visited) {
        visited[u] = true;
        for(int v: adj[u]) {
            if(!visited[v]) {
                dfs(adj, v, visited);
            }
        }
    }
};
```

### **Complexity Analysis:**

- **Time Complexity:** O(n + m) where n is number of nodes and m is number of edges
  - Building adjacency list: O(m)
  - DFS visits each node once: O(n)
  - DFS processes each edge once: O(m)
  - Total: O(n + m)
- **Space Complexity:** O(n + m)
  - Adjacency list: O(n + m)
  - Visited array: O(n)
  - Recursion stack: O(n) worst case (chain of nodes)
  - Total: O(n + m)

### **Solution 3: Union-Find (Disjoint Set Union)**

```cpp
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        
        for(auto& edge: edges) {
            unite(parent, edge[0], edge[1]);
        }
        
        int rtn = 0;
        for(int i = 0; i < n; i++) {
            if(parent[i] == i) rtn++;
        }
        return rtn;
    }
private:
    int find(vector<int>& parent, int x) {
        if(parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }
    
    void unite(vector<int>& parent, int a, int b) {
        parent[find(parent, a)] = find(parent, b);
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Line 3-4)**:
   - Create parent array of size `n`
   - Initialize each node as its own parent using `iota()` (parent[i] = i)

2. **Union Edges (Lines 6-8)**:
   - For each edge `[a, b]`, unite nodes `a` and `b`
   - This merges the components containing `a` and `b`

3. **Count Components (Lines 10-13)**:
   - Count nodes where `parent[i] == i`
   - These are the root nodes, each representing one component

4. **Find Operation (Lines 16-20)**:
   - Recursively find the root of a node
   - **Path compression**: Set `parent[x] = find(parent, parent[x])` to flatten the tree
   - This makes future find operations faster

5. **Unite Operation (Lines 22-24)**:
   - Find roots of both nodes
   - Set one root's parent to the other root
   - This merges the two components

### **Why This Works:**

- **Union-Find groups components**: All nodes in a component share the same root
- **Path compression**: Makes find operations nearly O(1) amortized
- **Root counting**: Each root represents one component
- **No graph building needed**: Works directly with edge list

### **Complexity Analysis:**

- **Time Complexity:** O(n × α(n) + m × α(n)) ≈ O(n + m) where α is the inverse Ackermann function
  - **Initialization**: O(n) - setting up parent array
  - **Union operations**: O(m × α(n)) - for each edge, find and unite operations
    - `find()` with path compression: O(α(n)) amortized
    - `unite()` calls `find()` twice: O(α(n)) amortized
  - **Component counting**: O(n × α(n)) - find root for each node
  - **Total**: O(n × α(n) + m × α(n)) ≈ O(n + m) since α(n) < 5 for practical values
- **Space Complexity:** O(n)
  - Parent array: O(n)
  - No additional data structures needed
  - Recursion stack for find: O(n) worst case, but path compression limits depth

**Note:** The inverse Ackermann function α(n) grows extremely slowly. For all practical purposes, α(n) ≤ 5, making Union-Find operations effectively constant time.

### **Comparison of All Solutions:**

| Approach | Time Complexity | Space Complexity | Advantages |
|----------|----------------|-----------------|------------|
| BFS | O(n + m) | O(n + m) | Level-by-level exploration, intuitive |
| DFS | O(n + m) | O(n + m) | Recursive, simpler code |
| Union-Find | O(n + m) | O(n) | Most space efficient, no graph building |

## Key Insights

1. **Connected Components**: Groups of nodes reachable from each other
2. **Graph Traversal**: BFS/DFS explores all nodes in a component
3. **Visited Tracking**: Essential to avoid revisiting and count components correctly
4. **Unvisited = New Component**: Each unvisited node starts a new component

## Related Problems

- [LC 547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/) - Same problem with adjacency matrix
- [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) - Connected components in grid
- [LC 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/) - Find edge that creates cycle
- [LC 1319: Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) - Connect components

---

*This problem demonstrates the fundamental pattern for counting connected components using graph traversal algorithms.*

