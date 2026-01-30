---
layout: post
title: "238. Product of Array Except Self"
date: 2026-01-27 00:00:00 -0700
categories: [leetcode, medium, array, prefix-sum, two-pointers]
permalink: /2026/01/27/medium-238-product-of-array-except-self/
tags: [leetcode, medium, array, prefix-sum, two-pointers]
---

# 238. Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operator.

## Examples

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a **32-bit** integer.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Division operator**: Can we use the division operator? (Assumption: No - the problem explicitly states we cannot use division)

2. **Zero handling**: How should we handle arrays containing zeros? (Assumption: The product of prefix/suffix is guaranteed to fit in 32-bit integer, but we need to handle zeros carefully without division)

3. **Output format**: Should we return a new array or modify the input array in-place? (Assumption: Return a new array `answer`)

4. **Edge case - single element**: What if the array has only 2 elements? (Assumption: For `[a, b]`, return `[b, a]`)

5. **Integer overflow**: Are we guaranteed that the product won't overflow, or should we handle potential overflow? (Assumption: The problem guarantees products fit in 32-bit integer, but we should still be careful with intermediate calculations)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For each position i, calculate the product of all other elements by iterating through the array and multiplying all elements except nums[i]. This straightforward approach has O(n²) time complexity, which is too slow for large arrays. The challenge is avoiding division while computing products efficiently.

**Step 2: Semi-Optimized Approach (7 minutes)**

Calculate the total product of all elements, then for each position i, divide by nums[i] to get the product except self. However, the problem explicitly forbids using division. Alternatively, use two arrays: one storing prefix products (product of all elements before i) and another storing suffix products (product of all elements after i). Then multiply prefix[i] × suffix[i] for each position. This achieves O(n) time with O(n) space.

**Step 3: Optimized Solution (8 minutes)**

Use the output array itself to store prefix products in the first pass. Then, in a second pass from right to left, maintain a running suffix product and multiply it with the prefix product already stored in the output array. This achieves O(n) time with O(1) extra space (excluding the output array). The key insight is reusing the output array to store intermediate results, eliminating the need for separate prefix and suffix arrays.

## Solution Approach

This problem requires computing the product of all elements except the current one. The key challenge is doing this in O(n) time without using division.

### Key Insights:

1. **Left and Right Products**: For each index `i`, we need:
   - Product of all elements to the left: `nums[0] * nums[1] * ... * nums[i-1]`
   - Product of all elements to the right: `nums[i+1] * nums[i+2] * ... * nums[n-1]`
   - Final answer: `left[i] * right[i]`

2. **Two-Pass Approach**: 
   - First pass: Build left products array
   - Second pass: Build right products array
   - Third pass: Multiply left and right products

3. **Space Optimization**: Can be done with O(1) extra space (excluding output array) by using the output array itself

## Solution: Left and Right Product Arrays

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> L(len, 0), R(len, 0);
        vector<int> answer(len);

        L[0] = 1;
        for (int i = 1; i < len; i++) {
            L[i] = nums[i - 1] * L[i - 1];
        }

        R[len - 1] = 1;
        for (int i = len - 2; i >= 0; i--) {
            R[i] = nums[i + 1] * R[i + 1];
        }
        
        for (int i = 0; i < len; i++){
            answer[i] = L[i] * R[i];
        }
        return answer;
    }
};
```

### Algorithm Explanation:

#### **Step 1: Build Left Products Array**

```cpp
L[0] = 1;
for (int i = 1; i < len; i++) {
    L[i] = nums[i - 1] * L[i - 1];
}
```

- `L[i]` = product of all elements to the left of index `i`
- `L[0] = 1` (no elements to the left)
- `L[1] = nums[0]`
- `L[2] = nums[0] * nums[1]`
- `L[3] = nums[0] * nums[1] * nums[2]`
- ...

#### **Step 2: Build Right Products Array**

```cpp
R[len - 1] = 1;
for (int i = len - 2; i >= 0; i--) {
    R[i] = nums[i + 1] * R[i + 1];
}
```

- `R[i]` = product of all elements to the right of index `i`
- `R[len-1] = 1` (no elements to the right)
- `R[len-2] = nums[len-1]`
- `R[len-3] = nums[len-1] * nums[len-2]`
- `R[0] = nums[len-1] * nums[len-2] * ... * nums[1]`
- ...

#### **Step 3: Multiply Left and Right Products**

```cpp
for (int i = 0; i < len; i++){
    answer[i] = L[i] * R[i];
}
```

- For each index `i`, multiply left product and right product
- `answer[i] = L[i] * R[i]` = product of all elements except `nums[i]`

### Example Walkthrough:

**Input:** `nums = [1,2,3,4]`

```
Step 1: Build left products
  L[0] = 1
  L[1] = nums[0] * L[0] = 1 * 1 = 1
  L[2] = nums[1] * L[1] = 2 * 1 = 2
  L[3] = nums[2] * L[2] = 3 * 2 = 6
  L = [1, 1, 2, 6]

