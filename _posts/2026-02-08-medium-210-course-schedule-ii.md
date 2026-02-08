---
layout: post
title: "210. Course Schedule II"
date: 2026-02-08 00:00:00 -0700
categories: [leetcode, medium, graph, topological-sort]
permalink: /2026/02/08/medium-210-course-schedule-ii/
tags: [leetcode, medium, graph, topological-sort]
---

# 210. Course Schedule II

## Problem Statement

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

## Solution Approach

This is **topological sort** on a directed graph: edge `(bi, ai)` means `bi` must come before `ai`. If the graph has a cycle, no valid order exists. Two standard approaches:

1. **DFS + three-state coloring:** 0 = unvisited, 1 = visiting (on stack), 2 = visited. If we see a node with color 1 while DFS, there is a cycle. When we finish a node (color 2), append it to a list; reverse the list to get topological order.
2. **Kahn's algorithm (BFS):** Compute indegree of each node. Repeatedly take a node with indegree 0, add it to the order, and decrease indegree of its neighbors. If the final order has size `numCourses`, no cycle; else return `[]`.

## Solution 1: DFS with Three-State Coloring

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

- **Cycle:** Seeing `color[v] == 1` means `v` is on the current DFS stack → back edge → cycle.
- **Order:** We push a node when we finish it (all descendants done), so the list is **reverse** topological order; one reverse gives a valid order.
- **Time:** O(V + E). **Space:** O(V).

## Solution 2: Kahn's Algorithm (BFS)

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        queue<int> q;
        vector<int> order;

        for (auto& p : prerequisites) {
            adj[p[1]].emplace_back(p[0]);
            indegree[p[0]]++;
        }

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) q.push(i);
        }

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            order.emplace_back(u);
            for (int v : adj[u]) {
                if (--indegree[v] == 0) q.push(v);
            }
        }
        return order.size() == numCourses ? order : vector<int>{};
    }
};
```

- **Indegree:** `indegree[v]` = number of edges into `v`. Process nodes with indegree 0 (no unmet prerequisites).
- **Cycle:** If there is a cycle, some nodes never get indegree 0, so `order.size() < numCourses` → return `[]`.
- **Time:** O(V + E). **Space:** O(V).

## Comparison

| Approach        | Idea                    | Cycle check              |
|----------------|-------------------------|---------------------------|
| DFS + coloring | Finish order → reverse  | Back edge (color == 1)    |
| Kahn (BFS)     | Indegree 0 → order      | order.size() != numCourses |

## Key Insights

1. **Prerequisite = edge:** `[a, b]` means `b → a` in the graph; topological order has predecessors before successors.
2. **DFS order:** Finishing order is reverse topological; one reverse gives a valid schedule.
3. **Kahn:** No need to reverse; order is built in topological order as we dequeue.

## Related Problems

- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) — Only check if a valid order exists
- [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) — Topological sort from character constraints
