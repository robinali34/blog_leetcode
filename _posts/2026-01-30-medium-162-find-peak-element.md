---
layout: post
title: "162. Find Peak Element"
date: 2026-01-30 00:00:00 -0700
categories: [leetcode, medium, array, binary-search]
permalink: /2026/01/30/medium-162-find-peak-element/
tags: [leetcode, medium, array, binary-search]
---

# 162. Find Peak Element

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Peak definition**: What defines a peak element? (Assumption: Element strictly greater than both neighbors - nums[i] > nums[i-1] and nums[i] > nums[i+1])

2. **Boundary conditions**: How do we handle array boundaries? (Assumption: nums[-1] = nums[n] = -∞, so first/last element can be peaks if greater than their single neighbor)

3. **Multiple peaks**: What if there are multiple peaks? (Assumption: Return index of any peak - problem allows any valid peak index)

4. **Time complexity**: What time complexity is required? (Assumption: O(log n) - must use binary search, not linear scan)

5. **Array properties**: Are there any guarantees about the array? (Assumption: Adjacent elements are never equal - nums[i] != nums[i+1] for all valid i)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Scan through the array from left to right, checking each element to see if it's greater than both its neighbors. For the first element, only check if it's greater than the second element. For the last element, only check if it's greater than the second-to-last element. This approach has O(n) time complexity, which doesn't meet the O(log n) requirement.

**Step 2: Semi-Optimized Approach (7 minutes)**

Since we need O(log n) time complexity, we must use binary search. The key insight is that if we're at position `mid` and `nums[mid] < nums[mid + 1]`, then there must be a peak to the right (because the array goes up from mid, and eventually must come down or end at -∞). Similarly, if `nums[mid] > nums[mid + 1]`, there must be a peak to the left or at mid itself. This allows us to eliminate half of the search space at each step.

**Step 3: Optimized Solution (8 minutes)**

Use binary search with the insight that we can always move toward a direction where a peak is guaranteed to exist. If `nums[mid] < nums[mid + 1]`, move right (left = mid + 1). Otherwise, move left (right = mid). The loop condition `left < right` ensures we converge to a single element, which will be a peak. This achieves O(log n) time complexity and O(1) space complexity.

## Solution Approach

This problem requires finding a peak element in O(log n) time, which strongly suggests using binary search. The key insight is that we don't need to find all peaks or a specific peak - we just need to find any peak.

### Key Insights:

1. **Binary Search Applicability**: Even though the array isn't sorted, we can still use binary search by comparing with neighbors
2. **Peak Guarantee**: If `nums[mid] < nums[mid + 1]`, there must be a peak to the right
3. **Convergence**: Using `left < right` and updating `right = mid` or `left = mid + 1` ensures convergence to a peak

## Solution: Binary Search

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

### Algorithm Breakdown:

1. **Initialize**: Set `left = 0` and `right = nums.size() - 1`
2. **Binary Search Loop**: While `left < right`:
   - Calculate `mid = left + (right - left) / 2`
   - If `nums[mid] < nums[mid + 1]`: Peak must be to the right, so `left = mid + 1`
   - Otherwise: Peak is at `mid` or to the left, so `right = mid`
3. **Return**: When `left == right`, we've found a peak at index `left`

### Why This Works:

- If `nums[mid] < nums[mid + 1]`, the array is increasing from `mid` to `mid + 1`. Since `nums[n] = -∞`, there must be a peak somewhere to the right (the array must eventually decrease or end).
- If `nums[mid] >= nums[mid + 1]`, then either `mid` is a peak (if `nums[mid] > nums[mid - 1]`), or there's a peak to the left. We can safely set `right = mid` because we know a peak exists in `[left, mid]`.

### Sample Test Case Run:

**Input:** `nums = [1,2,3,1]`

```
Initial: left = 0, right = 3

Iteration 1:
  mid = 0 + (3 - 0) / 2 = 1
  nums[1] = 2, nums[2] = 3
  Since nums[1] < nums[2] (2 < 3), peak must be to the right
  left = mid + 1 = 2
  Search range: [2, 3]

Iteration 2:
  mid = 2 + (3 - 2) / 2 = 2
  nums[2] = 3, nums[3] = 1
  Since nums[2] > nums[3] (3 > 1), peak is at mid or to the left
  right = mid = 2
  Search range: [2, 2]

Loop condition: left (2) < right (2) is false, exit loop

Return: left = 2
```

**Verification:** `nums[2] = 3` is greater than both neighbors:
- `nums[1] = 2 < 3` ✓
- `nums[3] = 1 < 3` ✓

**Output:** `2` ✓

---

**Another Example:** `nums = [1,2,1,3,5,6,4]`

```
Initial: left = 0, right = 6

Iteration 1:
  mid = 0 + (6 - 0) / 2 = 3
  nums[3] = 3, nums[4] = 5
  Since nums[3] < nums[4] (3 < 5), peak must be to the right
  left = mid + 1 = 4
  Search range: [4, 6]

Iteration 2:
  mid = 4 + (6 - 4) / 2 = 5
  nums[5] = 6, nums[6] = 4
  Since nums[5] > nums[6] (6 > 4), peak is at mid or to the left
  right = mid = 5
  Search range: [4, 5]

Iteration 3:
  mid = 4 + (5 - 4) / 2 = 4
  nums[4] = 5, nums[5] = 6
  Since nums[4] < nums[5] (5 < 6), peak must be to the right
  left = mid + 1 = 5
  Search range: [5, 5]

Loop condition: left (5) < right (5) is false, exit loop

Return: left = 5
```

**Verification:** `nums[5] = 6` is greater than both neighbors:
- `nums[4] = 5 < 6` ✓
- `nums[6] = 4 < 6` ✓

**Output:** `5` ✓

## Complexity Analysis

- **Time Complexity**: O(log n) - Binary search eliminates half of the search space at each step
- **Space Complexity**: O(1) - Only using a constant amount of extra space

## Key Insights

1. **Binary Search on Unsorted Array**: Even though the array isn't sorted, we can use binary search by comparing with neighbors
2. **Peak Guarantee**: The boundary conditions (nums[-1] = nums[n] = -∞) guarantee that a peak always exists
3. **Direction Choice**: Comparing `nums[mid]` with `nums[mid + 1]` tells us which direction to search
4. **Loop Invariant**: At each step, we maintain that a peak exists in the current search range [left, right]

## Related Problems

- [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) - Similar problem with guaranteed mountain shape
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Binary search on modified sorted array
- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) - Binary search variant
