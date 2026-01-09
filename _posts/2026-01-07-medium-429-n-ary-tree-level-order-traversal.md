---
layout: post
title: "429. N-ary Tree Level Order Traversal"
date: 2026-01-07 00:00:00 -0700
categories: [leetcode, medium, tree, bfs, n-ary-tree]
permalink: /2026/01/07/medium-429-n-ary-tree-level-order-traversal/
tags: [leetcode, medium, tree, bfs, level-order-traversal, n-ary-tree]
---

# 429. N-ary Tree Level Order Traversal

## Problem Statement

Given an n-ary tree, return *the level order traversal of its nodes' values*.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

## Examples

**Example 1:**
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Explanation:
Level 0: [1]
Level 1: [3, 2, 4]
Level 2: [5, 6]
```

**Example 2:**
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

## Constraints

- The height of the n-ary tree is less than or equal to `1000`
- The total number of nodes is between `[0, 10^4]`

## Solution Approach

This is a classic **BFS (Breadth-First Search)** problem for N-ary trees. The key insight is to:
1. Use a queue to traverse the tree level by level
2. Process all nodes at the current level before moving to the next
3. Track the level size to know when we've processed all nodes at a level
4. Handle multiple children per node (unlike binary trees with only left/right)

### Key Insights:

1. **Level-by-Level Processing**: Process all nodes at the current level before moving to the next
2. **Queue for BFS**: Use a queue to maintain the order of nodes to be processed
3. **Level Size Tracking**: Store the queue size before processing a level to know how many nodes belong to that level
4. **Multiple Children**: Iterate through `children` vector instead of checking left/right

### Algorithm:

1. **Initialize**: Create result vector and queue, push root if it exists
2. **For each level**:
   - Get current level size (number of nodes at this level)
   - Process all nodes at current level
   - Add their values to the level vector
   - Add all their children to the queue for next level
3. **Return**: Result vector containing all levels

## Solution

### **Solution: BFS with Queue**

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> rtn;
        if(!root) return rtn;
        queue<Node*> q;
        q.push(root);
        while(!q.empty()) {
            vector<int> level;
            int levelSize = q.size();
            for(int i = 0; i < levelSize; i++) {
                Node* curr = q.front();
                q.pop();
                level.push_back(curr->val);
                for(auto& child: curr->children) {
                    q.push(child);
                }
            }
            rtn.push_back(level);
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 3-5)**:
   - Create empty result vector
   - Return empty result if root is null
   - Initialize queue and push root node

2. **Level Processing (Lines 6-20)**:
   - **For each level**:
     - **Get level size** (Line 8): Store `q.size()` before processing - this is the number of nodes at current level
     - **Create level vector** (Line 7): Empty vector to collect values for this level
     - **Process each node at current level** (Lines 9-16):
       - Remove node from front of queue
       - Add node value to level vector
       - **Iterate through all children** (Lines 14-16):
         - Add each child to queue for next level
     - **Add completed level** (Line 18): Push level vector to result

3. **Return (Line 21)**: Return the level order traversal

### **Why This Works:**

- **Queue maintains order**: FIFO ensures nodes are processed level by level
- **Level size tracking**: By storing `q.size()` before the loop, we know exactly how many nodes belong to the current level
- **Children added for next level**: Children are added to the queue but won't be processed until the next iteration
- **Multiple children handling**: Iterating through `children` vector handles any number of children per node

### **Example Walkthrough:**

**For `root = [1,null,3,2,4,null,5,6]`:**

```
Tree structure:
    1
  / | \
 3  2  4
/ \
5  6

Initial: q = [1], rtn = []

Level 0:
  levelSize = 1
  Process: [1]
    - curr = 1, add 1 to level
    - Add children [3, 2, 4] to queue
  level = [1]
  q = [3, 2, 4]
  rtn = [[1]]

Level 1:
  levelSize = 3
  Process: [3, 2, 4]
    - curr = 3, add 3 to level, add children [5, 6] to queue
    - curr = 2, add 2 to level, no children
    - curr = 4, add 4 to level, no children
  level = [3, 2, 4]
  q = [5, 6]
  rtn = [[1], [3, 2, 4]]

Level 2:
  levelSize = 2
  Process: [5, 6]
    - curr = 5, add 5 to level, no children
    - curr = 6, add 6 to level, no children
  level = [5, 6]
  q = []
  rtn = [[1], [3, 2, 4], [5, 6]]

Queue empty, return result
```

### **Complexity Analysis:**

- **Time Complexity:** O(n) where n is the number of nodes
  - Each node is visited exactly once
  - Each node is enqueued and dequeued once
  - Each edge (parent-child relationship) is processed once
- **Space Complexity:** O(n) for the result and O(w) for the queue where w is maximum width
  - Result stores all n node values
  - Queue stores at most one level of nodes (maximum width of tree)

## Key Insights

1. **BFS Structure**: Queue naturally maintains level-by-level order
2. **Level Size Tracking**: Critical to know when we've finished processing a level
3. **Multiple Children**: Use loop to iterate through `children` vector instead of checking specific child pointers
4. **Same Pattern as Binary Tree**: The algorithm is identical to binary tree level order, just iterate through children instead of left/right

## Comparison with Binary Tree Level Order

**Similarities:**
- Same BFS approach with queue
- Same level size tracking technique
- Same time and space complexity

**Differences:**
- **Binary Tree**: Check `left` and `right` children explicitly
- **N-ary Tree**: Iterate through `children` vector
- **N-ary Tree**: Can have any number of children (0 to many)

## Related Problems

- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Binary tree version
- [LC 103: Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) - Zigzag traversal
- [LC 107: Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) - Reverse level order
- [LC 559: Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) - Find depth of N-ary tree

---

*This problem demonstrates the BFS pattern for N-ary trees, which extends naturally from binary tree level order traversal.*


