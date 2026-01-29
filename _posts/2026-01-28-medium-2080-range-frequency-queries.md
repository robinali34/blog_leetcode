---
layout: post
title: "2080. Range Frequency Queries"
date: 2026-01-28 00:00:00 -0700
categories: [leetcode, medium, array, hash-map, binary-search, design]
permalink: /2026/01/28/medium-2080-range-frequency-queries/
tags: [leetcode, medium, array, hash-map, binary-search, design]
---

# 2080. Range Frequency Queries

## Problem Statement

Design a data structure that can query the frequency of a given value in a given subarray.

Implement the `RangeFreqQuery` class:

- `RangeFreqQuery(int[] arr)` Constructs an instance of the class with the given `0-indexed` integer array `arr`.
- `int query(int left, int right, int value)` Returns the frequency of `value` in the subarray `arr[left...right]` (inclusive).

A **subarray** is a contiguous sequence of elements within an array. `arr[left...right]` denotes the subarray that contains the elements of `nums` between indices `left` and `right` (inclusive).

## Examples

**Example 1:**

```
Input
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
Output
[null, 1, 2]

Explanation
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the entire array.
```

## Constraints

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^4`
- `0 <= left <= right < arr.length`
- At most `10^5` calls will be made to `query`.

## Solution Approach

This problem requires efficiently answering multiple range frequency queries. The key insight is to preprocess the array by grouping indices by value, then use binary search to quickly count occurrences in a range.

### Key Insights:

1. **Hash Map + Indices**: Store all indices where each value appears
2. **Binary Search**: Use `lower_bound` and `upper_bound` to find indices in range `[left, right]`
3. **Frequency = Count**: Number of indices in range equals frequency
4. **Preprocessing**: O(n) time to build the data structure
5. **Query**: O(log n) time per query using binary search

## Solution: Hash Map with Binary Search

```cpp
class RangeFreqQuery {
public:
    RangeFreqQuery(vector<int>& arr) {
        for(int i = 0; i < (int)arr.size(); i++) {
            freqArray[arr[i]].push_back(i);
        }
    }
    
    int query(int left, int right, int value) {
        if(!freqArray.contains(value)) return 0;
        vector<int>& v = freqArray[value];
        auto itLeft = lower_bound(v.begin(), v.end(), left);
        auto itRight = upper_bound(v.begin(), v.end(), right);
        return itRight - itLeft;
    }

private:
    unordered_map<int, vector<int>> freqArray;
};

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery* obj = new RangeFreqQuery(arr);
 * int param_1 = obj->query(left,right,value);
 */
```

### Algorithm Explanation:

#### **Step 1: Preprocessing - Build Index Map**

```cpp
RangeFreqQuery(vector<int>& arr) {
    for(int i = 0; i < (int)arr.size(); i++) {
        freqArray[arr[i]].push_back(i);
    }
}
```

- For each value, store all indices where it appears
- `freqArray[value]` = sorted list of indices containing `value`
- Since we iterate in order, indices are automatically sorted

**Example:** `arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]`

```
freqArray[12] = [0, 9]
freqArray[33] = [1, 7]
freqArray[4] = [2]
freqArray[56] = [3, 11]
freqArray[22] = [4, 8]
freqArray[2] = [5]
freqArray[34] = [6, 10]
```

#### **Step 2: Query - Binary Search for Range**

```cpp
int query(int left, int right, int value) {
    if(!freqArray.contains(value)) return 0;
    vector<int>& v = freqArray[value];
    auto itLeft = lower_bound(v.begin(), v.end(), left);
    auto itRight = upper_bound(v.begin(), v.end(), right);
    return itRight - itLeft;
}
```

**Key Operations:**

1. **Check if value exists**: If `value` not in map, return `0`

2. **Find first index >= left**: `lower_bound(v.begin(), v.end(), left)`
   - Returns iterator to first element `>= left`
   - Points to first occurrence of `value` in range `[left, right]` (or end if none)

3. **Find first index > right**: `upper_bound(v.begin(), v.end(), right)`
   - Returns iterator to first element `> right`
   - Points to first occurrence after range `[left, right]`

4. **Count occurrences**: `itRight - itLeft`
   - Number of elements between `itLeft` and `itRight`
   - Equals frequency of `value` in range `[left, right]`

### Example Walkthrough:

**Input:** `arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]`

**Query 1:** `query(1, 2, 4)`

```
Step 1: Check if value exists
  freqArray.contains(4) = true
  v = freqArray[4] = [2]

Step 2: Find indices in range [1, 2]
  lower_bound([2], 1) → points to index 0 (value 2 >= 1)
  upper_bound([2], 2) → points to index 1 (first value > 2)
  
Step 3: Count
  itRight - itLeft = 1 - 0 = 1
  
