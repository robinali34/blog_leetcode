---
layout: post
title: "[Medium] 2080. Range Frequency Queries"
date: 2026-01-28 00:00:00 -0700
categories: [leetcode, medium, array, hash-map, binary-search, design]
permalink: /2026/01/28/medium-2080-range-frequency-queries/
tags: [leetcode, medium, array, hash-map, binary-search, design]
---
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

## Thinking Process

1. **Preprocessing is Key**: Building index map once allows fast queries
- `lower_bound`: First index `>= left` (inclusive start)
- `upper_bound`: First index `> right` (exclusive end)
- Difference gives count in range

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
| **Standard binary search** *(this problem)* | $O(\log n)$ | $O(1)$ | Sorted array, `left <= right` |
| Lower / upper bound | $O(\log n)$ | $O(1)$ | First/last position, insert index |
| Binary search on rotated array | $O(\log n)$ | $O(1)$ | Identify sorted half, discard other |
| Binary search on answer | $O(n \log M)$ | $O(1)$ | Monotonic predicate over search space |

## Solution

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

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Preprocessing is Key**: Building index map once allows fast queries

**How the code works:**
1. **Preprocessing is Key**: Building index map once allows fast queries
- `lower_bound`: First index `>= left` (inclusive start)
- `upper_bound`: First index `> right` (exclusive end)
- Difference gives count in range
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
## Common Mistakes

1. **Value not in array**: `query(0, 5, 99)` → return `0`
2. **Value not in range**: `query(3, 5, 33)` when `33` only at indices `[1, 7]` → return `0`
3. **Single occurrence**: `query(0, 11, 4)` → return `1`
4. **All occurrences**: `query(0, 11, 33)` → return `2`
5. **Single element range**: `query(2, 2, 4)` → return `1` if `arr[2] == 4`

1. **Wrong binary search bounds**: Using `upper_bound` for both ends
2. **Not checking existence**: Accessing `freqArray[value]` without checking
3. **Index confusion**: Mixing 0-indexed and 1-indexed arrays
4. **Not using sorted indices**: Assuming indices are sorted without verification
5. **Inefficient approach**: Linear scan for each query (O(n) per query)

## Related Problems

- [LC 303: Range Sum Query - Immutable](https://robinali34.github.io/blog_leetcode/2026/01/01/easy-303-range-sum-query-immutable/) - Range sum queries
- [LC 307: Range Sum Query - Mutable](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-307-range-sum-query-mutable/) - Range sum with updates
- [LC 315: Count of Smaller Numbers After Self](https://robinali34.github.io/blog_leetcode/2026/01/17/hard-315-count-of-smaller-numbers-after-self/) - Counting in ranges
- [LC 327: Count of Range Sum](https://robinali34.github.io/blog_leetcode/2026/01/20/hard-327-count-of-range-sum/) - Range counting

## Key Takeaways

1. **Preprocessing is Key**: Building index map once allows fast queries
2. **Sorted Indices**: Since we iterate in order, indices are naturally sorted
3. **Binary Search**: Efficiently find indices in range `[left, right]`
4. **lower_bound vs upper_bound**:
   - `lower_bound`: First index `>= left` (inclusive start)
   - `upper_bound`: First index `> right` (exclusive end)
   - Difference gives count in range

5. **Hash Map Lookup**: O(1) average case to get indices for a value

## References

- [LC 2080: Range Frequency Queries on LeetCode](https://www.leetcode.com/problems/range-frequency-queries/)
- [LeetCode Discuss — LC 2080: Range Frequency Queries](https://www.leetcode.com/problems/range-frequency-queries/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/range-frequency-queries/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
