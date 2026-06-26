---
layout: post
title: "[Medium] 253. Meeting Rooms II"
date: 2025-12-11 00:00:00 -0800
categories: leetcode algorithm medium cpp array sorting priority-queue two-pointers problem-solving
---
Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of conference rooms required.

## Examples

**Example 1:**
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

**Example 2:**
```
Input: intervals = [[7,10],[2,4]]
Output: 1
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `0 <= starti < endi <= 10^6`

## Thinking Process

Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of conference rooms required.

- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

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
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Solution

**Time Complexity:** O(n log n) - Sorting + heap operations  
**Space Complexity:** O(n) - For the heap

This approach uses a min-heap to track the end times of meetings currently using rooms. When a new meeting starts, we check if any room has freed up (earliest end time <= new start time).

```cpp
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) return 0;
        
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b){
            return a[0] < b[0];
        });
        
        priority_queue<int, vector<int>, greater<int>> allocator;
        allocator.push(intervals[0][1]);
        
        for(int i = 1; i < intervals.size(); i++) {
            if(intervals[i][0] >= allocator.top()) {
                allocator.pop();
            }
            allocator.push(intervals[i][1]);
        }
        
        return allocator.size();
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of conference rooms required.

**How the code works:**
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `intervals = [[0,30],[5,10],[15,20]]`, expected output `2`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Operation | Priority Queue | Chronological Ordering | Bucket Sort |
|-----------|----------------|------------------------|-------------|
| Sorting | O(n log n) | O(n log n) | N/A |
| Processing | O(n log n) | O(n) | O(n + k) |
| **Overall** | **O(n log n)** | **O(n log n)** | **O(n + k)** |

**Note:** For bucket sort, k = 10^6 (maximum time value), so O(n + k) is effectively O(n) when n is large, but has constant factor overhead.

### How Solution 1 Works

1. **Sort intervals** by start time to process meetings chronologically
2. **Initialize heap** with the end time of the first meeting
3. **For each subsequent meeting**:
   - If the earliest ending meeting has finished (`intervals[i][0] >= allocator.top()`), reuse that room (pop from heap)
   - Add the current meeting's end time to the heap
4. **Result**: The heap size represents the maximum number of concurrent meetings

### Key Insight

The min-heap always contains the end times of all currently active meetings. When a new meeting starts:
- If the earliest ending meeting has finished, we can reuse that room
- Otherwise, we need a new room
- The heap size tracks the maximum number of rooms needed at any point
## Example Walkthrough

**Input:** `intervals = [[0,30],[5,10],[15,20]]`

### Solution 1 (Priority Queue):
```
Sorted: [[0,30], [5,10], [15,20]]

Step 1: Meeting [0,30] starts
        Heap: [30]
        Rooms: 1

Step 2: Meeting [5,10] starts
        Check: 5 >= 30? No, need new room
        Heap: [10, 30]
        Rooms: 2

Step 3: Meeting [15,20] starts
        Check: 15 >= 10? Yes, room freed
        Pop 10, Heap: [30]
        Push 20, Heap: [20, 30]
        Rooms: 2

Result: 2 rooms needed
```

### Solution 2 (Chronological Ordering):
```
Start: [0, 5, 15]
End:   [10, 20, 30]

Timeline:
0:  Meeting starts → usedRooms = 1
5:  Meeting starts → usedRooms = 2
10: Meeting ends → usedRooms = 1
15: Meeting starts → usedRooms = 2
20: Meeting ends → usedRooms = 1
30: Meeting ends → usedRooms = 0

Maximum usedRooms = 2
```

### Solution 3 (Bucket Sort):
```
Intervals: [[0,30], [5,10], [15,20]]

Timeline array (showing relevant indices):
Index:  0   5   10  15  20  30
Value: +1  +1  -1  +1  -1  -1

Prefix sum:
Index:  0   5   10  15  20  30
Count:  1   2   1   2   1   0

Maximum count = 2
Result: 2 rooms needed
```

### Complexity
| Operation | Priority Queue | Chronological Ordering | Bucket Sort |
|-----------|----------------|------------------------|-------------|
| Sorting | O(n log n) | O(n log n) | N/A |
| Processing | O(n log n) | O(n) | O(n + k) |
| **Overall** | **O(n log n)** | **O(n log n)** | **O(n + k)** |

**Note:** For bucket sort, k = 10^6 (maximum time value), so O(n + k) is effectively O(n) when n is large, but has constant factor overhead.

## Common Mistakes

1. **Empty intervals**: Return 0
2. **Single meeting**: Return 1
3. **No overlaps**: All meetings can use one room
4. **All overlap**: Need n rooms for n meetings
5. **Adjacent meetings**: `[0,5]` and `[5,10]` can share a room

1. **Not sorting**: Must sort by start time first
2. **Wrong comparison**: Using `>` instead of `>=` for end time check
3. **Heap management**: Forgetting to pop when room is freed
4. **Pointer logic**: Incorrect order of operations in two-pointer approach
5. **Edge case handling**: Not checking for empty input

## Optimization Notes

### Solution 1 Optimization:
- The heap size represents active meetings, which is exactly what we need
- No need to track maximum separately - final heap size is the answer

### Solution 2 Optimization:
- Can track maximum during traversal instead of storing all values
- Two separate arrays allow independent sorting

### Solution 3 Optimization:
- For sparse time ranges, use `map<int, int>` instead of array
- This reduces space from O(k) to O(n) but increases time to O(n log n)
- Best when time range is bounded and meetings are dense

## Key Takeaways

- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

## References

- [LC 253: Meeting Rooms II on LeetCode](https://www.leetcode.com/problems/meeting-rooms-ii/)
- [LeetCode Discuss — LC 253: Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/meeting-rooms-ii/editorial/) *(may require premium)*

## Related Problems

- [252. Meeting Rooms](https://www.leetcode.com/problems/meeting-rooms/) - Check if meetings can be scheduled (no overlap)
- [56. Merge Intervals](https://www.leetcode.com/problems/merge-intervals/) - Merge overlapping intervals
- [57. Insert Interval](https://www.leetcode.com/problems/insert-interval/) - Insert and merge intervals
- [435. Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/) - Remove minimum intervals to make non-overlapping
- [1094. Car Pooling](https://www.leetcode.com/problems/car-pooling/) - Similar interval scheduling problem

## Pattern Recognition

This problem demonstrates the **"Interval Scheduling"** pattern:

```
1. Sort intervals by start time
2. Track active/overlapping intervals
3. Use data structure (heap/pointers) to manage state
4. Count maximum concurrent intervals
```

Similar problems:
- Maximum overlapping intervals
- Resource allocation
- Event scheduling
- Timeline simulation

## Real-World Applications

1. **Conference Room Booking**: Determine minimum rooms needed
2. **Resource Allocation**: Allocate resources for overlapping tasks
3. **CPU Scheduling**: Schedule processes with time constraints
4. **Event Management**: Plan events with overlapping time slots
5. **Network Bandwidth**: Allocate bandwidth for overlapping requests
