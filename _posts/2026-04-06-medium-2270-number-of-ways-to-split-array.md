---
layout: post
title: "LeetCode 2270. Number of Ways to Split Array"
date: 2026-04-06
categories: [leetcode, medium, prefix-sum, array]
tags: [leetcode, medium, prefix-sum, array]
permalink: /2026/04/06/medium-2270-number-of-ways-to-split-array/
---

You are given a 0-indexed integer array `nums` of length `n`. A split at index `i` is **valid** if the sum of the first `i + 1` elements is **greater than or equal to** the sum of the remaining elements. Return the number of valid splits.

## Examples

**Example 1:**

```
Input: nums = [10,4,-8,7]
Output: 2
Explanation:
  Split at 0: [10] vs [4,-8,7] → 10 >= 3 ✓
  Split at 1: [10,4] vs [-8,7] → 14 >= -1 ✓
  Split at 2: [10,4,-8] vs [7] → 6 >= 7 ✗
```

**Example 2:**

```
Input: nums = [2,3,1,0]
Output: 2
Explanation:
  Split at 0: [2] vs [3,1,0] → 2 >= 4 ✗
  Split at 1: [2,3] vs [1,0] → 5 >= 1 ✓
  Split at 2: [2,3,1] vs [0] → 6 >= 0 ✓
```

## Constraints

- `2 <= n <= 10^5`
- `-10^5 <= nums[i] <= 10^5`

## Thinking Process

For each split index `i`, we need `sum(nums[0..i]) >= sum(nums[i+1..n-1])`. Computing both sums from scratch for every `i` would be $O(n^2)$.

Two approaches to get $O(n)$:

1. **Prefix sum array**: precompute prefix sums, then `leftSum = prefSum[i]` and `rightSum = prefSum[n-1] - prefSum[i]`
2. **Running sums**: maintain `leftSum` and `rightSum`, incrementally transferring each element from right to left

## Solution 1: Prefix Sum Array -- $O(n)$ time, $O(n)$ space

{% raw %}
```cpp
class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int n = nums.size();
        vector<long long> prefSum(n);
        prefSum[0] = nums[0];
        for (int i = 1; i < n; ++i) {
            prefSum[i] = prefSum[i - 1] + nums[i];
        }
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            long long leftSum = prefSum[i];
            long long rightSum = prefSum[n - 1] - prefSum[i];
            if (leftSum >= rightSum) {
                count++;
            }
        }
        return count;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ for prefix sum array

## Solution 2: Running Sums -- $O(n)$ time, $O(1)$ space

Start with `rightSum = total` and `leftSum = 0`. For each split, move `nums[i]` from right to left.

{% raw %}
```cpp
class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int n = nums.size();
        long long leftSum = 0, rightSum = 0;
        for (int num : nums) {
            rightSum += num;
        }
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            leftSum += nums[i];
            rightSum -= nums[i];
            if (leftSum >= rightSum) {
                count++;
            }
        }
        return count;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(1)$

## Why `long long`?

With $n$ up to $10^5$ and values up to $\pm 10^5$, the total sum can reach $\pm 10^{10}$, which overflows a 32-bit `int`. Using `long long` prevents this.

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Prefix Sum Array | $O(n)$ | $O(n)$ | Reusable for multiple queries |
| Running Sums | $O(n)$ | $O(1)$ | Optimal for single pass |

## Common Mistakes

- Using `int` instead of `long long` for sums (overflow)
- Iterating to `i < n` instead of `i < n - 1` (the right side must be non-empty)
- Off-by-one in prefix sum indexing

## Key Takeaways

- **"Compare left/right partition sums at every split"** = prefix sum or running sum
- The running sum approach is a space optimization: instead of storing all prefix sums, maintain two counters and transfer incrementally
- Always check value ranges to decide if `long long` is needed

## Related Problems

- [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) -- prefix sum fundamentals
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) -- prefix sum with modular arithmetic
- [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) -- prefix/suffix products
- [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) -- left sum == right sum

## Template Reference

- [Arrays & Strings — Prefix Sum](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
