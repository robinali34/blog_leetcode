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

### Solution 1: Recursive DFS (Preorder)

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
    void preorder(TreeNode* node, int currNum, int& rootToLeaf) {
        if (node == nullptr) return;
        
        currNum = currNum * 10 + node->val;
        
        if (node->left == nullptr && node->right == nullptr) {
            rootToLeaf += currNum;
        }
        
        preorder(node->left, currNum, rootToLeaf);
        preorder(node->right, currNum, rootToLeaf);
    }

public:
    int sumNumbers(TreeNode* root) {
        int rootToLeaf = 0;
        preorder(root, 0, rootToLeaf);
        return rootToLeaf;
    }
};
```

**Key Points:**
- Uses preorder traversal (process node, then left, then right)
- Passes `currNum` by value (each recursive call gets its own copy)
- Accumulates sum in `rootToLeaf` by reference
- Only adds to sum when reaching a leaf node

### Solution 2: Morris Traversal (O(1) Space)

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Morris traversal allows us to traverse the tree without using a stack or recursion, achieving O(1) space complexity.

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
    int sumNumbers(TreeNode* root) {
        int rootToLeaf = 0, currNum = 0;
        int steps;
        TreeNode* predecessor;
        
        while (root != nullptr) {
            if (root->left != nullptr) {
                // Find the inorder predecessor
                predecessor = root->left;
                steps = 1;
                while (predecessor->right != nullptr && predecessor->right != root) {
                    predecessor = predecessor->right;
                    steps++;
                }
                
                if (predecessor->right == nullptr) {
                    // Make current node the right child of its predecessor
                    currNum = currNum * 10 + root->val;
                    predecessor->right = root;
                    root = root->left;
                } else {
                    // Revert the changes made in the 'if' part to restore the original tree
                    if (predecessor->left == nullptr) {
                        rootToLeaf += currNum;
                    }
                    for (int i = 0; i < steps; i++) {
                        currNum /= 10;
                    }
                    predecessor->right = nullptr;
                    root = root->right;
                }
            } else {
                currNum = currNum * 10 + root->val;
                if (root->right == nullptr) {
                    rootToLeaf += currNum;
                }
                root = root->right;
            }
        }
        
        return rootToLeaf;
    }
};
```

**How Morris Traversal Works:**
1. **Thread Creation**: When visiting a node with a left child, find its inorder predecessor
2. **Link Creation**: Make the current node the right child of its predecessor (creating a temporary link)
3. **Traversal**: Move to the left child
4. **Link Removal**: When returning to a node via the temporary link, remove it and move right
5. **Number Tracking**: Track the current number and steps taken to backtrack correctly

**Key Points:**
- **O(1) space**: No recursion stack or explicit stack needed
- **Temporary links**: Uses right pointers of leaf nodes to create temporary links
- **Backtracking**: Divides `currNum` by 10 to backtrack when removing links
- **Complex logic**: More complex but achieves optimal space complexity

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

### Solution 1: Recursive Preorder

#### Helper Function: `preorder(node, currNum, rootToLeaf)`

```cpp
void preorder(TreeNode* node, int currNum, int& rootToLeaf) {
    if (node == nullptr) return;
```

**Why:** Handle null nodes gracefully. Return early if node is null.

```cpp
    currNum = currNum * 10 + node->val;
```

**Why:** Build the current path number by:
- Multiplying previous sum by 10 (shift digits left)
- Adding current node's value (append new digit)

```cpp
    if (node->left == nullptr && node->right == nullptr) {
        rootToLeaf += currNum;
    }
```

**Why:** Leaf node reached. Add the complete path number to the total sum.

```cpp
    preorder(node->left, currNum, rootToLeaf);
    preorder(node->right, currNum, rootToLeaf);
```

**Why:** Continue traversal to both subtrees. `currNum` is passed by value, so each recursive call gets its own copy.

#### Main Function: `sumNumbers(root)`

```cpp
int sumNumbers(TreeNode* root) {
    int rootToLeaf = 0;
    preorder(root, 0, rootToLeaf);
    return rootToLeaf;
}
```

