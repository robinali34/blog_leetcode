---
layout: post
title: "[Medium] 802. Find Eventual Safe States"
date: 2026-01-15 00:00:00 -0700
categories: [leetcode, medium, graph, dfs, cycle-detection]
permalink: /2026/01/15/medium-802-find-eventual-safe-states/
tags: [leetcode, medium, graph, dfs, cycle-detection, three-state-coloring]
---
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

## Thinking Process

1. **Safe Nodes**: Nodes that don't lead to cycles and eventually reach terminal nodes

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
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **Safe Nodes**: Nodes that don't lead to cycles and eventually reach terminal nodes

**How the code works:**
1. **Safe Nodes**: Nodes that don't lead to cycles and eventually reach terminal nodes
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `graph = [[1,2],[2,3],[5],[0],[5],[],[]]`, expected output `[2,4,5,6]`:

The graph is shown above.
Nodes 5 and 6 are terminal nodes, and every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

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
## Common Mistakes

1. **All terminal nodes**: `graph = [[],[],[]]` → return `[0,1,2]`
2. **All nodes in cycle**: `graph = [[1],[0]]` → return `[]`
3. **Single node**: `graph = [[]]` → return `[0]`
4. **Disconnected components**: Some safe, some unsafe
5. **Self-loops**: Node pointing to itself is unsafe

1. **Not detecting cycles correctly**: Forgetting to check if node is "visiting"
2. **Incorrect state transitions**: Not marking node as safe after checking neighbors
3. **Not handling terminal nodes**: Terminal nodes should be automatically safe
4. **Wrong return condition**: Returning `false` when encountering visiting node
5. **Not sorting result**: Result should be sorted in ascending order

## Related Problems

- [LC 207: Course Schedule](https://www.leetcode.com/problems/course-schedule/) - Cycle detection in directed graph
- [LC 210: Course Schedule II](https://www.leetcode.com/problems/course-schedule-ii/) - Topological sort ordering
- [LCR 113: Course Schedule II (CN)](https://robinali34.github.io/blog_leetcode/2026/01/14/medium-lcr113-course-schedule-ii/) - DFS with three-state coloring
- [LC 310: Minimum Height Trees](https://robinali34.github.io/blog_leetcode/2026/01/14/medium-310-minimum-height-trees/) - Graph traversal, BFS/DFS
- [LC 269: Alien Dictionary](https://robinali34.github.io/blog_leetcode/2026/01/14/hard-269-alien-dictionary/) - Topological sort

## Key Takeaways

1. **Safe Nodes**: Nodes that don't lead to cycles and eventually reach terminal nodes
2. **Three-State Coloring**: Efficient way to detect cycles and memoize safe nodes
3. **Terminal Nodes**: Automatically safe (no outgoing edges)
4. **Cycle Detection**: If we encounter a "visiting" node during DFS, cycle exists
5. **Memoization**: Once a node is determined safe, reuse the result

## References

- [LC 802: Find Eventual Safe States on LeetCode](https://www.leetcode.com/problems/find-eventual-safe-states/)
- [LeetCode Discuss — LC 802: Find Eventual Safe States](https://www.leetcode.com/problems/find-eventual-safe-states/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-eventual-safe-states/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
