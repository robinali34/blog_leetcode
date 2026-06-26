---
layout: post
title: "[Easy] 270. Closest Binary Search Tree Value"
date: 2025-12-30 22:30:00 -0700
categories: [leetcode, easy, binary-search-tree, tree, recursion, binary-search]
permalink: /2025/12/30/easy-270-closest-binary-search-tree-value/
---
Given the `root` of a binary search tree and a `target` value, return *the value in the BST that is closest to the `target`*. If there are multiple answers, print the smallest.

## Thinking Process

Given the `root` of a binary search tree and a `target` value, return *the value in the BST that is closest to the `target`*. If there are multiple answers, print the smallest.

- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 130" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary search: shrink [lo … hi]</text>

  <rect x="40" y="40" width="48" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="64" y="58" text-anchor="middle" font-size="12" fill="#3A3530">lo</text>
  <rect x="108" y="40" width="48" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="132" y="58" text-anchor="middle" font-size="12" fill="#3A3530">mid</text>
  <rect x="196" y="40" width="48" height="32" rx="4" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="220" y="58" text-anchor="middle" font-size="12" fill="#3A3530">hi</text>
  <rect x="60" y="90" width="160" height="28" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="140" y="108" text-anchor="middle" font-size="11" fill="#6B6560">discard half each step → O(log n)</text>
  <path d="M132 72v12M220 72v12" stroke="#9A9792" stroke-width="1.5" marker-end="url(#a)"/>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Standard binary search** *(this problem)* | O(log n) | O(1) | Sorted array, `left <= right` |
| Lower / upper bound | O(log n) | O(1) | First/last position, insert index |
| Binary search on rotated array | O(log n) | O(1) | Identify sorted half, discard other |
| Binary search on answer | O(n log M) | O(1) | Monotonic predicate over search space |

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

### Complexity
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [270. Closest Binary Search Tree Value](https://www.leetcode.com/problems/closest-binary-search-tree-value/) - Current problem
- [272. Closest Binary Search Tree Value II](https://www.leetcode.com/problems/closest-binary-search-tree-value-ii/) - Find k closest values
- [700. Search in a Binary Search Tree](https://www.leetcode.com/problems/search-in-a-binary-search-tree/) - Search for exact value
- [701. Insert into a Binary Search Tree](https://www.leetcode.com/problems/insert-into-a-binary-search-tree/) - Insert value

## Tags

`Binary Search Tree`, `Tree`, `Recursion`, `Binary Search`, `Easy`

## Key Takeaways

- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

## References

- [LC 270: Closest Binary Search Tree Value on LeetCode](https://www.leetcode.com/problems/closest-binary-search-tree-value/)
- [LeetCode Discuss — LC 270: Closest Binary Search Tree Value](https://www.leetcode.com/problems/closest-binary-search-tree-value/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/closest-binary-search-tree-value/editorial/) *(may require premium)*

## Template Reference

- [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/)
