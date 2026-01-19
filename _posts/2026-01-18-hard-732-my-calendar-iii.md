---
layout: post
title: "732. My Calendar III"
date: 2026-01-18 00:00:00 -0700
categories: [leetcode, hard, array, binary-search, design, segment-tree, ordered-set]
permalink: /2026/01/18/hard-732-my-calendar-iii/
tags: [leetcode, hard, array, binary-search, design, segment-tree, lazy-propagation, sweep-line, difference-array]
---

# 732. My Calendar III

## Problem Statement

A `k`-booking happens when `k` events have some non-empty intersection (i.e., there is some time that is common to all `k` events).

You are given some events `[startTime, endTime)`, after each given event, return an integer `k` representing the maximum `k`-booking from all the previous events.

Your event will be represented as a pair of integers `start` and `end` that represents a booking on the half-open interval `[start, end)`, the range of real numbers `x` such that `start <= x < end`.

Implement the `MyCalendarThree` class:

- `MyCalendarThree()` Initializes the object.
- `int book(int startTime, int endTime)` Returns an integer `k` representing the largest integer such that there exists a `k`-booking in the calendar.

## Examples

**Example 1:**
```
Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1
myCalendarThree.book(50, 60); // return 1
myCalendarThree.book(10, 40); // return 2
myCalendarThree.book(5, 15);  // return 3
myCalendarThree.book(5, 10);  // return 3
myCalendarThree.book(25, 55); // return 3
```

## Constraints

- `0 <= startTime < endTime <= 10^9`
- At most `400` calls will be made to `book`.

## Solution Approach

