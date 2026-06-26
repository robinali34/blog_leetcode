---
layout: post
title: "[Medium] 684. Redundant Connection"
date: 2025-12-29 14:30:00 -0700
categories: [leetcode, medium, union-find, dsu, graph, cycle-detection, dfs]
permalink: /2025/12/29/medium-684-redundant-connection/
---
In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return *an edge that can be removed so that the resulting graph is a tree of `n` nodes*. If there are multiple answers, return the answer that occurs **last** in the input.

## Thinking Process

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

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
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Examples

**Example 1:**
```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Explanation: The edge [2,3] creates a cycle, so it should be removed.
```

**Example 2:**
```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
Explanation: The edge [1,4] creates a cycle, so it should be removed.
```

## Constraints

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ai < bi <= edges.length`
- `ai != bi`
- There are no repeated edges.
- The given graph is connected.

## DSU Template

Here's the general template for Union-Find (DSU) with union by rank:

```cpp
class DSU {
private:
    vector<int> parent;
    vector<int> rank;

public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    // Find with path compression
    int find(int x) {
        if(parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    // Union by rank
    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if(x == y) return false; // Already in same set

        // Union by rank: attach smaller tree to larger tree
        if(rank[x] < rank[y]) {
            parent[x] = y;
        } else if(rank[x] > rank[y]) {
            parent[y] = x;
        } else {
            parent[y] = x;
            rank[x]++;
        }
        return true;
    }

    // Check if two nodes are connected
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};
```

### **Key Template Components:**

1. **Data Structures**:
   - `parent[i]`: Parent of node `i` (root if `parent[i] == i`)
   - `rank[i]`: Approximate depth of tree rooted at `i`

2. **Path Compression**:
   - Flattens tree during find operation
   - Makes future finds faster

3. **Union by Rank**:
   - Keeps trees balanced
   - Attaches smaller tree to larger tree
   - Only increases rank when ranks are equal

4. **Time Complexity**:
   - Nearly O(1) per operation (inverse Ackermann function)
   - O(α(n)) where α grows extremely slowly

### Complexity
### **Solution 1: DSU**

**Time Complexity:** O(n × α(n)) ≈ O(n)
- **DSU operations**: O(α(n)) per operation (nearly constant)
- **Process n edges**: O(n × α(n))
- **Total**: O(n) for practical purposes

**Space Complexity:** O(n)
- **Parent array**: O(n)
- **Rank array**: O(n)
- **Total**: O(n)

### **Solution 2: DFS**

**Time Complexity:** O(n)
- **Graph construction**: O(n)
- **DFS traversal**: O(n) - visit each node once
- **Cycle extraction**: O(n) - worst case
- **Edge search**: O(n) - check all edges
- **Total**: O(n)

**Space Complexity:** O(n)
- **Adjacency list**: O(n)
- **Visited array**: O(n)
- **Parent array**: O(n)
- **Cycle node map**: O(n)
- **DFS recursion stack**: O(n)
- **Total**: O(n)

## Key Points

1. **DSU is Optimal**: Union-Find is the most efficient approach for cycle detection
2. **Path Compression**: Speeds up find operations significantly
3. **Union by Rank**: Keeps trees balanced for better performance
4. **1-based to 0-based**: Convert node indices when using DSU
5. **Last Edge Priority**: Problem asks for last edge in input that creates cycle
6. **Single Cycle**: Graph has exactly one cycle (one extra edge in tree)

## Comparison: DSU vs DFS

| Aspect | DSU | DFS |
|--------|-----|-----|
| **Time Complexity** | O(n × α(n)) ≈ O(n) | O(n) |
| **Space Complexity** | O(n) | O(n) |
| **Implementation** | Simpler | More complex |
| **Cycle Detection** | Direct (during union) | Requires traversal |
| **Edge Order** | Natural (process in order) | Need to track and search |
| **Recommended** | ✅ Yes | ⚠️ Works but more complex |

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [685. Redundant Connection II](https://www.leetcode.com/problems/redundant-connection-ii/) - Directed graph version
- [547. Number of Provinces](https://www.leetcode.com/problems/number-of-provinces/) - Count connected components
- [721. Accounts Merge](https://www.leetcode.com/problems/accounts-merge/) - DSU for merging accounts
- [1319. Number of Operations to Make Network Connected](https://www.leetcode.com/problems/number-of-operations-to-make-network-connected/) - DSU for connectivity

## Tags

`Union-Find`, `DSU`, `Disjoint Set Union`, `Graph`, `Cycle Detection`, `DFS`, `Medium`

## Key Takeaways

- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

## References

- [LC 684: Redundant Connection on LeetCode](https://www.leetcode.com/problems/redundant-connection/)
- [LeetCode Discuss — LC 684: Redundant Connection](https://www.leetcode.com/problems/redundant-connection/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/redundant-connection/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
