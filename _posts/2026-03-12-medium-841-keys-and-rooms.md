---
layout: post
title: "[Medium] 841. Keys and Rooms"
date: 2026-03-12
categories: [leetcode, medium, graph, dfs, bfs]
tags: [leetcode, medium, graph, dfs, bfs, reachability]
permalink: /2026/03/12/medium-841-keys-and-rooms/
---

There are `n` rooms labeled `0` to `n-1`. All rooms are locked except room `0`. Each room contains a set of keys to other rooms. Given `rooms[i]` -- the set of keys in room `i` -- return `true` if you can visit **all** rooms.

## Examples

**Example 1:**

```
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: Room 0 → key 1 → Room 1 → key 2 → Room 2 → key 3 → Room 3
```

**Example 2:**

```
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: Room 2 is never reachable.
```

## Constraints

- `n == rooms.length`
- `2 <= n <= 1000`
- `0 <= rooms[i].length <= 1000`
- `1 <= sum(rooms[i].length) <= 3000`
- `0 <= rooms[i][j] < n`
- All values of `rooms[i]` are unique

## Thinking Process

### Graph Abstraction

Each room is a **node** and each key is a **directed edge** to another room. Starting from room 0, can we reach all nodes?

This is a **graph reachability** problem -- standard DFS or BFS from a starting node.

### Algorithm

1. Start from room 0
2. Traverse reachable rooms using DFS or BFS
3. Track visited rooms
4. If `visited.size() == n`, all rooms are reachable

## Approach 1: DFS (Stack) -- $O(V + E)$

{% raw %}
```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        unordered_set<int> visited;
        stack<int> st;

        visited.insert(0);
        st.push(0);

        while (!st.empty()) {
            int room = st.top();
            st.pop();

            for (int key : rooms[room]) {
                if (!visited.count(key)) {
                    visited.insert(key);
                    st.push(key);
                }
            }
        }

        return visited.size() == n;
    }
};
```
{% endraw %}

**Time**: $O(V + E)$ where $V$ = rooms, $E$ = total keys
**Space**: $O(V)$

## Approach 2: BFS (Queue) -- $O(V + E)$

{% raw %}
```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        unordered_set<int> visited;
        queue<int> q;

        visited.insert(0);
        q.push(0);

        while (!q.empty()) {
            int room = q.front();
            q.pop();

            for (int key : rooms[room]) {
                if (!visited.count(key)) {
                    visited.insert(key);
                    q.push(key);
                }
            }
        }

        return visited.size() == n;
    }
};
```
{% endraw %}

**Time**: $O(V + E)$
**Space**: $O(V)$

## Common Mistakes

- Starting with all rooms as "visitable" instead of just room 0
- Not marking rooms as visited when adding to the stack/queue (causes duplicates)
- Treating this as an undirected graph (keys are one-way: having key to room 3 doesn't mean room 3 has a key back)

## Key Takeaways

- **"Can we reach all nodes from a source?"** = graph reachability = DFS or BFS
- The rooms/keys metaphor maps directly to an adjacency list: `rooms[i]` is the neighbor list for node `i`
- Both DFS and BFS give the same result here since we only care about reachability, not shortest path

## Related Problems

- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) -- DFS/BFS grid traversal
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) -- connected components
- [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) -- BFS shortest path
- [323. Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) -- connectivity

## Template Reference

- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
