---
layout: post
title: "[Medium] 1353. Maximum Number of Events That Can Be Attended"
date: 2026-04-13
categories: [leetcode, medium, greedy, heap]
tags: [leetcode, medium, greedy, heap, sorting, scheduling]
permalink: /2026/04/13/medium-1353-maximum-number-of-events-that-can-be-attended/
---

You are given an array of `events` where `events[i] = [startDay, endDay]`. You can attend an event on **any single day** in the range `[startDay, endDay]`. You can only attend **one event per day**. Return the **maximum number of events** you can attend.

## Examples

**Example 1:**

```
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: Attend all three:
  Day 1 → event [1,2]
  Day 2 → event [2,3]
  Day 3 → event [3,4]
```

**Example 2:**

```
Input: events = [[1,2],[2,3],[3,4],[1,2]]
Output: 4
Explanation:
  Day 1 → event [1,2] (first)
  Day 2 → event [1,2] (second)
  Day 2 → can't, already used. Day 3 → event [2,3]
  Day 4 → event [3,4]
```

## Constraints

- `1 <= events.length <= 10^5`
- `events[i].length == 2`
- `1 <= startDay <= endDay <= 10^5`

## Thinking Process

### Key Observations

1. **Each event is flexible** -- you don't have to attend on the start day; any day in `[start, end]` works
2. **Greedy insight**: on any given day, attend the event that **expires soonest** (smallest end day). Delaying it risks losing it forever, while events with later deadlines are safer to postpone
3. **Efficient simulation**: move day by day, maintain available events in a min-heap, pick the one expiring soonest

### Algorithm

1. **Sort** events by start day
2. Use a **min-heap** of end days (earliest deadline on top)
3. Iterate by day:
   - Add all newly available events (start day ≤ current day)
   - Remove expired events from the heap (end day < current day)
   - Attend the event with the smallest end day (pop from heap)
   - Advance to the next day

### Walk-through

```
events (sorted): [[1,2], [1,2], [2,3], [3,4]]

Day 1: add [1,2],[1,2] → heap={2,2}
        attend end=2 → heap={2}, rtn=1

Day 2: add [2,3] → heap={2,3}
        attend end=2 → heap={3}, rtn=2

Day 3: add [3,4] → heap={3,4}
        attend end=3 → heap={4}, rtn=3

Day 4: attend end=4 → heap={}, rtn=4

Answer: 4 ✓
```

### Why Skip to the Next Event's Start?

If the heap is empty and there are more events, we jump `day` forward to `events[i][0]` instead of incrementing one by one. This avoids iterating through idle days and keeps the algorithm efficient.

## Solution: Sort + Greedy Min-Heap -- $O(n \log n)$

{% raw %}
```cpp
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end());
        priority_queue<int, vector<int>, greater<int>> pq;
        int n = events.size();
        int i = 0, day = 0, rtn = 0;

        while (i < n || !pq.empty()) {
            if (pq.empty()) day = events[i][0];
            while (i < n && events[i][0] <= day) {
                pq.push(events[i][1]);
                i++;
            }
            while (!pq.empty() && pq.top() < day) pq.pop();
            if (!pq.empty()) {
                pq.pop();
                rtn++;
                day++;
            }
        }
        return rtn;
    }
};
```
{% endraw %}

**Time**: $O(n \log n)$ -- sorting + each event enters/leaves the heap once
**Space**: $O(n)$ -- heap

## Key Details

**Why min-heap of end days (not start days)?**
We want to prioritize the event that expires soonest. Start days don't matter once an event is available -- only the deadline matters for the greedy choice.

**Why `pq.top() < day` (not `<=`)?**
An event with `end == day` is still valid today. We only discard events whose end day is strictly **before** the current day.

**Why the `if (pq.empty()) day = events[i][0]` jump?**
Without this, we'd increment `day` through potentially thousands of idle days. Jumping to the next event's start keeps the outer loop proportional to $O(n)$ iterations.

## Common Mistakes

- Sorting by end day instead of start day (need start day ordering to add events as days progress)
- Not removing expired events before picking (could "attend" an already-expired event)
- Incrementing `day` one by one even when the heap is empty (TLE on large gaps)

## Key Takeaways

- **"Maximize events attended with earliest-deadline-first"** = sort by start + min-heap of end days
- This is a variant of the **Earliest Deadline First (EDF)** scheduling strategy
- The pattern of "add available → remove expired → pick best" is common in event scheduling problems

## Related Problems

- [2406. Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) -- greedy + heap on intervals
- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) -- min-heap scheduling
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) -- greedy interval scheduling
- [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) -- DP interval scheduling

## Template Reference

- [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/)
