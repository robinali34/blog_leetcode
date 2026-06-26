---
layout: post
title: "[Medium] 198. House Robber"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp dynamic-programming dp problem-solving
permalink: /posts/2025-11-18-medium-198-house-robber/
tags: [leetcode, medium, dynamic-programming, dp, array, optimization]
---
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Thinking Process

1. **DP State Definition**: `dp[i]` represents the maximum money robbed up to house `i-1` (1-indexed)
- `dp[i-1] + nums[i]`: Rob current house (can't rob previous)
- `dp[i]`: Skip current house (keep previous maximum)
- `dp[0] = 0` (no houses)

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
**Space Complexity:** O(n) - DP array (can be optimized to O(1))

This is a classic dynamic programming problem. The key insight is that for each house, we have two choices:
1. **Rob it**: Add its value to the maximum from two houses ago
2. **Skip it**: Take the maximum from the previous house

### Solution: DP Array Approach

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() <= 0) return 0;
        if(nums.size() == 1) return nums[0];
        
        vector<int> dp(nums.size() + 1);
        dp[0] = 0;
        dp[1] = nums[0];
        
        for(int i = 1; i < (int)nums.size(); i++) {
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i]);
        } 
        
        return dp[nums.size()];
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **DP State Definition**: `dp[i]` represents the maximum money robbed up to house `i-1` (1-indexed)

