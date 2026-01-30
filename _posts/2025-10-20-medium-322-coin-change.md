---
layout: post
title: "322. Coin Change"
date: 2025-10-20 14:30:00 -0700
categories: [leetcode, medium, dynamic-programming, dp, coin-change]
permalink: /2025/10/20/medium-322-coin-change/
---

# 322. Coin Change

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

## Examples

**Example 1:**
```
Input: coins = [1,3,4], amount = 6
Output: 2
Explanation: 6 = 3 + 3
```

**Example 2:**
```
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up just with coins of 2.
```

**Example 3:**
```
Input: coins = [1], amount = 0
Output: 0
```

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Coin usage**: Can we use each coin multiple times? (Assumption: Yes - unlimited supply of each coin denomination)

2. **Optimization goal**: What are we optimizing for? (Assumption: Minimum number of coins needed to make up the amount)

3. **Impossible case**: What if amount cannot be made? (Assumption: Return -1 - no combination of coins can make the amount)

4. **Zero amount**: What if amount is 0? (Assumption: Return 0 - no coins needed)

5. **Return value**: What should we return? (Assumption: Integer - minimum number of coins, or -1 if impossible)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to find minimum coins. Let me try all combinations recursively."

**Naive Solution**: Recursively explore all possible coin combinations. For each amount, try every coin and recursively solve for the remaining amount.

**Complexity**: O(S^n) time, O(S) space where S = amount, n = number of coins

**Issues**:
- Exponential time complexity - explores all combinations
- Recomputes same subproblems repeatedly (e.g., amount-1 solved multiple times)
- Will timeout for large amounts
- No optimization - pure brute-force exploration

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I'm solving the same subproblems multiple times. Memoization can help avoid recomputation."

**Improved Solution**: Add memoization table to cache results of subproblems. When solving for an amount, check if already computed before recursing.

**Complexity**: O(S × n) time, O(S) space

**Improvements**:
- O(S × n) time complexity - each amount computed once
- Avoids recomputation through memoization
- Still uses recursion stack space O(S)
- Significant improvement over brute-force

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "Bottom-up DP eliminates recursion overhead and is more intuitive. Build solution from base case upward."

**Best Solution**: Use bottom-up dynamic programming. Initialize dp[0] = 0, then for each amount from 1 to target, try all coins and take minimum.

**Complexity**: O(S × n) time, O(S) space

**Key Realizations**:
1. Bottom-up DP is cleaner and avoids stack overflow risk
2. Use `amount + 1` as impossible value (greater than any valid solution)
3. Build solution from smaller amounts to larger amounts
4. Optimal substructure: `dp[i] = min(dp[i - coin] + 1)` for all valid coins
5. More intuitive than top-down - can visualize the table filling process

## Solution Structure Breakdown

### Evolution from Naive to Optimized

**Naive Approach** (Recursive):
- **Structure**: Try all coin combinations recursively
- **Complexity**: O(S^n) time, O(S) space (stack)
- **Limitation**: Exponential time, recomputes subproblems

**Semi-Optimized Approach** (Top-Down DP):
- **Structure**: Recursive + memoization cache
- **Complexity**: O(S × n) time, O(S) space
- **Improvement**: Eliminates recomputation, still uses recursion

**Optimized Approach** (Bottom-Up DP):
- **Structure**: Iterative DP building from base case
- **Complexity**: O(S × n) time, O(S) space
- **Enhancement**: No recursion overhead, clearer logic

### Code Structure Comparison

| Approach | Pattern | Time | Space | Clarity |
|----------|---------|------|-------|---------|
| **Naive** | Recursive exploration | O(S^n) | O(S) | Low |
| **Semi-Opt** | Memoized recursion | O(S×n) | O(S) | Medium |
| **Optimized** | Bottom-up DP | O(S×n) | O(S) | High |

## Solution Approach

This is a classic **Dynamic Programming** problem that asks for the minimum number of coins needed to make a given amount. Since we can use each coin unlimited times, this is an **unbounded knapsack** problem.

### Key Insights:

1. **Optimal substructure**: The minimum coins for amount `i` can be computed from smaller amounts
2. **Overlapping subproblems**: Same subproblems are solved multiple times
3. **Unbounded knapsack**: Each coin can be used unlimited times
4. **Bottom-up DP**: Build solution from smaller amounts to larger amounts

### Algorithm:

1. **DP array**: `dp[i]` represents minimum coins needed for amount `i`
2. **Base case**: `dp[0] = 0` (0 coins needed for amount 0)
3. **Transition**: For each amount `i`, try each coin and take minimum
4. **Result**: Return `dp[amount]` if it's valid, otherwise `-1`

## Solution

### **Solution 1: Brute-Force Recursive Approach**

**Time Complexity:** O(S^n) where S = amount, n = number of coins  
**Space Complexity:** O(S) for recursion stack

Recursively explore all possible coin combinations.

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        if (amount < 0) return -1;
        
        int minCoins = INT_MAX;
        for (int coin : coins) {
            int result = coinChange(coins, amount - coin);
            if (result != -1) {
                minCoins = min(minCoins, result + 1);
            }
        }
        
        return minCoins == INT_MAX ? -1 : minCoins;
    }
};
```

**Note**: This approach will timeout for large amounts due to exponential time complexity.

### **Solution 2: Top-Down DP with Memoization**

**Time Complexity:** O(S × n)  
**Space Complexity:** O(S) for memoization and recursion stack

Add memoization to cache results and avoid recomputation.

```cpp
class Solution {
private:
    vector<int> memo;
    
