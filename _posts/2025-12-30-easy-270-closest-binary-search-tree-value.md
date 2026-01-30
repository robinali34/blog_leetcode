---
layout: post
title: "270. Closest Binary Search Tree Value"
date: 2025-12-30 22:30:00 -0700
categories: [leetcode, easy, binary-search-tree, tree, recursion, binary-search]
permalink: /2025/12/30/easy-270-closest-binary-search-tree-value/
---

# 270. Closest Binary Search Tree Value

## Problem Statement

Given the `root` of a binary search tree and a `target` value, return *the value in the BST that is closest to the `target`*. If there are multiple answers, print the smallest.

## Examples

**Example 1:**
```
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
```

**Example 2:**
```
Input: root = [1], target = 4.428571
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `0 <= Node.val <= 10^9`
- `-10^9 <= target <= 10^9`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Closest definition**: What does "closest" mean? (Assumption: Node value with minimum absolute difference from target - |node.val - target|)

2. **BST properties**: What are BST properties? (Assumption: Left subtree < root < right subtree - can use this to prune search)

3. **Return value**: What should we return? (Assumption: Integer - value of node closest to target)

4. **Tie-breaking**: What if multiple nodes are equally close? (Assumption: Return any one - typically return first found)

5. **Empty tree**: What if tree is empty? (Assumption: Per constraints, tree has at least 1 node)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Traverse the entire tree (inorder, preorder, or postorder) and collect all node values. Then find the value with minimum absolute difference from the target. This approach visits all nodes regardless of BST properties, giving O(n) time and O(n) space for storing values. It works but doesn't leverage BST properties for optimization.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use BST properties: if target < node value, search left subtree; if target > node value, search right subtree. Track the closest value seen so far. This reduces the search space but still may need to explore both subtrees in some cases. Time complexity is O(h) where h is height, but worst case is still O(n) for unbalanced trees.

**Step 3: Optimized Solution (5 minutes)**

Use iterative or recursive traversal that leverages BST properties. At each node, update the closest value if current node is closer. Then, based on target comparison, decide to go left or right (can prune one subtree). Continue until reaching a leaf or null. This achieves O(h) time complexity where h is height, and O(1) space for iterative or O(h) for recursive. The key insight is that BST properties allow us to prune half the search space at each step, similar to binary search, making this optimal.

## Solution Approach

This problem requires finding the value in a BST that is closest to a given target. We can leverage the **BST property** to efficiently search for the closest value without exploring the entire tree.

### Key Insights:

1. **BST Property**: For any node, values in left subtree are smaller, values in right subtree are larger
2. **Recursive Search**: Compare target with current node, then search in appropriate subtree
3. **Compare Candidates**: When we have multiple candidates, compare distances to target
4. **Early Termination**: Can stop early in some cases, but need to check both sides potentially

### Algorithm:

1. **Compare with root**: Check if root value is closer than current best
2. **Search subtree**: Based on target vs root value, search left or right subtree
3. **Compare results**: Compare candidate from subtree with root value
4. **Return closest**: Return the value closest to target

## Solution

### **Solution: Recursive with Closer Value Comparison**

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
private:
    int closerValue(double lower, double upper, double target) {
        return upper - target >= target - lower? lower : upper;
    }
public:
    int closestValue(TreeNode* root, double target) {
        if(root == nullptr)  return 0;
        if(root->val > target && root->left != nullptr) {
            return closerValue(closestValue(root->left, target), root->val, target);
        }
        if(root->val < target && root->right != nullptr) {
            return closerValue(root->val, closestValue(root->right, target), target);
        }
        return root->val;
    }
};
```

### **Algorithm Explanation:**

1. **Helper Function `closerValue` (Lines 15-17)**:
   - Compares two values (`lower` and `upper`) to determine which is closer to `target`
   - Returns `lower` if `target - lower <= upper - target` (lower is closer or equal)
   - Returns `upper` otherwise
   - Handles tie-breaking: when distances are equal, prefers smaller value (lower)

