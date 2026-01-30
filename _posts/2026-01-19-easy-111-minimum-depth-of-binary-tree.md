---
layout: post
title: "111. Minimum Depth of Binary Tree"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
permalink: /2026/01/19/easy-111-minimum-depth-of-binary-tree/
tags: [leetcode, easy, tree, dfs, bfs, recursion]
---

# 111. Minimum Depth of Binary Tree

## Problem Statement

Given a binary tree, find its **minimum depth**.

The minimum depth is the number of nodes along the **shortest path** from the root node down to the nearest **leaf node**.

**Note:** A leaf is a node with no children.

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 2
Explanation: The minimum depth is 2, which is the path: 3 → 9.
```

**Example 2:**
```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
Explanation: The minimum depth is 5, which is the path: 2 → 3 → 4 → 5 → 6.
```

## Constraints

- The number of nodes in the tree is in the range `[0, 10^5]`.
- `-1000 <= Node.val <= 1000`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Minimum depth definition**: What defines minimum depth - path to nearest leaf? (Assumption: Yes - minimum depth is the number of nodes along the shortest path from root to nearest leaf)

2. **Leaf node**: What is considered a leaf node? (Assumption: A node with no children - both left and right are null)

3. **Empty tree**: What should we return for an empty tree? (Assumption: Return 0 - no nodes means depth 0)

4. **Skewed tree**: How should we handle a skewed tree (all nodes on one side)? (Assumption: Minimum depth equals the number of nodes in the skewed path)

5. **Tree modification**: Should we modify the tree or just traverse it? (Assumption: Just traverse - no modification needed)

## Solution Approach

This problem requires finding the shortest path from root to any leaf node. The key difference from maximum depth is handling nodes with only one child correctly.

### Key Insights:

1. **Leaf Node**: Node with no children (both left and right are null)
2. **Single Child**: If a node has only one child, we must follow that child (can't use null as depth 0)
3. **Both Children**: Take minimum of left and right subtree depths
4. **Base Case**: Empty tree has depth 0

## Solution: Recursive DFS (Handling Single Child)

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
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        if(!root->left && !root->right) return 1;
        int minDep = INT_MAX;
        if(root->left) {
            minDep = min(minDep, minDepth(root->left));
        }
        if(root->right) {
            minDep = min(minDep, minDepth(root->right));
        }
        return minDep + 1;
    }
};
```

### Algorithm Explanation:

1. **Base Case**: If root is `nullptr`, return 0

2. **Leaf Node Check**: If both children are null, return 1 (leaf node)

3. **Single Child Handling**:
   - Initialize `minDep = INT_MAX`
   - Only consider non-null children
   - If `root->left` exists, recursively find its minimum depth
   - If `root->right` exists, recursively find its minimum depth
   - Update `minDep` with the minimum of existing children

4. **Return**: `minDep + 1` (add current node to depth)

### Why This Approach?

The key insight is that we **cannot** use `min(minDepth(left), minDepth(right))` directly when one child is null, because:
- If left is null, `minDepth(left)` returns 0
- Taking `min(0, right_depth)` would incorrectly return 0
- We must only consider non-null children

### Example Walkthrough:

**Input:** `root = [3,9,20,null,null,15,7]`

```
Tree structure:
      3
     / \
    9   20
       /  \
      15   7

minDepth(3):
  root = 3, has both children
  minDep = INT_MAX
  
  left = minDepth(9):
    root = 9, no children → leaf node
    return 1
  
  minDep = min(INT_MAX, 1) = 1
  
  right = minDepth(20):
    root = 20, has both children
    minDep = INT_MAX
    
    left = minDepth(15):
      root = 15, no children → leaf node
      return 1
    
    minDep = min(INT_MAX, 1) = 1
    
    right = minDepth(7):
      root = 7, no children → leaf node
      return 1
    
    minDep = min(1, 1) = 1
    return 1 + 1 = 2
  
  minDep = min(1, 2) = 1
  return 1 + 1 = 2 ✓
```

**Input:** `root = [2,null,3,null,4,null,5,null,6]` (skewed tree)

```
Tree structure:
  2
   \
    3
     \
      4
       \
        5
         \
          6

minDepth(2):
  root = 2, only right child
  minDep = INT_MAX
  
  left = null → skip
  
  right = minDepth(3):
    root = 3, only right child
    minDep = INT_MAX
    
    right = minDepth(4):
      ... (continues recursively)
      
      Eventually reaches leaf node 6:
        return 1
      
      Backtrack: 5 → 4 → 3 → 2
      Each adds 1
    
    return 5
  
  return 5 + 1 = 6
  
Wait, but the answer should be 5. Let me recalculate:
  Actually, the depth is 5 nodes: 2 → 3 → 4 → 5 → 6
  
  minDepth(6): return 1
  minDepth(5): return 1 + 1 = 2
  minDepth(4): return 2 + 1 = 3
  minDepth(3): return 3 + 1 = 4
  minDepth(2): return 4 + 1 = 5 ✓
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
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        
        // If left subtree is null, only right side matters
        if (!root->left) return 1 + minDepth(root->right);
        
        // If right subtree is null, only left side matters
        if (!root->right) return 1 + minDepth(root->left);
        
        // Both subtrees exist, take the minimum
        return 1 + min(minDepth(root->left), minDepth(root->right));
    }
};
```

