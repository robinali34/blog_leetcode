---
layout: post
title: "[Medium] 56. Merge Intervals"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp array sorting interval problem-solving
permalink: /posts/2025-11-24-medium-56-merge-intervals/
tags: [leetcode, medium, array, sorting, intervals, merge]
---

# [Medium] 56. Merge Intervals

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

## Examples

**Example 1:**
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

**Example 2:**
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`

## Solution: Sort and Merge

**Time Complexity:** O(n log n) - dominated by sorting  
**Space Complexity:** O(n) - for the merged result

The key insight is to sort intervals by start time, then merge overlapping intervals by comparing with the last merged interval.

### Solution: Sort and Merge

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.size() == 0) return {};
        
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> merged;
        
        for(int i = 0; i < (int)intervals.size(); i++) {
            int left = intervals[i][0], right = intervals[i][1];
            
            if(merged.size() == 0 || merged.back()[1] < left) {
                merged.push_back({left, right});
            } else {
                merged.back()[1] = max(merged.back()[1], right);
            }
        }
        
        return merged;
    }
};
```

## How the Algorithm Works

### Key Insight: Sort First

**Why sort?**
- After sorting by start time, overlapping intervals become adjacent
- We only need to compare each interval with the last merged interval
- If current interval doesn't overlap with last merged, it won't overlap with any previous ones

### Step-by-Step Example: `intervals = [[1,3],[2,6],[8,10],[15,18]]`

```
Step 1: Sort intervals (already sorted)
  intervals = [[1,3], [2,6], [8,10], [15,18]]

Step 2: Initialize
  merged = []

Step 3: Process [1,3]
  merged is empty → add [1,3]
  merged = [[1,3]]

Step 4: Process [2,6]
  Check: merged.back()[1] = 3, current left = 2
  Since 3 >= 2, intervals overlap → merge
  merged.back()[1] = max(3, 6) = 6
  merged = [[1,6]]

Step 5: Process [8,10]
  Check: merged.back()[1] = 6, current left = 8
  Since 6 < 8, no overlap → add [8,10]
  merged = [[1,6], [8,10]]

Step 6: Process [15,18]
  Check: merged.back()[1] = 10, current left = 15
  Since 10 < 15, no overlap → add [15,18]
  merged = [[1,6], [8,10], [15,18]]

Final: [[1,6], [8,10], [15,18]]
```

**Visual Representation:**
```
Before:  [1,3]  [2,6]  [8,10]  [15,18]
         └─┬─┘
           └─── Overlap ───┘

After:   [1,6]  [8,10]  [15,18]
```

## Key Insights

1. **Sorting is crucial**: Sort by start time to make overlapping intervals adjacent
2. **Compare with last merged**: Only need to check overlap with the last interval in merged list
3. **Overlap condition**: Two intervals `[a,b]` and `[c,d]` overlap if `c <= b`
4. **Merge by extending**: When overlapping, extend end time to `max(b, d)`

## Algorithm Breakdown

### Sorting

```cpp
sort(intervals.begin(), intervals.end());
```

**Why this works:**
- `vector<vector<int>>` sorts lexicographically
- First compares `intervals[i][0]` (start time)
- If equal, compares `intervals[i][1]` (end time)
- This gives us intervals sorted by start time

### Merging Logic

```cpp
if(merged.size() == 0 || merged.back()[1] < left) {
    merged.push_back({left, right});
} else {
    merged.back()[1] = max(merged.back()[1], right);
}
```

**Breakdown:**
- **Empty merged list**: First interval, add it
- **No overlap**: `merged.back()[1] < left` means current interval starts after last ends
- **Overlap**: `merged.back()[1] >= left` means intervals overlap, extend end time

### Overlap Detection

**Two intervals overlap if:**
```
[a, b] and [c, d] overlap when: c <= b
```

**Why `c <= b`?**
- If `c <= b`, the start of second interval is before/at the end of first
- This means they overlap or are adjacent (which counts as overlap)

**Examples:**
- `[1,3]` and `[2,6]`: `2 <= 3` → overlap ✓
- `[1,4]` and `[4,5]`: `4 <= 4` → overlap ✓ (adjacent counts)
- `[1,3]` and `[4,6]`: `4 <= 3` → no overlap ✗

## Edge Cases

1. **Empty input**: Return empty array
2. **Single interval**: Return as-is
3. **All intervals overlap**: Merge into one interval
4. **No overlaps**: Return all intervals unchanged
5. **Adjacent intervals**: `[1,4]` and `[4,5]` merge to `[1,5]`
6. **Nested intervals**: `[1,6]` and `[2,4]` merge to `[1,6]`

## Alternative Approaches

### Approach 2: Custom Comparator

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.empty()) return {};
        
        sort(intervals.begin(), intervals.end(), 
             [](const vector<int>& a, const vector<int>& b) {
                 return a[0] < b[0];
             });
        
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        
        for(int i = 1; i < intervals.size(); i++) {
            if(intervals[i][0] <= merged.back()[1]) {
                merged.back()[1] = max(merged.back()[1], intervals[i][1]);
            } else {
                merged.push_back(intervals[i]);
            }
        }
        
        return merged;
    }
};
```

**Pros:**
- Explicit comparator makes intent clear
- Slightly more readable

**Cons:**
- More verbose
- Same complexity

### Approach 3: In-Place Merging

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1) excluding output

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.empty()) return {};
        
        sort(intervals.begin(), intervals.end());
        
        int writeIdx = 0;
        for(int i = 1; i < intervals.size(); i++) {
            if(intervals[i][0] <= intervals[writeIdx][1]) {
                intervals[writeIdx][1] = max(intervals[writeIdx][1], intervals[i][1]);
            } else {
                writeIdx++;
                intervals[writeIdx] = intervals[i];
            }
        }
        
        intervals.resize(writeIdx + 1);
        return intervals;
    }
};
```

