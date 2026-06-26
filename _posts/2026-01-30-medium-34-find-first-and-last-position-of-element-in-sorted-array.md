---
layout: post
title: "[Medium] 34. Find First and Last Position of Element in Sorted Array"
date: 2026-01-30 00:00:00 -0700
categories: [leetcode, medium, array, binary-search]
permalink: /2026/01/30/medium-34-find-first-and-last-position-of-element-in-sorted-array/
tags: [leetcode, medium, array, binary-search]
---
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Explanation: The target value 8 appears at indices 3 and 4.
```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Explanation: The target value 6 is not found in the array.
```

**Example 3:**

```
Input: nums = [], target = 0
Output: [-1,-1]
Explanation: The array is empty, so target is not found.
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Thinking Process

1. **Lower Bound vs Upper Bound**: Understanding the difference between lower bound (first position >= target) and upper bound (first position > target) is crucial

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
| Standard binary search | O(log n) | O(1) | Sorted array, `left <= right` |
| Lower / upper bound | O(log n) | O(1) | First/last position, insert index |
| **Binary search on rotated array** *(this problem)* | O(log n) | O(1) | Identify sorted half, discard other |
| Binary search on answer | O(n log M) | O(1) | Monotonic predicate over search space |

## Solution

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.empty()) return {-1, -1};
        int left = lowerBound(nums, target);
        if (left == nums.size() || nums[left] != target) {
            return {-1, -1};
        }
        int right = upperBound(nums, target) - 1;
        return {left, right};
    }

private:
    int lowerBound(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    }

    int upperBound(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] <= target) left = mid + 1;
            else right = mid;
        }
        return left;
    }
};
```

### Solution Explanation

**Approach:** Binary search on rotated array (this problem)

**Key idea:** 1. **Lower Bound vs Upper Bound**: Understanding the difference between lower bound (first position >= target) and upper bound (first position > target) is crucial

**How the code works:**
1. **Lower Bound vs Upper Bound**: Understanding the difference between lower bound (first position >= target) and upper bound (first position > target) is crucial
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

**Walkthrough** — input `nums = [5,7,7,8,8,10], target = 8`, expected output `[3,4]`:

The target value 8 appears at indices 3 and 4.

- **Time Complexity**: O(log n) - Two binary searches, each taking O(log n) time
- **Space Complexity**: O(1) - Only using a constant amount of extra space
## Related Problems

- [35. Search Insert Position](https://www.leetcode.com/problems/search-insert-position/) - Find insertion position (lower bound)
- [704. Binary Search](https://www.leetcode.com/problems/binary-search/) - Standard binary search
- [33. Search in Rotated Sorted Array](https://www.leetcode.com/problems/search-in-rotated-sorted-array/) - Binary search on rotated array
- [162. Find Peak Element](https://www.leetcode.com/problems/find-peak-element/) - Binary search variant

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Lower Bound vs Upper Bound**: Understanding the difference between lower bound (first position >= target) and upper bound (first position > target) is crucial
2. **Binary Search Variants**: This problem demonstrates two important binary search variants that are commonly used
3. **Boundary Conditions**: Careful handling of edge cases (empty array, target not found) is essential
4. **Range Calculation**: Upper bound minus 1 gives the last occurrence when target exists

## References

- [LC 34: Find First and Last Position of Element in Sorted Array on LeetCode](https://www.leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [LeetCode Discuss — LC 34: Find First and Last Position of Element in Sorted Array](https://www.leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
