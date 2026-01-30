---
layout: post
title: "207. Course Schedule"
date: 2025-10-20 16:30:00 -0700
categories: [leetcode, medium, graph, topological-sort, cycle-detection]
permalink: /2025/10/20/medium-207-course-schedule/
---

# 207. Course Schedule

## Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

## Examples

**Example 1:**
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All the pairs `prerequisites[i]` are **unique**.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Prerequisite format**: How are prerequisites represented? (Assumption: [ai, bi] means to take course ai, you must first take course bi - bi is prerequisite for ai)

2. **Cycle detection**: What makes a schedule impossible? (Assumption: If there's a cycle in prerequisites - circular dependency makes it impossible)

3. **Return value**: What should we return? (Assumption: Boolean - true if can finish all courses, false if cycle exists)

4. **All courses**: Must we take all courses? (Assumption: Yes - need to determine if we can finish all numCourses courses)

5. **No prerequisites**: What if there are no prerequisites? (Assumption: Return true - can take courses in any order)

## Solution Approach

This problem is asking whether we can complete all courses given their prerequisites. This translates to checking if the **directed graph** formed by courses and prerequisites has **no cycles**.

### Key Insights:

1. **Graph representation**: Courses are nodes, prerequisites are directed edges
2. **Cycle detection**: If there's a cycle, we can't complete all courses
3. **Two approaches**: 
   - **Topological Sort (Kahn's Algorithm)**: Use indegree counting
   - **DFS Cycle Detection**: Use three-state coloring (white/gray/black)

### Algorithm:

#### **Approach 1: Topological Sort**
1. **Build graph**: Create adjacency list and calculate indegrees
2. **Find sources**: Start with courses having no prerequisites (indegree = 0)
3. **Process**: Remove sources and update indegrees of neighbors
4. **Check**: If all courses processed, no cycle exists

#### **Approach 2: DFS Cycle Detection**
1. **Three states**: 0=unvisited, 1=visiting, 2=visited
2. **DFS traversal**: Visit each unvisited node
3. **Cycle detection**: If we encounter a "visiting" node, cycle exists
4. **State update**: Mark as visiting during DFS, visited after completion

## Solution

### **Solution 1: Topological Sort (Kahn's Algorithm)**

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses, 0);
        vector<vector<int>> adj(numCourses);

        for(auto& p : prerequisites) {
            adj[p[1]].push_back(p[0]);
            indegree[p[0]]++;
        }
        queue<int> q;
        for(int i = 0; i < numCourses; i++) {
            if(indegree[i] == 0) q.push(i);
        }
        int count = 0;
        while(!q.empty()) {
            int course = q.front();
            q.pop();
            count++;
            for(int next: adj[course]) {
                if(--indegree[next] == 0) q.push(next);
            }
        }
        return count == numCourses;
    }
};
```

### **Solution 2: DFS Cycle Detection**

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        for(auto& p: prerequisites) {
            adj[p[1]].push_back(p[0]);
        }
        // 0: unvisited, 1: visiting, 2: visited
        vector<int> state(numCourses, 0);
        for(int i = 0; i < numCourses; i++) {
            if(hasCycle(i, adj, state)) return false;
        }
        return true;
    }
private:
    bool hasCycle(int node, vector<vector<int>>& adj, vector<int>& state) {
        if(state[node] == 1) return true; // found a cycle
        if(state[node] == 2) return false;
        state[node] = 1;
        for(int neighbor: adj[node]) {
            if(hasCycle(neighbor, adj, state)) return true;
        }
        state[node] = 2;
        return false;
    }
};
```

### **Algorithm Explanation:**

#### **Topological Sort Approach:**
1. **Build graph**: Create adjacency list and calculate indegrees
2. **Initialize queue**: Add all courses with indegree 0 (no prerequisites)
3. **Process**: Remove course from queue, decrement indegrees of its neighbors
4. **Add to queue**: If neighbor's indegree becomes 0, add to queue
5. **Check completion**: If count equals numCourses, all courses can be completed

#### **DFS Cycle Detection Approach:**
1. **Three states**: 0=unvisited, 1=visiting, 2=visited
2. **DFS from each unvisited node**: Check for cycles
3. **Cycle detection**: If we encounter a "visiting" node during DFS, cycle exists
4. **State transitions**: unvisited → visiting → visited

### **Example Walkthrough:**

**For `numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`:**

```
Graph:
0 → 1 → 3
  ↘ 2 ↗

Topological Sort:
1. Indegrees: [0,1,1,2]
2. Start with course 0 (indegree=0)
3. Remove 0: indegrees become [0,0,0,2]
4. Add courses 1,2 to queue
5. Remove 1: indegrees become [0,0,0,1]
6. Remove 2: indegrees become [0,0,0,0]
7. Add course 3 to queue
8. Remove 3: count=4, return true

DFS Cycle Detection:
1. Start DFS from course 0
2. Visit 0: state[0]=1 (visiting)
3. Visit 1: state[1]=1 (visiting)
4. Visit 3: state[3]=1 (visiting)
5. No more neighbors, state[3]=2 (visited)
6. Back to 1: state[1]=2 (visited)
7. Back to 0: state[0]=2 (visited)
8. Continue with courses 2,3...
9. No cycles found, return true
```

## Complexity Analysis

### **Time Complexity:** O(V + E)
- **V**: Number of courses (numCourses)
- **E**: Number of prerequisites
- **Graph building**: O(E)
- **Traversal**: O(V + E)
- **Total**: O(V + E)

### **Space Complexity:** O(V + E)
- **Adjacency list**: O(V + E)
- **Indegree array**: O(V)
- **Queue/Stack**: O(V)
- **State array**: O(V)
- **Total**: O(V + E)

## Key Points

1. **Graph problem**: Courses and prerequisites form a directed graph
2. **Cycle detection**: Cycle means impossible to complete all courses
3. **Two approaches**: Topological sort and DFS both work
4. **Topological sort**: More intuitive for this problem
5. **DFS**: More general approach for cycle detection

## Comparison: Topological Sort vs DFS

| Aspect | Topological Sort | DFS Cycle Detection |
|--------|------------------|-------------------|
| **Approach** | Indegree counting | Three-state coloring |
| **Intuition** | Process courses in order | Detect cycles directly |
| **Space** | Queue + Indegree array | Recursion stack + State array |
| **Code** | More straightforward | More elegant |
| **Performance** | Similar | Similar |

## Alternative Approaches

### **DFS Iterative (Stack)**
```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        for(auto& p: prerequisites) {
            adj[p[1]].push_back(p[0]);
        }
        
        vector<int> state(numCourses, 0); // 0: unvisited, 1: visiting, 2: visited
        stack<int> stk;
        
        for(int i = 0; i < numCourses; i++) {
            if(state[i] == 0) {
                stk.push(i);
                while(!stk.empty()) {
                    int node = stk.top();
                    if(state[node] == 2) {
                        stk.pop();
                        continue;
                    }
                    if(state[node] == 1) return false; // cycle detected
                    
                    state[node] = 1; // visiting
                    for(int neighbor: adj[node]) {
                        if(state[neighbor] == 0) {
                            stk.push(neighbor);
                        } else if(state[neighbor] == 1) {
                            return false; // cycle detected
                        }
                    }
                    if(stk.top() == node) {
                        state[node] = 2; // visited
                        stk.pop();
                    }
                }
            }
        }
        return true;
    }
};
```

## Related Problems

- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Return actual schedule
- [802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) - Similar cycle detection
- [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) - DAG longest path

## Tags

`Graph`, `Topological Sort`, `Cycle Detection`, `DFS`, `Medium`
