---
layout: post
title: "[Medium] 314. Binary Tree Vertical Order Traversal"
date: 2025-10-20 15:00:00 -0700
categories: [leetcode, medium, tree, bfs, vertical-order]
permalink: /2025/10/20/medium-314-binary-tree-vertical-order-traversal/
---
Given the root of a binary tree, return the **vertical order traversal** of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from **left to right**.

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9
Column  0: Nodes 3 and 15
Column  1: Only node 20
Column  2: Only node 7
```

**Example 2:**
```
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
```

**Example 3:**
```
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Thinking Process

Given the root of a binary tree, return the **vertical order traversal** of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from **left to right**.

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
| Queue BFS | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| **Level-order BFS** *(this problem)* | O(n) | O(w) | Process by depth/layer |

## Solution

### **Solution: BFS with Column Tracking**

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
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> rtn;
        if(!root) return rtn;
        map<int, vector<int>> map;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        while(!q.empty()) {
            int size = q.size();
            for(int i = 0; i < (int)q.size(); i++) {
                TreeNode* curr = q.front().first;
                int dir = q.front().second;
                q.pop();
                map[dir].push_back(curr->val);
                if(curr->left) q.push({curr->left, dir - 1});
                if(curr->right) q.push({curr->right, dir + 1});
            }
        }
        for(auto& [node, vals]: map) {
            rtn.push_back(vals);
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Level-order BFS (this problem)

**Key idea:** Given the root of a binary tree, return the **vertical order traversal** of its nodes' values. (i.e., from top to bottom, column by column).

**How the code works:**
- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

**Walkthrough** — input `root = [3,9,20,null,null,15,7]`, expected output `[[9],[3,15],[20],[7]]`:

Column -1: Only node 9
Column  0: Nodes 3 and 15
Column  1: Only node 20
Column  2: Only node 7

### **Algorithm Explanation:**

1. **Initialize**: Create empty result vector and map for column grouping
2. **BFS setup**: Start with root at column 0
3. **Level processing**: For each level, process all nodes at that level
4. **Column assignment**: 
   - Left child: `column - 1`
   - Right child: `column + 1`
5. **Grouping**: Add node values to their respective columns
6. **Result construction**: Convert map to result vector in sorted column order

### **Example Walkthrough:**

**For `root = [3,9,20,null,null,15,7]`:**

```
Tree structure:
    3
   / \
  9   20
     /  \
    15   7

Column assignment:
    3 (col=0)
   / \
  9   20
(col=-1) (col=1)
     /  \
    15   7
(col=0) (col=2)

BFS Process:
Level 0: [(3,0)] → map[0] = [3]
Level 1: [(9,-1), (20,1)] → map[-1] = [9], map[1] = [20]
Level 2: [(15,0), (7,2)] → map[0] = [3,15], map[2] = [7]

Final map: {-1: [9], 0: [3,15], 1: [20], 2: [7]}
Result: [[9], [3,15], [20], [7]]
```

### **Time Complexity:** O(n log n)
- **BFS traversal**: O(n) - visit each node once
- **Map operations**: O(log n) per insertion (map is sorted)
- **Total**: O(n log n)

### **Space Complexity:** O(n)
- **Queue**: O(n) - maximum width of tree
- **Map**: O(n) - stores all node values
- **Result**: O(n) - output vector
- **Total**: O(n)
## Key Points

1. **BFS for level order**: Maintains top-to-bottom order within columns
2. **Column tracking**: Use integer column indices for grouping
3. **Map for grouping**: Automatically sorts columns from left to right
4. **Level-by-level processing**: Ensures proper ordering within columns
5. **Edge case handling**: Return empty vector for null root

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [987. Vertical Order Traversal of a Binary Tree](https://www.leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) - More complex ordering rules
- [102. Binary Tree Level Order Traversal](https://www.leetcode.com/problems/binary-tree-level-order-traversal/) - Level order traversal
- [199. Binary Tree Right Side View](https://www.leetcode.com/problems/binary-tree-right-side-view/) - Right view traversal

## Tags

`Tree`, `BFS`, `Vertical Order`, `Level Order`, `Medium`

## Key Takeaways

- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

## References

- [LC 314: Binary Tree Vertical Order Traversal on LeetCode](https://www.leetcode.com/problems/binary-tree-vertical-order-traversal/)
- [LeetCode Discuss — LC 314: Binary Tree Vertical Order Traversal](https://www.leetcode.com/problems/binary-tree-vertical-order-traversal/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/binary-tree-vertical-order-traversal/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
