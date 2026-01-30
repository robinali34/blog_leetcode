---
layout: post
title: "133. Clone Graph"
date: 2025-10-20 16:00:00 -0700
categories: [leetcode, medium, graph, dfs, bfs, clone]
permalink: /2025/10/20/medium-133-clone-graph/
---

# 133. Clone Graph

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Clone definition**: What does "clone" mean? (Assumption: Create a deep copy - new nodes with same values and structure, but different memory addresses)

2. **Graph type**: Is the graph directed or undirected? (Assumption: Undirected - edges are bidirectional, represented as neighbors list)

3. **Node structure**: What information does each node contain? (Assumption: Node has val and list of neighbors - need to clone both)

4. **Empty graph**: How should we handle null/empty graph? (Assumption: Return null - no graph to clone)

5. **Cycle handling**: How should we handle cycles? (Assumption: Use visited map to avoid infinite loops - track cloned nodes)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to clone a graph. Let me try creating nodes first, then connecting them."

**Naive Solution**: Two-pass approach: first pass create all nodes, second pass connect edges. But need to map original nodes to cloned nodes.

**Complexity**: O(V + E) time, O(V) space

**Issues**:
- Two passes needed
- Need to maintain mapping between original and cloned nodes
- More complex than necessary
- Doesn't handle cycles naturally

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use DFS/BFS with a visited map that stores cloned nodes. This handles cycles naturally."

**Improved Solution**: Use DFS or BFS traversal. For each node, create clone if not already cloned, then recursively clone neighbors. Use hash map to track cloned nodes and avoid cycles.

**Complexity**: O(V + E) time, O(V) space

**Improvements**:
- Single pass with recursion/iteration
- Naturally handles cycles through visited map
- Clean and intuitive approach
- Works for both DFS and BFS

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "DFS is more elegant for this problem. Let me refine the implementation."

**Best Solution**: DFS with hash map storing cloned nodes. When visiting a node, create clone if needed, then recursively clone all neighbors. Map ensures each node is cloned exactly once.

**Key Realizations**:
1. DFS/BFS both work, DFS is more elegant
2. Hash map is essential for cycle detection and node mapping
3. O(V + E) time is optimal - must visit all nodes and edges
4. O(V) space is optimal - need to store all cloned nodes

## Solution Approach

This problem requires creating a **deep copy** of a graph, meaning we need to create new nodes with the same structure and relationships as the original graph.

### Key Insights:

1. **Deep copy**: Create new nodes, not just copy references
2. **Graph traversal**: Need to visit all nodes and their neighbors
3. **Avoid cycles**: Use visited tracking to prevent infinite loops
4. **Node mapping**: Map original nodes to cloned nodes
5. **Two approaches**: BFS (iterative) or DFS (recursive)

### Algorithm:

1. **Create node mapping**: `unordered_map<Node*, Node*>` to track cloned nodes
2. **Traverse graph**: Visit all nodes using BFS or DFS
3. **Clone nodes**: Create new nodes with same values
4. **Build relationships**: Connect cloned nodes based on original relationships
5. **Return root**: Return the cloned version of the starting node

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

## Complexity Analysis

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

## Alternative Approaches

### **DFS Iterative (Stack)**
```cpp
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(!node) return nullptr;
        unordered_map<Node*, Node*> visited;
        stack<Node*> stk;
        stk.push(node);
        visited[node] = new Node(node->val);
        
        while(!stk.empty()) {
            Node* curr = stk.top();
            stk.pop();
            
            for(auto& neighbor: curr->neighbors) {
                if(!visited.contains(neighbor)) {
                    visited[neighbor] = new Node(neighbor->val);
                    stk.push(neighbor);
                }
                visited[curr]->neighbors.push_back(visited[neighbor]);
            }
        }
        return visited[node];
    }
};
```

## Related Problems

- [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) - Similar cloning concept
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) - Graph traversal
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) - Graph cycle detection

## Tags

`Graph`, `DFS`, `BFS`, `Clone`, `Deep Copy`, `Medium`
