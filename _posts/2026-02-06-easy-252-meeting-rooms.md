---
layout: post
title: "[Easy] 252. Meeting Rooms"
date: 2026-02-06 00:00:00 -0700
categories: [leetcode, easy, array, sorting, intervals]
permalink: /2026/02/06/easy-252-meeting-rooms/
tags: [leetcode, easy, array, sorting, intervals]
---
Given an array of meeting time intervals where `intervals[i] = [starti, endi]`, determine if a person could attend all meetings.

## Examples

**Example 1:**

```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: [0,30] overlaps with [5,10] (and with [15,20]), so the person cannot attend all.
```

**Example 2:**

```
Input: intervals = [[7,10],[2,4]]
Output: true
Explanation: No overlap; the person can attend all meetings.
```

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti < endi <= 10^6`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Prefix sum** *(this problem)* | $O(n)$ | $O(n)$ | Range queries, subarray sum |
| Sort + scan | $O(n \log n)$ | $O(1)$ | Intervals, meeting rooms |
| Kadane's algorithm | $O(n)$ | $O(1)$ | Maximum subarray |
| Hash map counting | $O(n)$ | $O(n)$ | Frequency, two-sum variants |

## Thinking Process

Sort intervals by start time. After sorting, any overlap must appear between **consecutive** meetings — if `intervals[i].start < intervals[i-1].end`, the person is double-booked.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Intervals on timeline</text>

  <line x1="30" y1="60" x2="250" y2="60" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="50" y="48" width="60" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="100" y="48" width="50" height="24" rx="3" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="160" y="48" width="70" height="24" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="95" text-anchor="middle" font-size="11" fill="#6B6560">sort by start → scan overlaps</text>

</svg>

## Solution — $O(n \log n)$ time, $O(\log n)$ space

```cpp
class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < intervals[i - 1][1]) {
                return false;
            }
        }
        return true;
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** Sort intervals by start time. After sorting, any overlap must appear between **consecutive** meetings — if `intervals[i].start < intervals[i-1].end`, the person is double-booked.

**Walkthrough** — input `intervals = [[0,30],[5,10],[15,20]]`, expected output `false`:

[0,30] overlaps with [5,10] (and with [15,20]), so the person cannot attend all.

**Time:** $O(n \log n) · **Space:** $O(\log n)
## Related Problems

- [253. Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/) — Minimum number of rooms
- [56. Merge Intervals](https://www.leetcode.com/problems/merge-intervals/) — Merge overlapping intervals

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Sort by start:** After sorting, overlaps can only occur between adjacent intervals.
2. **Overlap condition:** Current start < previous end ⇒ overlap.
3. **Follow-up:** [253. Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/) asks for the minimum number of rooms (sweep line or min-heap).

## References

- [LC 252: Meeting Rooms on LeetCode](https://www.leetcode.com/problems/meeting-rooms/)
- [LeetCode Discuss — LC 252: Meeting Rooms](https://www.leetcode.com/problems/meeting-rooms/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/meeting-rooms/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
