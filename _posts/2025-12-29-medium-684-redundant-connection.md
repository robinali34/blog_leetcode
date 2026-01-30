---
layout: post
title: "684. Redundant Connection"
date: 2025-12-29 14:30:00 -0700
categories: [leetcode, medium, union-find, dsu, graph, cycle-detection, dfs]
permalink: /2025/12/29/medium-684-redundant-connection/
---

# 684. Redundant Connection

## Problem Statement

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return *an edge that can be removed so that the resulting graph is a tree of `n` nodes*. If there are multiple answers, return the answer that occurs **last** in the input.

## Examples

**Example 1:**
```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Explanation: The edge [2,3] creates a cycle, so it should be removed.
```

**Example 2:**
```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
Explanation: The edge [1,4] creates a cycle, so it should be removed.
```

## Constraints

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ai < bi <= edges.length`
- `ai != bi`
- There are no repeated edges.
- The given graph is connected.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Redundant edge definition**: What makes an edge redundant? (Assumption: An edge that creates a cycle in an otherwise tree structure - the edge that forms the cycle)

2. **Graph type**: Is the graph directed or undirected? (Assumption: Undirected - edges have no direction)

3. **Tree property**: What is the base structure? (Assumption: Graph with n nodes and n edges - one extra edge makes it not a tree)

4. **Return format**: What should we return if multiple redundant edges exist? (Assumption: Return the last edge in the input array that creates a cycle)

5. **Edge representation**: How are edges represented? (Assumption: [ai, bi] where ai and bi are node labels, 1-indexed per constraints)

## Solution Approach

This problem requires finding the edge that creates a cycle in an undirected graph. Since the graph started as a tree (connected, no cycles) and one edge was added, there is exactly one cycle. We need to find and return the redundant edge.

### Key Insights:

1. **Cycle Detection**: The redundant edge is the one that connects two nodes already in the same connected component
2. **Union-Find (DSU)**: Efficiently detect cycles by checking if two nodes are already connected before adding an edge
3. **DFS Approach**: Build graph and use DFS to detect cycles, then find the last edge in the cycle
4. **Last Edge Priority**: If multiple edges form cycles, return the one that appears last in the input

### Algorithm Options:

1. **DSU Approach**: Process edges in order, return first edge that connects already-connected nodes
2. **DFS Approach**: Build graph, find cycle, return last edge in cycle that appears in input

## Solution 1: Union-Find (DSU) - Recommended

### **Solution: DSU with Union by Rank**

```cpp
class DSU{
private:
    vector<int> parent;
    vector<int> rank;

public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if(parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if(x == y) return false;

        if(rank[x] < rank[y]) {
            parent[x] = y;
        } else if(rank[x] > rank[y]) {
            parent[y] = x;
        } else {
            parent[y] = x;
            rank[x]++;
        }
        return true;
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        const int n = edges.size();
        DSU dsu(n);

        for(const auto& edge: edges) {
            if(!dsu.unite(edge[0] - 1, edge[1] - 1)) {
                return edge;
            }
        }
        return {};
    }
};
```

### **Algorithm Explanation:**

1. **DSU Initialization (Lines 8-15)**:
   - `parent[i] = i`: Each node is its own parent initially
   - `rank[i] = 0`: All trees start with rank 0

2. **Find with Path Compression (Lines 17-22)**:
   - Recursively find root parent
   - Path compression: `parent[x] = find(parent[x])` flattens tree
   - Returns root of the set containing `x`

3. **Union by Rank (Lines 24-38)**:
   - Find roots of both nodes
   - If same root: already connected → return `false` (cycle detected!)
   - If different roots: merge sets using union by rank
   - Attach smaller tree to larger tree to keep balanced

4. **Main Solution (Lines 41-51)**:
   - Process edges in order
   - Convert 1-based to 0-based indexing: `edge[0] - 1, edge[1] - 1`
   - If `unite` returns `false`: nodes already connected → cycle found!
   - Return the redundant edge immediately

### **Example Walkthrough:**

**For `edges = [[1,2],[1,3],[2,3]]`:**

```
Initial: parent = [0,1,2], rank = [0,0,0]

