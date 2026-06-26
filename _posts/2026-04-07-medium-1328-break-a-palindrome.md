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



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

## Solution

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

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** ### Impossible Case

**How the code works:**
**Step 1: Try to make it smaller.** Scan the **first half** of the string. If any character is not `'a'`, change it to `'a'`. This makes the string smaller and breaks the palindrome (since we only changed one side).
**Step 2: If all `'a'`s.** The string is `"aaa...aaa"`. Any change in the first half would be mirrored and remain a palindrome if we changed to `'a'` -- but they're already `'a'`. The smallest option is to change the **last** character to `'b'`.
- Changing a character in the first half to something smaller affects the lexicographic order more significantly (earlier positions matter more)
- We skip the middle character for odd-length strings because changing it doesn't break the palindrome (it mirrors to itself)

**Walkthrough** — input `palindrome = "abccba"`, expected output `"aaccba"`:

Change 'b' at index 1 to 'a'.
## Common Mistakes

- Not handling the `n == 1` edge case (impossible to break)
- Scanning the entire string instead of just the first half (changing the second half of a palindrome could recreate a palindrome)
- Changing the middle character of an odd-length all-`'a'` palindrome (e.g., `"aaa"` → `"aba"` is still a palindrome)

## Key Takeaways

- **"Lexicographically smallest with one change"** = greedy from left to right, make the earliest position as small as possible
- The first-half-only scan is the key insight: changing one side of a palindrome always breaks it
- The all-`'a'` fallback (change last to `'b'`) handles the edge case where no position can be made smaller

## Related Problems

- [9. Palindrome Number](https://www.leetcode.com/problems/palindrome-number/) -- palindrome check
- [125. Valid Palindrome](https://www.leetcode.com/problems/valid-palindrome/) -- palindrome validation
- [680. Valid Palindrome II](https://www.leetcode.com/problems/valid-palindrome-ii/) -- palindrome with one deletion
- [151. Reverse Words in a String](https://www.leetcode.com/problems/reverse-words-in-a-string/) -- string manipulation

## References

- [LC 1328: Break a Palindrome on LeetCode](https://www.leetcode.com/problems/break-a-palindrome/)
- [LeetCode Discuss — LC 1328: Break a Palindrome](https://www.leetcode.com/problems/break-a-palindrome/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/break-a-palindrome/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
