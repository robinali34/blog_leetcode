---
layout: post
title: "101. Symmetric Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-101-symmetric-tree/
tags: [leetcode, easy, tree, dfs, recursion]
---

# 101. Symmetric Tree

## Problem Statement

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Examples

**Example 1:**
```
Input: root = [1,2,2,3,4,4,3]
Output: true

Tree structure:
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```

**Example 2:**
```
Input: root = [1,2,2,null,3,null,3]
Output: false

Tree structure:
      1
     / \
    2   2
     \   \
      3   3
```

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Symmetric definition**: What makes a tree symmetric? (Assumption: Tree is symmetric if it's a mirror image of itself - left subtree mirrors right subtree)

2. **Empty tree**: Is an empty tree considered symmetric? (Assumption: Yes - empty tree is symmetric by definition)

3. **Single node**: Is a tree with only root symmetric? (Assumption: Yes - single node is symmetric)

4. **Value comparison**: Do we compare values or just structure? (Assumption: Both - structure must be mirror and values at mirror positions must be equal)

5. **Tree modification**: Should we modify the tree or just check symmetry? (Assumption: Just check - no modification needed)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Convert the tree to a string representation (e.g., using preorder traversal) for both left and right subtrees, then compare the strings. Alternatively, collect all nodes at each level and check if each level is symmetric. This approach is straightforward but inefficient, requiring O(n) space for string storage and O(n) time for comparison.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use BFS to traverse level by level. For each level, collect all node values (including nulls for missing children) and check if the level array is symmetric. This maintains the level-order structure but requires storing entire levels, which uses O(n) space. The logic for handling null nodes and comparing levels can be complex.

**Step 3: Optimized Solution (5 minutes)**

Use recursive DFS with a helper function that compares two subtrees as mirrors. For the root, check if left and right subtrees are mirrors. For two nodes to be mirrors: their values must be equal, the left child of one must mirror the right child of the other, and vice versa. This approach uses O(h) space for recursion stack where h is the height, and O(n) time to visit all nodes. The recursive solution is elegant and naturally handles the mirror property without extra data structures.

## Solution Approach

This problem requires checking if a binary tree is symmetric (mirror of itself). A tree is symmetric if the left subtree is a mirror image of the right subtree.

### Key Insights:

1. **Mirror Property**: Left subtree must be mirror of right subtree
2. **Recursive Comparison**: Compare left child of left subtree with right child of right subtree (and vice versa)
3. **Base Cases**: Handle null nodes correctly
4. **Helper Function**: Use a helper to compare two subtrees as mirrors

## Solution: Recursive DFS with Helper Function

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
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return isMirror(root->left, root->right);
    }

private:
    bool isMirror(TreeNode* a, TreeNode* b) {
        if(!a && !b) return true;
        if(!a || !b) return false;
        if(a->val != b->val) return false;
        return isMirror(a->left, b->right) &&
                isMirror(a->right, b->left);
    }
};
```

### Algorithm Explanation:

1. **Main Function `isSymmetric`**:
   - If root is `nullptr`, return `true` (empty tree is symmetric)
   - Check if left and right subtrees are mirrors using helper function

2. **Helper Function `isMirror`**:
   - **Base Case - Both Null**: If both `a` and `b` are `nullptr`, return `true`
   - **Base Case - One Null**: If one is null but the other isn't, return `false` (structure mismatch)
   - **Base Case - Value Mismatch**: If both exist but `a->val != b->val`, return `false`
   - **Recursive Case**: 
     - Compare `a->left` with `b->right` (outer nodes)
     - Compare `a->right` with `b->left` (inner nodes)
     - Return `true` only if **both** comparisons succeed (AND operation)

### Why This Works?

For a tree to be symmetric:
- The root's left and right subtrees must be mirrors
- In a mirror comparison:
  - Left child of left subtree ↔ Right child of right subtree (outer)
  - Right child of left subtree ↔ Left child of right subtree (inner)

### Example Walkthrough:

**Example 1:** `root = [1,2,2,3,4,4,3]`

```
Tree structure:
      1
     / \
    2   2
   / \ / \
  3  4 4  3

isSymmetric(1):
  root exists
  Check: isMirror(2, 2)
    a = 2, b = 2
    Both exist, values equal (2 == 2)
    
    Check outer: isMirror(3, 3):
      a = 3, b = 3
      Both exist, values equal (3 == 3)
      
      Check outer: isMirror(null, null):
        Both null → return true
      
      Check inner: isMirror(null, null):
        Both null → return true
      
      return true && true = true
    
    Check inner: isMirror(4, 4):
      a = 4, b = 4
      Both exist, values equal (4 == 4)
      
      Check outer: isMirror(null, null):
        Both null → return true
      
      Check inner: isMirror(null, null):
        Both null → return true
      
      return true && true = true
    
    return true && true = true
  
  return true ✓