Edge [1,2]: unite(0, 1)
- find(0) = 0, find(1) = 1 (different roots)
- rank[0] == rank[1] → parent[1] = 0, rank[0]++
- parent = [0,0,2], rank = [1,0,0]
- Return true (no cycle)

Edge [1,3]: unite(0, 2)
- find(0) = 0, find(2) = 2 (different roots)
- rank[0] > rank[2] → parent[2] = 0
- parent = [0,0,0], rank = [1,0,0]
- Return true (no cycle)

Edge [2,3]: unite(1, 2)
- find(1) = 0, find(2) = 0 (same root!)
- Return false → CYCLE DETECTED!
- Return [2,3]
```

## Solution 2: DFS Cycle Detection

### **Solution: DFS to Find Cycle**

```cpp
class Solution {
private:
    int cycleStart = -1;
    void dfs(int src, vector<bool>& visited, vector<vector<pair<int, int>>> adjList, vector<int>& parent) {
        visited[src] = true;
        for(auto& p : adjList[src]) {
            int adj = p.first;
            if(!visited[adj]) {
                parent[adj] = src;
                dfs(adj, visited, adjList, parent);
            } else if(adj != parent[src] && cycleStart == -1) {
                cycleStart = adj;
                parent[adj] = src;
            }
        }
    }

public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        const int n = edges.size();
        vector<bool> visited(n, false);
        vector<int> parent(n, -1);
        vector<vector<pair<int, int>>> adjList(n);
        for(auto& edge: edges) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            adjList[u].push_back({v, 0});
            adjList[v].push_back({u, 0});
        }
        dfs(0, visited, adjList, parent);
        unordered_map<int, int> cycleNode;
        int node = cycleStart;
        do {
            cycleNode[node] = 1;
            node = parent[node];
        } while (node != cycleStart);
        for(int i = edges.size() - 1; i >= 0; i--) {
            if(cycleNode[edges[i][0] - 1] &&
            cycleNode[edges[i][1] - 1]) {
                return edges[i];
            }
        }
        return {};
    }
};
```

### **Algorithm Explanation:**

1. **Graph Construction (Lines 25-32)**:
   - Build adjacency list from edges
   - Convert 1-based to 0-based indexing
   - Store bidirectional edges

2. **DFS Cycle Detection (Lines 4-16)**:
   - Perform DFS from node 0
   - Track parent for each node
   - If visiting an already-visited node that's not the parent: cycle found!
   - Mark `cycleStart` when cycle detected

3. **Cycle Extraction (Lines 33-38)**:
   - Start from `cycleStart`
   - Follow parent pointers to extract all nodes in cycle
   - Store cycle nodes in `cycleNode` map

4. **Find Last Edge in Cycle (Lines 39-44)**:
   - Iterate edges from end to beginning
   - Find first edge where both endpoints are in cycle
   - Return that edge (last in input order)

### **Example Walkthrough:**

**For `edges = [[1,2],[1,3],[2,3]]`:**

```
Graph:
1 -- 2
|    |
3 ---|

DFS from node 0:
- Visit 0 (node 1), parent[0] = -1
- Visit 1 (node 2), parent[1] = 0
- Visit 2 (node 3), parent[2] = 1
- From 2, try to visit 0 (node 1)
  - 0 is visited and 0 != parent[2] (1) → CYCLE!
  - cycleStart = 0

Extract cycle:
- Start from 0: cycleNode[0] = 1
- parent[0] = -1? No, wait... parent[0] was set to 2 in cycle detection
- Follow: 0 → 2 → 1 → 0
- cycleNode = {0, 1, 2}

