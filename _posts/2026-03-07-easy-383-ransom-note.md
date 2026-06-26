---
layout: post
title: "[Easy] 383. Ransom Note"
date: 2026-03-07
categories: [leetcode, easy, string, hash]
tags: [leetcode, easy, string, hash, frequency-count]
permalink: /2026/03/07/easy-383-ransom-note/
---
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine`. Each letter in `magazine` can only be used once.

## Examples

**Example 1:**

```
Input: ransomNote = "a", magazine = "b"
Output: false
```

**Example 2:**

```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

**Example 3:**

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

## Constraints

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Thinking Process

This is a frequency counting problem: does `magazine` have enough of each character to build `ransomNote`?

Count character frequencies in `magazine`, then consume them for each character in `ransomNote`. If any count goes negative, the magazine doesn't have enough of that letter.

### Walk-Through: ransomNote = "aa", magazine = "aab"

```
After scanning magazine:  a:2, b:1
Consume 'a' → a:1
Consume 'a' → a:0
All valid → return true
```

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

## Approach 1: Frequency Array -- O(n + m) time, O(1) space

Since characters are lowercase letters, a 26-element array suffices.
```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int count[26] = {0};

        for (char c : magazine)
            count[c - 'a']++;

        for (char c : ransomNote) {
            count[c - 'a']--;
            if (count[c - 'a'] < 0)
                return false;
        }

        return true;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** This is a frequency counting problem: does `magazine` have enough of each character to build `ransomNote`?

**Walkthrough** — input `ransomNote = "a", magazine = "b"`, expected output `false`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Approach 2: Hash Map -- O(n + m) time, O(k) space

Generalizes to any character set.
```cpp
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> count;

        for (char c : magazine) count[c]++;

        for (char c : ransomNote) {
            if (--count[c] < 0) return false;
        }

        return true;
    }
};
```

**Time**: O(n + m)
**Space**: O(k) where k is the number of distinct characters

## Common Mistakes

- Counting `ransomNote` instead of `magazine` first (need to build the supply before consuming)
- Forgetting the early exit on negative count (checking only at the end misses efficiency)

## Key Takeaways

- Same frequency counting pattern as [LC 242 Valid Anagram](/2026/03/07/easy-242-valid-anagram/), but **one-directional**: magazine supplies letters, ransom note consumes them
- The array solution is preferred in interviews: faster, constant space, simpler
- This is a "is A a subset of B (with multiplicity)" check

## Related Problems

- [242. Valid Anagram](https://www.leetcode.com/problems/valid-anagram/) -- same frequency counting, bidirectional
- [49. Group Anagrams](https://www.leetcode.com/problems/group-anagrams/) -- group by frequency signature
- [1189. Maximum Number of Balloons](https://www.leetcode.com/problems/maximum-number-of-balloons/) -- frequency supply/demand variant

## References

- [LC 383: Ransom Note on LeetCode](https://www.leetcode.com/problems/ransom-note/)
- [LeetCode Discuss — LC 383: Ransom Note](https://www.leetcode.com/problems/ransom-note/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/ransom-note/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
