---
layout: post
title: "[Medium] 2461. Maximum Sum of Distinct Subarrays With Length K"
date: 2026-04-09
categories: [leetcode, medium, sliding-window, hash-map]
tags: [leetcode, medium, sliding-window, hash-map, array]
permalink: /2026/04/09/medium-2461-maximum-sum-of-distinct-subarrays-with-length-k/
---
Given an integer array `nums` and an integer `k`, find the **maximum sum** among all subarrays of length `k` that have **all distinct** elements. Return `0` if no such subarray exists.

## Examples

**Example 1:**

```
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: Subarrays of length 3 with distinct elements:
  [1,5,4] sum=10, [5,4,2] sum=11, [4,2,9] sum=15
  [2,9,9] has duplicate, [9,9,9] has duplicate
  Maximum = 15
```

**Example 2:**

```
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: [4,4,4] has duplicates, no valid subarray exists.
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Thinking Process

### Two Constraints on the Window

The sliding window must satisfy:
1. **Length exactly `k`** -- standard fixed-size window
2. **All distinct elements** -- no duplicates inside

When a duplicate enters, we can't just shrink by one -- we must shrink past the **previous occurrence** of that duplicate to restore uniqueness.

### Algorithm

Use a hash map `numToIdx` tracking the last seen index of each element. For each new `end`:

1. Look up the last occurrence of `nums[end]`
2. Shrink `begin` past that occurrence (to remove the duplicate)
3. Also shrink if window exceeds size `k`
4. If window size equals `k`, update the answer

The running sum `currSum` is maintained incrementally as we shrink/expand.

### Walk-through

```
nums = [1, 5, 4, 2, 9, 9, 9], k = 3

end=0: [1]         currSum=1,  size=1
end=1: [1,5]       currSum=6,  size=2
end=2: [1,5,4]     currSum=10, size=3 → rtn=10
end=3: shrink(size>k) → [5,4,2]  currSum=11, size=3 → rtn=11
end=4: shrink(size>k) → [4,2,9]  currSum=15, size=3 → rtn=15
end=5: 9 seen at idx=4, shrink past 4 → [9]  currSum=9, size=1
end=6: 9 seen at idx=5, shrink past 5 → [9]  currSum=9, size=1

Answer: 15 ✓
```

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Sliding window</text>

  <rect x="20" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="36" y="63" text-anchor="middle" font-size="11">a</text>
  <rect x="52" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="68" y="63" text-anchor="middle" font-size="11">b</text>
  <rect x="84" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="63" text-anchor="middle" font-size="11">c</text>
  <rect x="116" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="132" y="63" text-anchor="middle" font-size="11">d</text>
  <rect x="148" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="164" y="63" text-anchor="middle" font-size="11">e</text>
  <rect x="52" y="38" width="64" height="42" rx="4" fill="none" stroke="#C4956A" stroke-width="2" stroke-dasharray="4"/>
  <text x="84" y="32" text-anchor="middle" font-size="10" fill="#C4956A" font-weight="600">window</text>
  <text x="110" y="105" text-anchor="middle" font-size="11" fill="#6B6560">expand right, shrink left when invalid</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Fixed-size window** *(this problem)* | O(n) | O(1) | Window size known upfront |
| Variable-size window | O(n) | O(1) | Expand/shrink until valid |
| Window + hash map | O(n) | O(k) | Track character/count frequencies |
| Deque window max | O(n) | O(k) | Monotonic deque for max/min in window |

## Solution
```cpp
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long rtn = 0, currSum = 0;
        int begin = 0, end = 0;

        unordered_map<int, int> numToIdx;
        while (end < nums.size()) {
            int currNum = nums[end];
            int lastOccur = (numToIdx.contains(currNum) ? numToIdx[currNum] : -1);
            while (begin <= lastOccur || end - begin + 1 > k) {
                currSum -= nums[begin];
                begin++;
            }
            numToIdx[currNum] = end;
            currSum += nums[end];
            if (end - begin + 1 == k) {
                rtn = max(rtn, currSum);
            }
            end++;
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** ### Two Constraints on the Window

**How the code works:**
1. **Length exactly `k`** -- standard fixed-size window
2. **All distinct elements** -- no duplicates inside
1. Look up the last occurrence of `nums[end]`
2. Shrink `begin` past that occurrence (to remove the duplicate)
3. Also shrink if window exceeds size `k`
4. If window size equals `k`, update the answer

**Walkthrough** — input `nums = [1,5,4,2,9,9,9], k = 3`, expected output `15`:

Subarrays of length 3 with distinct elements:
  [1,5,4] sum=10, [5,4,2] sum=11, [4,2,9] sum=15
  [2,9,9] has duplicate, [9,9,9] has duplicate
  Maximum = 15
## Key Details

**Why `begin <= lastOccur` (not `<`)?** We need to move `begin` **past** the previous occurrence, so we shrink while `begin` is still at or before `lastOccur`.

**Why combine both conditions in one `while`?** A single shrink loop handles both constraints simultaneously:
- `end - begin + 1 > k` enforces the size limit
- `begin <= lastOccur` enforces uniqueness

**Why `long long`?** With 10^5 elements each up to 10^5, the sum can reach 10^{10}.

## Common Mistakes

- Only checking window size without handling duplicates (misses the distinct constraint)
- Not updating `numToIdx` after shrinking (stale indices cause incorrect shrinks)
- Using a frequency map + separate duplicate counter instead of last-index tracking (works but more complex)

## Key Takeaways

- **"Fixed-size window + all distinct"** = sliding window with last-occurrence tracking
- Storing the **index** of the last occurrence (not just frequency) lets us jump `begin` directly past the duplicate
- The combined shrink condition handles both constraints elegantly in one loop

## Related Problems

- [3. Longest Substring Without Repeating Characters](https://www.leetcode.com/problems/longest-substring-without-repeating-characters/) -- variable-size distinct window
- [713. Subarray Product Less Than K](https://www.leetcode.com/problems/subarray-product-less-than-k/) -- sliding window counting
- [219. Contains Duplicate II](https://www.leetcode.com/problems/contains-duplicate-ii/) -- duplicate within window of size k
- [992. Subarrays with K Different Integers](https://www.leetcode.com/problems/subarrays-with-k-different-integers/) -- exact k distinct elements

## References

- [LC 2461: Maximum Sum of Distinct Subarrays With Length K on LeetCode](https://www.leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)
- [LeetCode Discuss — LC 2461: Maximum Sum of Distinct Subarrays With Length K](https://www.leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings — Sliding Window](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