**How the code works:**
1. **DP State Definition**: `dp[i]` represents the maximum money robbed up to house `i-1` (1-indexed)
- `dp[i-1] + nums[i]`: Rob current house (can't rob previous)
- `dp[i]`: Skip current house (keep previous maximum)
- `dp[0] = 0` (no houses)
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?

**Walkthrough** — input `nums = [1,2,3,1]`, expected output `4`:

Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DP Array (1-indexed)** | O(n) | O(n) | Clear indexing, easy to understand | O(n) space |
| **Space-Optimized** | O(n) | O(1) | Optimal space usage | Can't trace path |
| **DP Array (0-indexed)** | O(n) | O(n) | Standard DP pattern | Requires base case handling |
## Algorithm Breakdown

```cpp
int rob(vector<int>& nums) {
    // Edge cases
    if(nums.size() <= 0) return 0;
    if(nums.size() == 1) return nums[0];
    
    // DP array: dp[i] = max money up to house i-1
    vector<int> dp(nums.size() + 1);
    dp[0] = 0;        // No houses
    dp[1] = nums[0];  // Only first house
    
    // For each house starting from index 1
    for(int i = 1; i < (int)nums.size(); i++) {
        // Choose: rob current house OR skip it
        dp[i + 1] = max(
            dp[i - 1] + nums[i],  // Rob current (skip previous)
            dp[i]                  // Skip current (keep previous max)
        );
    }
    
    return dp[nums.size()];  // Maximum for all houses
}
```

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DP Array (1-indexed)** | O(n) | O(n) | Clear indexing, easy to understand | O(n) space |
| **Space-Optimized** | O(n) | O(1) | Optimal space usage | Can't trace path |
| **DP Array (0-indexed)** | O(n) | O(n) | Standard DP pattern | Requires base case handling |

## Recurrence Relation Explanation

The core recurrence relation is:

```
dp[i+1] = max(dp[i-1] + nums[i], dp[i])
```

**Why this works:**
- **`dp[i-1] + nums[i]`**: If we rob house `i`, we can't rob house `i-1`, so we take the maximum from `i-2` (stored in `dp[i-1]`) and add current house value
- **`dp[i]`**: If we skip house `i`, we keep the maximum from all previous houses up to `i-1`

This ensures we never rob two adjacent houses while maximizing the total amount.

## Implementation Details

### 1-Indexed vs 0-Indexed

**1-Indexed (Your Solution):**
```cpp
dp[0] = 0;           // No houses
dp[1] = nums[0];     // First house
dp[i+1] = max(...);  // Current house at index i
```

**0-Indexed (Standard):**
```cpp
dp[0] = nums[0];     // First house
dp[1] = max(nums[0], nums[1]);  // First two houses
dp[i] = max(...);    // Current house at index i
```

Both approaches are correct; 1-indexed makes base cases simpler.

### Type Casting

```cpp
for(int i = 1; i < (int)nums.size(); i++)
```

The `(int)` cast prevents comparison warnings between `int` and `size_t`. Alternatively:
```cpp
for(size_t i = 1; i < nums.size(); i++)
```

## Common Mistakes

1. **Empty array**: `nums = []` → return `0`
2. **Single house**: `nums = [5]` → return `5`
3. **Two houses**: `nums = [2,1]` → return `max(2,1) = 2`
4. **All zeros**: `nums = [0,0,0]` → return `0`
5. **Alternating pattern**: `nums = [1,2,1,2]` → return `max(1+1, 2+2) = 4`

1. **Forgetting edge cases**: Empty array or single element
2. **Wrong recurrence**: Using `dp[i-2]` instead of `dp[i-1]` for 1-indexed
3. **Index out of bounds**: Not handling base cases properly
4. **Wrong return value**: Returning `dp[nums.size()-1]` instead of `dp[nums.size()]` for 1-indexed
5. **Not considering skip option**: Only considering robbing current house

## Optimization Tips

1. **Space Optimization**: Use two variables instead of array for O(1) space
2. **Early Termination**: Can add checks for special cases
3. **Memoization**: For recursive approach, use memoization to avoid recomputation
4. **Bottom-Up DP**: Preferred over top-down for better cache performance

## Related Problems

- [213. House Robber II](https://www.leetcode.com/problems/house-robber-ii/) - Houses arranged in a circle
- [337. House Robber III](https://www.leetcode.com/problems/house-robber-iii/) - Binary tree structure
- [740. Delete and Earn](https://www.leetcode.com/problems/delete-and-earn/) - Similar DP pattern
- [1980. Find Unique Binary String](https://www.leetcode.com/problems/find-unique-binary-string/) - Different problem but similar constraint pattern

## Real-World Applications

1. **Resource Allocation**: Maximizing profit with constraints
2. **Scheduling**: Selecting non-overlapping intervals with maximum value
3. **Network Optimization**: Routing with constraints
4. **Game Theory**: Optimal strategy selection
5. **Financial Planning**: Investment decisions with restrictions

## Pattern Recognition

This problem follows the **"Pick or Skip"** DP pattern:

```
For each element:
  Option 1: Pick it (with constraints)
  Option 2: Skip it
  
Choose the option that maximizes/minimizes the objective
```

Similar problems:
- Maximum Subarray (Kadane's algorithm)
- Climbing Stairs
- Coin Change
- Knapsack problems

---

*This problem is a fundamental introduction to dynamic programming, teaching the "pick or skip" decision pattern that appears in many optimization problems.*

## Key Takeaways

1. **DP State Definition**: `dp[i]` represents the maximum money robbed up to house `i-1` (1-indexed)
2. **Recurrence Relation**: `dp[i+1] = max(dp[i-1] + nums[i], dp[i])`
   - `dp[i-1] + nums[i]`: Rob current house (can't rob previous)
   - `dp[i]`: Skip current house (keep previous maximum)
3. **Base Cases**: 
   - `dp[0] = 0` (no houses)
   - `dp[1] = nums[0]` (only first house)
4. **1-Indexed DP Array**: Using `dp[i+1]` makes indexing cleaner and avoids edge cases

## References

- [LC 198: House Robber on LeetCode](https://www.leetcode.com/problems/house-robber/)
- [LeetCode Discuss — LC 198: House Robber](https://www.leetcode.com/problems/house-robber/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/house-robber/editorial/) *(may require premium)*

## Template Reference

- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
