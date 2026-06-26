---
layout: post
title: "[Hard] 715. Range Module"
date: 2025-12-31 16:30:00 -0700
categories: [leetcode, hard, design, data-structures, interval, map, tree-map]
permalink: /2025/12/31/hard-715-range-module/
---
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

## Solution Structure Breakdown

### Evolution from Naive to Optimized

**Naive Approach** (List-based):
- **Structure**: Store intervals in unsorted list, linear scan
- **Complexity**: O(n) per operation, O(n^2) worst case
- **Limitation**: No efficient way to find/merge intervals

**Semi-Optimized Approach** (Sorted Vector):
- **Structure**: Maintain sorted vector, binary search for position
- **Complexity**: O(log n) search + O(n) insertion/deletion
- **Improvement**: Faster search, but still O(n) for modifications

**Optimized Approach** (Sorted Map):
- **Structure**: `std::map` for automatic sorting and O(log n) operations
- **Complexity**: O(k log n) where k = intervals affected
- **Enhancement**: Efficient merge/split operations

### Code Structure Comparison

| Approach | Data Structure | Search | Insert/Delete | Merge Logic |
|----------|---------------|--------|---------------|-------------|
| **Naive** | Unsorted list | O(n) | O(1) | O(n^2) |
| **Semi-Opt** | Sorted vector | O(log n) | O(n) | O(n) |
| **Optimized** | Sorted map | O(log n) | O(log n) | O(k log n) |

## Thinking Process

A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as **half-open intervals** `[left, right)`.

Implement the `RangeModule` class:

- Identify required operations and their frequency (get/put/insert).
- Combine data structures: hash map + list, heap + map, trie + DFS.
- Amortized $O(1)$ often needs lazy cleanup or doubly-linked lists.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Design pattern</text>

  <rect x="40" y="45" width="70" height="36" rx="4" fill="#D4D8E0" stroke="#8B8680"/><text x="75" y="67" text-anchor="middle" font-size="10">API</text>
  <rect x="150" y="45" width="90" height="36" rx="4" fill="#E0D8E4" stroke="#A098A8"/><text x="195" y="67" text-anchor="middle" font-size="10">hash + list</text>
  <path d="M110 63h36" stroke="#8B8680" stroke-width="2" marker-end="url(#arr2)"/>
  <defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>
  <text x="140" y="105" text-anchor="middle" font-size="11" fill="#6B6560">compose data structures for operations</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Hash map + list** *(this problem)* | $O(1)$ avg | $O(n)$ | LRU cache pattern |
| Heap + hash map | $O(\log n)$ | $O(n)$ | LFU, time-based store |
| Trie (prefix tree) | $O(m)$ | $O(nm)$ | Word search, autocomplete |
| Deque / circular buffer | $O(1)$ | $O(n)$ | Queue with fixed capacity |

## Solution

### **Solution 1: Brute-Force List-Based Approach**

**Time Complexity:** O(n) per operation, O(n^2) worst case for merging  
**Space Complexity:** O(n)

Store all intervals in an unsorted list and linearly scan for operations.

```cpp
class RangeModule {
private:
    vector<pair<int, int>> intervals;
    
    void mergeIntervals() {
        if (intervals.empty()) return;
        sort(intervals.begin(), intervals.end());
        vector<pair<int, int>> merged;
        merged.push_back(intervals[0]);
        
        for (int i = 1; i < intervals.size(); i++) {
            if (merged.back().second >= intervals[i].first) {
                merged.back().second = max(merged.back().second, intervals[i].second);
            } else {
                merged.push_back(intervals[i]);
            }
        }
        intervals = merged;
    }
    
public:
    RangeModule() {
        
    }
    
    void addRange(int left, int right) {
        intervals.push_back({left, right});
        mergeIntervals();  // O(n log n) + O(n)
    }
    
    bool queryRange(int left, int right) {
        for (auto& [l, r] : intervals) {
            if (l <= left && right <= r) return true;
        }
        return false;
    }
    
    void removeRange(int left, int right) {
        vector<pair<int, int>> newIntervals;
        for (auto& [l, r] : intervals) {
            if (r <= left || l >= right) {
                newIntervals.push_back({l, r});
            } else {
                if (l < left) newIntervals.push_back({l, left});
                if (r > right) newIntervals.push_back({right, r});
            }
        }
        intervals = newIntervals;
    }
};
```

**Note**: This approach is inefficient due to O(n) operations and O(n^2) worst case merging.

### **Solution 2: Sorted Vector with Binary Search**

**Time Complexity:** O(log n) search + O(n) insertion/deletion per operation  
**Space Complexity:** O(n)

Maintain sorted intervals using a vector with binary search for finding positions.

```cpp
class RangeModule {
private:
    vector<pair<int, int>> intervals;  // Kept sorted
    
    int findInsertPos(int left) {
        int low = 0, high = intervals.size();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (intervals[mid].first <= left) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
    
public:
    RangeModule() {
        
    }
    
    void addRange(int left, int right) {
        int pos = findInsertPos(left);  // O(log n)
        intervals.insert(intervals.begin() + pos, {left, right});  // O(n)
        // Merge overlapping intervals - O(n)
        mergeIntervals();
    }
    
    bool queryRange(int left, int right) {
        int pos = findInsertPos(left);  // O(log n)
        if (pos > 0) {
            auto& prev = intervals[pos - 1];
            if (prev.first <= left && right <= prev.second) return true;
        }
        return false;
    }
    
    void removeRange(int left, int right) {
        // Find and remove/split intervals - O(n)
        vector<pair<int, int>> newIntervals;
        for (auto& [l, r] : intervals) {
            if (r <= left || l >= right) {
                newIntervals.push_back({l, r});
            } else {
                if (l < left) newIntervals.push_back({l, left});
                if (r > right) newIntervals.push_back({right, r});
            }
        }
        intervals = newIntervals;
    }
    
private:
    void mergeIntervals() {
        if (intervals.empty()) return;
        vector<pair<int, int>> merged;
        merged.push_back(intervals[0]);
        
        for (int i = 1; i < intervals.size(); i++) {
            if (merged.back().second >= intervals[i].first) {
                merged.back().second = max(merged.back().second, intervals[i].second);
            } else {
                merged.push_back(intervals[i]);
            }
        }
        intervals = merged;
    }
};
```

**Note**: Better than brute-force with O(log n) search, but still O(n) for insertions/deletions.

### **Solution 3: Map-Based Interval Management (Recommended)**

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

### Complexity
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [715. Range Module](https://www.leetcode.com/problems/range-module/) - Current problem
- [56. Merge Intervals](https://www.leetcode.com/problems/merge-intervals/) - Merge overlapping intervals
- [57. Insert Interval](https://www.leetcode.com/problems/insert-interval/) - Insert and merge
- [352. Data Stream as Disjoint Intervals](https://www.leetcode.com/problems/data-stream-as-disjoint-intervals/) - Similar interval management

## Tags

`Design`, `Data Structures`, `Interval`, `Map`, `Tree Map`, `Hard`

## Key Takeaways

- Identify required operations and their frequency (get/put/insert).
- Combine data structures: hash map + list, heap + map, trie + DFS.
- Amortized $O(1)$ often needs lazy cleanup or doubly-linked lists.

## References

- [LC 715: Range Module on LeetCode](https://www.leetcode.com/problems/range-module/)
- [LeetCode Discuss — LC 715: Range Module](https://www.leetcode.com/problems/range-module/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/range-module/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
