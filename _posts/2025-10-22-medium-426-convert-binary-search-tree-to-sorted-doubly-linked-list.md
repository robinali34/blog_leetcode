---
layout: post
title: "LC 426: Convert Binary Search Tree to Sorted Doubly Linked List"
date: 2025-10-22 12:00:00 -0700
categories: leetcode medium tree linked-list
permalink: /posts/2025-10-22-medium-426-convert-binary-search-tree-to-sorted-doubly-linked-list/
tags: [leetcode, medium, tree, linked-list, bst, inorder-traversal, recursion]
---

# LC 426: Convert Binary Search Tree to Sorted Doubly Linked List

**Difficulty:** Medium  
**Category:** Tree, Linked List, DFS  
**Companies:** Amazon, Microsoft, Facebook

## Problem Statement

Convert a Binary Search Tree to a sorted Circular Doubly Linked List in-place.

Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in-place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

### Examples

**Example 1:**
```
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
```

**Example 2:**
```
Input: root = [2,1,3]
Output: [1,2,3]
```

### Constraints

- `-1000 <= Node.val <= 1000`
- `Node.left.val < Node.val < Node.right.val` (BST property)
- `1 <= Number of Nodes <= 1000`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Doubly linked list**: What is the structure? (Assumption: Each node has left (prev) and right (next) pointers, circular list)

2. **Sorting order**: What order should nodes be in? (Assumption: In-order traversal order - sorted ascending by value)

3. **Return value**: What should we return? (Assumption: Head of the circular doubly linked list - smallest value node)

4. **Tree modification**: Can we modify the tree? (Assumption: Yes - convert in-place by modifying pointers)

5. **Circular list**: Should the list be circular? (Assumption: Yes - last node's right points to first, first node's left points to last)

## Solution Approaches

### Approach 1: Inorder Traversal with Global Variables (Recommended)

**Key Insight:** Use inorder traversal to visit nodes in sorted order, maintaining first and last nodes to build the doubly linked list.

**Algorithm:**
1. Use inorder traversal to process nodes in sorted order
2. Maintain global `first` and `last` pointers
3. For each node, connect it to the previous node
4. After traversal, connect first and last to make it circular

**Time Complexity:** O(n)  
**Space Complexity:** O(h) where h is height of tree

```cpp
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if(!root) return nullptr;
        inorder(root);
        last->right = first;
        first->left = last;
        return first;
    }
private:
    Node* first = nullptr, *last = nullptr;
    void inorder(Node* node) {
        if(node) {
            inorder(node->left);
            if(last) {
                last->right = node;
                node->left = last;
            } else {
                first = node;
            }
            last = node;
            inorder(node->right);
        }
    }
};
```

### Approach 2: Inorder Traversal with Return Values

**Algorithm:**
1. Perform inorder traversal
2. Return the head and tail of the doubly linked list
3. Connect the head and tail to make it circular

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

```cpp
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if(!root) return nullptr;
        
        Node* head = nullptr;
        Node* tail = nullptr;
        inorder(root, head, tail);
        
        head->left = tail;
        tail->right = head;
        return head;
    }
    
private:
    void inorder(Node* node, Node*& head, Node*& tail) {
        if(!node) return;
        
        inorder(node->left, head, tail);
        
        if(!head) {
            head = node;
        } else {
            tail->right = node;
            node->left = tail;
        }
        tail = node;
        
        inorder(node->right, head, tail);
    }
};
```

### Approach 3: Iterative Inorder Traversal

**Algorithm:**
1. Use iterative inorder traversal with stack
2. Process nodes in sorted order
3. Build doubly linked list incrementally
4. Connect first and last nodes

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

```cpp
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if(!root) return nullptr;
        
        stack<Node*> stk;
        Node* first = nullptr;
        Node* last = nullptr;
        Node* curr = root;
        
        while(curr || !stk.empty()) {
            while(curr) {
                stk.push(curr);
                curr = curr->left;
            }
            
            curr = stk.top();
            stk.pop();
            
            if(!first) {
                first = curr;
            } else {
                last->right = curr;
                curr->left = last;
            }
            last = curr;
            
            curr = curr->right;
        }
        
        first->left = last;
        last->right = first;
        return first;
    }
};
```

## Algorithm Analysis

### Approach Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Global Variables | O(n) | O(h) | Simple, clean | Uses global state |
| Return Values | O(n) | O(h) | No global variables | More complex |
| Iterative | O(n) | O(h) | No recursion | More code |

### Key Insights

1. **Inorder Traversal**: BST inorder gives sorted order
2. **Doubly Linked List**: Each node needs left and right pointers
3. **Circular Connection**: Connect first and last nodes
4. **In-place Transformation**: Modify existing tree structure

## Implementation Details

### Global Variables Approach
```cpp
Node* first = nullptr, *last = nullptr;

void inorder(Node* node) {
    if(node) {
        inorder(node->left);
        // Process current node
        if(last) {
            last->right = node;
            node->left = last;
        } else {
            first = node;  // First node in sorted order
        }
        last = node;
        inorder(node->right);
    }
}
```

### Circular Connection
```cpp
// After inorder traversal
last->right = first;  // Last points to first
first->left = last;   // First points to last
return first;         // Return smallest element
```

## Edge Cases

1. **Empty Tree**: `nullptr` → return `nullptr`
2. **Single Node**: `[1]` → circular list with one node
3. **Left Skewed**: `[1,null,2,null,3]` → sorted order
4. **Right Skewed**: `[1,2,null,3]` → sorted order

## Follow-up Questions

- What if the tree wasn't a BST?
- How would you handle duplicate values?
- What if you needed a non-circular doubly linked list?
- How would you optimize for very large trees?

## Related Problems

- [LC 114: Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
- [LC 897: Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)
- [LC 98: Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

## Optimization Techniques

1. **Inorder Traversal**: Leverage BST property for sorted order
2. **Global Variables**: Simplify state management
3. **In-place Transformation**: No extra space for new nodes
4. **Circular Connection**: Efficient circular list creation

## Code Quality Notes

1. **Readability**: Global variables approach is most intuitive
2. **Performance**: All approaches have O(n) time complexity
3. **Space Efficiency**: O(h) space for recursion stack
4. **Robustness**: Handles all edge cases correctly

---

*This problem demonstrates the power of inorder traversal on BSTs and shows how tree structures can be transformed into linked list structures while maintaining sorted order.*
