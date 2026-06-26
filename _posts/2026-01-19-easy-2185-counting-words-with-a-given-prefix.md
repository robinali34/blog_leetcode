---
layout: post
title: "[Easy] 2185. Counting Words With a Given Prefix"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, string, array]
permalink: /2026/01/19/easy-2185-counting-words-with-a-given-prefix/
tags: [leetcode, easy, string, array, prefix, simulation]
---
You are given an array of strings `words` and a string `pref`.

Return the **number** of strings in `words` that contain `pref` as a **prefix**.

A **prefix** of a string `s` is any leading contiguous substring of `s`.

## Examples

**Example 1:**
```
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
```

**Example 2:**
```
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
```

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length, pref.length <= 100`
- `words[i]` and `pref` consist of lowercase English letters.

## Thinking Process

1. **Simple Prefix Matching**: Use substring comparison for clarity

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.



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
| **Two pointers on string** *(this problem)* | $O(n)$ | $O(1)$ | Palindrome, parsing |
| Hash map / frequency | $O(n)$ | $O(k)$ | Anagram, character counts |
| KMP / rolling hash | $O(n)$ | $O(n)$ | Pattern matching |
| Stack parsing | $O(n)$ | $O(n)$ | Decode string, parentheses |

## Solution

```cpp
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int cnt = 0;
        const int prel = pref.length();
        for(auto& word: words) {
            if(word.substr(0, prel) == pref) {
                cnt++;
            }
        }
        return cnt;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** 1. **Simple Prefix Matching**: Use substring comparison for clarity

**How the code works:**
1. **Simple Prefix Matching**: Use substring comparison for clarity
- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

**Walkthrough** — input `words = ["pay","attention","practice","attend"], pref = "at"`, expected output `2`:

The 2 strings that contain "at" as a prefix are: "attention" and "attend".
## Common Mistakes

1. **Word shorter than prefix**: `substr(0, prel)` returns a shorter string, comparison fails correctly
2. **Empty prefix**: If `pref = ""`, all words match (but constraints guarantee `pref.length >= 1`)
3. **Prefix equals word**: Word still counts (e.g., `pref = "at"`, `word = "at"` → match)
4. **No matches**: Returns 0 correctly
5. **All words match**: Returns `words.length`
6. **Single character prefix**: Works correctly with `pref = "a"`

1. **Out-of-bounds access**: Not checking word length before accessing characters
2. **Off-by-one errors**: Incorrect substring indices
3. **Case sensitivity**: Problem states lowercase only, but worth noting
4. **Forgetting to increment counter**: Missing the increment statement
5. **Using wrong comparison**: Comparing entire word instead of prefix

## When to Use This Pattern

1. **Prefix Matching**: Checking if strings start with specific patterns
2. **Filtering**: Selecting items from a collection based on prefix
3. **Autocomplete**: Finding words that start with user input
4. **String Processing**: Text analysis and pattern matching
5. **Data Validation**: Checking format or structure of strings

## Related Problems

- [LC 208: Implement Trie (Prefix Tree)](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-208-implement-trie/) - More efficient for multiple prefix queries
- [LC 211: Design Add and Search Words Data Structure](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-211-design-add-and-search-words-data-structure/) - Trie with wildcard support
- [LC 648: Replace Words](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-648-replace-words/) - Prefix matching with replacement
- [LC 14: Longest Common Prefix](https://www.leetcode.com/problems/longest-common-prefix/) - Finding common prefix
- [LC 720: Longest Word in Dictionary](https://www.leetcode.com/problems/longest-word-in-dictionary/) - Prefix-based word selection

## Key Takeaways

1. **Simple Prefix Matching**: Use substring comparison for clarity
2. **Length Safety**: `substr(0, prel)` automatically handles cases where word is shorter than prefix (returns shorter substring)
3. **Efficient**: Linear time complexity, suitable for given constraints
4. **Readable**: Clear and straightforward implementation

## References

- [LC 2185: Counting Words With a Given Prefix on LeetCode](https://www.leetcode.com/problems/counting-words-with-a-given-prefix/)
- [LeetCode Discuss — LC 2185: Counting Words With a Given Prefix](https://www.leetcode.com/problems/counting-words-with-a-given-prefix/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/counting-words-with-a-given-prefix/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
