---
layout: post
title: "100. Same Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-100-same-tree/
tags: [leetcode, easy, tree, dfs, recursion]
---

# 100. Same Tree

## Problem Statement

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are **structurally identical**, and the nodes have the **same value**.

## Examples

**Example 1:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true

Tree p:        Tree q:
    1              1
   / \            / \
  2   3          2   3
```

**Example 2:**
```
Input: p = [1,2], q = [1,null,2]
Output: false

Tree p:        Tree q:
    1              1
   /                 \
  2                   2
```

**Example 3:**
```
Input: p = [1,2,1], q = [1,1,2]
Output: false

Tree p:        Tree q:
    1              1
   / \            / \
  2   1          1   2
```

## Constraints

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Solution Approach

This problem requires checking if two binary trees are identical in both structure and values. We can use a recursive DFS approach to compare nodes at corresponding positions.

### Key Insights:

1. **Structural Identity**: Both trees must have the same structure (same nodes at same positions)
2. **Value Identity**: Corresponding nodes must have the same values
3. **Recursive Comparison**: Compare root values, then recursively compare left and right subtrees
4. **Base Cases**: Handle null nodes correctly

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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q) return true;
        if(!p || !q || p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

### Algorithm Explanation:

1. **Base Case - Both Null**:
   - If both `p` and `q` are `nullptr`, they are identical → return `true`

2. **Base Case - One Null or Value Mismatch**:
   - If one is null but the other isn't → return `false` (structure mismatch)
   - If both exist but `p->val != q->val` → return `false` (value mismatch)
   - Combined check: `if(!p || !q || p->val != q->val) return false;`

3. **Recursive Case**:
   - Both nodes exist and have same value
   - Recursively check left subtrees: `isSameTree(p->left, q->left)`
   - Recursively check right subtrees: `isSameTree(p->right, q->right)`
   - Return `true` only if **both** subtrees are identical (AND operation)

### Why This Works?

The algorithm uses **pre-order traversal** (check current node, then children):
- First check if current nodes match (structure and value)
- Then recursively verify both subtrees match
- All nodes must match for trees to be identical

### Example Walkthrough:

**Example 1:** `p = [1,2,3]`, `q = [1,2,3]`

```
Tree p:        Tree q:
    1              1
   / \            / \
  2   3          2   3

isSameTree(1, 1):
  Both exist, values equal (1 == 1)
  
  Check left: isSameTree(2, 2):
    Both exist, values equal (2 == 2)
    
    Check left: isSameTree(null, null):
      Both null → return true
    
    Check right: isSameTree(null, null):
      Both null → return true
    
    return true && true = true
  
  Check right: isSameTree(3, 3):
    Both exist, values equal (3 == 3)
    
    Check left: isSameTree(null, null):
      Both null → return true
    
    Check right: isSameTree(null, null):
      Both null → return true
    
    return true && true = true
  
  return true && true = true ✓
```

**Example 2:** `p = [1,2]`, `q = [1,null,2]`

```
Tree p:        Tree q:
    1              1
   /                 \
  2                   2

isSameTree(1, 1):
  Both exist, values equal (1 == 1)
  
  Check left: isSameTree(2, null):
    One null, one exists → return false
  
  return true && false = false ✓
```

**Example 3:** `p = [1,2,1]`, `q = [1,1,2]`

```
Tree p:        Tree q:
    1              1
   / \            / \
  2   1          1   2

isSameTree(1, 1):
  Both exist, values equal (1 == 1)
  
  Check left: isSameTree(2, 1):
    Both exist, but values differ (2 != 1) → return false
  
  return true && false = false ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Visit each node exactly once
  - n = minimum number of nodes in both trees
  - Early termination when mismatch found

- **Space Complexity:** O(h)
  - Recursion call stack depth = height of tree
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

## Alternative Approaches

### Solution 2: More Explicit Base Cases

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        if (p->val != q->val) return false;
        
        return isSameTree(p->left, q->left) && 
               isSameTree(p->right, q->right);
    }
};
```

**Key Difference**: Separates null checks and value check for clarity

**Complexity**: Same as Solution 1

### Solution 3: Iterative DFS with Stack

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        stack<pair<TreeNode*, TreeNode*>> st;
        st.push({p, q});
        
        while (!st.empty()) {
            auto [node1, node2] = st.top();
            st.pop();
            
            if (!node1 && !node2) continue;
            if (!node1 || !node2) return false;
            if (node1->val != node2->val) return false;
            
            st.push({node1->right, node2->right});
            st.push({node1->left, node2->left});
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<pair<TreeNode*, TreeNode*>> q_nodes;
        q_nodes.push({p, q});
        
        while (!q_nodes.empty()) {
            auto [node1, node2] = q_nodes.front();
            q_nodes.pop();
            
            if (!node1 && !node2) continue;
            if (!node1 || !node2) return false;
            if (node1->val != node2->val) return false;
            
            q_nodes.push({node1->left, node2->left});
            q_nodes.push({node1->right, node2->right});
        }
        
        return true;
    }
};
```

**Complexity**: 
- Time: O(n)
- Space: O(w) where w is maximum width

## Key Insights

1. **Three Base Cases**: Both null, one null, or value mismatch
2. **Symmetric Comparison**: Compare corresponding nodes in both trees
3. **AND Logic**: Both subtrees must match for trees to be identical
4. **Early Termination**: Return false immediately when mismatch found
5. **Pre-order Traversal**: Check current node before recursing

## Edge Cases

1. **Both empty**: `p = []`, `q = []` → return `true`
2. **One empty**: `p = []`, `q = [1]` → return `false`
3. **Single node match**: `p = [1]`, `q = [1]` → return `true`
4. **Single node mismatch**: `p = [1]`, `q = [2]` → return `false`
5. **Same structure, different values**: `p = [1,2]`, `q = [1,3]` → return `false`
6. **Different structure**: `p = [1,2]`, `q = [1,null,2]` → return `false`

## Common Mistakes

1. **Not checking both nulls first**: Accessing values before null check
   ```cpp
   // WRONG:
   if (p->val != q->val) return false; // ❌ Crashes if p or q is null
   ```

2. **Wrong logic operator**: Using OR instead of AND
   ```cpp
   // WRONG:
   return isSameTree(p->left, q->left) || isSameTree(p->right, q->right);
   // ❌ Returns true if only one subtree matches
   ```

3. **Not handling null correctly**: Forgetting that one tree can be null while the other isn't
4. **Comparing references**: Comparing node pointers instead of values
5. **Missing value check**: Only checking structure, not values

## Comparison with Related Problems

| Problem | Key Difference |
|---------|----------------|
| **LC 100: Same Tree** | Check if two trees are **completely identical** |
| **LC 101: Symmetric Tree** | Check if tree is **symmetric** (mirror of itself) |
| **LC 572: Subtree of Another Tree** | Check if one tree is **subtree** of another |
| **LC 226: Invert Binary Tree** | **Mirror** a tree (swap left/right) |

## Related Problems

- [LC 100: Same Tree](https://leetcode.com/problems/same-tree/) - This problem
- [LC 101: Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) - Check if tree is symmetric
- [LC 226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) - Mirror a binary tree
- [LC 572: Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) - Check if subtree exists
- [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Find maximum depth
- [LC 110: Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) - Check if tree is balanced

---

*This problem demonstrates **recursive tree comparison**. The key insight is handling three cases: both null (match), one null (mismatch), or both exist (check value and recurse). It's a fundamental tree operation used in many tree problems.*