2. **Base Case (Line 20)**:
   - If root is `nullptr`, return 0 (shouldn't happen per constraints, but safety check)

3. **Target Less Than Root (Lines 21-23)**:
   - If `root->val > target` and left subtree exists:
     - Search left subtree recursively
     - Compare result from left subtree with root value
     - Return the closer one

4. **Target Greater Than Root (Lines 24-26)**:
   - If `root->val < target` and right subtree exists:
     - Search right subtree recursively
     - Compare root value with result from right subtree
     - Return the closer one

5. **Leaf Node or No Appropriate Subtree (Line 27)**:
   - If we can't go further (leaf node or no appropriate subtree), return root value

### **Example Walkthrough:**

**Example 1: `root = [4,2,5,1,3], target = 3.714286`**

```
BST:
      4
     / \
    2   5
   / \
  1   3

Step 1: root = 4, target = 3.714286
  root->val (4) > target (3.714286) → go left
  root->left exists → recurse left

Step 2: root = 2, target = 3.714286
  root->val (2) < target (3.714286) → go right
  root->right exists → recurse right

Step 3: root = 3, target = 3.714286
  root->val (3) < target (3.714286) → go right
  root->right == nullptr → return 3

Step 4: Back to root = 2
  Compare: closerValue(2, 3, 3.714286)
  target - 2 = 1.714286
  3 - target = 0.285714
  1.714286 > 0.285714 → return 3

Step 5: Back to root = 4
  Compare: closerValue(3, 4, 3.714286)
  target - 3 = 0.714286
  4 - target = 0.285714
  0.714286 > 0.285714 → return 4

Result: 4
```

**Visual Representation:**

```
Target: 3.714286

Tree traversal:
4 → 2 → 3 (leaf, return 3)
     ↑
     Compare 2 vs 3: 3 is closer
     Return 3
↑
Compare 4 vs 3: 4 is closer (distance 0.286 vs 0.714)
Return 4
```

## Algorithm Breakdown

### **Key Insight: BST Property Utilization**

The algorithm uses BST property to narrow down the search:

- **If `target < root->val`**: 
  - Closest value is either in left subtree or root itself
  - Search left, then compare with root
  
- **If `target > root->val`**:
  - Closest value is either root or in right subtree
  - Search right, then compare with root

- **If `target == root->val`**:
  - Root is the closest (distance = 0)
  - Return root value

### **Closer Value Logic**

```cpp
int closerValue(double lower, double upper, double target) {
    return upper - target >= target - lower? lower : upper;
}
```

This function determines which value is closer:
- `target - lower`: Distance from lower to target
- `upper - target`: Distance from target to upper
- If `upper - target >= target - lower`: Lower is closer or equal → return lower
- Otherwise: Upper is closer → return upper

**Why this works:**
- When distances are equal, we prefer the smaller value (lower)
- This handles the constraint: "If there are multiple answers, print the smallest"

### **Recursive Structure**

The recursion follows this pattern:
1. **Base case**: Leaf node or no appropriate subtree → return current value
2. **Recursive case**: 
   - Search appropriate subtree
   - Compare subtree result with current value
   - Return closer value

## Complexity Analysis

### **Time Complexity:** O(h)
- **h = height of tree**
- **Best case (balanced BST)**: O(log n)
- **Worst case (skewed tree)**: O(n)
- **Each recursive call**: O(1) work, traverse one path from root to leaf

### **Space Complexity:** O(h)
- **Recursion stack**: O(h) for recursive calls
- **Best case (balanced BST)**: O(log n)
- **Worst case (skewed tree)**: O(n)

## Key Points

1. **BST Property**: Leverage BST structure to search efficiently
2. **Recursive Search**: Search appropriate subtree based on target comparison
3. **Compare Candidates**: Always compare subtree result with current node
4. **Tie Breaking**: When distances are equal, prefer smaller value
5. **Single Path**: Only traverse one path from root to leaf (not entire tree)

## Alternative Approaches

### **Approach 1: Recursive (Current Solution)**
- **Time**: O(h)
- **Space**: O(h) for recursion
- **Best for**: Clear and intuitive solution

### **Approach 2: Iterative**
- **Time**: O(h)
- **Space**: O(1)
- **Use while loop**: Traverse tree iteratively, track closest value
- **Best for**: Space-efficient solution

### **Approach 3: In-Order Traversal**
- **Time**: O(n)
- **Space**: O(h)
- **Traverse all nodes**: Find closest in sorted order
- **Use case**: When you need all values sorted

## Detailed Example Walkthrough

### **Example: `root = [4,2,6,1,3,5,7], target = 3.5`**

```
BST:
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Step 1: root = 4, target = 3.5
  4 > 3.5 → go left, recurse left subtree

Step 2: root = 2, target = 3.5
  2 < 3.5 → go right, recurse right subtree

Step 3: root = 3, target = 3.5
  3 < 3.5 → go right
  root->right == nullptr → return 3

Step 4: Back to root = 2
  Compare: closerValue(2, 3, 3.5)
  target - 2 = 1.5
  3 - target = 0.5
  1.5 > 0.5 → return 3

Step 5: Back to root = 4
  Compare: closerValue(3, 4, 3.5)
  target - 3 = 0.5
  4 - target = 0.5
  0.5 == 0.5 → return 3 (prefer smaller when equal)

Result: 3
```

### **Iterative Approach for Comparison**

```cpp
class Solution {
public:
    int closestValue(TreeNode* root, double target) {
        int closest = root->val;
        while (root) {
            if (abs(root->val - target) < abs(closest - target)) {
                closest = root->val;
            }
            root = target < root->val ? root->left : root->right;
        }
        return closest;
    }
};
```

**Comparison:**
- **Iterative**: O(1) space, simpler loop
- **Recursive**: O(h) space, more intuitive structure
- **Both**: O(h) time complexity

## Edge Cases

1. **Single node**: Return root value
2. **Target equals node value**: Return that value (distance = 0)
3. **Target very large**: Return maximum value in tree
4. **Target very small**: Return minimum value in tree
5. **Two nodes equally close**: Return smaller value (per constraints)

## Related Problems

- [270. Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/) - Current problem
- [272. Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) - Find k closest values
- [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) - Search for exact value
- [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) - Insert value

## Tags

`Binary Search Tree`, `Tree`, `Recursion`, `Binary Search`, `Easy`

