---
layout: post
title: "993. Cousins in Binary Tree"
date: 2026-01-07 00:00:00 -0700
categories: [leetcode, easy, tree, bfs, binary-tree]
permalink: /2026/01/07/easy-993-cousins-in-binary-tree/
tags: [leetcode, easy, tree, bfs, binary-tree, level-order-traversal]
---

# 993. Cousins in Binary Tree

## Problem Statement

Given the `root` of a binary tree with unique values and the values of two different nodes of the tree `x` and `y`, return `true` *if the nodes corresponding to the values* `x` *and* `y` *are **cousins**, or* `false` *otherwise*.

Two nodes of a binary tree are **cousins** if they have the same depth with different parents.

Note that in a binary tree, the root node is at depth `0`, and children of each depth `k` node are at depth `k + 1`.

## Examples

**Example 1:**
```
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Explanation: Nodes 4 and 3 are at the same depth but have the same parent (node 2).
```

**Example 2:**
```
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Explanation: Nodes 5 and 4 are at the same depth and have different parents.
```

**Example 3:**
```
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
Explanation: Nodes 2 and 3 are siblings (same parent), not cousins.
```

## Constraints

- The number of nodes in the tree is in the range `[2, 100]`.
- `1 <= Node.val <= 100`
- Each node has a **unique** value.
- `x != y`
- `x` and `y` are guaranteed to exist in the tree.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Cousin definition**: What are cousins? (Assumption: Nodes at same depth (level) but with different parents - not siblings)

2. **Depth requirement**: What does "same depth" mean? (Assumption: Same distance from root - same level in tree)

3. **Return value**: What should we return? (Assumption: Boolean - true if x and y are cousins, false otherwise)

4. **Node existence**: Are x and y guaranteed to exist? (Assumption: Yes - per constraints, both nodes exist in tree)

5. **Sibling check**: What if nodes are siblings? (Assumption: Return false - cousins must have different parents)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Find the parent and depth of node x, then find the parent and depth of node y. Check if they have the same depth but different parents. To find parent and depth, use DFS or BFS to traverse the tree, tracking parent and depth for each node. This approach works but requires two traversals or careful tracking during one traversal.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use BFS level by level. For each level, check if both x and y are present. If they are in the same level, check if they have different parents. However, tracking parents during BFS requires storing parent information, which adds complexity. Alternatively, use DFS to find both nodes and their properties in one pass.

**Step 3: Optimized Solution (5 minutes)**

Use a single DFS or BFS traversal. For each node, track its depth and parent. When we find x, store its depth and parent. When we find y, store its depth and parent. After traversal, check if depths are equal and parents are different. This achieves O(n) time to visit all nodes and O(h) space for recursion/queue, which is optimal. The key insight is that we can find both nodes' properties in a single traversal by tracking depth and parent information as we explore the tree.

## Solution Approach

This problem requires checking if two nodes are **cousins**, which means:
1. They are at the **same depth** (level)
2. They have **different parents**

### Key Insights:

1. **Cousins Definition**: Same depth, different parents
2. **BFS with Parent Tracking**: Use BFS to traverse level by level, tracking parent for each node
3. **Early Termination**: Once both nodes are found, we can break early
4. **Parent Comparison**: Check if parents are different after finding both nodes

### Algorithm:

1. **Initialize**: Queue with (node, parent) pairs, start with (root, nullptr)
2. **For each level**:
   - Process all nodes at current level
   - Track parent and depth for nodes x and y
   - If both found, break early
3. **Check conditions**: Same depth AND different parents

## Solution

