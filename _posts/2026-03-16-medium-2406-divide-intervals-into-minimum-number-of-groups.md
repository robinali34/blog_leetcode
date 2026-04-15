---
layout: post
title: "[Medium] 2406. Divide Intervals Into Minimum Number of Groups"
date: 2026-03-16
categories: [leetcode, medium, greedy, heap, intervals]
tags: [leetcode, medium, greedy, heap, intervals, sweep-line]
permalink: /2026/03/16/medium-2406-divide-intervals-into-minimum-number-of-groups/
---

You are given a 2D array `intervals` where `intervals[i] = [left_i, right_i]` represents the **inclusive** interval `[left_i, right_i]`. Divide the intervals into one or more **groups** such that no two intervals in the same group **overlap** (two intervals overlap if there is at least one common number). Return the **minimum** number of groups needed.

## Examples

**Example 1:**

```
Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation:
  Group 1: [1,5], [6,8]
  Group 2: [2,3], [5,10]
  Group 3: [1,10]
No two intervals in the same group overlap.
```

**Example 2:**

```
Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: No intervals overlap, so one group is enough.
```

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `1 <= left_i <= right_i <= 10^6`

## Thinking Process

### Key Insight

The minimum number of groups = the **maximum number of intervals that overlap at any point in time**.

This is the classic **meeting rooms II** pattern: each interval is a "meeting," and each group is a "room." We need the minimum number of rooms so no two meetings in the same room overlap.

### Greedy + Min-Heap Strategy

1. **Sort** intervals by start time
2. Use a **min-heap** tracking the end times of each group's last interval
3. For each new interval:
   - If the earliest-ending group finishes **before** the new interval starts (`pq.top() < start`), reuse that group (pop it)
   - Push the new interval's end time onto the heap
4. The heap size at the end = minimum number of groups

### Walk-through

```
intervals (sorted): [1,5], [1,10], [2,3], [5,10], [6,8]
                     min-heap (end times)

[1,5]:   heap empty → push 5          heap = {5}
[1,10]:  top=5, 5 < 1? No → push 10  heap = {5, 10}
[2,3]:   top=5, 5 < 2? No → push 3   heap = {3, 5, 10}
[5,10]:  top=3, 3 < 5? Yes → pop 3, push 10  heap = {5, 10, 10}
[6,8]:   top=5, 5 < 6? Yes → pop 5, push 8   heap = {8, 10, 10}

Answer: heap.size() = 3
```

### Why `<` and Not `<=`?

Intervals are **inclusive**: `[1,5]` and `[5,10]` share the point 5, so they overlap. We can only reuse a group when `pq.top() < start` (strictly less), not `<=`.

## Solution: Greedy + Min-Heap -- $O(n \log n)$

{% raw %}
```cpp
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        priority_queue<int, vector<int>, greater<int>> pq;

        for (auto& interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            if (!pq.empty() && pq.top() < start) {
                pq.pop();
            }
            pq.push(end);
        }

        return pq.size();
    }
};
```
{% endraw %}

**Time**: $O(n \log n)$ -- sorting + heap operations
**Space**: $O(n)$ -- heap can hold all intervals in the worst case

## Solution 2: Sweep Line (Line Sweep) -- $O(n \log n)$

Instead of simulating group assignment, directly compute the **maximum overlap** using a sweep line.

**Idea**: For each interval $[l, r]$, create two events:
- $+1$ at time $l$ (an interval starts)
- $-1$ at time $r+1$ (an interval ends -- `+1` because endpoints are inclusive)

Sort events by time, sweep through, and track the running count. The peak = minimum groups.

{% raw %}
```cpp
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        vector<pair<int, int>> events;
        for (auto& interval : intervals) {
            events.push_back({interval[0], 1});
            events.push_back({interval[1] + 1, -1});
        }
        sort(events.begin(), events.end());

        int curr = 0;
        int maxOverlap = 0;
        for (auto& [time, val] : events) {
            curr += val;
            maxOverlap = max(maxOverlap, curr);
        }
        return maxOverlap;
    }
};
```
{% endraw %}

**Time**: $O(n \log n)$ -- sorting events
**Space**: $O(n)$ -- events array

### Why `end + 1`?

Since intervals are **inclusive**, `[1,5]` and `[5,10]` overlap at point 5. The end event must be placed at `r + 1` so the $-1$ fires *after* the inclusive endpoint, correctly counting both intervals as overlapping at `r`.

## Common Mistakes

- Using `<=` instead of `<` for the reuse check (intervals are inclusive, so equal endpoints overlap)
- Forgetting to sort by start time first
- Popping more than one element from the heap per interval (we only free the earliest-ending group)

## Key Takeaways

- **"Minimum groups with no overlap"** = **"Maximum overlap at any point"** = Meeting Rooms II pattern
- Sort by start + min-heap of end times is the standard $O(n \log n)$ approach
- The strict `<` vs `<=` depends on whether endpoints are inclusive or exclusive -- always check the problem statement

## Related Problems

- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) -- identical pattern (exclusive endpoints)
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) -- greedy interval scheduling
- [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) -- greedy intervals
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) -- interval merging

## Template Reference

- [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/)
