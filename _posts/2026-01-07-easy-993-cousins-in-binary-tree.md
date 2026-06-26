---
layout: post
title: "[Easy] 993. Cousins in Binary Tree"
date: 2026-01-07 00:00:00 -0700
categories: [leetcode, easy, tree, bfs, binary-tree]
permalink: /2026/01/07/easy-993-cousins-in-binary-tree/
tags: [leetcode, easy, tree, bfs, binary-tree, level-order-traversal]
---
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

## Thinking Process

1. **Cousins = Same Depth + Different Parents**: Both conditions must be satisfied

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
| **Queue BFS** *(this problem)* | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| Level-order BFS | O(n) | O(w) | Process by depth/layer |

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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** 1. **Cousins = Same Depth + Different Parents**: Both conditions must be satisfied

**How the code works:**
1. **Cousins = Same Depth + Different Parents**: Both conditions must be satisfied
- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

**Walkthrough** — input `root = [1,2,3,4], x = 4, y = 3`, expected output `false`:

Nodes 4 and 3 are at the same depth but have the same parent (node 2).

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
## Edge Cases

1. **Root is one of the nodes**: Root has no parent (nullptr), so it can't be cousin with any other node
2. **Siblings**: Same parent but same depth - not cousins
3. **Different depths**: Different parents but different depths - not cousins
4. **One node not found**: Shouldn't happen per constraints, but handled by initialization

## Related Problems

- [LC 102: Binary Tree Level Order Traversal](https://www.leetcode.com/problems/binary-tree-level-order-traversal/) - Level order traversal
- [LC 863: All Nodes Distance K in Binary Tree](https://www.leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) - Find nodes at distance k
- [LC 236: Lowest Common Ancestor of a Binary Tree](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) - Find LCA

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Cousins = Same Depth + Different Parents**: Both conditions must be satisfied
2. **BFS for Level Tracking**: BFS naturally processes nodes level by level
3. **Parent Tracking**: Store parent with each node to compare later
4. **Early Termination**: Break once both nodes are found to optimize

## References

- [LC 993: Cousins in Binary Tree on LeetCode](https://www.leetcode.com/problems/cousins-in-binary-tree/)
- [LeetCode Discuss — LC 993: Cousins in Binary Tree](https://www.leetcode.com/problems/cousins-in-binary-tree/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/cousins-in-binary-tree/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
