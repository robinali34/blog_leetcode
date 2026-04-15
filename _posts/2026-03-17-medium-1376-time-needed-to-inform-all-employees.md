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

### Baseline (Naive) -- $O(n^2)$

For each employee, walk up through `manager[i] → manager[manager[i]] → ... → head` and sum `informTime` along the path. Track the maximum. In a chain structure each walk is $O(n)$, giving $O(n^2)$ total.

### Bottleneck

Repeated traversal of the same paths -- computing the same prefix sums over and over.

### Optimization

This is a **tree rooted at `headID`** where `manager → subordinate` forms a directed edge. The problem becomes:

> Find the **longest weighted path** from root to any leaf.

Build an adjacency list and traverse once with DFS or BFS. Each node is visited exactly once.

### DFS Recurrence

$$\text{time}(node) = \text{informTime}[node] + \max_{child}(\text{time}(child))$$

Base case: leaf nodes have no children, so `max(child times) = 0`.

## Solution 1: DFS -- $O(n)$

{% raw %}
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
{% endraw %}

**Time**: $O(n)$ -- each node visited once
**Space**: $O(n)$ -- adjacency list + recursion stack

## Solution 2: BFS -- $O(n)$

Propagate accumulated time level by level. Track the maximum time seen at any node.

{% raw %}
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

        queue<pair<int, int>> q;
        q.push({headID, 0});
        int maxTime = 0;

        while (!q.empty()) {
            auto [node, time] = q.front();
            q.pop();
            maxTime = max(maxTime, time);
            for (int child : graph[node]) {
                q.push({child, time + informTime[node]});
            }
        }

        return maxTime;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$

## Common Mistakes

- Confusing the direction: edges go from manager to subordinates, not the other way
- Adding `informTime` of leaf nodes (leaves have `informTime = 0` but the logic should still be correct since it adds 0)
- Forgetting to propagate accumulated time in BFS (each child's time = parent's accumulated time + parent's `informTime`)

## Key Takeaways

- **"Maximum time from root to any leaf"** = longest path in a weighted tree = single DFS/BFS
- Building an adjacency list from the `manager[]` array converts the problem into standard tree traversal
- DFS gives a clean recursive formulation; BFS carries accumulated time as state in the queue

## Related Problems

- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) -- longest path in unweighted tree
- [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) -- longest path through any node
- [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) -- graph reachability via DFS/BFS
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) -- directed graph traversal

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
