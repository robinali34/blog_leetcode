---
layout: post
title: "[Easy] 509. Fibonacci Number"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm easy cpp dynamic-programming recursion problem-solving
permalink: /posts/2025-11-18-easy-509-fibonacci-number/
tags: [leetcode, easy, dynamic-programming, recursion, math, fibonacci]
---

# [Easy] 509. Fibonacci Number

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Fibonacci definition**: What is the Fibonacci sequence? (Assumption: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1)

2. **Base cases**: What are the base cases? (Assumption: F(0) = 0, F(1) = 1 - standard Fibonacci)

3. **Return value**: What should we return? (Assumption: Integer - F(n) - nth Fibonacci number)

4. **Input range**: What is the range of n? (Assumption: Per constraints, 0 <= n <= 30 - small range)

5. **Time complexity**: What time complexity is expected? (Assumption: O(n) - linear time with DP, O(2^n) naive recursion)

## Interview Deduction Process (10 minutes)

### Step 1: Brute-Force Approach (2 minutes)
**Initial Thought**: "I need to compute Fibonacci. Let me use recursive definition directly."

**Naive Solution**: Recursive function: F(n) = F(n-1) + F(n-2) with base cases F(0)=0, F(1)=1.

**Complexity**: O(2^n) time, O(n) space

**Issues**:
- Exponential time complexity
- Recomputes same values many times
- Very inefficient
- Doesn't leverage memoization

### Step 2: Semi-Optimized Approach (3 minutes)
**Insight**: "I can use memoization to cache computed values."

**Improved Solution**: Use recursion with memoization. Store computed Fibonacci values in hash map/array to avoid recomputation.

**Complexity**: O(n) time, O(n) space

**Improvements**:
- Memoization eliminates recomputation
- O(n) time is much better
- Still uses recursion stack
- Can optimize space

### Step 3: Optimized Solution (5 minutes)
**Final Optimization**: "I can use iterative DP to avoid recursion stack."

**Best Solution**: Iterative DP (bottom-up). Use two variables to track F(n-1) and F(n-2), compute F(n) iteratively.

**Complexity**: O(n) time, O(1) space

**Key Realizations**:
1. DP is natural approach for Fibonacci
2. O(n) time is optimal
3. O(1) space is optimal with iterative approach
4. Bottom-up avoids recursion overhead

## Solution: Dynamic Programming (Bottom-Up)

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

## How the Algorithm Works

### Step-by-Step Example: `n = 5`

```
Initial: cache = [0, 0, 0, 0, 0, 0]
         cache[0] = 0
         cache[1] = 1

i = 2: cache[2] = cache[1] + cache[0] = 1 + 0 = 1
        cache = [0, 1, 1, 0, 0, 0]

i = 3: cache[3] = cache[2] + cache[1] = 1 + 1 = 2
        cache = [0, 1, 1, 2, 0, 0]

i = 4: cache[4] = cache[3] + cache[2] = 2 + 1 = 3
        cache = [0, 1, 1, 2, 3, 0]

i = 5: cache[5] = cache[4] + cache[3] = 3 + 2 = 5
        cache = [0, 1, 1, 2, 3, 5]

Result: F(5) = 5
```

### Visual Representation

```
Fibonacci Sequence:
F(0) = 0
F(1) = 1
F(2) = F(1) + F(0) = 1 + 0 = 1
F(3) = F(2) + F(1) = 1 + 1 = 2
F(4) = F(3) + F(2) = 2 + 1 = 3
F(5) = F(4) + F(3) = 3 + 2 = 5

Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

## Key Insights

1. **Bottom-Up DP**: Build solution from base cases upward
2. **Memoization**: Store previously computed values to avoid recalculation
3. **Base Cases**: F(0) = 0 and F(1) = 1 are the foundation
4. **Recurrence Relation**: F(n) = F(n-1) + F(n-2) for n > 1
5. **Overlapping Subproblems**: Each Fibonacci number depends on previous two

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

## Edge Cases

1. **n = 0**: Return 0
2. **n = 1**: Return 1
3. **n = 2**: Return 1 (first non-base Fibonacci number)
4. **n = 30**: Maximum constraint value

## Alternative Approaches

### Approach 2: Space-Optimized Iterative (O(1) Space)

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Only keep track of the last two values instead of the entire array:

```cpp
class Solution {
public:
    int fib(int n) {
        if(n <= 0) return 0;
        if(n == 1) return 1;
        
        int prev2 = 0;  // F(0)
        int prev1 = 1;  // F(1)
        
        for(int i = 2; i <= n; i++) {
            int curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        
        return prev1;
    }
};
```

**Pros:**
- O(1) space complexity
- More memory efficient
- Same time complexity

**Cons:**
- Can't access previous Fibonacci numbers after computation

### Approach 3: Recursive with Memoization

**Time Complexity:** O(n)  
**Space Complexity:** O(n) due to recursion stack and memoization

```cpp
class Solution {
public:
    int fib(int n) {
        vector<int> memo(n + 1, -1);
        return fibHelper(n, memo);
    }
    
private:
    int fibHelper(int n, vector<int>& memo) {
        if(n <= 0) return 0;
        if(n == 1) return 1;
        
        if(memo[n] != -1) return memo[n];
        
        memo[n] = fibHelper(n - 1, memo) + fibHelper(n - 2, memo);
        return memo[n];
    }
};
```

**Pros:**
- Top-down approach (more intuitive for some)
- Natural recursive structure

**Cons:**
- O(n) space for recursion stack
- Function call overhead

### Approach 4: Pure Recursion (Not Recommended)

**Time Complexity:** O(2^n) - Exponential!  
**Space Complexity:** O(n) - Recursion stack

```cpp
class Solution {
public:
    int fib(int n) {
        if(n <= 0) return 0;
        if(n == 1) return 1;
        return fib(n - 1) + fib(n - 2);
    }
};
```

**Why not recommended:**
- Extremely slow for large n
- Recalculates same values multiple times
- Only shown for educational purposes

### Approach 5: Matrix Exponentiation (Advanced)

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

Uses matrix exponentiation for logarithmic time complexity:

```cpp
class Solution {
public:
    int fib(int n) {
        if(n <= 0) return 0;
        if(n == 1) return 1;
        
        // Matrix: [F(n+1) F(n)  ] = [1 1]^n
        //         [F(n)   F(n-1)]   [1 0]
        vector<vector<int>> base = \{\{1, 1\}, \{1, 0\}\};
        vector<vector<int>> result = matrixPower(base, n);
        
        return result[0][1];
    }
    
private:
    vector<vector<int>> matrixPower(vector<vector<int>>& m, int n) {
        if(n == 1) return m;
        
        vector<vector<int>> half = matrixPower(m, n / 2);
        vector<vector<int>> result = matrixMultiply(half, half);
        
        if(n % 2 == 1) {
            result = matrixMultiply(result, m);
        }
        
        return result;
    }
    
    vector<vector<int>> matrixMultiply(vector<vector<int>>& a, vector<vector<int>>& b) {
        return {
            {a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]},
            {a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]}
        };
    }
};
```

**Pros:**
- O(log n) time complexity
- Efficient for very large n

**Cons:**
- More complex implementation
- Overkill for small n (n ≤ 30)

## Complexity Analysis

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

- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Same recurrence relation
- [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) - Fibonacci with costs
- [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) - Three-term recurrence
- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) - This problem

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

