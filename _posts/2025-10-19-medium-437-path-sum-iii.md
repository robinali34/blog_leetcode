---
layout: post
title: "[Medium] 437. Path Sum III"
date: 2025-10-19 17:25:53 -0700
categories: leetcode algorithm medium cpp tree dfs recursion problem-solving
---
Given the `root` of a binary tree and an integer `targetSum`, return the number of paths where the sum of the values along the path equals `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

## Examples

**Example 1:**
```
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are:
- Path 1: 10 → 5 → 3 = 18 (sum = 18)
- Path 2: 5 → 3 = 8 (sum = 8)
- Path 3: 5 → 2 → 1 = 8 (sum = 8)
```

**Example 2:**
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
Explanation: The paths that sum to 22 are:
- Path 1: 5 → 4 → 11 → 2 = 22 (sum = 22)
- Path 2: 4 → 11 → 7 = 22 (sum = 22)
- Path 3: 5 → 8 → 4 → 5 = 22 (sum = 22)
```

## Constraints

- The number of nodes in the tree is in the range `[0, 1000]`.
- `-10^9 <= Node.val <= 10^9`
- `-1000 <= targetSum <= 1000`

## Thinking Process

1. **Start from each node:** Check all paths starting from each node
1. **Current node check:** If node value equals target, count it

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
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Solution

**Time Complexity:** O(n²) where n is the number of nodes  
**Space Complexity:** O(h) where h is the height of the tree

Use DFS to explore all possible paths starting from each node, checking if the path sum equals the target.

```cpp
class Solution {
private:
    int dfs(TreeNode* node, int targetSum) {
        if(!node) return 0;
        int cnt = 0;
        if(targetSum == node->val) cnt++;
        return cnt + dfs(node->left, targetSum - node->val) + dfs(node->right, targetSum - node->val);
    }
    
public:
    int pathSum(TreeNode* root, int targetSum) {
        if(!root) return 0;
        return dfs(root, targetSum) + pathSum(root->left, targetSum) + pathSum(root->right, targetSum);
    }
};
```

### Solution Explanation
**Key Insight:** For each node, check all paths starting from that node, then recursively check paths starting from its children.

**Steps:**
1. **Base case:** If root is null, return 0
2. **DFS from current node:** Count paths starting from current node
3. **Recursive calls:** Check paths starting from left and right children
4. **Sum results:** Return total count from all three sources

## Step-by-Step Example

### Example: `root = [10,5,-3,3,2,null,11,3,-2,null,1]`, `targetSum = 8`

**Tree Structure:**
```
        10
       /  \
      5   -3
     / \    \
    3   2   11
   / \   \
  3  -2   1
```

**DFS from each node:**

| Node | Target | Paths Found | Count |
|------|--------|------------|-------|
| 10 | 8 | 10→5→3 (18), 10→5→2→1 (18) | 0 |
| 5 | 8 | 5→3 (8), 5→2→1 (8) | 2 |
| -3 | 8 | -3→11 (8) | 1 |
| 3 | 8 | 3 (3) | 0 |
| 2 | 8 | 2→1 (3) | 0 |
| 11 | 8 | 11 (11) | 0 |
| 3 | 8 | 3 (3) | 0 |
| -2 | 8 | -2 (-2) | 0 |
| 1 | 8 | 1 (1) | 0 |

**Total count:** 2 + 1 = 3

## Algorithm Breakdown

### DFS Function:
```cpp
int dfs(TreeNode* node, int targetSum) {
    if(!node) return 0;
    int cnt = 0;
    if(targetSum == node->val) cnt++;
    return cnt + dfs(node->left, targetSum - node->val) + dfs(node->right, targetSum - node->val);
}
```

**Process:**
1. **Base case:** Return 0 if node is null
2. **Check current node:** If node value equals target, increment count
3. **Recursive calls:** Check left and right subtrees with updated target
4. **Return total count** from current node and subtrees

### Main Function:
```cpp
int pathSum(TreeNode* root, int targetSum) {
    if(!root) return 0;
    return dfs(root, targetSum) + pathSum(root->left, targetSum) + pathSum(root->right, targetSum);
}
```

