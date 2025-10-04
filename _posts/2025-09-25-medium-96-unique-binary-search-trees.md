---
layout: post
title: "[Medium] 96. Unique Binary Search Trees"
date: 2025-09-25 00:00:00 -0000
categories: leetcode
tags: [algorithm, dynamic-programming, math, catalan-numbers, medium, cpp]
---

# [Medium] 96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) that have exactly n nodes with values from 1 to n.

## Examples

**Example 1:**
```
Input: n = 3
Output: 5
Explanation: For n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

**Example 2:**
```
Input: n = 1
Output: 1
```

## Constraints

- 1 <= n <= 19

## Approach

There are three main approaches to solve this problem:

1. **Dynamic Programming**: Build up the solution using the recurrence relation
2. **Catalan Numbers**: Use the mathematical formula for Catalan numbers
3. **Optimized DP**: Slight variations in DP implementation

The key insight is that the number of unique BSTs follows the Catalan number sequence.

## Solution 1: Dynamic Programming (Initialized with 1s)

```cpp
class Solution {
public:
    int numTrees(int n) {
        vector<int> cache(n + 1, 1);
        for(int i = 2; i <= n; i++) {
            int sum = 0;
            for(int j = 1; j <= i; j++) {
                int left = j - 1;
                int right = i - j;
                sum += cache[left] * cache[right];
            }
            cache[i] = sum;
        }
        return cache[n];
    }
};
```

**Time Complexity:** O(n²) - Nested loops
**Space Complexity:** O(n) - DP array

## Solution 2: Dynamic Programming (Explicit Base Cases)

```cpp
class Solution {
public:
    int numTrees(int n) {
        vector<int> cache(n + 1, 0);
        cache[0] = 1;
        cache[1] = 1;
        for(int i = 2; i <= n; i++) {
            for(int j = 1; j <= i; j++) {
                cache[i] += cache[j - 1] * cache[i - j];
            }
        }
        return cache[n];
    }
};
```

**Time Complexity:** O(n²) - Nested loops
**Space Complexity:** O(n) - DP array

## Solution 3: Catalan Numbers Formula

```cpp
class Solution {
public:
    int numTrees(int n) {
        long long rtn = 1;
        for(int i = 0; i < n; i++) {
            rtn = rtn * 2 * (2 * i + 1) / (i + 2);
        }
        return (int)rtn;
    }
};
```

**Time Complexity:** O(n) - Single loop
**Space Complexity:** O(1) - Constant space

## Step-by-Step Example (Solution 1)

For n = 3:

1. **Initial**: cache = [1, 1, 1, 1]
2. **i = 2**: 
   - j = 1: left = 0, right = 1 → cache[0] * cache[1] = 1 * 1 = 1
   - j = 2: left = 1, right = 0 → cache[1] * cache[0] = 1 * 1 = 1
   - cache[2] = 1 + 1 = 2
3. **i = 3**:
   - j = 1: left = 0, right = 2 → cache[0] * cache[2] = 1 * 2 = 2
   - j = 2: left = 1, right = 1 → cache[1] * cache[1] = 1 * 1 = 1
   - j = 3: left = 2, right = 0 → cache[2] * cache[0] = 2 * 1 = 2
   - cache[3] = 2 + 1 + 2 = 5

Final result: 5

## Mathematical Insight

The number of unique BSTs with n nodes is the **n-th Catalan number**:

C(n) = (2n)! / ((n+1)! * n!) = (1/(n+1)) * C(2n,n)

The recurrence relation is:
C(n) = Σ(i=1 to n) C(i-1) * C(n-i)

## Key Insights

1. **Recurrence Relation**: For each root i, left subtree has i-1 nodes, right subtree has n-i nodes
2. **Catalan Numbers**: The sequence follows Catalan number pattern
3. **Dynamic Programming**: Build up solutions from smaller subproblems
4. **Mathematical Formula**: Direct calculation using Catalan number formula

## Solution Comparison

- **DP (Solution 1)**: Initializes all values to 1, simpler logic
- **DP (Solution 2)**: Explicit base cases, more traditional DP approach
- **Catalan Formula**: Most efficient O(n) time, O(1) space

## Common Mistakes

1. **Not understanding the recurrence relation** for BST counting
2. **Integer overflow** in Catalan number calculation
3. **Incorrect base cases** in DP approach
4. **Confusing with permutation problems** instead of combination

## Edge Cases

- n = 1: return 1 (single node)
- n = 2: return 2 (two possible BSTs)
- n = 0: return 1 (empty tree)

## Related Problems

- [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)
- [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)
- [96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) (this problem)
