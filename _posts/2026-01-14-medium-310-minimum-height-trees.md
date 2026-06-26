---
layout: post
title: "[Medium] 310. Minimum Height Trees"
date: 2026-01-14 00:00:00 -0700
categories: [leetcode, medium, graph, tree, topological-sort, bfs]
permalink: /2026/01/14/medium-310-minimum-height-trees/
tags: [leetcode, medium, graph, tree, topological-sort, bfs, peeling-leaves]
---
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

## Thinking Process

1. **Tree Centers**: At most 2 centers exist (middle of longest path)

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
| **Queue BFS** *(this problem)* | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| Level-order BFS | O(n) | O(w) | Process by depth/layer |

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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** 1. **Tree Centers**: At most 2 centers exist (middle of longest path)

**How the code works:**
1. **Tree Centers**: At most 2 centers exist (middle of longest path)
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `n = 4, edges = [[1,0],[1,2],[1,3]]`, expected output `[1]`:

As shown, the height of the tree when rooted at node 1 is 1, which is the minimum possible.

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
## Common Mistakes

1. **Single node**: `n = 1` → return `[0]`
2. **Two nodes**: `n = 2, edges = [[0,1]]` → return `[0,1]` (both are centers)
3. **Linear tree**: `n = 4, edges = [[0,1],[1,2],[2,3]]` → return `[1,2]` (middle nodes)
4. **Star tree**: `n = 4, edges = [[0,1],[0,2],[0,3]]` → return `[0]` (center)
5. **Balanced tree**: Returns 1 or 2 centers depending on structure

1. **Not handling single node**: Forgetting edge case `n == 1`
2. **Wrong stopping condition**: Should stop when `remainingNodes <= 2`, not `== 0`
3. **Not batch processing**: Processing leaves one at a time instead of by level
4. **Wrong degree update**: Not updating degrees correctly when removing leaves
5. **Not tracking remaining nodes**: Forgetting to decrement `remainingNodes`

## Related Problems

- [LC 207: Course Schedule](https://www.leetcode.com/problems/course-schedule/) - Topological sort
- [LC 210: Course Schedule II](https://www.leetcode.com/problems/course-schedule-ii/) - Topological sort ordering
- [LC 310: Minimum Height Trees](https://www.leetcode.com/problems/minimum-height-trees/) - This problem
- [LC 323: Number of Connected Components](https://www.leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) - Graph connectivity

## Key Takeaways

1. **Tree Centers**: At most 2 centers exist (middle of longest path)
2. **Peeling Leaves**: Repeatedly remove leaves until centers remain
3. **Batch Processing**: Process all leaves at same level together
4. **Convergence**: Always converges to 1 or 2 nodes
5. **MHT Roots**: Centers minimize maximum distance to any leaf

## References

- [LC 310: Minimum Height Trees on LeetCode](https://www.leetcode.com/problems/minimum-height-trees/)
- [LeetCode Discuss — LC 310: Minimum Height Trees](https://www.leetcode.com/problems/minimum-height-trees/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-height-trees/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
