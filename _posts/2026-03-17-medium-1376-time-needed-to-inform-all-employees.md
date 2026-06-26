---
layout: post
title: "[Medium] 1376. Time Needed to Inform All Employees"
date: 2026-03-17
categories: [leetcode, medium, tree, dfs, bfs]
tags: [leetcode, medium, tree, dfs, bfs, graph]
permalink: /2026/03/17/medium-1376-time-needed-to-inform-all-employees/
---
A company has `n` employees numbered `0` to `n-1`. Each employee has exactly one direct manager given in `manager[i]`, except the head of the company (`manager[headID] == -1`). An employee needs `informTime[i]` minutes to inform **all** their direct subordinates. Return the total time needed to inform all employees.

## Examples

**Example 1:**

```
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: Only the head, no one to inform.
```

**Example 2:**

```
Input: n = 6, headID = 2,
       manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: Head (2) informs all 5 subordinates in 1 minute.
```

**Example 3:**

```
Input: n = 7, headID = 6,
       manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
Output: 21
Explanation: Chain 6→5→4→3→2→1→0, total = 1+2+3+4+5+6 = 21.
```

## Constraints

- `1 <= n <= 10^5`
- `0 <= headID < n`
- `manager.length == n`
- `informTime.length == n`
- `informTime[i] >= 0`
- The input forms a valid tree

## Thinking Process

### Baseline (Naive) -- O(n^2)

For each employee, walk up through `manager[i] → manager[manager[i]] → ... → head` and sum `informTime` along the path. Track the maximum. In a chain structure each walk is O(n), giving O(n^2) total.

### Bottleneck

Repeated traversal of the same paths -- computing the same prefix sums over and over.

### Optimization

This is a **tree rooted at `headID`** where `manager → subordinate` forms a directed edge. The problem becomes:

> Find the **longest weighted path** from root to any leaf.

Build an adjacency list and traverse once with DFS or BFS. Each node is visited exactly once.

### DFS Recurrence

$text{time}(node) = text{informTime}[node] + max_{child}(text{time}(child))

Base case: leaf nodes have no children, so `max(child times) = 0`.

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
```cpp
class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        unordered_map<int, vector<int>> graph;
        for (int i = 0; i < n; i++) {
            if (manager[i] != -1) {
                graph[manager[i]].push_back(i);
            }
        }
        return dfs(headID, graph, informTime);
    }

private:
    int dfs(int node, unordered_map<int, vector<int>>& graph, vector<int>& informTime) {
        int maxTime = 0;
        for (int child : graph[node]) {
            maxTime = max(maxTime, dfs(child, graph, informTime));
        }
        return informTime[node] + maxTime;
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** ### Baseline (Naive) -- O(n^2)$

**Walkthrough** — input `n = 1, headID = 0, manager = [-1], informTime = [0]`, expected output `0`:

Only the head, no one to inform.
## Common Mistakes

- Confusing the direction: edges go from manager to subordinates, not the other way
- Adding `informTime` of leaf nodes (leaves have `informTime = 0` but the logic should still be correct since it adds 0)
- Forgetting to propagate accumulated time in BFS (each child's time = parent's accumulated time + parent's `informTime`)

## Key Takeaways

- **"Maximum time from root to any leaf"** = longest path in a weighted tree = single DFS/BFS
- Building an adjacency list from the `manager[]` array converts the problem into standard tree traversal
- DFS gives a clean recursive formulation; BFS carries accumulated time as state in the queue

## Related Problems

- [104. Maximum Depth of Binary Tree](https://www.leetcode.com/problems/maximum-depth-of-binary-tree/) -- longest path in unweighted tree
- [543. Diameter of Binary Tree](https://www.leetcode.com/problems/diameter-of-binary-tree/) -- longest path through any node
- [841. Keys and Rooms](https://www.leetcode.com/problems/keys-and-rooms/) -- graph reachability via DFS/BFS
- [207. Course Schedule](https://www.leetcode.com/problems/course-schedule/) -- directed graph traversal

## References

- [LC 1376: Time Needed to Inform All Employees on LeetCode](https://www.leetcode.com/problems/time-needed-to-inform-all-employees/)
- [LeetCode Discuss — LC 1376: Time Needed to Inform All Employees](https://www.leetcode.com/problems/time-needed-to-inform-all-employees/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/time-needed-to-inform-all-employees/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
