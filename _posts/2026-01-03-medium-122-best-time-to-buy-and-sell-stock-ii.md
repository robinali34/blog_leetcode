---
layout: post
title: "122. Best Time to Buy and Sell Stock II"
date: 2026-01-03 06:00:00 -0700
categories: [leetcode, medium, array, greedy, dynamic-programming]
permalink: /2026/01/03/medium-122-best-time-to-buy-and-sell-stock-ii/
---

# 122. Best Time to Buy and Sell Stock II

## Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it then immediately sell it on the **same day**.

Find and return *the **maximum profit** you can achieve*.

## Examples

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```

**Example 2:**
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```

**Example 3:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
```

## Constraints

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Transaction rules**: What are the transaction rules? (Assumption: Can buy and sell multiple times, but must sell before buying again - can hold at most one share)

2. **Optimization goal**: What are we optimizing for? (Assumption: Maximum total profit from all transactions)

3. **Return value**: What should we return? (Assumption: Integer - maximum profit possible)

4. **Multiple transactions**: Can we make multiple transactions? (Assumption: Yes - can buy and sell as many times as we want)

5. **No transaction**: What if we never buy? (Assumption: Profit is 0 - no transactions made)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Try all possible combinations of buy and sell days. For each possible sequence of transactions (buy, sell, buy, sell, ...), calculate the total profit. This requires exploring all possible transaction sequences, which has exponential complexity. The challenge is determining the optimal sequence of buy/sell decisions.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use dynamic programming: dp[i][holding] = maximum profit up to day i, where holding indicates whether we own stock. For each day, decide to buy, sell, or hold. This requires tracking state (holding or not) and has O(n) time with O(n) space. However, we can optimize further since we only need previous day's state.

**Step 3: Optimized Solution (8 minutes)**

Use greedy approach: capture every price increase. If price[i+1] > price[i], buy on day i and sell on day i+1 (or equivalently, add price[i+1] - price[i] to profit). This works because we can make unlimited transactions, so we should capture every opportunity to profit. This achieves O(n) time with O(1) space. The key insight is that the maximum profit equals the sum of all positive price differences between consecutive days, since we can make a transaction for each price increase.

## Solution Approach

This is a **greedy algorithm** problem. The key insight is that we can capture all positive price differences (gains) by buying and selling on consecutive days whenever the price increases.

### Key Insights:

1. **Greedy Strategy**: Capture every price increase
2. **Local Maximum**: Buy before price increase, sell after
3. **Sum of Gains**: Total profit = sum of all positive day-to-day differences
4. **Optimal**: This greedy approach captures maximum profit

### Algorithm:

1. **Iterate**: Go through prices array
2. **Calculate Difference**: For each day, calculate price difference from previous day
3. **Sum Positive Differences**: Add all positive differences to profit
4. **Return**: Total maximum profit

## Solution

### **Solution: Greedy - Capture All Gains**

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0) return 0;
        int maxProfit = 0, lastPrice = prices[0];
        for(int i = 1; i < (int)prices.size(); i++) {
            maxProfit += max(0, prices[i] - prices[i - 1]);
        }
        return maxProfit;
    }
};
```

### **Algorithm Explanation:**

1. **Edge Case (Line 4)**:
   - If prices array is empty, return 0 (no profit possible)

2. **Initialize (Line 5)**:
   - `maxProfit`: Accumulator for total profit (starts at 0)
   - `lastPrice`: Previous day's price (initialized but not used in this version)

3. **Calculate Profit (Lines 6-8)**:
   - **For each day** starting from index 1:
     - **Calculate difference**: `prices[i] - prices[i - 1]`
     - **Add positive gains**: `max(0, prices[i] - prices[i - 1])`
       - If price increased, add the gain to profit
       - If price decreased or stayed same, add 0
     - **Accumulate**: Add to `maxProfit`

4. **Return (Line 9)**:
   - Return total accumulated profit

### **Example Walkthrough:**

**Example 1: `prices = [7,1,5,3,6,4]`**

```
Initial: maxProfit = 0

i=1: prices[1]=1, prices[0]=7
  Difference: 1 - 7 = -6
  Gain: max(0, -6) = 0
  maxProfit = 0 + 0 = 0

i=2: prices[2]=5, prices[1]=1
  Difference: 5 - 1 = 4
  Gain: max(0, 4) = 4
  maxProfit = 0 + 4 = 4

i=3: prices[3]=3, prices[2]=5
  Difference: 3 - 5 = -2
  Gain: max(0, -2) = 0
  maxProfit = 4 + 0 = 4

i=4: prices[4]=6, prices[3]=3
  Difference: 6 - 3 = 3
  Gain: max(0, 3) = 3
  maxProfit = 4 + 3 = 7

i=5: prices[5]=4, prices[4]=6
  Difference: 4 - 6 = -2
  Gain: max(0, -2) = 0
  maxProfit = 7 + 0 = 7

Result: 7
```

