---
layout: post
title: "981. Time Based Key-Value Store"
date: 2026-01-30 00:00:00 -0700
categories: [leetcode, medium, hash-table, binary-search, design]
permalink: /2026/01/30/medium-981-time-based-key-value-store/
tags: [leetcode, medium, hash-table, binary-search, design]
---

# 981. Time Based Key-Value Store

## Problem Statement

Design a time-based key-value data structure that can store multiple values for the same key at different timestamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the key `key` with the `value` at the given time `timestamp`.
- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

## Examples

**Example 1:**

```
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
```

**Example 2:**

```
Input
["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
[[], ["love", "high", 10], ["love", "low", 20], ["love", 5], ["love", 10], ["love", 10], ["love", 15], ["love", 20], ["love", 25]]
Output
[null, null, null, "", "high", "high", "low", "low", "low"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("love", "high", 10);
timeMap.set("love", "low", 20);
timeMap.get("love", 5);  // return "" (no value at timestamp <= 5)
timeMap.get("love", 10); // return "high"
timeMap.get("love", 10); // return "high"
timeMap.get("love", 15); // return "high" (closest timestamp <= 15 is 10)
timeMap.get("love", 20); // return "low"
timeMap.get("love", 25); // return "low"
```

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits.
- `1 <= timestamp <= 10^7`
- All the timestamps `timestamp` of `set` are strictly increasing.
- At most `2 * 10^5` calls will be made to `set` and `get`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Timestamp ordering**: Are timestamps strictly increasing? (Assumption: Yes - all timestamps in `set` are strictly increasing, which means we can use binary search)

2. **Get behavior**: What should `get` return if no value exists at or before the timestamp? (Assumption: Return empty string `""` - no value found)

3. **Multiple values**: Can the same key have multiple values at different timestamps? (Assumption: Yes - each `set` call adds a new timestamp-value pair for the key)

4. **Get requirement**: What value should `get` return if multiple values exist? (Assumption: Return value associated with the largest `timestamp_prev <= timestamp` - closest valid timestamp)

5. **Data structure**: What data structure should we use? (Assumption: Hash map to store key -> list of (timestamp, value) pairs, sorted by timestamp)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For `set`, simply append the (timestamp, value) pair to a list for that key. For `get`, scan through all values for the key from the end (since timestamps are increasing), find the first value with `timestamp <= target_timestamp`, and return it. This approach has O(1) time for `set` but O(n) time for `get`, where n is the number of values for that key.

**Step 2: Semi-Optimized Approach (7 minutes)**

Since timestamps are strictly increasing, the values for each key are stored in sorted order by timestamp. We can use binary search to find the largest timestamp that is <= target timestamp. This reduces `get` time complexity to O(log n) while keeping `set` at O(1).

**Step 3: Optimized Solution (8 minutes)**

Use a hash map to store key -> vector of (timestamp, value) pairs. Since timestamps are strictly increasing, the vector is automatically sorted. For `get`, use binary search to find the largest timestamp <= target timestamp. We can implement binary search manually or use STL's `lower_bound` with a custom comparator. This achieves O(1) time for `set` and O(log n) time for `get`.

## Solution Approach

This problem requires designing a data structure that supports efficient insertion and retrieval based on timestamps. The key insight is that timestamps are strictly increasing, which means we can maintain sorted order and use binary search.

### Key Insights:

1. **Strictly Increasing Timestamps**: Since timestamps are strictly increasing, values are automatically sorted
2. **Binary Search**: Use binary search to find the largest timestamp <= target timestamp
3. **Hash Map Storage**: Use hash map to map keys to their timestamp-value pairs
4. **Lower Bound Pattern**: Finding the largest timestamp <= target is similar to finding the upper bound minus 1

## Solution 1: Binary Search with Custom Implementation

```cpp
class TimeMap {
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        cache[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        if(!cache.contains(key)) return "";

        string rtn = "";
        const auto& values = cache[key];
        int left = 0, right = values.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(values[mid].first <= timestamp) {
                rtn = values[mid].second;
                left = mid + 1; //search right for newer valid timestamp
            } else {
                right = mid;
            }
        }
        return rtn;
    }

private:
    unordered_map<string, vector<pair<int, string>>> cache;
};
```

