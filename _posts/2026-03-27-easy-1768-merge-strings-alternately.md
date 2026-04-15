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

## Solution: Two Pointers -- $O(m + n)$

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
{% endraw %}

**Time**: $O(m + n)$
**Space**: $O(1)$ auxiliary (output excluded)

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

- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) -- two-pointer merge
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) -- merge pattern on linked lists
- [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) -- two-pointer on intervals

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
