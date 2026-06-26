---
layout: post
title: "[Medium] 452. Minimum Number of Arrows to Burst Balloons"
date: 2026-01-03 03:00:00 -0700
categories: [leetcode, medium, array, greedy, sorting, intervals]
permalink: /2026/01/03/medium-452-minimum-number-of-arrows-to-burst-balloons/
---
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D array `points` where `points[i] = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is **burst** by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return *the **minimum number of arrows** that must be shot to burst all balloons*.

## Examples

**Example 1:**
```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
```

**Example 2:**
```
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon.
```

**Example 3:**
```
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
```

## Constraints

- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-2^31 <= xstart < xend <= 2^31 - 1`

## Thinking Process

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D array `points` where `points[i] = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is **burst** by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

## Solution

### **Solution: Greedy with End Coordinate Sorting**

```cpp
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0) return 0;
        sort(points.begin(), points.end(), [](const auto& u, const auto& v){
            return u[1] < v[1];
        });
        int pos = points[0][1];
        int arrows = 1;
        for(auto& ballon: points) {
            if(ballon[0] > pos) {
                pos = ballon[1];
                arrows++;
            }
        }
        return arrows;
    }
};
```

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D array `points` where `points[i] = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.

**How the code works:**
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `points = [[10,16],[2,8],[1,6],[7,12]]`, expected output `2`:

The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

**Time:** - **Sorting**: O(n log n) where n is the number of balloons · **Space:** O(1)

### **Algorithm Explanation:**

1. **Edge Case (Line 4)**:
   - If points array is empty, return 0 (no arrows needed)

2. **Sort by End Coordinate (Lines 5-7)**:
   - Sort balloons by their end coordinate (`u[1] < v[1]`)
   - This ensures we process balloons with earlier end coordinates first
   - **Key**: Sorting by end coordinate allows greedy choice to be optimal

3. **Initialize (Lines 8-9)**:
   - `pos`: Position of the last arrow shot (end coordinate of first balloon)
   - `arrows`: Number of arrows needed (start with 1 for the first balloon)

4. **Process Remaining Balloons (Lines 10-14)**:
   - **For each balloon** starting from index 1:
     - **If doesn't overlap**: `ballon[0] > pos`
       - Current balloon's start is after last arrow position
       - Shoot new arrow at this balloon's end coordinate
       - Update `pos` to current balloon's end
       - Increment `arrows`
     - **Else**: Balloon overlaps with current arrow position
       - Current arrow can burst this balloon (no new arrow needed)
       - Don't update `pos` (keep shooting at same position)

### **Example Walkthrough:**

**Example 1: `points = [[10,16],[2,8],[1,6],[7,12]]`**

**After sorting by end coordinate:**
```
Original: [[10,16],[2,8],[1,6],[7,12]]
Sorted:   [[1,6], [2,8], [7,12], [10,16]]
          [1,6] end=6
          [2,8] end=8
          [7,12] end=12
          [10,16] end=16
```

**Execution:**
```
Initial: pos = 6 (from [1,6]), arrows = 1

i=1: [2,8]
  Check: 2 > 6? No (overlaps, arrow at x=6 can burst it)
  No new arrow needed

i=2: [7,12]
  Check: 7 > 6? Yes (doesn't overlap)
  Shoot new arrow: pos = 12, arrows = 2

i=3: [10,16]
  Check: 10 > 12? No (overlaps, arrow at x=12 can burst it)
  No new arrow needed

Result: 2 arrows
Arrow positions: x=6 (bursts [1,6], [2,8]), x=12 (bursts [7,12], [10,16])
```

**Example 2: `points = [[1,2],[3,4],[5,6],[7,8]]`**

**After sorting by end coordinate:**
```
Already sorted: [[1,2], [3,4], [5,6], [7,8]]
```

**Execution:**
```
Initial: pos = 2 (from [1,2]), arrows = 1

i=1: [3,4]
  Check: 3 > 2? Yes (doesn't overlap)
  Shoot new arrow: pos = 4, arrows = 2

i=2: [5,6]
  Check: 5 > 4? Yes (doesn't overlap)
  Shoot new arrow: pos = 6, arrows = 3

i=3: [7,8]
  Check: 7 > 6? Yes (doesn't overlap)
  Shoot new arrow: pos = 8, arrows = 4

Result: 4 arrows (one for each balloon)
```

**Example 3: `points = [[1,2],[2,3],[3,4],[4,5]]`**

**After sorting by end coordinate:**
```
Already sorted: [[1,2], [2,3], [3,4], [4,5]]
```

**Execution:**
```
Initial: pos = 2 (from [1,2]), arrows = 1

i=1: [2,3]
  Check: 2 > 2? No (overlaps, arrow at x=2 can burst it)
  No new arrow needed

i=2: [3,4]
  Check: 3 > 2? Yes (doesn't overlap)
  Shoot new arrow: pos = 4, arrows = 2

i=3: [4,5]
  Check: 4 > 4? No (overlaps, arrow at x=4 can burst it)
  No new arrow needed

Result: 2 arrows
Arrow positions: x=2 (bursts [1,2], [2,3]), x=4 (bursts [3,4], [4,5])
```

## Algorithm Breakdown

### **Why Sort by End Coordinate?**

Sorting by end coordinate is crucial for the greedy strategy:

