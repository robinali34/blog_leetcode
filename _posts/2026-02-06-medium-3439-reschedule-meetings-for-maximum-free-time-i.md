---
layout: post
title: "[Medium] 3439. Reschedule Meetings for Maximum Free Time I"
date: 2026-02-06 00:00:00 -0700
categories: [leetcode, medium, array, intervals, sliding-window, prefix-sum]
permalink: /2026/02/06/medium-3439-reschedule-meetings-for-maximum-free-time-i/
tags: [leetcode, medium, array, intervals, sliding-window, prefix-sum]
---
You are given an integer `eventTime` (the event runs from time `0` to `eventTime`) and two arrays `startTime` and `endTime` representing `n` **non-overlapping** meetings. You may **reschedule at most `k`** meetings (move their start times while keeping duration and relative order) to maximize the **longest continuous free time** during the event. Meetings must remain non-overlapping and within `[0, eventTime]`.

Return the maximum free time achievable.

## Examples

**Example 1:**

```
Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]
Output: 2
Explanation: Reschedule meeting [1,2] to [2,3]. Free blocks: [0,1], [3,5] → max free time 2.
```

**Example 2:**

```
Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]
Output: 6
Explanation: Reschedule [2,4] to [1,3]. Free blocks: [0,1], [4,9], [9,10] → max free time 6 ([3,9] or similar).
```

## Constraints

- `1 <= n <= 10^5`
- `0 <= eventTime <= 10^9`
- `0 <= k <= n`
- `startTime.length == endTime.length == n`
- `0 <= startTime[i] < endTime[i] <= eventTime`
- Meetings are non-overlapping and sorted by start time (typical).

## Thinking Process

1. **Window of k meetings:** The best free block we can create by rescheduling at most k meetings is the maximum over all contiguous windows of k meetings: free time = span length − total duration of those k meetings.

- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Intervals on timeline</text>

  <line x1="30" y1="60" x2="250" y2="60" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="50" y="48" width="60" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="100" y="48" width="50" height="24" rx="3" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="160" y="48" width="70" height="24" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="95" text-anchor="middle" font-size="11" fill="#6B6560">sort by start → scan overlaps</text>

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

Precompute prefix sums of meeting durations, then for each window of `k` consecutive meetings compute free time and take the max.

```cpp
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size(), rtn = 0;
        vector<int> sum(n + 1);
        for (int i = 0; i < n; i++) {
            sum[i + 1] = sum[i] + endTime[i] - startTime[i];
        }
        for (int i = k - 1; i < n; i++) {
            int right = i == n - 1 ? eventTime : startTime[i + 1];
            int left = i == k - 1 ? 0 : endTime[i - k];
            rtn = max(rtn, right - left - (sum[i + 1] - sum[i - k + 1]));
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** 1. **Window of k meetings:** The best free block we can create by rescheduling at most k meetings is the maximum over all contiguous windows of k meetings: free time = span length − total duration of those k meetings.

**How the code works:**
1. **Window of k meetings:** The best free block we can create by rescheduling at most k meetings is the maximum over all contiguous windows of k meetings: free time = span length − total duration of those k meetings.
- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

**Walkthrough** — input `eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]`, expected output `2`:

Reschedule meeting [1,2] to [2,3]. Free blocks: [0,1], [3,5] → max free time 2.

**Time:** O(n). **Space:** O(n).
## Comparison

| Approach        | Time | Space |
|----------------|------|--------|
| Prefix sum     | O(n) | O(n)   |
| Sliding window | O(n) | O(1)   |

## Related Problems

- [252. Meeting Rooms](https://www.leetcode.com/problems/meeting-rooms/) — Check if all meetings can be attended
- [253. Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/) — Minimum rooms needed

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Window of k meetings:** The best free block we can create by rescheduling at most k meetings is the maximum over all contiguous windows of k meetings: free time = span length − total duration of those k meetings.
2. **Span boundaries:** `left` = end of meeting before the window (or 0); `right` = start of meeting after the window (or `eventTime`).
3. **Prefix sum vs sliding window:** Same formula; sliding window avoids extra array for O(1) space.

## References

- [LC 3439: Reschedule Meetings for Maximum Free Time I on LeetCode](https://www.leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/)
- [LeetCode Discuss — LC 3439: Reschedule Meetings for Maximum Free Time I](https://www.leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
