---
layout: post
title: "104. Maximum Depth of Binary Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-104-maximum-depth-of-binary-tree/
tags: [leetcode, easy, tree, dfs, bfs, recursion]
---

# 104. Maximum Depth of Binary Tree

## Problem Statement

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
Explanation: The maximum depth is 3, which is the path: 3 → 20 → 15 (or 3 → 20 → 7).
```

**Example 2:**
```
Input: root = [1,null,2]
Output: 2
Explanation: The maximum depth is 2, which is the path: 1 → 2.
```

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Tree type**: Is this a binary tree, BST, or general tree? (Assumption: Binary tree - each node has at most 2 children)

2. **Depth definition**: How is depth defined - number of nodes or number of edges? (Assumption: Typically depth = number of nodes from root to deepest leaf, but should clarify)

3. **Empty tree**: What should we return for an empty tree (null root)? (Assumption: Return 0 - no nodes means depth 0)

4. **Single node**: What's the depth of a tree with only root? (Assumption: Return 1 - root node itself has depth 1)

5. **Tree modification**: Should we modify the tree or just traverse it? (Assumption: Just traverse - no modification needed)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Use BFS to traverse level by level, counting the number of levels. Alternatively, use DFS to explore all paths and track the maximum depth reached. This straightforward approach works but may require maintaining additional state or using extra space for level tracking.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use iterative BFS with a queue, processing nodes level by level. Maintain a depth counter and increment it after processing each level. This requires O(n) time and O(w) space where w is the maximum width. Alternatively, use iterative DFS with a stack, maintaining depth for each node, but this is more complex.

**Step 3: Optimized Solution (5 minutes)**

Use recursive DFS: for each node, recursively find the maximum depth of left and right subtrees, then return 1 + max(left_depth, right_depth). Base case: if node is null, return 0. This achieves O(n) time to visit all nodes and O(h) space for recursion stack where h is height, which is optimal. The recursive solution is elegant and naturally handles the tree structure without extra data structures beyond the call stack.

## Solution Approach

This problem requires finding the longest path from root to any leaf node. There are several approaches:

1. **Recursive DFS with Depth Tracking**: Track current depth and return maximum
2. **Recursive DFS (Post-order)**: Return depth from bottom up
3. **Iterative BFS**: Level-order traversal counting levels
4. **Iterative DFS**: Use stack to simulate recursion

### Key Insights:

1. **Depth Definition**: Number of nodes from root to leaf (not edges)
2. **Recursive Structure**: Max depth = 1 + max(left_depth, right_depth)
3. **Base Case**: Empty tree has depth 0
4. **Leaf Node**: Node with no children contributes depth 1

## Solution: Recursive DFS with Depth Tracking

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
    int maxDepth(TreeNode* root) {
        return dfs(root, 0);
    }
    
private:
    int dfs(TreeNode* node, int maxDepth) {
        if(!node) return maxDepth;
        return max(dfs(node->left, maxDepth + 1), dfs(node->right, maxDepth + 1));
    }
};
```

### Algorithm Explanation:

1. **Base Case**: If node is `nullptr`, return current `maxDepth` (no increment)

2. **Recursive Case**: 
   - For each non-null node, increment depth by 1
   - Recursively explore left and right subtrees
   - Return the maximum depth from both subtrees

3. **Depth Tracking**: 
   - `maxDepth` parameter tracks current depth from root
   - Each recursive call increments depth by 1
   - Leaf nodes return their depth (no children to explore)

### Example Walkthrough:

**Input:** `root = [3,9,20,null,null,15,7]`

```
Tree structure:
      3
     / \
    9   20
       /  \
      15   7

dfs(3, 0):
  node = 3, maxDepth = 0
  left = dfs(9, 1)
    node = 9, maxDepth = 1
    left = dfs(null, 2) → return 2
    right = dfs(null, 2) → return 2
    return max(2, 2) = 2
  
  right = dfs(20, 1)
    node = 20, maxDepth = 1
    left = dfs(15, 2)
      node = 15, maxDepth = 2
      left = dfs(null, 3) → return 3
      right = dfs(null, 3) → return 3
      return max(3, 3) = 3
    
    right = dfs(7, 2)
      node = 7, maxDepth = 2
      left = dfs(null, 3) → return 3
      right = dfs(null, 3) → return 3
      return max(3, 3) = 3
    
    return max(3, 3) = 3
  
  return max(2, 3) = 3 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Visit each node exactly once
  - n = number of nodes in tree

- **Space Complexity:** O(h)
  - Recursion call stack depth = height of tree
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

## Alternative Approaches

### Solution 2: Standard Recursive DFS (Post-order)

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        return max(leftDepth, rightDepth) + 1;
    }
};
```

