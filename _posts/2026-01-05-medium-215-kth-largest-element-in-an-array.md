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

### Detailed Walkthrough: QuickSelect Example

Let's trace through an example to understand how QuickSelect works:

**Input:** `nums = [3, 2, 1, 5, 6, 4]`, `k = 2` (find 2nd largest)

**Step 1: Convert kth largest to position**
- Array size: `N = 6`
- 2nd largest = (6-2)th smallest = 4th smallest (0-indexed: position 4)
- We need to find element at position 4 in sorted order

**Step 2: Initial Call**
```
quickSelect([3,2,1,5,6,4], l=0, r=5, k=4)
```

**Step 3: First Partition (l=0, r=5, k=4)**

**Initial state:**
```
Array: [3, 2, 1, 5, 6, 4]
       l=0              r=5
       pivot = nums[0] = 3
       i = -1, j = 6
```

**Hoare's Partition Process:**

1. **Move i right** until `nums[i] >= pivot`:
   - `i = 0`: `nums[0] = 3 >= 3` ✓ (stop)

2. **Move j left** until `nums[j] <= pivot`:
   - `j = 5`: `nums[5] = 4 > 3` (continue)
   - `j = 4`: `nums[4] = 6 > 3` (continue)
   - `j = 3`: `nums[3] = 5 > 3` (continue)
   - `j = 2`: `nums[2] = 1 <= 3` ✓ (stop)

3. **Check if i < j**: `0 < 2` ✓, so swap:
   ```
   Array: [1, 2, 3, 5, 6, 4]
          i=0      j=2
   ```

4. **Continue loop**:
   - Move i right: `i = 1`: `nums[1] = 2 < 3` (continue)
   - `i = 2`: `nums[2] = 3 >= 3` ✓ (stop)
   - Move j left: `j = 1`: `nums[1] = 2 <= 3` ✓ (stop)
   - Check: `2 < 1` ✗ (loop ends)

**After partition:**
```
Array: [1, 2, 3, 5, 6, 4]
       l=0  j=1  i=2  r=5
       
Left partition (l to j): [1, 2]  (elements <= pivot)
Right partition (j+1 to r): [3, 5, 6, 4]  (elements > pivot)
Pivot position: j = 1
```

**Step 4: Decide which partition to recurse**

- `k = 4`, `j = 1`
- Check: `k <= j`? `4 <= 1`? ✗ (False)
- So we recurse on **right partition**: `quickSelect(nums, j+1=2, r=5, k=4)`

**Step 5: Second Partition (l=2, r=5, k=4)**

**State:**
```
Array: [1, 2, 3, 5, 6, 4]
              l=2      r=5
              pivot = nums[2] = 3
              i = 1, j = 6
```

**Partition Process:**

1. Move i right: `i = 2`: `nums[2] = 3 >= 3` ✓
2. Move j left:
   - `j = 5`: `nums[5] = 4 > 3` (continue)
   - `j = 4`: `nums[4] = 6 > 3` (continue)
   - `j = 3`: `nums[3] = 5 > 3` (continue)
   - `j = 2`: `nums[2] = 3 <= 3` ✓
3. Check: `2 < 2` ✗ (no swap, loop ends immediately)

**After partition:**
```
Array: [1, 2, 3, 5, 6, 4]
              l=2  j=2  r=5
              
Left partition: [] (empty)
Right partition: [3, 5, 6, 4]
```

**Step 6: Decide which partition**

- `k = 4`, `j = 2`
- Check: `k <= j`? `4 <= 2`? ✗ (False)
- Recurse on right: `quickSelect(nums, j+1=3, r=5, k=4)`

**Step 7: Third Partition (l=3, r=5, k=4)**

**State:**
```
Array: [1, 2, 3, 5, 6, 4]
                 l=3  r=5
                 pivot = nums[3] = 5
                 i = 2, j = 6
```

**Partition Process:**

1. Move i right: `i = 3`: `nums[3] = 5 >= 5` ✓
2. Move j left:
   - `j = 5`: `nums[5] = 4 <= 5` ✓
3. Check: `3 < 5` ✓, swap:
   ```
   Array: [1, 2, 3, 4, 6, 5]
                      i=3  j=5
   ```
4. Continue:
   - Move i right: `i = 4`: `nums[4] = 6 >= 5` ✓
   - Move j left: `j = 4`: `nums[4] = 6 > 5` (continue)
   - `j = 3`: `nums[3] = 4 <= 5` ✓
   - Check: `4 < 3` ✗ (loop ends)

**After partition:**
```
Array: [1, 2, 3, 4, 6, 5]
                 l=3  j=3  i=4  r=5
                 
Left partition: [4] (elements <= 5)
Right partition: [6, 5] (elements > 5)
```

**Step 8: Decide which partition**

- `k = 4`, `j = 3`
- Check: `k <= j`? `4 <= 3`? ✗ (False)
- Recurse on right: `quickSelect(nums, j+1=4, r=5, k=4)`

**Step 9: Fourth Partition (l=4, r=5, k=4)**

**State:**
```
Array: [1, 2, 3, 4, 6, 5]
                    l=4  r=5
                    pivot = nums[4] = 6
                    i = 3, j = 6
```

**Partition Process:**

1. Move i right: `i = 4`: `nums[4] = 6 >= 6` ✓
2. Move j left:
   - `j = 5`: `nums[5] = 5 <= 6` ✓
3. Check: `4 < 5` ✓, swap:
   ```
   Array: [1, 2, 3, 4, 5, 6]
                       i=4  j=5
   ```
4. Continue:
   - Move i right: `i = 5`: `nums[5] = 6 >= 6` ✓
   - Move j left: `j = 4`: `nums[4] = 5 <= 6` ✓
   - Check: `5 < 4` ✗ (loop ends)

**After partition:**
```
Array: [1, 2, 3, 4, 5, 6]
                    l=4  j=4  i=5  r=5
                    
Left partition: [5] (elements <= 6)
Right partition: [6] (elements > 6)
```

**Step 10: Decide which partition**

- `k = 4`, `j = 4`
- Check: `k <= j`? `4 <= 4`? ✓ (True!)
- Recurse on left: `quickSelect(nums, l=4, j=4, k=4)`

**Step 11: Base Case**

```
quickSelect(nums, l=4, r=4, k=4)
Check: l == r? 4 == 4? ✓
Return: nums[4] = 5
```

**Result:** The 2nd largest element is **5** ✓

### Understanding Hoare's Partition

**Key Points:**

1. **Two Pointers**: `i` starts before left, `j` starts after right
2. **Move i right**: Until finding element `>= pivot`
3. **Move j left**: Until finding element `<= pivot`
4. **Swap if needed**: If `i < j`, swap elements at i and j
5. **Final position**: After loop, `j` is the last position of left partition
6. **Partition property**: 
   - Elements at positions `[l, j]` are `<= pivot`
   - Elements at positions `[j+1, r]` are `> pivot`

**Why this works:**

- We only recurse on the partition containing our target position `k`
- Each partition eliminates roughly half the elements on average
- We never need to fully sort the array, just find the element at position `k`

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

