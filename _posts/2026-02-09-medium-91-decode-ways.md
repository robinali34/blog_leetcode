---
layout: post
title: "[Medium] 91. Decode Ways"
date: 2026-02-09 00:00:00 -0700
categories: [leetcode, medium, dynamic-programming]
permalink: /2026/02/09/medium-91-decode-ways/
tags: [leetcode, medium, dynamic-programming, string]
---
A message containing letters from `A-Z` can be **encoded** into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To **decode** an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `"11106"` can be mapped into:

*   `"AAJF"` with the grouping `(1 1 10 6)`
*   `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return *the **number** of ways to **decode** it*.

The test cases are generated so that the answer fits in a **32-bit** integer.

## Examples

**Example 1:**

```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**

```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

**Example 3:**

```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

## Constraints

*   `1 <= s.length <= 100`
*   `s` contains only digits and may contain leading zero(s).

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

## Thinking Process

This is a classic 1D dynamic programming problem, similar to the Fibonacci sequence or the Climbing Stairs problem, but with added validity checks for the digits.

### Solution 1: Standard 1D DP

```cpp
class Solution {
public:
    int numDecodings(string s) {
        if(s.empty() || s[0] == '0') return 0;

        int n = s.length();
        vector<int> dp(n, 0);
        dp[0] = 1;
        for(int i = 1; i < n; i++) {
            // Single char
            if(s[i] != '0') {
                dp[i] += dp[i - 1];
            }
            // Two chars
            int two_digits = (s[i - 1] - '0') * 10 + (s[i] - '0');
            if(s[i - 1] != '0' && two_digits <= 26) {
                dp[i] += (i >= 2 ? dp[i - 2] : 1);
            }
        }
        return dp[n - 1];
    }
};
```

### Solution 2: Space Optimized DP

```cpp
class Solution {
public:
    int numDecodings(string s) {
        if(s.empty() || s[0] == '0') return 0;

        int n = s.length();
        int prev1 = 1, prev2 = 1;
        for(int i = 1; i < n; i++) {
            int curr = 0;
            // Single char
            if(s[i] != '0') {
                curr += prev1;
            }
            // Two chars
            int two_digits = (s[i - 1] - '0') * 10 + (s[i] - '0');
            if(s[i - 1] != '0' && two_digits <= 26) {
                curr += (i >= 2 ? prev2 : 1);
            }
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};
```

### Complexity
*   **Time Complexity**: O(n), where n is the length of the string. We iterate through the string once.
*   **Space Complexity**: 
    *   Solution 1: O(n) for the DP array.
    *   Solution 2: O(1) as we only use a few integer variables.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">1D DP recurrence</text>

  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>

</svg>

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

*   [70. Climbing Stairs](https://www.leetcode.com/problems/climbing-stairs/)
*   [639. Decode Ways II](https://www.leetcode.com/problems/decode-ways-ii/)
*   [198. House Robber](https://www.leetcode.com/problems/house-robber/)

## Key Takeaways

- Time Complexity**: O(n), where n is the length of the string. We iterate through the string once.
- Space Complexity**:
- Solution 1: O(n) for the DP array.

## References

- [LC 91: Decode Ways on LeetCode](https://www.leetcode.com/problems/decode-ways/)
- [LeetCode Discuss — LC 91: Decode Ways](https://www.leetcode.com/problems/decode-ways/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/decode-ways/editorial/) *(may require premium)*

## Template Reference

See [Dynamic Programming Templates: 1D DP](/posts/2025-10-29-leetcode-templates-dp/#1d-dp-knapsacklinear) for more similar patterns.
