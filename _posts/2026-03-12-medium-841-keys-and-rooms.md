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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Thinking Process

### Graph Abstraction

Each room is a **node** and each key is a **directed edge** to another room. Starting from room 0, can we reach all nodes?

This is a **graph reachability** problem -- standard DFS or BFS from a starting node.

### Algorithm

1. Start from room 0
2. Traverse reachable rooms using DFS or BFS
3. Track visited rooms
4. If `visited.size() == n`, all rooms are reachable

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

## Approach 1: DFS (Stack) -- O(V + E)
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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** ### Graph Abstraction

**How the code works:**
1. Start from room 0
2. Traverse reachable rooms using DFS or BFS
3. Track visited rooms
4. If `visited.size() == n`, all rooms are reachable

**Walkthrough** — input `rooms = [[1],[2],[3],[]]`, expected output `true`:

Room 0 → key 1 → Room 1 → key 2 → Room 2 → key 3 → Room 3
## Approach 2: BFS (Queue) -- O(V + E)
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

**Time**: O(V + E)
**Space**: O(V)

## Common Mistakes

- Starting with all rooms as "visitable" instead of just room 0
- Not marking rooms as visited when adding to the stack/queue (causes duplicates)
- Treating this as an undirected graph (keys are one-way: having key to room 3 doesn't mean room 3 has a key back)

## Key Takeaways

- **"Can we reach all nodes from a source?"** = graph reachability = DFS or BFS
- The rooms/keys metaphor maps directly to an adjacency list: `rooms[i]` is the neighbor list for node `i`
- Both DFS and BFS give the same result here since we only care about reachability, not shortest path

## Related Problems

- [200. Number of Islands](https://www.leetcode.com/problems/number-of-islands/) -- DFS/BFS grid traversal
- [547. Number of Provinces](https://www.leetcode.com/problems/number-of-provinces/) -- connected components
- [1091. Shortest Path in Binary Matrix](https://www.leetcode.com/problems/shortest-path-in-binary-matrix/) -- BFS shortest path
- [323. Number of Connected Components](https://www.leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) -- connectivity

## References

- [LC 841: Keys and Rooms on LeetCode](https://www.leetcode.com/problems/keys-and-rooms/)
- [LeetCode Discuss — LC 841: Keys and Rooms](https://www.leetcode.com/problems/keys-and-rooms/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/keys-and-rooms/editorial/) *(may require premium)*

## Template Reference

- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
- [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/)