### Algorithm Breakdown:

1. **Data Structure**: `unordered_map<string, vector<pair<int, string>>>` - maps key to sorted list of (timestamp, value) pairs
2. **Set Operation**: Append (timestamp, value) to the vector for that key - O(1) amortized
3. **Get Operation**: 
   - Check if key exists, return `""` if not
   - Binary search to find the largest timestamp <= target timestamp
   - If `values[mid].first <= timestamp`, update result and search right for a newer valid timestamp
   - Otherwise, search left
   - Return the last valid value found

### Why This Works:

- **Binary Search Pattern**: We're finding the rightmost position where `timestamp <= target_timestamp`
- **Update on Valid**: When we find a valid timestamp (`<= target`), we update the result and continue searching right
- **Convergence**: The loop ensures we find the largest valid timestamp

## Solution 2: Using STL lower_bound

```cpp
class TimeMap {
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        cache[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        if(!cache.contains(key)) return "";

        const auto& values = cache[key];
        auto it = lower_bound(values.begin(), values.end(), timestamp,
                            [](const pair<int, string>& p, int ts) {
            return p.first < ts;
        });

        if(it != values.end() && it->first == timestamp) {
            return it->second;
        }
        if(it == values.begin()) return "";
        return prev(it)->second;
    }

private:
    unordered_map<string, vector<pair<int, string>>> cache;
};
```

### Algorithm Breakdown:

1. **Set Operation**: Same as Solution 1 - append to vector
2. **Get Operation**:
   - Use `lower_bound` with custom comparator to find first position where `timestamp >= target_timestamp`
   - If exact match found, return that value
   - If `lower_bound` returns `begin()`, no valid timestamp exists, return `""`
   - Otherwise, return the value at `prev(it)` (the largest timestamp < target_timestamp)

### Why This Works:

- **Lower Bound**: Finds the first position where `timestamp >= target_timestamp`
- **Exact Match**: If found, return immediately
- **Previous Element**: If not exact match, the previous element is the largest timestamp < target_timestamp

## Solution 3: Using STL upper_bound

```cpp
class TimeMap {
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        cache[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        if(!cache.contains(key)) return "";

        const auto& values = cache[key];
        auto it = upper_bound(values.begin(), values.end(), timestamp,
                            [](int ts, const pair<int, string>& p) {
            return ts < p.first;
        });

        if(it == values.begin()) return "";
        return prev(it)->second;
    }

private:
    unordered_map<string, vector<pair<int, string>>> cache;
};
```

### Algorithm Breakdown:

1. **Set Operation**: Same as previous solutions - append to vector
2. **Get Operation**:
   - Use `upper_bound` with custom comparator to find first position where `timestamp > target_timestamp`
   - The comparator `[](int ts, const pair<int, string>& p) { return ts < p.first; }` compares target timestamp with element's timestamp
   - If `upper_bound` returns `begin()`, no valid timestamp exists (all timestamps > target), return `""`
   - Otherwise, return the value at `prev(it)` (the largest timestamp <= target_timestamp)

### Why This Works:

- **Upper Bound**: Finds the first position where `timestamp > target_timestamp`
- **Previous Element**: The element before `upper_bound` is the largest timestamp <= target_timestamp
- **Simpler Logic**: No need to check for exact match - `prev(it)` always gives the correct answer
- **Comparator Order**: Note the parameter order is reversed: `(int ts, const pair<int, string>& p)` instead of `(const pair<int, string>& p, int ts)`

### Sample Test Case Run:

**Input:** 
```
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);
timeMap.get("foo", 1);
timeMap.get("foo", 3);
timeMap.set("foo", "bar2", 4);
timeMap.get("foo", 4);
timeMap.get("foo", 5);
```

**Solution 1 Execution:**

