---
layout: post
title: "1136. Parallel Courses"
date: 2026-01-27 00:00:00 -0700
categories: [leetcode, hard, graph, topological-sort, dfs, dynamic-programming]
permalink: /2026/01/27/hard-1136-parallel-courses/
tags: [leetcode, hard, graph, topological-sort, dfs, dynamic-programming, memoization]
---

# 1136. Parallel Courses

## Problem Statement

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where `relations[i] = [prevCoursei, nextCoursei]`, representing a prerequisite relationship between course `prevCoursei` and course `nextCoursei`: course `prevCoursei` has to be taken before course `nextCoursei`.

In one semester, you can take any number of courses as long as you have taken all the prerequisites for the course you are taking.

Return *the **minimum number of semesters** needed to take all courses*. If there is no way to take all the courses, return `-1`.

## Examples

**Example 1:**

```
Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
```

**Example 2:**

```
Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because there is a prerequisite cycle.
```

## Constraints

- `1 <= n <= 5000`
- `1 <= relations.length <= 5000`
- `relations[i].length == 2`
- `1 <= prevCoursei, nextCoursei <= n`
- `prevCoursei != nextCoursei`
- All the pairs `[prevCoursei, nextCoursei]` are **unique**.

## Solution Approach

This problem requires finding the **longest path in a DAG (Directed Acyclic Graph)**. If the graph contains a cycle, it's impossible to complete all courses.

### Key Insights:

1. **Graph Representation**: Courses are nodes, prerequisites are directed edges
2. **Longest Path**: The minimum semesters needed equals the length of the longest path in the DAG
3. **Cycle Detection**: If a cycle exists, return `-1`
4. **DFS with Memoization**: Use DFS to find longest path from each node, memoize results
5. **Three-State Coloring**: 
   - `0` = unvisited
   - `-1` = currently visiting (cycle detection)
   - `positive` = visited and memoized (length of longest path from this node)

## Solution: DFS with Memoization

```cpp
class Solution {
public:
    int minimumSemesters(int n, vector<vector<int>>& relations) {
        vector<vector<int>> graph(n + 1);
        for(auto& relation: relations) {
            graph[relation[0]].push_back(relation[1]);
        }

        vector<int> visited(n + 1, 0);
        int maxLen = 1;
        for(int node = 1; node < n + 1; node++) {
            int len = dfs(node, graph, visited);
            if(len == -1) return -1; // Found a cycle
            maxLen = max(maxLen, len);
        }
        return maxLen;
    }

private:
    int dfs(const int node, vector<vector<int>>& graph, vector<int>& visited) {
        if(visited[node] != 0) {
            return visited[node];
        }
        visited[node] = -1;
        int maxLen = 1;
        for(auto& endNode : graph[node]) {
            int len = dfs(endNode, graph, visited);
            if(len == -1) return -1;
            maxLen = max(maxLen, len + 1);
        }
        visited[node] = maxLen;
        return maxLen;
    }
};
```

### Algorithm Explanation:

#### **Step 1: Build Graph**

```cpp
vector<vector<int>> graph(n + 1);
for(auto& relation: relations) {
    graph[relation[0]].push_back(relation[1]);
}
```

- Build adjacency list: `graph[u]` contains all nodes that `u` points to
- `graph[prevCourse]` contains `nextCourse` (prerequisite relationship)

#### **Step 2: DFS from Each Node**

```cpp
for(int node = 1; node < n + 1; node++) {
    int len = dfs(node, graph, visited);
    if(len == -1) return -1; // Found a cycle
    maxLen = max(maxLen, len);
}
```

- For each unvisited node, find the longest path starting from it
- If cycle detected (`len == -1`), return `-1`
- Track maximum length across all nodes

#### **Step 3: DFS with Memoization**

```cpp
int dfs(const int node, vector<vector<int>>& graph, vector<int>& visited) {
    if(visited[node] != 0) {
        return visited[node];
    }
    visited[node] = -1;
    int maxLen = 1;
    for(auto& endNode : graph[node]) {
        int len = dfs(endNode, graph, visited);
        if(len == -1) return -1;
        maxLen = max(maxLen, len + 1);
    }
    visited[node] = maxLen;
    return maxLen;
}
```

**Key Operations:**

1. **Memoization Check**: If `visited[node] != 0`, return cached result
   - If `visited[node] > 0`: Already computed, return length
   - If `visited[node] == -1`: Currently visiting (cycle detected in caller)

2. **Mark as Visiting**: `visited[node] = -1`
   - Marks node as currently being processed
   - If we encounter `-1` during DFS, we found a cycle

3. **DFS on Neighbors**: For each neighbor `endNode`:
   - Recursively find longest path from `endNode`
   - If cycle found (`len == -1`), propagate `-1` up
   - Update `maxLen = max(maxLen, len + 1)`
   - `len + 1` because we're adding current node to the path

4. **Memoize Result**: `visited[node] = maxLen`
   - Store computed length for future use
   - Convert from `-1` (visiting) to positive (visited)

### Example Walkthrough:

**Input:** `n = 3`, `relations = [[1,3],[2,3]]`

