---
layout: post
title: "[Medium] 162. Find Peak Element"
date: 2026-01-30 00:00:00 -0700
categories: [leetcode, medium, array, binary-search]
permalink: /2026/01/30/medium-162-find-peak-element/
tags: [leetcode, medium, array, binary-search]
---
A **peak element** is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time complexity.

## Examples

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

**Example 2:**

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

**Example 3:**

```
Input: nums = [1]
Output: 0
Explanation: For arrays with a single element, that element is a peak.
```

## Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- For all valid `i`, `nums[i] != nums[i + 1]`

## Thinking Process

1. **Binary Search on Unsorted Array**: Even though the array isn't sorted, we can use binary search by comparing with neighbors

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
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};
```

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Binary Search on Unsorted Array**: Even though the array isn't sorted, we can use binary search by comparing with neighbors

**How the code works:**
1. **Binary Search on Unsorted Array**: Even though the array isn't sorted, we can use binary search by comparing with neighbors
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

**Walkthrough** — input `nums = [1,2,3,1]`, expected output `2`:

3 is a peak element and your function should return the index number 2.

- **Time Complexity**: O(log n) - Binary search eliminates half of the search space at each step
- **Space Complexity**: O(1) - Only using a constant amount of extra space
## Related Problems

- [852. Peak Index in a Mountain Array](https://www.leetcode.com/problems/peak-index-in-a-mountain-array/) - Similar problem with guaranteed mountain shape
- [33. Search in Rotated Sorted Array](https://www.leetcode.com/problems/search-in-rotated-sorted-array/) - Binary search on modified sorted array
- [153. Find Minimum in Rotated Sorted Array](https://www.leetcode.com/problems/find-minimum-in-rotated-sorted-array/) - Binary search variant

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Binary Search on Unsorted Array**: Even though the array isn't sorted, we can use binary search by comparing with neighbors
2. **Peak Guarantee**: The boundary conditions (nums[-1] = nums[n] = -∞) guarantee that a peak always exists
3. **Direction Choice**: Comparing `nums[mid]` with `nums[mid + 1]` tells us which direction to search
4. **Loop Invariant**: At each step, we maintain that a peak exists in the current search range [left, right]

## References

- [LC 162: Find Peak Element on LeetCode](https://www.leetcode.com/problems/find-peak-element/)
- [LeetCode Discuss — LC 162: Find Peak Element](https://www.leetcode.com/problems/find-peak-element/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-peak-element/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
