---
layout: post
title: "729. My Calendar I"
date: 2026-01-17 00:00:00 -0700
categories: [leetcode, medium, array, binary-search, design, ordered-set]
permalink: /2026/01/17/medium-729-my-calendar-i/
tags: [leetcode, medium, array, binary-search, design, ordered-set, interval, overlap-detection]
---

# 729. My Calendar I

## Problem Statement

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a **double booking**.

A **double booking** happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

Your event will be represented as a pair of integers `start` and `end` that represents a booking on the half-open interval `[start, end)`, the range of real numbers `x` such that `start <= x < end`.

Implement the `MyCalendar` class:

- `MyCalendar()` Initializes the calendar object.
- `bool book(int start, int end)` Returns `true` if the event can be added to the calendar successfully without causing a double booking. Otherwise, return `false` and do not add the event to the calendar.

## Examples

**Example 1:**
```
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 25); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
```

## Constraints

- `0 <= start < end <= 10^9`
- At most `1000` calls will be made to `book`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Interval format**: Are intervals inclusive or exclusive? (Assumption: Half-open interval [start, end) - start is inclusive, end is exclusive)

2. **Overlap definition**: What constitutes an overlap? (Assumption: Two intervals overlap if they share any common time point - [a, b) overlaps [c, d) if max(a, c) < min(b, d))

