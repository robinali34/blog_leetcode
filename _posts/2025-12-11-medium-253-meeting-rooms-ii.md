---
layout: post
title: "[Medium] 253. Meeting Rooms II"
date: 2025-12-11 00:00:00 -0800
categories: leetcode algorithm medium cpp array sorting priority-queue two-pointers problem-solving
---

# [Medium] 253. Meeting Rooms II

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

## Solution 1: Priority Queue (Min Heap)

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

## Solution 2: Chronological Ordering (Two Pointers)

**Time Complexity:** O(n log n) - Sorting  
**Space Complexity:** O(n) - For separate start and end arrays

This approach separates start and end times, then uses two pointers to simulate the timeline and count concurrent meetings.

```cpp
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) return 0;

        vector<int> start(intervals.size());
        vector<int> end(intervals.size());
        
        for(int i = 0; i < intervals.size(); i++) {
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }

        sort(start.begin(), start.end());
        sort(end.begin(), end.end());

        int startPointer = 0, endPointer = 0;
        int usedRooms = 0;
        while(startPointer < intervals.size()) {
            if(start[startPointer] >= end[endPointer]) {
                usedRooms -= 1;
                endPointer += 1;
            }
            usedRooms += 1;
            startPointer += 1;
        }

        return usedRooms;
    }
};
```

### How Solution 2 Works

1. **Separate start and end times** into two arrays
2. **Sort both arrays** independently
3. **Use two pointers** to traverse both arrays:
   - `startPointer`: Points to next meeting starting
   - `endPointer`: Points to next meeting ending
4. **Simulate timeline**:
   - When a meeting starts (`startPointer`), increment `usedRooms`
   - If a meeting ends before the new one starts (`start[startPointer] >= end[endPointer]`), decrement `usedRooms` and move `endPointer`
5. **Track maximum**: The maximum value of `usedRooms` during traversal is the answer

### Key Insight

By processing events in chronological order, we can track how many meetings are active at any moment. When a meeting starts, we need a room. When a meeting ends, we free a room.

## Comparison of Approaches

| Aspect | Priority Queue | Chronological Ordering |
|--------|----------------|------------------------|
| **Time Complexity** | O(n log n) | O(n log n) |
| **Space Complexity** | O(n) | O(n) |
| **Intuition** | Track active meetings | Simulate timeline |
| **Code Complexity** | Moderate | Simpler |
| **Extensibility** | Easy to extend | Straightforward |

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

## Complexity Analysis

| Operation | Priority Queue | Chronological Ordering |
|-----------|----------------|------------------------|
| Sorting | O(n log n) | O(n log n) |
| Processing | O(n log n) | O(n) |
| **Overall** | **O(n log n)** | **O(n log n)** |

## Edge Cases

1. **Empty intervals**: Return 0
2. **Single meeting**: Return 1
3. **No overlaps**: All meetings can use one room
4. **All overlap**: Need n rooms for n meetings
5. **Adjacent meetings**: `[0,5]` and `[5,10]` can share a room

## Common Mistakes

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

## Related Problems

- [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) - Check if meetings can be scheduled (no overlap)
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) - Merge overlapping intervals
- [57. Insert Interval](https://leetcode.com/problems/insert-interval/) - Insert and merge intervals
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) - Remove minimum intervals to make non-overlapping
- [1094. Car Pooling](https://leetcode.com/problems/car-pooling/) - Similar interval scheduling problem

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

