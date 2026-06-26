---
layout: post
title: "[Medium] LCR 113. Course Schedule II"
date: 2026-01-14 00:00:00 -0700
categories: [leetcode, medium, graph, topological-sort, dfs]
permalink: /2026/01/14/medium-lcr113-course-schedule-ii/
tags: [leetcode, medium, graph, topological-sort, dfs, cycle-detection]
---
# LCR 113. Course Schedule II

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

Return *the ordering of courses you should take to finish all courses*. If there are many valid answers, return **any of them**. If it is impossible to finish all courses, return **an empty array**.

## Examples

**Example 1:**
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

**Example 2:**
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: []
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

**Example 3:**
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: One correct course order is [0,2,1,3]. Another correct ordering is [0,1,2,3].
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- All the pairs `[ai, bi]` are **distinct**.

## Thinking Process

1. **Reverse Graph**: Building graph in reverse allows direct return of DFS path

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

### **Solution: DFS with Three-State Coloring**

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        adj.resize(numCourses);
        visited.resize(numCourses, 0);
        for(const auto& info: prerequisites) {
            // Build reverse order, so the DFS path can be directed returned
            adj[info[0]].emplace_back(info[1]);
        }
        // DFS on each un-visited node
        for(int i = 0; i < numCourses && isValid; i++) {
            if(visited[i] == 0) {
                dfs(i);
            }
        }
        if(!isValid) return{};
        return rtn;
    }
private:
    vector<vector<int>> adj;
    vector<int> visited;
    vector<int> rtn;
    bool isValid = true;

    void dfs(int u) {
        visited[u] = 1;  // Mark as visiting
        for(int v: adj[u]) {
            if(visited[v] == 0) {
                dfs(v);
                if(!isValid) return;
            } else if(visited[v] == 1) {
                isValid = false;  // Cycle detected
                return;
            } 
        }
        visited[u] = 2;  // Mark as visited
        rtn.emplace_back(u);  // Add to result (post-order)
    }
};
```

### Solution Explanation

**Approach:** BFS / DFS traversal (this problem)

**Key idea:** 1. **Reverse Graph**: Building graph in reverse allows direct return of DFS path

**How the code works:**
1. **Reverse Graph**: Building graph in reverse allows direct return of DFS path
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `numCourses = 2, prerequisites = [[1,0]]`, expected output `[0,1]`:

There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

### **Algorithm Explanation:**

1. **Graph Construction (Lines 6-10)**:
   - Build **reverse graph**: `adj[info[0]]` contains `info[1]`
   - This means `info[0]` depends on `info[1]` (info[1] must come before info[0])
   - Reverse graph allows direct return of DFS path as topological order

2. **DFS from Each Node (Lines 11-16)**:
   - For each unvisited node (`visited[i] == 0`), start DFS
   - Early termination if cycle detected (`!isValid`)

3. **DFS Function (Lines 25-38)**:
   - **Mark as Visiting (Line 26)**: `visited[u] = 1`
   - **Process Neighbors (Lines 27-33)**:
     - If unvisited (`visited[v] == 0`), recurse
     - If visiting (`visited[v] == 1`), **cycle detected** → set `isValid = false`
     - If visited (`visited[v] == 2`), skip (already processed)
   - **Mark as Visited (Line 34)**: `visited[u] = 2`
   - **Add to Result (Line 35)**: Post-order addition ensures dependencies come first

4. **Return Result (Lines 17-18)**:
   - If cycle found, return empty array
   - Otherwise, return topological order

### **Why Reverse Graph Works:**

- **Normal Graph**: `adj[bi]` contains `ai` → DFS gives reverse topological order (need to reverse)
- **Reverse Graph**: `adj[ai]` contains `bi` → DFS directly gives correct topological order
- **Post-order Addition**: Adding nodes after processing dependencies ensures correct order

### **Example Walkthrough:**

**Input:** `numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`

```
Step 1: Build Reverse Graph
  adj[1] = [0]  (1 depends on 0)
  adj[2] = [0]  (2 depends on 0)
  adj[3] = [1, 2]  (3 depends on 1 and 2)

