---
layout: post
title: "[Easy] 938. Range Sum of BST"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm easy cpp tree bst dfs problem-solving
permalink: /posts/2025-11-24-easy-938-range-sum-of-bst/
tags: [leetcode, easy, tree, bst, dfs, recursion]
---

# [Easy] 938. Range Sum of BST

Given the `root` node of a binary search tree and two integers `low` and `high`, return *the sum of values of all nodes with a value in the **inclusive** range `[low, high]`*.

## Examples

**Example 1:**
```
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
```

**Example 2:**
```
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
```

## Constraints

- The number of nodes in the tree is in the range `[1, 2 * 10^4]`.
- `1 <= Node.val <= 10^5`
- `1 <= low <= high <= 10^5`
- All `Node.val` are **unique**.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Range definition**: What is the range? (Assumption: [low, high] - inclusive on both ends, sum all node values in this range)

2. **BST properties**: What are BST properties? (Assumption: Left subtree < root < right subtree - can use this to prune)

3. **Return value**: What should we return? (Assumption: Integer - sum of all node values in range [low, high])

4. **Range boundaries**: Are boundaries inclusive? (Assumption: Yes - nodes with value equal to low or high are included)

5. **Empty tree**: What if tree is empty? (Assumption: Return 0 - no nodes to sum)

## Solution: Recursive DFS with BST Pruning

**Time Complexity:** O(n) worst case, but often better due to pruning  
**Space Complexity:** O(h) where h is the height of the tree (recursion stack)

The key insight is to leverage BST properties to prune branches that cannot contain values in the range `[low, high]`.

### Solution: Recursive DFS with Pruning

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
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(root == nullptr) return 0;
        
        if(root->val > high) {
            return rangeSumBST(root->left, low, high);
        } else if(root->val < low) {
            return rangeSumBST(root->right, low, high);
        }
        
        return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
    }
};
```

## How the Algorithm Works

### Key Insight: BST Property Pruning

**BST Property:** For any node:
- All nodes in left subtree have values < node.val
- All nodes in right subtree have values > node.val

**Pruning Logic:**
- If `root->val > high`: All values in right subtree are > high, skip right subtree
- If `root->val < low`: All values in left subtree are < low, skip left subtree
- Otherwise: Include current node and search both subtrees

### Step-by-Step Example: `root = [10,5,15,3,7,null,18], low = 7, high = 15`

```
Tree Structure:
        10
       /  \
      5    15
     / \     \
    3   7     18

Traversal:
1. root=10, val=10
   - 10 is in [7,15] → include 10
   - Search left subtree (5)
   - Search right subtree (15)
   Sum = 10 + ...

2. root=5, val=5
   - 5 < 7 (low) → skip left subtree (3)
   - Search right subtree (7)
   Sum = 10 + ...

3. root=7, val=7
   - 7 is in [7,15] → include 7
   - Search left subtree (null)
   - Search right subtree (null)
   Sum = 10 + 7 + ...

4. root=15, val=15
   - 15 is in [7,15] → include 15
   - Search left subtree (null)
   - Search right subtree (18)
   Sum = 10 + 7 + 15 + ...

5. root=18, val=18
   - 18 > 15 (high) → skip right subtree
   - Search left subtree (null)
   Sum = 10 + 7 + 15

Final: 10 + 7 + 15 = 32
```

**Visual Representation:**
```
        10 ✓ (in range)
       /  \
      5 ✗  15 ✓ (in range)
     / \     \
    3 ✗ 7 ✓  18 ✗
          (in range)

