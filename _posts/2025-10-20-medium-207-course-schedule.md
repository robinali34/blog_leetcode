---
layout: post
title: "[Medium] 207. Course Schedule"
date: 2025-10-20 16:30:00 -0700
categories: [leetcode, medium, graph, topological-sort, cycle-detection]
permalink: /2025/10/20/medium-207-course-schedule/
---
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

## Thinking Process

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

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
| **BFS / DFS traversal** *(this problem)* | $O(V+E)$ | $O(V)$ | Connectivity, flood fill |
| Dijkstra | $O((V+E)\log V)$ | $O(V)$ | Non-negative edge weights |
| Union-Find (DSU) | $O(\alpha(n))$ | $O(n)$ | Dynamic connectivity |
| Topological sort | $O(V+E)$ | $O(V)$ | DAG ordering, cycle detection |

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

### Solution Explanation

**Approach:** BFS / DFS traversal (this problem)

**Key idea:** There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

**How the code works:**
- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `numCourses = 2, prerequisites = [[1,0]]`, expected output `true`:

There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [210. Course Schedule II](https://www.leetcode.com/problems/course-schedule-ii/) - Return actual schedule
- [802. Find Eventual Safe States](https://www.leetcode.com/problems/find-eventual-safe-states/) - Similar cycle detection
- [329. Longest Increasing Path in a Matrix](https://www.leetcode.com/problems/longest-increasing-path-in-a-matrix/) - DAG longest path

## Tags

`Graph`, `Topological Sort`, `Cycle Detection`, `DFS`, `Medium`

## Key Takeaways

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.

## References

- [LC 207: Course Schedule on LeetCode](https://www.leetcode.com/problems/course-schedule/)
- [LeetCode Discuss — LC 207: Course Schedule](https://www.leetcode.com/problems/course-schedule/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/course-schedule/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
