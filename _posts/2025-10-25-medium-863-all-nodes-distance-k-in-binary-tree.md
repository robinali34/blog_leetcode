---
layout: post
title: "[Medium] 863. All Nodes Distance K in Binary Tree"
date: 2025-10-25 13:00:00 -0700
categories: leetcode medium tree dfs bfs
permalink: /posts/2025-10-25-medium-863-all-nodes-distance-k-in-binary-tree/
tags: [leetcode, medium, tree, binary-tree, dfs, bfs, graph, recursion]
---
**Difficulty:** Medium  
**Category:** Tree, DFS, BFS  
**Companies:** Amazon, Facebook, Google, Microsoft, Apple

Given the `root` of a binary tree, the value of a `target` node, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

You can return the answer in any order.

## Examples
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

## Constraints
- The number of nodes in the tree is in the range `[1, 500]`.
- `0 <= Node.val <= 500`
- All the values `Node.val` are unique.
- `target` is the value of one of the nodes in the tree.
- `k >= 0`

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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** Difficulty:** Medium

**How the code works:**
**Difficulty:** Medium
**Category:** Tree, DFS, BFS
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2`, expected output `[7,4,1]`:

The nodes that are a distance 2 from the target node (value 5) have values 7, 4, and 1.
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [LC 314: Binary Tree Vertical Order Traversal](https://www.leetcode.com/problems/binary-tree-vertical-order-traversal/)
- [LC 863: All Nodes Distance K](https://www.leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) *(This problem)*
- [LC 1161: Maximum Level Sum of a Binary Tree](https://www.leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)
- [LC 742: Closest Leaf in a Binary Tree](https://www.leetcode.com/problems/closest-leaf-in-a-binary-tree/)

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

## Key Takeaways

- **Pattern:** Recursive DFS (this problem)
- Difficulty:** Medium
- Category:** Tree, DFS, BFS

## References

- [LC 863: All Nodes Distance K in Binary Tree on LeetCode](https://www.leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
- [LeetCode Discuss — LC 863: All Nodes Distance K in Binary Tree](https://www.leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/all-nodes-distance-k-in-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)

## Thinking Process

**Difficulty:** Medium

**Category:** Tree, DFS, BFS

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
