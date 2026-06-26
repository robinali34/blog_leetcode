---
layout: post
title: "[Medium] 692. Top K Frequent Words"
date: 2026-01-08 00:00:00 -0700
categories: [leetcode, medium, hash-table, heap, sorting, string]
permalink: /2026/01/08/medium-692-top-k-frequent-words/
tags: [leetcode, medium, hash-table, heap, sorting, string, priority-queue]
---
Given an array of strings `words` and an integer `k`, return *the* `k` *most frequent strings*.

Return the answer **sorted by the frequency** from highest to lowest. Sort the words with the same frequency by their **lexicographical order**.

## Examples

**Example 1:**
```
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
```

**Example 2:**
```
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 2
Output: ["the","is"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
```

## Constraints

- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- `k` is in the range `[1, The number of unique words[i]]`

## Thinking Process

1. **Custom Comparator**: The key is the two-level sorting: frequency first, then lexicographic order

- Heap gives fast access to min/max without full sorting.
- Size-$k$ heap handles Top-K in $O(n \log k)$.
- Lazy deletion when elements leave the heap before removal.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 120" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary heap</text>

  <circle cx="140" cy="35" r="16" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="39" text-anchor="middle" font-size="11">1</text>
  <circle cx="90" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="90" y="79" text-anchor="middle" font-size="10">3</text>
  <circle cx="190" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="190" y="79" text-anchor="middle" font-size="10">2</text>
  <line x1="140" y1="51" x2="90" y2="61" stroke="#9A9792"/><line x1="140" y1="51" x2="190" y2="61" stroke="#9A9792"/>
  <text x="140" y="110" text-anchor="middle" font-size="11" fill="#6B6560">parent ≤ children (min-heap)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Min/max heap** *(this problem)* | $O(n \log k)$ | $O(k)$ | Top-K, streaming median |
| Two heaps | $O(n \log n)$ | $O(n)$ | Median from data stream |
| Heap + lazy deletion | $O(n \log n)$ | $O(n)$ | Delayed removal |
| Priority-driven search | $O(n \log n)$ | $O(n)$ | Dijkstra, best-first expansion |

## Solution

### **Solution: Hash Map + Custom Sorting**

```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for(auto& word: words) {
            cnt[word]++;
        }
        vector<string> rtn;
        for(auto& [key, value]: cnt) {
            rtn.emplace_back(key);
        }
        sort(rtn.begin(), rtn.end(), [&](const string& a, const string& b){
            return cnt[a] == cnt[b]? a < b : cnt[a] > cnt[b];
        });
        rtn.erase(rtn.begin() + k, rtn.end());
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Min/max heap (this problem)

**Key idea:** 1. **Custom Comparator**: The key is the two-level sorting: frequency first, then lexicographic order

**How the code works:**
1. **Custom Comparator**: The key is the two-level sorting: frequency first, then lexicographic order
- Heap gives fast access to min/max without full sorting.
- Size-$k$ heap handles Top-K in $O(n \log k)$.
- Lazy deletion when elements leave the heap before removal.

**Walkthrough** — input `words = ["i","love","leetcode","i","love","coding"], k = 2`, expected output `["i","love"]`:

"i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
## Related Problems

- [LC 347: Top K Frequent Elements](https://www.leetcode.com/problems/top-k-frequent-elements/) - Similar problem with integers
- [LC 215: Kth Largest Element in an Array](https://www.leetcode.com/problems/kth-largest-element-in-an-array/) - Kth largest element
- [LC 451: Sort Characters By Frequency](https://www.leetcode.com/problems/sort-characters-by-frequency/) - Sort by frequency
- [LC 973: K Closest Points to Origin](https://www.leetcode.com/problems/k-closest-points-to-origin/) - Top K with custom ordering

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Custom Comparator**: The key is the two-level sorting: frequency first, then lexicographic order
2. **Hash Map Efficiency**: `unordered_map` provides O(1) average case for frequency counting
3. **Sorting Trade-off**: Simple sorting works well for small inputs; heap is better for large k
4. **Lexicographic Order**: When frequencies are equal, use standard string comparison (`<`)

## References

- [LC 692: Top K Frequent Words on LeetCode](https://www.leetcode.com/problems/top-k-frequent-words/)
- [LeetCode Discuss — LC 692: Top K Frequent Words](https://www.leetcode.com/problems/top-k-frequent-words/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/top-k-frequent-words/editorial/) *(may require premium)*

## Template Reference

- [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/)