```
Step 1: set("foo", "bar", 1)
  cache["foo"] = [(1, "bar")]

Step 2: get("foo", 1)
  values = [(1, "bar")]
  left = 0, right = 1
  
  Iteration 1:
    mid = 0 + (1 - 0) / 2 = 0
    values[0].first = 1 <= 1 ✓
    rtn = "bar"
    left = 0 + 1 = 1
    Search range: [1, 1]
  
  Loop condition: left (1) < right (1) is false, exit loop
  
  Return: "bar" ✓

Step 3: get("foo", 3)
  values = [(1, "bar")]
  left = 0, right = 1
  
  Iteration 1:
    mid = 0 + (1 - 0) / 2 = 0
    values[0].first = 1 <= 3 ✓
    rtn = "bar"
    left = 0 + 1 = 1
    Search range: [1, 1]
  
  Loop condition: left (1) < right (1) is false, exit loop
  
  Return: "bar" ✓

Step 4: set("foo", "bar2", 4)
  cache["foo"] = [(1, "bar"), (4, "bar2")]

Step 5: get("foo", 4)
  values = [(1, "bar"), (4, "bar2")]
  left = 0, right = 2
  
  Iteration 1:
    mid = 0 + (2 - 0) / 2 = 1
    values[1].first = 4 <= 4 ✓
    rtn = "bar2"
    left = 1 + 1 = 2
    Search range: [2, 2]
  
  Loop condition: left (2) < right (2) is false, exit loop
  
  Return: "bar2" ✓

Step 6: get("foo", 5)
  values = [(1, "bar"), (4, "bar2")]
  left = 0, right = 2
  
  Iteration 1:
    mid = 0 + (2 - 0) / 2 = 1
    values[1].first = 4 <= 5 ✓
    rtn = "bar2"
    left = 1 + 1 = 2
    Search range: [2, 2]
  
  Loop condition: left (2) < right (2) is false, exit loop
  
  Return: "bar2" ✓
```

**Output:** `[null, null, "bar", "bar", null, "bar2", "bar2"]` ✓

---

**Another Example:** `get("love", 15)` after `set("love", "high", 10)` and `set("love", "low", 20)`

```
Step 1: set("love", "high", 10)
  cache["love"] = [(10, "high")]

Step 2: set("love", "low", 20)
  cache["love"] = [(10, "high"), (20, "low")]

Step 3: get("love", 15)
  values = [(10, "high"), (20, "low")]
  left = 0, right = 2
  
  Iteration 1:
    mid = 0 + (2 - 0) / 2 = 1
    values[1].first = 20 <= 15 ✗
    right = mid = 1
    Search range: [0, 1]
  
  Iteration 2:
    mid = 0 + (1 - 0) / 2 = 0
    values[0].first = 10 <= 15 ✓
    rtn = "high"
    left = 0 + 1 = 1
    Search range: [1, 1]
  
  Loop condition: left (1) < right (1) is false, exit loop
  
  Return: "high" ✓
```

**Verification:** 
- Timestamp 10 <= 15 ✓
- Timestamp 20 > 15 ✗
- Largest valid timestamp is 10 with value "high" ✓

**Output:** `"high"` ✓

## Complexity Analysis

- **Time Complexity**: 
  - `set`: O(1) amortized - appending to vector
  - `get`: O(log n) - binary search, where n is the number of values for that key
- **Space Complexity**: O(n) - storing all key-value pairs with timestamps

## Key Insights

1. **Strictly Increasing Timestamps**: The guarantee that timestamps are strictly increasing means we don't need to sort - values are automatically in sorted order
2. **Binary Search Pattern**: Finding the largest timestamp <= target is a variant of binary search
3. **Rightmost Valid Element**: We need the rightmost position where `timestamp <= target_timestamp`
4. **STL Alternatives**: 
   - `lower_bound`: Finds first position where `timestamp >= target`, then check previous element
   - `upper_bound`: Finds first position where `timestamp > target`, previous element is always the answer
   - `upper_bound` is slightly simpler as it doesn't require checking for exact match

## Related Problems

- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Binary search with lower/upper bounds
- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) - Lower bound binary search
- [146. LRU Cache](https://leetcode.com/problems/lru-cache/) - Another design problem with time-based operations
- [729. My Calendar I](https://leetcode.com/problems/my-calendar-i/) - Interval-based design problem
