---
layout: post
title: "35. Search Insert Position"
date: 2026-01-30 00:00:00 -0700
categories: [leetcode, easy, array, binary-search]
permalink: /2026/01/30/easy-35-search-insert-position/
tags: [leetcode, easy, array, binary-search]
---

# 35. Search Insert Position

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Array properties**: What are the array properties? (Assumption: Array is sorted in ascending order with distinct values - no duplicates)

2. **Target found**: What if target is found? (Assumption: Return the index where target is located)

3. **Target not found**: What if target is not found? (Assumption: Return the index where target should be inserted to maintain sorted order)

4. **Time complexity**: What time complexity is required? (Assumption: O(log n) - must use binary search, not linear scan)

5. **Insertion position**: How is insertion position determined? (Assumption: First position where target can be inserted while maintaining sorted order - same as lower bound)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Scan through the array from left to right. If target is found, return its index. If not found, find the first position where `nums[i] > target` and return `i`. If all elements are less than target, return `nums.length`. This approach has O(n) time complexity, which doesn't meet the O(log n) requirement.

**Step 2: Semi-Optimized Approach (3 minutes)**

Since the array is sorted, we can use binary search. However, we need to handle both cases: when target is found and when it's not found. The key insight is that the insertion position is exactly the lower bound - the first position where `nums[i] >= target`.

**Step 3: Optimized Solution (5 minutes)**

Use binary search to find the lower bound of target. The lower bound is the first position where we can insert target while maintaining sorted order. This is exactly what we need: if target exists, lower bound returns its index; if not, it returns where it should be inserted. This achieves O(log n) time complexity and O(1) space complexity.

## Solution Approach

This problem is essentially finding the **lower bound** of the target value in a sorted array. The lower bound is the first position where `nums[i] >= target`, which is exactly the insertion position we need.

### Key Insights:

1. **Lower Bound = Insertion Position**: The insertion position is the same as the lower bound
2. **Binary Search**: Use binary search to find the lower bound efficiently
3. **Unified Solution**: The same algorithm works for both finding and inserting

## Solution: Binary Search (Lower Bound)

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

### Algorithm Breakdown:

1. **Initialize**: Set `left = 0` and `right = nums.size()` (note: `right` is exclusive)
2. **Binary Search Loop**: While `left < right`:
   - Calculate `mid = left + (right - left) / 2`
   - If `nums[mid] < target`: Target is to the right, so `left = mid + 1`
   - Otherwise: Target is at `mid` or to the left, so `right = mid`
3. **Return**: When `left == right`, we've found the insertion position at `left`

### Why This Works:

- **Lower Bound Logic**: This is the standard lower bound binary search
- **If target exists**: Lower bound returns the first occurrence (exact index)
- **If target doesn't exist**: Lower bound returns where it should be inserted
- **Boundary Cases**: 
  - If target < all elements: returns 0
  - If target > all elements: returns `nums.size()`

### Sample Test Case Run:

**Input:** `nums = [1,3,5,6]`, `target = 5`

```
Initial: left = 0, right = 4

Iteration 1:
  mid = 0 + (4 - 0) / 2 = 2
  nums[2] = 5, target = 5
  Since nums[2] >= target (5 >= 5), move left
  right = mid = 2
  Search range: [0, 2]

Iteration 2:
  mid = 0 + (2 - 0) / 2 = 1
  nums[1] = 3, target = 5
  Since nums[1] < target (3 < 5), move right
  left = mid + 1 = 2
  Search range: [2, 2]

Loop condition: left (2) < right (2) is false, exit loop

Return: left = 2
```

**Verification:** `nums[2] = 5 == target = 5` ✓

**Output:** `2` ✓

---

**Another Example:** `nums = [1,3,5,6]`, `target = 2`

```
Initial: left = 0, right = 4

Iteration 1:
  mid = 0 + (4 - 0) / 2 = 2
  nums[2] = 5, target = 2
  Since nums[2] >= target (5 >= 2), move left
  right = mid = 2
  Search range: [0, 2]

Iteration 2:
  mid = 0 + (2 - 0) / 2 = 1
  nums[1] = 3, target = 2
  Since nums[1] >= target (3 >= 2), move left
  right = mid = 1
  Search range: [0, 1]

Iteration 3:
  mid = 0 + (1 - 0) / 2 = 0
  nums[0] = 1, target = 2
  Since nums[0] < target (1 < 2), move right
  left = mid + 1 = 1
  Search range: [1, 1]

Loop condition: left (1) < right (1) is false, exit loop

Return: left = 1
```

**Verification:** 
- `nums[1] = 3 > target = 2` ✓ (insertion position)
- `nums[0] = 1 < target = 2` ✓ (before insertion)

**Output:** `1` ✓

---

**Edge Case:** `nums = [1,3,5,6]`, `target = 7`

```
Initial: left = 0, right = 4

Iteration 1:
  mid = 0 + (4 - 0) / 2 = 2
  nums[2] = 5, target = 7
  Since nums[2] < target (5 < 7), move right
  left = mid + 1 = 3
  Search range: [3, 4]

Iteration 2:
  mid = 3 + (4 - 3) / 2 = 3
  nums[3] = 6, target = 7
  Since nums[3] < target (6 < 7), move right
  left = mid + 1 = 4
  Search range: [4, 4]

Loop condition: left (4) < right (4) is false, exit loop

Return: left = 4
```

**Verification:** 
- `left = 4 == nums.size()` ✓ (insert at end)
- All elements are less than target ✓

**Output:** `4` ✓

---

**Edge Case:** `nums = [1,3,5,6]`, `target = 0`

```
Initial: left = 0, right = 4

Iteration 1:
  mid = 0 + (4 - 0) / 2 = 2
  nums[2] = 5, target = 0
  Since nums[2] >= target (5 >= 0), move left
  right = mid = 2
  Search range: [0, 2]

Iteration 2:
  mid = 0 + (2 - 0) / 2 = 1
  nums[1] = 3, target = 0
  Since nums[1] >= target (3 >= 0), move left
  right = mid = 1
  Search range: [0, 1]

Iteration 3:
  mid = 0 + (1 - 0) / 2 = 0
  nums[0] = 1, target = 0
  Since nums[0] >= target (1 >= 0), move left
  right = mid = 0
  Search range: [0, 0]

Loop condition: left (0) < right (0) is false, exit loop

Return: left = 0
```

**Verification:** 
- `left = 0` ✓ (insert at beginning)
- All elements are greater than target ✓

**Output:** `0` ✓

## Complexity Analysis

- **Time Complexity**: O(log n) - Binary search eliminates half of the search space at each step
- **Space Complexity**: O(1) - Only using a constant amount of extra space

## Key Insights

1. **Lower Bound Pattern**: This problem is a direct application of the lower bound binary search pattern
2. **Unified Logic**: The same algorithm handles both finding and inserting cases
3. **Exclusive Right Bound**: Using `right = nums.size()` (exclusive) simplifies boundary handling
4. **Loop Invariant**: At each step, we maintain that the insertion position is in `[left, right]`

## Related Problems

- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Uses lower bound and upper bound
- [704. Binary Search](https://leetcode.com/problems/binary-search/) - Standard binary search
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Binary search on rotated array
- [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/) - Binary search variant
