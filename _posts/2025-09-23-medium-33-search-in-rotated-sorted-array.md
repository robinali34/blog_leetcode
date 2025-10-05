---
layout: post
title: "[Medium] 33. Search in Rotated Sorted Array"
date: 2025-09-23 10:00:00 -0000
categories: leetcode algorithm binary-search data-structures array medium cpp rotated-array search problem-solving
---

# [Medium] 33. Search in Rotated Sorted Array

This is a classic binary search problem that requires understanding how to search in a rotated sorted array. The key insight is that even though the array is rotated, we can still use binary search by determining which half of the array is sorted.

## Problem Description

Given a rotated sorted array and a target value, find the index of the target in the array. If the target is not found, return -1.

## Template in C++

### Binary search on answer

```cpp
int bs_on_answer(int left, int right) {
    while (left <= right) {
        int pivot = left + (right - left) / 2;
        if (condition(pivot)) {
            right = pivot + 1;
        } else {
            left = pivot + 1;
        }
    }
    return -1;
}
```

## Solution in C++

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            
            // Subarray on mid's left is sorted
            if (nums[mid] >= nums[left]) {
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // Subarray on mid's right is sorted
            else {
                if (target <= nums[right] && target > nums[mid]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        
        return -1;
    }
};
```

## Solution in Python

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # Subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Subarray on mid's right is sorted
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
```

## Algorithm Explanation

The key insight is that in a rotated sorted array, at least one half of the array (either left or right of the middle element) will always be sorted. We can use this property to determine which half to search:

1. **Check if the left half is sorted**: If `nums[mid] >= nums[left]`, then the left half is sorted
2. **Check if the right half is sorted**: If `nums[mid] < nums[left]`, then the right half is sorted
3. **Determine search direction**: Based on which half is sorted and where the target might be located, we decide whether to search left or right

## Time Complexity
- **Time**: O(log n) - Binary search approach
- **Space**: O(1) - Constant extra space

## Example

For array `[4,5,6,7,0,1,2]` and target `0`:
- Initially: left=0, right=6, mid=3
- nums[3]=7, nums[0]=4, so left half [4,5,6,7] is sorted
- target=0 is not in [4,5,6,7], so search right half
- Continue binary search in right half until target is found

This problem demonstrates the power of binary search even in seemingly complex scenarios like rotated arrays.
