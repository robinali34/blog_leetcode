---
layout: post
title: "[Medium] 429. N-ary Tree Level Order Traversal"
date: 2026-01-07 00:00:00 -0700
categories: [leetcode, medium, tree, bfs, n-ary-tree]
permalink: /2026/01/07/medium-429-n-ary-tree-level-order-traversal/
tags: [leetcode, medium, tree, bfs, level-order-traversal, n-ary-tree]
---
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

## Thinking Process

1. **BFS Structure**: Queue naturally maintains level-by-level order

- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.



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
| Queue BFS | $O(n)$ | $O(n)$ | Shortest path in unweighted graphs |
| Multi-source BFS | $O(n)$ | $O(n)$ | Start from all sources simultaneously |
| 0-1 BFS / deque | $O(n)$ | $O(n)$ | Weights 0 or 1 |
| **Level-order BFS** *(this problem)* | $O(n)$ | $O(w)$ | Process by depth/layer |

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

### Solution Explanation

**Approach:** Level-order BFS (this problem)

**Key idea:** 1. **BFS Structure**: Queue naturally maintains level-by-level order

**How the code works:**
1. **BFS Structure**: Queue naturally maintains level-by-level order
- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

**Walkthrough** — input `root = [1,null,3,2,4,null,5,6]`, expected output `[[1],[3,2,4],[5,6]]`:

Level 0: [1]
Level 1: [3, 2, 4]
Level 2: [5, 6]

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

- [LC 102: Binary Tree Level Order Traversal](https://www.leetcode.com/problems/binary-tree-level-order-traversal/) - Binary tree version
- [LC 103: Binary Tree Zigzag Level Order Traversal](https://www.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) - Zigzag traversal
- [LC 107: Binary Tree Level Order Traversal II](https://www.leetcode.com/problems/binary-tree-level-order-traversal-ii/) - Reverse level order
- [LC 559: Maximum Depth of N-ary Tree](https://www.leetcode.com/problems/maximum-depth-of-n-ary-tree/) - Find depth of N-ary tree

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **BFS Structure**: Queue naturally maintains level-by-level order
2. **Level Size Tracking**: Critical to know when we've finished processing a level
3. **Multiple Children**: Use loop to iterate through `children` vector instead of checking specific child pointers
4. **Same Pattern as Binary Tree**: The algorithm is identical to binary tree level order, just iterate through children instead of left/right

## References

- [LC 429: N-ary Tree Level Order Traversal on LeetCode](https://www.leetcode.com/problems/n-ary-tree-level-order-traversal/)
- [LeetCode Discuss — LC 429: N-ary Tree Level Order Traversal](https://www.leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/n-ary-tree-level-order-traversal/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
