---
layout: post
title: "226. Invert Binary Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-226-invert-binary-tree/
tags: [leetcode, easy, tree, dfs, recursion]
---

# 226. Invert Binary Tree

## Problem Statement

Given the `root` of a binary tree, invert the tree, and return *its root*.

## Examples

**Example 1:**
```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Before inversion:
      4
     / \
    2   7
   / \ / \
  1  3 6  9

After inversion:
      4
     / \
    7   2
   / \ / \
  9  6 3  1
```

**Example 2:**
```
Input: root = [2,1,3]
Output: [2,3,1]

Before inversion:
    2
   / \
  1   3

After inversion:
    2
   / \
  3   1
```

**Example 3:**
```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Inversion definition**: What exactly does "invert" mean? (Assumption: Swap left and right children for every node in the tree)

2. **Tree modification**: Should we modify the tree in-place or return a new tree? (Assumption: Modify in-place - return the root of the modified tree)

3. **Empty tree**: What should we return for an empty tree? (Assumption: Return null - no tree to invert)

4. **Single node**: What happens with a tree containing only root? (Assumption: Return root unchanged - no children to swap)

5. **Recursive vs iterative**: Are there any constraints on using recursion? (Assumption: No - recursion is fine, but iterative approach also works)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Create a new tree with the same structure but swapped children. Traverse the original tree, and for each node, create a new node with left and right children swapped. This approach works but requires O(n) extra space for the new tree and O(n) time to build it. Since we're modifying in-place, this isn't necessary.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use iterative BFS with a queue. Process nodes level by level, swapping left and right children for each node, then enqueue both children. This approach uses O(w) space where w is the maximum width of the tree, and O(n) time. It works well but requires maintaining a queue data structure.

**Step 3: Optimized Solution (5 minutes)**

Use recursive DFS: for each node, recursively invert the left and right subtrees, then swap the left and right children of the current node. Base case: if node is null, return null. This approach uses O(h) space for the recursion stack where h is the height, and O(n) time to visit all nodes. The recursive solution is elegant, naturally handles the tree structure, and modifies the tree in-place without extra data structures beyond the call stack.

## Solution Approach

This problem requires swapping the left and right children of every node in the tree. We can use a recursive DFS approach to traverse the tree and swap children at each node.

### Key Insights:

1. **Swap Children**: For each node, swap its left and right children
2. **Recursive Traversal**: Process subtrees recursively
3. **Base Case**: Empty node (null) requires no action
4. **In-Place Modification**: Modify the tree structure directly

## Solution: Recursive DFS

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
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return root;
        TreeNode* tmp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(tmp);
        return root;
    }
};
```

### Algorithm Explanation:

1. **Base Case**: 
   - If `root` is `nullptr`, return `root` (no action needed)

2. **Swap Children**:
   - Store `root->left` in a temporary variable `tmp`
   - Recursively invert `root->right` and assign to `root->left`
   - Recursively invert the original `root->left` (stored in `tmp`) and assign to `root->right`

3. **Return**: Return the modified root node

### Why This Works?

The algorithm uses **post-order traversal** (process children before parent):
- First, recursively invert both subtrees
- Then swap the already-inverted subtrees
- This ensures all nodes below are inverted before swapping

**Alternative interpretation**: The algorithm swaps children and then recursively inverts the swapped subtrees, which is equivalent to inverting subtrees first then swapping.

### Example Walkthrough:

**Input:** `root = [4,2,7,1,3,6,9]`

