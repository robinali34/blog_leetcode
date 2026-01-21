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

