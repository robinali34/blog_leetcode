---
layout: post
title: "[Medium] 532. K-diff Pairs in an Array"
date: 2026-02-06 00:00:00 -0700
categories: [leetcode, medium, array, hash-table]
permalink: /2026/02/06/medium-532-k-diff-pairs-in-an-array/
tags: [leetcode, medium, array, hash-table]
---
Given an array of integers `nums` and an integer `k`, return the number of **unique** k-diff pairs in the array.

A **k-diff pair** is an integer pair `(nums[i], nums[j])` where:

- `0 <= i, j < nums.length`
- `i != j`
- `|nums[i] - nums[j]| == k`

Pairs `(i, j)` and `(j, i)` count as the same pair.

## Examples

**Example 1:**

```
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: The two 2-diff pairs are (1, 3) and (3, 5). (Two 1s yield one unique pair (1,3).)
```

**Example 2:**

```
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: The four 1-diff pairs are (1,2), (2,3), (3,4), (4,5).
```

**Example 3:**

```
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: The only 0-diff pair is (1, 1).
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^7 <= nums[i] <= 10^7`
- `0 <= k <= 10^7`

## Thinking Process

1. **Unique pairs:** Count by distinct values (or by one representative of each pair), not by indices.

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

One pass to build frequency map; then handle k==0 (count values with freq > 1) and k>0 (count values where num+k exists).

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;
        for (auto& i : nums) {
            freqs[i] += 1;
        }

        int rtn = 0;
        if (k == 0) {
            for (auto& [_, freq] : freqs) {
                if (freq > 1) rtn++;
            }
        } else {
            for (auto& [num, _] : freqs) {
                if (freqs.contains(num + k)) {
                    rtn++;
                }
            }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** 1. **Unique pairs:** Count by distinct values (or by one representative of each pair), not by indices.

**How the code works:**
1. **Unique pairs:** Count by distinct values (or by one representative of each pair), not by indices.
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

**Walkthrough** — input `nums = [3,1,4,1,5], k = 2`, expected output `2`:

The two 2-diff pairs are (1, 3) and (3, 5). (Two 1s yield one unique pair (1,3).)

**Time:** O(n). **Space:** O(n).
## Related Problems

- [1. Two Sum](https://www.leetcode.com/problems/two-sum/) — Find pairs with a target sum
- [454. 4Sum II](https://www.leetcode.com/problems/4sum-ii/) — Count pairs from four arrays

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Unique pairs:** Count by distinct values (or by one representative of each pair), not by indices.
2. **k == 0:** Count distinct numbers that appear more than once.
3. **k > 0:** Only check `num + k` (or only `num - k`) to count each pair once.
4. **Avoid k < 0:** Problem states `k >= 0`; no need to handle negative k.

## References

- [LC 532: K-diff Pairs in an Array on LeetCode](https://www.leetcode.com/problems/k-diff-pairs-in-an-array/)
- [LeetCode Discuss — LC 532: K-diff Pairs in an Array](https://www.leetcode.com/problems/k-diff-pairs-in-an-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/k-diff-pairs-in-an-array/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
