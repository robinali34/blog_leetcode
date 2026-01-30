---
layout: post
title: "685. Redundant Connection II"
date: 2025-12-30 21:30:00 -0700
categories: [leetcode, hard, union-find, dsu, graph, cycle-detection, directed-graph]
permalink: /2025/12/30/hard-685-redundant-connection-ii/
---

# 685. Redundant Connection II

## Problem Statement

In this problem, a **rooted tree** is a directed graph such that there is exactly one node (the root) for which all other nodes are descendants of this node, plus exactly one parent for every node (except the root node which has no parents).

The given input is a directed graph that started as a rooted tree with `n` nodes (with distinct values from `1` to `n`), with one additional directed edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed.

The resulting graph is given as a 2D-array of `edges`. Each element of `edges` is a pair `[ui, vi]` that represents a **directed edge** connecting nodes `ui` and `vi`, where `ui` is a parent of child `vi`.

Return *an edge that can be removed so that the resulting graph is a rooted tree of `n` nodes*. If there are multiple answers, return the answer that occurs **last** in the given 2D-array.

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Tree structure**: What makes a valid tree? (Assumption: Directed tree with n nodes and n-1 edges, one root, no cycles)

2. **Redundant edge**: What makes an edge redundant? (Assumption: Edge that creates cycle or gives node two parents - violates tree properties)

3. **Return format**: What should we return? (Assumption: Edge to remove - [u, v] that should be removed to make valid tree)

4. **Multiple redundant edges**: What if multiple edges are redundant? (Assumption: Return the last edge in edges array that can be removed)

5. **Edge direction**: Are edges directed? (Assumption: Yes - edges[i] = [ui, vi] means edge from ui to vi)

## Solution Approach

This problem is the **directed graph** version of LC 684. Unlike the undirected case, we need to handle two types of issues:

1. **Node with Two Parents (Conflict)**: A node receives edges from two different parents
2. **Cycle in Graph**: A cycle exists in the directed graph

### Key Insights:

1. **Two Problem Types**:
   - **Conflict**: Node has two parents (invalidates tree property)
   - **Cycle**: Directed cycle exists (invalidates tree property)

2. **Union-Find for Cycles**: Use Union-Find to detect cycles in directed graph
3. **Parent Tracking**: Track parent of each node to detect conflicts
4. **Priority**: Return last edge in input that causes the problem

### Algorithm:

1. **Detect Conflicts**: Track parent of each node, identify if any node has two parents
2. **Detect Cycles**: Use Union-Find to detect cycles
3. **Handle Cases**:
   - No conflict: Return edge that creates cycle
   - Conflict exists: Return appropriate edge based on cycle detection

## Solution

### **Solution: Union-Find with Conflict Detection**

```cpp
struct UnionFind {
    vector<int> ancestor;
    UnionFind(int n) {
        ancestor.resize(n);
        for(int i = 0; i < n; i++) {
            ancestor[i] = i;
        }
    }

    int find(int index) {
        return index == ancestor[index] ? index : ancestor[index] = find(ancestor[index]);
    }

    void merge(int u, int v) {
        ancestor[find(u)] = find(v);
    }
};

class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        const int n = edges.size();
        UnionFind uf = UnionFind(n + 1);
        vector<int> parent(n + 1);
        for(int i = 1; i <= n; i++) {
            parent[i] = i;
        }
        int conflict = -1;
        int cycle = -1;
        for(int i = 0; i < n; i++) {
            vector<int> edge = edges[i];
            int node1 = edge[0], node2 = edge[1];
            if(parent[node2] != node2) {
                conflict = i;
            } else {
                parent[node2] = node1;
                if(uf.find(node1) == uf.find(node2)) {
                    cycle = i;
                } else {
                    uf.merge(node1, node2);
                }
            }
        }
        if(conflict < 0) {
            return {edges[cycle][0], edges[cycle][1]};
        } else {
            vector<int> conflictEdge = edges[conflict];
            if(cycle >= 0) {
                return {parent[conflictEdge[1]], conflictEdge[1]};
            } else {
                return {conflictEdge[0], conflictEdge[1]};
            }
        }
    }
};
```

### **Algorithm Explanation:**

1. **Union-Find Structure (Lines 1-18)**:
   - `ancestor[i]`: Root ancestor of node `i`
   - `find(index)`: Find root with path compression
   - `merge(u, v)`: Merge sets containing `u` and `v`

2. **Initialization (Lines 22-28)**:
   - Create Union-Find for `n+1` nodes (1-indexed)
   - Initialize `parent` array: `parent[i] = i` (each node is its own parent initially)
   - Track `conflict` and `cycle` edge indices

3. **Process Each Edge (Lines 29-42)**:
   - **Conflict Detection (Lines 33-34)**:
     - If `parent[node2] != node2`: Node2 already has a parent → conflict!
     - Mark this edge as conflict edge
   - **Cycle Detection (Lines 35-41)**:
     - Set `parent[node2] = node1`
     - If `uf.find(node1) == uf.find(node2)`: Already connected → cycle!
     - Otherwise: Merge the two nodes

