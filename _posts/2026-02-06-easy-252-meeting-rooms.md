---
layout: post
title: "252. Meeting Rooms"
date: 2026-02-06 00:00:00 -0700
categories: [leetcode, easy, array, sorting, intervals]
permalink: /2026/02/06/easy-252-meeting-rooms/
tags: [leetcode, easy, array, sorting, intervals]
---

# 252. Meeting Rooms

## Problem Statement

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

## Clarification Questions

1. **Overlap:** Are two intervals that only touch at an endpoint (e.g. [1,2] and [2,3]) considered overlapping? (Typically no — one can end as the next starts.)
2. **Empty input:** Return true for empty or single-interval input.

## Solution Approach

Sort intervals by start time. Then any overlap would appear between consecutive pairs: if the next meeting starts before the previous one ends, there is an overlap. So for each `i >= 1`, check `intervals[i][0] < intervals[i-1][1]`; if true, return false. Otherwise return true.

## Solution: Sort and Check Consecutive Pairs

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

- **Time:** O(n log n) — sort dominates.
- **Space:** O(log n) for sort (or O(1) if in-place sort).

## Key Insights

1. **Sort by start:** After sorting, overlaps can only occur between adjacent intervals.
2. **Overlap condition:** Current start < previous end ⇒ overlap.
3. **Follow-up:** [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) asks for the minimum number of rooms (sweep line or min-heap).

## Related Problems

- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) — Minimum number of rooms
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) — Merge overlapping intervals
