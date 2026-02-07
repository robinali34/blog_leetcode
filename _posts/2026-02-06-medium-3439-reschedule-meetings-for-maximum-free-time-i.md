---
layout: post
title: "3439. Reschedule Meetings for Maximum Free Time I"
date: 2026-02-06 00:00:00 -0700
categories: [leetcode, medium, array, intervals, sliding-window, prefix-sum]
permalink: /2026/02/06/medium-3439-reschedule-meetings-for-maximum-free-time-i/
tags: [leetcode, medium, array, intervals, sliding-window, prefix-sum]
---

# 3439. Reschedule Meetings for Maximum Free Time I

## Problem Statement

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

## Solution Approach

**Idea:** For any contiguous block of `k` meetings, we can reschedule only those `k` meetings so that they are packed optimally within the span from the end of the meeting just before the block to the start of the meeting just after the block. That leaves one contiguous free segment of length:

`(right - left) - (total duration of those k meetings)`

where `left` = end of the meeting before the block (or 0) and `right` = start of the meeting after the block (or `eventTime`). We take the maximum over all windows of `k` consecutive meetings.

- **Prefix-sum version:** Precompute `sum[i]` = total duration of meetings `0..i-1`. For each window `[i-k+1, i]`, free time = `(right - left) - (sum[i+1] - sum[i-k+1])`.
- **Sliding-window version:** Maintain running total `t` of the current `k` meetings' durations; same formula with `t` instead of the prefix-sum difference.

## Solution 1: Prefix Sum

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

- **Indexing:** Window of `k` meetings ending at index `i` = meetings `[i-k+1, i]`. Their total duration = `sum[i+1] - sum[i-k+1]`. Span: `[left, right]` with `left` = `endTime[i-k]` (or 0 if no meeting before), `right` = `startTime[i+1]` (or `eventTime` if no meeting after).
- **Time:** O(n). **Space:** O(n).

## Solution 2: Sliding Window (Running Sum)

Same formula; maintain the total duration of the current `k` meetings with a running sum instead of prefix sum.

```cpp
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size(), rtn = 0, t = 0;
        vector<int> sum(n + 1);
        for (int i = 0; i < n; i++) {
            t += endTime[i] - startTime[i];
            int left = i <= k - 1 ? 0 : endTime[i - k];
            int right = i == n - 1 ? eventTime : startTime[i + 1];
            rtn = max(rtn, right - left - t);
            if (i >= k - 1) {
                t -= endTime[i - k + 1] - startTime[i - k + 1];
            }
        }
        return rtn;
    }
};
```

- **Running sum:** `t` is the total duration of meetings in the current window. When `i >= k - 1`, subtract the duration of meeting `i - k + 1` so that `t` stays the sum of the last `k` meetings. (The `vector<int> sum(n+1)` in the code is unused; removing it gives O(1) space.)
- **Time:** O(n). **Space:** O(1) if we remove the unused `sum` array.

### Optional cleanup (Solution 2)

Remove the unused `sum` to make space O(1):

```cpp
int n = startTime.size(), rtn = 0, t = 0;
for (int i = 0; i < n; i++) {
    t += endTime[i] - startTime[i];
    int left = i <= k - 1 ? 0 : endTime[i - k];
    int right = i == n - 1 ? eventTime : startTime[i + 1];
    rtn = max(rtn, right - left - t);
    if (i >= k - 1)
        t -= endTime[i - k + 1] - startTime[i - k + 1];
}
return rtn;
```

## Comparison

| Approach        | Time | Space |
|----------------|------|--------|
| Prefix sum     | O(n) | O(n)   |
| Sliding window | O(n) | O(1)   |

## Key Insights

1. **Window of k meetings:** The best free block we can create by rescheduling at most k meetings is the maximum over all contiguous windows of k meetings: free time = span length − total duration of those k meetings.
2. **Span boundaries:** `left` = end of meeting before the window (or 0); `right` = start of meeting after the window (or `eventTime`).
3. **Prefix sum vs sliding window:** Same formula; sliding window avoids extra array for O(1) space.

## Related Problems

- [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) — Check if all meetings can be attended
- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) — Minimum rooms needed