```
Step 1: Build graph
  graph[1] = [3]
  graph[2] = [3]
  graph[3] = []

Step 2: DFS from each node
  DFS from node 1:
    visited[1] = -1 (mark as visiting)
    Visit graph[1] = [3]
      DFS from node 3:
        visited[3] = -1
        graph[3] = [] (no neighbors)
        maxLen = 1
        visited[3] = 1
        return 1
    maxLen = max(1, 1+1) = 2
    visited[1] = 2
    return 2
    
  DFS from node 2:
    visited[2] = -1
    Visit graph[2] = [3]
      DFS from node 3:
        visited[3] = 1 (already computed)
        return 1
    maxLen = max(1, 1+1) = 2
    visited[2] = 2
    return 2
    
  DFS from node 3:
    visited[3] = 1 (already computed)
    return 1

Step 3: Find maximum
  maxLen = max(2, 2, 1) = 2
  
Result: return 2 ✓
```

**Cycle Detection Example:** `n = 3`, `relations = [[1,2],[2,3],[3,1]]`

```
DFS from node 1:
  visited[1] = -1
  Visit graph[1] = [2]
    DFS from node 2:
      visited[2] = -1
      Visit graph[2] = [3]
        DFS from node 3:
          visited[3] = -1
          Visit graph[3] = [1]
            DFS from node 1:
              visited[1] = -1 (currently visiting!)
              return -1 (cycle detected!)
          return -1
      return -1
  return -1

Result: return -1 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(V + E)
  - Building graph: O(E)
  - DFS from each node: O(V + E) total
  - Each edge visited once, each node visited once
  - Overall: O(V + E)

- **Space Complexity:** O(V + E)
  - Graph adjacency list: O(V + E)
  - Visited array: O(V)
  - Recursion stack: O(V) in worst case
  - Overall: O(V + E)

## Key Insights

1. **Longest Path in DAG**: Minimum semesters = length of longest path
   - Each node in path must be taken in sequence
   - Longest path determines minimum semesters needed

2. **Cycle Detection**: Three-state coloring
   - `0` = unvisited
   - `-1` = visiting (if encountered again, cycle exists)
   - `positive` = visited and memoized

3. **Memoization**: Avoids recomputing longest path from each node
   - Once computed, result is cached in `visited[node]`
   - Significantly improves efficiency

4. **DFS Order**: Process all neighbors before finalizing current node
   - Ensures we find longest path through all possible routes

5. **Base Case**: Node with no outgoing edges has length 1
   - Can be taken in first semester (if no prerequisites)

## Edge Cases

1. **No prerequisites**: `n = 3`, `relations = []` → return `1` (all in one semester)
2. **Cycle exists**: `n = 2`, `relations = [[1,2],[2,1]]` → return `-1`
3. **Linear chain**: `n = 4`, `relations = [[1,2],[2,3],[3,4]]` → return `4`
4. **Multiple paths**: `n = 3`, `relations = [[1,3],[2,3]]` → return `2`
5. **Single node**: `n = 1`, `relations = []` → return `1`

## Common Mistakes

1. **Not detecting cycles**: Forgetting to check for `-1` during DFS
2. **Wrong memoization**: Not converting `-1` to positive value after computation
3. **Wrong base case**: Returning `0` instead of `1` for leaf nodes
4. **Not finding max**: Only checking one path instead of maximum across all paths
5. **Index confusion**: Using 0-indexed vs 1-indexed nodes

## Alternative Approach: Topological Sort (Kahn's Algorithm)

```cpp
class Solution {
public:
    int minimumSemesters(int n, vector<vector<int>>& relations) {
        vector<vector<int>> graph(n + 1);
        vector<int> indegree(n + 1, 0);
        
        for(auto& relation: relations) {
            graph[relation[0]].push_back(relation[1]);
            indegree[relation[1]]++;
        }
        
        queue<int> q;
        for(int i = 1; i <= n; i++) {
            if(indegree[i] == 0) {
                q.push(i);
            }
        }
        
        int semesters = 0;
        int coursesTaken = 0;
        
        while(!q.empty()) {
            semesters++;
            int size = q.size();
            for(int i = 0; i < size; i++) {
                int node = q.front();
                q.pop();
                coursesTaken++;
                
                for(int neighbor: graph[node]) {
                    indegree[neighbor]--;
                    if(indegree[neighbor] == 0) {
                        q.push(neighbor);
                    }
                }
            }
        }
        
        return coursesTaken == n ? semesters : -1;
    }
};
```

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V + E)

## Comparison of Approaches

| Aspect | DFS with Memoization | Topological Sort (Kahn's) |
|--------|---------------------|---------------------------|
| **Time** | O(V + E) | O(V + E) |
| **Space** | O(V + E) | O(V + E) |
| **Intuition** | Find longest path | Level-by-level processing |
| **Cycle Detection** | Three-state coloring | Check if all nodes processed |
| **Best For** | Finding longest path | Level-by-level semantics |

## Related Problems

- [LC 207: Course Schedule](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-207-course-schedule/) - Check if all courses can be completed
- [LC 210: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Return course ordering
- [LC 329: Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) - Similar longest path problem
- [LC 802: Find Eventual Safe States](https://robinali34.github.io/blog_leetcode/2026/01/15/medium-802-find-eventual-safe-states/) - Cycle detection in directed graph

---

*This problem demonstrates **DFS with memoization** to find the longest path in a DAG. The key insight is using three-state coloring (`0`, `-1`, `positive`) for both cycle detection and memoization, elegantly solving both problems in a single DFS pass.*
