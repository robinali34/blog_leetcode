---
layout: post
title: "5. Longest Palindromic Substring"
date: 2026-01-08 00:00:00 -0700
categories: [leetcode, medium, string, two-pointers, dynamic-programming]
permalink: /2026/01/08/medium-5-longest-palindromic-substring/
tags: [leetcode, medium, string, two-pointers, palindrome, expand-around-center, manacher]
---

# 5. Longest Palindromic Substring

## Problem Statement

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

## Solution 1: Expand Around Center

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

## Solution 2: Manacher's Algorithm

```cpp
class Solution {
private:
    string preprocess(const string& s) {
        string t = "^";
        for (char c : s) {
            t += "#";
            t += c;
        }
        t += "#$";
        return t;
    }

public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";

        string t = preprocess(s);
        int n = t.size();
        vector<int> p(n, 0);

        int center = 0, right = 0;

        for (int i = 1; i < n - 1; i++) {
            int mirror = 2 * center - i;

            if (i < right)
                p[i] = min(right - i, p[mirror]);

            // Expand around center i
            while (t[i + p[i] + 1] == t[i - p[i] - 1])
                p[i]++;

            // Update center and right boundary
            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }
        }

        // Find the longest palindrome
        int maxLen = 0, centerIndex = 0;
        for (int i = 1; i < n - 1; i++) {
            if (p[i] > maxLen) {
                maxLen = p[i];
                centerIndex = i;
            }
        }

        int start = (centerIndex - maxLen) / 2;
        return s.substr(start, maxLen);
    }
};
```

### **Algorithm Explanation:**

1. **Preprocessing (Lines 3-11)**:
   - Transform string by inserting `#` between characters
   - Add sentinels `^` at start and `$` at end
   - Example: `"aba"` → `"^#a#b#a#$"`
   - **Why?** This converts all palindromes to odd-length, simplifying the algorithm

2. **Main Algorithm (Lines 17-33)**:
   - `p[i]`: Length of palindrome centered at position `i` in transformed string
   - `center`: Center of the rightmost palindrome found so far
   - `right`: Right boundary of the palindrome centered at `center`
   - **For each position `i`**:
     - **Mirror symmetry**: If `i` is within current palindrome, use mirror position to initialize `p[i]`
     - **Expand**: Try to expand palindrome centered at `i`
     - **Update**: If palindrome extends beyond `right`, update `center` and `right`

3. **Find Longest (Lines 35-42)**:
   - Find the maximum value in `p` array
   - Convert back to original string indices

### **Key Insight: Mirror Symmetry**

If we know a palindrome centered at `center` extends to `right`, and `i` is within this palindrome, then:
- The palindrome centered at `i` will be at least as long as the palindrome at its mirror position `mirror = 2*center - i`
- This avoids redundant checks, making it O(n)

### **Example Walkthrough:**

**For `s = "babad"`:**

```
Step 1: Preprocess
t = "^#b#a#b#a#d#$"

Step 2: Build p array
i=1: p[1]=0, center=1, right=1
i=2: p[2]=1 (palindrome "#b#"), center=2, right=3
i=3: p[3]=0, center=2, right=3
i=4: p[4]=3 (palindrome "#b#a#b#"), center=4, right=7
i=5: p[5]=0, center=4, right=7
i=6: p[6]=1 (palindrome "#a#b#"), center=6, right=7
i=7: p[7]=0, center=4, right=7
i=8: p[8]=0, center=4, right=7
i=9: p[9]=0, center=4, right=7

Step 3: Find maximum
maxLen = 3, centerIndex = 4
start = (4 - 3) / 2 = 0
Result: s.substr(0, 3) = "bab"
```

### **Complexity Analysis:**

- **Time Complexity:** O(n)
  - Each character is processed at most once
  - The `right` boundary only moves forward
  - Total: O(n)
- **Space Complexity:** O(n)
  - O(n) for transformed string `t`
  - O(n) for `p` array

## Comparison of Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Expand Around Center | O(n²) | O(1) | Simple, intuitive, good for interviews |
| Manacher's Algorithm | O(n) | O(n) | Optimal, but more complex |
| Dynamic Programming | O(n²) | O(n²) | Straightforward but uses more space |

## Key Insights

1. **Two Types of Centers**: Odd-length (single char) and even-length (between chars)
2. **Expand Greedily**: For each center, expand as far as possible
3. **Manacher's Symmetry**: Use previously computed palindromes to avoid redundant checks
4. **Preprocessing**: Transform string to handle even-length palindromes uniformly

## Edge Cases

1. **Single character**: `"a"` → return `"a"`
2. **All same characters**: `"aaa"` → return `"aaa"`
3. **No palindrome > 1**: `"abc"` → return `"a"` (or any single char)
4. **Two palindromes of same length**: `"babad"` → return either `"bab"` or `"aba"`

## Common Mistakes

1. **Missing even-length palindromes**: Forgetting to check centers between characters
2. **Index out of bounds**: Not checking bounds before accessing array
3. **Wrong expansion logic**: Not expanding symmetrically from center
4. **Manacher's preprocessing**: Forgetting to convert back to original indices

## Related Problems

- [LC 647: Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) - Count all palindromic substrings (same expand-around-center technique)
- [LC 516: Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) - Find longest palindromic subsequence (DP)
- [LC 125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) - Check if string is palindrome
- [LC 680: Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) - Can make palindrome with 1 deletion

---

*This problem demonstrates two fundamental approaches to palindrome problems: the intuitive expand-around-center technique and the optimal Manacher's algorithm. The expand-around-center approach is recommended for interviews due to its simplicity and clarity.*