**Visual Representation:**
```
Prices: [7, 1, 5, 3, 6, 4]
         ↓  ↓  ↓  ↓  ↓  ↓
Day:     0  1  2  3  4  5

Gains:
  Day 0→1: 1-7 = -6 (loss, ignore)
  Day 1→2: 5-1 = +4 (gain, capture) ✓
  Day 2→3: 3-5 = -2 (loss, ignore)
  Day 3→4: 6-3 = +3 (gain, capture) ✓
  Day 4→5: 4-6 = -2 (loss, ignore)

Total: 4 + 3 = 7
```

**Example 2: `prices = [1,2,3,4,5]`**

```
Initial: maxProfit = 0

i=1: 2-1 = 1 → maxProfit = 1
i=2: 3-2 = 1 → maxProfit = 2
i=3: 4-3 = 1 → maxProfit = 3
i=4: 5-4 = 1 → maxProfit = 4

Result: 4
```

**Visual Representation:**
```
Prices: [1, 2, 3, 4, 5]
Gains:  +1 +1 +1 +1
Total:  1 + 1 + 1 + 1 = 4
```

**Example 3: `prices = [7,6,4,3,1]`**

```
Initial: maxProfit = 0

i=1: 6-7 = -1 → maxProfit = 0
i=2: 4-6 = -2 → maxProfit = 0
i=3: 3-4 = -1 → maxProfit = 0
i=4: 1-3 = -2 → maxProfit = 0

Result: 0 (no positive gains)
```

## Algorithm Breakdown

### **Why Greedy Works**

The greedy strategy is optimal because:
1. **No Future Information**: We don't need to know future prices
2. **Local Optimal**: Capturing every price increase is always beneficial
3. **No Regret**: If we skip a gain today, we can't capture it later (each day is independent)
4. **Optimal Substructure**: Maximum profit = sum of all positive day-to-day gains

### **Key Insight: Capture All Gains**

Instead of trying to find the best buy/sell pairs, we can:
- **Buy and sell on consecutive days** whenever price increases
- **Sum all positive differences** to get maximum profit
- This is equivalent to buying at local minima and selling at local maxima

**Example:**
```
Prices: [1, 5, 3, 6]

Strategy 1: Buy at 1, sell at 5, buy at 3, sell at 6
  Profit: (5-1) + (6-3) = 4 + 3 = 7

Strategy 2: Buy at 1, sell at 6 (skip intermediate)
  Profit: 6-1 = 5

Strategy 3: Capture all gains (greedy)
  Day 0→1: 5-1 = 4
  Day 1→2: 3-5 = -2 (ignore)
  Day 2→3: 6-3 = 3
  Total: 4 + 3 = 7 ✓
```

### **Mathematical Proof**

For any price sequence, the maximum profit is:
```
maxProfit = Σ max(0, prices[i] - prices[i-1]) for i from 1 to n-1
```

This captures all positive price movements, which is optimal.

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the length of prices array
  - Single pass through the array
  - Constant time operations for each element
- **Space Complexity**: O(1)
  - Only using a few variables
  - No additional data structures

## Key Points

1. **Greedy Strategy**: Capture every price increase
2. **Simple Logic**: Sum all positive day-to-day differences
3. **Optimal**: Greedy approach finds maximum profit
4. **No DP Needed**: Simple greedy is sufficient
5. **Efficient**: O(n) time, O(1) space

## Alternative Approaches

### **Approach 1: Greedy (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Optimal solution, most efficient

### **Approach 2: Dynamic Programming**
- **Time**: O(n)
- **Space**: O(1) or O(n)
- **Use when**: Need to track state (holding/not holding stock)
- **Idea**: `dp[i][0]` = max profit at day i not holding, `dp[i][1]` = holding

### **Approach 3: Peak Valley Approach**
- **Time**: O(n)
- **Space**: O(1)
- **Idea**: Find local minima (valleys) and local maxima (peaks)
- **Equivalent**: Same as greedy, just different perspective

## Edge Cases

1. **Empty array**: `[]` → return 0
2. **Single price**: `[5]` → return 0 (no transaction possible)
3. **All increasing**: `[1,2,3,4,5]` → return 4
4. **All decreasing**: `[5,4,3,2,1]` → return 0
5. **Constant prices**: `[5,5,5,5]` → return 0
6. **Mixed**: `[7,1,5,3,6,4]` → return 7

## Common Mistakes

1. **Wrong logic**: Trying to find single best buy/sell pair
2. **Missing edge case**: Not handling empty array
3. **Wrong index**: Off-by-one errors in loop
4. **Negative profit**: Not using `max(0, ...)` to ignore losses
5. **Complex solution**: Using DP when greedy is sufficient

## Related Problems

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Single transaction
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) - At most 2 transactions
- [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) - At most k transactions
- [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) - With cooldown period
- [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) - With transaction fee

## Comparison with Other Stock Problems

**LC 121 (Single Transaction):**
- Goal: Maximum profit with one buy and one sell
- Approach: Track minimum price and maximum profit
- Complexity: O(n)

**LC 122 (Unlimited Transactions - Current):**
- Goal: Maximum profit with unlimited transactions
- Approach: Sum all positive price differences
- Complexity: O(n)

**LC 123 (At Most 2 Transactions):**
- Goal: Maximum profit with at most 2 transactions
- Approach: DP with state tracking
- Complexity: O(n)

## Tags

`Array`, `Greedy`, `Dynamic Programming`, `Medium`

