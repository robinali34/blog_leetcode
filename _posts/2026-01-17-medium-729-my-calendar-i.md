---
layout: post
title: "[Medium] 729. My Calendar I"
date: 2026-01-17 00:00:00 -0700
categories: [leetcode, medium, array, binary-search, design, ordered-set]
permalink: /2026/01/17/medium-729-my-calendar-i/
tags: [leetcode, medium, array, binary-search, design, ordered-set, interval, overlap-detection]
---
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

## Thinking Process

1. **Ordered Set**: `std::set` maintains sorted order automatically

- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 130" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary search: shrink [lo … hi]</text>

  <rect x="40" y="40" width="48" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="64" y="58" text-anchor="middle" font-size="12" fill="#3A3530">lo</text>
  <rect x="108" y="40" width="48" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="132" y="58" text-anchor="middle" font-size="12" fill="#3A3530">mid</text>
  <rect x="196" y="40" width="48" height="32" rx="4" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="220" y="58" text-anchor="middle" font-size="12" fill="#3A3530">hi</text>
  <rect x="60" y="90" width="160" height="28" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="140" y="108" text-anchor="middle" font-size="11" fill="#6B6560">discard half each step → O(log n)</text>
  <path d="M132 72v12M220 72v12" stroke="#9A9792" stroke-width="1.5" marker-end="url(#a)"/>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Standard binary search** *(this problem)* | O(log n) | O(1) | Sorted array, `left <= right` |
| Lower / upper bound | O(log n) | O(1) | First/last position, insert index |
| Binary search on rotated array | O(log n) | O(1) | Identify sorted half, discard other |
| Binary search on answer | O(n log M) | O(1) | Monotonic predicate over search space |

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

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Ordered Set**: `std::set` maintains sorted order automatically

**How the code works:**
1. **Ordered Set**: `std::set` maintains sorted order automatically
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

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
## Common Mistakes

1. **Empty calendar**: First booking always succeeds
2. **Adjacent intervals**: `[10, 20)` and `[20, 30)` don't overlap (half-open)
3. **Exact overlap**: `[10, 20)` and `[10, 20)` overlap
4. **Contained interval**: `[10, 30)` contains `[15, 25)` → overlap
5. **Large ranges**: Handle up to 10^9 values

1. **Inclusive end**: Treating end as inclusive instead of exclusive
2. **Wrong overlap check**: Not checking both next and previous events
3. **Iterator errors**: Not checking `end()` before dereferencing
4. **Boundary conditions**: `prev(begin())` is undefined, always check `begin()` first
5. **Comparison logic**: Confusing `lower_bound` behavior with custom comparators

## Related Problems

- [LC 731: My Calendar II](https://www.leetcode.com/problems/my-calendar-ii/) - Allow double booking with triple booking prevention
- [LC 732: My Calendar III](https://www.leetcode.com/problems/my-calendar-iii/) - Count maximum overlapping events
- [LC 56: Merge Intervals](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-56-merge-intervals/) - Merge overlapping intervals
- [LC 57: Insert Interval](https://www.leetcode.com/problems/insert-interval/) - Insert and merge intervals
- [LC 252: Meeting Rooms](https://www.leetcode.com/problems/meeting-rooms/) - Check if intervals can be scheduled

## Key Takeaways

1. **Ordered Set**: `std::set` maintains sorted order automatically
2. **Binary Search**: `lower_bound` efficiently finds insertion point
3. **Half-Open Intervals**: End is exclusive, so `[10, 20)` and `[20, 30)` don't overlap
4. **Two Checks**: Only need to check next and previous events (at most 2)
5. **Overlap Condition**: `s1 < e2 && s2 < e1` for intervals `[s1, e1)` and `[s2, e2)`

## References

- [LC 729: My Calendar I on LeetCode](https://www.leetcode.com/problems/my-calendar-i/)
- [LeetCode Discuss — LC 729: My Calendar I](https://www.leetcode.com/problems/my-calendar-i/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/my-calendar-i/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
