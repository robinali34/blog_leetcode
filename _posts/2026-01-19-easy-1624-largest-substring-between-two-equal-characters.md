---
layout: post
title: "[Easy] 1624. Largest Substring Between Two Equal Characters"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, string, hash-table]
permalink: /2026/01/19/easy-1624-largest-substring-between-two-equal-characters/
tags: [leetcode, easy, string, hash-table, substring, two-pointers]
---
Given a string `s`, return the **length of the longest substring** between two equal characters, **excluding** the two equal characters themselves. If no such substring exists, return `-1`.

A **substring** is a contiguous sequence of characters within a string.

## Examples

**Example 1:**
```
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
```

**Example 2:**
```
Input: s = "abca"
Output: 2
Explanation: The optimal substring is "bc" which is of length 2.
```

**Example 3:**
```
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
```

**Example 4:**
```
Input: s = "cabbac"
Output: 4
Explanation: The optimal substring is "abba" which is of length 4.
```

## Constraints

- `1 <= s.length <= 300`
- `s` contains only lowercase English letters.

## Thinking Process

1. **Two-Pass Approach**: First pass tracks indices, second pass calculates distances

- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Solution

```cpp
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        unordered_map<char, int> LeftIdx, RightIdx;
        int maxLen = -1;
        for(int i = 0; i < (int)s.length(); i++) {
            if(!LeftIdx.contains(s[i])) {
                LeftIdx[s[i]] = i;
            } else {
                RightIdx[s[i]] = i;
            }
        }
        for(auto& [c, idx]: RightIdx) {
            maxLen = max(maxLen, RightIdx[c] - LeftIdx[c] - 1);
        }
        return maxLen;
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** 1. **Two-Pass Approach**: First pass tracks indices, second pass calculates distances

**How the code works:**
1. **Two-Pass Approach**: First pass tracks indices, second pass calculates distances
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `s = "aa"`, expected output `0`:

The optimal substring here is an empty substring between the two 'a's.
## Common Mistakes

1. **No duplicate characters**: `s = "abc"` → return `-1`
2. **Adjacent duplicates**: `s = "aa"` → return `0` (empty substring)
3. **Single character**: `s = "a"` → return `-1`
4. **All same character**: `s = "aaaa"` → return `2` (between first and last)
5. **Multiple pairs**: `s = "cabbac"` → return `4` (between first and last 'c')
6. **Overlapping pairs**: `s = "abba"` → return `2` (between first and last 'a')

1. **Incorrect distance calculation**: Using `right - left` instead of `right - left - 1`
2. **Not handling single occurrence**: Forgetting to return `-1` when no duplicates
3. **Off-by-one errors**: Incorrect substring length calculation
4. **Not updating rightmost**: Only tracking first occurrence, missing last occurrence
5. **Initialization**: Not initializing `maxLen` to `-1` correctly

## When to Use This Pattern

1. **Substring Problems**: Finding distances between character occurrences
2. **Character Frequency**: Tracking first/last occurrence positions
3. **Range Queries**: Calculating lengths between specific positions
4. **String Analysis**: Analyzing character distribution patterns
5. **Optimization Problems**: Finding maximum/minimum distances

## Related Problems

- [LC 3: Longest Substring Without Repeating Characters](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) - Finding longest substring with unique characters
- [LC 159: Longest Substring with At Most Two Distinct Characters](https://www.leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) - Substring with character constraints
- [LC 340: Longest Substring with At Most K Distinct Characters](https://www.leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) - Generalization of LC 159
- [LC 424: Longest Repeating Character Replacement](https://www.leetcode.com/problems/longest-repeating-character-replacement/) - Substring with replacements
- [LC 904: Fruit Into Baskets](https://www.leetcode.com/problems/fruit-into-baskets/) - Similar sliding window pattern

## Key Takeaways

1. **Two-Pass Approach**: First pass tracks indices, second pass calculates distances
2. **Hash Map Efficiency**: O(1) lookup and insertion for character tracking
3. **Distance Formula**: Length between indices `i` and `j` is `j - i - 1` (excluding endpoints)
4. **Edge Case Handling**: Return `-1` when no character appears twice
5. **Optimization**: Only track rightmost index for characters that appear multiple times

## References

- [LC 1624: Largest Substring Between Two Equal Characters on LeetCode](https://www.leetcode.com/problems/largest-substring-between-two-equal-characters/)
- [LeetCode Discuss — LC 1624: Largest Substring Between Two Equal Characters](https://www.leetcode.com/problems/largest-substring-between-two-equal-characters/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/largest-substring-between-two-equal-characters/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
