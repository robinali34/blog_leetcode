---
layout: post
title: "[Medium] 209. Minimum Size Subarray Sum"
date: 2026-01-26 00:00:00 -0700
categories: [leetcode, medium, array, sliding-window, binary-search, prefix-sum]
permalink: /2026/01/26/medium-209-minimum-size-subarray-sum/
tags: [leetcode, medium, array, sliding-window, binary-search, prefix-sum, two-pointers]
---
Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a **subarray** whose sum is greater than or equal to* `target`. If there is no such subarray, return `0`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

**Example 3:**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Thinking Process

1. **Prefix Sum + Binary Search**:
- Good when you need to query multiple ranges
- O(n log n) time, O(n) space
- More complex but flexible

- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 130" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary search: shrink [lo … hi]</text>

  <rect x="40" y="40" width="48" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="64" y="58" text-anchor="middle" font-size="12" fill="#3A3530">lo</text>
  <rect x="108" y="40" width="48" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="132" y="58" text-anchor="middle" font-size="12" fill="#3A3530">mid</text>
  <rect x="196" y="40" width="48" height="32" rx="4" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="220" y="58" text-anchor="middle" font-size="12" fill="#3A3530">hi</text>
  <rect x="60" y="90" width="160" height="28" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="140" y="108" text-anchor="middle" font-size="11" fill="#6B6560">discard half each step → O(log n)</text>
  <path d="M132 72v12M220 72v12" stroke="#9A9792" stroke-width="1.5" marker-end="url(#a)"/>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Standard binary search** *(this problem)* | O(log n) | O(1) | Sorted array, `left <= right` |
| Lower / upper bound | O(log n) | O(1) | First/last position, insert index |
| Binary search on rotated array | O(log n) | O(1) | Identify sorted half, discard other |
| Binary search on answer | O(n log M) | O(1) | Monotonic predicate over search space |

## Solution

```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if(nums.empty()) return 0;
        const int N = nums.size();
        int rtn = INT_MAX;
        vector<int> sums(N + 1, 0);
        for(int i = 1; i <= N; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }
        for(int i = 1; i <= N; i++) {
            int currTarget = target + sums[i - 1];
            auto it = lower_bound(sums.begin(), sums.end(), currTarget);
            if(it != sums.end()) {
                rtn = min(rtn, (int)(it - sums.begin()) - (i - 1));
            }
        }
        return rtn == INT_MAX? 0 : rtn;
    }
};
```

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Prefix Sum + Binary Search**:

**How the code works:**
1. **Prefix Sum + Binary Search**:
- Good when you need to query multiple ranges
- O(n log n) time, O(n) space
- More complex but flexible
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.

**Walkthrough** — input `target = 7, nums = [2,3,1,2,4,3]`, expected output `2`:

The subarray [4,3] has the minimal length under the problem constraint.
## Common Mistakes

1. **Empty array**: `nums = []` → return `0`
2. **No valid subarray**: `nums = [1,1,1]`, `target = 10` → return `0`
3. **Single element**: `nums = [5]`, `target = 5` → return `1`
4. **Entire array needed**: `nums = [1,2,3]`, `target = 6` → return `3`
5. **First element**: `nums = [10,1,1]`, `target = 10` → return `1`

1. **Wrong binary search target**: Forgetting to add `sums[i-1]` to target
2. **Index calculation**: Wrong length calculation `(it - sums.begin()) - (i - 1)`
3. **Not checking bounds**: Not checking if `it != sums.end()`
4. **Sliding window**: Not shrinking window when sum >= target
5. **Return value**: Returning `INT_MAX` instead of `0` when no solution

## Related Problems

- [LC 3: Longest Substring Without Repeating Characters](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) - Sliding window pattern
- [LC 76: Minimum Window Substring](https://www.leetcode.com/problems/minimum-window-substring/) - Similar sliding window
- [LC 209: Minimum Size Subarray Sum](https://www.leetcode.com/problems/minimum-size-subarray-sum/) - This problem
- [LC 862: Shortest Subarray with Sum at Least K](https://www.leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) - Similar with negative numbers
- [LC 53: Maximum Subarray](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-53-maximum-subarray/) - Maximum sum subarray

## Key Takeaways

1. **Prefix Sum + Binary Search**:
   - Good when you need to query multiple ranges
   - O(n log n) time, O(n) space
   - More complex but flexible

2. **Sliding Window**:
   - More intuitive and efficient
   - O(n) time, O(1) space
   - Preferred for single query problems

3. **Monotonic Property**: Prefix sums are non-decreasing (all positive), enabling binary search

4. **Window Shrinking**: Once sum >= target, shrink from left to find minimum length

## References

- [LC 209: Minimum Size Subarray Sum on LeetCode](https://www.leetcode.com/problems/minimum-size-subarray-sum/)
- [LeetCode Discuss — LC 209: Minimum Size Subarray Sum](https://www.leetcode.com/problems/minimum-size-subarray-sum/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-size-subarray-sum/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
