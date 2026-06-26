---
layout: post
title: "[Medium] 416. Partition Equal Subset Sum"
date: 2026-02-11
categories: [leetcode, medium, dynamic-programming]
tags: [leetcode, medium, dp, knapsack]
permalink: /2026/02/11/medium-416-partition-equal-subset-sum/
---
Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or* `false` *otherwise*.

## Examples

**Example 1:**

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Thinking Process

This problem is a classic variation of the **0/1 Knapsack Problem**. 

1.  **Total Sum Check**: First, calculate the sum of all elements. If the total sum is odd, it's impossible to split it into two equal integer partitions, so return `false`.
2.  **Target Sum**: If the total sum is even, our goal is to find a subset of elements that sums up to `target = totalSum / 2`. If we find such a subset, the remaining elements will automatically sum to `target` as well.
3.  **Transformation**: The problem becomes: "Can we pick a subset of items from `nums` such that their sum is exactly `target`?"

### 1. Brute Force (DFS)

We can try to include or exclude each element recursively.
- **Base Case**: If `target == 0`, we found a subset. If `target < 0` or we run out of elements, return `false`.
- **Recursive Step**: For index `i`, we can either:
    - Include `nums[i]` in the sum (subtract from target).
    - Exclude `nums[i]` (keep target same).

Time Complexity: O(2^n) - TLE.

### 2. Top-Down DP (Memoization)

The brute force approach re-calculates the same state `(index, currentTarget)` multiple times. We can cache these results.
Note: Using `vector<vector<int>>` (with -1 for unvisited) is preferred over `vector<vector<bool>>` to distinguish between "visited and false" vs "unvisited".

Time Complexity: O(n · text{target})
Space Complexity: O(n · text{target})

### 3. Bottom-Up DP (2D)

We can build a table `dp[i][j]` representing whether sum `j` is possible using the first `i` items.
- `dp[i][j] = dp[i-1][j]` (don't include item `i`) `|| dp[i-1][j - nums[i-1]]` (include item `i`).

### 4. Space Optimized DP (1D)

Notice that `dp[i][j]` only depends on the previous row `dp[i-1]`. We can reduce the space to a 1D array.
When iterating through the 1D array, we must iterate **backwards** from `target` to `nums[i]`. This ensures that when we calculate `dp[j]`, we are using values from the *previous* iteration (effectively `dp[i-1]`), not values we just updated in the *current* iteration.

Time Complexity: O(n · text{target})
Space Complexity: O(text{target})

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

### Approach 1: DFS (Time Limit Exceeded)
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        if (totalSum % 2 != 0) return false;
        int subSetSum = totalSum / 2;
        return dfs(nums, nums.size() - 1, subSetSum); 
    }

private:
    bool dfs(vector<int>& nums, int n, int subSetSum) {
        if (subSetSum == 0) return true;
        if (n < 0 || subSetSum < 0) return false;
        return dfs(nums, n - 1, subSetSum - nums[n]) || dfs(nums, n - 1, subSetSum);
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** This problem is a classic variation of the **0/1 Knapsack Problem**.

**How the code works:**
1.  **Total Sum Check**: First, calculate the sum of all elements. If the total sum is odd, it's impossible to split it into two equal integer partitions, so return `false`.
2.  **Target Sum**: If the total sum is even, our goal is to find a subset of elements that sums up to `target = totalSum / 2`. If we find such a subset, the remaining elements will automatically sum to `target` as well.
3.  **Transformation**: The problem becomes: "Can we pick a subset of items from `nums` such that their sum is exactly `target`?"
- **Base Case**: If `target == 0`, we found a subset. If `target < 0` or we run out of elements, return `false`.
- **Recursive Step**: For index `i`, we can either:
- Include `nums[i]` in the sum (subtract from target).

**Walkthrough** — input `nums = [1,5,11,5]`, expected output `true`:

The array can be partitioned as [1, 5, 5] and [11].
## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

- **Pattern:** 1D DP (this problem)
- **Base Case**: If `target == 0`, we found a subset. If `target < 0` or we run out of elements, return `false`.
- **Recursive Step**: For index `i`, we can either:

## References

- [LC 416: Partition Equal Subset Sum on LeetCode](https://www.leetcode.com/problems/partition-equal-subset-sum/)
- [LeetCode Discuss — LC 416: Partition Equal Subset Sum](https://www.leetcode.com/problems/partition-equal-subset-sum/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/partition-equal-subset-sum/editorial/) *(may require premium)*

## Template Reference

- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
