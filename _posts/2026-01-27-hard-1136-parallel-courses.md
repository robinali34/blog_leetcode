---
layout: post
title: "[Hard] 1136. Parallel Courses"
date: 2026-01-27 00:00:00 -0700
categories: [leetcode, hard, graph, topological-sort, dfs, dynamic-programming]
permalink: /2026/01/27/hard-1136-parallel-courses/
tags: [leetcode, hard, graph, topological-sort, dfs, dynamic-programming, memoization]
---
You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where `relations[i] = [prevCoursei, nextCoursei]`, representing a prerequisite relationship between course `prevCoursei` and course `nextCoursei`: course `prevCoursei` has to be taken before course `nextCoursei`.

In one semester, you can take any number of courses as long as you have taken all the prerequisites for the course you are taking.

Return *the **minimum number of semesters** needed to take all courses*. If there is no way to take all the courses, return `-1`.

## Thinking Process

1. **Longest Path in DAG**: Minimum semesters = length of longest path
- Each node in path must be taken in sequence
- Longest path determines minimum semesters needed
- `0` = unvisited

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



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
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

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

## Common Mistakes

1. **No prerequisites**: `n = 3`, `relations = []` → return `1` (all in one semester)
2. **Cycle exists**: `n = 2`, `relations = [[1,2],[2,1]]` → return `-1`
3. **Linear chain**: `n = 4`, `relations = [[1,2],[2,3],[3,4]]` → return `4`
4. **Multiple paths**: `n = 3`, `relations = [[1,3],[2,3]]` → return `2`
5. **Single node**: `n = 1`, `relations = []` → return `1`

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

## Related Problems

- [LC 207: Course Schedule](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-207-course-schedule/) - Check if all courses can be completed
- [LC 210: Course Schedule II](https://www.leetcode.com/problems/course-schedule-ii/) - Return course ordering
- [LC 329: Longest Increasing Path in a Matrix](https://www.leetcode.com/problems/longest-increasing-path-in-a-matrix/) - Similar longest path problem
- [LC 802: Find Eventual Safe States](https://robinali34.github.io/blog_leetcode/2026/01/15/medium-802-find-eventual-safe-states/) - Cycle detection in directed graph

## Key Takeaways

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

## References

- [LC 1136: Parallel Courses on LeetCode](https://www.leetcode.com/problems/parallel-courses/)
- [LeetCode Discuss — LC 1136: Parallel Courses](https://www.leetcode.com/problems/parallel-courses/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/parallel-courses/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
