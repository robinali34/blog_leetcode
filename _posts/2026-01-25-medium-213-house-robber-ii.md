---
layout: post
title: "[Medium] 213. House Robber II"
date: 2026-01-25 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming]
permalink: /2026/01/25/medium-213-house-robber-ii/
tags: [leetcode, medium, array, dynamic-programming, dp, circular-array]
---
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. **All houses at this place are arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

## Examples

**Example 1:**

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent.
```

**Example 2:**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 3:**

```
Input: nums = [1,2,3]
Output: 3
Explanation: Rob house 2 (money = 2) or house 3 (money = 3).
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Thinking Process

1. **Circular Constraint**: First and last houses are adjacent, so we can't rob both
- Exclude last house: `[0..N-2]`
- Exclude first house: `[1..N-1]`

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

```cpp
class Solution {
/*
Cycle: rtn max(robLinear(0.. N - 2), robLinear(1,.. N - 1))
dp[i] = max(dp[i-2] + nums[i], dp[i - 1])
*/
public:
    int rob(vector<int>& nums) {
        const int N = nums.size();
        if(N == 1) return nums[0];
        return max(
            rob(nums, 0, N - 2),
            rob(nums, 1, N - 1)
        );
    }
private:
    int rob(vector<int>& nums, int l, int r) {
        int prev2 = 0, prev1 = 0;
        for(int i = l; i <= r; i++) {
            int curr = max(prev2 + nums[i], prev1);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **Circular Constraint**: First and last houses are adjacent, so we can't rob both

**How the code works:**
1. **Circular Constraint**: First and last houses are adjacent, so we can't rob both
- Exclude last house: `[0..N-2]`
- Exclude first house: `[1..N-1]`
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `nums = [2,3,2]`, expected output `3`:

You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent.
## Common Mistakes

1. **Single house**: `nums = [5]` → return `5`
2. **Two houses**: `nums = [2,3]` → return `max(2,3) = 3`
3. **Three houses**: `nums = [2,3,2]` → return `3` (can't rob first and last)
4. **All same**: `nums = [1,1,1,1]` → return `2` (rob two non-adjacent)
5. **First and last are large**: `nums = [10,1,1,10]` → return `10` (rob either first or last)

1. **Not handling single house**: Forgetting edge case `N == 1`
2. **Wrong range**: Using `[0..N-1]` and `[1..N]` instead of `[0..N-2]` and `[1..N-1]`
3. **Including both endpoints**: Trying to include both first and last in one case
4. **Not taking maximum**: Forgetting to compare both cases
5. **Index out of bounds**: Not checking bounds when `N == 1` or `N == 2`

## Why This Works

### Circular Constraint:

Since houses are arranged in a circle, if we rob house 0, we cannot rob house N-1. This creates two mutually exclusive cases:

1. **Case 1**: Rob houses `[0..N-2]`
   - We can rob house 0, but not house N-1
   - This is a linear problem

2. **Case 2**: Rob houses `[1..N-1]`
   - We cannot rob house 0, but can rob house N-1
   - This is also a linear problem

By taking the maximum of both cases, we ensure we get the optimal solution while respecting the circular constraint.

### Visual Representation:

```
Case 1: [0..N-2] (exclude last)
  [0] [1] [2] ... [N-2] [N-1]
   ✓   ?   ?   ...   ?    ✗

Case 2: [1..N-1] (exclude first)
  [0] [1] [2] ... [N-2] [N-1]
   ✗   ?   ?   ...   ?    ✓

Result: max(case1, case2)
```

## Related Problems

- [LC 198: House Robber](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-198-house-robber/) - Linear version
- [LC 337: House Robber III](https://www.leetcode.com/problems/house-robber-iii/) - Binary tree structure
- [LC 740: Delete and Earn](https://www.leetcode.com/problems/delete-and-earn/) - Similar DP pattern
- [LC 256: Paint House](https://www.leetcode.com/problems/paint-house/) - Similar constraint pattern

---

*This problem extends House Robber to a circular arrangement. The key insight is breaking the circular constraint into two linear subproblems and taking the maximum, effectively reducing a circular problem to two linear problems.*

## Key Takeaways

1. **Circular Constraint**: First and last houses are adjacent, so we can't rob both
2. **Break into Two Cases**: 
   - Exclude last house: `[0..N-2]`
   - Exclude first house: `[1..N-1]`
3. **Reuse Linear Solution**: Use the same DP logic from House Robber
4. **Space Optimization**: O(1) space using two variables instead of array
5. **Edge Case**: Single house doesn't need splitting

## References

- [LC 213: House Robber II on LeetCode](https://www.leetcode.com/problems/house-robber-ii/)
- [LeetCode Discuss — LC 213: House Robber II](https://www.leetcode.com/problems/house-robber-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/house-robber-ii/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