**Key Difference**: 
- Returns depth from bottom up (post-order)
- Simpler: no depth parameter needed
- Base case returns 0 for null, then adds 1 at each level

**Complexity**: Same as Solution 1

### Solution 3: Iterative BFS (Level-order Traversal)

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        
        queue<TreeNode*> q;
        q.push(root);
        int depth = 0;
        
        while (!q.empty()) {
            int levelSize = q.size();
            depth++;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return depth;
    }
};
```

**Algorithm**:
1. Use queue for level-order traversal
2. Process all nodes at current level
3. Increment depth for each level
4. Add children to queue for next level

**Complexity**:
- Time: O(n) - visit each node once
- Space: O(w) - where w is maximum width (worst case O(n))

### Solution 4: Iterative DFS with Stack

```cpp
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        
        stack<pair<TreeNode*, int>> st;
        st.push({root, 1});
        int maxDepth = 0;
        
        while (!st.empty()) {
            auto [node, depth] = st.top();
            st.pop();
            
            maxDepth = max(maxDepth, depth);
            
            if (node->right) st.push({node->right, depth + 1});
            if (node->left) st.push({node->left, depth + 1});
        }
        
        return maxDepth;
    }
};
```

**Complexity**: Same as recursive DFS

## Key Insights

1. **Depth vs Height**: 
   - Depth: distance from root (this problem)
   - Height: distance from leaf (often same value)

2. **Recursive Structure**: 
   - Max depth = 1 + max(left_depth, right_depth)
   - Base case: null node returns 0

3. **Top-down vs Bottom-up**:
   - Top-down: Pass depth parameter down (Solution 1)
   - Bottom-up: Return depth from children (Solution 2)

4. **Tree Traversal**:
   - DFS: Natural for depth calculation
   - BFS: Count levels for depth

## Edge Cases

1. **Empty tree**: `root = null` → return `0`
2. **Single node**: `root = [1]` → return `1`
3. **Skewed tree**: `[1,2,null,3,null,4]` → return `4`
4. **Balanced tree**: `[3,9,20,null,null,15,7]` → return `3`
5. **Left-only tree**: `[1,2,null,3]` → return `3`

## Common Mistakes

1. **Wrong base case**: Returning `-1` or `1` for null instead of `0`
2. **Off-by-one error**: Counting edges instead of nodes
3. **Not handling null**: Accessing children without null check
4. **Wrong return**: Returning `maxDepth` instead of `max(left, right) + 1`
5. **Stack overflow**: Deep recursion without iterative alternative

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DFS with Depth Tracking** | O(n) | O(h) | Explicit depth tracking | Extra parameter |
| **Standard Recursive DFS** | O(n) | O(h) | Simplest, most elegant | Recursion overhead |
| **Iterative BFS** | O(n) | O(w) | No recursion, level-by-level | More code, queue space |
| **Iterative DFS** | O(n) | O(h) | No recursion | More complex than recursive |

## When to Use Each Approach

- **Standard Recursive DFS**: Most common, simplest solution
- **DFS with Depth Tracking**: When you need current depth during traversal
- **Iterative BFS**: When recursion depth is a concern, or need level information
- **Iterative DFS**: When avoiding recursion, similar to recursive logic

## Related Problems

- [LC 111: Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) - Find minimum depth
- [LC 110: Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) - Check if tree is balanced
- [LC 543: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) - Longest path between any two nodes
- [LC 559: Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) - Extension to N-ary tree
- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - BFS traversal

---

*This problem demonstrates fundamental **tree traversal** techniques. The recursive DFS approach elegantly captures the recursive nature of trees: the depth of a tree is one more than the maximum depth of its subtrees.*

