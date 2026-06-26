---
layout: post
title: "[Medium] 5. Longest Palindromic Substring"
date: 2026-01-08 00:00:00 -0700
categories: [leetcode, medium, string, two-pointers, dynamic-programming]
permalink: /2026/01/08/medium-5-longest-palindromic-substring/
tags: [leetcode, medium, string, two-pointers, palindrome, expand-around-center, manacher]
---
Given a string `s`, return *the longest **palindromic substring** in* `s`.

A **palindrome** is a string that reads the same backward as forward.

## Examples

**Example 1:**
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

**Example 3:**
```
Input: s = "a"
Output: "a"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Solution Approaches

There are several approaches to solve this problem:

1. **Expand Around Center**: For each position, expand outward to find palindromes (O(n²) time, O(1) space)
2. **Manacher's Algorithm**: Linear time algorithm using preprocessing (O(n) time, O(n) space)
3. **Dynamic Programming**: Build a DP table to track palindromes (O(n²) time, O(n²) space)

### Approach 1: Expand Around Center (Recommended for Interviews)

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

The key insight is that every palindrome expands from a center. For each position, we check:
- **Odd-length palindromes**: Center at a single character (e.g., "aba" centered at 'b')
- **Even-length palindromes**: Center between two characters (e.g., "abba" centered between two 'b's)

### Approach 2: Manacher's Algorithm (Optimal)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Uses preprocessing to transform the string and then uses symmetry properties to avoid redundant checks.

## Thinking Process

1. **Two Types of Centers**: Odd-length (single char) and even-length (between chars)

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
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Solution

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        const int N = s.size();
        if(N < 2) return s;
        int start = 0, maxLen = 1;
        for(int i = 0; i < N; i++) {
            expandAroundCenter(s, i, i, start, maxLen);
            expandAroundCenter(s, i, i + 1, start, maxLen);
        }
        return s.substr(start, maxLen);
    }

private:
    void expandAroundCenter(const string& s, int left, int right, int& start, int& maxLen) {
        const int N = s.size();
        while(left >=0 && right < N && s[left] == s[right]) {
            int len = right - left + 1;
            if(len > maxLen) {
                start = left;
                maxLen = len;
            }
            left--;
            right++;
        }
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 4-6)**:
   - Handle edge case: if string length < 2, return the string itself
   - Initialize `start = 0` and `maxLen = 1` to track the longest palindrome found

2. **For Each Position (Lines 7-10)**:
   - **Check odd-length palindromes**: Expand from `(i, i)` - center at single character
   - **Check even-length palindromes**: Expand from `(i, i+1)` - center between two characters

3. **Expand Function (Lines 13-22)**:
   - **Expand outward**: While characters match and within bounds, expand `left--` and `right++`
   - **Update maximum**: If current palindrome length > `maxLen`, update `start` and `maxLen`
   - **Stop when mismatch**: Stop expanding when characters don't match or out of bounds

### **Why This Works:**

- **Two types of centers**: Handles both odd and even length palindromes
- **Greedy expansion**: For each center, expands as far as possible
- **Optimal tracking**: Updates the longest palindrome found so far

### **Example Walkthrough:**

**For `s = "babad"`:**

```
Initial: start = 0, maxLen = 1

i = 0: Check "b"
  - Odd: expandAroundCenter(0, 0) → "b" (len=1, no update)
  - Even: expandAroundCenter(0, 1) → "ba" (no match, stop)
  
i = 1: Check "a"
  - Odd: expandAroundCenter(1, 1) → "a" → "bab" (len=3, update: start=0, maxLen=3)
  - Even: expandAroundCenter(1, 2) → "ab" (no match, stop)
  
i = 2: Check "b"
  - Odd: expandAroundCenter(2, 2) → "b" → "aba" (len=3, no update, same length)
  - Even: expandAroundCenter(2, 3) → "ba" (no match, stop)
  
i = 3: Check "a"
  - Odd: expandAroundCenter(3, 3) → "a" (len=1, no update)
  - Even: expandAroundCenter(3, 4) → "ad" (no match, stop)
  
i = 4: Check "d"
  - Odd: expandAroundCenter(4, 4) → "d" (len=1, no update)
  - Even: expandAroundCenter(4, 5) → out of bounds

Result: s.substr(0, 3) = "bab"
```

### **Complexity Analysis:**

- **Time Complexity:** O(n²)
  - For each of n positions, we expand outward
  - In worst case, expansion can go up to n/2 in each direction
  - Total: O(n × n) = O(n²)
- **Space Complexity:** O(1)
  - Only using a few variables: `start`, `maxLen`, `left`, `right`

## Common Mistakes

1. **Single character**: `"a"` → return `"a"`
2. **All same characters**: `"aaa"` → return `"aaa"`
3. **No palindrome > 1**: `"abc"` → return `"a"` (or any single char)
4. **Two palindromes of same length**: `"babad"` → return either `"bab"` or `"aba"`

1. **Missing even-length palindromes**: Forgetting to check centers between characters
2. **Index out of bounds**: Not checking bounds before accessing array
3. **Wrong expansion logic**: Not expanding symmetrically from center
4. **Manacher's preprocessing**: Forgetting to convert back to original indices

## Related Problems

- [LC 647: Palindromic Substrings](https://www.leetcode.com/problems/palindromic-substrings/) - Count all palindromic substrings (same expand-around-center technique)
- [LC 516: Longest Palindromic Subsequence](https://www.leetcode.com/problems/longest-palindromic-subsequence/) - Find longest palindromic subsequence (DP)
- [LC 125: Valid Palindrome](https://www.leetcode.com/problems/valid-palindrome/) - Check if string is palindrome
- [LC 680: Valid Palindrome II](https://www.leetcode.com/problems/valid-palindrome-ii/) - Can make palindrome with 1 deletion

## Key Takeaways

1. **Two Types of Centers**: Odd-length (single char) and even-length (between chars)
2. **Expand Greedily**: For each center, expand as far as possible
3. **Manacher's Symmetry**: Use previously computed palindromes to avoid redundant checks
4. **Preprocessing**: Transform string to handle even-length palindromes uniformly

## References

- [LC 5: Longest Palindromic Substring on LeetCode](https://www.leetcode.com/problems/longest-palindromic-substring/)
- [LeetCode Discuss — LC 5: Longest Palindromic Substring](https://www.leetcode.com/problems/longest-palindromic-substring/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/longest-palindromic-substring/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