Result: return 1 ✓
```

**Query 2:** `query(0, 11, 33)`

```
Step 1: Check if value exists
  freqArray.contains(33) = true
  v = freqArray[33] = [1, 7]

Step 2: Find indices in range [0, 11]
  lower_bound([1, 7], 0) → points to index 0 (value 1 >= 0)
  upper_bound([1, 7], 11) → points to index 2 (first value > 11)
  
Step 3: Count
  itRight - itLeft = 2 - 0 = 2
  
Result: return 2 ✓
```

**Query 3:** `query(3, 5, 33)`

```
Step 1: Check if value exists
  freqArray.contains(33) = true
  v = freqArray[33] = [1, 7]

Step 2: Find indices in range [3, 5]
  lower_bound([1, 7], 3) → points to index 1 (value 7 >= 3)
  upper_bound([1, 7], 5) → points to index 1 (first value > 5)
  
Step 3: Count
  itRight - itLeft = 1 - 1 = 0
  
Result: return 0 ✓ (no occurrences in range [3, 5])
```

### Complexity Analysis:

- **Time Complexity:**
  - **Constructor:** O(n) where n is array length
  - **Query:** O(log m) where m is number of occurrences of `value`
    - Binary search on sorted indices: O(log m)
    - In worst case, m = n, so O(log n)
  - **Overall:** O(n) preprocessing + O(q log n) for q queries

- **Space Complexity:** O(n)
  - Hash map stores all indices: O(n) total space
  - Each index stored exactly once

## Key Insights

1. **Preprocessing is Key**: Building index map once allows fast queries
2. **Sorted Indices**: Since we iterate in order, indices are naturally sorted
3. **Binary Search**: Efficiently find indices in range `[left, right]`
4. **lower_bound vs upper_bound**:
   - `lower_bound`: First index `>= left` (inclusive start)
   - `upper_bound`: First index `> right` (exclusive end)
   - Difference gives count in range

5. **Hash Map Lookup**: O(1) average case to get indices for a value

## Edge Cases

1. **Value not in array**: `query(0, 5, 99)` → return `0`
2. **Value not in range**: `query(3, 5, 33)` when `33` only at indices `[1, 7]` → return `0`
3. **Single occurrence**: `query(0, 11, 4)` → return `1`
4. **All occurrences**: `query(0, 11, 33)` → return `2`
5. **Single element range**: `query(2, 2, 4)` → return `1` if `arr[2] == 4`

## Common Mistakes

1. **Wrong binary search bounds**: Using `upper_bound` for both ends
2. **Not checking existence**: Accessing `freqArray[value]` without checking
3. **Index confusion**: Mixing 0-indexed and 1-indexed arrays
4. **Not using sorted indices**: Assuming indices are sorted without verification
5. **Inefficient approach**: Linear scan for each query (O(n) per query)

## Alternative Approaches

### Approach 1: Naive Linear Scan (TLE)

```cpp
int query(int left, int right, int value) {
    int count = 0;
    for(int i = left; i <= right; i++) {
        if(arr[i] == value) count++;
    }
    return count;
}
```

**Time:** O(n) per query  
**Space:** O(1)  
**Problem:** Too slow for `10^5` queries

### Approach 2: Segment Tree (Overkill)

```cpp
// Build segment tree storing frequency map for each range
// Query: Merge frequency maps from segments
```

**Time:** O(n log n) build, O(log n) query  
**Space:** O(n log n)  
**Problem:** More complex, not necessary for this problem

## Comparison of Approaches

| Approach | Preprocessing | Query Time | Space | Best For |
|----------|--------------|------------|-------|----------|
| **Hash Map + Binary Search** | O(n) | O(log n) | O(n) | This problem ✓ |
| **Naive Linear Scan** | O(1) | O(n) | O(1) | Small arrays |
| **Segment Tree** | O(n log n) | O(log n) | O(n log n) | Range updates needed |

## Related Problems

- [LC 303: Range Sum Query - Immutable](https://robinali34.github.io/blog_leetcode/2026/01/01/easy-303-range-sum-query-immutable/) - Range sum queries
- [LC 307: Range Sum Query - Mutable](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-307-range-sum-query-mutable/) - Range sum with updates
- [LC 315: Count of Smaller Numbers After Self](https://robinali34.github.io/blog_leetcode/2026/01/17/hard-315-count-of-smaller-numbers-after-self/) - Counting in ranges
- [LC 327: Count of Range Sum](https://robinali34.github.io/blog_leetcode/2026/01/20/hard-327-count-of-range-sum/) - Range counting

---

*This problem demonstrates **hash map preprocessing with binary search** for efficient range frequency queries. The key insight is storing sorted indices for each value, then using binary search to quickly count occurrences in a range.*
