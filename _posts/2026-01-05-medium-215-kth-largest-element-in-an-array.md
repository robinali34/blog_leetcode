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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Kth largest definition**: How is "kth largest" defined? (Assumption: When sorted in descending order, the element at position k-1 (1-indexed kth largest))

2. **Duplicate handling**: How should we handle duplicate values? (Assumption: Duplicates are counted separately - if [3,2,3,1], 1st largest is 3, 2nd is 3, 3rd is 2)

3. **Array modification**: Can we modify the input array? (Assumption: Typically yes - QuickSelect modifies array, but should clarify)

4. **K validity**: Is k guaranteed to be valid? (Assumption: Yes - per constraints, 1 <= k <= nums.length)

5. **Return value**: Should we return the value or the index? (Assumption: Return the value - integer representing kth largest element)

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

### Example Walkthrough

**Input:**
```
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
```

**We search for index:**
```
N - k = 9 - 4 = 5
```

**First call:**
```
quickSelect(nums, l=0, r=8, k=5)
pivot = nums[0] = 3
i = -1, j = 9 (initial)
```

**Partition process:**
- Move i right: i=0 (nums[0]=3 >= 3)
- Move j left: j=8 (nums[8]=6 > 3), j=7 (nums[7]=5 > 3), j=6 (nums[6]=5 > 3), j=5 (nums[5]=4 > 3), j=4 (nums[4]=2 <= 3)
- Swap nums[0] and nums[4]
- Continue: i=1 (nums[1]=2 < 3), i=2 (nums[2]=3 >= 3)
- Continue: j=3 (nums[3]=1 <= 3)
- Swap nums[2] and nums[3]
- Continue: i=3 (nums[3]=3 >= 3)
- Continue: j=2 (nums[2]=1 <= 3)
- Loop ends: i=3, j=2

**After partition:**
```
[2, 2, 1, 3, 3 | 4, 5, 5, 6]
 l=0        j=2  i=3      r=8
```

```
l=0, r=8, j=2, k=5
k > j → search right side [j+1, r] = [3, 8]
```

**Second call:**
```
quickSelect(nums, l=3, r=8, k=5)
pivot = nums[3] = 3
i = 2, j = 9 (initial)
```

**Partition process:**
- Move i right: i=3 (nums[3]=3 >= 3)
- Move j left: j=8 (nums[8]=6 > 3), j=7 (nums[7]=5 > 3), j=6 (nums[6]=5 > 3), j=5 (nums[5]=4 > 3), j=4 (nums[4]=3 <= 3)
- Loop ends: i=3, j=4

**After partition:**
```
[2, 2, 1, 3, 3 | 4, 5, 5, 6]
            l=3  j=4  i=5  r=8
```

```
l=3, r=8, j=4, k=5
k > j → search right side [j+1, r] = [5, 8]
```

**Third call:**
```
quickSelect(nums, l=5, r=8, k=5)
pivot = nums[5] = 4
i = 4, j = 9 (initial)
```

**Partition process:**
- Move i right: i=5 (nums[5]=4 >= 4)
- Move j left: j=8 (nums[8]=6 > 4), j=7 (nums[7]=5 > 4), j=6 (nums[6]=5 > 4), j=5 (nums[5]=4 <= 4)
- Loop ends: i=5, j=5

**After partition:**
```
[2, 2, 1, 3, 3, 4 | 5, 5, 6]
                l=5  j=5  i=6  r=8
```

```
l=5, r=8, j=5, k=5
k <= j → search left side [l, j] = [5, 5]
```

**Base case:**
```
quickSelect(nums, l=5, r=5, k=5)
l == r == 5
return nums[5] = 4
```

**✅ Answer = 4**

### Runtime Analysis

**Why QuickSelect is O(n) Average Case:**

1. **Each Partition Step is O(m) where m is the subarray size:**
   - **First call**: Partitions 9 elements → O(9) time
   - **Second call**: Partitions 6 elements → O(6) time  
   - **Third call**: Partitions 4 elements → O(4) time
   - Each partition makes a single pass through the subarray using two pointers (i and j)
   - Time per partition = size of subarray being partitioned

2. **Why the total is O(n) and not O(n²):**
   - **Key insight**: We only recurse on ONE partition (the one containing k), not both
   - On average, each partition eliminates roughly **half** the elements
   - The subarray sizes form a **geometric series**: n + n/2 + n/4 + n/8 + ...
   - **Geometric series sum**: n × (1 + 1/2 + 1/4 + 1/8 + ...) = n × 2 = **O(n)**
   - In our example: 9 + 6 + 4 = 19 ≈ 2n (where n=9)

3. **Why worst case is O(n²):**
   - If pivot is always the smallest/largest element, we eliminate only 1 element per partition
   - Subarray sizes: n + (n-1) + (n-2) + ... = n(n+1)/2 = **O(n²)**
   - Can be avoided by randomizing the pivot selection

4. **Space Complexity:**
   - **O(1)** extra space per recursive call (only storing l, r, k, pivot, i, j)
   - **Recursion stack**: O(log n) average depth, O(n) worst case
   - Total space: O(log n) average, O(n) worst case

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

