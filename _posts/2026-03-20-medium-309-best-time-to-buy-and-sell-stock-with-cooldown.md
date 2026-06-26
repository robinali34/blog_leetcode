---
layout: post
title: "[Medium] 309. Best Time to Buy and Sell Stock with Cooldown"
date: 2026-03-20
categories: [leetcode, medium, dp]
tags: [leetcode, medium, dp, state-machine, stock]
permalink: /2026/03/20/medium-309-best-time-to-buy-and-sell-stock-with-cooldown/
---
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`. Find the maximum profit with as many transactions as you like, subject to: after you sell, you must **cooldown for one day** before buying again.

## Examples

**Example 1:**

```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: buy→sell→cooldown→buy→sell = (2-1) + (2-0) = 3
```

**Example 2:**

```
Input: prices = [1]
Output: 0
```

## Constraints

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Thinking Process

### State Machine DP

On any day we're in exactly one of three states:

```
        buy
  ┌──────────────┐
  ▼              │
hold ──sell──► rest ──idle──► sold
  │                            │
  └────────keep────────────────┘
              idle
```

- **hold**: we own a stock (either bought today or carried from yesterday)
- **rest**: we just sold (cooldown -- cannot buy tomorrow)
- **sold**: we don't own a stock and are free to buy (either stayed idle or finished cooldown)

### Transitions

$text{hold}[i] = max(text{hold}[i-1],\ text{sold}[i-1] - text{prices}[i])

Keep holding, or buy today (only from `sold` state, not from `rest`).

text{rest}[i] = text{hold}[i-1] + text{prices}[i]

Sell today (transition from `hold` to `rest`).

text{sold}[i] = max(text{sold}[i-1],\ text{rest}[i-1])

Stay idle, or cooldown finished (transition from `rest` to `sold`).

### Base Case

Day 0: `hold = -prices[0]`, `sold = 0`, `rest = 0`

### Answer

\max(\text{sold}, \text{rest}) -- we either have no stock and are free, or we just sold. We never want to end in `hold`.

### Walk-through

```
prices = [1, 2, 3, 0, 2]

Day 0: hold=-1, sold=0, rest=0
Day 1: hold=max(-1, 0-2)=-1, sold=max(0, 0)=0, rest=-1+2=1
Day 2: hold=max(-1, 0-3)=-1, sold=max(0, 1)=1, rest=-1+3=2
Day 3: hold=max(-1, 1-0)=1,  sold=max(1, 2)=2, rest=-1+0=-1
Day 4: hold=max(1, 2-2)=1,   sold=max(2, -1)=2, rest=1+2=3

Answer: max(sold=2, rest=3) = 3 ✓
```

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
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;
        int hold = -prices[0];
        int sold = 0;
        int rest = 0;

        for (int i = 1; i < n; i++) {
            int pre_hold = hold;
            int pre_sold = sold;
            int pre_rest = rest;
            hold = max(pre_hold, pre_sold - prices[i]);
            sold = max(pre_sold, pre_rest);
            rest = pre_hold + prices[i];
        }
        return max(sold, rest);
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** ### State Machine DP

**How the code works:**
- **hold**: we own a stock (either bought today or carried from yesterday)
- **rest**: we just sold (cooldown -- cannot buy tomorrow)
- **sold**: we don't own a stock and are free to buy (either stayed idle or finished cooldown)

**Walkthrough** — input `prices = [1,2,3,0,2]`, expected output `3`:

buy→sell→cooldown→buy→sell = (2-1) + (2-0) = 3
## Why Save `pre_` Values?

All three states depend on the **previous day's** values. If we update `hold` first, it would corrupt the computation of `rest` (which needs the old `hold`). Saving previous values ensures all transitions use day i-1 consistently.

## Common Mistakes

- Allowing buy from `rest` state (violates the cooldown constraint)
- Forgetting to return `max(sold, rest)` -- selling on the last day (`rest`) can be optimal
- Not saving previous-day values before updating (order-dependent bug)

## Key Takeaways

- **Stock problems with constraints** map cleanly to state machine DP
- Three states (`hold`, `sold`, `rest`) capture the cooldown rule naturally
- Space optimization from O(n) array to O(1) variables is straightforward since each state only depends on the previous day

## Stock Problem Family

| Problem | Constraint | States |
|---|---|---|
| 121 Best Time to Buy and Sell Stock | 1 transaction | `hold`, `sold` |
| 122 Best Time II | Unlimited | `hold`, `sold` |
| 123 Best Time III | At most 2 | `hold1`, `sold1`, `hold2`, `sold2` |
| 188 Best Time IV | At most k | `hold[j]`, `sold[j]` for j \in [1,k]$ |
| **309 With Cooldown** | **Unlimited + cooldown** | **`hold`, `sold`, `rest`** |
| 714 With Transaction Fee | Unlimited + fee | `hold`, `sold` |

## Related Problems

- [122. Best Time to Buy and Sell Stock II](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) -- no cooldown version
- [714. Best Time to Buy and Sell Stock with Transaction Fee](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) -- fee instead of cooldown
- [188. Best Time to Buy and Sell Stock IV](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) -- at most k transactions

## References

- [LC 309: Best Time to Buy and Sell Stock with Cooldown on LeetCode](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
- [LeetCode Discuss — LC 309: Best Time to Buy and Sell Stock with Cooldown](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/editorial/) *(may require premium)*

## Template Reference

- [DP](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
