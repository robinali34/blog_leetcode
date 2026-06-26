---
layout: post
title: "[Medium] 981. Time Based Key-Value Store"
date: 2026-01-30 00:00:00 -0700
categories: [leetcode, medium, hash-table, binary-search, design]
permalink: /2026/01/30/medium-981-time-based-key-value-store/
tags: [leetcode, medium, hash-table, binary-search, design]
---
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

## Thinking Process

1. **Strictly Increasing Timestamps**: The guarantee that timestamps are strictly increasing means we don't need to sort - values are automatically in sorted order
- `lower_bound`: Finds first position where `timestamp >= target`, then check previous element
- `upper_bound`: Finds first position where `timestamp > target`, previous element is always the answer
- `upper_bound` is slightly simpler as it doesn't require checking for exact match

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

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Strictly Increasing Timestamps**: The guarantee that timestamps are strictly increasing means we don't need to sort - values are automatically in sorted order

**How the code works:**
1. **Strictly Increasing Timestamps**: The guarantee that timestamps are strictly increasing means we don't need to sort - values are automatically in sorted order
- `lower_bound`: Finds first position where `timestamp >= target`, then check previous element
- `upper_bound`: Finds first position where `timestamp > target`, previous element is always the answer
- `upper_bound` is slightly simpler as it doesn't require checking for exact match
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.

**Time:** - `set`: O(1) amortized - appending to vector · **Space:** O(n) - storing all key-value pairs with timestamps
## Related Problems

- [34. Find First and Last Position of Element in Sorted Array](https://www.leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Binary search with lower/upper bounds
- [35. Search Insert Position](https://www.leetcode.com/problems/search-insert-position/) - Lower bound binary search
- [146. LRU Cache](https://www.leetcode.com/problems/lru-cache/) - Another design problem with time-based operations
- [729. My Calendar I](https://www.leetcode.com/problems/my-calendar-i/) - Interval-based design problem

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Strictly Increasing Timestamps**: The guarantee that timestamps are strictly increasing means we don't need to sort - values are automatically in sorted order
2. **Binary Search Pattern**: Finding the largest timestamp <= target is a variant of binary search
3. **Rightmost Valid Element**: We need the rightmost position where `timestamp <= target_timestamp`
4. **STL Alternatives**: 
   - `lower_bound`: Finds first position where `timestamp >= target`, then check previous element
   - `upper_bound`: Finds first position where `timestamp > target`, previous element is always the answer
   - `upper_bound` is slightly simpler as it doesn't require checking for exact match

## References

- [LC 981: Time Based Key-Value Store on LeetCode](https://www.leetcode.com/problems/time-based-key-value-store/)
- [LeetCode Discuss — LC 981: Time Based Key-Value Store](https://www.leetcode.com/problems/time-based-key-value-store/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/time-based-key-value-store/editorial/) *(may require premium)*

## Template Reference

- [Search](/blog_leetcode/posts/2026-01-20-leetcode-templates-search/)
