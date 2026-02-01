---
layout: post
title: "34. Find First and Last Position of Element in Sorted Array"
date: 2026-01-30 00:00:00 -0700
categories: [leetcode, medium, array, binary-search]
permalink: /2026/01/30/medium-34-find-first-and-last-position-of-element-in-sorted-array/
tags: [leetcode, medium, array, binary-search]
---

# 34. Find First and Last Position of Element in Sorted Array

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Array properties**: What are the array properties? (Assumption: Array is sorted in non-decreasing order - can contain duplicates)

2. **Target existence**: What if target is not found? (Assumption: Return [-1, -1] - target doesn't exist in array)

3. **Return format**: What should we return? (Assumption: Array of two integers [start, end] - first and last position of target)

4. **Time complexity**: What time complexity is required? (Assumption: O(log n) - must use binary search, not linear scan)

5. **Single occurrence**: What if target appears only once? (Assumption: Return [index, index] - same index for both start and end)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Scan through the array from left to right to find the first occurrence of target, then scan from right to left to find the last occurrence. This approach has O(n) time complexity, which doesn't meet the O(log n) requirement.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use binary search to find the target, then expand left and right to find the boundaries. However, in the worst case (all elements are target), this still requires O(n) time to expand, which doesn't meet the requirement.

**Step 3: Optimized Solution (8 minutes)**

Use two binary searches: one to find the lower bound (first position where target can be inserted, which is the first occurrence) and one to find the upper bound (first position where target+1 can be inserted, which is one past the last occurrence). Subtract 1 from the upper bound to get the last occurrence. This achieves O(log n) time complexity with two binary searches.

## Solution Approach

This problem requires finding the first and last occurrence of a target in a sorted array with O(log n) time complexity. The key insight is to use two binary searches: one for the lower bound and one for the upper bound.

### Key Insights:

1. **Lower Bound**: The first position where target can be inserted (first occurrence of target)
2. **Upper Bound**: The first position where target+1 can be inserted (one past the last occurrence)
3. **Two Binary Searches**: Use separate binary search functions for lower and upper bounds
4. **Boundary Handling**: Check if target exists before calculating the range

## Solution: Binary Search with Lower and Upper Bounds

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

### Algorithm Breakdown:

1. **Edge Case**: If array is empty, return `[-1, -1]`
2. **Find Lower Bound**: Use binary search to find first position where `target` can be inserted
3. **Check Existence**: If `lowerBound == nums.size()` or `nums[lowerBound] != target`, target doesn't exist, return `[-1, -1]`
4. **Find Upper Bound**: Use binary search to find first position where `target + 1` can be inserted
5. **Calculate Range**: Last occurrence is `upperBound - 1`
6. **Return**: `[lowerBound, upperBound - 1]`

### Lower Bound Binary Search:

- **Purpose**: Find the first position where target can be inserted (first occurrence)
- **Logic**: If `nums[mid] < target`, move right (`left = mid + 1`). Otherwise, move left (`right = mid`)
- **Result**: Returns the first index where `nums[index] >= target`

### Upper Bound Binary Search:

- **Purpose**: Find the first position where target+1 can be inserted (one past last occurrence)
- **Logic**: If `nums[mid] <= target`, move right (`left = mid + 1`). Otherwise, move left (`right = mid`)
- **Result**: Returns the first index where `nums[index] > target`

### Why This Works:

- **Lower Bound**: Finds the first position where we can insert target, which is exactly the first occurrence
- **Upper Bound**: Finds the first position where we can insert target+1, which is one position after the last occurrence
- **Range Calculation**: `[lowerBound, upperBound - 1]` gives us the exact range of target occurrences

### Sample Test Case Run:

**Input:** `nums = [5,7,7,8,8,10]`, `target = 8`

```
Step 1: Find Lower Bound (first occurrence of 8)

Initial: left = 0, right = 6

Iteration 1:
  mid = 0 + (6 - 0) / 2 = 3
  nums[3] = 8, target = 8
  Since nums[3] >= target (8 >= 8), move left
  right = mid = 3
  Search range: [0, 3]

Iteration 2:
  mid = 0 + (3 - 0) / 2 = 1
  nums[1] = 7, target = 8
  Since nums[1] < target (7 < 8), move right
  left = mid + 1 = 2
  Search range: [2, 3]

Iteration 3:
  mid = 2 + (3 - 2) / 2 = 2
  nums[2] = 7, target = 8
  Since nums[2] < target (7 < 8), move right
  left = mid + 1 = 3
  Search range: [3, 3]

Loop condition: left (3) < right (3) is false, exit loop

Lower Bound = 3

Step 2: Check if target exists
  nums[3] = 8 == target = 8 ✓
  Target exists at index 3

Step 3: Find Upper Bound (first position where 9 can be inserted)

Initial: left = 0, right = 6

Iteration 1:
  mid = 0 + (6 - 0) / 2 = 3
  nums[3] = 8, target = 8
  Since nums[3] <= target (8 <= 8), move right
  left = mid + 1 = 4
  Search range: [4, 6]

Iteration 2:
  mid = 4 + (6 - 4) / 2 = 5
  nums[5] = 10, target = 8
  Since nums[5] > target (10 > 8), move left
  right = mid = 5
  Search range: [4, 5]

Iteration 3:
  mid = 4 + (5 - 4) / 2 = 4
  nums[4] = 8, target = 8
  Since nums[4] <= target (8 <= 8), move right
  left = mid + 1 = 5
  Search range: [5, 5]

Loop condition: left (5) < right (5) is false, exit loop

Upper Bound = 5

Step 4: Calculate range
  First occurrence: lowerBound = 3
  Last occurrence: upperBound - 1 = 5 - 1 = 4

Result: [3, 4]
```

**Verification:**
- `nums[3] = 8` ✓ (first occurrence)
- `nums[4] = 8` ✓ (last occurrence)
- `nums[2] = 7 ≠ 8` ✓ (before first)
- `nums[5] = 10 ≠ 8` ✓ (after last)

**Output:** `[3, 4]` ✓

---

**Another Example:** `nums = [5,7,7,8,8,10]`, `target = 6`

```
Step 1: Find Lower Bound

Initial: left = 0, right = 6

Iteration 1:
  mid = 0 + (6 - 0) / 2 = 3
  nums[3] = 8, target = 6
  Since nums[3] >= target (8 >= 6), move left
  right = mid = 3
  Search range: [0, 3]

Iteration 2:
  mid = 0 + (3 - 0) / 2 = 1
  nums[1] = 7, target = 6
  Since nums[1] >= target (7 >= 6), move left
  right = mid = 1
  Search range: [0, 1]

Iteration 3:
  mid = 0 + (1 - 0) / 2 = 0
  nums[0] = 5, target = 6
  Since nums[0] < target (5 < 6), move right
  left = mid + 1 = 1
  Search range: [1, 1]

Loop condition: left (1) < right (1) is false, exit loop

Lower Bound = 1

Step 2: Check if target exists
  nums[1] = 7 != target = 6 ✗
  Target does not exist

Result: [-1, -1]
```

**Output:** `[-1, -1]` ✓

## Complexity Analysis

- **Time Complexity**: O(log n) - Two binary searches, each taking O(log n) time
- **Space Complexity**: O(1) - Only using a constant amount of extra space

## Key Insights

1. **Lower Bound vs Upper Bound**: Understanding the difference between lower bound (first position >= target) and upper bound (first position > target) is crucial
2. **Binary Search Variants**: This problem demonstrates two important binary search variants that are commonly used
3. **Boundary Conditions**: Careful handling of edge cases (empty array, target not found) is essential
4. **Range Calculation**: Upper bound minus 1 gives the last occurrence when target exists

## Related Problems

- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) - Find insertion position (lower bound)
- [704. Binary Search](https://leetcode.com/problems/binary-search/) - Standard binary search
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Binary search on rotated array
- [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/) - Binary search variant
