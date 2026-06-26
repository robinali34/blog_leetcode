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
| **Min/max heap** *(this problem)* | O(n log k) | O(k) | Top-K, streaming median |
| Two heaps | O(n log n) | O(n) | Median from data stream |
| Heap + lazy deletion | O(n log n) | O(n) | Delayed removal |
| Priority-driven search | O(n log n) | O(n) | Dijkstra, best-first expansion |

## Solution

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

### Solution Explanation

**Approach:** Min/max heap (this problem)

**Key idea:** ### Key Insight

**How the code works:**
1. **Sort** intervals by start time
2. Use a **min-heap** tracking the end times of each group's last interval
3. For each new interval:
- If the earliest-ending group finishes **before** the new interval starts (`pq.top() < start`), reuse that group (pop it)
- Push the new interval's end time onto the heap
4. The heap size at the end = minimum number of groups

**Walkthrough** — input `intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]`, expected output `3`:

Group 1: [1,5], [6,8]
  Group 2: [2,3], [5,10]
  Group 3: [1,10]
No two intervals in the same group overlap.
## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

- **"Minimum groups with no overlap"** = **"Maximum overlap at any point"** = Meeting Rooms II pattern
- Sort by start + min-heap of end times is the standard O(n log n) approach
- The strict `<` vs `<=` depends on whether endpoints are inclusive or exclusive -- always check the problem statement

## Related Problems

- [253. Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/) -- identical pattern (exclusive endpoints)
- [435. Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/) -- greedy interval scheduling
- [452. Minimum Number of Arrows to Burst Balloons](https://www.leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) -- greedy intervals
- [56. Merge Intervals](https://www.leetcode.com/problems/merge-intervals/) -- interval merging

## References

- [LC 2406: Divide Intervals Into Minimum Number of Groups on LeetCode](https://www.leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)
- [LeetCode Discuss — LC 2406: Divide Intervals Into Minimum Number of Groups](https://www.leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/editorial/) *(may require premium)*

## Template Reference

- [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/)
