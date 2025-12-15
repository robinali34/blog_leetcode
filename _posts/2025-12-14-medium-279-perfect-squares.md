---
layout: post
title: "[Medium] 279. Perfect Squares"
date: 2025-12-14 00:00:00 -0800
categories: leetcode algorithm medium cpp math dynamic-programming bfs problem-solving
---

{% raw %}
# [Medium] 279. Perfect Squares

Given an integer `n`, return *the least number of perfect square numbers that sum to* `n`.

A **perfect square** is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, `1`, `4`, `9`, and `16` are perfect squares while `3` and `11` are not.

## Examples

**Example 1:**
```
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:**
```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

**Example 3:**
```
Input: n = 1
Output: 1
```

## Constraints

- `1 <= n <= 10^4`

## Solution 1: Mathematical Approach (Legendre's Theorem) - Recommended

**Time Complexity:** O(√n)  
**Space Complexity:** O(1)

This solution uses **Legendre's three-square theorem** and **Lagrange's four-square theorem** to determine the minimum number of perfect squares needed.

```cpp
class Solution {
private:
    bool isSquare(int n) {
        int sq = (int) sqrt(n);
        return n == sq * sq;
    }
public:
    int numSquares(int n) {
        // Reduce n by removing factors of 4
        while(n % 4 == 0) {
            n /= 4;
        }
        
        // Legendre's three-square theorem: n = 4^a(8b + 7)
        // If n ≡ 7 (mod 8), then n requires 4 squares
        if(n % 8 == 7) {
            return 4;
        }
        
        // Check if n is a perfect square (requires 1 square)
        if(isSquare(n)) {
            return 1;
        }
        
        // Check if n can be expressed as sum of 2 squares
        for(int i = 1; i * i <= n; i++) {
            if(isSquare(n - i * i)) {
                return 2;
            }
        }
        
        // Otherwise, requires 3 squares (Legendre's theorem)
        return 3;
    }
};
```

### How Solution 1 Works

1. **Reduce by factors of 4**: 
   - If `n = 4^a × m`, then `numSquares(n) = numSquares(m)`
   - This optimization reduces the problem size

