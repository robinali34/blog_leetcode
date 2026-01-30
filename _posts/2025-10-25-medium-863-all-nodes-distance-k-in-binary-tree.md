---
layout: post
title: "LC 863: All Nodes Distance K in Binary Tree"
date: 2025-10-25 13:00:00 -0700
categories: leetcode medium tree dfs bfs
permalink: /posts/2025-10-25-medium-863-all-nodes-distance-k-in-binary-tree/
tags: [leetcode, medium, tree, binary-tree, dfs, bfs, graph, recursion]
---

# LC 863: All Nodes Distance K in Binary Tree

**Difficulty:** Medium  
**Category:** Tree, DFS, BFS  
**Companies:** Amazon, Facebook, Google, Microsoft, Apple

## Problem Statement

Given the `root` of a binary tree, the value of a `target` node, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

You can return the answer in any order.

### Examples

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (value 5) have values 7, 4, and 1.
```

**Example 2:**
```
Input: root = [1], target = 1, k = 3
Output: []
```

### Constraints

- The number of nodes in the tree is in the range `[1, 500]`.
- `0 <= Node.val <= 500`
- All the values `Node.val` are unique.
- `target` is the value of one of the nodes in the tree.
- `k >= 0`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Distance definition**: What is distance? (Assumption: Number of edges between nodes - shortest path length)

2. **Target node**: How is target specified? (Assumption: Given target node value - need to find all nodes at distance k from it)

3. **Return format**: What should we return? (Assumption: List of node values at distance k from target)

4. **Tree traversal**: Can we traverse in all directions? (Assumption: Yes - can go up to parent and down to children)

5. **K value**: What if k is 0? (Assumption: Return target node itself - distance 0)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

First, find the target node using DFS. Then, from the target node, perform BFS to find all nodes at distance k. However, this only finds nodes in the subtree rooted at target. To find nodes in other parts of the tree, we need to traverse upward to parents, which requires parent pointers or a second pass to build parent mapping.

**Step 2: Semi-Optimized Approach (7 minutes)**

Build a parent map: first traverse the tree to build a mapping from each node to its parent. Then, from the target node, perform BFS considering both children and parent. This allows us to traverse in all directions (up and down) to find nodes at distance k. This works but requires two passes: one to build parent map, one to do BFS.

**Step 3: Optimized Solution (8 minutes)**

Use BFS with parent map: first find the target node and build parent mapping in one DFS pass. Then perform BFS from target, treating the tree as an undirected graph (can go to children or parent). Use a visited set to avoid revisiting nodes. This achieves O(n) time with O(n) space, which is optimal. The key insight is that we can treat the binary tree as an undirected graph for BFS, allowing us to traverse both up (to parents) and down (to children) to find all nodes at distance k.

## Solution Approaches

### Approach 1: Convert Tree to Graph with DFS

**Key Insight:** Convert the binary tree into an undirected graph, then perform BFS/DFS from the target node to find all nodes at distance k.

**Algorithm:**
1. Build adjacency list by traversing the tree
2. Store parent-child relationships bidirectionally
3. Perform DFS starting from target node
4. Track visited nodes to avoid cycles
5. Collect nodes at exact distance k

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        buildGraph(root, nullptr);
        visited.insert(target->val);
        dfs(target->val, 0, k);
        return rtn;
    }
private:
    unordered_map<int, vector<int>> graph;
    vector<int> rtn;
    unordered_set<int> visited;

    void buildGraph(TreeNode* curr, TreeNode* parent) {
        if(curr && parent) {
            graph[curr->val].push_back(parent->val);
            graph[parent->val].push_back(curr->val);
        }
        if(curr->left) buildGraph(curr->left, curr);
        if(curr->right) buildGraph(curr->right, curr);
    }

    void dfs(int curr, int dist, int K) {
        if(dist == K) {
            rtn.push_back(curr);
            return;
        }
        for(int neighbor: graph[curr]) {
            if(!visited.contains(neighbor)) {
                visited.insert(neighbor);
                dfs(neighbor, dist + 1, K);
            }
        }
    }
};
```

### Approach 2: Parent Pointer Map with DFS

**Key Insight:** Create a parent pointer map to traverse up the tree, then use DFS to explore all neighbors (left, right, parent).

**Algorithm:**
1. Traverse tree to build parent map
2. Start DFS from target node
3. For each node, explore left, right, and parent
4. Track visited nodes
5. Collect nodes at distance k

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        addParent(root, nullptr);
        vector<int> rtn;
        unordered_set<TreeNode*> visited;
        dfs(target, k, rtn, visited);
        return rtn;
    }

