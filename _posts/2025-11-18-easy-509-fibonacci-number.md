---
layout: post
title: "[Easy] 509. Fibonacci Number"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm easy cpp dynamic-programming recursion problem-solving
permalink: /posts/2025-11-18-easy-509-fibonacci-number/
tags: [leetcode, easy, dynamic-programming, recursion, math, fibonacci]
---
The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```

Given `n`, calculate `F(n)`.

## Examples

**Example 1:**
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

**Example 2:**
```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

**Example 3:**
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

## Constraints

- `0 <= n <= 30`

## Thinking Process

1. **Bottom-Up DP**: Build solution from base cases upward

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">1D DP recurrence</text>

  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

## Solution

**Time Complexity:** O(n) - Single pass through the array  
**Space Complexity:** O(n) - Cache array (can be optimized to O(1))

This solution uses bottom-up dynamic programming with memoization to avoid recalculating Fibonacci numbers.

### Solution: DP with Cache Array

```cpp
class Solution {
public:
    int fib(int n) {
        vector<int> cache(n + 1, 0);
        
        if(n <= 0) return 0;
        if(n == 1) return 1;
        
        cache[0] = 0;
        cache[1] = 1;
        
        for(int i = 2; i <= n; i++) {
            cache[i] = cache[i - 1] + cache[i - 2];
        }
        
        return cache[n];
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **Bottom-Up DP**: Build solution from base cases upward

**How the code works:**
1. **Bottom-Up DP**: Build solution from base cases upward
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `n = 2`, expected output `1`:

F(2) = F(1) + F(0) = 1 + 0 = 1.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DP with Cache** | O(n) | O(n) | Simple, clear | O(n) space |
| **Space-Optimized** | O(n) | O(1) | Optimal space | Can't access history |
| **Recursive + Memo** | O(n) | O(n) | Intuitive | Stack overhead |
| **Pure Recursion** | O(2^n) | O(n) | Simple | Extremely slow |
| **Matrix Exponentiation** | O(log n) | O(1) | Very fast | Complex |
## Algorithm Breakdown

```cpp
int fib(int n) {
    // Create cache array for memoization
    vector<int> cache(n + 1, 0);
    
    // Handle base cases
    if(n <= 0) return 0;
    if(n == 1) return 1;
    
    // Initialize base values
    cache[0] = 0;
    cache[1] = 1;
    
    // Build solution bottom-up
    for(int i = 2; i <= n; i++) {
        cache[i] = cache[i - 1] + cache[i - 2];
    }
    
    return cache[n];
}
```

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DP with Cache** | O(n) | O(n) | Simple, clear | O(n) space |
| **Space-Optimized** | O(n) | O(1) | Optimal space | Can't access history |
| **Recursive + Memo** | O(n) | O(n) | Intuitive | Stack overhead |
| **Pure Recursion** | O(2^n) | O(n) | Simple | Extremely slow |
| **Matrix Exponentiation** | O(log n) | O(1) | Very fast | Complex |

## Implementation Details

### Cache Initialization

```cpp
vector<int> cache(n + 1, 0);
```

Creates an array of size `n + 1` initialized to 0. This allows indexing from 0 to n.

### Base Case Handling

```cpp
if(n <= 0) return 0;
if(n == 1) return 1;
```

Early returns for base cases avoid unnecessary computation and array access.

### Loop Construction

```cpp
for(int i = 2; i <= n; i++) {
    cache[i] = cache[i - 1] + cache[i - 2];
}
```

Builds Fibonacci numbers sequentially from F(2) to F(n).

## Common Mistakes

1. **n = 0**: Return 0
2. **n = 1**: Return 1
3. **n = 2**: Return 1 (first non-base Fibonacci number)
4. **n = 30**: Maximum constraint value

1. **Off-by-one errors**: Using `i < n` instead of `i <= n`
2. **Array bounds**: Not allocating `n + 1` elements
3. **Base case order**: Checking `n == 1` before `n <= 0`
4. **Uninitialized cache**: Not setting `cache[0]` and `cache[1]`
5. **Wrong return value**: Returning `cache[n-1]` instead of `cache[n]`

## Optimization Tips

1. **Space Optimization**: Use two variables instead of array for O(1) space
2. **Early Returns**: Handle base cases immediately
3. **Memoization**: Cache results to avoid recalculation (already done in DP)
4. **Matrix Exponentiation**: Use for very large n (though n ≤ 30 here)

## Related Problems

- [70. Climbing Stairs](https://www.leetcode.com/problems/climbing-stairs/) - Same recurrence relation
- [746. Min Cost Climbing Stairs](https://www.leetcode.com/problems/min-cost-climbing-stairs/) - Fibonacci with costs
- [1137. N-th Tribonacci Number](https://www.leetcode.com/problems/n-th-tribonacci-number/) - Three-term recurrence
- [509. Fibonacci Number](https://www.leetcode.com/problems/fibonacci-number/) - This problem

## Real-World Applications

1. **Algorithm Analysis**: Fibonacci heap data structure
2. **Nature**: Modeling growth patterns (pinecones, sunflowers)
3. **Art**: Golden ratio and aesthetic proportions
4. **Computer Science**: Dynamic programming examples
5. **Mathematics**: Number theory and sequences

## Pattern Recognition

This problem demonstrates the **"Classic DP Pattern"**:

```
1. Identify base cases
2. Define recurrence relation
3. Build solution bottom-up or top-down
4. Optimize space if possible
```

Similar problems:
- Climbing Stairs
- Min Cost Climbing Stairs
- Tribonacci Number
- House Robber (with constraints)

## Fibonacci Sequence Properties

1. **Golden Ratio**: As n increases, F(n+1)/F(n) approaches φ ≈ 1.618
2. **Binet's Formula**: Closed-form solution using golden ratio
3. **Pisano Period**: Fibonacci modulo m has a repeating cycle
4. **Sum Property**: Sum of first n Fibonacci numbers = F(n+2) - 1

## Why DP is Preferred

1. **Avoids Recalculation**: Pure recursion recalculates F(3) multiple times
2. **Efficient**: O(n) time vs O(2^n) for naive recursion
3. **Simple**: Easy to understand and implement
4. **Space Trade-off**: Can optimize to O(1) space easily

---

*This problem is a perfect introduction to dynamic programming, demonstrating how memoization can transform exponential time complexity into linear time.*

## Key Takeaways

1. **Bottom-Up DP**: Build solution from base cases upward
2. **Memoization**: Store previously computed values to avoid recalculation
3. **Base Cases**: F(0) = 0 and F(1) = 1 are the foundation
4. **Recurrence Relation**: F(n) = F(n-1) + F(n-2) for n > 1
5. **Overlapping Subproblems**: Each Fibonacci number depends on previous two

## References

- [LC 509: Fibonacci Number on LeetCode](https://www.leetcode.com/problems/fibonacci-number/)
- [LeetCode Discuss — LC 509: Fibonacci Number](https://www.leetcode.com/problems/fibonacci-number/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/fibonacci-number/editorial/) *(may require premium)*

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