```
Initial tree:
      4
     / \
    2   7
   / \ / \
  1  3 6  9

invertTree(4):
  root = 4, has children
  tmp = 2 (left child)
  
  root->left = invertTree(7):
    root = 7, has children
    tmp = 6 (left child)
    
    root->left = invertTree(9):
      root = 9, leaf node
      return 9
    
    root->right = invertTree(6):
      root = 6, leaf node
      return 6
    
    After swap: 7 has children (9, 6)
    return 7
  
  root->right = invertTree(2):
    root = 2, has children
    tmp = 1 (left child)
    
    root->left = invertTree(3):
      root = 3, leaf node
      return 3
    
    root->right = invertTree(1):
      root = 1, leaf node
      return 1
    
    After swap: 2 has children (3, 1)
    return 2
  
  After swap: 4 has children (7, 2)
  return 4

Final tree:
      4
     / \
    7   2
   / \ / \
  9  6 3  1
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

### Solution 2: Simplified Recursive DFS

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;
        
        TreeNode* left = invertTree(root->left);
        TreeNode* right = invertTree(root->right);
        
        root->left = right;
        root->right = left;
        
        return root;
    }
};
```

**Key Difference**: More explicit - invert subtrees first, then swap

**Complexity**: Same as Solution 1

### Solution 3: Iterative DFS with Stack

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;
        
        stack<TreeNode*> st;
        st.push(root);
        
        while (!st.empty()) {
            TreeNode* node = st.top();
            st.pop();
            
            // Swap children
            TreeNode* tmp = node->left;
            node->left = node->right;
            node->right = tmp;
            
            // Push children to stack
            if (node->left) st.push(node->left);
            if (node->right) st.push(node->right);
        }
        
        return root;
    }
};
```

**Complexity**: 
- Time: O(n)
- Space: O(h) for stack

### Solution 4: Iterative BFS with Queue

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            
            // Swap children
            TreeNode* tmp = node->left;
            node->left = node->right;
            node->right = tmp;
            
            // Enqueue children
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        
        return root;
    }
};
```

**Complexity**: 
- Time: O(n)
- Space: O(w) where w is maximum width

## Key Insights

1. **Post-order Traversal**: Process children before parent (or swap then recurse)
2. **In-Place Modification**: Modify tree structure directly, no need for new tree
3. **Symmetric Operation**: Swapping is symmetric - order doesn't matter
4. **Base Case**: Empty node requires no action
5. **Return Root**: Always return the root node after modification

## Edge Cases

1. **Empty tree**: `root = null` → return `null`
2. **Single node**: `root = [1]` → return `[1]` (no change)
3. **Skewed tree**: `[1,2,null]` → becomes `[1,null,2]`
4. **Balanced tree**: Works correctly for any balanced tree
5. **Large tree**: Handles up to 100 nodes efficiently

## Common Mistakes

1. **Not handling null**: Forgetting to check for empty node
   ```cpp
   // WRONG:
   TreeNode* tmp = root->left; // ❌ Crashes if root is null
   ```

2. **Wrong traversal order**: Processing parent before children (pre-order)
3. **Creating new nodes**: Unnecessarily creating new tree instead of modifying in-place
4. **Not returning root**: Forgetting to return the modified root
5. **Swapping before recursion**: Should swap after or during recursion

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Recursive DFS (Provided)** | O(n) | O(h) | Clean, concise | Recursion overhead |
| **Simplified Recursive DFS** | O(n) | O(h) | More explicit | Same as above |
| **Iterative DFS** | O(n) | O(h) | No recursion overhead | More code |
| **Iterative BFS** | O(n) | O(w) | Level-order traversal | More space for wide trees |

## When to Use Each Approach

- **Recursive DFS**: Most common, simplest solution (recommended)
- **Iterative DFS**: When avoiding recursion or stack overflow concerns
- **Iterative BFS**: When level-order processing is preferred

## Related Problems

- [LC 226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) - This problem
- [LC 100: Same Tree](https://leetcode.com/problems/same-tree/) - Check if two trees are identical
- [LC 101: Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) - Check if tree is symmetric
- [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Find maximum depth
- [LC 111: Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) - Find minimum depth
- [LC 617: Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/) - Merge two trees

---

*This problem demonstrates **tree manipulation** using recursive DFS. The key insight is swapping children at each node while recursively processing subtrees. It's a fundamental tree operation that appears in many tree problems.*

