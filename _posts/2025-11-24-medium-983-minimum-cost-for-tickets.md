---
layout: post
title: "[Medium] 983. Minimum Cost For Tickets"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp dynamic-programming problem-solving
permalink: /posts/2025-11-24-medium-983-minimum-cost-for-tickets/
tags: [leetcode, medium, dynamic-programming, dp, optimization]
---

# [Medium] 983. Minimum Cost For Tickets

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Ticket types**: What ticket types are available? (Assumption: 1-day pass (costs[0]), 7-day pass (costs[1]), 30-day pass (costs[2]))

2. **Travel days**: What are travel days? (Assumption: Array of days when we need to travel - days[i] is the day number)

3. **Optimization goal**: What are we optimizing for? (Assumption: Minimum cost to cover all travel days)

4. **Return value**: What should we return? (Assumption: Integer - minimum cost to cover all travel days)

5. **Ticket validity**: How long are tickets valid? (Assumption: 1-day pass covers 1 day, 7-day pass covers 7 consecutive days, 30-day pass covers 30 consecutive days)

## Solution: Dynamic Programming

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

## How the Algorithm Works

### Key Insight: DP State Definition

**DP State:** `dp[i]` = minimum cost to travel up to day `i`

**Transition:**
- If day `i` is **not** a travel day: `dp[i] = dp[i-1]` (no cost)
- If day `i` **is** a travel day: choose minimum of:
  - Buy 1-day pass: `dp[i-1] + costs[0]`
  - Buy 7-day pass: `dp[i-7] + costs[1]` (covers days i-6 to i)
  - Buy 30-day pass: `dp[i-30] + costs[2]` (covers days i-29 to i)

### Step-by-Step Example: `days = [1,4,6,7,8,20], costs = [2,7,15]`

```
Travel days: {1, 4, 6, 7, 8, 20}
Last day: 20

Day-by-day DP:
Day 0: dp[0] = 0 (base case)

Day 1: Travel day
  - Option 1: dp[0] + costs[0] = 0 + 2 = 2
  - Option 2: dp[max(0,1-7)] + costs[1] = dp[0] + 7 = 7
  - Option 3: dp[max(0,1-30)] + costs[2] = dp[0] + 15 = 15
  dp[1] = min(2, 7, 15) = 2

Day 2: Not a travel day
  dp[2] = dp[1] = 2

Day 3: Not a travel day
  dp[3] = dp[2] = 2

Day 4: Travel day
  - Option 1: dp[3] + costs[0] = 2 + 2 = 4
  - Option 2: dp[max(0,4-7)] + costs[1] = dp[0] + 7 = 7
  - Option 3: dp[max(0,4-30)] + costs[2] = dp[0] + 15 = 15
  dp[4] = min(4, 7, 15) = 4

Day 5: Not a travel day
  dp[5] = dp[4] = 4

Day 6: Travel day
  - Option 1: dp[5] + costs[0] = 4 + 2 = 6
  - Option 2: dp[max(0,6-7)] + costs[1] = dp[0] + 7 = 7
  - Option 3: dp[max(0,6-30)] + costs[2] = dp[0] + 15 = 15
  dp[6] = min(6, 7, 15) = 6

Day 7: Travel day
  - Option 1: dp[6] + costs[0] = 6 + 2 = 8
  - Option 2: dp[max(0,7-7)] + costs[1] = dp[0] + 7 = 7
  - Option 3: dp[max(0,7-30)] + costs[2] = dp[0] + 15 = 15
  dp[7] = min(8, 7, 15) = 7

Day 8: Travel day
  - Option 1: dp[7] + costs[0] = 7 + 2 = 9
  - Option 2: dp[max(0,8-7)] + costs[1] = dp[1] + 7 = 2 + 7 = 9
  - Option 3: dp[max(0,8-30)] + costs[2] = dp[0] + 15 = 15
  dp[8] = min(9, 9, 15) = 9

Days 9-19: Not travel days
  dp[9] = dp[10] = ... = dp[19] = 9

Day 20: Travel day
  - Option 1: dp[19] + costs[0] = 9 + 2 = 11
  - Option 2: dp[max(0,20-7)] + costs[1] = dp[13] + 7 = 9 + 7 = 16
  - Option 3: dp[max(0,20-30)] + costs[2] = dp[0] + 15 = 15
  dp[20] = min(11, 16, 15) = 11

Final answer: dp[20] = 11
```

**Visual Representation:**
```
Days:    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
Travel:      ✓        ✓     ✓  ✓  ✓
DP:      0  2  2  2  4  4  6  7  9  9  9  9  9  9  9  9  9  9  9  9 11

Optimal strategy:
- Day 1: Buy 1-day pass ($2)
- Day 4: Buy 7-day pass ($7) - covers days 4-10
- Day 20: Buy 1-day pass ($2)
Total: $11
```

## Key Insights

1. **DP State**: Track minimum cost up to each day
2. **Non-Travel Days**: Cost doesn't increase (no ticket needed)
3. **Travel Days**: Choose minimum among three pass options
4. **Pass Coverage**: 7-day pass covers 7 consecutive days, 30-day covers 30
5. **Boundary Handling**: Use `max(0, i-duration)` to handle early days

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

## Edge Cases

1. **Single travel day**: Buy 1-day pass
2. **Consecutive travel days**: 7-day or 30-day pass might be cheaper
3. **Sparse travel days**: 1-day passes might be optimal
4. **Dense travel days**: 30-day pass likely optimal
5. **Early days**: `max(0, i-duration)` handles days < 7 or < 30

## Alternative Approaches

### Approach 2: Top-Down DP with Memoization

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
private:
    vector<int> days, costs, memo;
    int durations[3] = {1, 7, 30};
    
    int dp(int i) {
        if (i >= days.size()) return 0;
        if (memo[i] != -1) return memo[i];
        
        memo[i] = INT_MAX;
        
        for (int k = 0; k < 3; k++) {
            // Find first day after current pass expires
            int j = upper_bound(days.begin(), days.end(), 
                               days[i] + durations[k] - 1) - days.begin();
            memo[i] = min(memo[i], dp(j) + costs[k]);
        }
        
        return memo[i];
    }
    
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        this->days = days;
        this->costs = costs;
        memo.assign(days.size(), -1);
        return dp(0);
    }
};
```

**Pros:**
- Only processes travel days (more efficient for sparse schedules)
- Natural recursive structure

**Cons:**
- More complex with `upper_bound`
- Recursion overhead

### Approach 3: Day-by-Day DP (Current Solution)

**Pros:**
- Simple and intuitive
- Easy to understand
- No recursion overhead
- O(1) lookup with set

**Cons:**
- Processes all days up to last_day (but max 365 days)

## Complexity Analysis

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

- [322. Coin Change](https://leetcode.com/problems/coin-change/) - Similar DP optimization
- [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/) - Counting ways
- [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/) - DP with choices
- [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) - DP with multiple choices

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

---

*This problem demonstrates how to use dynamic programming to find the minimum cost when multiple choices are available, with careful handling of non-travel days and pass coverage periods.*

