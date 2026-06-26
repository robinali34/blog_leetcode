---
layout: post
title: "[Medium] 435. Non-overlapping Intervals"
date: 2026-01-03 02:00:00 -0700
categories: [leetcode, medium, array, greedy, sorting, intervals, dynamic-programming]
permalink: /2026/01/03/medium-435-non-overlapping-intervals/
---
Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return *the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping*.

Note that intervals that only touch at the boundary (e.g., `[1,2]` and `[2,3]`) are considered non-overlapping.

## Examples

**Example 1:**
```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

**Example 2:**
```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

**Example 3:**
```
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= starti < endi <= 5 * 10^4`

## Thinking Process

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return *the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping*.

Note that intervals that only touch at the boundary (e.g., `[1,2]` and `[2,3]`) are considered non-overlapping.

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



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
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

## Solution

### **Solution: Greedy with End Time Sorting**

```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto& a, auto&b){
            return a[1] < b[1];
        });

        int remove = 0;
        int end = INT_MIN;
        for(auto& interval: intervals){
            if(interval[0] < end) {
                remove++;
            } else {
                end = interval[1];
            }
        }
        return remove;
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return *the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping*.

**How the code works:**
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `intervals = [[1,2],[2,3],[3,4],[1,3]]`, expected output `1`:

[1,3] can be removed and the rest of the intervals are non-overlapping.

**Time:** - **Sorting**: O(n log n) where n is the number of intervals · **Space:** O(1)

### **Algorithm Explanation:**

1. **Edge Case (Line 4)**:
   - If intervals array is empty, return 0 (no removals needed)

2. **Sort by End Time (Lines 6-8)**:
   - Sort intervals by their end time (`u[1] < v[1]`)
   - This ensures we process intervals with earlier end times first
   - **Key**: Sorting by end time allows greedy choice to be optimal

3. **Initialize (Lines 10-11)**:
   - `right`: End time of the last kept interval
   - Initialize with first interval's end time (we always keep the first interval)
   - `removals`: Counter for number of intervals to remove

4. **Process Remaining Intervals (Lines 12-18)**:
   - **For each interval** starting from index 1:
     - **If overlaps**: `intervals[i][0] < right`
       - Current interval's start is before last kept interval's end
       - Increment `removals` (we remove this overlapping interval)
     - **Else**: No overlap
       - Update `right` to current interval's end time
       - Keep this interval (don't increment removals)

### **Example Walkthrough:**

**Example 1: `intervals = [[1,2],[2,3],[3,4],[1,3]]`**

**After sorting by end time:**
```
Original: [[1,2],[2,3],[3,4],[1,3]]
Sorted:   [[1,2], [2,3], [1,3], [3,4]]
          [1,2] end=2
          [2,3] end=3
          [1,3] end=3
          [3,4] end=4
```

**Execution:**
```
Initial: right = 2 (from [1,2]), removals = 0

i=1: [2,3]
  Check: 2 < 2? No (no overlap)
  Keep: right = 3, removals = 0

i=2: [1,3]
  Check: 1 < 3? Yes (overlaps with [2,3])
  Remove: removals = 1

i=3: [3,4]
  Check: 3 < 3? No (no overlap, boundary touch is OK)
  Keep: right = 4, removals = 1

Result: 1 removal
Kept intervals: [1,2], [2,3], [3,4]
```

**Example 2: `intervals = [[1,2],[1,2],[1,2]]`**

**After sorting by end time:**
```
All intervals have same end time: [[1,2], [1,2], [1,2]]
```

**Execution:**
```
Initial: right = 2 (from first [1,2]), removals = 0

i=1: [1,2]
  Check: 1 < 2? Yes (overlaps)
  Remove: removals = 1

i=2: [1,2]
  Check: 1 < 2? Yes (overlaps)
  Remove: removals = 2

Result: 2 removals
Kept intervals: [1,2] (only the first one)
```

**Example 3: `intervals = [[1,2],[2,3]]`**

**After sorting by end time:**
```
Already sorted: [[1,2], [2,3]]
```

**Execution:**
```
Initial: right = 2 (from [1,2]), removals = 0

