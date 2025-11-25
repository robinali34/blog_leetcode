---
layout: post
title: "[Medium] 129. Sum Root to Leaf Numbers"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp tree dfs problem-solving
permalink: /posts/2025-11-24-medium-129-sum-root-to-leaf-numbers/
tags: [leetcode, medium, tree, dfs, recursion, binary-tree]
---

# [Medium] 129. Sum Root to Leaf Numbers

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return *the total sum of all root-to-leaf numbers*. Test cases are generated so that the answer will fit in a **32-bit** integer.

A **leaf** node is a node with no children.

## Examples

**Example 1:**
```
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

**Example 2:**
```
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.
- `0 <= Node.val <= 9`
- The depth of the tree will not exceed `10`.

## Solution: DFS with Path Accumulation

**Time Complexity:** O(n) where n is the number of nodes  
**Space Complexity:** O(h) where h is the height of the tree (recursion stack)

The key insight is to traverse the tree using DFS, maintaining the current number formed by the path from root to the current node. When we reach a leaf node, we add that number to the total sum.

### Solution: Recursive DFS

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x, left(left), right(right) {}
 * };
 */
class Solution {
private:
    int dfs(TreeNode* node, int prevSum) {
        if(node == nullptr) return 0;
        
        int sum = prevSum * 10 + node->val;
        
        if(node->left == nullptr && node->right == nullptr) {
            return sum;
        } else {
            return dfs(node->left, sum) + dfs(node->right, sum);
        }
    }
public:
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
};
```

## How the Algorithm Works

### Key Insight: Path Accumulation

**Path Number Construction:**
- Start with `prevSum = 0` at the root
- For each node, multiply `prevSum` by 10 and add the current node's value
- This builds the number digit by digit as we traverse down the tree

**Leaf Detection:**
- When both `left` and `right` are `nullptr`, we've reached a leaf
- Return the accumulated sum for this path
- Otherwise, recursively sum results from left and right subtrees

### Step-by-Step Example: `root = [1,2,3]`

```
Tree Structure:
    1
   / \
  2   3

Traversal:
1. dfs(1, 0)
   - sum = 0 * 10 + 1 = 1
   - Not a leaf (has children)
   - Return dfs(2, 1) + dfs(3, 1)

2. dfs(2, 1)
   - sum = 1 * 10 + 2 = 12
   - Is a leaf (no children)
   - Return 12

3. dfs(3, 1)
   - sum = 1 * 10 + 3 = 13
   - Is a leaf (no children)
   - Return 13

Final: 12 + 13 = 25
```

**Visual Representation:**
```
        1 (prevSum=0, sum=1)
       / \
      2   3
    (sum=12) (sum=13)
    
Paths:
1->2: 12
1->3: 13
Total: 25
```

### Step-by-Step Example: `root = [4,9,0,5,1]`

```
Tree Structure:
        4
       / \
      9   0
     / \
    5   1

Traversal:
1. dfs(4, 0)
   - sum = 0 * 10 + 4 = 4
   - Not a leaf
   - Return dfs(9, 4) + dfs(0, 4)

2. dfs(9, 4)
   - sum = 4 * 10 + 9 = 49
   - Not a leaf
   - Return dfs(5, 49) + dfs(1, 49)

3. dfs(5, 49)
   - sum = 49 * 10 + 5 = 495
   - Is a leaf
   - Return 495

4. dfs(1, 49)
   - sum = 49 * 10 + 1 = 491
   - Is a leaf
   - Return 491

5. dfs(0, 4)
   - sum = 4 * 10 + 0 = 40
   - Is a leaf
   - Return 40

