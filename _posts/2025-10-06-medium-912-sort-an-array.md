---
layout: post
title: "[Medium] 912. Sort an Array"
date: 2025-10-06 00:00:00 -0000
categories: leetcode algorithm medium cpp sorting merge-sort heap-sort counting-sort data-structures divide-conquer problem-solving
---

# [Medium] 912. Sort an Array

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Sorting algorithm**: Can we use built-in sort? (Assumption: Problem asks to implement sorting algorithm - need to implement manually)

2. **Sort order**: What order should we sort in? (Assumption: Ascending order - smallest to largest)

3. **Stability**: Does sort need to be stable? (Assumption: Not specified, but stable sort is preferred - maintain relative order of equal elements)

4. **In-place sorting**: Should we sort in-place? (Assumption: Can modify input array - typically O(n) space for merge sort)

5. **Time complexity**: What time complexity is expected? (Assumption: O(n log n) - optimal comparison-based sorting)

## Solution 1: Merge Sort

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

### How Merge Sort Works:

1. **Divide**: Split the array into two halves
2. **Conquer**: Recursively sort both halves
3. **Combine**: Merge the sorted halves back together

The merge operation compares elements from both halves and places them in the correct order.

## Solution 2: Heap Sort

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)

Heap sort uses a max-heap to sort the array in-place.

```cpp
class Solution {
private:
    void heapify(vector<int>& arr, int n, int i) {
        int largest = i, left = 2 * i + 1, right = 2 * i + 2;
        
        // Find the largest among root and children
        if(left < n && arr[left] > arr[largest]) {
            largest = left;
        }
        if(right < n && arr[right] > arr[largest]) {
            largest = right;
        }
        
        // If largest is not root, swap and heapify
        if(largest != i) {
            swap(arr[i], arr[largest]);
            heapify(arr, n, largest);
        }
    }
    
    void heapSort(vector<int>& arr) {
        int n = arr.size();
        
        // Build max heap
        for(int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }
        
        // Extract elements from heap one by one
        for(int i = n - 1; i >= 0; i--) {
            swap(arr[0], arr[i]);  // Move max to end
            heapify(arr, i, 0);    // Heapify reduced heap
        }
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        heapSort(nums);
        return nums;
    }
};
```

### How Heap Sort Works:

1. **Build Max Heap**: Convert array to max-heap
2. **Extract Maximum**: Repeatedly extract the maximum element and place it at the end
3. **Heapify**: Maintain heap property after each extraction

## Solution 3: Counting Sort

**Time Complexity:** O(n + k) where k is the range of input  
**Space Complexity:** O(k)

Counting sort works well when the range of numbers is small.

```cpp
class Solution {
private:    
    void countSort(vector<int>& arr) {
        unordered_map<int, int> counts;
        int minVal = *min_element(arr.begin(), arr.end());
        int maxVal = *max_element(arr.begin(), arr.end());
        
        // Count frequency of each element
        for(auto& val: arr) counts[val]++;
        
        // Reconstruct sorted array
        int idx = 0;
        for(int val = minVal; val <= maxVal; val++) {
            if(counts.find(val) != counts.end()) {
                while(counts[val] > 0) {
                    arr[idx] = val;
                    idx++;
                    counts[val] -= 1;
                }
            }
        }
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        countSort(nums);
        return nums;
    }
};
```

### How Counting Sort Works:

1. **Count**: Count frequency of each element
2. **Reconstruct**: Place elements back in sorted order based on their counts

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

## Key Insights

1. **Merge Sort** guarantees O(n log n) time complexity and is stable
2. **Heap Sort** is in-place but not stable
3. **Counting Sort** can be very fast when the range is small
4. All three solutions meet the O(n log n) requirement for this problem

## Related Problems

- [75. Sort Colors](https://leetcode.com/problems/sort-colors/) - Counting sort variant
- [148. Sort List](https://leetcode.com/problems/sort-list/) - Merge sort on linked list
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Heap-based approach