**Key Difference**: Explicitly handles single-child cases before computing min

**Complexity**: Same as Solution 1

### Solution 3: Iterative BFS (Level-order Traversal)

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        queue<TreeNode*> q;
        if(root) q.push(root);
        int depth = 0;
        while(!q.empty()) {
            int sz = q.size();
            depth++;
            for(int i = 0; i < sz; i++) {
                TreeNode* curr = q.front();
                q.pop();
                if(!curr->left && !curr->right) return depth;
                if(curr->left) q.push(curr->left);
                if(curr->right) q.push(curr->right);
            }
        }
        return depth;
    }
};
```

**Algorithm**:
1. Use BFS to traverse level by level
2. Track depth by incrementing at the start of each level
3. Process all nodes at current level
4. **Early termination**: First leaf node encountered gives minimum depth
5. Return immediately when leaf is found

**Key Features**:
- **Level-by-level processing**: Process all nodes at current depth before moving to next
- **Early exit**: Return as soon as first leaf is found (optimal for shallow trees)
- **No depth storage**: Depth tracked by level counter, not stored per node

**Example Walkthrough**:

**Input:** `root = [3,9,20,null,null,15,7]`

```
Tree structure:
      3
     / \
    9   20
       /  \
      15   7

Level 0: depth = 0
Level 1: depth = 1, process [3]
  Check: 3 has children → continue
  Add: 9, 20 to queue

Level 2: depth = 2, process [9, 20]
  Check 9: no children → LEAF FOUND!
  Return depth = 2 ✓
```

**Complexity**:
- Time: O(n) - worst case visit all nodes, but can stop early
- Space: O(w) - where w is maximum width (worst case O(n))

**Advantage**: Can stop early when first leaf is found, optimal for trees with shallow leaves

### Solution 4: Iterative DFS with Stack

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        
        stack<pair<TreeNode*, int>> st;
        st.push({root, 1});
        int minDepth = INT_MAX;
        
        while (!st.empty()) {
            auto [node, depth] = st.top();
            st.pop();
            
            if (!node->left && !node->right) {
                minDepth = min(minDepth, depth);
            }
            
            if (node->right) st.push({node->right, depth + 1});
            if (node->left) st.push({node->left, depth + 1});
        }
        
        return minDepth;
    }
};
```

**Complexity**: Same as recursive DFS

## Key Differences from Maximum Depth

| Aspect | Maximum Depth | Minimum Depth |
|--------|---------------|---------------|
| **Formula** | `1 + max(left, right)` | `1 + min(left, right)` |
| **Null Handling** | Can use `max(0, depth)` | Must skip null children |
| **Single Child** | Works with `max(0, child)` | Must only consider non-null child |
| **Early Termination** | No early exit possible | BFS can stop at first leaf |

## Edge Cases

1. **Empty tree**: `root = null` → return `0`
2. **Single node**: `root = [1]` → return `1`
3. **Skewed tree**: `[2,null,3,null,4]` → return `3` (must follow the only path)
4. **Balanced tree**: `[3,9,20,null,null,15,7]` → return `2` (shortest path: 3 → 9)
5. **One child only**: `[1,2,null]` → return `2` (can't use null as depth 0)

## Common Mistakes

1. **Wrong null handling**: Using `min(minDepth(left), minDepth(right))` when one is null
   ```cpp
   // WRONG:
   return 1 + min(minDepth(root->left), minDepth(root->right));
   // If left is null, minDepth(left) = 0, min(0, right) = 0 ❌
   ```

2. **Not checking leaf**: Forgetting to return 1 for leaf nodes
3. **Base case error**: Returning wrong value for null node
4. **Off-by-one**: Counting edges instead of nodes
5. **Missing single-child check**: Not handling nodes with only one child

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Recursive DFS (Provided)** | O(n) | O(h) | Handles single child correctly | May explore deep paths unnecessarily |
| **Simplified Recursive DFS** | O(n) | O(h) | Cleaner code, explicit handling | Same as above |
| **Iterative BFS** | O(n) | O(w) | Can stop early at first leaf | More space for wide trees |
| **Iterative DFS** | O(n) | O(h) | No recursion overhead | More complex than recursive |

## When to Use Each Approach

- **Recursive DFS**: Most common, simplest solution
- **Simplified Recursive DFS**: When you want cleaner code
- **Iterative BFS**: When shallow leaves exist early (can optimize)
- **Iterative DFS**: When avoiding recursion

## Related Problems

- [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Find maximum depth (similar problem)
- [LC 110: Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) - Check if tree is balanced
- [LC 112: Path Sum](https://leetcode.com/problems/path-sum/) - Check if path sum exists
- [LC 111: Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) - This problem
- [LC 559: Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) - Extension to N-ary tree

---

*This problem demonstrates the importance of **correctly handling single-child nodes** when finding minimum depth. Unlike maximum depth, we cannot treat null children as having depth 0, as that would incorrectly shorten the path to a leaf.*

