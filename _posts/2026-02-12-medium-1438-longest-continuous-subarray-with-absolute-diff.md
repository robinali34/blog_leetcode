---
layout: post
title: "[Medium] 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit"
date: 2026-02-12 00:00:00 -0700
categories: [leetcode, medium, sliding-window, monotonic-queue]
tags: [leetcode, medium, sliding-window, monotonic-queue]
permalink: /2026/02/12/medium-1438-longest-continuous-subarray-with-absolute-diff/
---
## Problem

Given an integer array `nums` and an integer `limit`, return the size of the longest continuous subarray such that the absolute difference between the maximum and minimum element in the subarray is less than or equal to `limit`.

## Examples

**Example 1**

```
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: The longest subarray is [2,4] or [4,7].
```

**Example 2**

```
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The longest subarray is [2,4,7,2].
```

**Example 3**

```
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
Explanation: The longest subarray of equal values is length 3 (three 2's).
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Fixed-size window** *(this problem)* | $O(n)$ | $O(1)$ | Window size known upfront |
| Variable-size window | $O(n)$ | $O(1)$ | Expand/shrink until valid |
| Window + hash map | $O(n)$ | $O(k)$ | Track character/count frequencies |
| Deque window max | $O(n)$ | $O(k)$ | Monotonic deque for max/min in window |

## Thinking Process

We need the longest window [l..r] where max(nums[l..r]) - min(nums[l..r]) <= limit.

Two common sliding-window techniques:

1. Multiset (or balanced BST) to maintain current window's min and max. Expand right pointer; when condition violated, shrink left pointer and erase from multiset. Time: O(n log n), Space: O(n).

2. Monotonic deques (optimal): maintain two deques:
   - `decrease` keeps current window's values in decreasing order (front = max)
   - `increase` keeps values in increasing order (front = min)
   Push new value by popping from back while invariant violated. When shrinking left, pop from front if it equals outgoing value. This yields O(n) time and O(n) space.



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

## Solutions

### Multiset (balanced BST) — O(n log n)

{% raw %}
```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        multiset<int> ms;
        int left = 0, rtn = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            ms.insert(nums[right]);
            while (*ms.rbegin() - *ms.begin() > limit) {
                ms.erase(ms.find(nums[left]));
                left++;
            }
            rtn = max(rtn, right - left + 1);
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** We need the longest window [l..r] where max(nums[l..r]) - min(nums[l..r]) <= limit.

**How the code works:**
1. Multiset (or balanced BST) to maintain current window's min and max. Expand right pointer; when condition violated, shrink left pointer and erase from multiset. Time: O(n log n), Space: O(n).
2. Monotonic deques (optimal): maintain two deques:
- `decrease` keeps current window's values in decreasing order (front = max)
- `increase` keeps values in increasing order (front = min)
## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

- **Pattern:** Fixed-size window (this problem)
- `decrease` keeps current window's values in decreasing order (front = max)
- `increase` keeps values in increasing order (front = min)

## References

- [LC 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit on LeetCode](https://www.leetcode.com/problems/longest-continuous-subarray-with-absolute-diff/)
- [LeetCode Discuss — LC 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://www.leetcode.com/problems/longest-continuous-subarray-with-absolute-diff/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/longest-continuous-subarray-with-absolute-diff/editorial/) *(may require premium)*

## Template Reference

- [Monotonic Queue / Sliding Window](/posts/2025-10-29-leetcode-templates-data-structures/#monotonic-queue)