Final: 495 + 491 + 40 = 1026
```

## Key Insights

1. **Path Accumulation**: Build the number incrementally by multiplying by 10 and adding the current digit
2. **Leaf Detection**: Only add to sum when reaching a leaf node (no children)
3. **Recursive Sum**: Combine results from left and right subtrees
4. **Base Case**: Return 0 for null nodes (handles empty subtrees)

## Algorithm Breakdown

### Helper Function: `dfs(node, prevSum)`

```cpp
int dfs(TreeNode* node, int prevSum) {
    if(node == nullptr) return 0;
```

**Why:** Handle null nodes gracefully. Empty subtree contributes 0 to the sum.

```cpp
    int sum = prevSum * 10 + node->val;
```

**Why:** Build the current path number by:
- Multiplying previous sum by 10 (shift digits left)
- Adding current node's value (append new digit)

```cpp
    if(node->left == nullptr && node->right == nullptr) {
        return sum;
    }
```

**Why:** Leaf node reached. Return the complete path number.

```cpp
    else {
        return dfs(node->left, sum) + dfs(node->right, sum);
    }
```

**Why:** Not a leaf. Recursively sum results from both subtrees, passing the current accumulated sum.

### Main Function: `sumNumbers(root)`

```cpp
int sumNumbers(TreeNode* root) {
    return dfs(root, 0);
}
```

**Why:** Start DFS from root with initial sum of 0.

## Edge Cases

1. **Single node**: Tree with one node returns that node's value
2. **All left children**: Skewed tree to the left
3. **All right children**: Skewed tree to the right
4. **Node with value 0**: Zero values are handled correctly
5. **Deep tree**: Up to depth 10 (constraint)

## Alternative Approaches

### Approach 2: Iterative DFS with Stack

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

```cpp
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if(root == nullptr) return 0;
        
        stack<pair<TreeNode*, int>> stk;
        stk.push({root, 0});
        int totalSum = 0;
        
        while(!stk.empty()) {
            auto [node, prevSum] = stk.top();
            stk.pop();
            
            int sum = prevSum * 10 + node->val;
            
            if(node->left == nullptr && node->right == nullptr) {
                totalSum += sum;
            } else {
                if(node->right != nullptr) {
                    stk.push({node->right, sum});
                }
                if(node->left != nullptr) {
                    stk.push({node->left, sum});
                }
            }
        }
        
        return totalSum;
    }
};
```

**Pros:**
- Avoids recursion stack overflow
- More control over traversal order

**Cons:**
- More verbose
- Still O(h) space for stack

### Approach 3: BFS with Queue

**Time Complexity:** O(n)  
**Space Complexity:** O(w) where w is the maximum width

```cpp
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if(root == nullptr) return 0;
        
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        int totalSum = 0;
        
        while(!q.empty()) {
            auto [node, prevSum] = q.front();
            q.pop();
            
            int sum = prevSum * 10 + node->val;
            
            if(node->left == nullptr && node->right == nullptr) {
                totalSum += sum;
            } else {
                if(node->left != nullptr) {
                    q.push({node->left, sum});
                }
                if(node->right != nullptr) {
                    q.push({node->right, sum});
                }
            }
        }
        
        return totalSum;
    }
};
```

**Pros:**
- Level-order traversal
- Can be useful for certain tree structures

**Cons:**
- Uses more space for wide trees
- Less intuitive for this problem

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Recursive DFS** | O(n) | O(h) | Simple, elegant | Recursion overhead |
| **Iterative DFS** | O(n) | O(h) | No recursion | More code |
| **BFS** | O(n) | O(w) | Level-order | More space for wide trees |

## Implementation Details

### Why Multiply by 10?

**Decimal Number System:**
```
Path: 1 -> 2 -> 3
Step 1: 0 * 10 + 1 = 1
Step 2: 1 * 10 + 2 = 12
Step 3: 12 * 10 + 3 = 123
```

Multiplying by 10 shifts digits left, making room for the new digit.

### Recursive Call Structure

```cpp
return dfs(node->left, sum) + dfs(node->right, sum);
```

**Breakdown:**
1. `dfs(node->left, sum)`: Sum of all paths through left subtree
2. `dfs(node->right, sum)`: Sum of all paths through right subtree
3. Add both results together

### Path Accumulation Pattern

```
Root: prevSum = 0
  ↓
Node 1: prevSum * 10 + val1 = 0 * 10 + 1 = 1
  ↓
Node 2: prevSum * 10 + val2 = 1 * 10 + 2 = 12
  ↓
Leaf: return 12
```

## Common Mistakes

1. **Forgetting to multiply by 10**: Results in incorrect number construction
2. **Not checking for leaf nodes**: May double-count or miss paths
3. **Not handling null nodes**: Can cause null pointer exceptions
4. **Wrong base case**: Returning wrong value for null nodes
5. **Not passing accumulated sum**: Forgetting to pass `sum` to recursive calls

## Optimization Tips

1. **Early termination**: Not applicable here (must visit all leaves)
2. **Memoization**: Not useful (each path is unique)
3. **Iterative for deep trees**: Use iterative approach to avoid stack overflow

## Related Problems

- [112. Path Sum](https://leetcode.com/problems/path-sum/) - Check if path sum equals target
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/) - Return all paths with target sum
- [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/) - Count paths with target sum
- [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) - Return all root-to-leaf paths as strings

## Real-World Applications

1. **File System Paths**: Representing directory structures as numbers
2. **Trie Structures**: Encoding paths in prefix trees
3. **Decision Trees**: Representing decision paths numerically
4. **Expression Trees**: Evaluating numeric expressions

## Pattern Recognition

This problem demonstrates the **"Path Accumulation"** pattern:

```
1. Traverse tree from root to leaves
2. Accumulate value along the path
3. When reaching leaf, process accumulated value
4. Combine results from all paths
```

Similar problems:
- Path sum problems
- Tree serialization
- Expression evaluation

## Why DFS Works Best

**DFS Advantages:**
- Natural fit for tree traversal
- Maintains path information naturally
- Simple recursive implementation
- Efficient space usage (O(h))

**BFS Alternative:**
- Can work but less intuitive
- Requires storing path information for each node
- More space for wide trees

## Step-by-Step Trace: `root = [4,9,0,5,1]`

```
Tree:
        4
       / \
      9   0
     / \
    5   1

Call Stack:
dfs(4, 0)
├─ sum = 4
├─ dfs(9, 4)
│  ├─ sum = 49
│  ├─ dfs(5, 49) → 495 (leaf)
│  └─ dfs(1, 49) → 491 (leaf)
│  Returns: 495 + 491 = 986
└─ dfs(0, 4)
   └─ sum = 40 → 40 (leaf)
   Returns: 40

Final: 986 + 40 = 1026
```

## Mathematical Insight

**Number Construction:**
For a path with digits `d₁, d₂, ..., dₖ`:
```
Number = d₁ × 10^(k-1) + d₂ × 10^(k-2) + ... + dₖ × 10^0
```

**Our Approach:**
```
Step 1: num = d₁
Step 2: num = num × 10 + d₂ = d₁ × 10 + d₂
Step 3: num = num × 10 + d₃ = (d₁ × 10 + d₂) × 10 + d₃ = d₁ × 100 + d₂ × 10 + d₃
...
```

This matches the mathematical formula!

---

*This problem demonstrates how to traverse a binary tree while accumulating path information, using DFS to efficiently compute the sum of all root-to-leaf numbers.*

