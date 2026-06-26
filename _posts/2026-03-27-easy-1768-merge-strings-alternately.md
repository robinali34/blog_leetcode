---
layout: post
title: "[Easy] 1768. Merge Strings Alternately"
date: 2026-03-27
categories: [leetcode, easy, string, two-pointers]
tags: [leetcode, easy, string, two-pointers]
permalink: /2026/03/27/easy-1768-merge-strings-alternately/
---
Given two strings `word1` and `word2`, merge them by adding letters in alternating order, starting with `word1`. If one string is longer, append the remaining letters at the end.

## Examples

**Example 1:**

```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: a p b q c r
```

**Example 2:**

```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: a p b q + remaining "rs"
```

**Example 3:**

```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: a p b q + remaining "cd"
```

## Constraints

- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters

## Thinking Process

Use two pointers `i` and `j` to walk through both strings simultaneously. In each iteration, take one character from `word1` (if available), then one from `word2` (if available). The loop continues until both strings are exhausted, naturally handling unequal lengths.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Opposite ends** *(this problem)* | $O(n)$ | $O(1)$ | Sorted array pair search, reversal |
| Slow / fast pointers | $O(n)$ | $O(1)$ | Linked list middle, cycle detection |
| Same-direction chase | $O(n)$ | $O(1)$ | Remove duplicates in-place |
| Sliding window (variable) | $O(n)$ | $O(1)$ | Subarray with constraint |

## Solution

{% raw %}
```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        int i = 0, j = 0;
        string rtn;
        rtn.reserve(m + n);

        while (i < m || j < n) {
            if (i < m) {
                rtn += word1[i++];
            }
            if (j < n) {
                rtn += word2[j++];
            }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** Use two pointers `i` and `j` to walk through both strings simultaneously. In each iteration, take one character from `word1` (if available), then one from `word2` (if available). The loop continues until both strings are exhausted, naturally handling unequal lengths.

**Walkthrough** — input `word1 = "abc", word2 = "pqr"`, expected output `"apbqcr"`:

a p b q c r
## Key Details

**`reserve(m + n)`**: Pre-allocates the result string to avoid reallocations during appending. Not required for correctness but good practice.

**`||` not `&&`**: Using `||` in the loop condition ensures we keep going until *both* strings are done. With `&&` we'd stop at the shorter string and lose the remaining characters.

## Common Mistakes

- Using `&&` instead of `||` in the while condition (truncates the longer string)
- Appending both characters unconditionally without checking bounds

## Key Takeaways

- Simple two-pointer merge pattern -- the same idea behind merging two sorted arrays
- The `if` guards inside the loop elegantly handle unequal lengths without separate tail-appending logic

## Related Problems

- [88. Merge Sorted Array](https://www.leetcode.com/problems/merge-sorted-array/) -- two-pointer merge
- [21. Merge Two Sorted Lists](https://www.leetcode.com/problems/merge-two-sorted-lists/) -- merge pattern on linked lists
- [986. Interval List Intersections](https://www.leetcode.com/problems/interval-list-intersections/) -- two-pointer on intervals

## References

- [LC 1768: Merge Strings Alternately on LeetCode](https://www.leetcode.com/problems/merge-strings-alternately/)
- [LeetCode Discuss — LC 1768: Merge Strings Alternately](https://www.leetcode.com/problems/merge-strings-alternately/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/merge-strings-alternately/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
