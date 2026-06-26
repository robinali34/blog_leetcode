---
layout: post
title: "[Easy] 35. Search Insert Position"
date: 2026-01-30 00:00:00 -0700
categories: [leetcode, easy, array, binary-search]
permalink: /2026/01/30/easy-35-search-insert-position/
tags: [leetcode, easy, array, binary-search]
---
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2
Explanation: The target value 5 is found at index 2.
```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1
Explanation: The target value 2 is not found, so it would be inserted at index 1.
```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4
Explanation: The target value 7 is not found, so it would be inserted at index 4 (after all elements).
```

**Example 4:**

```
Input: nums = [1,3,5,6], target = 0
Output: 0
Explanation: The target value 0 is not found, so it would be inserted at index 0 (before all elements).
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-10^4 <= target <= 10^4`

## Thinking Process

1. **Lower Bound Pattern**: This problem is a direct application of the lower bound binary search pattern

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
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    }
};
```

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Lower Bound Pattern**: This problem is a direct application of the lower bound binary search pattern

**How the code works:**
1. **Lower Bound Pattern**: This problem is a direct application of the lower bound binary search pattern
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

**Walkthrough** — input `nums = [1,3,5,6], target = 5`, expected output `2`:

The target value 5 is found at index 2.

- **Time Complexity**: O(log n) - Binary search eliminates half of the search space at each step
- **Space Complexity**: O(1) - Only using a constant amount of extra space
## Related Problems

- [34. Find First and Last Position of Element in Sorted Array](https://www.leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Uses lower bound and upper bound
- [704. Binary Search](https://www.leetcode.com/problems/binary-search/) - Standard binary search
- [33. Search in Rotated Sorted Array](https://www.leetcode.com/problems/search-in-rotated-sorted-array/) - Binary search on rotated array
- [162. Find Peak Element](https://www.leetcode.com/problems/find-peak-element/) - Binary search variant

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Lower Bound Pattern**: This problem is a direct application of the lower bound binary search pattern
2. **Unified Logic**: The same algorithm handles both finding and inserting cases
3. **Exclusive Right Bound**: Using `right = nums.size()` (exclusive) simplifies boundary handling
4. **Loop Invariant**: At each step, we maintain that the insertion position is in `[left, right]`

## References

- [LC 35: Search Insert Position on LeetCode](https://www.leetcode.com/problems/search-insert-position/)
- [LeetCode Discuss — LC 35: Search Insert Position](https://www.leetcode.com/problems/search-insert-position/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/search-insert-position/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