Step 2: Build right products
  R[3] = 1
  R[2] = nums[3] * R[3] = 4 * 1 = 4
  R[1] = nums[2] * R[2] = 3 * 4 = 12
  R[0] = nums[1] * R[1] = 2 * 12 = 24
  R = [24, 12, 4, 1]

Step 3: Multiply left and right
  answer[0] = L[0] * R[0] = 1 * 24 = 24
  answer[1] = L[1] * R[1] = 1 * 12 = 12
  answer[2] = L[2] * R[2] = 2 * 4 = 8
  answer[3] = L[3] * R[3] = 6 * 1 = 6
  answer = [24, 12, 8, 6] ✓
```

**Verification:**
- `answer[0] = 24` = `2 * 3 * 4` ✓ (product except `nums[0] = 1`)
- `answer[1] = 12` = `1 * 3 * 4` ✓ (product except `nums[1] = 2`)
- `answer[2] = 8` = `1 * 2 * 4` ✓ (product except `nums[2] = 3`)
- `answer[3] = 6` = `1 * 2 * 3` ✓ (product except `nums[3] = 4`)

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Building left products: O(n)
  - Building right products: O(n)
  - Multiplying products: O(n)
  - Overall: O(n)

- **Space Complexity:** O(n)
  - Left products array: O(n)
  - Right products array: O(n)
  - Output array: O(n)
  - Overall: O(n)

## Space-Optimized Solution

We can optimize space by using the output array itself to store left products, then building right products on the fly:

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> answer(len, 1);
        
        // Build left products in answer array
        for (int i = 1; i < len; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }
        
        // Build right products on the fly and multiply
        int right = 1;
        for (int i = len - 1; i >= 0; i--) {
            answer[i] *= right;
            right *= nums[i];
        }
        
        return answer;
    }
};
```

**Space Complexity:** O(1) extra space (excluding output array)

## Key Insights

1. **Two Arrays Approach**: Use separate arrays for left and right products for clarity

2. **Space Optimization**: Can use output array to store left products, then build right products on the fly

3. **No Division**: Avoids division operator, which would fail with zeros

4. **Handles Zeros**: Works correctly even when array contains zeros

5. **Prefix/Suffix Products**: Similar to prefix sum, but with multiplication

## Edge Cases

1. **Two elements**: `nums = [2, 3]` → `answer = [3, 2]`
2. **Contains zero**: `nums = [-1,1,0,-3,3]` → `answer = [0,0,9,0,0]`
3. **All same**: `nums = [2,2,2]` → `answer = [4,4,4]`
4. **Negative numbers**: `nums = [-1,2,-3,4]` → `answer = [24,-12,8,-6]`
5. **Single zero**: `nums = [1,0,3,4]` → `answer = [0,12,0,0]`

## Common Mistakes

1. **Using division**: `answer[i] = totalProduct / nums[i]` fails with zeros
2. **Wrong initialization**: Forgetting to set `L[0] = 1` and `R[len-1] = 1`
3. **Index off-by-one**: Confusing left/right boundaries
4. **Integer overflow**: Not considering product might exceed 32-bit (but constraints guarantee it won't)
5. **Space optimization**: Not realizing we can use output array for left products

## Comparison with Alternative Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Left/Right Arrays** | O(n) | O(n) | Clear and intuitive |
| **Space-Optimized** | O(n) | O(1) | Uses output array |
| **Division (Invalid)** | O(n) | O(1) | Fails with zeros |

## Related Problems

- [LC 42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) - Similar left/right pass pattern
- [LC 135: Candy](https://leetcode.com/problems/candy/) - Left and right passes
- [LC 2256: Minimum Average Difference](https://leetcode.com/problems/minimum-average-difference/) - Prefix and suffix sums
- [LC 724: Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) - Left and right sums

---

*This problem demonstrates the **left and right product arrays** technique, which is useful for problems requiring prefix/suffix computations. The key insight is breaking the problem into two parts: products to the left and products to the right.*
