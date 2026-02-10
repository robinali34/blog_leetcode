---
layout: post
title: "91. Decode Ways"
date: 2026-02-09 00:00:00 -0700
categories: [leetcode, medium, dynamic-programming]
permalink: /2026/02/09/medium-91-decode-ways/
tags: [leetcode, medium, dynamic-programming, string]
---

# 91. Decode Ways

## Problem Statement

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

## Clarification Questions

1.  **Leading zeros**: Does a string starting with '0' have any valid decodings? (No, '0' doesn't map to anything and leading zeros are invalid for 2-digit mappings)
2.  **Invalid characters**: Can the string contain non-digit characters? (Constraint says only digits)
3.  **Result size**: Does the result fit in a standard integer? (Yes, fits in 32-bit integer)

## Interview Deduction Process

1.  **Subproblem identification**: To find the ways to decode a string of length `n`, we can look at the ways to decode the string up to `n-1` (if the last digit is valid) and the string up to `n-2` (if the last two digits are valid).
2.  **State definition**: Let `dp[i]` be the number of ways to decode the prefix of the string of length `i+1`.
3.  **Transitions**:
    *   **Single digit**: If `s[i] != '0'`, we can append `s[i]` to any decoding of `s[0...i-1]`. So `dp[i] += dp[i-1]`.
    *   **Two digits**: If the substring `s[i-1...i]` represents a number between 10 and 26, we can append this 2-digit number to any decoding of `s[0...i-2]`. So `dp[i] += dp[i-2]`.
4.  **Space optimization**: Notice that `dp[i]` only depends on `dp[i-1]` and `dp[i-2]`. We can reduce space complexity from $O(n)$ to $O(1)$ by using two variables.

## Solution Approach

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

## Complexity Analysis

*   **Time Complexity**: $O(n)$, where $n$ is the length of the string. We iterate through the string once.
*   **Space Complexity**: 
    *   Solution 1: $O(n)$ for the DP array.
    *   Solution 2: $O(1)$ as we only use a few integer variables.

## Related Problems

*   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
*   [639. Decode Ways II](https://leetcode.com/problems/decode-ways-ii/)
*   [198. House Robber](https://leetcode.com/problems/house-robber/)

## Template Reference

See [Dynamic Programming Templates: 1D DP](/posts/2025-10-29-leetcode-templates-dp/#1d-dp-knapsacklinear) for more similar patterns.