Find last edge in cycle:
- Check edges from end: [2,3] → nodes 1,2 both in cycle → Return [2,3]
```

## DSU Template

Here's the general template for Union-Find (DSU) with union by rank:

```cpp
class DSU {
private:
    vector<int> parent;
    vector<int> rank;

public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    // Find with path compression
    int find(int x) {
        if(parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    // Union by rank
    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if(x == y) return false; // Already in same set

        // Union by rank: attach smaller tree to larger tree
        if(rank[x] < rank[y]) {
            parent[x] = y;
        } else if(rank[x] > rank[y]) {
            parent[y] = x;
        } else {
            parent[y] = x;
            rank[x]++;
        }
        return true;
    }

    // Check if two nodes are connected
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};
```

### **Key Template Components:**

1. **Data Structures**:
   - `parent[i]`: Parent of node `i` (root if `parent[i] == i`)
   - `rank[i]`: Approximate depth of tree rooted at `i`

2. **Path Compression**:
   - Flattens tree during find operation
   - Makes future finds faster

3. **Union by Rank**:
   - Keeps trees balanced
   - Attaches smaller tree to larger tree
   - Only increases rank when ranks are equal

4. **Time Complexity**:
   - Nearly O(1) per operation (inverse Ackermann function)
   - O(α(n)) where α grows extremely slowly

## Complexity Analysis

### **Solution 1: DSU**

**Time Complexity:** O(n × α(n)) ≈ O(n)
- **DSU operations**: O(α(n)) per operation (nearly constant)
- **Process n edges**: O(n × α(n))
- **Total**: O(n) for practical purposes

**Space Complexity:** O(n)
- **Parent array**: O(n)
- **Rank array**: O(n)
- **Total**: O(n)

### **Solution 2: DFS**

**Time Complexity:** O(n)
- **Graph construction**: O(n)
- **DFS traversal**: O(n) - visit each node once
- **Cycle extraction**: O(n) - worst case
- **Edge search**: O(n) - check all edges
- **Total**: O(n)

**Space Complexity:** O(n)
- **Adjacency list**: O(n)
- **Visited array**: O(n)
- **Parent array**: O(n)
- **Cycle node map**: O(n)
- **DFS recursion stack**: O(n)
- **Total**: O(n)

## Key Points

1. **DSU is Optimal**: Union-Find is the most efficient approach for cycle detection
2. **Path Compression**: Speeds up find operations significantly
3. **Union by Rank**: Keeps trees balanced for better performance
4. **1-based to 0-based**: Convert node indices when using DSU
5. **Last Edge Priority**: Problem asks for last edge in input that creates cycle
6. **Single Cycle**: Graph has exactly one cycle (one extra edge in tree)

## Comparison: DSU vs DFS

| Aspect | DSU | DFS |
|--------|-----|-----|
| **Time Complexity** | O(n × α(n)) ≈ O(n) | O(n) |
| **Space Complexity** | O(n) | O(n) |
| **Implementation** | Simpler | More complex |
| **Cycle Detection** | Direct (during union) | Requires traversal |
| **Edge Order** | Natural (process in order) | Need to track and search |
| **Recommended** | ✅ Yes | ⚠️ Works but more complex |

## Alternative Approaches

### **Approach 1: DSU (Current Solution 1)**
- **Time**: O(n × α(n)) ≈ O(n)
- **Space**: O(n)
- **Best for**: Cycle detection in undirected graphs

### **Approach 2: DFS (Current Solution 2)**
- **Time**: O(n)
- **Space**: O(n)
- **Use case**: When you need to extract full cycle information

### **Approach 3: BFS Cycle Detection**
- **Time**: O(n)
- **Space**: O(n)
- **Similar to DFS**: Can detect cycles but more complex

## Related Problems

- [685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) - Directed graph version
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) - Count connected components
- [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) - DSU for merging accounts
- [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) - DSU for connectivity

## Tags

`Union-Find`, `DSU`, `Disjoint Set Union`, `Graph`, `Cycle Detection`, `DFS`, `Medium`

