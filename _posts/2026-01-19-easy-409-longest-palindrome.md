---
layout: post
title: "[Easy] 409. Longest Palindrome"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, string, hash-table, greedy]
permalink: /2026/01/19/easy-409-longest-palindrome/
tags: [leetcode, easy, string, hash-table, greedy, bit-manipulation, palindrome]
---
Given a string `s` which consists of lowercase or uppercase letters, return the **length of the longest palindrome** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome here.

**Note:** You can use any characters from the string, and you can rearrange them arbitrarily.

## Examples

**Example 1:**
```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```

**Example 2:**
```
Input: s = "a"
Output: 1
Explanation: The longest palindrome is "a".
```

**Example 3:**
```
Input: s = "bb"
Output: 2
Explanation: The longest palindrome is "bb".
```

## Constraints

- `1 <= s.length <= 2000`
- `s` consists of lowercase and/or uppercase English letters only.

## Thinking Process

1. **Palindrome Structure**: Symmetric pairs + optional center

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

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

```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        int maskl = 0; //[a - z]
        int maskU = 0; //[A - Z]
        int rtn = 0;
        for(char c: s) {
            if('a' <= c && c <= 'z') {
                int bit = 1 << (c - 'a');
                if(maskl & bit) {
                    rtn += 2;
                }
                maskl ^= bit;
            } else {
                int bit = 1 << (c - 'A');
                if(maskU & bit) {
                    rtn += 2;
                }
                maskU ^= bit;
            }
        }
        return (maskl || maskU) ? rtn + 1: rtn;
    }
};
```

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** 1. **Palindrome Structure**: Symmetric pairs + optional center

**How the code works:**
1. **Palindrome Structure**: Symmetric pairs + optional center
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `s = "abccccdd"`, expected output `7`:

One longest palindrome that can be built is "dccaccd", whose length is 7.
## Common Mistakes

1. **Single character**: `s = "a"` → return 1
2. **All pairs**: `s = "bb"` → return 2
3. **All same character**: `s = "aaaa"` → return 4
4. **Mixed case**: `s = "Aa"` → return 1 (case sensitive)
5. **No pairs**: `s = "abc"` → return 1 (one character in center)
6. **All unique**: `s = "abcdef"` → return 1

1. **Case sensitivity**: Treating 'A' and 'a' as same
2. **Center placement**: Forgetting to add 1 when odd counts exist
3. **Pair counting**: Incorrectly counting pairs
4. **Bit manipulation**: Off-by-one errors in bit shifting
5. **Empty string**: Not handling edge case (but constraints guarantee length ≥ 1)

## Related Problems

- [LC 5: Longest Palindromic Substring](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-5-longest-palindromic-substring/) - Find longest palindrome substring
- [LC 125: Valid Palindrome](https://www.leetcode.com/problems/valid-palindrome/) - Check if string is palindrome
- [LC 131: Palindrome Partitioning](https://robinali34.github.io/blog_leetcode/2025/09/30/medium-131-palindrome-partitioning/) - Partition into palindromes
- [LC 647: Palindromic Substrings](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-647-palindromic-substrings/) - Count palindromic substrings
- [LC 1177: Can Make Palindrome from Substring](https://robinali34.github.io/blog_leetcode/2026/01/01/medium-1177-can-make-palindrome-from-substring/) - Check if substring can form palindrome
- [LC 1400: Construct K Palindrome Strings](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-1400-construct-k-palindrome-strings/) - Construct multiple palindromes

## Key Takeaways

1. **Palindrome Structure**: Symmetric pairs + optional center
2. **Pair Counting**: Each pair contributes 2 to length
3. **Odd Handling**: At most one character can be in center
4. **Bit Manipulation**: Efficient way to track odd/even counts
5. **Case Sensitivity**: Must handle uppercase and lowercase separately

## References

- [LC 409: Longest Palindrome on LeetCode](https://www.leetcode.com/problems/longest-palindrome/)
- [LeetCode Discuss — LC 409: Longest Palindrome](https://www.leetcode.com/problems/longest-palindrome/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/longest-palindrome/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
