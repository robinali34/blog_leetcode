---
layout: post
title: "[Easy] 3110. Score of a String"
date: 2026-01-18 00:00:00 -0700
categories: [leetcode, easy, string, array]
permalink: /2026/01/18/easy-3110-score-of-a-string/
tags: [leetcode, easy, string, array, simulation, ascii]
---
You are given a string `s`. The **score** of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the **score** of `s`.

## Examples

**Example 1:**
```
Input: s = "hello"
Output: 13

Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'l' = 108, 'o' = 111.
So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
```

**Example 2:**
```
Input: s = "zaz"
Output: 50

Explanation:
The ASCII values of the characters in s are: 'z' = 122, 'a' = 97, 'z' = 122.
So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
```

## Constraints

- `2 <= s.length <= 100`
- `s` consists only of lowercase English letters.

## Thinking Process

1. **Simple Simulation**: No complex algorithm needed, just iterate and sum

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
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Solution

```cpp
class Solution {
public:
    int scoreOfString(string s) {
        int sum = 0;
        for(int i = 0; i < (int)s.length() - 1; i++) {
            sum += abs(s[i] - s[i + 1]);
        }
        return sum;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** 1. **Simple Simulation**: No complex algorithm needed, just iterate and sum

**How the code works:**
1. **Simple Simulation**: No complex algorithm needed, just iterate and sum
- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

**Walkthrough** — input `s = "hello"`, expected output `13`:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'l' = 108, 'o' = 111.
So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
## Common Mistakes

1. **Minimum length (n=2)**: `s = "ab"` → `|97 - 98| = 1`
2. **Same characters**: `s = "aa"` → `|97 - 97| = 0`
3. **Maximum difference**: `s = "az"` → `|97 - 122| = 25`
4. **Repeated characters**: `s = "aaa"` → `0 + 0 = 0`
5. **Alternating**: `s = "abab"` → `1 + 1 + 1 = 3`

1. **Off-by-one error**: Looping to `s.length()` instead of `s.length() - 1`
2. **Unsigned comparison**: Not casting `s.length()` to `int` can cause issues
3. **Forgetting absolute value**: Using `s[i] - s[i+1]` without `abs()`
4. **Empty string**: Not handling (though constraints guarantee `n >= 2`)
5. **Integer overflow**: Not an issue here since ASCII values are small (97-122)

## Related Problems

- [LC 3111: Minimum Rectangles to Cover Points](https://www.leetcode.com/problems/minimum-rectangles-to-cover-points/) - Similar string/array processing
- [LC 3112: Minimum Time to Visit Disappearing Nodes](https://www.leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/) - Graph traversal
- [LC 13: Roman to Integer](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-13-roman-to-integer/) - Character value processing
- [LC 171: Excel Sheet Column Number](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-171-excel-sheet-column-number/) - Character to number conversion

---

*This problem is a simple **simulation** exercise that demonstrates basic string iteration and ASCII value manipulation. The key is to iterate through adjacent pairs and sum their absolute differences.*

## Key Takeaways

1. **Simple Simulation**: No complex algorithm needed, just iterate and sum
2. **ASCII Conversion**: Characters automatically convert to integers in C++
3. **Boundary Handling**: Loop from `0` to `length-2` to access all adjacent pairs
4. **Type Safety**: Cast `s.length()` to `int` to avoid unsigned comparison issues
5. **Absolute Value**: Always use `abs()` to ensure positive differences

## References

- [LC 3110: Score of a String on LeetCode](https://www.leetcode.com/problems/score-of-a-string/)
- [LeetCode Discuss — LC 3110: Score of a String](https://www.leetcode.com/problems/score-of-a-string/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/score-of-a-string/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