This problem requires finding the **maximum number of overlapping intervals** after each booking. Unlike [LC 729: My Calendar I](https://robinali34.github.io/blog_leetcode/2026/01/17/medium-729-my-calendar-i/) which only checks for any overlap, we need to count and track the maximum overlap.

### Key Insights:

1. **Sweep Line Algorithm**: Use difference array to track interval starts (+1) and ends (-1)
2. **Segment Tree**: For range updates and range maximum queries over large ranges
3. **Split Intervals**: Maintain active intervals and split at boundaries
4. **Maximum Overlap**: Track the maximum count at any point in time

### Algorithm:

1. **Sweep Line**: Mark start with +1, end with -1, then sweep to find maximum
2. **Segment Tree**: Update range [start, end-1] with +1, query maximum
3. **Split Intervals**: Split intervals at boundaries and track counts

## Solution

### **Solution 1: Sweep Line / Difference Array (Map)**

Use an ordered map to track interval boundaries and sweep to find maximum overlap.

```cpp
class MyCalendarThree {
public:
    MyCalendarThree() {
        
    }
    
    int book(int startTime, int endTime) {
        mp[startTime]++;
        mp[endTime]--;
        int maxBooking = 0;
        int active = 0;
        for(auto &[time, curr] : mp) {
            active += curr;
            maxBooking = max(maxBooking, active);
        }
        return maxBooking;
    }

private:
    map<int, int> mp;
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime, endTime);
 */
```

### **Algorithm Explanation:**

1. **Difference Array**: 
   - `mp[startTime]++`: Mark interval start (+1)
   - `mp[endTime]--`: Mark interval end (-1)

2. **Sweep Line**:
   - Iterate through sorted time points
   - Accumulate active bookings: `active += curr`
   - Track maximum: `maxBooking = max(maxBooking, active)`

3. **Why It Works**:
   - Each start adds 1 to active count
   - Each end subtracts 1 from active count
   - Maximum active count = maximum overlap

### **Example Walkthrough:**

**Input:** `book(10, 20)`, `book(50, 60)`, `book(10, 40)`

```
Step 1: book(10, 20)
  mp[10] = 1, mp[20] = -1
  Sweep: active = 0 → 1 (at 10) → 0 (at 20)
  maxBooking = 1 ✓

Step 2: book(50, 60)
  mp[50] = 1, mp[60] = -1
  Sweep: active = 0 → 1 (at 10) → 0 (at 20) → 1 (at 50) → 0 (at 60)
  maxBooking = 1 ✓

Step 3: book(10, 40)
  mp[10] = 2, mp[40] = -1
  Sweep: active = 0 → 2 (at 10) → 1 (at 20) → 0 (at 40) → 1 (at 50) → 0 (at 60)
  maxBooking = 2 ✓
```

### **Complexity Analysis:**

- **Time Complexity:** O(n log n) per `book()` call
  - Map insertion: O(log n)
  - Iteration over map: O(n) where n = number of unique time points
  - Overall: O(n log n)

- **Space Complexity:** O(n)
  - Store up to 2n time points (start and end for each booking)
  - Overall: O(n)

### **Solution 2: Segment Tree with Lazy Propagation**

Use segment tree for range updates and maximum queries over large ranges.

```cpp
class MyCalendarThree {
public:
    MyCalendarThree() {
        
    }
    
    int book(int startTime, int endTime) {
        update(startTime, endTime - 1, 1, 1e9, 1);
        return vals[1];
    }

private:
    unordered_map<int, int> vals;
    unordered_map<int, int> lazy;
    int max_len = 1e9;

    void update(int start, int end, int left, int right, int idx) {
        if(start > right || end < left) return;

        if (left >= start && right <= end) {
            lazy[idx]++;
            vals[idx]++;
        } else {
            int mid = (left + right) / 2;
            update(start, end, left, mid, idx * 2);
            update(start, end, mid + 1, right, idx * 2 + 1);
            vals[idx] = lazy[idx] + max(vals[idx * 2], vals[idx * 2 + 1]);
        }
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime, endTime);
 */
```

### **Algorithm Explanation:**

1. **Lazy Propagation**: Defer updates to children until needed
2. **Range Update**: Update range [start, end-1] with +1
3. **Maximum Query**: Root node stores maximum overlap
4. **Dynamic Nodes**: Use `unordered_map` for sparse segment tree

### **Complexity Analysis:**

- **Time Complexity:** O(log M) per `book()` call
  - M = range size (10^9)
  - Each update traverses tree height: O(log M)

- **Space Complexity:** O(n log M)
  - n = number of bookings
  - Each booking creates O(log M) nodes
  - Overall: O(n log M)

### **Solution 3: Split Intervals (Line Sweep)**

Split intervals at boundaries and maintain active counts.

```cpp
class MyCalendarThree {
public:
    MyCalendarThree() {
        starts[0] = 0;
        starts[(int)1e9 + 1] = 0;
        maxBooking = 0;
    }
    
    int book(int startTime, int endTime) {
        split(startTime);
        split(endTime);
        for(auto it = starts.find(startTime); it->first < endTime; it++) {
            maxBooking = max(maxBooking, ++(it->second));
        }
        return maxBooking;
    }

private:
    map<int, int> starts;
    int maxBooking;

    void split(int x) {
        starts[x] = (--starts.upper_bound(x))->second;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime, endTime);
 */
```

### **Algorithm Explanation:**

1. **Split Function**: 
   - `split(x)` ensures interval starting at `x` exists
   - Copies count from previous interval

2. **Book Function**:
   - Split at start and end boundaries
   - Increment count for all intervals in [start, end)
   - Track maximum booking

3. **Why It Works**:
   - Maintains intervals between boundaries
   - Each interval has a count
   - Maximum count = maximum overlap

### **Example Walkthrough:**

**Input:** `book(10, 20)`, `book(10, 40)`

```
Step 1: book(10, 20)
  split(10): starts[10] = starts[0] = 0
  split(20): starts[20] = starts[10] = 0
  Increment [10, 20): starts[10] = 1
  maxBooking = 1 ✓

Step 2: book(10, 40)
  split(10): already exists
  split(40): starts[40] = starts[20] = 0
  Increment [10, 40): 
    starts[10] = 2
    starts[20] = 1 (new interval)
  maxBooking = 2 ✓
```

### **Complexity Analysis:**

- **Time Complexity:** O(n) per `book()` call
  - Split: O(log n) for map operations
  - Iteration: O(n) for intervals in range
  - Overall: O(n)

- **Space Complexity:** O(n)
  - Store up to 2n boundaries
  - Overall: O(n)

## Key Insights

1. **Sweep Line**: Most intuitive, tracks active bookings at each time point
2. **Segment Tree**: Efficient for large ranges, supports range updates
3. **Split Intervals**: Maintains explicit intervals with counts
4. **Half-Open Intervals**: End is exclusive, so `[10, 20)` and `[20, 30)` don't overlap
5. **Maximum Tracking**: Need to track maximum across all time points

## Edge Cases

1. **Single booking**: `book(10, 20)` → return `1`
2. **No overlap**: `book(10, 20)`, `book(30, 40)` → return `1`
3. **Complete overlap**: `book(10, 20)`, `book(10, 20)` → return `2`
4. **Partial overlap**: `book(10, 30)`, `book(20, 40)` → return `2`
5. **Multiple overlaps**: `book(10, 20)`, `book(15, 25)`, `book(18, 22)` → return `3`

## Common Mistakes

1. **Inclusive end**: Treating end as inclusive instead of exclusive
2. **Not tracking maximum**: Forgetting to update maximum after each booking
3. **Segment tree range**: Using [start, end] instead of [start, end-1]
4. **Split logic**: Not properly splitting intervals at boundaries
5. **Iterator errors**: Invalidating iterators during iteration

## Comparison of Approaches

| Approach | Time per book() | Space | Code Complexity | Best For |
|----------|----------------|-------|-----------------|----------|
| **Sweep Line (Map)** | O(n log n) | O(n) | Simple | General purpose, easy to understand |
| **Segment Tree** | O(log M) | O(n log M) | Complex | Large ranges, many bookings |
| **Split Intervals** | O(n) | O(n) | Moderate | When explicit intervals needed |

## Related Problems

- [LC 729: My Calendar I](https://robinali34.github.io/blog_leetcode/2026/01/17/medium-729-my-calendar-i/) - Check for any overlap
- [LC 731: My Calendar II](https://leetcode.com/problems/my-calendar-ii/) - Allow double booking, prevent triple
- [LC 56: Merge Intervals](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-56-merge-intervals/) - Merge overlapping intervals
- [LC 218: The Skyline Problem](https://robinali34.github.io/blog_leetcode/2025/10/05/hard-218-skyline-problem/) - Similar sweep line approach

---

*This problem demonstrates multiple approaches for **maximum overlap counting**: Sweep Line (difference array), Segment Tree with lazy propagation, and Split Intervals. The key insight is tracking active bookings at each time point and finding the maximum.*