**Pros:**
- O(1) extra space (modifies input)
- More memory efficient

**Cons:**
- Modifies input array
- Less intuitive

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Sort and Merge** | O(n log n) | O(n) | Simple, clear | Extra space |
| **Custom Comparator** | O(n log n) | O(n) | Explicit | More verbose |
| **In-Place** | O(n log n) | O(1) | Space efficient | Modifies input |

## Implementation Details

### Why Lexicographic Sort Works

```cpp
sort(intervals.begin(), intervals.end());
```

**For `vector<vector<int>>`:**
- Compares first element (`intervals[i][0]`)
- If equal, compares second element (`intervals[i][1]`)
- This sorts by start time, then by end time if starts are equal

**Example:**
```
Before: [[2,6], [1,3], [8,10]]
After:  [[1,3], [2,6], [8,10]]
```

### Overlap Condition Explained

```cpp
merged.back()[1] < left  // No overlap
merged.back()[1] >= left // Overlap
```

**Why this works:**
- `merged.back()[1]` is the end time of last merged interval
- `left` is the start time of current interval
- If `end < start`, there's a gap → no overlap
- If `end >= start`, they overlap or are adjacent

### Merge Operation

```cpp
merged.back()[1] = max(merged.back()[1], right);
```

**Why max?**
- When merging `[a,b]` and `[c,d]` where `c <= b`
- New interval is `[a, max(b,d)]`
- We keep the earlier start (`a`) and later end (`max(b,d)`)

## Common Mistakes

1. **Forgetting to sort**: Without sorting, algorithm fails
2. **Wrong overlap condition**: Using `>=` instead of `<=` or vice versa
3. **Not handling empty input**: Forgetting edge case
4. **Wrong merge logic**: Not using `max()` for end time
5. **Index out of bounds**: Not checking `merged.size() == 0`

## Optimization Tips

1. **Early return**: Check empty input first
2. **Reserve space**: Can reserve `intervals.size()` for `merged` if needed
3. **In-place if allowed**: Use in-place approach to save space

## Related Problems

- [57. Insert Interval](https://leetcode.com/problems/insert-interval/) - Insert and merge
- [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) - Check if intervals overlap
- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) - Count overlapping intervals
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) - Remove minimum intervals
- [1094. Car Pooling](https://leetcode.com/problems/car-pooling/) - Interval scheduling

## Real-World Applications

1. **Calendar Scheduling**: Merging overlapping time slots
2. **Resource Allocation**: Combining overlapping resource reservations
3. **Network Routing**: Merging overlapping IP ranges
4. **Database Queries**: Optimizing range queries
5. **Event Management**: Consolidating overlapping events

## Pattern Recognition

This problem demonstrates the **"Interval Merging"** pattern:

```
1. Sort intervals by start time
2. Iterate through sorted intervals
3. Compare current with last merged interval
4. If overlap → merge by extending end time
5. If no overlap → add as new interval
```

Similar problems:
- Insert Interval
- Meeting Rooms
- Non-overlapping Intervals
- Car Pooling

## Step-by-Step Trace: `intervals = [[1,4],[0,4]]`

```
Step 1: Sort intervals
  Before: [[1,4], [0,4]]
  After:  [[0,4], [1,4]]  (sorted by start time)

Step 2: Initialize
  merged = []

Step 3: Process [0,4]
  merged is empty → add [0,4]
  merged = [[0,4]]

Step 4: Process [1,4]
  Check: merged.back()[1] = 4, current left = 1
  Since 4 >= 1, intervals overlap → merge
  merged.back()[1] = max(4, 4) = 4
  merged = [[0,4]]

Final: [[0,4]]
```

## Why Sorting is Essential

**Without sorting:**
```
Input: [[2,6], [1,3], [8,10]]
Process [2,6]: merged = [[2,6]]
Process [1,3]: Check 6 < 1? No, but [1,3] should merge with [2,6]!
               Algorithm fails because [1,3] comes after [2,6]
```

**With sorting:**
```
Input: [[1,3], [2,6], [8,10]]
Process [1,3]: merged = [[1,3]]
Process [2,6]: Check 3 >= 2? Yes → merge → [[1,6]]
Process [8,10]: Check 6 < 8? Yes → add → [[1,6], [8,10]]
```

## Interval Overlap Visualization

```
No Overlap:
  [a---b]        [c---d]
  └─ gap ─┘

Overlap:
  [a---b]
      [c---d]
  └─ overlap ─┘

Adjacent (counts as overlap):
  [a---b][c---d]
  └─ adjacent ─┘

Nested:
  [a--------b]
    [c---d]
  └─ nested ─┘
```

---

*This problem is a classic interval merging problem that demonstrates the importance of sorting and efficient overlap detection.*

