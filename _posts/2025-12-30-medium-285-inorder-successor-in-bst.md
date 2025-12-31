---
layout: post
title: "285. Inorder Successor in BST"
date: 2025-12-30 20:30:00 -0700
categories: [leetcode, medium, binary-search-tree, tree, inorder-traversal]
permalink: /2025/12/30/medium-285-inorder-successor-in-bst/
---

# 285. Inorder Successor in BST

## Problem Statement

Given the root of a binary search tree (BST) and a node `p` in it, return *the in-order successor of that node in the BST*. If the given node has no in-order successor in the tree, return `null`.

The successor of a node `p` is the node with the smallest key greater than `p.val`.

## Examples

**Example 1:**
```
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor is 2. Note that both p and the return value is of TreeNode type.
```

**Example 2:**
```
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the node 6, so the answer is null.
```

## Constraints

- The number of nodes in the tree will be in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- All Nodes will have unique values.

## Solution Approach

This problem requires finding the in-order successor of a given node in a BST. The in-order successor is the node with the smallest value greater than the given node's value.

### Key Insights:

1. **Two Cases**: 
   - **Case 1**: Node `p` has a right child → successor is the leftmost node in right subtree
   - **Case 2**: Node `p` has no right child → successor is an ancestor (lowest ancestor with left child being ancestor of p)

2. **BST Property**: Use BST property to traverse efficiently
3. **Iterative Search**: Search from root to find the successor when p has no right child

### Algorithm:

1. **Check right child**: If `p->right` exists, find leftmost node in right subtree
2. **Search from root**: If no right child, traverse from root to find successor
3. **Track candidate**: Keep track of node with value greater than `p->val`

## Solution

### **Solution: Two-Case Handling**

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
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        TreeNode* successor = nullptr;
        if(p->right != nullptr) {
            successor = p->right;
            while(successor->left != nullptr) {
                successor = successor->left;
            }
            return successor;
        }
        TreeNode* node = root;
        while(node != nullptr) {
            if(node->val > p->val) {
                successor = node;
                node = node->left;
            } else {
                node = node->right;
            }
        }
        return successor;
    }
};
```

### **Algorithm Explanation:**

1. **Case 1: Node has Right Child (Lines 12-19)**:
   - If `p->right` exists, the successor is in the right subtree
   - Go to right child: `successor = p->right`
   - Find leftmost node: Traverse left until `nullptr`
   - Return the leftmost node (smallest value in right subtree)

2. **Case 2: Node has No Right Child (Lines 20-29)**:
   - If `p->right` is `nullptr`, successor is an ancestor
   - Traverse from root to find successor
   - **When `node->val > p->val`**:
     - Current node is a candidate (greater than p)
     - Update `successor = node`
     - Go left to find smaller candidate (if exists)
   - **When `node->val <= p->val`**:
     - Current node is not greater than p
     - Go right to find larger node
   - Return `successor` (lowest ancestor with value > p->val)

### **Example Walkthrough:**

**Example 1: `root = [2,1,3], p = 1`**

```
BST:
    2
   / \
  1   3

Case 2: p (1) has no right child
Traverse from root:

Step 1: node = 2, p->val = 1
  node->val (2) > p->val (1) → candidate found!
  successor = 2
  Go left: node = 1

Step 2: node = 1, p->val = 1
  node->val (1) <= p->val (1) → not a candidate
  Go right: node = nullptr

Result: successor = 2
```

**Example 2: `root = [5,3,6,2,4,null,null,1], p = 3`**

```
BST:
        5
       / \
      3   6
     / \
    2   4
   /
  1

Case 1: p (3) has right child (4)
  successor = p->right = 4
  Check left: 4->left = nullptr
  Return: 4
```

**Example 3: `root = [5,3,6,2,4,null,null,1], p = 6`**

```
BST:
        5
       / \
      3   6
     / \
    2   4
   /
  1

Case 2: p (6) has no right child
Traverse from root:

Step 1: node = 5, p->val = 6
  node->val (5) <= p->val (6) → not a candidate
  Go right: node = 6

Step 2: node = 6, p->val = 6
  node->val (6) <= p->val (6) → not a candidate
  Go right: node = nullptr

