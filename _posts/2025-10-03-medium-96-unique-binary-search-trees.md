---
layout: post
title: "[Medium] 96. Unique Binary Search Trees"
date: 2025-10-03 00:00:00 -0000
categories: leetcode algorithm dynamic-programming data-structures math catalan-numbers medium cpp binary-search-trees problem-solving
---
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

## Thinking Process

There are three main approaches to solve this problem:

1. **Dynamic Programming**: Build up the solution using the recurrence relation
2. **Catalan Numbers**: Use the mathematical formula for Catalan numbers
3. **Optimized DP**: Slight variations in DP implementation

The key insight is that the number of unique BSTs follows the Catalan number sequence.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">BST count: split at root</text>

  <text x="70" y="38" text-anchor="middle" font-size="11" fill="#6B6560">root = 2</text>
  <circle cx="70" cy="55" r="14" fill="#E0D8E4" stroke="#8E9AAF" stroke-width="2"/>
  <text x="70" y="59" text-anchor="middle" font-size="11">2</text>
  <circle cx="40" cy="95" r="12" fill="#D4D8E0" stroke="#8B8680"/><text x="40" y="99" text-anchor="middle" font-size="10">1</text>
  <circle cx="100" cy="95" r="12" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="99" text-anchor="middle" font-size="10">3</text>
  <line x1="70" y1="69" x2="40" y2="83" stroke="#8E9AAF" stroke-width="1.5"/>
  <line x1="70" y1="69" x2="100" y2="83" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="25" y="115" font-size="9" fill="#7A8EA0">C(1)</text>
  <text x="95" y="115" font-size="9" fill="#7A8EA0">C(1)</text>
  <text x="200" y="70" font-size="11" fill="#5A5752">C(n) = Σ C(j-1)·C(n-j)</text>
  <text x="200" y="88" font-size="10" fill="#9A9792">pick root j, multiply subtrees</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

## Solution

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

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** There are three main approaches to solve this problem:

**How the code works:**
1. **Dynamic Programming**: Build up the solution using the recurrence relation
2. **Catalan Numbers**: Use the mathematical formula for Catalan numbers
3. **Optimized DP**: Slight variations in DP implementation

**Walkthrough** — input `n = 3`, expected output `5`:

For n = 3, there are a total of 5 unique BST's:
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

## Common Mistakes

1. **Not understanding the recurrence relation** for BST counting
2. **Integer overflow** in Catalan number calculation
3. **Incorrect base cases** in DP approach
4. **Confusing with permutation problems** instead of combination

- n = 1: return 1 (single node)
- n = 2: return 2 (two possible BSTs)
- n = 0: return 1 (empty tree)

## Related Problems

- [95. Unique Binary Search Trees II](https://www.leetcode.com/problems/unique-binary-search-trees-ii/)
- [241. Different Ways to Add Parentheses](https://www.leetcode.com/problems/different-ways-to-add-parentheses/)
- [96. Unique Binary Search Trees](https://www.leetcode.com/problems/unique-binary-search-trees/) (this problem)

## References

- [LC 96: Unique Binary Search Trees on LeetCode](https://www.leetcode.com/problems/unique-binary-search-trees/)
- [LeetCode Discuss — LC 96: Unique Binary Search Trees](https://www.leetcode.com/problems/unique-binary-search-trees/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/unique-binary-search-trees/editorial/) *(may require premium)*

## Key Takeaways

1. **Recurrence Relation**: For each root i, left subtree has i-1 nodes, right subtree has n-i nodes
2. **Catalan Numbers**: The sequence follows Catalan number pattern
3. **Dynamic Programming**: Build up solutions from smaller subproblems
4. **Mathematical Formula**: Direct calculation using Catalan number formula
