---
layout: post
title: "[Easy] 392. Is Subsequence"
date: 2026-01-03 05:00:00 -0700
categories: [leetcode, easy, string, two-pointers, greedy, dynamic-programming]
permalink: /2026/01/03/easy-392-is-subsequence/
---
Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`*, or* `false` *otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Thinking Process

Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`*, or* `false` *otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



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
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

## Examples

**Example 1:**
```
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: "abc" is a subsequence of "ahbgdc" (characters at positions 0, 2, 5).
```

**Example 2:**
```
Input: s = "axc", t = "ahbgdc"
Output: false
Explanation: "axc" is not a subsequence of "ahbgdc" because 'x' is not found in "ahbgdc".
```

## Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

## Algorithm Breakdown

### **Why Two Pointers Work**

The two-pointer approach is optimal because:
1. **Order Preservation**: We only advance `i` when we find a match, ensuring order
2. **Greedy Choice**: Always match the first occurrence in `t` (greedy)
3. **Linear Time**: Single pass through both strings
4. **Optimal**: O(n + m) time complexity

### **Pointer Movement Logic**

- **When characters match** (`s[i] == t[j]`):
  - Advance `i` (found character in `s`)
  - Advance `j` (move past matched character in `t`)
  - Then advance `j` again (check next character in `t`)

- **When characters don't match** (`s[i] != t[j]`):
  - Keep `i` unchanged (still looking for this character)
  - Advance `j` (skip this character in `t`)

**Note**: The code increments `j` twice when there's a match (once in the `if` block, once after). This is equivalent to:
```cpp
if(s[i] == t[j]) {
    i++;
}
j++;  // Always advance j
```

### **Subsequence Property**

A subsequence maintains the **relative order** of characters:
- `"ace"` is a subsequence of `"abcde"` (positions 0, 2, 4)
- `"aec"` is NOT a subsequence of `"abcde"` (can't get 'e' before 'c')

## Time & Space Complexity

- **Time Complexity**: O(m) where m is the length of `t`
  - We iterate through `t` at most once
  - Pointer `i` can only advance up to `n` (length of `s`)
  - In worst case, we scan all of `t`
- **Space Complexity**: O(1)
  - Only using a few variables
  - No additional data structures

## Key Points

1. **Two Pointers**: Efficient matching technique
2. **Greedy Matching**: Match first occurrence in `t`
3. **Order Preservation**: Characters must appear in same order
4. **Simple Check**: All characters matched if `i == N`
5. **Edge Case**: Empty string `s` is always a subsequence

## Common Mistakes

1. **Empty `s`**: `s = ""` → return `true` (empty is subsequence of any string)
2. **Empty `t`**: `s = "a"`, `t = ""` → return `false`
3. **Same strings**: `s = "abc"`, `t = "abc"` → return `true`
4. **Single character**: `s = "a"`, `t = "abc"` → return `true`
5. **No match**: `s = "x"`, `t = "abc"` → return `false`
6. **Repeated characters**: `s = "aa"`, `t = "abac"` → return `true`

1. **Wrong pointer logic**: Not advancing `j` when no match
2. **Order violation**: Matching characters out of order
3. **Off-by-one**: Wrong loop condition or index checking
4. **Empty string**: Forgetting that empty string is always subsequence
5. **Not checking all characters**: Returning early before checking all of `s`

## Related Problems

- [524. Longest Word in Dictionary through Deleting](https://www.leetcode.com/problems/longest-word-in-dictionary-through-deleting/) - Find longest subsequence
- [792. Number of Matching Subsequences](https://www.leetcode.com/problems/number-of-matching-subsequences/) - Count subsequences
- [1143. Longest Common Subsequence](https://www.leetcode.com/problems/longest-common-subsequence/) - Find LCS (DP)
- [727. Minimum Window Subsequence](https://www.leetcode.com/problems/minimum-window-subsequence/) - Find minimum window containing subsequence

## Follow-Up: Multiple Queries

If we need to check many strings `s` against the same `t`, we can optimize:

```cpp
// Preprocess t to store character positions
unordered_map<char, vector<int>> charPositions;
for(int i = 0; i < t.length(); i++) {
    charPositions[t[i]].push_back(i);
}

// For each query s, use binary search
bool isSubsequence(string s, unordered_map<char, vector<int>>& pos) {
    int prev = -1;
    for(char c : s) {
        auto it = upper_bound(pos[c].begin(), pos[c].end(), prev);
        if(it == pos[c].end()) return false;
        prev = *it;
    }
    return true;
}
```

**Time**: O(m + n log m) per query (better when many queries)

## Tags

`String`, `Two Pointers`, `Greedy`, `Dynamic Programming`, `Easy`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 392: Is Subsequence on LeetCode](https://www.leetcode.com/problems/is-subsequence/)
- [LeetCode Discuss — LC 392: Is Subsequence](https://www.leetcode.com/problems/is-subsequence/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/is-subsequence/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
