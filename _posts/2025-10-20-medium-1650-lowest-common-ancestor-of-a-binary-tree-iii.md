---
layout: post
title: "1650. Lowest Common Ancestor of a Binary Tree III"
date: 2025-10-20 13:55:00 -0700
categories: leetcode algorithm medium tree binary-tree lca
permalink: /2025/10/20/medium-1650-lowest-common-ancestor-of-a-binary-tree-iii/
---

# 1650. Lowest Common Ancestor of a Binary Tree III

**Difficulty:** Medium  
**Category:** Tree, Binary Tree, LCA

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **LCA definition**: What is Lowest Common Ancestor? (Assumption: Deepest node that is ancestor of both p and q - common ancestor closest to the nodes)

2. **Node structure**: What information do nodes have? (Assumption: Node has val, parent pointer - can traverse upward, not just downward)

3. **Self-ancestor**: Can a node be its own ancestor? (Assumption: Yes - per examples, node can be LCA of itself and another node)

4. **Return value**: What should we return? (Assumption: Node pointer to the LCA of p and q)

5. **Tree type**: Is this a binary tree? (Assumption: Yes - binary tree, but with parent pointers instead of just child pointers)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to find LCA. Let me find paths from root to both nodes, then find common ancestor."

**Naive Solution**: Find path from root to p, path from root to q, find last common node in both paths.

**Complexity**: O(n) time, O(n) space

**Issues**:
- Requires finding root first
- Needs to store paths
- Doesn't leverage parent pointers
- Can be optimized

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use parent pointers to traverse upward from both nodes."

**Improved Solution**: Traverse upward from p to root, store visited nodes. Then traverse upward from q, first common node is LCA.

**Complexity**: O(n) time, O(n) space

**Improvements**:
- Leverages parent pointers
- O(n) time is good
- Still uses O(n) space for visited set
- Can optimize space

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "I can use two-pointer technique - make both pointers travel same distance."

**Best Solution**: Use two-pointer technique. Find depths of p and q. Move deeper pointer up to same depth. Then move both pointers up until they meet at LCA.

**Complexity**: O(n) time, O(1) space

**Key Realizations**:
1. Parent pointers enable upward traversal
2. Two-pointer technique eliminates need for visited set
3. O(n) time is optimal
4. O(1) space is optimal

## Approach

This is a variation of the **Lowest Common Ancestor (LCA)** problem where each node has a reference to its parent. The key insight is to use the **two-pointer technique** similar to finding the intersection of two linked lists.

### Algorithm:
1. **Start from both nodes** `p` and `q`
2. **Traverse upward** using parent pointers
3. **When one pointer reaches null**, redirect it to the other node
4. **Continue until both pointers meet** at the LCA
5. **Return the meeting point**

### Key Insight:
This approach ensures both pointers travel the same total distance, making them meet at the LCA.

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

## Complexity Analysis

**Time Complexity:** O(h) where h is the height of the tree
- In worst case, both nodes are at maximum depth
- Each pointer travels at most 2h steps (h up + h down)

**Space Complexity:** O(1)
- Only using two pointers, no additional data structures

## Key Insights

1. **Two-Pointer Technique:** Similar to finding linked list intersection
2. **Distance Equalization:** Both pointers travel same total distance
3. **Parent Pointer Utilization:** Leverages the parent reference efficiently
4. **No Extra Space:** Constant space solution
5. **Elegant Logic:** Simple but powerful algorithm

## Alternative Approaches

### Approach 1: Path Collection
```cpp
Node* lowestCommonAncestor(Node* p, Node* q) {
    unordered_set<Node*> path;
    
    // Collect path from p to root
    Node* curr = p;
    while(curr) {
        path.insert(curr);
        curr = curr->parent;
    }
    
    // Find first common node in path from q to root
    curr = q;
    while(curr) {
        if(path.count(curr)) return curr;
        curr = curr->parent;
    }
    
    return nullptr;
}
```

### Approach 2: Depth Calculation
```cpp
int getDepth(Node* node) {
    int depth = 0;
    while(node) {
        depth++;
        node = node->parent;
    }
    return depth;
}

Node* lowestCommonAncestor(Node* p, Node* q) {
    int depthP = getDepth(p);
    int depthQ = getDepth(q);
    
    // Move deeper node up to same level
    while(depthP > depthQ) {
        p = p->parent;
        depthP--;
    }
    while(depthQ > depthP) {
        q = q->parent;
        depthQ--;
    }
    
    // Move both up until they meet
    while(p != q) {
        p = p->parent;
        q = q->parent;
    }
    
    return p;
}
```

## Comparison of Approaches

| Approach | Time | Space | Elegance |
|----------|------|-------|----------|
| **Two-Pointer** | O(h) | O(1) | ⭐⭐⭐⭐⭐ |
| **Path Collection** | O(h) | O(h) | ⭐⭐⭐ |
| **Depth Calculation** | O(h) | O(1) | ⭐⭐⭐⭐ |

**The two-pointer approach is optimal** because:
- **Constant Space:** No additional data structures
- **Elegant Logic:** Simple and intuitive
- **Efficient:** Single pass through the tree
- **Clean Code:** Minimal implementation

## Key Concepts

1. **Lowest Common Ancestor:** Deepest node that has both nodes as descendants
2. **Parent Pointer:** Each node knows its parent (unlike standard binary tree)
3. **Two-Pointer Technique:** Classic algorithm pattern for finding intersections
4. **Distance Equalization:** Mathematical insight that makes the algorithm work
5. **Tree Traversal:** Upward traversal using parent pointers

This problem demonstrates the power of the two-pointer technique and shows how mathematical insights can lead to elegant solutions in tree problems.
