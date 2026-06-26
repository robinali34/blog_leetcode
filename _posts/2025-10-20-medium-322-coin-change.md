---
layout: post
title: "[Medium] 322. Coin Change"
date: 2025-10-20 14:30:00 -0700
categories: [leetcode, medium, dynamic-programming, dp, coin-change]
permalink: /2025/10/20/medium-322-coin-change/
---
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

## Thinking Process

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

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
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

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

### Complexity
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [518. Coin Change 2](https://www.leetcode.com/problems/coin-change-2/) - Count number of ways
- [279. Perfect Squares](https://www.leetcode.com/problems/perfect-squares/) - Similar DP approach
- [377. Combination Sum IV](https://www.leetcode.com/problems/combination-sum-iv/) - Count combinations
- [416. Partition Equal Subset Sum](https://www.leetcode.com/problems/partition-equal-subset-sum/) - Subset sum problem

## Tags

`Dynamic Programming`, `DP`, `Coin Change`, `Unbounded Knapsack`, `Medium`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 322: Coin Change on LeetCode](https://www.leetcode.com/problems/coin-change/)
- [LeetCode Discuss — LC 322: Coin Change](https://www.leetcode.com/problems/coin-change/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/coin-change/editorial/) *(may require premium)*

## Template Reference

- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
