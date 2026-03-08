---
layout: post
title: "LeetCode 383. Ransom Note"
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

## Approach 1: Frequency Array -- $O(n + m)$ time, $O(1)$ space

Since characters are lowercase letters, a 26-element array suffices.

{% raw %}
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
{% endraw %}

**Time**: $O(n + m)$
**Space**: $O(1)$ -- fixed 26-element array

## Approach 2: Hash Map -- $O(n + m)$ time, $O(k)$ space

Generalizes to any character set.

{% raw %}
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
{% endraw %}

**Time**: $O(n + m)$
**Space**: $O(k)$ where $k$ is the number of distinct characters

## Common Mistakes

- Counting `ransomNote` instead of `magazine` first (need to build the supply before consuming)
- Forgetting the early exit on negative count (checking only at the end misses efficiency)

## Key Takeaways

- Same frequency counting pattern as [LC 242 Valid Anagram](/2026/03/07/easy-242-valid-anagram/), but **one-directional**: magazine supplies letters, ransom note consumes them
- The array solution is preferred in interviews: faster, constant space, simpler
- This is a "is A a subset of B (with multiplicity)" check

## Related Problems

- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) -- same frequency counting, bidirectional
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) -- group by frequency signature
- [1189. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/) -- frequency supply/demand variant

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
