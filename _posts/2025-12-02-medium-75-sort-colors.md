---
layout: post
title: "[Medium] 75. Sort Colors"
date: 2025-12-02 00:00:00 -0800
categories: leetcode algorithm medium cpp array two-pointers sorting problem-solving
---

# [Medium] 75. Sort Colors

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

## Examples

**Example 1:**
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Example 2:**
```
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## Solution: Dutch National Flag Algorithm (Two Pointers)

**Time Complexity:** O(n) - Single pass through the array  
**Space Complexity:** O(1) - In-place sorting with only constant extra space

The Dutch National Flag algorithm uses two pointers to partition the array into three regions:
- **Left region (0s)**: `[0, p0)`
- **Middle region (1s)**: `[p0, i)`
- **Right region (2s)**: `(p2, n-1]`

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int p0 = 0, p2 = n - 1;
        
        for(int i = 0; i <= p2; i++) {
            while(i <= p2 && nums[i] == 2) {
                swap(nums[i], nums[p2]);
                p2--;
            }
            
            if(nums[i] == 0) {
                swap(nums[i], nums[p0]);
                p0++;
            }
        }
    }
};
```

## How the Algorithm Works

### Key Insight: Three-Way Partitioning

The algorithm maintains three regions:
1. **0s region**: All elements before `p0` are 0s
2. **1s region**: Elements between `p0` and `i` are 1s (or being processed)
3. **2s region**: All elements after `p2` are 2s

### Algorithm Steps

1. **Initialize pointers**:
   - `p0 = 0`: Next position to place a 0
   - `p2 = n - 1`: Next position to place a 2
   - `i = 0`: Current element being processed

2. **Process each element**:
   - If `nums[i] == 2`: Swap with `nums[p2]` and decrement `p2` (use `while` to handle swapped 2s)
   - If `nums[i] == 0`: Swap with `nums[p0]` and increment `p0`
   - If `nums[i] == 1`: Leave it (it's in the correct region), increment `i`

3. **Termination**: When `i > p2`, all elements are processed

### Why the `while` Loop for 2s?

When we swap `nums[i]` with `nums[p2]`, the element at `p2` might be a 2. We need to keep swapping until `nums[i]` is not 2, otherwise we might leave a 2 in the wrong position.

### Example Walkthrough

**Input:** `nums = [2,0,2,1,1,0]`

```
Initial: [2, 0, 2, 1, 1, 0]
         i=0              p2=5, p0=0

i=0: nums[0]=2, swap with nums[5]=0
     [0, 0, 2, 1, 1, 2]
     i=0              p2=4, p0=0
     nums[0]=0, swap with nums[0] (no change), p0=1

i=1: nums[1]=0, swap with nums[1] (no change), p0=2

i=2: nums[2]=2, swap with nums[4]=1
     [0, 0, 1, 1, 2, 2]
     i=2          p2=3, p0=2
     nums[2]=1, leave it

i=3: nums[3]=1, leave it
     i=3 > p2=3, done

Result: [0, 0, 1, 1, 2, 2] ✓
```

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Single pass | O(n) | O(1) |
| Swaps | O(n) worst case | - |
| **Overall** | **O(n)** | **O(1)** |

## Key Points

1. **In-place sorting**: No extra space needed (except for variables)
2. **Single pass**: Each element is visited at most twice
3. **Two pointers**: `p0` for 0s, `p2` for 2s
4. **While loop for 2s**: Ensures swapped 2s are handled correctly
5. **Order matters**: Handle 2s first (with while), then 0s

## Edge Cases

1. **All same color**: `[0,0,0]`, `[1,1,1]`, `[2,2,2]`
2. **Already sorted**: `[0,1,2]`
3. **Reverse sorted**: `[2,1,0]`
4. **Single element**: `[1]`

## Common Mistakes

1. **Not using `while` for 2s**: If you use `if`, swapped 2s might be left in wrong position
2. **Wrong loop condition**: Must use `i <= p2`, not `i < n`
3. **Incrementing `i` after swapping 0**: After swapping with `p0`, we should increment `i` (which happens naturally in the for loop)
4. **Not handling swapped 2s**: The `while` loop is crucial for correctness

## Alternative Approach: Counting Sort

For this specific problem (only 3 values), we could use counting sort:

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0};
        for(int num : nums) count[num]++;
        
        int idx = 0;
        for(int color = 0; color < 3; color++) {
            while(count[color]-- > 0) {
                nums[idx++] = color;
            }
        }
    }
};
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1) - Only 3 counters

However, the two-pointer approach is more general and can be extended to partition problems.

## Related Problems

- [324. Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) - Uses 3-way partition
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Partitioning
- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) - General sorting
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) - Two-pointer partitioning

## Pattern Recognition

This problem demonstrates the **"Two-Pointer Partitioning"** pattern:

```
1. Use two pointers to maintain boundaries
2. Process elements in a single pass
3. Swap elements to move them to correct regions
4. Handle edge cases (like swapped values) carefully
```

Similar problems:
- Partition array by value
- Move specific elements to one side
- Three-way partitioning

