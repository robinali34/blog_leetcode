---
layout: post
title: "[Hard] 327. Count of Range Sum"
date: 2026-01-20 00:00:00 -0700
categories: [leetcode, hard, array, divide-and-conquer]
permalink: /2026/01/20/hard-327-count-of-range-sum/
tags: [leetcode, hard, array, divide-and-conquer, merge-sort, segment-tree, prefix-sum]
---
Given an integer array `nums` and two integers `lower` and `upper`, return *the number of range sums that lie in `[lower, upper]` inclusive*.

Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and `j` inclusive, where `i <= j`.

## Thinking Process

1. **Prefix Sum Transformation**: Convert subarray sum problem to prefix sum difference problem
- **Divide & Conquer**: Sort prefix sums, count pairs using two pointers
- **Segment Tree**: Maintain count of prefix sums, query range for each new prefix

- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Prefix sum | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| **Hash map counting** *(this problem)* | O(n) | O(n) | Frequency, two-sum variants |

## Examples

**Example 1:**
```
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
```

**Example 2:**
```
Input: nums = [0], lower = 0, upper = 0
Output: 1
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `-10^5 <= lower <= upper <= 10^5`

## Common Mistakes

1. **Single element**: `nums = [0]`, `lower = 0`, `upper = 0` → return `1`
2. **All negative**: `nums = [-2,-1]`, `lower = -3`, `upper = -1` → count valid ranges
3. **Large numbers**: Use `long long` to prevent overflow
4. **Empty ranges**: Handle cases where no valid ranges exist
5. **Overflow prevention**: Prefix sums can exceed `int` range

1. **Integer overflow**: Not using `long long` for prefix sums
   ```cpp
   // WRONG:
   vector<int> prefix(n + 1, 0); // ❌ May overflow
   ```

2. **Off-by-one errors**: Incorrect prefix sum indexing
3. **Missing prefix[0]**: Forgetting to include empty prefix (sum = 0)
4. **Wrong range**: Confusing `prefix[j] - upper` and `prefix[j] - lower`
5. **Memory leaks**: Not managing segment tree nodes properly (though solution doesn't delete)

## Related Problems

- [LC 327: Count of Range Sum](https://www.leetcode.com/problems/count-of-range-sum/) - This problem
- [LC 315: Count of Smaller Numbers After Self](https://www.leetcode.com/problems/count-of-smaller-numbers-after-self/) - Similar divide & conquer approach
- [LC 493: Reverse Pairs](https://www.leetcode.com/problems/reverse-pairs/) - Count pairs with condition
- [LC 307: Range Sum Query - Mutable](https://www.leetcode.com/problems/range-sum-query-mutable/) - Segment tree for range sum
- [LC 303: Range Sum Query - Immutable](https://www.leetcode.com/problems/range-sum-query-immutable/) - Prefix sum basics

## Key Takeaways

1. **Prefix Sum Transformation**: Convert subarray sum problem to prefix sum difference problem
2. **Range Condition**: `lower <= prefix[j] - prefix[i] <= upper` becomes `prefix[j] - upper <= prefix[i] <= prefix[j] - lower`
3. **Two Approaches**:
   - **Divide & Conquer**: Sort prefix sums, count pairs using two pointers
   - **Segment Tree**: Maintain count of prefix sums, query range for each new prefix
4. **Dynamic Node Creation**: Reduces memory for sparse segment trees

## References

- [LC 327: Count of Range Sum on LeetCode](https://www.leetcode.com/problems/count-of-range-sum/)
- [LeetCode Discuss — LC 327: Count of Range Sum](https://www.leetcode.com/problems/count-of-range-sum/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/count-of-range-sum/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
