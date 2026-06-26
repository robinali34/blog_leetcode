---
layout: post
title: "[Medium] 974. Subarray Sums Divisible by K"
date: 2026-02-02 00:00:00 -0700
categories: [leetcode, medium, array, hash-table, prefix-sum]
permalink: /2026/02/02/medium-974-subarray-sums-divisible-by-k/
tags: [leetcode, medium, array, hash-table, prefix-sum]
---
Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

```
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

**Example 2:**

```
Input: nums = [5], k = 9
Output: 0
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `2 <= k <= 10^4`

## Thinking Process

1. **Modulo Property**: If two prefix sums have the same modulo value, the subarray between them is divisible by `k`

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
    int subarraysDivByK(vector<int>& nums, int k) {
        int prefixMod = 0, cnt = 0;
        vector<int> prefixMods(k, 0);
        prefixMods[0] = 1; 
        for(int num: nums) {
            prefixMod = (prefixMod + num % k + k) % k;
            cnt += prefixMods[prefixMod];
            prefixMods[prefixMod]++;
        }
        return cnt;
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** 1. **Modulo Property**: If two prefix sums have the same modulo value, the subarray between them is divisible by `k`

**How the code works:**
1. **Modulo Property**: If two prefix sums have the same modulo value, the subarray between them is divisible by `k`
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

**Walkthrough** — input `nums = [4,5,0,-2,-3,1], k = 5`, expected output `7`:

There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(k) - Array of size `k` to store modulo counts (more efficient than O(n) hash map)
## Comparison with Related Problems

| Problem | Goal | Technique | Space Complexity |
|---------|------|-----------|------------------|
| LC 560 | Count subarrays with sum = k | Prefix Sum + Hash Map | O(n) |
| LC 325 | Maximum length subarray with sum = k | Prefix Sum + Hash Map | O(n) |
| LC 974 | Count subarrays divisible by k | Prefix Modulo + Array | O(k) |

## Related Problems

- [1. Two Sum](https://www.leetcode.com/problems/two-sum/) - Hash map lookup for target sum
- [325. Maximum Size Subarray Sum Equals k](https://www.leetcode.com/problems/maximum-size-subarray-sum-equals-k/) - Find maximum length subarray
- [560. Subarray Sum Equals K](https://www.leetcode.com/problems/subarray-sum-equals-k/) - Count subarrays with sum k
- [523. Continuous Subarray Sum](https://www.leetcode.com/problems/continuous-subarray-sum/) - Check for subarray sum divisible by k
- [209. Minimum Size Subarray Sum](https://www.leetcode.com/problems/minimum-size-subarray-sum/) - Find minimum length subarray

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Modulo Property**: If two prefix sums have the same modulo value, the subarray between them is divisible by `k`
2. **Negative Modulo Handling**: Use `(num % k + k) % k` to ensure non-negative modulo for negative numbers
3. **Array vs Hash Map**: Since modulo values are in range `[0, k-1]`, we can use an array instead of a hash map, saving space
4. **Initial State**: Initialize with `prefixMods[0] = 1` to handle subarrays starting from index 0
5. **Integer Overflow Prevention**: The modulo operation naturally prevents integer overflow by keeping values in range `[0, k-1]`

## References

- [LC 974: Subarray Sums Divisible by K on LeetCode](https://www.leetcode.com/problems/subarray-sums-divisible-by-k/)
- [LeetCode Discuss — LC 974: Subarray Sums Divisible by K](https://www.leetcode.com/problems/subarray-sums-divisible-by-k/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/subarray-sums-divisible-by-k/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
