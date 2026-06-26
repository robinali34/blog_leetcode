---
layout: post
title: "[Medium] 2270. Number of Ways to Split Array"
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

For each split index `i`, we need `sum(nums[0..i]) >= sum(nums[i+1..n-1])`. Computing both sums from scratch for every `i` would be O(n^2).

Two approaches to get O(n):

1. **Prefix sum array**: precompute prefix sums, then `leftSum = prefSum[i]` and `rightSum = prefSum[n-1] - prefSum[i]`
2. **Running sums**: maintain `leftSum` and `rightSum`, incrementally transferring each element from right to left

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Prefix sum** *(this problem)* | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| Hash map counting | O(n) | O(n) | Frequency, two-sum variants |

## Solution
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

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** For each split index `i`, we need `sum(nums[0..i]) >= sum(nums[i+1..n-1])`. Computing both sums from scratch for every `i` would be O(n^2).

**How the code works:**
1. **Prefix sum array**: precompute prefix sums, then `leftSum = prefSum[i]` and `rightSum = prefSum[n-1] - prefSum[i]`
2. **Running sums**: maintain `leftSum` and `rightSum`, incrementally transferring each element from right to left

**Walkthrough** — input `nums = [10,4,-8,7]`, expected output `2`:

Split at 0: [10] vs [4,-8,7] → 10 >= 3 ✓
  Split at 1: [10,4] vs [-8,7] → 14 >= -1 ✓
  Split at 2: [10,4,-8] vs [7] → 6 >= 7 ✗
## Why `long long`?

With n up to 10^5 and values up to pm 10^5, the total sum can reach pm 10^{10}, which overflows a 32-bit `int`. Using `long long` prevents this.

## Comparison

| Approach | Time | Space | Notes |
|---|---|---|---|
| Prefix Sum Array | O(n) | O(n) | Reusable for multiple queries |
| Running Sums | O(n) | O(1) | Optimal for single pass |

## Common Mistakes

- Using `int` instead of `long long` for sums (overflow)
- Iterating to `i < n` instead of `i < n - 1` (the right side must be non-empty)
- Off-by-one in prefix sum indexing

## Key Takeaways

- **"Compare left/right partition sums at every split"** = prefix sum or running sum
- The running sum approach is a space optimization: instead of storing all prefix sums, maintain two counters and transfer incrementally
- Always check value ranges to decide if `long long` is needed

## Related Problems

- [303. Range Sum Query - Immutable](https://www.leetcode.com/problems/range-sum-query-immutable/) -- prefix sum fundamentals
- [523. Continuous Subarray Sum](https://www.leetcode.com/problems/continuous-subarray-sum/) -- prefix sum with modular arithmetic
- [238. Product of Array Except Self](https://www.leetcode.com/problems/product-of-array-except-self/) -- prefix/suffix products
- [724. Find Pivot Index](https://www.leetcode.com/problems/find-pivot-index/) -- left sum == right sum

## References

- [LC 2270: Number of Ways to Split Array on LeetCode](https://www.leetcode.com/problems/number-of-ways-to-split-array/)
- [LeetCode Discuss — LC 2270: Number of Ways to Split Array](https://www.leetcode.com/problems/number-of-ways-to-split-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/number-of-ways-to-split-array/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings — Prefix Sum](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
