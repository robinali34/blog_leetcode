---
layout: post
title: "236. Lowest Common Ancestor of a Binary Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, medium, tree, dfs]
permalink: /2026/01/19/medium-236-lowest-common-ancestor-of-a-binary-tree/
tags: [leetcode, medium, tree, dfs, recursion, lca]
---

# 236. Lowest Common Ancestor of a Binary Tree

## Problem Statement

Given a binary tree, find the **lowest common ancestor (LCA)** of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**)."

## Examples

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Tree structure:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

**Example 2:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 1 is 5 (a node can be a descendant of itself).

Tree structure:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

**Example 3:**
```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Tree type**: Is this a binary tree, BST, or general tree? (Assumption: Binary tree - not necessarily a BST, nodes can have any values)

2. **Node existence**: Are we guaranteed that both p and q exist in the tree? (Assumption: Yes - constraints guarantee both nodes exist)

3. **LCA definition**: Can a node be its own ancestor? (Assumption: Yes - if p is ancestor of q, then p is the LCA)

4. **Duplicate values**: Can nodes have duplicate values? (Assumption: No - all node values are unique per constraints)

5. **Return value**: Should we return the node itself or its value? (Assumption: Return the node (TreeNode*) - typical LCA problem requirement)

## Solution Approach

This problem requires finding the lowest common ancestor of two nodes in a binary tree. The LCA is the deepest node that has both `p` and `q` as descendants.

### Key Insights:

1. **Post-order Traversal**: Process children before parent to find LCA bottom-up
2. **Return Strategy**: 
   - Return the node if it matches `p` or `q`
   - If both subtrees return non-null, current node is LCA
   - Otherwise, return whichever subtree found a match
3. **Self as Descendant**: A node can be its own descendant (if `p` or `q` is ancestor)

## Solution: Recursive DFS (Post-order)

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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return isCommonAncestor(root, p, q);
    }
private:
    TreeNode* isCommonAncestor(TreeNode* node, TreeNode* p, TreeNode* q){
        if(!node) return nullptr;
        TreeNode* left = isCommonAncestor(node->left, p, q);
        TreeNode* right = isCommonAncestor(node->right, p, q);
        if(node == p || node == q) return node;
        if(left && right) return node;
        return left ? left : right;
    }
};
```

### Algorithm Explanation:

1. **Base Case**: 
   - If `node` is `nullptr`, return `nullptr` (not found)

2. **Recursive Calls**:
   - Recursively search left subtree: `isCommonAncestor(node->left, p, q)`
   - Recursively search right subtree: `isCommonAncestor(node->right, p, q)`

3. **Current Node Check**:
   - If current node equals `p` or `q`, return `node` (found one target)

4. **LCA Detection**:
   - If **both** `left` and `right` are non-null → current node is LCA
   - This means `p` and `q` are in different subtrees

5. **Propagate Result**:
   - If only one subtree found a match, return that result
   - `return left ? left : right;` propagates the found node upward

### Why This Works?

The algorithm uses **post-order traversal**:
- First, recursively search both subtrees
- Then, check if current node is one of the targets
- If both subtrees found targets, current node is the LCA
- Otherwise, propagate whichever subtree found a target

**Key Insight**: The LCA is the first node where both `p` and `q` appear in different subtrees (or one is the node itself).

### Example Walkthrough:

**Example 1:** `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 1`

```
Tree structure:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

isCommonAncestor(3, 5, 1):
  node = 3, not null
  
  left = isCommonAncestor(5, 5, 1):
    node = 5, matches p → return 5
  
  right = isCommonAncestor(1, 5, 1):
    node = 1, matches q → return 1
  
  node != p && node != q
  left = 5 (non-null), right = 1 (non-null)
  Both non-null → return 3 (LCA) ✓
```

**Example 2:** `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 4`

