---
layout: post
title: "[Easy] 1207. Unique Number of Occurrences"
date: 2025-10-20 18:00:00 -0700
categories: leetcode easy array hash-table
permalink: /posts/2025-10-20-easy-1207-unique-number-of-occurrences/
tags: [leetcode, easy, array, hash-table, counting]
---
**Difficulty:** Easy  
**Category:** Array, Hash Table  
**Companies:** Amazon, Google, Microsoft


Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique**, or `false` otherwise.

## Examples
**Example 1:**
```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 occurrences, and 3 has 1 occurrence. No two values have the same number of occurrences.
```

**Example 2:**
```
Input: arr = [1,2]
Output: false
Explanation: The value 1 has 1 occurrence, and 2 has 1 occurrence. Two values have the same number of occurrences.
```

**Example 3:**
```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
Explanation: The value -3 has 3 occurrences, 0 has 2 occurrences, 1 has 4 occurrences, and 10 has 1 occurrence. No two values have the same number of occurrences.
```

## Constraints
- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

## Solution Approaches

### Approach 1: Hash Map + Hash Set (Recommended)

**Algorithm:**
1. Count frequency of each element using hash map
2. Store all frequencies in a hash set
3. Check if hash set size equals hash map size (no duplicate frequencies)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> freqs;
        unordered_set<int> occurs;
        for(int num: arr) freqs[num]++;

        for(auto& [num, freq]: freqs)
            occurs.insert(freq);
        return occurs.size() == freqs.size();
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** Difficulty:** Easy

**How the code works:**
**Difficulty:** Easy
**Category:** Array, Hash Table
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

**Walkthrough** — input `arr = [1,2,2,1,1,3]`, expected output `true`:

The value 1 has 3 occurrences, 2 has 2 occurrences, and 3 has 1 occurrence. No two values have the same number of occurrences.
## Implementation Details

### Hash Set Insert Behavior
```cpp
// insert() returns pair<iterator, bool>
// second is true if insertion successful (no duplicate)
if(!occurs.insert(freq).second) return false;
```

### Array Offset Technique
```cpp
// Offset by 1000 to handle negative numbers
freq[num + 1000]++;
```

## Edge Cases

1. **Single Element**: `[1]` → true (frequency 1 is unique)
2. **All Same Elements**: `[1,1,1]` → true (frequency 3 is unique)
3. **All Different Elements**: `[1,2,3]` → true (all frequencies are 1)
4. **Duplicate Frequencies**: `[1,2,2,3]` → false (both 1 and 3 have frequency 1)

## Follow-up Questions

- What if the array could contain very large numbers?
- How would you handle floating-point numbers?
- What if you needed to find which frequencies are duplicated?
- How would you optimize for very large arrays?

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [LC 347: Top K Frequent Elements](https://www.leetcode.com/problems/top-k-frequent-elements/)
- [LC 451: Sort Characters By Frequency](https://www.leetcode.com/problems/sort-characters-by-frequency/)
- [LC 692: Top K Frequent Words](https://www.leetcode.com/problems/top-k-frequent-words/)

## Optimization Techniques

1. **Early Termination**: Stop as soon as duplicate frequency is found
2. **Space Optimization**: Use arrays instead of hash maps for small ranges
3. **Memory Efficiency**: Avoid storing unnecessary data
4. **Cache Performance**: Array-based approach has better cache locality

## Code Quality Notes

1. **Readability**: First approach is most readable and maintainable
2. **Performance**: Array approach is fastest for small ranges
3. **Scalability**: Hash map approach works for any range
4. **Robustness**: All approaches handle edge cases correctly

## Key Takeaways

- **Pattern:** Prefix sum (this problem)
- Difficulty:** Easy
- Category:** Array, Hash Table

## References

- [LC 1207: Unique Number of Occurrences on LeetCode](https://www.leetcode.com/problems/unique-number-of-occurrences/)
- [LeetCode Discuss — LC 1207: Unique Number of Occurrences](https://www.leetcode.com/problems/unique-number-of-occurrences/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/unique-number-of-occurrences/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)

## Thinking Process

**Difficulty:** Easy

**Category:** Array, Hash Table

- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Prefix sum** *(this problem)* | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| Hash map counting | O(n) | O(n) | Frequency, two-sum variants |