Nodes visited: 10, 5, 7, 15, 18
Nodes included: 10, 7, 15
Sum = 32
```

## Key Insights

1. **BST Property**: Use BST ordering to skip entire subtrees
2. **Pruning Optimization**: Don't traverse subtrees that can't contain valid values
3. **Inclusive Range**: Include nodes where `low <= val <= high`
4. **Recursive Structure**: Natural fit for tree traversal

## Algorithm Breakdown

### Base Case

```cpp
if(root == nullptr) return 0;
```

**Why:** Empty subtree contributes 0 to the sum.

### Pruning Cases

```cpp
if(root->val > high) {
    return rangeSumBST(root->left, low, high);
}
```

**Why:** If current value > high, all values in right subtree are also > high (BST property). Only search left subtree.

```cpp
else if(root->val < low) {
    return rangeSumBST(root->right, low, high);
}
```

**Why:** If current value < low, all values in left subtree are also < low (BST property). Only search right subtree.

### Include Current Node

```cpp
return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
```

**Why:** Current node is in range `[low, high]`, so:
- Include its value
- Search both subtrees (they might contain valid values)

## Edge Cases

1. **Single node**: Tree with one node
2. **All nodes in range**: Entire tree contributes to sum
3. **No nodes in range**: Return 0
4. **Range at boundaries**: low or high equals node values
5. **Skewed tree**: Left-skewed or right-skewed BST

## Alternative Approaches

### Approach 2: Iterative DFS with Stack

**Time Complexity:** O(n) worst case  
**Space Complexity:** O(h)

```cpp
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(root == nullptr) return 0;
        
        stack<TreeNode*> stk;
        stk.push(root);
        int sum = 0;
        
        while(!stk.empty()) {
            TreeNode* node = stk.top();
            stk.pop();
            
            if(node == nullptr) continue;
            
            if(node->val > high) {
                stk.push(node->left);
            } else if(node->val < low) {
                stk.push(node->right);
            } else {
                sum += node->val;
                stk.push(node->left);
                stk.push(node->right);
            }
        }
        
        return sum;
    }
};
```

**Pros:**
- Avoids recursion stack overflow
- More control over traversal

**Cons:**
- More verbose
- Still O(h) space for stack

### Approach 3: Inorder Traversal (No Pruning)

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

```cpp
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(root == nullptr) return 0;
        
        int sum = 0;
        if(root->val >= low && root->val <= high) {
            sum += root->val;
        }
        
        sum += rangeSumBST(root->left, low, high);
        sum += rangeSumBST(root->right, low, high);
        
        return sum;
    }
};
```

**Pros:**
- Simple, straightforward

**Cons:**
- No pruning optimization
- Visits all nodes even if outside range

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Recursive with Pruning** | O(n) worst, often better | O(h) | Simple, efficient | Recursion overhead |
| **Iterative with Stack** | O(n) worst, often better | O(h) | No recursion | More code |
| **Inorder (No Pruning)** | O(n) | O(h) | Simple | Less efficient |

## Implementation Details

### Why Pruning Works

**BST Property:**
```
For node with value v:
- Left subtree: all values < v
- Right subtree: all values > v
```

**Pruning Logic:**
- `v > high` → Right subtree values > v > high → Skip right
- `v < low` → Left subtree values < v < low → Skip left

### Recursive Call Structure

```cpp
return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
```

**Breakdown:**
1. `root->val`: Current node's value (if in range)
2. `rangeSumBST(root->left, ...)`: Sum from left subtree
3. `rangeSumBST(root->right, ...)`: Sum from right subtree
4. Add all three together

## Common Mistakes

1. **Forgetting BST property**: Not pruning subtrees
2. **Wrong comparison**: Using `>=` or `<=` incorrectly
3. **Not handling null**: Forgetting null checks
4. **Inclusive range**: Not including boundary values correctly
5. **Traversing unnecessary subtrees**: Not using pruning optimization

## Optimization Tips

1. **Use BST pruning**: Always leverage BST properties for efficiency
2. **Early termination**: Can optimize further if needed (not applicable here)
3. **Iterative for deep trees**: Use iterative approach to avoid stack overflow

## Related Problems

- [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) - Similar BST traversal
- [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) - BST modification
- [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) - BST traversal with counting
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) - BST property validation

## Real-World Applications

1. **Database Queries**: Range queries in B-trees (similar to BST)
2. **Interval Trees**: Finding values in ranges
3. **Statistics**: Summing values in a range
4. **Data Analysis**: Aggregating data within bounds

## Pattern Recognition

This problem demonstrates the **"BST Range Query"** pattern:

```
1. Use BST property to prune branches
2. If current value outside range → skip appropriate subtree
3. If current value in range → include and search both subtrees
4. Recursively combine results
```

Similar problems:
- Search in BST
- Count nodes in range
- Find values in range

## Why Pruning is Important

**Without Pruning:**
- Visits all n nodes: O(n) time
- No benefit from BST structure

**With Pruning:**
- Skips subtrees outside range
- Often visits fewer nodes
- Still O(n) worst case, but much better average case
- Especially efficient when range is narrow or at tree edges

## Step-by-Step Trace: `root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10`

```
Tree Structure:
          10
        /    \
       5      15
      / \    /  \
     3   7  13   18
    /   /
   1   6

Traversal:
1. root=10, val=10
   - 10 is in [6,10] → include 10
   - Search left (5) and right (15)
   Sum = 10 + ...

2. root=5, val=5
   - 5 < 6 (low) → skip left (3), search right (7)
   Sum = 10 + ...

3. root=7, val=7
   - 7 is in [6,10] → include 7
   - Search left (6) and right (null)
   Sum = 10 + 7 + ...

4. root=6, val=6
   - 6 is in [6,10] → include 6
   - Search left (null) and right (null)
   Sum = 10 + 7 + 6 + ...

5. root=15, val=15
   - 15 > 10 (high) → skip right (18), search left (13)
   Sum = 10 + 7 + 6 + ...

6. root=13, val=13
   - 13 > 10 (high) → skip right, search left (null)
   Sum = 10 + 7 + 6

Final: 10 + 7 + 6 = 23
```

## BST Property Recap

**Binary Search Tree (BST) Properties:**
1. **Left subtree**: All values < root value
2. **Right subtree**: All values > root value
3. **Both subtrees**: Are also BSTs (recursive property)

**Why This Helps:**
- If `root->val > high`, entire right subtree is > high
- If `root->val < low`, entire left subtree is < low
- We can skip entire subtrees without checking individual nodes

---

*This problem demonstrates how to leverage BST properties for efficient range queries, using pruning to avoid unnecessary traversals.*

