---
layout: post
title: "[Medium] 325. Maximum Size Subarray Sum Equals k"
date: 2026-02-01 00:00:00 -0700
categories: [leetcode, medium, array, hash-table, prefix-sum]
permalink: /2026/02/01/medium-325-maximum-size-subarray-sum-equals-k/
tags: [leetcode, medium, array, hash-table, prefix-sum]
---
Given an integer array `nums` and an integer `k`, return the maximum length of a subarray that sums to `k`. If there is no such subarray, return `0`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

```
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
```

**Example 2:**

```
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
```

**Example 3:**

```
Input: nums = [2,0,0,3], k = 3
Output: 3
Explanation: The subarray [0, 0, 3] sums to 3 and is the longest.
```

## Constraints

- `1 <= nums.length <= 2 * 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `-10^9 <= k <= 10^9`

## Thinking Process

1. **Prefix Sum Technique**: Convert subarray sum problem to prefix sum difference problem

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
| **Prefix sum** *(this problem)* | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| Hash map counting | O(n) | O(n) | Frequency, two-sum variants |

## Solution

```cpp
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        int max_len = 0;
        for(int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for(int j = i; j < nums.size(); j++) {
                sum += nums[j];
                if(sum == k) {
                    max_len = max(max_len, j - i + 1);
                }
            }
        }
        return max_len;
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** 1. **Prefix Sum Technique**: Convert subarray sum problem to prefix sum difference problem

**How the code works:**
1. **Prefix Sum Technique**: Convert subarray sum problem to prefix sum difference problem
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

**Walkthrough** — input `nums = [1,-1,5,-2,3], k = 3`, expected output `4`:

The subarray [1, -1, 5, -2] sums to 3 and is the longest.

### Algorithm Breakdown:

1. **Outer Loop**: Iterate through all possible starting positions `i`
2. **Inner Loop**: For each starting position, iterate through all ending positions `j >= i`
3. **Sum Calculation**: Accumulate sum from `i` to `j`
4. **Check and Update**: If sum equals `k`, update maximum length

### Why This Works:

- **Exhaustive Search**: Checks all possible subarrays
- **Correctness**: Guaranteed to find the maximum length subarray
- **Simple Logic**: Straightforward implementation

### Solution 1 (Brute-Force):
- **Time Complexity**: O(n²) - Two nested loops, each checking O(n) positions
- **Space Complexity**: O(1) - Only using a constant amount of extra space

### Solution 2 (Prefix Sum with Hash Map):
- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(n) - Hash map can store up to n distinct prefix sums
## Related Problems

- [1. Two Sum](https://www.leetcode.com/problems/two-sum/) - Hash map lookup for target sum
- [560. Subarray Sum Equals K](https://www.leetcode.com/problems/subarray-sum-equals-k/) - Count subarrays with sum k
- [209. Minimum Size Subarray Sum](https://www.leetcode.com/problems/minimum-size-subarray-sum/) - Find minimum length subarray
- [523. Continuous Subarray Sum](https://www.leetcode.com/problems/continuous-subarray-sum/) - Check for subarray sum divisible by k
- [974. Subarray Sums Divisible by K](https://www.leetcode.com/problems/subarray-sums-divisible-by-k/) - Count subarrays divisible by k

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Prefix Sum Technique**: Convert subarray sum problem to prefix sum difference problem
2. **Hash Map Lookup**: Use hash map to find previous prefix sums in O(1) time
3. **First Occurrence**: Store only the first occurrence of each prefix sum to maximize subarray length
4. **Direct Match**: Check if current prefix sum equals `k` (subarray from index 0)
5. **Overflow Prevention**: Use `long long` to handle large sums and prevent integer overflow
6. **Edge Cases**: Handle cases where prefix sum equals `k` directly, and cases with zeros in the array

## References

- [LC 325: Maximum Size Subarray Sum Equals k on LeetCode](https://www.leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
- [LeetCode Discuss — LC 325: Maximum Size Subarray Sum Equals k](https://www.leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/maximum-size-subarray-sum-equals-k/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
