---
layout: post
title: "715. Range Module"
date: 2025-12-31 16:30:00 -0700
categories: [leetcode, hard, design, data-structures, interval, map, tree-map]
permalink: /2025/12/31/hard-715-range-module/
---

# 715. Range Module

## Problem Statement

A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as **half-open intervals** `[left, right)`.

Implement the `RangeModule` class:

- `RangeModule()` Initializes the object of the data structure.
- `void addRange(int left, int right)` Adds the **half-open interval** `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.
- `bool queryRange(int left, int right)` Returns `true` if every real number in the interval `[left, right)` is currently being tracked, and `false` otherwise.
- `void removeRange(int left, int right)` Stops tracking every real number currently being tracked in the **half-open interval** `[left, right)`.

## Examples

**Example 1:**
```
Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);  // Track [10, 20)
rangeModule.removeRange(14, 16); // Stop tracking [14, 16)
rangeModule.queryRange(10, 14); // Returns true (every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // Returns false (numbers like 13.5, 14, 14.5, 15 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // Returns true (the number 16 in [16, 17) is still being tracked, despite the removeRange operation)
```

## Constraints

- `1 <= left < right <= 10^9`
- At most `10^4` calls will be made to `addRange`, `queryRange`, and `removeRange`.

## Solution Approach

This problem requires efficiently managing intervals (ranges) with support for adding, querying, and removing. We can use a **sorted map** (like `std::map` in C++) to store non-overlapping intervals, where keys are start points and values are end points.

### Key Insights:

1. **Sorted Map**: Use `map<int, int>` to store intervals in sorted order by start point
2. **Merge Intervals**: When adding, merge overlapping or adjacent intervals
3. **Split Intervals**: When removing, split intervals that partially overlap
4. **Query Check**: Check if query range is completely contained in an existing interval

### Algorithm:

1. **addRange**: Find overlapping intervals, merge them, remove subsumed intervals
2. **queryRange**: Check if query range is completely within a single interval
3. **removeRange**: Split intervals that overlap with removal range

## Solution

### **Solution: Map-Based Interval Management**

```cpp
class RangeModule {
private:
    map<int, int> intervals;

public:
    RangeModule() {
        
    }
    
    void addRange(int left, int right) {
        auto it = intervals.upper_bound(left);
        if(it != intervals.begin()) {
            auto start = prev(it);
            if(start->second >= right) return;
            if(start->second >= left) {
                left = start->first;
                intervals.erase(start);
            }
        }
        while(it != intervals.end() && it->first <= right) {
            right = max(right, it->second);
            it = intervals.erase(it);
        }
        intervals[left] = right;
    }
    
    bool queryRange(int left, int right) {
        auto it = intervals.upper_bound(left);
        if(it == intervals.begin()) return false;
        it = prev(it);
        return right <= it->second;
    }
    
    void removeRange(int left, int right) {
        auto it = intervals.upper_bound(left);
        if(it != intervals.begin()) {
            auto start = prev(it);
            if(start->second >= right) {
                int ri = start->second;
                if(start->first == left) {
                    intervals.erase(start);
                } else {
                    start->second = left;
                }
                if(right != ri) {
                    intervals[right] = ri;
                }
                return;
            } else if(start->second > left) {
                if(start->first == left) {
                    intervals.erase(start);
                } else {
                    start->second = left;
                }
            }
        }
        while(it != intervals.end() && it->first < right) {
            if(it->second <= right) {
                it = intervals.erase(it);
            } else {
                intervals[right] = it->second;
                intervals.erase(it);
                break;
            }
        }
    }
};
```

### **Algorithm Explanation:**

#### **1. addRange (Lines 10-24)**

**Purpose**: Add interval `[left, right)`, merging with overlapping intervals.

**Steps**:
1. **Find insertion point** (Line 11): `upper_bound(left)` finds first interval starting after `left`
2. **Check previous interval** (Lines 12-19):
   - If previous interval ends at or after `right`: already covered, return
   - If previous interval ends at or after `left`: merge by extending `left` to previous start
3. **Merge overlapping intervals** (Lines 20-23):
   - While current interval starts before or at `right`: merge by extending `right`
   - Remove merged intervals
4. **Insert merged interval** (Line 24): Add final merged interval

**Example**:
```
Initial: intervals = {[10, 20]}
addRange(15, 25):
  it = upper_bound(15) → points to [10, 20]
  prev(it) = [10, 20]
  start->second (20) >= left (15) → merge
  left = 10
  it->first (10) <= right (25) → merge
  right = max(25, 20) = 25
  Result: {[10, 25]}
