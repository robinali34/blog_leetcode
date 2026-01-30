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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Interval format**: Are intervals inclusive or exclusive? (Assumption: Typically inclusive on both ends [start, end] - need to clarify)

2. **Overlap definition**: What constitutes an overlap? (Assumption: Two intervals overlap if they share any common point - [a, b] overlaps [c, d] if max(a, c) <= min(b, d))

3. **Merging rule**: How should we merge overlapping intervals? (Assumption: Combine into single interval [min(start1, start2), max(end1, end2)])

4. **Output format**: Should we return merged intervals or modify input? (Assumption: Return new array of merged intervals - don't modify input)

5. **Order requirement**: Does the order of intervals matter? (Assumption: No - can sort first, then merge - output order doesn't matter)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to merge intervals. Let me check all pairs of intervals."

**Naive Solution**: Check all pairs of intervals, merge overlapping ones, repeat until no more merges possible.

**Complexity**: O(n²) time, O(n) space

**Issues**:
- O(n²) time - inefficient
- May need multiple passes
- Doesn't leverage sorting
- Can be optimized

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can sort intervals by start time, then merge adjacent overlapping intervals."

**Improved Solution**: Sort intervals by start time. Traverse sorted intervals, merge with previous if overlapping.

**Complexity**: O(n log n) time, O(n) space

**Improvements**:
- Sorting enables single-pass merging
- O(n log n) time is much better
- Handles all cases correctly
- Clean and intuitive

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "Sort and merge approach is optimal. Can optimize space by modifying in-place."

**Best Solution**: Sort intervals by start time. Traverse and merge: if current overlaps with last merged interval, update end; otherwise add new interval.

**Complexity**: O(n log n) time, O(n) space

**Key Realizations**:
1. Sorting is key insight
2. O(n log n) time is optimal for sorting approach
3. Single pass after sorting is efficient
4. O(n) space for result is necessary

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
            if(!merged.size() || merged.back()[1] < left) {
                merged.push_back({left, right});
            } else {
                merged.back()[1] = max (merged.back()[1], right);
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

## Follow-Up: Merge Intervals from Two Arrays

**Problem:** Given two arrays of intervals `arr1` and `arr2`, merge all intervals from both arrays into one merged array.

**Example:**
```
Input: 
  arr1 = [[1,3],[2,6],[8,10]]
  arr2 = [[2,4],[7,9],[15,18]]

Output: [[1,6],[7,10],[15,18]]
Explanation: 
  - [1,3] and [2,6] from arr1 merge to [1,6]
  - [2,4] from arr2 overlaps with [1,6] → merge to [1,6]
  - [8,10] from arr1 and [7,9] from arr2 merge to [7,10]
  - [15,18] from arr2 is separate
```

### Solution: Combine, Sort, and Merge

**Time Complexity:** O((m+n) log(m+n)) where m and n are sizes of arr1 and arr2  
**Space Complexity:** O(m+n)

The key insight is to combine both arrays, sort all intervals together, then apply the standard merge algorithm.

```cpp
class Solution {
public:
    vector<vector<int>> mergeTwoArrays(
        vector<vector<int>>& arr1, 
        vector<vector<int>>& arr2
    ) {
        // Combine both arrays
        vector<vector<int>> combined;
        combined.insert(combined.end(), arr1.begin(), arr1.end());
        combined.insert(combined.end(), arr2.begin(), arr2.end());
        
        // Sort by start time
        sort(combined.begin(), combined.end());
        
        // Merge overlapping intervals
        vector<vector<int>> merged;
        for(int i = 0; i < (int)combined.size(); i++) {
            int left = combined[i][0], right = combined[i][1];
            
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

### Alternative: More Efficient Approach

**Time Complexity:** O(m log m + n log n + m + n)  
**Space Complexity:** O(m + n)

First merge each array individually, then merge the two merged arrays using two pointers.

```cpp
class Solution {
private:
    // Helper function to merge intervals in one array
    vector<vector<int>> mergeOneArray(vector<vector<int>>& intervals) {
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
    
public:
    vector<vector<int>> mergeTwoArrays(
        vector<vector<int>>& arr1, 
        vector<vector<int>>& arr2
    ) {
        // Merge each array individually
        vector<vector<int>> merged1 = mergeOneArray(arr1);
        vector<vector<int>> merged2 = mergeOneArray(arr2);
        
        // Merge the two merged arrays using two pointers
        vector<vector<int>> result;
        int i = 0, j = 0;
        
        while(i < merged1.size() || j < merged2.size()) {
            // Choose the interval with smaller start time
            vector<int> current;
            if(j >= merged2.size() || 
               (i < merged1.size() && merged1[i][0] <= merged2[j][0])) {
                current = merged1[i++];
            } else {
                current = merged2[j++];
            }
            
            // Merge with last interval in result if overlapping
            if(result.size() == 0 || result.back()[1] < current[0]) {
                result.push_back(current);
            } else {
                result.back()[1] = max(result.back()[1], current[1]);
            }
        }
        
        return result;
    }
};
```

### How the Two-Pointer Approach Works

**Step-by-Step Example:**
```
arr1 (merged): [[1,6], [8,10]]
arr2 (merged): [[2,4], [7,9], [15,18]]

Step 1: Compare [1,6] and [2,4]
  Choose [1,6] (smaller start)
  result = [[1,6]]

Step 2: Compare [8,10] and [2,4]
  Choose [2,4] (smaller start)
  Check: 6 >= 2 → overlap → merge
  result.back()[1] = max(6, 4) = 6
  result = [[1,6]]

Step 3: Compare [8,10] and [7,9]
  Choose [7,9] (smaller start)
  Check: 6 < 7 → no overlap → add
  result = [[1,6], [7,9]]

Step 4: Compare [8,10] and [15,18]
  Choose [8,10] (smaller start)
  Check: 9 >= 8 → overlap → merge
  result.back()[1] = max(9, 10) = 10
  result = [[1,6], [7,10]]

Step 5: Only [15,18] remains
  Add [15,18]
  result = [[1,6], [7,10], [15,18]]
```

### Complexity Comparison

| Approach | Time Complexity | Space Complexity | Pros | Cons |
|----------|----------------|------------------|------|------|
| **Combine & Sort** | O((m+n) log(m+n)) | O(m+n) | Simple, straightforward | Sorts all intervals together |
| **Two-Pointer Merge** | O(m log m + n log n + m + n) | O(m+n) | More efficient if arrays are pre-sorted | More complex implementation |

**When to use each:**
- **Combine & Sort**: Simpler code, good when arrays are small or unsorted
- **Two-Pointer**: More efficient when arrays are already sorted or large

### Key Insights for Follow-Up

1. **Combine first**: Merge both arrays before sorting
2. **Same merge logic**: After combining, use the same overlap detection
3. **Two-pointer optimization**: Can merge two already-merged arrays efficiently
4. **Pre-sorting benefit**: If arrays are pre-sorted, two-pointer is optimal

---

*This problem is a classic interval merging problem that demonstrates the importance of sorting and efficient overlap detection.*
