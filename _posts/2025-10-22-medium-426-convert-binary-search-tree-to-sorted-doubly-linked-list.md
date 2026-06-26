---
layout: post
title: "[Medium] 426. Convert Binary Search Tree to Sorted Doubly Linked List"
date: 2025-10-22 12:00:00 -0700
categories: leetcode medium tree linked-list
permalink: /posts/2025-10-22-medium-426-convert-binary-search-tree-to-sorted-doubly-linked-list/
tags: [leetcode, medium, tree, linked-list, bst, inorder-traversal, recursion]
---
**Difficulty:** Medium  
**Category:** Tree, Linked List, DFS  
**Companies:** Amazon, Microsoft, Facebook


Convert a Binary Search Tree to a sorted Circular Doubly Linked List in-place.

Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in-place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

## Examples
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

## Constraints
- `-1000 <= Node.val <= 1000`
- `Node.left.val < Node.val < Node.right.val` (BST property)
- `1 <= Number of Nodes <= 1000`

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

### Solution Explanation

**Approach:** Divide & conquer on tree (this problem)

**Key idea:** Difficulty:** Medium

**How the code works:**
**Difficulty:** Medium
**Category:** Tree, Linked List, DFS
- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

**Walkthrough** — input `root = [4,2,5,1,3]`, expected output `[1,2,3,4,5]`:

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [LC 114: Flatten Binary Tree to Linked List](https://www.leetcode.com/problems/flatten-binary-tree-to-linked-list/)
- [LC 897: Increasing Order Search Tree](https://www.leetcode.com/problems/increasing-order-search-tree/)
- [LC 98: Validate Binary Search Tree](https://www.leetcode.com/problems/validate-binary-search-tree/)

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

## Key Takeaways

- **Pattern:** Divide & conquer on tree (this problem)
- Difficulty:** Medium
- Category:** Tree, Linked List, DFS

## References

- [LC 426: Convert Binary Search Tree to Sorted Doubly Linked List on LeetCode](https://www.leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)
- [LeetCode Discuss — LC 426: Convert Binary Search Tree to Sorted Doubly Linked List](https://www.leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)

## Thinking Process

**Difficulty:** Medium

**Category:** Tree, Linked List, DFS

- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Linked list: pointer walk</text>

  <rect x="30" y="50" width="44" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="52" y="68" text-anchor="middle" font-size="12">1</text>
  <path d="M74 66h16" stroke="#8B8680" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="90" y="50" width="44" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="112" y="68" text-anchor="middle" font-size="12">2</text>
  <path d="M134 66h16" stroke="#8B8680" stroke-width="2"/>
  <rect x="150" y="50" width="44" height="32" rx="4" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="172" y="68" text-anchor="middle" font-size="12">3</text>
  <text x="130" y="105" text-anchor="middle" font-size="11" fill="#6B6560">slow → → fast (2x speed)</text>
  <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Recursive DFS | O(n) | O(h) | Depth, path sum, subtree queries |
| BFS level-order | O(n) | O(w) | Level traversal, zigzag |
| Inorder on BST | O(n) | O(h) | Sorted order, successor |
| **Divide & conquer on tree** *(this problem)* | O(n) | O(h) | Diameter, max path |
