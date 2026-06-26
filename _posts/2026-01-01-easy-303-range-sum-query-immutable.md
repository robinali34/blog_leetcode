---
layout: post
title: "[Easy] 303. Range Sum Query - Immutable"
date: 2026-01-01 00:00:00 -0700
categories: [leetcode, easy, array, design, prefix-sum]
permalink: /2026/01/01/easy-303-range-sum-query-immutable/
---
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

## Thinking Process

Given an integer array `nums`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Design pattern</text>

  <rect x="40" y="45" width="70" height="36" rx="4" fill="#D4D8E0" stroke="#8B8680"/><text x="75" y="67" text-anchor="middle" font-size="10">API</text>
  <rect x="150" y="45" width="90" height="36" rx="4" fill="#E0D8E4" stroke="#A098A8"/><text x="195" y="67" text-anchor="middle" font-size="10">hash + list</text>
  <path d="M110 63h36" stroke="#8B8680" stroke-width="2" marker-end="url(#arr2)"/>
  <defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>
  <text x="140" y="105" text-anchor="middle" font-size="11" fill="#6B6560">compose data structures for operations</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Prefix sum** *(this problem)* | $O(n)$ | $O(n)$ | Range queries, subarray sum |
| Sort + scan | $O(n \log n)$ | $O(1)$ | Intervals, meeting rooms |
| Kadane's algorithm | $O(n)$ | $O(1)$ | Maximum subarray |
| Hash map counting | $O(n)$ | $O(n)$ | Frequency, two-sum variants |

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

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** Given an integer array `nums`, handle multiple queries of the following type:

**How the code works:**
1. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

**Time:** - **Initialization**: O(n) - build prefix sum array · **Space:** O(n) - store prefix sum array

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

## Edge Cases

1. **Single element**: `nums = [5]`, `sumRange(0, 0)` = 5
2. **All negative**: `nums = [-1, -2, -3]`
3. **All positive**: `nums = [1, 2, 3]`
4. **Mixed signs**: `nums = [-2, 0, 3, -5, 2, -1]`
5. **Large numbers**: Handle integer overflow (not an issue with constraints)

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [304. Range Sum Query 2D - Immutable](https://www.leetcode.com/problems/range-sum-query-2d-immutable/) - 2D version
- [307. Range Sum Query - Mutable](https://www.leetcode.com/problems/range-sum-query-mutable/) - Mutable 1D version
- [308. Range Sum Query 2D - Mutable](https://www.leetcode.com/problems/range-sum-query-2d-mutable/) - Mutable 2D version
- [560. Subarray Sum Equals K](https://www.leetcode.com/problems/subarray-sum-equals-k/) - Uses prefix sums

## Tags

`Array`, `Design`, `Prefix Sum`, `Easy`

## Key Takeaways

- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

## References

- [LC 303: Range Sum Query - Immutable on LeetCode](https://www.leetcode.com/problems/range-sum-query-immutable/)
- [LeetCode Discuss — LC 303: Range Sum Query - Immutable](https://www.leetcode.com/problems/range-sum-query-immutable/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/range-sum-query-immutable/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