**Process:**
1. **Base case:** Return 0 if root is null
2. **DFS from root:** Count paths starting from root
3. **Recursive calls:** Count paths starting from left and right subtrees
4. **Return total count** from all sources

### Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| DFS from each node | O(n) | O(h) |
| Total DFS calls | O(n) | O(h) |
| **Total** | **O(n²)** | **O(h)** |

Where n is the number of nodes and h is the height of the tree.

## Detailed Example Walkthrough

### Example: `root = [5,4,8,11,null,13,4,7,2,null,null,5,1]`, `targetSum = 22`

**Tree Structure:**
```
        5
       / \
      4   8
     /   / \
    11  13  4
   / \     / \
  7   2   5   1
```

**DFS from each node:**

| Node | Target | Paths Found | Count |
|------|--------|------------|-------|
| 5 | 22 | 5→4→11→2 (22), 5→8→4→5 (22) | 2 |
| 4 | 22 | 4→11→7 (22) | 1 |
| 8 | 22 | 8→13 (21), 8→4→5 (17), 8→4→1 (13) | 0 |
| 11 | 22 | 11→7 (18), 11→2 (13) | 0 |
| 13 | 22 | 13 (13) | 0 |
| 4 | 22 | 4→5 (9), 4→1 (5) | 0 |
| 7 | 22 | 7 (7) | 0 |
| 2 | 22 | 2 (2) | 0 |
| 5 | 22 | 5 (5) | 0 |
| 1 | 22 | 1 (1) | 0 |

**Total count:** 2 + 1 = 3

## Common Mistakes

1. **Empty tree:** `root = null` → `0`
2. **Single node:** `root = [5]`, `targetSum = 5` → `1`
3. **No valid paths:** `root = [1,2,3]`, `targetSum = 10` → `0`
4. **Negative values:** `root = [1,-2,3]`, `targetSum = 1` → `2`

1. **Wrong path direction:** Allowing paths to go upwards
2. **Missing base cases:** Not handling null nodes properly
3. **Incorrect target update:** Not subtracting current node value
4. **Double counting:** Counting same path multiple times

## Related Problems

- [112. Path Sum](https://www.leetcode.com/problems/path-sum/)
- [113. Path Sum II](https://www.leetcode.com/problems/path-sum-ii/)
- [124. Binary Tree Maximum Path Sum](https://www.leetcode.com/problems/binary-tree-maximum-path-sum/)
- [257. Binary Tree Paths](https://www.leetcode.com/problems/binary-tree-paths/)

## Why This Solution Works

### DFS Approach:
1. **Complete coverage:** Checks all possible starting points
2. **Path continuation:** Allows paths to start from any node
3. **Target reduction:** Properly updates target for subtrees
4. **Recursive structure:** Naturally handles tree traversal

### Path Counting:
1. **Current node check:** Counts if current node equals target
2. **Subtree exploration:** Continues checking with updated target
3. **Sum accumulation:** Adds counts from all subtrees
4. **Correct result:** Produces accurate path count

### Key Algorithm Properties:
1. **Correctness:** Always produces valid result
2. **Completeness:** Checks all possible paths
3. **Efficiency:** O(n²) time complexity
4. **Simplicity:** Easy to understand and implement

## References

- [LC 437: Path Sum III on LeetCode](https://www.leetcode.com/problems/path-sum-iii/)
- [LeetCode Discuss — LC 437: Path Sum III](https://www.leetcode.com/problems/path-sum-iii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/path-sum-iii/editorial/) *(may require premium)*

## Key Takeaways

### DFS Approach:
1. **Start from each node:** Check all paths starting from each node
2. **Path continuation:** Paths can start from any node and go downwards
3. **Target reduction:** Subtract current node value from target
4. **Recursive exploration:** Explore all possible paths

### Path Counting:
1. **Current node check:** If node value equals target, count it
2. **Subtree exploration:** Continue checking with updated target
3. **Sum accumulation:** Add counts from all subtrees
4. **Complete coverage:** Check all possible starting points
