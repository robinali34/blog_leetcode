---
layout: post
title: "[Hard] 685. Redundant Connection II"
date: 2025-12-30 21:30:00 -0700
categories: [leetcode, hard, union-find, dsu, graph, cycle-detection, directed-graph]
permalink: /2025/12/30/hard-685-redundant-connection-ii/
---
In this problem, a **rooted tree** is a directed graph such that there is exactly one node (the root) for which all other nodes are descendants of this node, plus exactly one parent for every node (except the root node which has no parents).

The given input is a directed graph that started as a rooted tree with `n` nodes (with distinct values from `1` to `n`), with one additional directed edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed.

The resulting graph is given as a 2D-array of `edges`. Each element of `edges` is a pair `[ui, vi]` that represents a **directed edge** connecting nodes `ui` and `vi`, where `ui` is a parent of child `vi`.

Return *an edge that can be removed so that the resulting graph is a rooted tree of `n` nodes*. If there are multiple answers, return the answer that occurs **last** in the given 2D-array.

## Thinking Process

In this problem, a **rooted tree** is a directed graph such that there is exactly one node (the root) for which all other nodes are descendants of this node, plus exactly one parent for every node (except the root node which has no parents).

The given input is a directed graph that started as a rooted tree with `n` nodes (with distinct values from `1` to `n`), with one additional directed edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed.

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
| **BFS / DFS traversal** *(this problem)* | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| Union-Find (DSU) | O(α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |

## Examples

**Example 1:**
```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Explanation: The directed edge [2,3] creates a cycle, so it should be removed.
```

**Example 2:**
```
Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]
Explanation: The directed edge [4,1] creates a cycle, so it should be removed.
```

**Example 3:**
```
Input: edges = [[2,1],[3,1],[4,2],[1,4]]
Output: [2,1]
Explanation: Node 1 has two parents (2 and 3), and there's also a cycle. 
The edge [2,1] should be removed.
```

## Constraints

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ui, vi <= n`
- `ui != vi`

## Algorithm Breakdown

### **Key Insight: Two Types of Problems**

In a directed graph that should be a rooted tree:

1. **Conflict (Two Parents)**:
   - A node has two incoming edges (two parents)
   - Invalidates the "exactly one parent" property
   - Detected when `parent[node2] != node2`

2. **Cycle**:
   - A directed cycle exists in the graph
   - Invalidates the tree property
   - Detected using Union-Find: if `find(u) == find(v)` before adding edge `(u,v)`

### **Decision Logic**

```cpp
if(conflict < 0) {
    // No conflict, just return cycle edge
    return cycle_edge;
} else {
    // Conflict exists
    if(cycle >= 0) {
        // Both conflict and cycle: return first parent edge
        return {parent[conflictNode], conflictNode};
    } else {
        // Only conflict: return conflict edge
        return conflict_edge;
    }
}
```

**Why this works:**
- **No conflict + cycle**: Simple case, return cycle edge
- **Conflict + cycle**: The cycle involves the conflict node, so we need to remove the first parent edge (the one that's part of the cycle)
- **Conflict only**: No cycle, so removing the conflict edge fixes it

### Complexity
### **Time Complexity:** O(n × α(n)) ≈ O(n)
- **Union-Find operations**: O(α(n)) per operation (nearly constant)
- **Process n edges**: O(n × α(n))
- **Total**: O(n) for practical purposes

### **Space Complexity:** O(n)
- **Union-Find ancestor array**: O(n)
- **Parent array**: O(n)
- **Total**: O(n)

## Key Points

1. **Directed Graph**: Unlike LC 684, edges are directed
2. **Two Issues**: Handle both conflicts (two parents) and cycles
3. **Union-Find**: Use DSU to detect cycles efficiently
4. **Parent Tracking**: Track parent to detect conflicts
5. **Priority Logic**: Return appropriate edge based on conflict/cycle combination

## Comparison: LC 684 vs LC 685

| Aspect | LC 684 (Undirected) | LC 685 (Directed) |
|--------|-------------------|-------------------|
| **Graph Type** | Undirected | Directed |
| **Issues** | Cycle only | Conflict + Cycle |
| **DSU Usage** | Direct cycle detection | Cycle detection + conflict handling |
| **Complexity** | O(n × α(n)) | O(n × α(n)) |
| **Difficulty** | Medium | Hard |

## Detailed Example Walkthrough

### **Example: `edges = [[1,2],[2,3],[3,1],[1,4]]`**

```
Step 1: Initialize
parent = [0,1,2,3,4]
uf: all nodes separate

Step 2: Process [1,2]
  parent[2] == 2 → no conflict
  parent[2] = 1
  uf.find(1) != uf.find(2) → no cycle
  uf.merge(1, 2)
  parent = [0,1,1,3,4]

Step 3: Process [2,3]
  parent[3] == 3 → no conflict
  parent[3] = 2
  uf.find(2) == uf.find(1) (from merge), uf.find(3) == 3
  uf.find(1) != uf.find(3) → no cycle
  uf.merge(2, 3) → uf.merge(1, 3)
  parent = [0,1,1,2,4]

Step 4: Process [3,1]
  parent[1] == 1 → no conflict
  parent[1] = 3
  uf.find(3) == uf.find(1) (both in same set) → CYCLE!
  cycle = 2
  parent = [0,3,1,2,4]

Step 5: Process [1,4]
  parent[4] == 4 → no conflict
  parent[4] = 1
  uf.find(1) != uf.find(4) → no cycle
  uf.merge(1, 4)
  parent = [0,3,1,2,1]

Result:
  conflict = -1 (no conflict)
  cycle = 2 (edge [3,1])
  return [3,1]
```

## Edge Cases

1. **Only cycle**: No conflicts, return cycle edge
2. **Only conflict**: No cycle, return conflict edge
3. **Both conflict and cycle**: Return first parent edge
4. **Root node conflict**: Root receives an edge (shouldn't happen in valid input)
5. **Self-loop**: Edge from node to itself (shouldn't happen per constraints)

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [684. Redundant Connection](https://www.leetcode.com/problems/redundant-connection/) - Undirected graph version
- [685. Redundant Connection II](https://www.leetcode.com/problems/redundant-connection-ii/) - Current problem (directed)
- [547. Number of Provinces](https://www.leetcode.com/problems/number-of-provinces/) - Connected components
- [990. Satisfiability of Equality Equations](https://www.leetcode.com/problems/satisfiability-of-equality-equations/) - DSU application

## Tags

`Union-Find`, `DSU`, `Disjoint Set Union`, `Graph`, `Cycle Detection`, `Directed Graph`, `Hard`

## Key Takeaways

- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

## References

- [LC 685: Redundant Connection II on LeetCode](https://www.leetcode.com/problems/redundant-connection-ii/)
- [LeetCode Discuss — LC 685: Redundant Connection II](https://www.leetcode.com/problems/redundant-connection-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/redundant-connection-ii/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