i=1: [2,3]
  Check: 2 < 2? No (no overlap, boundary touch is OK)
  Keep: right = 3, removals = 0

Result: 0 removals
Kept intervals: [1,2], [2,3]
```
## Algorithm Breakdown

### **Why Sort by End Time?**

Sorting by end time is crucial for the greedy strategy:

1. **Maximize Remaining Space**: Intervals with earlier end times leave more room for future intervals
2. **Optimal Choice**: Keeping the interval with earliest end time is always optimal
3. **Greedy Property**: This choice doesn't prevent optimal solutions later

**Counter-example (sorting by start time):**
```
Intervals: [[1,10], [2,3], [4,5]]

Sort by start: [[1,10], [2,3], [4,5]]
  Keep [1,10] → right = 10
  [2,3] overlaps (2 < 10) → remove
  [4,5] overlaps (4 < 10) → remove
  Removals: 2

Sort by end: [[2,3], [4,5], [1,10]]
  Keep [2,3] → right = 3
  [4,5] no overlap (4 >= 3) → keep, right = 5
  [1,10] overlaps (1 < 5) → remove
  Removals: 1 (optimal!)
```

### **Overlap Detection**

Two intervals `[a, b]` and `[c, d]` overlap if:
```
c < b  (current start < previous end)
```

**Why not `c <= b`?**
- The problem states: "intervals that only touch at the boundary are considered non-overlapping"
- So `[1,2]` and `[2,3]` are **not** overlapping
- We use `<` instead of `<=`

### **Greedy Strategy**

The algorithm uses a greedy strategy:
1. **Always keep the first interval** (after sorting)
2. **For each subsequent interval**:
   - If it doesn't overlap with the last kept interval → keep it
   - If it overlaps → remove it (we already have a better choice)

This maximizes the number of kept intervals, which minimizes removals.

## Time & Space Complexity

- **Time Complexity**: 
  - **Sorting**: O(n log n) where n is the number of intervals
  - **Iteration**: O(n) - single pass through sorted intervals
  - **Total**: O(n log n)
- **Space Complexity**: O(1)
  - Only using a few variables
  - Sorting is in-place (or O(n) if not in-place, but typically O(1) extra space)

## Key Points

1. **Sort by End Time**: Critical for greedy strategy to work
2. **Greedy Choice**: Keep intervals with earliest end times
3. **Overlap Check**: Use `<` not `<=` (boundary touch is non-overlapping)
4. **Optimal**: Greedy approach finds optimal solution
5. **Simple**: Straightforward implementation after sorting

## Common Mistakes

1. **Empty array**: `[]` → return 0
2. **Single interval**: `[[1,2]]` → return 0
3. **No overlaps**: `[[1,2],[3,4],[5,6]]` → return 0
4. **All overlap**: `[[1,3],[1,3],[1,3]]` → return 2
5. **Boundary touch**: `[[1,2],[2,3]]` → return 0 (non-overlapping)
6. **Nested intervals**: `[[1,5],[2,3],[4,6]]` → return 1

1. **Wrong sort key**: Sorting by start time instead of end time
2. **Wrong overlap condition**: Using `<=` instead of `<`
3. **Not handling empty input**: Forgetting edge case
4. **Wrong initialization**: Not initializing `right` correctly
5. **Off-by-one error**: Starting loop from wrong index

## Related Problems

- [56. Merge Intervals](https://www.leetcode.com/problems/merge-intervals/) - Merge overlapping intervals
- [252. Meeting Rooms](https://www.leetcode.com/problems/meeting-rooms/) - Check if intervals overlap
- [253. Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/) - Count overlapping intervals
- [452. Minimum Number of Arrows to Burst Balloons](https://www.leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) - Similar greedy interval problem
- [646. Maximum Length of Pair Chain](https://www.leetcode.com/problems/maximum-length-of-pair-chain/) - Find longest chain of non-overlapping intervals

## Tags

`Array`, `Greedy`, `Sorting`, `Intervals`, `Dynamic Programming`, `Medium`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 435: Non-overlapping Intervals on LeetCode](https://www.leetcode.com/problems/non-overlapping-intervals/)
- [LeetCode Discuss — LC 435: Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/non-overlapping-intervals/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
