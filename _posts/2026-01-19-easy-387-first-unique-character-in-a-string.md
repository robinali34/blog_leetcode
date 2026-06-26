---
layout: post
title: "[Easy] 387. First Unique Character in a String"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, string, hash-table]
permalink: /2026/01/19/easy-387-first-unique-character-in-a-string/
tags: [leetcode, easy, string, hash-table, bit-manipulation, frequency-counting]
---
Given a string `s`, find the **first non-repeating character** in it and return its **index**. If it does not exist, return `-1`.

## Examples

**Example 1:**
```
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not repeat.
```

**Example 2:**
```
Input: s = "loveleetcode"
Output: 2
Explanation: The character 'v' at index 2 is the first character that does not repeat.
```

**Example 3:**
```
Input: s = "aabb"
Output: -1
Explanation: All characters repeat, so return -1.
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Thinking Process

1. **Bit Manipulation**: Efficient way to track seen-once vs seen-multiple using XOR and AND operations

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 90" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Bit manipulation</text>

  <text x="40" y="50" font-family="monospace" font-size="14" fill="#3A3530">1 0 1 1 0 1 0</text>
  <text x="40" y="75" font-size="11" fill="#6B6560">XOR pairs · masks · shifts</text>

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
    int firstUniqChar(string s) {
        int once = 0, multi = 0;
        int idx = -1;
        for(char ch : s) {
            int bit = 1 << (ch - 'a');
            multi |= once & bit;
            once ^= bit;
            once &= ~multi;
        }

        for(int i = 0; i < (int)s.length(); i++) {
            int bit = 1 << (s[i] - 'a');
            if(once & bit) {
                return i;
            }
        }
        return -1;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** 1. **Bit Manipulation**: Efficient way to track seen-once vs seen-multiple using XOR and AND operations

**How the code works:**
1. **Bit Manipulation**: Efficient way to track seen-once vs seen-multiple using XOR and AND operations
- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

**Walkthrough** — input `s = "leetcode"`, expected output `0`:

The character 'l' at index 0 is the first character that does not repeat.
## Common Mistakes

1. **All unique**: `s = "abc"` → return `0`
2. **All duplicate**: `s = "aabb"` → return `-1`
3. **Single character**: `s = "a"` → return `0`
4. **Unique at end**: `s = "aabbc"` → return `4`
5. **Unique in middle**: `s = "aabcc"` → return `2` ('b')
6. **Long string**: All characters unique, return `0`

1. **Wrong bit operations**: Incorrect XOR/AND logic in bit manipulation
2. **Index confusion**: Not tracking first occurrence correctly
3. **Off-by-one**: Incorrect character to index conversion
4. **Not handling all duplicates**: Forgetting to return `-1`
5. **Wrong order**: Returning last unique instead of first

## Related Problems

- [LC 383: Ransom Note](https://www.leetcode.com/problems/ransom-note/) - Character frequency counting
- [LC 389: Find the Difference](https://www.leetcode.com/problems/find-the-difference/) - Find extra character
- [LC 451: Sort Characters By Frequency](https://www.leetcode.com/problems/sort-characters-by-frequency/) - Sort by frequency
- [LC 438: Find All Anagrams in a String](https://www.leetcode.com/problems/find-all-anagrams-in-a-string/) - Character frequency matching
- [LC 567: Permutation in String](https://www.leetcode.com/problems/permutation-in-string/) - Sliding window with frequency

## Key Takeaways

1. **Bit Manipulation**: Efficient way to track seen-once vs seen-multiple using XOR and AND operations
2. **Index Tracking**: Store first occurrence index to find minimum later
3. **Two-Pass Approach**: Count first, then find first unique
4. **Early Exit**: Can optimize by scanning string in second pass instead of all 26 characters

## References

- [LC 387: First Unique Character in a String on LeetCode](https://www.leetcode.com/problems/first-unique-character-in-a-string/)
- [LeetCode Discuss — LC 387: First Unique Character in a String](https://www.leetcode.com/problems/first-unique-character-in-a-string/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/first-unique-character-in-a-string/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
