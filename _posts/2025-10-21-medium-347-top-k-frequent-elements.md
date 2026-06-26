---
layout: post
title: "[Medium] 347. Top K Frequent Elements"
date: 2025-10-21 16:00:00 -0700
categories: leetcode medium array hash-table heap
permalink: /posts/2025-10-21-medium-347-top-k-frequent-elements/
tags: [leetcode, medium, array, hash-table, heap, bucket-sort, quickselect]
---
**Difficulty:** Medium  
**Category:** Array, Hash Table, Heap, Bucket Sort, Quickselect  
**Companies:** Amazon, Google, Facebook, Microsoft, Apple


Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

## Examples
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

## Constraints
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

### Solution Explanation

**Approach:** Min/max heap (this problem)

**Key idea:** 1. **Bucket Sort Advantage**: Most efficient with O(n) time complexity

**How the code works:**
1. **Bucket Sort Advantage**: Most efficient with O(n) time complexity
- Heap gives fast access to min/max without full sorting.
- Size-k heap handles Top-K in O(n log k).
- Lazy deletion when elements leave the heap before removal.

**Walkthrough** — input `nums = [1,1,1,2,2,3], k = 2`, expected output `[1,2]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Approach | Time Complexity | Space Complexity | Best When |
|----------|-----------------|------------------|-----------|
| Bucket Sort | O(n) | O(n) | General purpose, optimal |
| Quickselect | O(n) avg, O(n²) worst | O(n) | Large datasets, k ≈ n |
| Min Heap | O(n log k) | O(n) | k << n, memory efficient |
| Max Heap | O(n log n) | O(n) | Simple implementation |
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

- [LC 215: Kth Largest Element in an Array](https://www.leetcode.com/problems/kth-largest-element-in-an-array/)
- [LC 973: K Closest Points to Origin](https://www.leetcode.com/problems/k-closest-points-to-origin/)
- [LC 692: Top K Frequent Words](https://www.leetcode.com/problems/top-k-frequent-words/)

## Implementation Notes

1. **Bucket Sort**: Use `vector<vector<int>>` where index represents frequency
2. **Quickselect**: Random pivot selection for better average performance
3. **Heap**: Use `priority_queue` with custom comparator for min/max heap
4. **Hash Map**: `unordered_map` for O(1) frequency counting

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Bucket Sort Advantage**: Most efficient with O(n) time complexity
2. **Frequency Range**: Maximum frequency is at most n (array length)
3. **Heap Trade-offs**: Min heap better when k is small, max heap simpler but less efficient
4. **Quickselect Optimization**: Good average case but worst case can be O(n²)

## References

- [LC 347: Top K Frequent Elements on LeetCode](https://www.leetcode.com/problems/top-k-frequent-elements/)
- [LeetCode Discuss — LC 347: Top K Frequent Elements](https://www.leetcode.com/problems/top-k-frequent-elements/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/top-k-frequent-elements/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)

## Thinking Process

1. **Bucket Sort Advantage**: Most efficient with O(n) time complexity

- Heap gives fast access to min/max without full sorting.
- Size-k heap handles Top-K in O(n log k).
- Lazy deletion when elements leave the heap before removal.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 120" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary heap</text>

  <circle cx="140" cy="35" r="16" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="39" text-anchor="middle" font-size="11">1</text>
  <circle cx="90" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="90" y="79" text-anchor="middle" font-size="10">3</text>
  <circle cx="190" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="190" y="79" text-anchor="middle" font-size="10">2</text>
  <line x1="140" y1="51" x2="90" y2="61" stroke="#9A9792"/><line x1="140" y1="51" x2="190" y2="61" stroke="#9A9792"/>
  <text x="140" y="110" text-anchor="middle" font-size="11" fill="#6B6560">parent ≤ children (min-heap)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Min/max heap** *(this problem)* | O(n log k) | O(k) | Top-K, streaming median |
| Two heaps | O(n log n) | O(n) | Median from data stream |
| Heap + lazy deletion | O(n log n) | O(n) | Delayed removal |
| Priority-driven search | O(n log n) | O(n) | Dijkstra, best-first expansion |
