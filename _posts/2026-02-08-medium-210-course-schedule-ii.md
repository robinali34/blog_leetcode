---
layout: post
title: "[Medium] 210. Course Schedule II"
date: 2026-02-08 00:00:00 -0700
categories: [leetcode, medium, graph, topological-sort]
permalink: /2026/02/08/medium-210-course-schedule-ii/
tags: [leetcode, medium, graph, topological-sort]
---
You have `numCourses` courses labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` means you must take course `bi` before course `ai`. Return any valid ordering of courses to finish all of them, or an empty array if it is impossible.

## Examples

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: To take course 1 you must take course 0 first. So [0,1] is valid.
```

**Example 2:**

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] (or [0,1,2,3], etc.)
Explanation: 0 has no prereq; 1 and 2 depend on 0; 3 depends on 1 and 2.
```

**Example 3:**

```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`; all pairs are distinct

## Thinking Process

1. **Prerequisite = edge:** `[a, b]` means `b → a` in the graph; topological order has predecessors before successors.

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
| **BFS / DFS traversal** *(this problem)* | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| Union-Find (DSU) | O(α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |

## Solution

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> color(numCourses, 0); // 0: unvisited, 1: visiting, 2: visited
        vector<int> order;
        bool valid = true;
        for (auto& p : prerequisites) {
            adj[p[1]].emplace_back(p[0]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (color[i] == 0) dfs(i, adj, color, order, valid);
        }
        if (!valid) return {};
        reverse(order.begin(), order.end());
        return order;
    }

private:
    void dfs(int u, vector<vector<int>>& adj, vector<int>& color, vector<int>& order, bool& valid) {
        color[u] = 1;
        for (int v : adj[u]) {
            if (color[v] == 0) {
                dfs(v, adj, color, order, valid);
                if (!valid) return;
            } else if (color[v] == 1) {
                valid = false;
                return;
            }
        }
        color[u] = 2;
        order.emplace_back(u);
    }
};
```

### Solution Explanation

**Approach:** BFS / DFS traversal (this problem)

**Key idea:** 1. **Prerequisite = edge:** `[a, b]` means `b → a` in the graph; topological order has predecessors before successors.

**How the code works:**
1. **Prerequisite = edge:** `[a, b]` means `b → a` in the graph; topological order has predecessors before successors.
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `numCourses = 2, prerequisites = [[1,0]]`, expected output `[0,1]`:

To take course 1 you must take course 0 first. So [0,1] is valid.

**Time:** O(V + E). **Space:** O(V).
## Comparison

| Approach        | Idea                    | Cycle check              |
|----------------|-------------------------|---------------------------|
| DFS + coloring | Finish order → reverse  | Back edge (color == 1)    |
| Kahn (BFS)     | Indegree 0 → order      | order.size() != numCourses |

## Related Problems

- [207. Course Schedule](https://www.leetcode.com/problems/course-schedule/) — Only check if a valid order exists
- [269. Alien Dictionary](https://www.leetcode.com/problems/alien-dictionary/) — Topological sort from character constraints

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Prerequisite = edge:** `[a, b]` means `b → a` in the graph; topological order has predecessors before successors.
2. **DFS order:** Finishing order is reverse topological; one reverse gives a valid schedule.
3. **Kahn:** No need to reverse; order is built in topological order as we dequeue.

## References

- [LC 210: Course Schedule II on LeetCode](https://www.leetcode.com/problems/course-schedule-ii/)
- [LeetCode Discuss — LC 210: Course Schedule II](https://www.leetcode.com/problems/course-schedule-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/course-schedule-ii/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