```
Tree structure:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

isCommonAncestor(3, 5, 4):
  node = 3, not null
  
  left = isCommonAncestor(5, 5, 4):
    node = 5, matches p → return 5
    
    left = isCommonAncestor(6, 5, 4):
      node = 6, not p or q
      left = null, right = null
      return null
    
    right = isCommonAncestor(2, 5, 4):
      node = 2, not p or q
      
      left = isCommonAncestor(7, 5, 4):
        return null
      
      right = isCommonAncestor(4, 5, 4):
        node = 4, matches q → return 4
      
      left = null, right = 4
      return 4
    
    left = null, right = 4
    node = 5 (matches p)
    return 5
  
  right = isCommonAncestor(1, 5, 4):
    return null (not found in right subtree)
  
  left = 5 (non-null), right = null
  return 5 (LCA) ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Visit each node at most once
  - n = number of nodes in tree
  - Early termination possible but worst case visits all nodes

- **Space Complexity:** O(h)
  - Recursion call stack depth = height of tree
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

## Alternative Approaches

### Solution 2: Path Tracking (Find Paths First)

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> pathP, pathQ;
        findPath(root, p, pathP);
        findPath(root, q, pathQ);
        
        TreeNode* lca = nullptr;
        int i = 0;
        while (i < pathP.size() && i < pathQ.size() && 
               pathP[i] == pathQ[i]) {
            lca = pathP[i];
            i++;
        }
        return lca;
    }
    
private:
    bool findPath(TreeNode* root, TreeNode* target, vector<TreeNode*>& path) {
        if (!root) return false;
        
        path.push_back(root);
        if (root == target) return true;
        
        if (findPath(root->left, target, path) || 
            findPath(root->right, target, path)) {
            return true;
        }
        
        path.pop_back();
        return false;
    }
};
```

**Complexity**: 
- Time: O(n) - two traversals
- Space: O(h) - path storage + recursion

### Solution 3: Iterative with Parent Map

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        unordered_map<TreeNode*, TreeNode*> parent;
        stack<TreeNode*> st;
        parent[root] = nullptr;
        st.push(root);
        
        // Build parent map
        while (!parent.count(p) || !parent.count(q)) {
            TreeNode* node = st.top();
            st.pop();
            
            if (node->left) {
                parent[node->left] = node;
                st.push(node->left);
            }
            if (node->right) {
                parent[node->right] = node;
                st.push(node->right);
            }
        }
        
        // Find path from p to root
        set<TreeNode*> ancestors;
        TreeNode* curr = p;
        while (curr) {
            ancestors.insert(curr);
            curr = parent[curr];
        }
        
        // Find first common ancestor from q
        curr = q;
        while (curr) {
            if (ancestors.count(curr)) {
                return curr;
            }
            curr = parent[curr];
        }
        
        return nullptr;
    }
};
```

**Complexity**: 
- Time: O(n)
- Space: O(n) for parent map and set

## Key Insights

1. **Post-order Traversal**: Process children before parent to find LCA bottom-up
2. **Return Strategy**: 
   - Return node if it matches target
   - Return current node if both subtrees found targets
   - Otherwise, propagate the found result upward
3. **Self as Descendant**: If `p` is ancestor of `q`, return `p` (and vice versa)
4. **Single Pass**: Can find LCA in one traversal without storing paths

## Edge Cases

1. **One node is ancestor of other**: `p = 5`, `q = 4` → return `5`
2. **Root is LCA**: `p` and `q` in different subtrees → return root
3. **Both nodes in same subtree**: LCA is deeper in that subtree
4. **Root equals one target**: Return root
5. **Skewed tree**: Works correctly but O(n) space

## Common Mistakes

1. **Wrong traversal order**: Using pre-order instead of post-order
   ```cpp
   // WRONG:
   if (node == p || node == q) return node; // Check before recursion
   // ❌ May return too early
   ```

2. **Not handling self as descendant**: Forgetting that a node can be its own descendant
3. **Wrong return logic**: Returning null when one subtree found a match
   ```cpp
   // WRONG:
   if (left && right) return node;
   return nullptr; // ❌ Should return left or right
   ```

4. **Comparing values instead of nodes**: Using `node->val` instead of `node == p`
5. **Not propagating results**: Not returning the found node from subtrees

## Comparison with Related Problems

| Problem | Key Difference |
|---------|----------------|
| **LC 236: LCA of Binary Tree** | General binary tree, nodes may not exist |
| **LC 235: LCA of BST** | Binary Search Tree, can use BST properties |
| **LC 1650: LCA of Binary Tree III** | Nodes have parent pointers |
| **LC 1644: LCA of Binary Tree II** | Nodes may not exist in tree |

## Related Problems

- [LC 236: Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) - This problem
- [LC 235: Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) - BST version (easier)
- [LC 1644: Lowest Common Ancestor of a Binary Tree II](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/) - Nodes may not exist
- [LC 1650: Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) - Nodes have parent pointers
- [LC 1123: Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) - LCA of deepest leaves
- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Level-order traversal

---

*This problem demonstrates **post-order traversal** for finding the lowest common ancestor. The key insight is that the LCA is the first node where both targets appear in different subtrees (or one is the node itself). The elegant solution uses a single pass without storing paths, making it both time and space efficient.*

