---
layout: post
title: "[Medium] 1443. Minimum Time to Collect All Apples in a Tree"
date: 2025-10-20 13:45:00 -0700
categories: leetcode algorithm medium tree dfs bfs graph
permalink: /2025/10/20/medium-1443-minimum-time-to-collect-all-apples-in-a-tree/
---
**Difficulty:** Medium  
**Category:** Tree, DFS, BFS, Graph

Given an undirected tree consisting of `n` vertices numbered from `0` to `n-1`, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array `edges`, where `edges[i] = [ai, bi]` means that exists an edge connecting the vertices `ai` and `bi`. Additionally, there is a boolean array `hasApple`, where `hasApple[i] = true` means that vertex `i` has an apple; otherwise, vertex `i` does not have any apple.

## Examples

### Example 1:
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
```

### Example 2:
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
```

### Example 3:
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
```

## Constraints

- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai < bi < n`
- `fromi < toi`
- `hasApple.length == n`

## Thinking Process

This problem can be solved using either **DFS** or **BFS** approaches. The key insight is that we only need to visit subtrees that contain apples or lead to apples.

### DFS Approach (Optimal):
1. **Build adjacency list** from edges
2. **DFS from root (0)** with parent tracking to avoid cycles
3. **For each subtree**, calculate time needed if it contains apples
4. **Return total time** including 2 seconds per edge (going and coming back)

### BFS Approach:
1. **Build adjacency list** and **parent mapping** using BFS
2. **For each apple node**, trace path back to root
3. **Count edges** in the path, avoiding duplicates
4. **Return total time** (2 seconds per unique edge)

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

### Approach 1: DFS (Optimal)

```cpp
class Solution {
private:
    int dfs(vector<vector<int>>& adj, vector<bool>& hasApple, int node, int parent) {
        int totalTime = 0;
        for(auto& child: adj[node]) {
            if(child == parent) continue;
            int childTime = dfs(adj, hasApple, child, node);
            if(childTime > 0 || hasApple[child]) totalTime += childTime + 2;
        }
        return totalTime;
    }
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<int>> adj(n);
        for(auto& edge: edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        return dfs(adj, hasApple, 0, -1);
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** This problem can be solved using either **DFS** or **BFS** approaches. The key insight is that we only need to visit subtrees that contain apples or lead to apples.

**How the code works:**
1. **Build adjacency list** from edges
2. **DFS from root (0)** with parent tracking to avoid cycles
3. **For each subtree**, calculate time needed if it contains apples
4. **Return total time** including 2 seconds per edge (going and coming back)
1. **Build adjacency list** and **parent mapping** using BFS
2. **For each apple node**, trace path back to root
## Which Approach is More Optimal?

**DFS Approach is more optimal** for the following reasons:

1. **Single Pass:** DFS solves the problem in one traversal
2. **No Extra Data Structures:** Doesn't need parent array or visited set
3. **Cleaner Logic:** Directly calculates time during traversal
4. **Better Space Usage:** Only uses recursion stack vs multiple arrays
5. **More Intuitive:** Naturally handles the tree structure

**BFS Approach Trade-offs:**
- **Two Passes:** Requires BFS + path tracing
- **More Memory:** Uses parent array and visited set
- **Complex Logic:** More complex path tracing logic

## References

- [LC 1443: Minimum Time to Collect All Apples in a Tree on LeetCode](https://www.leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/)
- [LeetCode Discuss — LC 1443: Minimum Time to Collect All Apples in a Tree](https://www.leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Tree Structure:** Undirected tree with n-1 edges
2. **Edge Cost:** Each edge costs 2 seconds (going + coming back)
3. **Optimal Path:** Only visit edges that lead to apples
4. **DFS Advantage:** Natural fit for tree traversal problems
5. **Parent Tracking:** Essential to avoid cycles in undirected graph
