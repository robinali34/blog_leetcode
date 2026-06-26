---
layout: post
title: "[Medium] 133. Clone Graph"
date: 2025-10-20 16:00:00 -0700
categories: [leetcode, medium, graph, dfs, bfs, clone]
permalink: /2025/10/20/medium-133-clone-graph/
---
Given a reference of a node in a **connected undirected graph**.

Return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

## Examples

**Example 1:**
```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val=1)'s neighbors are 2nd node (val=2) and 4th node (val=4).
2nd node (val=2)'s neighbors are 1st node (val=1) and 3rd node (val=3).
3rd node (val=3)'s neighbors are 2nd node (val=2) and 4th node (val=4).
4th node (val=4)'s neighbors are 1st node (val=1) and 3rd node (val=3).
```

**Example 2:**
```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val=1 and it does not have any neighbors.
```

**Example 3:**
```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not contain any nodes.
```

## Constraints

- The number of nodes in the graph is in the range `[0, 100]`.
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The graph is connected and undirected.

## Thinking Process

Given a reference of a node in a **connected undirected graph**.

Return a **deep copy** (clone) of the graph.

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

## Solution

### **Solution 1: BFS (Iterative)**

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(!node) return nullptr;
        unordered_map<Node*, Node*> visited;
        queue<Node*> q;
        q.push(node);
        visited[node] = new Node(node->val);
        while(!q.empty()) {
            Node* curr = q.front();
            q.pop();
            for(auto& neighbor: curr->neighbors) {
                if(!visited.contains(neighbor)) {
                    visited[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                visited[curr]->neighbors.push_back(visited[neighbor]);
            }
        }
        return visited[node];
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** Given a reference of a node in a **connected undirected graph**.

**How the code works:**
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `adjList = [[2,4],[1,3],[2,4],[1,3]]`, expected output `[[2,4],[1,3],[2,4],[1,3]]`:

There are 4 nodes in the graph.
1st node (val=1)'s neighbors are 2nd node (val=2) and 4th node (val=4).
2nd node (val=2)'s neighbors are 1st node (val=1) and 3rd node (val=3).
3rd node (val=3)'s neighbors are 2nd node (val=2) and 4th node (val=4).
4th node (val=4)'s neighbors are 1st node (val=1) and 3rd node (val=3).

### **Solution 2: DFS (Recursive)**

```cpp
class Solution {
private:
    Node* dfs(Node* node, unordered_map<Node*, Node*>& visited) {
        if(visited.contains(node)) return visited[node];

        Node* clone = new Node(node->val);
        visited[node] = clone;
        for(auto& neighbor: node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor, visited));
        }
        return clone;
    }
public:
    Node* cloneGraph(Node* node) {
        if(node == nullptr) return nullptr;
        unordered_map<Node*, Node*> visited;
        return dfs(node, visited);
    }
};
```

### **Algorithm Explanation:**

#### **BFS Approach:**
1. **Initialize**: Create visited map and queue
2. **Start**: Add original node to queue and create its clone
3. **Process**: For each node in queue:
   - Create clones for unvisited neighbors
   - Add neighbors to queue for processing
   - Connect cloned nodes to their cloned neighbors
4. **Return**: Return cloned version of starting node

#### **DFS Approach:**
1. **Base case**: If node already cloned, return cloned version
2. **Create clone**: Make new node with same value
3. **Recursive**: For each neighbor, recursively clone and connect
4. **Return**: Return the cloned node

### **Example Walkthrough:**

**For graph with nodes 1, 2, 3, 4:**

```
Original Graph:
    1
   / \
  2---3
   \ /
    4

BFS Process:
1. Start with node 1, create clone(1)
2. Process node 1: create clone(2), clone(4), connect clone(1) to them
3. Process node 2: create clone(3), connect clone(2) to clone(1), clone(3)
4. Process node 4: connect clone(4) to clone(1), clone(3)
5. Process node 3: connect clone(3) to clone(2), clone(4)

Final cloned graph has same structure as original.
```

### **Time Complexity:** O(V + E)
- **V**: Number of vertices (nodes)
- **E**: Number of edges (neighbor relationships)
- **Traversal**: Visit each node and edge exactly once
- **Cloning**: O(1) per node creation

### **Space Complexity:** O(V)
- **Visited map**: O(V) - stores mapping from original to cloned nodes
- **Queue (BFS)**: O(V) - maximum nodes in queue
- **Recursion stack (DFS)**: O(V) - maximum recursion depth
- **Cloned graph**: O(V + E) - not counted in auxiliary space
## Key Points

1. **Deep copy**: Create new nodes, not copy references
2. **Cycle handling**: Use visited map to prevent infinite loops
3. **Node mapping**: Track original → cloned node relationships
4. **Graph traversal**: BFS or DFS both work effectively
5. **Edge cases**: Handle null input and single node graphs

## Comparison: BFS vs DFS

| Aspect | BFS | DFS |
|--------|-----|-----|
| **Approach** | Iterative | Recursive |
| **Space** | Queue + Map | Recursion Stack + Map |
| **Code** | More verbose | More concise |
| **Stack overflow** | No risk | Risk with deep graphs |
| **Performance** | Similar | Similar |

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [138. Copy List with Random Pointer](https://www.leetcode.com/problems/copy-list-with-random-pointer/) - Similar cloning concept
- [200. Number of Islands](https://www.leetcode.com/problems/number-of-islands/) - Graph traversal
- [207. Course Schedule](https://www.leetcode.com/problems/course-schedule/) - Graph cycle detection

## Tags

`Graph`, `DFS`, `BFS`, `Clone`, `Deep Copy`, `Medium`

## Key Takeaways

- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

## References

- [LC 133: Clone Graph on LeetCode](https://www.leetcode.com/problems/clone-graph/)
- [LeetCode Discuss — LC 133: Clone Graph](https://www.leetcode.com/problems/clone-graph/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/clone-graph/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
