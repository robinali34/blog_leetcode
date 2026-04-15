---
layout: post
title: "[Medium] 713. Subarray Product Less Than K"
date: 2026-03-21
categories: [leetcode, medium, sliding-window, two-pointers]
tags: [leetcode, medium, sliding-window, two-pointers, array]
permalink: /2026/03/21/medium-713-subarray-product-less-than-k/
---

Given an array of positive integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all elements is **strictly less than** `k`.

## Examples

**Example 1:**

```
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays with product < 100:
  [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]
```

**Example 2:**

```
Input: nums = [1,2,3], k = 0
Output: 0
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

## Thinking Process

### Why Sliding Window?

All elements are **positive**, so expanding the window (adding an element) can only **increase** the product, and shrinking (removing from the left) can only **decrease** it. This monotonic property is exactly what makes a sliding window work.

### Counting Trick

When `right` is fixed and the window `[left, right]` has product < k, how many valid subarrays **end at** `right`?

They are: `[left, right]`, `[left+1, right]`, ..., `[right, right]` -- that's `right - left + 1` subarrays.

By summing this for every `right`, we count all valid subarrays exactly once.

### Walk-through

```
nums = [10, 5, 2, 6], k = 100

right=0: prod=10 < 100,  cnt += 1  → [10]
right=1: prod=50 < 100,  cnt += 2  → [5], [10,5]
right=2: prod=100 >= 100, shrink: left=1, prod=10
          prod=10 < 100,  cnt += 2  → [2], [5,2]
right=3: prod=60 < 100,  cnt += 3  → [6], [2,6], [5,2,6]

Total: 1 + 2 + 2 + 3 = 8 ✓
```

### Edge Case

If `k <= 1`, no product of positive integers can be strictly less than `k`, so return 0 immediately.

## Solution: Sliding Window -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1) return 0;
        int n = nums.size();
        long long currProd = 1;
        int cnt = 0;
        for (int left = 0, right = 0; right < n; ++right) {
            currProd *= nums[right];
            while (currProd >= k) {
                currProd /= nums[left++];
            }
            cnt += (right - left + 1);
        }
        return cnt;
    }
};
```
{% endraw %}

**Time**: $O(n)$ -- each element enters and leaves the window at most once
**Space**: $O(1)$

## Why `long long` for the Product?

Elements can be up to 1000 and the array up to 30000 long. While the `while` loop keeps the product below `k` ($\leq 10^6$), a single multiplication `currProd *= nums[right]` can momentarily overflow `int` before the shrink loop fires. Using `long long` prevents this.

## Common Mistakes

- Forgetting the `k <= 1` early return (causes infinite shrink loop or wrong count)
- Counting subarrays starting at `left` instead of ending at `right` (double-counting)
- Using `int` for the running product (overflow before shrinking)

## Key Takeaways

- **"Count subarrays with bounded aggregate of positive values"** = sliding window
- The counting formula `right - left + 1` per step is reusable across many sliding window counting problems
- Positive elements guarantee monotonic product behavior, which is the precondition for the sliding window to work

## Related Problems

- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) -- sliding window on sum
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) -- sliding window on uniqueness
- [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) -- sliding window counting
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) -- prefix sum (not sliding window since negatives possible)

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