### **Solution: BFS with Parent Tracking**

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        if(!root) return false;

        queue<pair<TreeNode*, TreeNode*>> q;
        q.push({root, nullptr});
        TreeNode *xParent = nullptr, *yParent = nullptr;
        int xDepth = 1, yDepth = -1, depth = 0;
        while(!q.empty()) {
            int size = q.size();
            for(int i = 0; i < size; i++) {
                auto [node, parent] = q.front();
                q.pop();
                if(node->val == x) {
                    xParent = parent;
                    xDepth = depth;
                }
                if(node->val == y) {
                    yParent = parent;
                    yDepth = depth;
                }
                if(node->left) q.push({node->left, node});
                if(node->right) q.push({node->right, node});
            }
            if(xParent && yParent) break;
            depth++;
        }
        return xDepth == yDepth && xParent != yParent;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 4-7)**:
   - Return false if root is null
   - Create queue storing `(node, parent)` pairs
   - Push root with `nullptr` as parent (root has no parent)
   - Initialize tracking variables: `xParent`, `yParent`, `xDepth`, `yDepth`, `depth`

2. **Level Processing (Lines 8-26)**:
   - **For each level**:
     - Get level size before processing
     - **Process each node at current level** (Lines 11-22):
       - Extract node and parent from queue
       - **If node is x**: Store its parent and depth
       - **If node is y**: Store its parent and depth
       - **Add children**: Push left and right children with current node as parent
     - **Early termination** (Line 24): If both nodes found, break early
     - **Increment depth** (Line 25): Move to next level

3. **Check Cousins Condition (Line 27)**:
   - Return `true` if: `xDepth == yDepth` (same depth) AND `xParent != yParent` (different parents)

### **Why This Works:**

- **BFS ensures same level**: All nodes at the same level are processed together
- **Parent tracking**: Storing parent with each node allows us to check if parents differ
- **Early termination**: Once both nodes are found, we can stop searching
- **Depth tracking**: Incrementing depth after each level ensures correct depth calculation

### **Example Walkthrough:**

**For `root = [1,2,3,null,4,null,5], x = 5, y = 4`:**

```
Tree structure:
    1
   / \
  2   3
   \   \
    4   5

Initial: q = [(1, null)], xParent = null, yParent = null, depth = 0

Level 0 (depth = 0):
  size = 1
  Process: [(1, null)]
    - node = 1, parent = null
    - Not x or y
    - Add children: (2, 1), (3, 1)
  q = [(2, 1), (3, 1)]
  depth = 1

Level 1 (depth = 1):
  size = 2
  Process: [(2, 1), (3, 1)]
    - node = 2, parent = 1
      - Not x or y
      - Add child: (4, 2)
    - node = 3, parent = 1
      - Not x or y
      - Add child: (5, 3)
  q = [(4, 2), (5, 3)]
  depth = 2

Level 2 (depth = 2):
  size = 2
  Process: [(4, 2), (5, 3)]
    - node = 4, parent = 2
      - Found y! yParent = 2, yDepth = 2
    - node = 5, parent = 3
      - Found x! xParent = 3, xDepth = 2
  Both found: xParent && yParent = true, break

Check: xDepth == yDepth? 2 == 2? ✓
       xParent != yParent? 3 != 2? ✓
Result: true (they are cousins)
```

### **Complexity Analysis:**

- **Time Complexity:** O(n) where n is the number of nodes
  - Each node is visited at most once
  - Early termination when both nodes are found
- **Space Complexity:** O(n) for the queue
  - Queue stores at most one level of nodes (maximum width of tree)
  - O(1) extra space for tracking variables

## Key Insights

1. **Cousins = Same Depth + Different Parents**: Both conditions must be satisfied
2. **BFS for Level Tracking**: BFS naturally processes nodes level by level
3. **Parent Tracking**: Store parent with each node to compare later
4. **Early Termination**: Break once both nodes are found to optimize

## Edge Cases

1. **Root is one of the nodes**: Root has no parent (nullptr), so it can't be cousin with any other node
2. **Siblings**: Same parent but same depth - not cousins
3. **Different depths**: Different parents but different depths - not cousins
4. **One node not found**: Shouldn't happen per constraints, but handled by initialization

## Related Problems

- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Level order traversal
- [LC 863: All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) - Find nodes at distance k
- [LC 236: Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) - Find LCA

---

*This problem demonstrates BFS with parent tracking to check relationships between nodes in a binary tree.*


