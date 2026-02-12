---
layout: post
title: "LeetCode 416. Partition Equal Subset Sum"
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

## Approach

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

Time Complexity: $O(2^n)$ - TLE.

### 2. Top-Down DP (Memoization)

The brute force approach re-calculates the same state `(index, currentTarget)` multiple times. We can cache these results.
Note: Using `vector<vector<int>>` (with -1 for unvisited) is preferred over `vector<vector<bool>>` to distinguish between "visited and false" vs "unvisited".

Time Complexity: $O(n \cdot \text{target})$
Space Complexity: $O(n \cdot \text{target})$

### 3. Bottom-Up DP (2D)

We can build a table `dp[i][j]` representing whether sum `j` is possible using the first `i` items.
- `dp[i][j] = dp[i-1][j]` (don't include item `i`) `|| dp[i-1][j - nums[i-1]]` (include item `i`).

### 4. Space Optimized DP (1D)

Notice that `dp[i][j]` only depends on the previous row `dp[i-1]`. We can reduce the space to a 1D array.
When iterating through the 1D array, we must iterate **backwards** from `target` to `nums[i]`. This ensures that when we calculate `dp[j]`, we are using values from the *previous* iteration (effectively `dp[i-1]`), not values we just updated in the *current* iteration.

Time Complexity: $O(n \cdot \text{target})$
Space Complexity: $O(\text{target})$

## Solution

### Approach 1: DFS (Time Limit Exceeded)

{% raw %}
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
{% endraw %}

### Approach 2: DFS with Memoization

{% raw %}
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        if (totalSum % 2 != 0) return false;
        int subSetSum = totalSum / 2;
        int n = nums.size();

        // memo[i][j]: -1 unvisited, 0 false, 1 true
        vector<vector<int>> memo(n, vector<int>(subSetSum + 1, -1));
        return dfs(nums, n - 1, subSetSum, memo);
    }

private:
    bool dfs(vector<int>& nums, int i, int target, vector<vector<int>>& memo) {
        if (target == 0) return true;
        if (i < 0 || target < 0) return false;
        
        if (memo[i][target] != -1) return memo[i][target];
        
        bool result = dfs(nums, i - 1, target - nums[i], memo) || 
                      dfs(nums, i - 1, target, memo);
        
        return memo[i][target] = result;
    }
};
```
{% endraw %}

### Approach 3: 2D Dynamic Programming

{% raw %}
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2) return false;

        int subSetSum = sum / 2;
        int n = nums.size();
        // dp[i][j] means whether sum j is possible using first i items
        vector<vector<bool>> dp(n + 1, vector<bool>(subSetSum + 1, false));
        
        // Base case: sum 0 is always possible (by choosing nothing)
        for (int i = 0; i <= n; i++) dp[i][0] = true;

        for (int i = 1; i <= n; i++) {
            int curr = nums[i - 1];
            for (int j = 1; j <= subSetSum; j++) {
                if (j < curr) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - curr];
                }
            }
        }
        return dp[n][subSetSum];
    }
};
```
{% endraw %}

### Approach 4: 1D Dynamic Programming (Space Optimized)

{% raw %}
```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2) return false;

        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;

        for (int num : nums) {
            // Iterate backwards to avoid using the same element multiple times for the same sum
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }
};
```
{% endraw %}

## Template Reference

- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