3. **Adjacent intervals**: Can two intervals be adjacent (end of one equals start of another)? (Assumption: Yes - [10, 20) and [20, 30) don't overlap, can both be booked)

4. **Return value**: What should book() return? (Assumption: Return true if booking succeeds (no overlap), false if it conflicts with existing booking)

5. **Time range**: What's the valid range for start and end times? (Assumption: 0 <= start < end <= 10^9 per constraints)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Store all booked intervals in a list. For each `book(start, end)` call, check if the new interval overlaps with any existing interval. If no overlap, add it to the list and return true. Otherwise, return false. This approach has O(n) time per booking where n is the number of existing bookings, which is acceptable for small n but slow for many bookings.

**Step 2: Semi-Optimized Approach (7 minutes)**

Maintain intervals in a sorted list or set. When booking, use binary search to find the insertion position. Check overlap with the previous and next intervals only. This reduces overlap checking to O(1) after O(log n) binary search, giving O(log n) time per booking. However, insertion into a sorted list is O(n) in worst case.

**Step 3: Optimized Solution (8 minutes)**

Use a sorted data structure like `std::map` or `std::set`: store intervals as pairs `(start, end)` in sorted order. For each booking, use `lower_bound` to find the first interval with start >= new_start. Check overlap with this interval and the previous interval. If no overlap, insert and return true. This achieves O(log n) time per booking using balanced BST, which is optimal. The key insight is that we only need to check overlap with at most two intervals (the one that starts after our interval and the one that starts before), making binary search efficient.

## Solution Approach

This is an **interval overlap detection** problem. We need to efficiently check if a new interval overlaps with any existing intervals and insert it if no overlap exists.

### Key Insights:

1. **Half-Open Intervals**: `[start, end)` means start is inclusive, end is exclusive
2. **Overlap Condition**: Two intervals `[s1, e1)` and `[s2, e2)` overlap if `s1 < e2 && s2 < e1`
3. **Ordered Data Structure**: Use sorted structure to efficiently find potential overlaps
4. **Binary Search**: Find the next event and check previous event for overlaps

### Algorithm:

1. **Maintain Sorted Intervals**: Store intervals sorted by start time
2. **Find Next Event**: Use `lower_bound` to find first event with start >= new start
3. **Check Overlaps**: 
   - Check if next event overlaps (next.start < new.end)
   - Check if previous event overlaps (prev.end > new.start)
4. **Insert if Valid**: If no overlaps, insert the new interval

## Solution

### **Solution: Ordered Set (std::set) with Binary Search**

```cpp
class MyCalendar {
public:
    MyCalendar() {
        
    }
    
    bool book(int startTime, int endTime) {
        const pair<int, int> event{startTime, endTime};
        const auto nextEvent = calendar.lower_bound(event);
        if(nextEvent != calendar.end() && nextEvent->first < endTime) {
            return false;
        }
        if(nextEvent != calendar.begin()) {
            const auto preEvent = prev(nextEvent);
            if(preEvent->second > startTime) {
                return false;
            }
        }
        calendar.insert(event);
        return true;
    }

private:
    set<pair<int, int>> calendar;
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */
```

### **Algorithm Explanation:**

1. **Data Structure**: `set<pair<int, int>>` maintains intervals sorted by start time
   - Automatically sorted by first element (start time)
   - O(log n) insertion and search

2. **book() Method**:
   - **Find Next Event (Line 8)**: `lower_bound({start, end})` finds first interval with start >= new start
   - **Check Next Overlap (Lines 9-11)**: If next event exists and its start < new end, they overlap
   - **Check Previous Overlap (Lines 12-16)**: If previous event exists and its end > new start, they overlap
   - **Insert (Line 17)**: If no overlaps, insert and return true

### **Overlap Detection Logic:**

For intervals `[s1, e1)` and `[s2, e2)` to overlap:
- Condition: `s1 < e2 && s2 < e1`

In our code:
- **Next event check**: `nextEvent->first < endTime` means `s2 < e1` ✓
- **Previous event check**: `preEvent->second > startTime` means `e2 > s1` ✓

### **Example Walkthrough:**

**Input:** `book(10, 20)`, `book(15, 25)`, `book(20, 30)`

```
Step 1: book(10, 20)
  calendar = {}
  nextEvent = calendar.end() (no next event)
  preEvent check: nextEvent == begin() (no previous)
  Insert: calendar = {(10, 20)}
  Return: true ✓

Step 2: book(15, 25)
  calendar = {(10, 20)}
  nextEvent = lower_bound({15, 25}) = {(10, 20)} (start=10 < 15, but it's the closest)
  Actually, lower_bound finds first with start >= 15, so:
    nextEvent = calendar.end() (no event with start >= 15)
  Wait, let me reconsider...
  
  Actually: lower_bound({15, 25}) in set {(10, 20)}:
    - Compares (15, 25) with (10, 20)
    - Since 15 > 10, it continues
    - Reaches end, so nextEvent = end()
  
  Check next: nextEvent == end() → skip
  Check previous: prev(end()) = {(10, 20)}
    preEvent->second = 20 > 15 = startTime → OVERLAP!
  Return: false ✓

Step 3: book(20, 30)
  calendar = {(10, 20)}
  nextEvent = lower_bound({20, 30}) = end() (no event with start >= 20)
  Check next: skip
  Check previous: prev(end()) = {(10, 20)}
    preEvent->second = 20 > 20 = startTime? No, 20 is not > 20
    So no overlap (half-open: [10, 20) doesn't include 20)
  Insert: calendar = {(10, 20), (20, 30)}
  Return: true ✓
```

### **Complexity Analysis:**

- **Time Complexity:** O(log n) per `book()` call
  - `lower_bound`: O(log n)
  - `prev()`: O(1) for bidirectional iterators
  - `insert()`: O(log n)
  - Overall: O(log n) per operation

- **Space Complexity:** O(n)
  - Store up to n intervals
  - Each interval: O(1) space
  - Overall: O(n)

## Key Insights

1. **Ordered Set**: `std::set` maintains sorted order automatically
2. **Binary Search**: `lower_bound` efficiently finds insertion point
3. **Half-Open Intervals**: End is exclusive, so `[10, 20)` and `[20, 30)` don't overlap
4. **Two Checks**: Only need to check next and previous events (at most 2)
5. **Overlap Condition**: `s1 < e2 && s2 < e1` for intervals `[s1, e1)` and `[s2, e2)`

## Edge Cases

1. **Empty calendar**: First booking always succeeds
2. **Adjacent intervals**: `[10, 20)` and `[20, 30)` don't overlap (half-open)
3. **Exact overlap**: `[10, 20)` and `[10, 20)` overlap
4. **Contained interval**: `[10, 30)` contains `[15, 25)` → overlap
5. **Large ranges**: Handle up to 10^9 values

## Common Mistakes

1. **Inclusive end**: Treating end as inclusive instead of exclusive
2. **Wrong overlap check**: Not checking both next and previous events
3. **Iterator errors**: Not checking `end()` before dereferencing
4. **Boundary conditions**: `prev(begin())` is undefined, always check `begin()` first
5. **Comparison logic**: Confusing `lower_bound` behavior with custom comparators

## Alternative Approaches

### **Approach 2: Brute Force (Linear Scan)**

Simple approach for small number of bookings:

```cpp
class MyCalendar {
private:
    vector<pair<int, int>> events;
    
public:
    MyCalendar() {}
    
    bool book(int start, int end) {
        for (const auto& [s, e] : events) {
            // Check overlap: [s, e) and [start, end)
            if (start < e && s < end) {
                return false;
            }
        }
        events.push_back({start, end});
        return true;
    }
};
```

**Time Complexity:** O(n) per `book()` call  
**Space Complexity:** O(n)

**When to Use:** Small number of bookings (n ≤ 1000), simplicity preferred

### **Approach 3: Segment Tree / Interval Tree**

For more complex queries (range queries, multiple calendars):

```cpp
// More complex but supports advanced queries
// Typically overkill for this problem
```

**Time Complexity:** O(log n) per operation  
**Space Complexity:** O(n)

**When to Use:** Need range queries or more complex operations

### **Comparison:**

| Approach | Time per book() | Space | Code Complexity | Best For |
|----------|----------------|-------|-----------------|----------|
| **Ordered Set** | O(log n) | O(n) | Simple | General purpose |
| **Brute Force** | O(n) | O(n) | Very simple | Small inputs |
| **Segment Tree** | O(log n) | O(n) | Complex | Advanced queries |

## Related Problems

- [LC 731: My Calendar II](https://leetcode.com/problems/my-calendar-ii/) - Allow double booking with triple booking prevention
- [LC 732: My Calendar III](https://leetcode.com/problems/my-calendar-iii/) - Count maximum overlapping events
- [LC 56: Merge Intervals](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-56-merge-intervals/) - Merge overlapping intervals
- [LC 57: Insert Interval](https://leetcode.com/problems/insert-interval/) - Insert and merge intervals
- [LC 252: Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) - Check if intervals can be scheduled

---

*This problem demonstrates the **Ordered Set (std::set)** pattern for interval overlap detection. The key insight is using binary search to efficiently find potential overlapping intervals and checking at most two candidates (next and previous events).*

