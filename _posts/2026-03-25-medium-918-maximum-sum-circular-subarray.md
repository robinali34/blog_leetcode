---
layout: post
title: "LeetCode 918. Maximum Sum Circular Subarray"
date: 2026-03-25
categories: [leetcode, medium, dp, array, kadane]
tags: [leetcode, medium, dp, array, kadane]
permalink: /2026/03/25/medium-918-maximum-sum-circular-subarray/
---

Given a **circular** integer array `nums`, find the maximum possible sum of a non-empty subarray. A circular subarray can wrap around the end back to the beginning.

## Examples

**Example 1:**

```
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
```

**Example 2:**

```
Input: nums = [5,-3,5]
Output: 10
Explanation: Wrapping subarray [5, 5] (index 2→0) has sum 10.
```

**Example 3:**

```
Input: nums = [-3,-2,-3]
Output: -2
Explanation: All negative; best is single element [-2].
```

## Constraints

- `n == nums.length`
- `1 <= n <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Thinking Process

### Two Cases

The maximum subarray in a circular array falls into one of two cases:

```
Case 1: No wrapping (normal Kadane's)
  [ . . [max subarray] . . ]

Case 2: Wrapping around (subarray spans both ends)
  [part2 . [min subarray] . part1]
  ←─────── total ──────────────→
```

**Case 1**: Standard maximum subarray -- solved by Kadane's algorithm.

**Case 2**: The wrapping subarray = total sum minus the **minimum** subarray in the middle. So:

$$\text{wrap sum} = \text{total} - \text{minSubarraySum}$$

### Answer

$$\max(\text{maxSum},\ \text{total} - \text{minSum})$$

### Edge Case: All Negative

If every element is negative, `maxSum < 0`. In this case `total - minSum = 0` (the min subarray is the entire array), which would represent an empty subarray -- invalid. So we return `maxSum` directly.

### Walk-through

```
nums = [5, -3, 5]

Kadane max: curMax → 5, 2, 7  →  maxSum = 7? No...
  x=5:  curMax=max(5, 0+5)=5,   maxSum=max(5,5)=5
  x=-3: curMax=max(-3, 5-3)=2,  maxSum=max(5,2)=5
  x=5:  curMax=max(5, 2+5)=7,   maxSum=max(5,7)=7

Kadane min: curMin → 5, -3, -3  →  minSum = -3
  x=5:  curMin=min(5, 0+5)=5,   minSum=min(5,5)=5
  x=-3: curMin=min(-3, 5-3)=-3, minSum=min(5,-3)=-3
  x=5:  curMin=min(5, -3+5)=2,  minSum=min(-3,2)=-3

total = 7

maxSum=7 ≥ 0, so answer = max(7, 7-(-3)) = max(7, 10) = 10 ✓
```

## Solution: Double Kadane's -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int total = 0;
        int maxSum = nums[0], curMax = 0;
        int minSum = nums[0], curMin = 0;

        for (int x : nums) {
            curMax = max(x, curMax + x);
            maxSum = max(maxSum, curMax);

            curMin = min(x, curMin + x);
            minSum = min(minSum, curMin);

            total += x;
        }

        if (maxSum < 0) return maxSum;
        return max(maxSum, total - minSum);
    }
};
```
{% endraw %}

**Time**: $O(n)$ -- single pass computing both Kadane's simultaneously
**Space**: $O(1)$

## Why `total - minSum` Gives the Wrap-Around Sum

```
[  part2  |  min subarray  |  part1  ]
 ←──────── total ─────────────────────→

wrap sum = part1 + part2
         = total - min subarray
         = total - minSum
```

The wrapping subarray is everything **except** the minimum contiguous subarray. Subtracting the minimum from the total gives the maximum possible wrap.

## Common Mistakes

- Forgetting the all-negative edge case (`total - minSum = 0` represents an empty subarray)
- Running two separate loops instead of combining both Kadane's in one pass (works but unnecessary)
- Initializing `maxSum` and `minSum` to `0` instead of `nums[0]` (misses the case where the best answer is a single element)

## Key Takeaways

- **Circular max subarray = max(normal Kadane's, total - min Kadane's)** -- elegant reduction
- Running max-Kadane's and min-Kadane's simultaneously in a single pass keeps it $O(n)$ time, $O(1)$ space
- The "all negative" guard is the one subtlety -- without it, the wrap case incorrectly returns 0

## Related Problems

- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) -- standard Kadane's (non-circular)
- [134. Gas Station](https://leetcode.com/problems/gas-station/) -- circular array with running sum
- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) -- Kadane's variant with products
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) -- subarray with constraint

## Template Reference

- [DP](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
