---
layout: post
title: "[Medium] 1650. Lowest Common Ancestor of a Binary Tree III"
date: 2025-10-20 13:55:00 -0700
categories: leetcode algorithm medium tree binary-tree lca
permalink: /2025/10/20/medium-1650-lowest-common-ancestor-of-a-binary-tree-iii/
---
**Difficulty:** Medium  
**Category:** Tree, Binary Tree, LCA


Given two nodes of a binary tree `p` and `q`, return their **lowest common ancestor (LCA)**.

Each node has a reference to its parent node. The definition of LCA is: "The lowest common ancestor of two nodes `p` and `q` in a tree is the lowest node that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

## Examples

### Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

### Example 2:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

### Example 3:
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

## Thinking Process

This is a variation of the **Lowest Common Ancestor (LCA)** problem where each node has a reference to its parent. The key insight is to use the **two-pointer technique** similar to finding the intersection of two linked lists.

### Algorithm:
1. **Start from both nodes** `p` and `q`
2. **Traverse upward** using parent pointers
3. **When one pointer reaches null**, redirect it to the other node
4. **Continue until both pointers meet** at the LCA
5. **Return the meeting point**

### Key Insight:
This approach ensures both pointers travel the same total distance, making them meet at the LCA.



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
| Recursive DFS | $O(n)$ | $O(h)$ | Depth, path sum, subtree queries |
| BFS level-order | $O(n)$ | $O(w)$ | Level traversal, zigzag |
| Inorder on BST | $O(n)$ | $O(h)$ | Sorted order, successor |
| **Divide & conquer on tree** *(this problem)* | $O(n)$ | $O(h)$ | Diameter, max path |

## Solution

```cpp
class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        Node* a = p, *b = q;
        while(a != b) {
            a = a == nullptr ? q : a->parent;
            b = b == nullptr ? p : b->parent;
        }
        return a;
    }
};
```

### Solution Explanation

This is a variation of the **Lowest Common Ancestor (LCA)** problem where each node has a reference to its parent. The key insight is to use the **two-pointer technique** similar to finding the intersection of two linked lists.

See **Complexity** below for time and space analysis.
## Explanation

### Step-by-Step Process:

1. **Initialize pointers:** `a = p`, `b = q`
2. **Traverse upward:** While `a != b`:
   - If `a` is null, redirect to `q`; otherwise move to parent
   - If `b` is null, redirect to `p`; otherwise move to parent
3. **Return meeting point:** When `a == b`, return the LCA

### Why This Works:

**Distance Equalization:**
- **Path from p to root:** Let's say it has length `m`
- **Path from q to root:** Let's say it has length `n`
- **Total distance traveled by each pointer:** `m + n`
- **Meeting point:** Both pointers meet at the LCA

**Example Walkthrough:**
For a tree where `p` is at depth 2 and `q` is at depth 3:

- **Pointer a (from p):** p → parent → root → q → parent → LCA
- **Pointer b (from q):** q → parent → parent → root → p → parent → LCA
- **Both travel same distance:** 5 steps each
- **Meet at LCA:** After equal distance traveled

### Visual Example:
```
        Root
       /    \
      A      B
     / \    / \
    C   D  E   F
   /
  G
```

If `p = G` and `q = F`:
- **Path from G to root:** G → C → A → Root (3 steps)
- **Path from F to root:** F → B → Root (2 steps)
- **Pointer a:** G → C → A → Root → F → B → Root (6 steps)
- **Pointer b:** F → B → Root → G → C → A → Root (6 steps)
- **Meet at Root:** LCA = Root

### Complexity
**Time Complexity:** O(h) where h is the height of the tree
- In worst case, both nodes are at maximum depth
- Each pointer travels at most 2h steps (h up + h down)

**Space Complexity:** O(1)
- Only using two pointers, no additional data structures

## Key Concepts

1. **Lowest Common Ancestor:** Deepest node that has both nodes as descendants
2. **Parent Pointer:** Each node knows its parent (unlike standard binary tree)
3. **Two-Pointer Technique:** Classic algorithm pattern for finding intersections
4. **Distance Equalization:** Mathematical insight that makes the algorithm work
5. **Tree Traversal:** Upward traversal using parent pointers

This problem demonstrates the power of the two-pointer technique and shows how mathematical insights can lead to elegant solutions in tree problems.

## References

- [LC 1650: Lowest Common Ancestor of a Binary Tree III on LeetCode](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/)
- [LeetCode Discuss — LC 1650: Lowest Common Ancestor of a Binary Tree III](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Two-Pointer Technique:** Similar to finding linked list intersection
2. **Distance Equalization:** Both pointers travel same total distance
3. **Parent Pointer Utilization:** Leverages the parent reference efficiently
4. **No Extra Space:** Constant space solution
5. **Elegant Logic:** Simple but powerful algorithm
