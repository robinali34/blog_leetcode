---
layout: post
title: "LeetCode 242. Valid Anagram"
date: 2026-03-07
categories: [leetcode, easy, string, hash]
tags: [leetcode, easy, string, hash, sorting]
permalink: /2026/03/07/easy-242-valid-anagram/
---

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram uses the exact same characters with the exact same frequencies.

## Examples

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false
```

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters

**Follow-up:** What if the inputs contain Unicode characters?

## Thinking Process

Two strings are anagrams if and only if they have the same character frequencies. Three ways to check this:

1. **Frequency array** -- since only 26 lowercase letters, use a fixed-size array. Increment for `s`, decrement for `t`. If all counts are zero, it's an anagram.
2. **Hash map** -- generalizes to Unicode. Same logic but with a map instead of an array.
3. **Sorting** -- sort both strings and compare. Simplest but slowest.

The key trick: increment and decrement in the **same** array. If everything cancels to zero, the frequencies match.

## Approach 1: Frequency Array -- $O(n)$ time, $O(1)$ space

The expected optimal solution. Since characters are lowercase letters, a 26-element array suffices.

{% raw %}
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        int count[26] = {0};

        for (int i = 0; i < (int)s.size(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (int c : count) {
            if (c != 0) return false;
        }

        return true;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(1)$ -- fixed 26-element array

**Compact variant** -- early exit on negative count:

{% raw %}
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        for (char c : t) if (--cnt[c - 'a'] < 0) return false;
        return s.size() == t.size();
    }
};
```
{% endraw %}

## Approach 2: Hash Map -- $O(n)$ time, $O(n)$ space

Generalizes to Unicode characters. Use a map instead of a fixed array.

{% raw %}
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, int> freq;

        for (char c : s) freq[c]++;
        for (char c : t) {
            if (--freq[c] < 0) return false;
        }

        return true;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ -- up to $n$ distinct characters

## Approach 3: Sorting -- $O(n \log n)$

Sort both strings and compare directly. Simplest to write but slowest.

{% raw %}
```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};
```
{% endraw %}

**Time**: $O(n \log n)$
**Space**: $O(1)$ (ignoring sort internals)

## Comparison

| Approach | Time | Space | Unicode? |
|---|---|---|---|
| Frequency Array | $O(n)$ | $O(1)$ | No (26 letters only) |
| Hash Map | $O(n)$ | $O(n)$ | Yes |
| Sorting | $O(n \log n)$ | $O(1)$ | Yes |

## Common Mistakes

- Forgetting the length check -- different-length strings can never be anagrams
- Using two separate arrays/maps instead of one (works but wastes space)
- Not handling the follow-up: frequency array only works for fixed alphabets

## Key Takeaways

- **Frequency counting** is the core technique for anagram/permutation problems
- The `++` / `--` in one array trick is reusable: same pattern appears in sliding window permutation checks
- For small fixed alphabets, arrays beat hash maps in both speed and simplicity

## Related Problems

- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) -- group strings by sorted canonical form
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) -- sliding window + frequency count
- [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) -- same sliding window pattern

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
