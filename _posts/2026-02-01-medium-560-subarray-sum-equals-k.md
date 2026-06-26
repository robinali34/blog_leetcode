---
layout: post
title: "[Medium] 560. Subarray Sum Equals K"
date: 2026-02-01 00:00:00 -0700
categories: [leetcode, medium, array, hash-table, prefix-sum]
permalink: /2026/02/01/medium-560-subarray-sum-equals-k/
tags: [leetcode, medium, array, hash-table, prefix-sum]
---
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

```
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: The subarrays [1,1] and [1,1] sum to 2.
```

**Example 2:**

```
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: The subarrays [1,2] and [3] sum to 3.
```

**Example 3:**

```
Input: nums = [1,-1,0], k = 0
Output: 3
Explanation: The subarrays [1,-1], [-1,0], and [1,-1,0] sum to 0.
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

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
| **Prefix sum** *(this problem)* | $O(n)$ | $O(n)$ | Range queries, subarray sum |
| Sort + scan | $O(n \log n)$ | $O(1)$ | Intervals, meeting rooms |
| Kadane's algorithm | $O(n)$ | $O(1)$ | Maximum subarray |
| Hash map counting | $O(n)$ | $O(n)$ | Frequency, two-sum variants |

## Solution

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int cnt = 0, sum = 0;
        unordered_map<int, int> prefixSum;
        prefixSum[0] = 1;
        for(int num: nums) {
            sum += num;
            if(prefixSum.contains(sum - k)) {
                cnt += prefixSum[sum - k];
            }
            prefixSum[sum]++;
        }
        return cnt;
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

**Walkthrough** — input `nums = [1,1,1], k = 2`, expected output `2`:

The subarrays [1,1] and [1,1] sum to 2.

- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(n) - Hash map can store up to n distinct prefix sums
## Comparison with LC 325

| Problem | Goal | Hash Map Value | Key Difference |
|---------|------|----------------|----------------|
| LC 325 | Maximum length | First occurrence index | Tracks maximum length |
| LC 560 | Count subarrays | Count of occurrences | Counts all subarrays |

## Related Problems

- [1. Two Sum](https://www.leetcode.com/problems/two-sum/) - Hash map lookup for target sum
- [325. Maximum Size Subarray Sum Equals k](https://www.leetcode.com/problems/maximum-size-subarray-sum-equals-k/) - Find maximum length subarray
- [523. Continuous Subarray Sum](https://www.leetcode.com/problems/continuous-subarray-sum/) - Check for subarray sum divisible by k
- [974. Subarray Sums Divisible by K](https://www.leetcode.com/problems/subarray-sums-divisible-by-k/) - Count subarrays divisible by k
- [209. Minimum Size Subarray Sum](https://www.leetcode.com/problems/minimum-size-subarray-sum/) - Find minimum length subarray

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Prefix Sum Technique**: Convert subarray sum problem to prefix sum difference problem
2. **Hash Map Counting**: Count occurrences of each prefix sum to handle multiple subarrays with the same sum
3. **Initial State**: Initialize with `prefixSum[0] = 1` to handle subarrays starting from index 0
4. **Overlapping Subarrays**: The algorithm correctly counts all overlapping subarrays that sum to `k`
5. **Zero Sum Handling**: When `k = 0`, the algorithm correctly handles cases where prefix sums repeat

## References

- [LC 560: Subarray Sum Equals K on LeetCode](https://www.leetcode.com/problems/subarray-sum-equals-k/)
- [LeetCode Discuss — LC 560: Subarray Sum Equals K](https://www.leetcode.com/problems/subarray-sum-equals-k/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/subarray-sum-equals-k/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
