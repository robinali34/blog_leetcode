---
layout: post
title: "310. Minimum Height Trees"
date: 2026-01-14 00:00:00 -0700
categories: [leetcode, medium, graph, tree, topological-sort, bfs]
permalink: /2026/01/14/medium-310-minimum-height-trees/
tags: [leetcode, medium, graph, tree, topological-sort, bfs, peeling-leaves]
---

# 310. Minimum Height Trees

## Problem Statement

A tree is an undirected graph in which any two vertices are connected by **exactly** one path. In other words, any connected graph without simple cycles is a tree.

You are given a tree of `n` nodes labelled from `0` to `n - 1`. The tree is represented as an array `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the tree.

Return *the labels of all nodes that are the roots of **minimum height trees (MHTs)***. You can return the answer in **any order**.

A **minimum height tree** is a tree rooted at a node such that the tree has the smallest possible height among all possible rooted trees.

## Examples

**Example 1:**
```
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree when rooted at node 1 is 1, which is the minimum possible.
```

**Example 2:**
```
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
```

## Constraints

- `1 <= n <= 2 * 10^4`
- `edges.length == n - 1`
- `0 <= ai, bi < n`
- `ai != bi`
- All the pairs `(ai, bi)` are distinct.
- The given input is **guaranteed** to be a tree and there will be **no repeated** edges.

## Solution Approach

This problem requires finding the center(s) of a tree. The key insight is that **minimum height trees have their roots at the center(s) of the longest path (diameter) in the tree**.

### Key Insights:

1. **Tree Centers**: A tree has at most 2 centers (nodes at the middle of the longest path)
2. **Peeling Leaves**: Repeatedly remove leaves (nodes with degree 1) until 1 or 2 nodes remain
3. **Topological Sort**: Similar to Kahn's algorithm, process nodes with indegree 1
4. **Remaining Nodes**: The 1 or 2 nodes remaining after peeling are the centers (MHT roots)

### Algorithm:

1. **Build Graph**: Create adjacency list and calculate degrees
2. **Find Leaves**: Initialize queue with all nodes having degree 1
3. **Peel Leaves Iteratively**:
   - Process all leaves at current level
   - Remove leaves and update degrees of neighbors
   - Add new leaves (degree becomes 1) to queue
   - Continue until ≤ 2 nodes remain
4. **Return Centers**: Remaining nodes are the MHT roots

## Solution

### **Solution: Peeling Leaves (Topological Sort)**

```cpp
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        // Essentially it is to find the path with max length, return its central node(s)
        vector<int> rtn;
        if(n == 0) return rtn;
        if(n == 1) return {0};

        // Build the adj list
        vector<vector<int>> adj(n);
        vector<int> inDegree(n, 0);

        for(auto& edge: edges) {
            int u = edge[0], v = edge[1];
            adj[u].emplace_back(v);
            adj[v].emplace_back(u);
            inDegree[u]++;
            inDegree[v]++;
        }

        // Init leaves
        queue<int> leaves;
        for(int i = 0; i < n; i++) {
            if(inDegree[i] == 1) {
                leaves.push(i);
            }
        }

        // Trim leaves until <= 2 nodes remain
        int remainingNodes = n;
        while (remainingNodes > 2) {
            int leavesSize = leaves.size();
            remainingNodes -= leavesSize;
            for(int i = 0; i < leavesSize; i++) {
                int leaf = leaves.front();
                leaves.pop();
                // The leaf has only one neighbor
                for(int neighbor: adj[leaf]) {
                    inDegree[neighbor]--;
                    if(inDegree[neighbor] == 1) {
                        leaves.push(neighbor);
                    }
                }
            }
        }
        
        // Remaining nodes are roots of MHTs
        while(!leaves.empty()) {
            rtn.emplace_back(leaves.front());
            leaves.pop();
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Edge Cases (Lines 5-7)**:
   - If `n == 0`, return empty
   - If `n == 1`, return `[0]` (single node is the center)

2. **Build Graph (Lines 9-19)**:
   - Create adjacency list `adj` for undirected graph
   - Calculate `inDegree` (degree) for each node
   - For each edge `[u, v]`, add both directions and increment degrees

3. **Initialize Leaves (Lines 21-26)**:
   - Find all nodes with `degree == 1` (leaves)
   - Add them to queue for processing

4. **Peel Leaves Iteratively (Lines 28-42)**:
   - **While `remainingNodes > 2`**:
     - Process all leaves at current level (batch processing)
     - For each leaf:
       - Remove it (decrement `remainingNodes`)
       - For each neighbor:
         - Decrement neighbor's degree
         - If neighbor's degree becomes 1, add to queue (new leaf)
   - Continue until ≤ 2 nodes remain

5. **Return Centers (Lines 44-48)**:
   - Remaining nodes in queue are the centers (MHT roots)
   - Return them as result

### **Why This Works:**

- **Tree Centers**: The center(s) of a tree are at the middle of the longest path
- **Peeling Leaves**: Removing leaves doesn't change the center(s) of the tree
- **Convergence**: After peeling, 1 or 2 nodes remain (the centers)
- **MHT Roots**: Centers minimize the maximum distance to any leaf

### **Example Walkthrough:**

**Input:** `n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]`

```
Tree structure:
    0
    |
    3
   /|\
  1 2 4
        \
         5

Step 1: Build Graph
  adj[0] = [3]
  adj[1] = [3]
  adj[2] = [3]
  adj[3] = [0,1,2,4]
  adj[4] = [3,5]
  adj[5] = [4]

  inDegree = [1, 1, 1, 4, 2, 1]

Step 2: Initialize Leaves
  Leaves: [0, 1, 2, 5] (degree = 1)

Step 3: First Iteration (remainingNodes = 6 > 2)
  Process leaves: [0, 1, 2, 5]
  
  Process 0:
    Neighbor: 3
    inDegree[3] = 4 - 1 = 3
    remainingNodes = 6 - 1 = 5
  
  Process 1:
    Neighbor: 3
    inDegree[3] = 3 - 1 = 2
    remainingNodes = 5 - 1 = 4
  
  Process 2:
    Neighbor: 3
    inDegree[3] = 2 - 1 = 1
    remainingNodes = 4 - 1 = 3
  
  Process 5:
    Neighbor: 4
    inDegree[4] = 2 - 1 = 1
    remainingNodes = 3 - 1 = 2
  
  New leaves: [3, 4] (both have degree 1 now)
  Leaves queue: [3, 4]

Step 4: Check Condition
  remainingNodes = 2 ≤ 2 → Stop

Step 5: Return Centers
  Result: [3, 4]
```

**Visual Representation:**
```
Initial:         After 1st iteration:
    0                 
    |                 
    3                 3
   /|\               / \
  1 2 4             4
        \             
         5           

Centers: 3 and 4 (both are valid MHT roots)
```

### **Complexity Analysis:**

- **Time Complexity:** O(n)
  - Building graph: O(n)
  - Peeling leaves: O(n) - each node processed once
  - Overall: O(n)
- **Space Complexity:** O(n)
  - Adjacency list: O(n)
  - Degree array: O(n)
  - Queue: O(n)

## Key Insights

1. **Tree Centers**: At most 2 centers exist (middle of longest path)
2. **Peeling Leaves**: Repeatedly remove leaves until centers remain
3. **Batch Processing**: Process all leaves at same level together
4. **Convergence**: Always converges to 1 or 2 nodes
5. **MHT Roots**: Centers minimize maximum distance to any leaf

## Edge Cases

1. **Single node**: `n = 1` → return `[0]`
2. **Two nodes**: `n = 2, edges = [[0,1]]` → return `[0,1]` (both are centers)
3. **Linear tree**: `n = 4, edges = [[0,1],[1,2],[2,3]]` → return `[1,2]` (middle nodes)
4. **Star tree**: `n = 4, edges = [[0,1],[0,2],[0,3]]` → return `[0]` (center)
5. **Balanced tree**: Returns 1 or 2 centers depending on structure

## Common Mistakes

1. **Not handling single node**: Forgetting edge case `n == 1`
2. **Wrong stopping condition**: Should stop when `remainingNodes <= 2`, not `== 0`
3. **Not batch processing**: Processing leaves one at a time instead of by level
4. **Wrong degree update**: Not updating degrees correctly when removing leaves
5. **Not tracking remaining nodes**: Forgetting to decrement `remainingNodes`

## Alternative Approaches

### **Approach 2: Two-Pass BFS (Find Diameter)**

```cpp
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(n == 1) return {0};
        
        vector<vector<int>> adj(n);
        for(auto& e: edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        // First BFS: Find one end of diameter
        int u = bfs(adj, 0, n).first;
        
        // Second BFS: Find other end and path
        auto [v, parent] = bfs(adj, u, n);
        
        // Find middle node(s) of diameter
        vector<int> path;
        int curr = v;
        while(curr != -1) {
            path.push_back(curr);
            curr = parent[curr];
        }
        
        int len = path.size();
        if(len % 2 == 0) {
            return {path[len/2 - 1], path[len/2]};
        } else {
            return {path[len/2]};
        }
    }
    
private:
    pair<int, vector<int>> bfs(vector<vector<int>>& adj, int start, int n) {
        queue<int> q;
        vector<int> parent(n, -1);
        vector<bool> visited(n, false);
        q.push(start);
        visited[start] = true;
        int farthest = start;
        
        while(!q.empty()) {
            int u = q.front();
            q.pop();
            farthest = u;
            for(int v: adj[u]) {
                if(!visited[v]) {
                    visited[v] = true;
                    parent[v] = u;
                    q.push(v);
                }
            }
        }
        return {farthest, parent};
    }
};
```

**Time Complexity:** O(n) - Two BFS passes  
**Space Complexity:** O(n)

**Comparison:**
- **Peeling Leaves**: More intuitive, easier to implement
- **Two-Pass BFS**: More complex but directly finds diameter

## Related Problems

- [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) - Topological sort
- [LC 210: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Topological sort ordering
- [LC 310: Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) - This problem
- [LC 323: Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) - Graph connectivity

---

*This problem demonstrates the **Peeling Leaves** pattern for finding tree centers. The key insight is that minimum height trees have their roots at the center(s) of the longest path, which can be found by repeatedly removing leaves until 1 or 2 nodes remain.*

