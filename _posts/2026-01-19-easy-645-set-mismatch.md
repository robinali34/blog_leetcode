---
layout: post
title: "[Easy] 645. Set Mismatch"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, array, hash-table, math]
permalink: /2026/01/19/easy-645-set-mismatch/
tags: [leetcode, easy, array, hash-table, math, bit-manipulation, negative-marking]
---
You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another** number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form `[duplicate, missing]`.

## Examples

**Example 1:**
```
Input: nums = [1,2,2,4]
Output: [2,3]
Explanation: 2 is duplicated, 3 is missing.
```

**Example 2:**
```
Input: nums = [1,1]
Output: [1,2]
Explanation: 1 is duplicated, 2 is missing.
```

## Constraints

- `2 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^4`
- Exactly one number appears twice, exactly one is missing.

## Thinking Process

1. **Mathematical Approach**: Elegant solution using sum and square sum differences

- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 90" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Bit manipulation</text>

  <text x="40" y="50" font-family="monospace" font-size="14" fill="#3A3530">1 0 1 1 0 1 0</text>
  <text x="40" y="75" font-size="11" fill="#6B6560">XOR pairs · masks · shifts</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Prefix sum** *(this problem)* | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| Hash map counting | O(n) | O(n) | Frequency, two-sum variants |

## Solution

```cpp
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        const int N = nums.size();
        long long x = 0, y = 0;
        for(int i = 1; i <= N; i++) {
            x += nums[i - 1] - i;
            y += (long long) nums[i - 1] * nums[i - 1] - (long long)i * i;
        }
        int missing = (y - x * x) / (2 * x);
        int duplicate = missing + x;
        return {duplicate, missing};
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** 1. **Mathematical Approach**: Elegant solution using sum and square sum differences

**How the code works:**
1. **Mathematical Approach**: Elegant solution using sum and square sum differences
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

**Walkthrough** — input `nums = [1,2,2,4]`, expected output `[2,3]`:

2 is duplicated, 3 is missing.
## Common Mistakes

1. **Smallest input**: `nums = [1,1]` → `[1,2]`
2. **Largest input**: `nums = [1,2,3,...,n-1,n,n]` → `[n, n+1]` (but n+1 > n, so invalid)
3. **Duplicate at start**: `nums = [2,2,3,4]` → `[2,1]`
4. **Duplicate at end**: `nums = [1,2,3,3]` → `[3,4]` (but 4 > 3, so invalid)
5. **Missing at start**: `nums = [2,2,3,4]` → `[2,1]`
6. **Missing at end**: `nums = [1,1,2,3]` → `[1,4]` (but 4 > 3, so invalid)

1. **Integer overflow**: Not using `long long` for square calculations
2. **Index off-by-one**: Confusing 0-based vs 1-based indexing
3. **Sign errors**: Incorrect handling of negative values in mathematical approach
4. **Division by zero**: Not checking if `x == 0` (shouldn't happen per constraints)
5. **Wrong order**: Returning `[missing, duplicate]` instead of `[duplicate, missing]`

## Related Problems

- [LC 41: First Missing Positive](https://www.leetcode.com/problems/first-missing-positive/) - Find missing positive number
- [LC 268: Missing Number](https://www.leetcode.com/problems/missing-number/) - Find single missing number
- [LC 442: Find All Duplicates in an Array](https://www.leetcode.com/problems/find-all-duplicates-in-an-array/) - Find all duplicates
- [LC 448: Find All Numbers Disappeared in an Array](https://www.leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) - Find all missing numbers
- [LC 287: Find the Duplicate Number](https://www.leetcode.com/problems/find-the-duplicate-number/) - Find duplicate (no missing)

## Key Takeaways

1. **Mathematical Approach**: Elegant solution using sum and square sum differences
2. **Negative Marking**: Space-efficient in-place solution
3. **Hash Map**: Simple and intuitive, uses extra space
4. **XOR**: Bit manipulation approach, more complex but interesting

## References

- [LC 645: Set Mismatch on LeetCode](https://www.leetcode.com/problems/set-mismatch/)
- [LeetCode Discuss — LC 645: Set Mismatch](https://www.leetcode.com/problems/set-mismatch/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/set-mismatch/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
