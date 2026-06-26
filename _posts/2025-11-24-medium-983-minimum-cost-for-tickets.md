---
layout: post
title: "[Medium] 983. Minimum Cost For Tickets"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp dynamic-programming problem-solving
permalink: /posts/2025-11-24-medium-983-minimum-cost-for-tickets/
tags: [leetcode, medium, dynamic-programming, dp, optimization]
---
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array `days`. Each day is an integer from `1` to `365`.

Train tickets are sold in **three different ways**:

- a **1-day** pass is sold for `costs[0]` dollars,
- a **7-day** pass is sold for `costs[1]` dollars, and
- a **30-day** pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel.

- For example, if we get a **7-day** pass on day `2`, then we can travel for `7` days: `2`, `3`, `4`, `5`, `6`, `7`, and `8`.

Return *the minimum number of dollars you need to travel every day in the given list of days*.

## Examples

**Example 1:**
```
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 4, you bought a 7-day pass for costs[1] = $7, which covered days 4, 5, 6, 7, and 8.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
```

**Example 2:**
```
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
```

## Constraints

- `1 <= days.length <= 365`
- `1 <= days[i] <= 365`
- `days` is in strictly increasing order.
- `costs.length == 3`
- `1 <= costs[i] <= 1000`

## Thinking Process

1. **DP State**: Track minimum cost up to each day

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

**Time Complexity:** O(n) where n is the last travel day (at most 365)  
**Space Complexity:** O(n)

The key insight is to use dynamic programming to track the minimum cost to travel up to each day. For each day, we consider three options: buying a 1-day, 7-day, or 30-day pass.

### Solution: Bottom-Up DP (Optimized)

```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int lastDay = days.back();
        vector<int> dp(lastDay + 1, 0);
        unordered_set<int> travelDays(days.begin(), days.end());
        
        for (int i = 1; i <= lastDay; ++i) {
            if (travelDays.find(i) == travelDays.end()) {
                // Not a travel day - cost stays the same as previous day
                dp[i] = dp[i - 1];
            } else {
                // Travel day - choose minimum cost among three options
                dp[i] = min({
                    dp[i - 1] + costs[0],           // Buy 1-day pass
                    dp[max(0, i - 7)] + costs[1],   // Buy 7-day pass
                    dp[max(0, i - 30)] + costs[2]   // Buy 30-day pass
                });
            }
        }
        
        return dp[lastDay];
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **DP State**: Track minimum cost up to each day

**How the code works:**
1. **DP State**: Track minimum cost up to each day
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `days = [1,4,6,7,8,20], costs = [2,7,15]`, expected output `11`:

For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 4, you bought a 7-day pass for costs[1] = $7, which covered days 4, 5, 6, 7, and 8.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Bottom-Up DP** | O(n) | O(n) | Simple, intuitive | Processes all days |
| **Top-Down DP** | O(m) | O(m) | Only travel days | More complex |

Where `n` = last travel day (≤365), `m` = number of travel days
## Algorithm Breakdown

### Initialization

```cpp
int lastDay = days.back();
vector<int> dp(lastDay + 1, 0);
unordered_set<int> travelDays(days.begin(), days.end());
```

**Why:**
- `lastDay`: Only need to compute up to the last travel day
- `dp`: Array to store minimum cost for each day
- `travelDays`: Set for O(1) lookup of travel days

### Main DP Loop

```cpp
for (int i = 1; i <= lastDay; ++i) {
    if (travelDays.find(i) == travelDays.end()) {
        dp[i] = dp[i - 1];
    } else {
        dp[i] = min({
            dp[i - 1] + costs[0],
            dp[max(0, i - 7)] + costs[1],
            dp[max(0, i - 30)] + costs[2]
        });
    }
}
```

**Why:**
- **Non-travel day**: No cost, so cost equals previous day
- **Travel day**: Choose cheapest option among three passes
- **max(0, i-duration)**: Prevents negative indices

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Bottom-Up DP** | O(n) | O(n) | Simple, intuitive | Processes all days |
| **Top-Down DP** | O(m) | O(m) | Only travel days | More complex |

Where `n` = last travel day (≤365), `m` = number of travel days

## Implementation Details

### Why Use `max(0, i - duration)`?

**Example:** On day 5, buying a 7-day pass:
- Pass covers days 5-11
- Cost = `dp[5-7] + costs[1]` = `dp[-2] + costs[1]` ❌
- Use `max(0, 5-7)` = `dp[0] + costs[1]` ✓

**Why:** Days before day 1 don't exist, so use base case `dp[0] = 0`.

### Pass Coverage

**7-day pass bought on day `i`:**
- Covers days: `i, i+1, ..., i+6`
- Expires after day `i+6`
- Next cost starts from day `i+7`

**30-day pass bought on day `i`:**
- Covers days: `i, i+1, ..., i+29`
- Expires after day `i+29`
- Next cost starts from day `i+30`

### Why Set for Travel Days?

```cpp
unordered_set<int> travelDays(days.begin(), days.end());
```

**Why:** O(1) lookup instead of O(m) linear search in `days` array.

## Common Mistakes

1. **Single travel day**: Buy 1-day pass
2. **Consecutive travel days**: 7-day or 30-day pass might be cheaper
3. **Sparse travel days**: 1-day passes might be optimal
4. **Dense travel days**: 30-day pass likely optimal
5. **Early days**: `max(0, i-duration)` handles days < 7 or < 30

1. **Forgetting non-travel days**: Must set `dp[i] = dp[i-1]` for non-travel days
2. **Wrong pass coverage**: 7-day pass covers 7 days, not 6
3. **Negative indices**: Must use `max(0, i-duration)`
4. **Not considering all options**: Must compare all three pass types
5. **Base case**: `dp[0] = 0` (no cost before day 1)

## Optimization Tips

1. **Use set for O(1) lookup**: Faster than linear search
2. **Only iterate to last_day**: Don't need to go beyond
3. **Bottom-up DP**: Avoids recursion overhead
4. **Early termination**: Not applicable (need all days)

## Related Problems

- [322. Coin Change](https://www.leetcode.com/problems/coin-change/) - Similar DP optimization
- [518. Coin Change II](https://www.leetcode.com/problems/coin-change-ii/) - Counting ways
- [279. Perfect Squares](https://www.leetcode.com/problems/perfect-squares/) - DP with choices
- [377. Combination Sum IV](https://www.leetcode.com/problems/combination-sum-iv/) - DP with multiple choices

## Real-World Applications

1. **Subscription Planning**: Choosing optimal subscription plans
2. **Resource Allocation**: Minimizing costs for periodic needs
3. **Scheduling**: Optimizing ticket purchases for events
4. **Budget Planning**: Finding cheapest way to cover required periods

## Pattern Recognition

This problem demonstrates the **"Minimum Cost with Choices"** DP pattern:

```
1. Define state: dp[i] = minimum cost up to day i
2. For each state, consider all choices (1-day, 7-day, 30-day)
3. Take minimum among all choices
4. Handle non-travel days separately (no cost)
```

Similar problems:
- Coin change problems
- Knapsack variants
- Interval covering problems

## Why Bottom-Up DP Works Best

**Advantages:**
- Simple and intuitive
- No recursion overhead
- Easy to understand and debug
- Efficient for this problem size (max 365 days)

**Top-Down Alternative:**
- More efficient for sparse schedules
- Only processes travel days
- But more complex with `upper_bound`

## Step-by-Step Trace: `days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]`

```
Travel days: {1-10, 30, 31}
Last day: 31

