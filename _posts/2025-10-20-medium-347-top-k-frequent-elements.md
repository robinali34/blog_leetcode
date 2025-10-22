---
layout: post
title: "LC 347: Top K Frequent Elements"
date: 2025-10-20 16:00:00 -0700
categories: leetcode medium array hash-table heap
permalink: /posts/2025-10-20-medium-347-top-k-frequent-elements/
tags: [leetcode, medium, array, hash-table, heap, bucket-sort, quickselect]
---

# LC 347: Top K Frequent Elements

**Difficulty:** Medium  
**Category:** Array, Hash Table, Heap, Bucket Sort, Quickselect  
**Companies:** Amazon, Google, Facebook, Microsoft, Apple

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

### Examples

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

### Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`
- It is **guaranteed** that the answer is **unique**

## Solution Approaches

### Approach 1: Bucket Sort (Optimal)

**Algorithm:**
1. Count frequency of each element using hash map
2. Create buckets where index represents frequency
3. Iterate buckets from highest to lowest frequency
4. Collect elements until we have k elements

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(auto& num: nums) freq[num]++;

        int n = nums.size();
        vector<vector<int>> buckets(n + 1);
        for(auto& [num, count]: freq) {
            buckets[count].push_back(num);
        }
        vector<int> rtn;
        for(int i = n; i >= 0 && rtn.size() < k; i--) {
            for(int num: buckets[i]) {
                rtn.push_back(num);
                if(rtn.size() == k) break;
            }
        }
        return rtn;
    }
};
```

### Approach 2: Quickselect

**Algorithm:**
1. Count frequency of each element
2. Create array of unique elements
3. Use quickselect to find k-th largest frequency
4. Return elements with frequencies >= k-th largest

**Time Complexity:** O(n) average, O(n²) worst case  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        for(int n : nums) {
            count_map[n] += 1;
        }
        int n = count_map.size();
        for(pair<int, int> p: count_map) {
            unique.push_back(p.first);
        }
        quickselect(0, n - 1, n - k);
        vector<int> top_k_frequent(k);
        copy(unique.begin() + n - k, unique.end(), top_k_frequent.begin());
        return top_k_frequent;
    }

private:
    vector<int> unique;
    map<int, int> count_map;

    int partition(int left, int right, int pivot) {
        int pivot_freq = count_map[unique[pivot]];
        swap(unique[pivot], unique[right]);

        int store_idx = left;
        for(int i = left; i < right; i++) {
            if(count_map[unique[i]] < pivot_freq) {
                swap(unique[store_idx], unique[i]);
                store_idx += 1;
            }
        }
        swap(unique[right], unique[store_idx]);
        return store_idx;
    }

    void quickselect(int left, int right, int k_smallest){
        if(left == right) return;
        int pivot = left + rand() % (right - left + 1);
        pivot = partition(left, right, pivot);
        if(k_smallest == pivot) {
            return;
        } else if(k_smallest < pivot) {
            quickselect(left, pivot - 1, k_smallest);
        } else {
            quickselect(pivot + 1, right, k_smallest);
        }
    }
};
```

### Approach 3: Min Heap

**Algorithm:**
1. Count frequency of each element
2. Use min heap of size k to maintain top k frequent elements
3. For each element, if heap size < k, add it
4. If heap size = k and current element has higher frequency than minimum in heap, replace it

**Time Complexity:** O(n log k)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(int num : nums) {
            freq[num]++;
        }
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        
        for(auto& [num, count] : freq) {
            if(minHeap.size() < k) {
                minHeap.push({count, num});
            } else if(count > minHeap.top().first) {
                minHeap.pop();
                minHeap.push({count, num});
            }
        }
        
        vector<int> result;
        while(!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return result;
    }
};
```

### Approach 4: Max Heap

**Algorithm:**
1. Count frequency of each element
2. Use max heap to store all elements with their frequencies
3. Extract top k elements from heap

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(int num : nums) {
            freq[num]++;
        }
        
        priority_queue<pair<int, int>> maxHeap;
        for(auto& [num, count] : freq) {
            maxHeap.push({count, num});
        }
        
        vector<int> result;
        for(int i = 0; i < k; i++) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return result;
    }
};
```

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Best When |
|----------|-----------------|------------------|-----------|
| Bucket Sort | O(n) | O(n) | General purpose, optimal |
| Quickselect | O(n) avg, O(n²) worst | O(n) | Large datasets, k ≈ n |
| Min Heap | O(n log k) | O(n) | k << n, memory efficient |
| Max Heap | O(n log n) | O(n) | Simple implementation |

## Key Insights

1. **Bucket Sort Advantage**: Most efficient with O(n) time complexity
2. **Frequency Range**: Maximum frequency is at most n (array length)
3. **Heap Trade-offs**: Min heap better when k is small, max heap simpler but less efficient
4. **Quickselect Optimization**: Good average case but worst case can be O(n²)

## Algorithm Comparison

### Bucket Sort vs Heap Approaches

**Bucket Sort:**
- ✅ O(n) time complexity
- ✅ Simple implementation
- ❌ Uses O(n) extra space for buckets

**Min Heap:**
- ✅ O(n log k) time, good when k << n
- ✅ Memory efficient
- ❌ More complex implementation

**Max Heap:**
- ✅ Simple implementation
- ❌ O(n log n) time complexity
- ❌ Less efficient than min heap

## Follow-up Questions

- What if we need to handle dynamic updates (add/remove elements)?
- How would you optimize for very large datasets that don't fit in memory?
- What if we need the k most frequent elements in sorted order by frequency?

## Related Problems

- [LC 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [LC 973: K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- [LC 692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

## Implementation Notes

1. **Bucket Sort**: Use `vector<vector<int>>` where index represents frequency
2. **Quickselect**: Random pivot selection for better average performance
3. **Heap**: Use `priority_queue` with custom comparator for min/max heap
4. **Hash Map**: `unordered_map` for O(1) frequency counting

---

*This problem demonstrates the importance of choosing the right algorithm based on constraints and requirements. Bucket sort provides optimal O(n) solution for this specific problem.*