Result: successor = nullptr (no successor)
```

## Algorithm Breakdown

### **Key Insight: Two Distinct Cases**

The in-order successor can be found in two different locations:

**Case 1: Right Subtree Exists**
- If `p` has a right child, the successor is **always** in the right subtree
- Specifically, it's the **leftmost node** in the right subtree
- This is the smallest value greater than `p->val`

**Case 2: No Right Subtree**
- If `p` has no right child, the successor is an **ancestor**
- It's the **lowest ancestor** whose left subtree contains `p`
- We find it by traversing from root and tracking candidates

### **BST Property Utilization**

When searching from root (Case 2):
```cpp
if(node->val > p->val) {
    successor = node;      // Candidate found
    node = node->left;     // Try to find smaller candidate
} else {
    node = node->right;    // Need larger value
}
```

- **Go left**: When current node is greater, try to find smaller candidate
- **Go right**: When current node is not greater, need to find larger value
- **Track candidate**: Keep the smallest node with value > p->val

### **Why This Works**

1. **Case 1 (Right child exists)**:
   - In-order traversal: left → root → right
   - After visiting `p`, we visit its right subtree
   - The first node in right subtree (leftmost) is the successor

2. **Case 2 (No right child)**:
   - After visiting `p`, we backtrack to ancestors
   - The successor is the first ancestor we haven't visited yet
   - This is the lowest ancestor whose left subtree contains `p`

## Complexity Analysis

### **Time Complexity:** O(h)
- **Case 1**: O(h) - Find leftmost node in right subtree (at most h steps)
- **Case 2**: O(h) - Traverse from root to find successor (at most h steps)
- **Total**: O(h) where h = height of tree
  - **Balanced BST**: O(log n)
  - **Unbalanced BST**: O(n)

### **Space Complexity:** O(1)
- **Variables**: Only `successor` and `node` pointers
- **No recursion**: Iterative approach
- **No extra data structures**: Constant space
- **Total**: O(1)

## Key Points

1. **Two Cases**: Handle right child and no right child separately
2. **BST Property**: Use BST property to traverse efficiently
3. **Leftmost Node**: In right subtree, find leftmost node
4. **Ancestor Search**: When no right child, search from root
5. **Space Efficient**: O(1) space, no recursion stack

## Alternative Approaches

### **Approach 1: Two-Case Handling (Current Solution)**
- **Time**: O(h)
- **Space**: O(1)
- **Best for**: Space-efficient solution

### **Approach 2: In-Order Traversal**
- **Time**: O(n)
- **Space**: O(h) for recursion
- **Traverse**: Do in-order traversal, find p, return next
- **Use case**: When you need to understand in-order sequence

### **Approach 3: Recursive Search**
- **Time**: O(h)
- **Space**: O(h) for recursion stack
- **Recursive**: Recursively search for successor
- **Similar logic**: But uses recursion instead of iteration

## Detailed Example Walkthrough

### **Example: `root = [5,3,6,2,4,null,null,1], p = 2`**

```
BST:
        5
       / \
      3   6
     / \
    2   4
   /
  1

Case 2: p (2) has no right child
Traverse from root to find successor:

Step 1: node = 5, p->val = 2
  node->val (5) > p->val (2) → candidate!
  successor = 5
  Go left: node = 3

Step 2: node = 3, p->val = 2
  node->val (3) > p->val (2) → candidate!
  successor = 3 (better candidate, smaller than 5)
  Go left: node = 2

Step 3: node = 2, p->val = 2
  node->val (2) <= p->val (2) → not a candidate
  Go right: node = nullptr

Result: successor = 3
```

### **Visual Explanation:**

```
In-order traversal: 1 → 2 → 3 → 4 → 5 → 6

For p = 2:
- In-order: ... → 2 → 3 → ...
- Successor: 3

For p = 3:
- In-order: ... → 3 → 4 → ...
- Successor: 4 (leftmost in right subtree)

For p = 6:
- In-order: ... → 6 → (end)
- Successor: null (no node after 6)
```

## Edge Cases

1. **Largest node**: No successor (return `null`)
2. **Node with right child**: Successor in right subtree
3. **Node without right child**: Successor is ancestor
4. **Single node tree**: If p is the only node, return `null`
5. **Root node**: Successor depends on whether it has right child

## Related Problems

- [285. Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) - Current problem
- [510. Inorder Successor in BST II](https://leetcode.com/problems/inorder-successor-in-bst-ii/) - With parent pointer
- [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) - Iterator with next()
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) - BST validation

## Tags

`Binary Search Tree`, `Tree`, `Inorder Traversal`, `Medium`

