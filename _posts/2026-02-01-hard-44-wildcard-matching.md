---
layout: post
title: "[Hard] 44. Wildcard Matching"
date: 2026-02-01 00:00:00 -0700
categories: [leetcode, hard, string, dynamic-programming, greedy, two-pointers]
permalink: /2026/02/01/hard-44-wildcard-matching/
tags: [leetcode, hard, string, dynamic-programming, greedy, two-pointers]
---
Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'` where:

- `'?'` Matches any single character.
- `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

## Examples

**Example 1:**

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**

```
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
```

**Example 3:**

```
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

**Example 4:**

```
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, and the second '*' matches the substring "dce".
```

**Example 5:**

```
Input: s = "acdcb", p = "a*c?b"
Output: false
```

## Constraints

- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'?'` or `'*'`.

## Thinking Process

1. **Greedy Strategy**: Try matching as few characters as possible with `'*'` first, then expand if needed

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

## Solution

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty()) return s.empty();

        string pat = "^";
        for(char c: p){
            if(c == '?') pat += '.';
            else if (c == '*') pat += ".*";
            else pat += c;
        }
        pat.push_back('$');
        return regex_search(s, regex(pat));
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **Greedy Strategy**: Try matching as few characters as possible with `'*'` first, then expand if needed

**How the code works:**
1. **Greedy Strategy**: Try matching as few characters as possible with `'*'` first, then expand if needed
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `s = "aa", p = "a"`, expected output `false`:

"a" does not match the entire string "aa".

### Algorithm Breakdown:

1. **Pattern Conversion**: Convert wildcard pattern to regex pattern
   - `'?'` → `'.'` (matches any single character in regex)
   - `'*'` → `".*"` (matches any sequence in regex)
   - Regular characters remain unchanged
2. **Anchoring**: Add `'^'` at start and `'$'` at end to ensure full string match
3. **Regex Search**: Use `regex_search` to check if the entire string matches the pattern

### Why This Works:

- **Regex Equivalence**: Wildcard matching is equivalent to regex matching with specific conversions
- **Full Match**: The `^` and `$` anchors ensure the pattern matches the entire string
- **Simple Implementation**: Leverages built-in regex functionality

### Solution 1 (Regex):
- **Time Complexity**: O(m*n) - Regex matching typically has this complexity
- **Space Complexity**: O(m) - For the converted pattern string

### Solution 2 (Two-Pointer Greedy):
- **Time Complexity**: O(m*n) worst case, O(m+n) average case - In worst case, we may backtrack for each character
- **Space Complexity**: O(1) - Only using a constant amount of extra space

### Solution 3 (Recursion with Memoization):
- **Time Complexity**: O(m*n) - Each (i, j) pair is computed at most once
- **Space Complexity**: O(m*n) - For the memoization table and recursion stack

### Solution 4 (Dynamic Programming):
- **Time Complexity**: O(m*n) - Fill a 2D table of size m×n
- **Space Complexity**: O(m*n) - For the DP table (can be optimized to O(n) with space-optimized version)
## Related Problems

- [10. Regular Expression Matching](https://www.leetcode.com/problems/regular-expression-matching/) - Similar problem with more complex patterns
- [72. Edit Distance](https://www.leetcode.com/problems/edit-distance/) - Dynamic programming with string matching
- [97. Interleaving String](https://www.leetcode.com/problems/interleaving-string/) - String matching with constraints
- [115. Distinct Subsequences](https://www.leetcode.com/problems/distinct-subsequences/) - Pattern matching with counting

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Greedy Strategy**: Try matching as few characters as possible with `'*'` first, then expand if needed
2. **Backtracking**: When a mismatch occurs, backtrack to the last `'*'` and let it match one more character
3. **Star Consolidation**: Multiple consecutive `'*'` can be treated as a single `'*'`
4. **Pattern Completion**: After processing the string, skip any remaining `'*'` and check if pattern is fully consumed
5. **Regex Alternative**: For simplicity, can convert wildcard pattern to regex pattern, though less efficient
6. **DP State Definition**: `dp[i][j]` = whether `s[0..i-1]` matches `p[0..j-1]`
7. **Star Matching**: `'*'` can match zero characters (`dp[i][j-1]`) or one or more characters (`dp[i-1][j]`)
8. **Memoization**: Recursive approach with memoization avoids recomputing the same subproblems

## References

- [LC 44: Wildcard Matching on LeetCode](https://www.leetcode.com/problems/wildcard-matching/)
- [LeetCode Discuss — LC 44: Wildcard Matching](https://www.leetcode.com/problems/wildcard-matching/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/wildcard-matching/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