Key decisions:
Day 1: Buy 30-day pass ($15) - covers days 1-30
  - Cheaper than buying 10 individual 1-day passes ($20)
  - Cheaper than buying multiple 7-day passes

Day 31: Buy 1-day pass ($2) - covers day 31

DP progression:
dp[1] = min(2, 7, 15) = 2 (but we'll see 30-day is better)
...
dp[30] = 15 (30-day pass covers all days 1-30)
dp[31] = min(15+2, 15+7, 15+15) = 17

Actually, buying 30-day pass on day 1 covers days 1-30,
so dp[30] = 15, and dp[31] = 15 + 2 = 17
```

## Mathematical Insight

**Optimal Substructure:**
- To find minimum cost for days 1..i, we need minimum cost for days 1..(i-1), 1..(i-7), or 1..(i-30)
- Each subproblem is independent and optimal

**Greedy Doesn't Work:**
- Always buying cheapest pass per day doesn't work
- Example: 7-day pass might be cheaper than 7 individual 1-day passes
- Need to consider future days

## Why This Solution is Optimized

1. **Time Complexity**: O(n) where n ≤ 365 (linear)
2. **Space Complexity**: O(n) for DP array
3. **Lookup Efficiency**: O(1) with unordered_set
4. **Code Clarity**: Simple, readable bottom-up DP
5. **No Redundancy**: Processes each day exactly once

## Key Takeaways

1. **DP State**: Track minimum cost up to each day
2. **Non-Travel Days**: Cost doesn't increase (no ticket needed)
3. **Travel Days**: Choose minimum among three pass options
4. **Pass Coverage**: 7-day pass covers 7 consecutive days, 30-day covers 30
5. **Boundary Handling**: Use `max(0, i-duration)` to handle early days

## References

- [LC 983: Minimum Cost For Tickets on LeetCode](https://www.leetcode.com/problems/minimum-cost-for-tickets/)
- [LeetCode Discuss — LC 983: Minimum Cost For Tickets](https://www.leetcode.com/problems/minimum-cost-for-tickets/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-cost-for-tickets/editorial/) *(may require premium)*

## Template Reference

- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