```

#### **2. queryRange (Lines 26-31)**

**Purpose**: Check if entire range `[left, right)` is tracked.

**Steps**:
1. **Find candidate interval** (Line 27): `upper_bound(left)` finds first interval after `left`
2. **Check previous interval** (Line 28): Move to previous interval (might contain `left`)
3. **Verify coverage** (Line 30): Check if previous interval completely covers `[left, right)`

**Example**:
```
intervals = {[10, 20]}
queryRange(12, 18):
  it = upper_bound(12) → points to [10, 20]
  prev(it) = [10, 20]
  Check: right (18) <= it->second (20) → true
```

#### **3. removeRange (Lines 33-56)**

**Purpose**: Remove interval `[left, right)` from tracked ranges.

**Steps**:
1. **Find starting point** (Line 34): `upper_bound(left)` finds first interval after `left`
2. **Handle previous interval** (Lines 35-50):
   - If previous interval completely contains `[left, right)`:
     - Split into `[start, left)` and `[right, end)` if needed
   - If previous interval partially overlaps:
     - Truncate to `[start, left)`
3. **Remove/truncate following intervals** (Lines 51-56):
   - Remove intervals completely within `[left, right)`
   - Truncate interval that extends beyond `right`

**Example**:
```
intervals = {[10, 20]}
removeRange(14, 16):
  it = upper_bound(14) → points to [10, 20]
  prev(it) = [10, 20]
  start->second (20) >= right (16) → split needed
  start->first (10) != left (14) → truncate to [10, 14)
  right (16) != ri (20) → add [16, 20)
  Result: {[10, 14), [16, 20)}
```

### **Detailed Example Walkthrough:**

**Operations:**
```
1. addRange(10, 20)
   intervals = {[10, 20)}

2. addRange(15, 25)
   - Check [10, 20): overlaps, merge
   intervals = {[10, 25)}

3. removeRange(14, 16)
   - [10, 25) overlaps with [14, 16)
   - Split: [10, 14) and [16, 25)
   intervals = {[10, 14), [16, 25)}

4. queryRange(10, 14)
   - Find interval containing 10: [10, 14)
   - Check: 14 <= 14? Yes → true

5. queryRange(13, 15)
   - Find interval containing 13: [10, 14)
   - Check: 15 <= 14? No → false

6. queryRange(16, 17)
   - Find interval containing 16: [16, 25)
   - Check: 17 <= 25? Yes → true
```

## Algorithm Breakdown

### **Key Insight: Sorted Map for Intervals**

Using `map<int, int>` provides:
- **Sorted keys**: Intervals stored by start point
- **O(log n) operations**: Insert, delete, search
- **Efficient merging**: Easy to find overlapping intervals

### **Interval Merging Logic**

**addRange** merges intervals by:
1. Finding intervals that overlap or are adjacent
2. Extending `left` to earliest start
3. Extending `right` to latest end
4. Removing all subsumed intervals

### **Interval Splitting Logic**

**removeRange** splits intervals by:
1. Truncating intervals that start before `left`
2. Removing intervals completely within `[left, right)`
3. Creating new interval for part extending beyond `right`

## Complexity Analysis

### **Time Complexity:**
- **addRange**: O(k log n) where k = number of intervals to merge
- **queryRange**: O(log n) - binary search in map
- **removeRange**: O(k log n) where k = number of intervals to remove/split
- **n** = number of intervals stored

### **Space Complexity:** O(n)
- **Map storage**: O(n) intervals stored
- **Each operation**: O(1) extra space

## Key Points

1. **Half-Open Intervals**: `[left, right)` means left included, right excluded
2. **Sorted Map**: Maintains intervals in sorted order for efficient operations
3. **Merging**: Automatically merges overlapping/adjacent intervals
4. **Splitting**: Handles partial overlaps by splitting intervals
5. **Efficient Queries**: O(log n) lookup using binary search

## Edge Cases

1. **Empty intervals**: `left >= right` should be handled (though constraints say `left < right`)
2. **No overlapping**: Adding non-overlapping interval creates new entry
3. **Complete overlap**: Adding interval already covered does nothing
4. **Remove entire interval**: Removing completely removes interval
5. **Query outside range**: Returns false if no interval covers query

## Alternative Approaches

### **Approach 1: Map-Based (Current Solution)**
- **Time**: O(k log n) per operation
- **Space**: O(n)
- **Best for**: Efficient interval management

### **Approach 2: Segment Tree**
- **Time**: O(log max_value) per operation
- **Space**: O(max_value)
- **Use case**: When range of values is limited

### **Approach 3: Balanced BST of Intervals**
- **Time**: O(k log n) per operation
- **Space**: O(n)
- **Similar**: Custom interval tree structure

## Related Problems

- [715. Range Module](https://leetcode.com/problems/range-module/) - Current problem
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) - Merge overlapping intervals
- [57. Insert Interval](https://leetcode.com/problems/insert-interval/) - Insert and merge
- [352. Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) - Similar interval management

## Tags

`Design`, `Data Structures`, `Interval`, `Map`, `Tree Map`, `Hard`

