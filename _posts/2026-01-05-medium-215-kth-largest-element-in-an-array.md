---
layout: post
title: "[Medium] 215. Kth Largest Element in an Array"
date: 2026-01-05 00:00:00 -0700
categories: [leetcode, medium, array, heap, quickselect, divide-and-conquer]
permalink: /2026/01/05/medium-215-kth-largest-element-in-an-array/
tags: [leetcode, medium, array, heap, priority-queue, quickselect, divide-and-conquer, sorting]
---
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

## Thinking Process

1. **Min Heap Pattern**: Use min heap to maintain k largest elements

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

## Solution

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

### Why Min Heap for K Largest?

- **Min heap** keeps the **smallest** element at the top
- By maintaining size `k`, we keep the `k` largest elements
- The top element is the smallest among the `k` largest, which is the `kth` largest overall

### Detailed Walkthrough: Min Heap Example

Let's trace through an example to understand how the min heap solution works:

**Input:** `nums = [3, 2, 1, 5, 6, 4]`, `k = 2` (find 2nd largest)

**Goal:** Maintain a min heap of size 2 containing the 2 largest elements.

**Step-by-step execution:**

1. **Initialize:** `minHeap = []` (empty)

2. **Process 3:**
   - Push 3: `minHeap = [3]`
   - Size = 1 ≤ 2, no pop needed
   - Heap: `[3]` (top: 3)

3. **Process 2:**
   - Push 2: `minHeap = [2, 3]` (min heap: 2 at top)
   - Size = 2 ≤ 2, no pop needed
   - Heap: `[2, 3]` (top: 2)

4. **Process 1:**
   - Push 1: `minHeap = [1, 3, 2]` → heapify → `[1, 2, 3]`
   - Size = 3 > 2, pop smallest: remove 1
   - Heap: `[2, 3]` (top: 2)
   - **Note:** We removed 1 (smallest), keeping the 2 largest so far: [2, 3]

5. **Process 5:**
   - Push 5: `minHeap = [2, 3, 5]` → heapify → `[2, 3, 5]`
   - Size = 3 > 2, pop smallest: remove 2
   - Heap: `[3, 5]` (top: 3)
   - **Note:** We removed 2 (smallest), keeping the 2 largest so far: [3, 5]

6. **Process 6:**
   - Push 6: `minHeap = [3, 5, 6]` → heapify → `[3, 5, 6]`
   - Size = 3 > 2, pop smallest: remove 3
   - Heap: `[5, 6]` (top: 5)
   - **Note:** We removed 3 (smallest), keeping the 2 largest so far: [5, 6]

7. **Process 4:**
   - Push 4: `minHeap = [4, 5, 6]` → heapify → `[4, 5, 6]`
   - Size = 3 > 2, pop smallest: remove 4
   - Heap: `[5, 6]` (top: 5)
   - **Note:** We removed 4 (smallest), keeping the 2 largest: [5, 6]

8. **Result:**
   - Final heap: `[5, 6]` (top: 5)
   - Return `minHeap.top()` = **5** ✓ (2nd largest)

**Visual representation:**

```
After each step:
Step 1: [3]                    → Keep: [3]
Step 2: [2, 3]                 → Keep: [2, 3]
Step 3: [1, 2, 3] → pop 1      → Keep: [2, 3]
Step 4: [2, 3, 5] → pop 2      → Keep: [3, 5]
Step 5: [3, 5, 6] → pop 3      → Keep: [5, 6]
Step 6: [4, 5, 6] → pop 4      → Keep: [5, 6]

Final: Top of heap = 5 (2nd largest)
```

**Key Insight:**

- **Min heap** keeps the **smallest** element at the top
- By maintaining exactly `k` elements, we keep the `k` largest elements
- When size exceeds `k`, we remove the smallest (which is the top)
- After processing all elements, the top is the `kth` largest

## Follow-up Questions

- What if we need to handle dynamic updates (add/remove elements)?
- How would you optimize for very large datasets that don't fit in memory?
- What if we need the k largest elements in sorted order?

## Related Problems

- [LC 347: Top K Frequent Elements](https://www.leetcode.com/problems/top-k-frequent-elements/) - Similar heap pattern
- [LC 973: K Closest Points to Origin](https://www.leetcode.com/problems/k-closest-points-to-origin/) - K selection with custom comparator
- [LC 703: Kth Largest Element in a Stream](https://www.leetcode.com/problems/kth-largest-element-in-a-stream/) - Dynamic version
- [LC 378: Kth Smallest Element in a Sorted Matrix](https://www.leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) - 2D variant

## Implementation Notes

1. **Min Heap**: Use `priority_queue<int, vector<int>, greater<>>` for min heap
2. **QuickSelect**: Use Hoare's partition for better performance
3. **Randomization**: For QuickSelect, randomize pivot to avoid worst case
4. **Edge Cases**: Handle k = 1, k = n, and single element arrays

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Min Heap Pattern**: Use min heap to maintain k largest elements
2. **QuickSelect**: Partition-based selection avoids full sorting
3. **Index Conversion**: kth largest = (n-k)th smallest in sorted array
4. **Space Trade-off**: Heap uses O(k) space, QuickSelect uses O(1) space

## References

- [LC 215: Kth Largest Element in an Array on LeetCode](https://www.leetcode.com/problems/kth-largest-element-in-an-array/)
- [LeetCode Discuss — LC 215: Kth Largest Element in an Array](https://www.leetcode.com/problems/kth-largest-element-in-an-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/kth-largest-element-in-an-array/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
