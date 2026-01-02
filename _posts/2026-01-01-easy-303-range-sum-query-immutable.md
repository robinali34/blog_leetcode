---
layout: post
title: "303. Range Sum Query - Immutable"
date: 2026-01-01 00:00:00 -0700
categories: [leetcode, easy, array, design, prefix-sum]
permalink: /2026/01/01/easy-303-range-sum-query-immutable/
---

# 303. Range Sum Query - Immutable

## Problem Statement

Given an integer array `nums`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

## Examples

**Example 1:**
```
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls will be made to `sumRange`.

## Solution Approach

This problem requires efficiently answering multiple range sum queries on an immutable array. The key insight is to use **prefix sums** to answer each query in O(1) time.

### Key Insights:

1. **Prefix Sum Array**: Precompute cumulative sums during initialization
2. **Range Query Formula**: `sumRange(left, right) = prefix[right + 1] - prefix[left]`
3. **One-Based Indexing**: Use 1-based indexing in prefix array to handle edge cases
4. **O(1) Queries**: Each query takes constant time after preprocessing

### Algorithm:

1. **Initialize**: Build prefix sum array where `prefix[i]` = sum of first `i` elements
2. **Query**: Use prefix sums to compute range sum in O(1)

## Solution

### **Solution: Prefix Sum Array**

```cpp
class NumArray {
public:
    NumArray(vector<int>& nums) {
        const int N = nums.size();
        sums.resize(N + 1, 0);
        for(int i = 0; i < N; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        return sums[right + 1] - sums[left];
    }
private:
    vector<int> sums;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
```

### **Algorithm Explanation:**

1. **Constructor (Lines 3-9)**:
   - **Initialize size**: Create `sums` array of size `N + 1` (1-based indexing)
   - **Build prefix sums**: 
     - `sums[0] = 0` (base case)
     - `sums[i + 1] = sums[i] + nums[i]` for `i` from 0 to N-1
   - **Result**: `sums[i]` contains sum of elements from index 0 to i-1

2. **Sum Range (Lines 11-13)**:
   - **Formula**: `sumRange(left, right) = sums[right + 1] - sums[left]`
   - **Explanation**:
     - `sums[right + 1]` = sum of elements from 0 to right (inclusive)
     - `sums[left]` = sum of elements from 0 to left-1
     - Difference gives sum from left to right (inclusive)

### **Example Walkthrough:**

**Initialization:**
```
nums = [-2, 0, 3, -5, 2, -1]

Build prefix sums:
sums[0] = 0
sums[1] = sums[0] + nums[0] = 0 + (-2) = -2
sums[2] = sums[1] + nums[1] = -2 + 0 = -2
sums[3] = sums[2] + nums[2] = -2 + 3 = 1
sums[4] = sums[3] + nums[3] = 1 + (-5) = -4
sums[5] = sums[4] + nums[4] = -4 + 2 = -2
sums[6] = sums[5] + nums[5] = -2 + (-1) = -3

sums = [0, -2, -2, 1, -4, -2, -3]
```

**Query 1: `sumRange(0, 2)`**
```
sums[3] - sums[0] = 1 - 0 = 1
nums[0] + nums[1] + nums[2] = (-2) + 0 + 3 = 1 ✓
```

**Query 2: `sumRange(2, 5)`**
```
sums[6] - sums[2] = (-3) - (-2) = -1
nums[2] + nums[3] + nums[4] + nums[5] = 3 + (-5) + 2 + (-1) = -1 ✓
```

**Query 3: `sumRange(0, 5)`**
```
sums[6] - sums[0] = (-3) - 0 = -3
Sum of all elements = (-2) + 0 + 3 + (-5) + 2 + (-1) = -3 ✓
```

## Algorithm Breakdown

### **Prefix Sum Concept**

Prefix sum is a technique where we precompute cumulative sums:
- `prefix[i]` = sum of elements from index 0 to i-1
- Allows O(1) range sum queries

### **Why 1-Based Indexing?**

Using 1-based indexing in the prefix array simplifies the formula:
- `sums[0] = 0` (no elements)
- `sums[i]` = sum of first `i` elements (indices 0 to i-1)
- Range `[left, right]` = `sums[right + 1] - sums[left]`

### **Time & Space Complexity**

- **Time Complexity**:
  - **Initialization**: O(n) - build prefix sum array
  - **Query**: O(1) - constant time lookup
- **Space Complexity**: O(n) - store prefix sum array

## Key Points

1. **Prefix Sums**: Precompute cumulative sums for O(1) queries
2. **1-Based Indexing**: Simplifies range calculation
3. **Immutable Array**: No updates, so prefix sums never change
4. **Efficient**: Optimal for multiple queries on static data

## Alternative Approaches

### **Approach 1: Prefix Sum (Current Solution)**
- **Time**: O(n) init, O(1) query
- **Space**: O(n)
- **Best for**: Multiple queries on immutable array

### **Approach 2: Naive (Calculate Each Time)**
- **Time**: O(1) init, O(n) query
- **Space**: O(1)
- **Use when**: Very few queries expected

### **Approach 3: Segment Tree**
- **Time**: O(n) init, O(log n) query
- **Space**: O(n)
- **Overkill**: Not needed for immutable array

## Edge Cases

1. **Single element**: `nums = [5]`, `sumRange(0, 0)` = 5
2. **All negative**: `nums = [-1, -2, -3]`
3. **All positive**: `nums = [1, 2, 3]`
4. **Mixed signs**: `nums = [-2, 0, 3, -5, 2, -1]`
5. **Large numbers**: Handle integer overflow (not an issue with constraints)

## Related Problems

- [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) - 2D version
- [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) - Mutable 1D version
- [308. Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) - Mutable 2D version
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) - Uses prefix sums

## Tags

`Array`, `Design`, `Prefix Sum`, `Easy`

