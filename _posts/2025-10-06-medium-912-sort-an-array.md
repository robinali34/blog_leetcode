---
layout: post
title: "[Medium] 912. Sort an Array"
date: 2025-10-06 00:00:00 -0000
categories: leetcode algorithm medium cpp sorting merge-sort heap-sort counting-sort data-structures divide-conquer problem-solving
---
Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem in **O(n log n)** time complexity and with the smallest possible space complexity.

## Examples

**Example 1:**
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

**Example 2:**
```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Thinking Process

1. **Merge Sort** guarantees O(n log n) time complexity and is stable

- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Intervals on timeline</text>

  <line x1="30" y1="60" x2="250" y2="60" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="50" y="48" width="60" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="100" y="48" width="50" height="24" rx="3" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="160" y="48" width="70" height="24" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="95" text-anchor="middle" font-size="11" fill="#6B6560">sort by start → scan overlaps</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | Often O(n^2) or O(2^n) | O(n) | Baseline; clarifies the optimization target |
| **Sort + scan** *(this problem)* | O(n log n) | O(1) | Pairs, intervals, greedy ordering |
| Hash map / set | O(n) | O(n) | Frequency, membership, two-sum style |
| Single-pass linear | O(n) | O(1) | Two pointers, sliding window, Kadane |

## Solution

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

Merge sort is a divide-and-conquer algorithm that divides the array into two halves, sorts them recursively, and then merges the sorted halves.

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> cache(nums.size());
        mergeSort(nums, 0, nums.size() - 1, cache);
        return nums;
    }

private:
    void merge(vector<int>& arr, int left, int pivot, int right, vector<int>& cache){
        int start1 = left;
        int start2 = pivot + 1;
        int n1 = pivot - left + 1;
        int n2 = right - pivot;

        // Copy both halves to cache
        for(int i = 0; i < n1; i++) {
            cache[start1 + i] = arr[start1 + i];
        }
        for(int i = 0; i < n2; i++) {
            cache[start2 + i] = arr[start2 + i];
        }
        
        // Merge the two halves back into arr
        int i = 0, j = 0, k = left;
        while(i < n1 && j < n2) {
            if(cache[start1 + i] <= cache[start2 + j]) {
                arr[k] = cache[start1 + i];
                i++;
            } else {
                arr[k] = cache[start2 + j];
                j++;
            }
            k++;
        }
        
        // Copy remaining elements
        while(i < n1) {
            arr[k] = cache[start1 + i];
            i++;
            k++;
        }
        while(j < n2) {
            arr[k] = cache[start2 + j];
            j++;
            k++;
        }
    }

    void mergeSort(vector<int>& arr, int left, int right, vector<int>& cache) {
        if(left >= right) return;
        int pivot = left + (right - left) / 2;
        mergeSort(arr, left, pivot, cache);
        mergeSort(arr, pivot + 1, right, cache);
        merge(arr, left, pivot, right, cache);
    }
};
```

### Solution Explanation

**Approach:** Sort + scan (this problem)

**Key idea:** 1. **Merge Sort** guarantees O(n log n) time complexity and is stable

**How the code works:**
1. **Merge Sort** guarantees O(n log n) time complexity and is stable
- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.

**Walkthrough** — input `nums = [5,2,3,1]`, expected output `[1,2,3,5]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Algorithm Comparison

| Algorithm | Time Complexity | Space Complexity | Stability | In-Place |
|-----------|----------------|------------------|-----------|----------|
| Merge Sort | O(n log n) | O(n) | Stable | No |
| Heap Sort | O(n log n) | O(1) | Unstable | Yes |
| Counting Sort | O(n + k) | O(k) | Stable | No |

## When to Use Each Algorithm

- **Merge Sort**: When you need a stable sort and have O(n) extra space
- **Heap Sort**: When you need in-place sorting and don't care about stability
- **Counting Sort**: When the range of numbers is small compared to array size

## Related Problems

- [75. Sort Colors](https://www.leetcode.com/problems/sort-colors/) - Counting sort variant
- [148. Sort List](https://www.leetcode.com/problems/sort-list/) - Merge sort on linked list
- [215. Kth Largest Element in an Array](https://www.leetcode.com/problems/kth-largest-element-in-an-array/) - Heap-based approach

## References

- [LC 912: Sort an Array on LeetCode](https://www.leetcode.com/problems/sort-an-array/)
- [LeetCode Discuss — LC 912: Sort an Array](https://www.leetcode.com/problems/sort-an-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/sort-an-array/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Merge Sort** guarantees O(n log n) time complexity and is stable
2. **Heap Sort** is in-place but not stable
3. **Counting Sort** can be very fast when the range is small
4. All three solutions meet the O(n log n) requirement for this problem
