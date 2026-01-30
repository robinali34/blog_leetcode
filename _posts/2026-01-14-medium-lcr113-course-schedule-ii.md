---
layout: post
title: "LCR 113. Course Schedule II"
date: 2026-01-14 00:00:00 -0700
categories: [leetcode, medium, graph, topological-sort, dfs]
permalink: /2026/01/14/medium-lcr113-course-schedule-ii/
tags: [leetcode, medium, graph, topological-sort, dfs, cycle-detection]
---

# LCR 113. Course Schedule II

## Problem Statement

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

## Solution Approach

This problem is similar to [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/), but instead of just checking if all courses can be completed, we need to return the actual ordering. This is a **topological sort** problem on a directed graph.

### Key Insights:

1. **Graph Representation**: Courses are nodes, prerequisites are directed edges
2. **Reverse Graph**: Build graph in reverse order (`adj[ai]` contains `bi`) so DFS path can be directly returned
3. **Three-State Coloring**: Use `0=unvisited`, `1=visiting`, `2=visited` to detect cycles
4. **Cycle Detection**: If we encounter a "visiting" node during DFS, cycle exists
5. **Topological Order**: Add nodes to result after processing all dependencies (post-order)

### Algorithm:

1. **Build Reverse Graph**: `adj[ai]` contains `bi` (ai depends on bi)
2. **DFS from Each Unvisited Node**: Use three-state coloring
3. **Cycle Detection**: If `visited[v] == 1` (visiting), cycle detected
4. **Post-order Addition**: Add node to result after processing all neighbors
5. **Validation**: If cycle found, return empty array; otherwise return result

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

## Key Insights

1. **Reverse Graph**: Building graph in reverse allows direct return of DFS path
2. **Three-State Coloring**: `0=unvisited`, `1=visiting`, `2=visited` enables cycle detection
3. **Post-order Addition**: Add nodes after processing dependencies for correct order
4. **Cycle Detection**: Encountering a "visiting" node indicates a back edge (cycle)
5. **Early Termination**: Stop DFS immediately when cycle detected

## Edge Cases

1. **No prerequisites**: `prerequisites = []` → return `[0,1,2,...,n-1]` (any order)
2. **Single course**: `numCourses = 1` → return `[0]`
3. **Cycle exists**: Return empty array `[]`
4. **Linear chain**: `[[1,0],[2,1],[3,2]]` → return `[0,1,2,3]`
5. **Multiple valid orders**: Any valid topological order is acceptable

## Common Mistakes

1. **Wrong graph direction**: Building normal graph instead of reverse
2. **Not detecting cycles**: Forgetting to check for visiting nodes
3. **Wrong addition order**: Adding nodes in pre-order instead of post-order
4. **Not handling all nodes**: Forgetting to DFS from all unvisited nodes
5. **State management**: Not properly updating visited states

## Alternative Approaches

### **Approach 2: Kahn's Algorithm (BFS)**

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        
        for(auto& p: prerequisites) {
            adj[p[1]].push_back(p[0]);
            indegree[p[0]]++;
        }
        
        queue<int> q;
        for(int i = 0; i < numCourses; i++) {
            if(indegree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> result;
        while(!q.empty()) {
            int u = q.front();
            q.pop();
            result.push_back(u);
            
            for(int v: adj[u]) {
                if(--indegree[v] == 0) {
                    q.push(v);
                }
            }
        }
        
        if(result.size() != numCourses) {
            return {};  // Cycle exists
        }
        return result;
    }
};
```

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V + E)

**Comparison:**
- **DFS**: More elegant, uses recursion stack
- **Kahn's (BFS)**: More intuitive, uses queue, easier to understand

## Related Problems

- [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) - Check if courses can be finished
- [LC 210: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Same problem (English version)
- [LC 269: Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) - Topological sort for character ordering
- [LC 310: Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) - Peeling leaves pattern

## Reference

- Problem Link: [LCR 113. Course Schedule II](https://leetcode.cn/problems/QA2IGt/description/)

---

*This problem demonstrates **DFS-based topological sort** with three-state coloring for cycle detection. The key insight is building a reverse graph so the DFS path can be directly returned as the topological order.*