1. **Maximize Coverage**: Shooting at the end of a balloon maximizes the number of overlapping balloons we can burst
2. **Optimal Choice**: This choice is always optimal (doesn't prevent optimal solutions later)
3. **Greedy Property**: Shooting at the earliest end coordinate leaves maximum room for future balloons

**Counter-example (sorting by start coordinate):**
```
Balloons: [[1,10], [2,3], [4,5]]

Sort by start: [[1,10], [2,3], [4,5]]
  Shoot at x=10 → bursts [1,10]
  [2,3] overlaps (2 <= 10) → already burst
  [4,5] overlaps (4 <= 10) → already burst
  Arrows: 1

Sort by end: [[2,3], [4,5], [1,10]]
  Shoot at x=3 → bursts [2,3]
  [4,5] doesn't overlap (4 > 3) → shoot at x=5
  [1,10] overlaps (1 <= 5) → already burst
  Arrows: 2

Wait, this doesn't show the issue. Let me think of a better example...

Actually, sorting by end is correct. The issue with sorting by start would be:
[[1,6], [2,3], [4,5]]

Sort by start: [[1,6], [2,3], [4,5]]
  Shoot at x=6 → bursts all (optimal, 1 arrow)

Sort by end: [[2,3], [4,5], [1,6]]
  Shoot at x=3 → bursts [2,3]
  [4,5] doesn't overlap (4 > 3) → shoot at x=5
  [1,6] overlaps (1 <= 5) → already burst
  Arrows: 2 (suboptimal!)

Hmm, but wait - if we shoot at x=6 in the sorted-by-end approach, we'd get:
  Shoot at x=6 → bursts [2,3], [1,6]
  [4,5] overlaps (4 <= 6) → already burst
  Arrows: 1 (optimal!)

The key is that we shoot at the END of the first balloon, which is x=3, not x=6. But [1,6] starts at 1, which is <= 3, so it should be burst. But [1,6] ends at 6, which is after 3, so if we shoot at x=3, we can't burst [1,6] because 3 is not in [1,6]... wait, 3 IS in [1,6] (1 <= 3 <= 6), so it should work.

Actually, I think the algorithm is correct. Let me verify with the actual execution:
- After sorting by end: [[2,3], [4,5], [1,6]]
- pos = 3, arrows = 1
- [4,5]: 4 > 3? Yes → new arrow at x=5, arrows=2
- [1,6]: 1 > 5? No → overlaps, already burst by arrow at x=5

But wait, arrow at x=5 cannot burst [1,6] because 5 is in [1,6]? Yes, 1 <= 5 <= 6, so it can burst it. So the algorithm is correct.

The key insight is that we shoot at the END of balloons, and a balloon [a,b] can be burst by an arrow at x if a <= x <= b. So if we shoot at x=5, it can burst [1,6] because 1 <= 5 <= 6.
```

### **Overlap Detection**

Two balloons `[a, b]` and `[c, d]` can be burst by the same arrow if they overlap:
```
They overlap if: c <= b (current start <= previous end)
```

**Why `>` not `>=`?**
- We check `ballon[0] > pos` to see if we need a new arrow
- If `ballon[0] <= pos`, the balloon overlaps with the current arrow position
- The arrow at `pos` can burst this balloon (since `ballon[0] <= pos <= ballon[1]`)

### **Greedy Strategy**

The algorithm uses a greedy strategy:
1. **Sort by end coordinate**: Process balloons with earlier end coordinates first
2. **Shoot at end**: Always shoot arrow at the end coordinate of the first balloon in a group
3. **Maximize coverage**: This maximizes the number of overlapping balloons burst by one arrow

This minimizes the number of arrows needed.

## Time & Space Complexity

- **Time Complexity**: 
  - **Sorting**: O(n log n) where n is the number of balloons
  - **Iteration**: O(n) - single pass through sorted balloons
  - **Total**: O(n log n)
- **Space Complexity**: O(1)
  - Only using a few variables
  - Sorting is in-place (or O(n) if not in-place, but typically O(1) extra space)

## Key Points

1. **Sort by End Coordinate**: Critical for greedy strategy to work
2. **Greedy Choice**: Shoot arrow at end of first balloon in each group
3. **Overlap Check**: Use `>` to check if new arrow needed
4. **Boundary Touch**: Balloons touching at boundary can be burst by same arrow
5. **Optimal**: Greedy approach finds optimal solution

## Common Mistakes

1. **Empty array**: `[]` → return 0
2. **Single balloon**: `[[1,2]]` → return 1
3. **No overlaps**: `[[1,2],[3,4],[5,6]]` → return 3
4. **All overlap**: `[[1,5],[2,6],[3,7]]` → return 1
5. **Boundary touch**: `[[1,2],[2,3],[3,4]]` → return 2
6. **Nested balloons**: `[[1,10],[2,3],[4,5]]` → return 1

1. **Wrong sort key**: Sorting by start coordinate instead of end coordinate
2. **Wrong overlap condition**: Using `>=` instead of `>`
3. **Not handling empty input**: Forgetting edge case
4. **Wrong initialization**: Not initializing `pos` and `arrows` correctly
5. **Off-by-one error**: Starting loop from wrong index

## Related Problems

- [435. Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/) - Remove minimum intervals (similar greedy)
- [56. Merge Intervals](https://www.leetcode.com/problems/merge-intervals/) - Merge overlapping intervals
- [253. Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/) - Count overlapping intervals
- [646. Maximum Length of Pair Chain](https://www.leetcode.com/problems/maximum-length-of-pair-chain/) - Find longest chain

## Tags

`Array`, `Greedy`, `Sorting`, `Intervals`, `Medium`

## Key Takeaways

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

## References

- [LC 452: Minimum Number of Arrows to Burst Balloons on LeetCode](https://www.leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
- [LeetCode Discuss — LC 452: Minimum Number of Arrows to Burst Balloons](https://www.leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