    int dfs(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        if (amount < 0) return -1;
        if (memo[amount] != -1) return memo[amount];
        
        int minCoins = INT_MAX;
        for (int coin : coins) {
            int result = dfs(coins, amount - coin);
            if (result != -1) {
                minCoins = min(minCoins, result + 1);
            }
        }
        
        memo[amount] = (minCoins == INT_MAX) ? -1 : minCoins;
        return memo[amount];
    }
    
public:
    int coinChange(vector<int>& coins, int amount) {
        memo.assign(amount + 1, -1);
        return dfs(coins, amount);
    }
};
```

**Note**: Better than brute-force but still uses recursion stack space.

### **Solution 3: Dynamic Programming (Bottom-Up) - Recommended**

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;
        for(int i = 1; i <= amount; i++) {
            for(int j = 0; j < (int)coins.size(); j++) {
                if(coins[j] <= i) {
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1: dp[amount];
    }
};
```

### **Algorithm Explanation:**

1. **Initialize DP array**: `dp[i] = amount + 1` (impossible value for all amounts)
2. **Base case**: `dp[0] = 0` (0 coins needed for amount 0)
3. **Fill DP array**: For each amount `i` from 1 to `amount`:
   - Try each coin `coins[j]`
   - If `coins[j] <= i`, update `dp[i] = min(dp[i], dp[i - coins[j]] + 1)`
4. **Return result**: If `dp[amount] > amount`, return `-1` (impossible), otherwise return `dp[amount]`

### **Example Walkthrough:**

**For `coins = [1,3,4], amount = 6`:**

```
Initial: dp = [0, 7, 7, 7, 7, 7, 7]

i=1: Try coins [1,3,4]
- coin=1: dp[1] = min(7, dp[0] + 1) = min(7, 1) = 1
- coin=3: 3 > 1, skip
- coin=4: 4 > 1, skip
dp = [0, 1, 7, 7, 7, 7, 7]

i=2: Try coins [1,3,4]
- coin=1: dp[2] = min(7, dp[1] + 1) = min(7, 2) = 2
- coin=3: 3 > 2, skip
- coin=4: 4 > 2, skip
dp = [0, 1, 2, 7, 7, 7, 7]

i=3: Try coins [1,3,4]
- coin=1: dp[3] = min(7, dp[2] + 1) = min(7, 3) = 3
- coin=3: dp[3] = min(3, dp[0] + 1) = min(3, 1) = 1
- coin=4: 4 > 3, skip
dp = [0, 1, 2, 1, 7, 7, 7]

i=4: Try coins [1,3,4]
- coin=1: dp[4] = min(7, dp[3] + 1) = min(7, 2) = 2
- coin=3: dp[4] = min(2, dp[1] + 1) = min(2, 2) = 2
- coin=4: dp[4] = min(2, dp[0] + 1) = min(2, 1) = 1
dp = [0, 1, 2, 1, 1, 7, 7]

i=5: Try coins [1,3,4]
- coin=1: dp[5] = min(7, dp[4] + 1) = min(7, 2) = 2
- coin=3: dp[5] = min(2, dp[2] + 1) = min(2, 3) = 2
- coin=4: dp[5] = min(2, dp[1] + 1) = min(2, 2) = 2
dp = [0, 1, 2, 1, 1, 2, 7]

i=6: Try coins [1,3,4]
- coin=1: dp[6] = min(7, dp[5] + 1) = min(7, 3) = 3
- coin=3: dp[6] = min(3, dp[3] + 1) = min(3, 2) = 2
- coin=4: dp[6] = min(2, dp[2] + 1) = min(2, 3) = 2
dp = [0, 1, 2, 1, 1, 2, 2]

Result: dp[6] = 2 (coins: 3 + 3)
```

## Complexity Analysis

### **Time Complexity:** O(amount × coins.length)
- **Outer loop**: O(amount) - iterate through all amounts
- **Inner loop**: O(coins.length) - try each coin for each amount
- **Total**: O(amount × coins.length)

### **Space Complexity:** O(amount)
- **DP array**: O(amount) - stores minimum coins for each amount
- **No additional space**: Only the DP array is used

## Key Points

1. **Dynamic Programming**: Bottom-up approach building from smaller amounts
2. **Unbounded knapsack**: Each coin can be used unlimited times
3. **Optimal substructure**: Solution for amount `i` depends on smaller amounts
4. **Impossible detection**: Use `amount + 1` as impossible value
5. **Efficient**: Single pass through all amounts and coins

## Alternative Approaches

### **Top-Down DP (Memoization)**
```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> memo(amount + 1, -1);
        int result = dfs(coins, amount, memo);
        return result == INT_MAX ? -1 : result;
    }
    
private:
    int dfs(vector<int>& coins, int amount, vector<int>& memo) {
        if (amount == 0) return 0;
        if (amount < 0) return INT_MAX;
        if (memo[amount] != -1) return memo[amount];
        
        int minCoins = INT_MAX;
        for (int coin : coins) {
            int result = dfs(coins, amount - coin, memo);
            if (result != INT_MAX) {
                minCoins = min(minCoins, result + 1);
            }
        }
        
        memo[amount] = minCoins;
        return minCoins;
    }
};
```

## Related Problems

- [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/) - Count number of ways
- [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/) - Similar DP approach
- [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) - Count combinations
- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) - Subset sum problem

## Tags

`Dynamic Programming`, `DP`, `Coin Change`, `Unbounded Knapsack`, `Medium`
