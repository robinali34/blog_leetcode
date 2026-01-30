---
layout: post
title: "189. Rotate Array"
date: 2026-01-20 00:00:00 -0700
categories: [leetcode, medium, array]
permalink: /2026/01/20/medium-189-rotate-array/
tags: [leetcode, medium, array, rotation, two-pointers]
---

# 189. Rotate Array

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^9`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Rotation direction**: Which direction should we rotate - left or right? (Assumption: Rotate right by k positions - elements move to the right)

2. **In-place modification**: Should we modify the array in-place or return a new array? (Assumption: Modify in-place - O(1) extra space requirement)

3. **K larger than array size**: What if k is larger than the array length? (Assumption: Use modulo - `k % nums.length` to handle this case)

4. **Edge case - k = 0**: What should happen if k is 0? (Assumption: Array remains unchanged)

5. **Negative k**: Can k be negative? (Assumption: Based on constraints, k >= 0, but should clarify if negative k means left rotation)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Create a new array, copy elements to their rotated positions. Then copy back to original array. This requires O(n) extra space, which doesn't meet the O(1) space requirement. Alternatively, rotate one position at a time, repeating k times, but this has O(n × k) time complexity, which is too slow for large k.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a temporary array to store the last k elements, shift the first n-k elements right by k positions, then place the stored elements at the beginning. This requires O(k) extra space. Alternatively, use reverse operations: reverse entire array, then reverse first k elements and last n-k elements separately. However, need to handle k > n by using k % n.

**Step 3: Optimized Solution (8 minutes)**

Use reverse operations: first reverse the entire array, then reverse the first k elements, and finally reverse the last n-k elements. This achieves O(n) time with O(1) extra space, which is optimal. The key insight is that rotating right by k is equivalent to: reverse all, then reverse first k, then reverse last n-k. This elegant approach requires only three reverse operations and no extra space beyond a few variables.

## Solution 1: Brute Force Rotation (Simulate k Steps)

This solution rotates the array by 1 step, `k` times.

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        int temp, previous;
        for (int i = 0; i < k; i++) {
            previous = nums[nums.size() - 1];
            for (int j = 0; j < nums.size(); j++) {
                temp = nums[j];
                nums[j] = previous;
                previous = temp;
            }
        }
    }
};
```

### Explanation

- Normalize `k` with `k %= nums.size()` so that rotating by array length does nothing.
- For each of the `k` rotations:
  - Store the last element in `previous`.
  - Iterate through the array from left to right, swapping each element with `previous`.
  - This effectively shifts all elements to the right by 1, with the last element moved to the front.

### Complexity

- **Time Complexity:** O(n × k) — For each of the `k` steps, we traverse `n` elements.
- **Space Complexity:** O(1) — Only a few extra variables.

This approach is simple but can be too slow when `k` and `n` are large.

## Solution 2: Reverse Array Trick (Optimal)

We can rotate the array in-place using the **reverse** operation three times:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n - k` elements.

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        const int N = nums.size();
        k %= N;
        reverse(nums, 0, N - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, N - 1);
    }
private:
    void reverse(vector<int>& nums, int start, int end) {
        while(start < end) {
            int tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start++;
            end--;
        }
    }
};
```

### Why This Works

Let the array be split into two parts with respect to rotation by `k`:
- Original: `[A B]` where `A` is the first `n-k` elements, `B` is the last `k` elements.
- Rotated: `[B A]`.

The reverse trick does:
1. Reverse `[A B]` → `[B^R A^R]` (both parts reversed, order swapped)
2. Reverse `B^R` back to `B` → `[B A^R]`
3. Reverse `A^R` back to `A` → `[B A]`

### Complexity

- **Time Complexity:** O(n) — Each element is moved a constant number of times.
- **Space Complexity:** O(1) — In-place, using only a few extra variables.

## Comparison of Approaches

| Approach                    | Time Complexity | Space Complexity | Notes                          |
|----------------------------|-----------------|------------------|--------------------------------|
| Brute Force (k simulations)| O(n × k)        | O(1)             | Simple but slow for large k,n |
| Reverse Array (Optimal)    | O(n)            | O(1)             | Recommended in interviews      |

## Edge Cases

1. `k = 0` → Array remains unchanged.
2. `k` multiple of `n` → Array remains unchanged after normalization with `k %= n`.
3. Single element array → Always unchanged.
4. Large `k` (e.g., `k > n`) → Handled by `k %= n`.

## Related Problems

- [LC 61. Rotate List](https://leetcode.com/problems/rotate-list/)
- [LC 189. Rotate Array](https://leetcode.com/problems/rotate-array/) — This problem
- [LC 396. Rotate Function](https://leetcode.com/problems/rotate-function/)