2. **Check for 4 squares** (Legendre's three-square theorem):
   - If `n ≡ 7 (mod 8)`, then `n` requires exactly 4 perfect squares
   - This is a necessary and sufficient condition

3. **Check for 1 square**:
   - If `n` is a perfect square, return 1

4. **Check for 2 squares**:
   - Try all possible `i` such that `i² ≤ n`
   - Check if `n - i²` is also a perfect square
   - If yes, return 2

5. **Otherwise, return 3**:
   - By Legendre's theorem, any number not covered above requires 3 squares

### Mathematical Background

**Lagrange's Four-Square Theorem**: Every natural number can be represented as the sum of four integer squares.

**Legendre's Three-Square Theorem**: A natural number can be expressed as the sum of three squares if and only if it is not of the form `4^a(8b + 7)` for nonnegative integers `a` and `b`.

**Two-Square Theorem**: A number can be expressed as the sum of two squares if and only if in its prime factorization, every prime of the form `4k + 3` occurs with an even exponent.

## Solution 2: Dynamic Programming

**Time Complexity:** O(n × √n)  
**Space Complexity:** O(n)

Bottom-up DP approach similar to coin change problem.

```cpp
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        
        // Generate all perfect squares up to n
        vector<int> squares;
        for(int i = 1; i * i <= n; i++) {
            squares.push_back(i * i);
        }
        
        // Fill DP array
        for(int i = 1; i <= n; i++) {
            for(int sq : squares) {
                if(sq > i) break;
                dp[i] = min(dp[i], dp[i - sq] + 1);
            }
        }
        
        return dp[n];
    }
};
```

### How Solution 2 Works

1. **DP array**: `dp[i]` = minimum number of perfect squares that sum to `i`
2. **Base case**: `dp[0] = 0` (0 squares needed for 0)
3. **Transition**: For each `i`, try all perfect squares `sq ≤ i`
   - `dp[i] = min(dp[i], dp[i - sq] + 1)`
4. **Result**: `dp[n]` contains the answer

### Example Walkthrough (DP)

**n = 12:**
```
Squares: [1, 4, 9]

dp[0] = 0
dp[1] = min(∞, dp[0] + 1) = 1
dp[2] = min(∞, dp[1] + 1) = 2
dp[3] = min(∞, dp[2] + 1) = 3
dp[4] = min(∞, dp[0] + 1, dp[3] + 1) = min(∞, 1, 4) = 1
dp[5] = min(∞, dp[4] + 1, dp[1] + 1) = min(∞, 2, 2) = 2
...
dp[12] = min(∞, dp[11] + 1, dp[8] + 1, dp[3] + 1) = min(∞, 4, 3, 4) = 3
```

## Solution 3: BFS (Shortest Path)

**Time Complexity:** O(n × √n)  
**Space Complexity:** O(n)

Treat as a graph problem where we find the shortest path from `n` to `0`.

```cpp
class Solution {
public:
    int numSquares(int n) {
        queue<int> q;
        unordered_set<int> visited;
        
        q.push(n);
        visited.insert(n);
        int level = 0;
        
        while(!q.empty()) {
            int size = q.size();
            level++;
            
            while(size--) {
                int curr = q.front();
                q.pop();
                
                // Try subtracting each perfect square
                for(int i = 1; i * i <= curr; i++) {
                    int next = curr - i * i;
                    
                    if(next == 0) {
                        return level;
                    }
                    
                    if(visited.find(next) == visited.end()) {
                        visited.insert(next);
                        q.push(next);
                    }
                }
            }
        }
        
        return level;
    }
};
```

### How Solution 3 Works

1. **Graph representation**: 
   - Nodes: integers from `n` down to `0`
   - Edges: subtract a perfect square to move to next node
   - Goal: reach `0` in minimum steps

2. **BFS traversal**:
   - Start from `n`
   - At each level, subtract all possible perfect squares
   - First time we reach `0`, return the level (number of squares)

3. **Visited tracking**: Avoid revisiting the same number

## Solution 4: Optimized DP (Static Squares)

**Time Complexity:** O(n × √n)  
**Space Complexity:** O(n)

Pre-compute perfect squares and use static array for better performance.

```cpp
class Solution {
public:
    int numSquares(int n) {
        static vector<int> dp(1, 0);
        
        while(dp.size() <= n) {
            int m = dp.size();
            int minSquares = INT_MAX;
            
            for(int i = 1; i * i <= m; i++) {
                minSquares = min(minSquares, dp[m - i * i] + 1);
            }
            
            dp.push_back(minSquares);
        }
        
        return dp[n];
    }
};
```

### How Solution 4 Works

- **Static DP array**: Reuses computation across multiple test cases
- **Incremental building**: Only computes values up to `n` if needed
- **Efficient**: Better for multiple queries

## Comparison of Approaches

| Aspect | Mathematical | DP | BFS | Optimized DP |
|--------|--------------|----|----|--------------|
| **Time Complexity** | O(√n) | O(n×√n) | O(n×√n) | O(n×√n) |
| **Space Complexity** | O(1) | O(n) | O(n) | O(n) |
| **Code Complexity** | Medium | Simple | Simple | Simple |
| **Best For** | Single query | General case | General case | Multiple queries |
| **Mathematical Knowledge** | High | Low | Low | Low |

## Example Walkthrough

**Input:** `n = 12`

### Solution 1 (Mathematical):
```
Step 1: Reduce by 4
  12 % 4 = 0 → n = 12 / 4 = 3
  3 % 4 = 3 ≠ 0, stop

Step 2: Check 4 squares
  3 % 8 = 3 ≠ 7, continue

Step 3: Check 1 square
  isSquare(3)? No (1²=1, 2²=4 > 3)

Step 4: Check 2 squares
  i=1: 3 - 1 = 2, isSquare(2)? No
  i=2: 3 - 4 = -1 < 0, stop
  No 2-square representation found

Step 5: Return 3
  Result: 3
```

### Solution 2 (DP):
```
Squares: [1, 4, 9]

dp[0] = 0
dp[1] = 1 (1)
dp[2] = 2 (1+1)
dp[3] = 3 (1+1+1)
dp[4] = 1 (4)
dp[5] = 2 (4+1)
dp[6] = 3 (4+1+1)
dp[7] = 4 (4+1+1+1)
dp[8] = 2 (4+4)
dp[9] = 1 (9)
dp[10] = 2 (9+1)
dp[11] = 3 (9+1+1)
dp[12] = 3 (4+4+4)

Result: 3
```

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Mathematical | O(√n) | O(1) | Fastest, requires math knowledge |
| DP | O(n×√n) | O(n) | Standard approach |
| BFS | O(n×√n) | O(n) | Graph-based approach |
| Optimized DP | O(n×√n) | O(n) | Better for multiple queries |

## Edge Cases

1. **Perfect square**: `n = 1, 4, 9, 16, ...` → return 1
2. **Sum of 2 squares**: `n = 2, 5, 10, 13, ...` → return 2
3. **Sum of 3 squares**: `n = 3, 6, 11, 12, ...` → return 3
4. **Sum of 4 squares**: `n = 7, 15, 23, ...` → return 4
5. **Large n**: `n = 10^4` → all solutions handle efficiently

## Common Mistakes

1. **Not reducing by 4**: Missing the optimization step
2. **Wrong modulo check**: Using `n % 8 == 7` incorrectly
3. **Integer overflow**: Not handling large squares correctly
4. **DP initialization**: Forgetting to set `dp[0] = 0`
5. **Square generation**: Not generating all squares up to `n`

## Key Insights

1. **Mathematical approach**: Fastest but requires number theory knowledge
2. **DP approach**: Most intuitive, similar to coin change
3. **BFS approach**: Natural for shortest path problems
4. **Optimization**: Reducing by factors of 4 doesn't change the answer
5. **Upper bound**: Maximum answer is 4 (Lagrange's theorem)

## Optimization Tips

1. **Pre-compute squares**: Generate perfect squares once
2. **Early termination**: In DP, can break early if `dp[i] == 1`
3. **Static DP**: Use static array for multiple queries
4. **Mathematical shortcuts**: Use Legendre's theorem when possible

## Related Problems

- [322. Coin Change](https://leetcode.com/problems/coin-change/) - Similar DP pattern
- [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) - Count combinations
- [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/) - Count ways
- [91. Decode Ways](https://leetcode.com/problems/decode-ways/) - DP with constraints

## Pattern Recognition

This problem demonstrates multiple patterns:

1. **Mathematical Optimization**: Using number theory to optimize
2. **Unbounded Knapsack**: Similar to coin change (unlimited use)
3. **Shortest Path**: BFS finds minimum steps
4. **Dynamic Programming**: Building solution from subproblems

## Real-World Applications

1. **Cryptography**: Number theory applications
2. **Optimization**: Resource allocation problems
3. **Algorithm Design**: Pattern matching in DP problems
4. **Mathematical Research**: Number representation problems

{% endraw %}