```

**Example 2:** `root = [1,2,2,null,3,null,3]`

```
Tree structure:
      1
     / \
    2   2
     \   \
      3   3

isSymmetric(1):
  root exists
  Check: isMirror(2, 2)
    a = 2, b = 2
    Both exist, values equal (2 == 2)
    
    Check outer: isMirror(null, null):
      Both null → return true
    
    Check inner: isMirror(3, 3):
      a = 3, b = 3
      Both exist, values equal (3 == 3)
      
      Check outer: isMirror(null, null):
        Both null → return true
      
      Check inner: isMirror(null, null):
        Both null → return true
      
      return true && true = true
    
    return true && true = true
  
  Wait, this should return false...
  
  Actually, let me reconsider:
    a = 2 (left subtree), b = 2 (right subtree)
    
    Check outer: isMirror(a->left, b->right):
      a->left = null, b->right = 3
      One null, one exists → return false
    
    return true && false = false ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Visit each node exactly once
  - n = number of nodes in tree
  - Early termination when mismatch found

- **Space Complexity:** O(h)
  - Recursion call stack depth = height of tree
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

## Alternative Approaches

### Solution 2: Inline Helper Function

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* a, TreeNode* b) {
        if (!a && !b) return true;
        if (!a || !b) return false;
        return a->val == b->val && 
               isMirror(a->left, b->right) && 
               isMirror(a->right, b->left);
    }
};
```

**Key Difference**: Combines value check with recursive calls using AND

**Complexity**: Same as Solution 1

### Solution 3: Iterative DFS with Stack

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        
        stack<pair<TreeNode*, TreeNode*>> st;
        st.push({root->left, root->right});
        
        while (!st.empty()) {
            auto [a, b] = st.top();
            st.pop();
            
            if (!a && !b) continue;
            if (!a || !b) return false;
            if (a->val != b->val) return false;
            
            st.push({a->right, b->left});
            st.push({a->left, b->right});
        }
        
        return true;
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
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        
        queue<pair<TreeNode*, TreeNode*>> q;
        q.push({root->left, root->right});
        
        while (!q.empty()) {
            auto [a, b] = q.front();
            q.pop();
            
            if (!a && !b) continue;
            if (!a || !b) return false;
            if (a->val != b->val) return false;
            
            q.push({a->left, b->right});
            q.push({a->right, b->left});
        }
        
        return true;
    }
};
```

**Complexity**: 
- Time: O(n)
- Space: O(w) where w is maximum width

## Key Insights

1. **Mirror Comparison**: Compare left subtree with right subtree as mirrors
2. **Cross Comparison**: 
   - `a->left` ↔ `b->right` (outer nodes)
   - `a->right` ↔ `b->left` (inner nodes)
3. **Three Base Cases**: Both null, one null, or value mismatch
4. **AND Logic**: Both comparisons must succeed for symmetry
5. **Empty Tree**: Empty tree is symmetric

## Edge Cases

1. **Empty tree**: `root = []` → return `true`
2. **Single node**: `root = [1]` → return `true`
3. **Symmetric tree**: `[1,2,2,3,4,4,3]` → return `true`
4. **Asymmetric structure**: `[1,2,2,null,3,null,3]` → return `false`
5. **Asymmetric values**: `[1,2,2,3,4,5,3]` → return `false`
6. **One child**: `[1,2,null]` → return `false`

## Common Mistakes

1. **Wrong comparison order**: Comparing `a->left` with `b->left` instead of `b->right`
   ```cpp
   // WRONG:
   return isMirror(a->left, b->left) && isMirror(a->right, b->right);
   // ❌ This checks if trees are identical, not mirrors
   ```

2. **Not handling null correctly**: Accessing values before null check
3. **Wrong logic operator**: Using OR instead of AND
4. **Missing value check**: Only checking structure, not values
5. **Comparing same side**: Forgetting to cross-compare (left with right)

## Comparison with Related Problems

| Problem | Key Difference |
|---------|----------------|
| **LC 101: Symmetric Tree** | Check if tree is **mirror of itself** |
| **LC 100: Same Tree** | Check if two trees are **completely identical** |
| **LC 226: Invert Binary Tree** | **Mirror** a tree (swap left/right) |
| **LC 572: Subtree of Another Tree** | Check if one tree is **subtree** of another |

## Related Problems

- [LC 101: Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) - This problem
- [LC 100: Same Tree](https://leetcode.com/problems/same-tree/) - Check if two trees are identical
- [LC 226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) - Mirror a binary tree
- [LC 572: Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) - Check if subtree exists
- [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Find maximum depth
- [LC 110: Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) - Check if tree is balanced

---

*This problem demonstrates **mirror comparison** in binary trees. The key insight is comparing the left subtree with the right subtree as mirrors, which requires cross-comparing nodes: `a->left` with `b->right` and `a->right` with `b->left`. It's closely related to LC 100 (Same Tree) but with mirror logic instead of identical comparison.*

