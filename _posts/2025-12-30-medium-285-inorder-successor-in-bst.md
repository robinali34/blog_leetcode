---
layout: post
title: "[Medium] 285. Inorder Successor in BST"
date: 2025-12-30 20:30:00 -0700
categories: [leetcode, medium, binary-search-tree, tree, inorder-traversal]
permalink: /2025/12/30/medium-285-inorder-successor-in-bst/
---
Given the root of a binary search tree (BST) and a node `p` in it, return *the in-order successor of that node in the BST*. If the given node has no in-order successor in the tree, return `null`.

The successor of a node `p` is the node with the smallest key greater than `p.val`.

## Thinking Process

Given the root of a binary search tree (BST) and a node `p` in it, return *the in-order successor of that node in the BST*. If the given node has no in-order successor in the tree, return `null`.

The successor of a node `p` is the node with the smallest key greater than `p.val`.

- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 165" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Tree DFS (bottom-up)</text>

  <line x1="140" y1="42" x2="80" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="140" y1="42" x2="200" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="80" y1="88" x2="50" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="200" y1="88" x2="230" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <circle cx="140" cy="42" r="18" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="140" y="46" text-anchor="middle" font-size="12" fill="#3D3535">3</text>
  <circle cx="80" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="80" y="92" text-anchor="middle" font-size="11" fill="#3D3535">9</text>
  <circle cx="200" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="200" y="92" text-anchor="middle" font-size="11" fill="#3D3535">20</text>
  <circle cx="50" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="50" y="132" text-anchor="middle" font-size="10" fill="#3D3535">15</text>
  <circle cx="230" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="230" y="132" text-anchor="middle" font-size="10" fill="#3D3535">7</text>
  <text x="140" y="155" text-anchor="middle" font-size="11" fill="#6B6560">post-order: combine left + right + 1</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Recursive DFS | O(n) | O(h) | Depth, path sum, subtree queries |
| BFS level-order | O(n) | O(w) | Level traversal, zigzag |
| **Inorder on BST** *(this problem)* | O(n) | O(h) | Sorted order, successor |
| Divide & conquer on tree | O(n) | O(h) | Diameter, max path |

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

### Complexity
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [285. Inorder Successor in BST](https://www.leetcode.com/problems/inorder-successor-in-bst/) - Current problem
- [510. Inorder Successor in BST II](https://www.leetcode.com/problems/inorder-successor-in-bst-ii/) - With parent pointer
- [173. Binary Search Tree Iterator](https://www.leetcode.com/problems/binary-search-tree-iterator/) - Iterator with next()
- [98. Validate Binary Search Tree](https://www.leetcode.com/problems/validate-binary-search-tree/) - BST validation

## Tags

`Binary Search Tree`, `Tree`, `Inorder Traversal`, `Medium`

## Key Takeaways

- Trees have no cycles — recursion is natural.
- Combine results from left and right subtrees at each node.
- Base case is usually `null`; height drives stack space.

## References

- [LC 285: Inorder Successor in BST on LeetCode](https://www.leetcode.com/problems/inorder-successor-in-bst/)
- [LeetCode Discuss — LC 285: Inorder Successor in BST](https://www.leetcode.com/problems/inorder-successor-in-bst/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/inorder-successor-in-bst/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