4. **Return Result (Lines 43-52)**:
   - **No Conflict**: Return edge that creates cycle
   - **Conflict Exists**:
     - If cycle also exists: Return first parent edge (the one that's part of cycle)
     - If no cycle: Return conflict edge itself

### **Example Walkthrough:**

**Example 1: `edges = [[1,2],[1,3],[2,3]]`**

```
Step 1: Initialize
parent = [0,1,2,3]  (1-indexed, parent[i]=i initially)
conflict = -1, cycle = -1

Step 2: Process edge [1,2]
  node1=1, node2=2
  parent[2] == 2 → no conflict
  parent[2] = 1
  uf.find(1) != uf.find(2) → no cycle
  uf.merge(1, 2)
  parent = [0,1,1,3]

Step 3: Process edge [1,3]
  node1=1, node2=3
  parent[3] == 3 → no conflict
  parent[3] = 1
  uf.find(1) != uf.find(3) → no cycle
  uf.merge(1, 3)
  parent = [0,1,1,1]

Step 4: Process edge [2,3]
  node1=2, node2=3
  parent[3] == 1 != 3 → CONFLICT!
  conflict = 2
  (Don't update parent or check cycle)

Result: conflict = -1? No, conflict = 2
But wait, let me re-check the logic...

Actually, when conflict is detected, we don't update parent.
So when we process [2,3]:
  parent[3] = 1 (from previous step)
  parent[3] != 3 → conflict = 2
  We skip updating parent and cycle check

But we need to check cycle separately. Let me trace more carefully...

Actually, the issue is that when conflict is found, we skip the cycle check.
But we should still check if there's a cycle with the existing edges.

Wait, I think the logic is:
- If parent[node2] != node2, we have a conflict, so we mark conflict = i
- Otherwise, we set parent and check for cycle

So for [2,3]:
  parent[3] = 1 (from [1,3])
  parent[3] != 3 → conflict = 2
  We don't check cycle for this edge

But we already have cycle information from previous edges.

Actually, let me re-read the code:
- conflict tracks the LAST edge that causes conflict
- cycle tracks the LAST edge that causes cycle
- We process edges in order

For the example:
- [1,2]: No conflict, no cycle
- [1,3]: No conflict, no cycle  
- [2,3]: Conflict! (node 3 already has parent 1)

But wait, we also need to check if [2,3] creates a cycle.
Since we skip the cycle check when conflict is detected, we need to handle this differently.

Actually, I think the algorithm works like this:
1. First pass: Detect conflicts and cycles separately
2. If no conflict: Return cycle edge
3. If conflict: Check if removing conflict edge fixes it, or if we need the first parent edge

Let me trace Example 3 which has both conflict and cycle.
```

**Example 3: `edges = [[2,1],[3,1],[4,2],[1,4]]`**

```
Step 1: Initialize
parent = [0,1,2,3,4]
conflict = -1, cycle = -1

Step 2: Process [2,1]
  parent[1] == 1 → no conflict
  parent[1] = 2
  uf.find(2) != uf.find(1) → no cycle
  uf.merge(2, 1)
  parent = [0,2,2,3,4]

Step 3: Process [3,1]
  parent[1] == 2 != 1 → CONFLICT!
  conflict = 1
  (Skip parent update and cycle check)
  parent = [0,2,2,3,4] (unchanged)

Step 4: Process [4,2]
  parent[2] == 2 → no conflict
  parent[2] = 4
  uf.find(4) != uf.find(2) → no cycle (2's root is 2, 4's root is 4)
  uf.merge(4, 2)
  parent = [0,2,4,3,4]

Step 5: Process [1,4]
  parent[4] == 4 → no conflict
  parent[4] = 1
  uf.find(1) == uf.find(4)? 
    find(1) = find(2) = find(4) = 4 (after merges)
    find(4) = 4
    Yes! CYCLE!
  cycle = 3
  parent = [0,2,4,3,1]

Result:
  conflict = 1 (edge [3,1])
  cycle = 3 (edge [1,4])
  
  conflict >= 0, so:
    conflictEdge = [3,1]
    cycle >= 0, so:
      return {parent[1], 1} = {2, 1}
```

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

## Complexity Analysis

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

## Alternative Approaches

### **Approach 1: Union-Find with Conflict Detection (Current Solution)**
- **Time**: O(n × α(n)) ≈ O(n)
- **Space**: O(n)
- **Best for**: Efficient single-pass solution

### **Approach 2: DFS Cycle Detection**
- **Time**: O(n)
- **Space**: O(n)
- **Use DFS**: Build graph, detect cycles with DFS
- **Handle conflicts**: Track parents separately

### **Approach 3: Two-Pass Approach**
- **Time**: O(n × α(n))
- **Space**: O(n)
- **First pass**: Detect conflicts
- **Second pass**: Check cycles with/without conflict edges

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

## Related Problems

- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) - Undirected graph version
- [685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) - Current problem (directed)
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) - Connected components
- [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) - DSU application

## Tags

`Union-Find`, `DSU`, `Disjoint Set Union`, `Graph`, `Cycle Detection`, `Directed Graph`, `Hard`