private:
    unordered_map<TreeNode*, TreeNode*> parent;
    
    void addParent(TreeNode* curr, TreeNode* parent) {
        if(curr) {
            this->parent[curr] = parent;
            addParent(curr->left, curr);
            addParent(curr->right, curr);
        }
    }

    void dfs(TreeNode* curr, int dist, vector<int>& rtn, unordered_set<TreeNode*>& visited) {
        if(!curr || visited.contains(curr)) return;
        visited.insert(curr);
        if(dist == 0) {
            rtn.push_back(curr->val);
            return;
        }
        dfs(parent[curr], dist - 1, rtn, visited);
        dfs(curr->left, dist - 1, rtn, visited);
        dfs(curr->right, dist - 1, rtn, visited);
    }
};
```

### Approach 3: BFS with Graph Representation

**Algorithm:**
1. Build adjacency list representation
2. Use BFS with queue to find nodes at distance k
3. Track level/distance during traversal
4. Collect nodes exactly at distance k

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        buildGraph(root, nullptr);
        vector<int> rtn;
        queue<pair<int, int>> q;  // {node, distance}
        unordered_set<int> visited;
        
        q.push({target->val, 0});
        visited.insert(target->val);
        
        while(!q.empty()) {
            auto [curr, dist] = q.front();
            q.pop();
            
            if(dist == k) {
                rtn.push_back(curr);
            } else if(dist < k) {
                for(int neighbor: graph[curr]) {
                    if(!visited.contains(neighbor)) {
                        visited.insert(neighbor);
                        q.push({neighbor, dist + 1});
                    }
                }
            }
        }
        return rtn;
    }

private:
    unordered_map<int, vector<int>> graph;
    vector<int> rtn;
    
    void buildGraph(TreeNode* curr, TreeNode* parent) {
        if(curr && parent) {
            graph[curr->val].push_back(parent->val);
            graph[parent->val].push_back(curr->val);
        }
        if(curr->left) buildGraph(curr->left, curr);
        if(curr->right) buildGraph(curr->right, curr);
    }
};
```

## Algorithm Analysis

### Approach Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Graph + DFS | O(n) | O(n) | Simple, intuitive | Extra memory for graph |
| Parent Map + DFS | O(n) | O(n) | No extra graph structure | More complex traversal |
| Graph + BFS | O(n) | O(n) | Level-order traversal | Slightly more code |

### Key Insights

1. **Tree as Graph**: Binary trees are directed acyclic graphs; adding parent pointers makes them undirected
2. **Multi-directional Search**: Can traverse up (parent) and down (children) in tree
3. **Cycle Prevention**: Must track visited nodes to avoid infinite loops
4. **Distance Tracking**: Depth-first or breadth-first approaches both work

## Implementation Details

### Building Parent-Child Relationships
```cpp
// Store bidirectional edges
if(curr && parent) {
    graph[curr->val].push_back(parent->val);
    graph[parent->val].push_back(curr->val);
}
```

### DFS with Distance Control
```cpp
void dfs(int curr, int dist, int K) {
    if(dist == K) {
        rtn.push_back(curr);
        return;
    }
    // Recursively explore all neighbors
    for(int neighbor: graph[curr]) {
        if(!visited.contains(neighbor)) {
            visited.insert(neighbor);
            dfs(neighbor, dist + 1, K);
        }
    }
}
```

### Three-Directional Search
```cpp
// Explore: parent, left child, right child
dfs(parent[curr], dist - 1, rtn, visited);
dfs(curr->left, dist - 1, rtn, visited);
dfs(curr->right, dist - 1, rtn, visited);
```

## Edge Cases

1. **Target is Root**: Still works, no parent path
2. **k = 0**: Returns only target node
3. **Single Node Tree**: Returns empty array if k > 0
4. **k Beyond Tree Depth**: Returns empty array
5. **Target at Leaf**: Must go up to parent then down

## Follow-up Questions

- What if the tree had more than 2 children per node?
- How would you modify for a directed graph?
- What if nodes could have duplicate values?
- How would you find nodes within distance k (not exactly k)?

## Related Problems

- [LC 314: Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/)
- [LC 863: All Nodes Distance K](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) *(This problem)*
- [LC 1161: Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)
- [LC 742: Closest Leaf in a Binary Tree](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/)

## Optimization Techniques

1. **Graph Conversion**: O(n) one-time preprocessing
2. **Visited Tracking**: O(1) lookup prevents redundant work
3. **Early Termination**: Stop at distance k exactly
4. **Bidirectional Edges**: Store parent-child relationships for undirected graph behavior

## Code Quality Notes

1. **Clarity**: Graph approach is most intuitive for new learners
2. **Modularity**: Separate graph building from search logic
3. **Memory**: Both approaches use O(n) space for n nodes
4. **Performance**: All solutions are optimal O(n) time

---

*This problem beautifully demonstrates how binary trees can be treated as graphs when we need multi-directional traversal capabilities.*