**Why:** Initialize sum to 0, start preorder traversal from root, return accumulated sum.

**Key Difference from Previous Approach:**
- Uses `void` function that accumulates result in a reference parameter
- Passes `currNum` by value (each call gets independent copy)
- More explicit about accumulating the sum

### Solution 2: Morris Traversal

#### Key Components

**1. Finding Predecessor:**
```cpp
predecessor = root->left;
steps = 1;
while (predecessor->right != nullptr && predecessor->right != root) {
    predecessor = predecessor->right;
    steps++;
}
```
- Find the rightmost node in the left subtree
- Track number of steps for backtracking

**2. Creating Temporary Link:**
```cpp
if (predecessor->right == nullptr) {
    currNum = currNum * 10 + root->val;
    predecessor->right = root;  // Create link
    root = root->left;
}
```
- Create temporary link from predecessor to current node
- This allows us to return to current node later

**3. Removing Link and Backtracking:**
```cpp
else {
    if (predecessor->left == nullptr) {
        rootToLeaf += currNum;
    }
    for (int i = 0; i < steps; i++) {
        currNum /= 10;  // Backtrack number
    }
    predecessor->right = nullptr;  // Remove link
    root = root->right;
}
```
- When we return via temporary link, we've finished left subtree
- Backtrack `currNum` by dividing by 10 for each step
- Remove temporary link to restore tree structure

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
| **Recursive DFS (Preorder)** | O(n) | O(h) | Simple, elegant | Recursion overhead |
| **Morris Traversal** | O(n) | O(1) | Optimal space | Complex implementation |
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

**Morris Traversal Advantages:**
- O(1) space complexity (optimal)
- No recursion or explicit stack
- Useful for memory-constrained environments

**Morris Traversal Disadvantages:**
- More complex implementation
- Modifies tree structure temporarily (though restored)
- Harder to understand and debug

**BFS Alternative:**
- Can work but less intuitive
- Requires storing path information for each node
- More space for wide trees

## Morris Traversal Deep Dive

### How It Works

Morris traversal is a technique to traverse a binary tree without using a stack or recursion. It uses temporary links (threads) to navigate the tree.

**Key Steps:**

1. **If current node has left child:**
   - Find the inorder predecessor (rightmost node in left subtree)
   - If predecessor's right is null, create a temporary link to current node
   - Move to left child
   - If predecessor's right points to current, we've already visited left subtree
   - Remove the link and move to right child

2. **If current node has no left child:**
   - Process current node
   - Move to right child

### Step-by-Step Morris Traversal: `root = [1,2,3]`

```
Initial: root = 1, currNum = 0, rootToLeaf = 0

Step 1: root = 1 (has left child = 2)
  - Find predecessor: 2 (no right child)
  - currNum = 0 * 10 + 1 = 1
  - Create link: 2->right = 1
  - Move to left: root = 2

Step 2: root = 2 (no left child)
  - currNum = 1 * 10 + 2 = 12
  - Is leaf? Yes → rootToLeaf += 12 (rootToLeaf = 12)
  - Move to right: root = 1 (via temporary link)

Step 3: root = 1 (has left child = 2, and 2->right = 1)
  - Predecessor found with link back to 1
  - Backtrack: currNum = 12 / 10 = 1
  - Remove link: 2->right = nullptr
  - Move to right: root = 3

Step 4: root = 3 (no left child)
  - currNum = 1 * 10 + 3 = 13
  - Is leaf? Yes → rootToLeaf += 13 (rootToLeaf = 25)
  - Move to right: root = nullptr

Done: return 25
```

### Why Divide by 10?

When backtracking in Morris traversal, we need to undo the number accumulation. Since we multiplied by 10 for each step down, we divide by 10 for each step back up.

```
Going down: 0 → 1 → 12
Going up:   12 → 1 (divide by 10)
Going down: 1 → 13
```

### When to Use Morris Traversal

**Use Morris Traversal when:**
- Memory is extremely constrained
- Need O(1) space complexity
- Tree structure can be temporarily modified

**Use Recursive DFS when:**
- Code simplicity is priority
- Space is not a concern
- Need easy-to-understand solution

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