Step 2: DFS from node 0
  visited[0] = 1 (visiting)
  adj[0] is empty
  visited[0] = 2 (visited)
  rtn = [0]

Step 3: DFS from node 1
  visited[1] = 1 (visiting)
  Check neighbor 0: visited[0] = 2 (visited) → skip
  visited[1] = 2 (visited)
  rtn = [0, 1]

Step 4: DFS from node 2
  visited[2] = 1 (visiting)
  Check neighbor 0: visited[0] = 2 (visited) → skip
  visited[2] = 2 (visited)
  rtn = [0, 1, 2]

Step 5: DFS from node 3
  visited[3] = 1 (visiting)
  Check neighbor 1: visited[1] = 2 (visited) → skip
  Check neighbor 2: visited[2] = 2 (visited) → skip
  visited[3] = 2 (visited)
  rtn = [0, 1, 2, 3]

Result: [0, 1, 2, 3] ✓
```

**With Cycle Example:** `numCourses = 2, prerequisites = [[1,0],[0,1]]`

```
Step 1: Build Reverse Graph
  adj[1] = [0]
  adj[0] = [1]

Step 2: DFS from node 0
  visited[0] = 1 (visiting)
  Check neighbor 1: visited[1] = 0 (unvisited) → recurse
  
  DFS from node 1:
    visited[1] = 1 (visiting)
    Check neighbor 0: visited[0] = 1 (visiting) → CYCLE DETECTED!
    isValid = false
    return

Result: [] (empty array) ✓
```

### **Complexity Analysis:**

- **Time Complexity:** O(V + E)
  - Building graph: O(E)
  - DFS traversal: O(V + E)
  - Overall: O(V + E)
- **Space Complexity:** O(V + E)
  - Adjacency list: O(V + E)
  - Visited array: O(V)
  - Result array: O(V)
  - Recursion stack: O(V) worst case
  - Overall: O(V + E)
## Common Mistakes

1. **No prerequisites**: `prerequisites = []` → return `[0,1,2,...,n-1]` (any order)
2. **Single course**: `numCourses = 1` → return `[0]`
3. **Cycle exists**: Return empty array `[]`
4. **Linear chain**: `[[1,0],[2,1],[3,2]]` → return `[0,1,2,3]`
5. **Multiple valid orders**: Any valid topological order is acceptable

1. **Wrong graph direction**: Building normal graph instead of reverse
2. **Not detecting cycles**: Forgetting to check for visiting nodes
3. **Wrong addition order**: Adding nodes in pre-order instead of post-order
4. **Not handling all nodes**: Forgetting to DFS from all unvisited nodes
5. **State management**: Not properly updating visited states

## Related Problems

- [LC 207: Course Schedule](https://www.leetcode.com/problems/course-schedule/) - Check if courses can be finished
- [LC 210: Course Schedule II](https://www.leetcode.com/problems/course-schedule-ii/) - Same problem (English version)
- [LC 269: Alien Dictionary](https://www.leetcode.com/problems/alien-dictionary/) - Topological sort for character ordering
- [LC 310: Minimum Height Trees](https://www.leetcode.com/problems/minimum-height-trees/) - Peeling leaves pattern

## Reference

- Problem Link: [LCR 113. Course Schedule II](https://leetcode.cn/problems/QA2IGt/description/)

## Key Takeaways

1. **Reverse Graph**: Building graph in reverse allows direct return of DFS path
2. **Three-State Coloring**: `0=unvisited`, `1=visiting`, `2=visited` enables cycle detection
3. **Post-order Addition**: Add nodes after processing dependencies for correct order
4. **Cycle Detection**: Encountering a "visiting" node indicates a back edge (cycle)
5. **Early Termination**: Stop DFS immediately when cycle detected

## References

- [LC 113 on LeetCode](https://www.leetcode.com/problems/course-schedule-ii/)
- [LeetCode Discuss — LC 113](https://www.leetcode.com/problems/course-schedule-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/course-schedule-ii/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
