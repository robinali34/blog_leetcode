---
layout: post
title: "215. Kth Largest Element in an Array"
date: 2026-01-05 00:00:00 -0700
categories: [leetcode, medium, array, heap, quickselect, divide-and-conquer]
permalink: /2026/01/05/medium-215-kth-largest-element-in-an-array/
tags: [leetcode, medium, array, heap, priority-queue, quickselect, divide-and-conquer, sorting]
---

# 215. Kth Largest Element in an Array

## Problem Statement

Given an integer array `nums` and an integer `k`, return *the* `kth` *largest element in the array*.

Note that it is the `kth` largest element in the **sorted order**, not the `kth` distinct element.

Can you solve it without sorting?

## Examples

**Example 1:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: The 2nd largest element is 5.
```

**Example 2:**
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Explanation: The 4th largest element is 4.
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Solution Approaches

There are several approaches to solve this problem:

1. **Min Heap**: Maintain a min heap of size k, keeping only the k largest elements
2. **QuickSelect**: Use partition-based selection algorithm (similar to quicksort)
3. **Sorting**: Sort the array and return the kth element (O(n log n))

### Approach 1: Min Heap (Recommended)

**Time Complexity:** O(n log k)  
**Space Complexity:** O(k)

Use a min heap to maintain the k largest elements. When the heap size exceeds k, remove the smallest element.

### Approach 2: QuickSelect

**Time Complexity:** O(n) average, O(n²) worst case  
**Space Complexity:** O(1) (excluding recursion stack)

Use the partition algorithm from quicksort to find the kth largest element without fully sorting the array.

## Solution 1: Min Heap

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<>> minHeap;
        for(int num: nums) {
            minHeap.push(num);
            if(minHeap.size() > k) minHeap.pop();
        }
        return minHeap.top();
    }
};
```

### Algorithm Explanation:

1. **Initialize**: Create a min heap using `priority_queue` with `greater<>` comparator
2. **Process Elements**: 
   - Push each element into the min heap
   - If heap size exceeds `k`, pop the smallest element (maintains k largest)
3. **Return**: The top element is the kth largest

### Why Min Heap for K Largest?

- **Min heap** keeps the **smallest** element at the top
- By maintaining size `k`, we keep the `k` largest elements
- The top element is the smallest among the `k` largest, which is the `kth` largest overall

### Complexity Analysis:

- **Time**: O(n log k) - Each of n elements is pushed/popped from a heap of size k
- **Space**: O(k) - Heap stores at most k elements

## Solution 2: QuickSelect

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        const int N = nums.size();
        return quickSelect(nums, 0, N - 1, N - k);
    }
private:
    int quickSelect(vector<int>& nums, int l, int r, int k) {
        if(l == r) return nums[k];
        int pivot = nums[l], i = l - 1, j = r + 1;
        while(i < j) {
            do i++; while(nums[i] < pivot);
            do j--; while(nums[j] > pivot);
            if(i < j)
                swap(nums[i], nums[j]);
        }
        if(k <= j) return quickSelect(nums, l, j, k);
        else return quickSelect(nums, j + 1, r, k);
    }
};
```

### Algorithm Explanation:

1. **Partition**: Use Hoare's partition scheme to partition around a pivot
2. **Recursive Selection**:
   - If kth element is in left partition, recurse on left
   - Otherwise, recurse on right partition
3. **Base Case**: When `l == r`, we've found the kth element

### How QuickSelect Works:

1. **Choose Pivot**: Use first element as pivot (can be randomized for better average performance)
2. **Partition**: Rearrange array so elements < pivot are on left, > pivot on right
3. **Recurse**: Based on pivot position, recurse on the partition containing the kth element

### Complexity Analysis:

- **Time**: 
  - Average: O(n) - Each partition eliminates roughly half the elements
  - Worst case: O(n²) - Bad pivot selection (can be avoided with randomization)
- **Space**: O(1) excluding recursion stack (O(log n) average, O(n) worst case)

### Key Insight:

- We're looking for the element at position `N - k` in sorted order (0-indexed)
- QuickSelect finds the element at position `k` without fully sorting
- Only recurses on the partition containing the target element

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | When to Use |
|----------|----------------|-----------------|-------------|
| Min Heap | O(n log k) | O(k) | When k is small, need streaming solution |
| QuickSelect | O(n) avg, O(n²) worst | O(1) | When k is large, need O(1) space |
| Sorting | O(n log n) | O(1) | Simple but less efficient |

## Key Insights

1. **Min Heap Pattern**: Use min heap to maintain k largest elements
2. **QuickSelect**: Partition-based selection avoids full sorting
3. **Index Conversion**: kth largest = (n-k)th smallest in sorted array
4. **Space Trade-off**: Heap uses O(k) space, QuickSelect uses O(1) space

## Follow-up Questions

- What if we need to handle dynamic updates (add/remove elements)?
- How would you optimize for very large datasets that don't fit in memory?
- What if we need the k largest elements in sorted order?

## Related Problems

- [LC 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - Similar heap pattern
- [LC 973: K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) - K selection with custom comparator
- [LC 703: Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) - Dynamic version
- [LC 378: Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) - 2D variant

## Implementation Notes

1. **Min Heap**: Use `priority_queue<int, vector<int>, greater<>>` for min heap
2. **QuickSelect**: Use Hoare's partition for better performance
3. **Randomization**: For QuickSelect, randomize pivot to avoid worst case
4. **Edge Cases**: Handle k = 1, k = n, and single element arrays

---

*This problem demonstrates two fundamental approaches: heap-based selection and partition-based selection. The choice depends on constraints and requirements.*

