---
layout: post
title: "[Medium] 1328. Break a Palindrome"
date: 2026-04-07
categories: [leetcode, medium, string, greedy]
tags: [leetcode, medium, string, greedy]
permalink: /2026/04/07/medium-1328-break-a-palindrome/
---

Given a palindromic string `palindrome`, replace **exactly one** character to make it **not** a palindrome, and make the resulting string the **lexicographically smallest** possible. Return the result, or an empty string if it is impossible.

## Examples

**Example 1:**

```
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: Change 'b' at index 1 to 'a'.
```

**Example 2:**

```
Input: palindrome = "a"
Output: ""
Explanation: Single character — impossible to break.
```

**Example 3:**

```
Input: palindrome = "aa"
Output: "ab"
Explanation: All 'a's — change last to 'b'.
```

**Example 4:**

```
Input: palindrome = "aba"
Output: "abb"
Explanation: Middle char doesn't matter (odd length), all others are 'a' — change last to 'b'.
```

## Constraints

- `1 <= palindrome.length <= 1000`
- `palindrome` consists of lowercase English letters

## Thinking Process

### Impossible Case

A single character string is always a palindrome no matter what we change it to. Return `""`.

### Greedy Strategy

To get the **lexicographically smallest** non-palindrome:

**Step 1: Try to make it smaller.** Scan the **first half** of the string. If any character is not `'a'`, change it to `'a'`. This makes the string smaller and breaks the palindrome (since we only changed one side).

**Step 2: If all `'a'`s.** The string is `"aaa...aaa"`. Any change in the first half would be mirrored and remain a palindrome if we changed to `'a'` -- but they're already `'a'`. The smallest option is to change the **last** character to `'b'`.

### Why Only the First Half?

- Changing a character in the first half to something smaller affects the lexicographic order more significantly (earlier positions matter more)
- We skip the middle character for odd-length strings because changing it doesn't break the palindrome (it mirrors to itself)

### Walk-through

```
"abccba" (n=6, first half indices: 0,1,2)
  i=0: 'a' == 'a' → skip
  i=1: 'b' != 'a' → change to 'a' → "aaccba" ✓

"aaa" (n=3, first half indices: 0)
  i=0: 'a' == 'a' → skip
  All 'a's → change last to 'b' → "aab" ✓
```

## Solution: Greedy -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.size();
        if (n == 1) return "";

        for (int i = 0; i < n / 2; ++i) {
            if (palindrome[i] != 'a') {
                palindrome[i] = 'a';
                return palindrome;
            }
        }
        palindrome[n - 1] = 'b';
        return palindrome;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(1)$ auxiliary (modifying in place)

## Common Mistakes

- Not handling the `n == 1` edge case (impossible to break)
- Scanning the entire string instead of just the first half (changing the second half of a palindrome could recreate a palindrome)
- Changing the middle character of an odd-length all-`'a'` palindrome (e.g., `"aaa"` → `"aba"` is still a palindrome)

## Key Takeaways

- **"Lexicographically smallest with one change"** = greedy from left to right, make the earliest position as small as possible
- The first-half-only scan is the key insight: changing one side of a palindrome always breaks it
- The all-`'a'` fallback (change last to `'b'`) handles the edge case where no position can be made smaller

## Related Problems

- [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) -- palindrome check
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) -- palindrome validation
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) -- palindrome with one deletion
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) -- string manipulation

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
