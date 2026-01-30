---
layout: post
title: "[Medium] 647. Palindromic Substrings"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp string two-pointers problem-solving
permalink: /posts/2025-11-24-medium-647-palindromic-substrings/
tags: [leetcode, medium, string, two-pointers, palindrome, expand-around-center]
---

# [Medium] 647. Palindromic Substrings

Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

## Examples

**Example 1:**
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

**Example 3:**
```
Input: s = "racecar"
Output: 10
Explanation: 
Palindromic substrings: "r", "a", "c", "e", "c", "a", "r", "ceec", "aceca", "racecar"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Substring definition**: Does substring need to be contiguous? (Assumption: Yes - substring is contiguous by definition)

2. **Palindrome definition**: What makes a substring a palindrome? (Assumption: Reads same forwards and backwards - symmetric string)

3. **Return value**: Should we return substrings or count? (Assumption: Return count - integer representing number of palindromic substrings)

4. **Single characters**: Do single characters count? (Assumption: Yes - single character is a palindrome)

5. **Duplicate substrings**: Should we count duplicate palindromes? (Assumption: Yes - if "aa" appears twice, count both occurrences)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to count palindromic substrings. Let me check all possible substrings."

**Naive Solution**: Check all possible substrings, for each check if it's palindrome, count valid ones.

**Complexity**: O(n³) time, O(1) space

**Issues**:
- O(n³) time - very inefficient
- Repeats palindrome checking for overlapping substrings
- Doesn't leverage palindrome properties
- Can be optimized

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use DP to check palindromes efficiently, or expand around centers."

**Improved Solution**: Use DP table to check palindromes. dp[i][j] = true if s[i..j] is palindrome. Fill table and count true values.

**Complexity**: O(n²) time, O(n²) space

**Improvements**:
- DP eliminates redundant palindrome checks
- O(n²) time is much better
- Handles all cases correctly
- Can optimize space

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "Expand around centers is more space-efficient than DP."

**Best Solution**: Expand around centers. For each center (character or between characters), expand outward while palindromic. Count all palindromes found.

**Complexity**: O(n²) time, O(1) space

**Key Realizations**:
1. Expand around centers is elegant approach
2. O(n²) time is optimal - must check all centers
3. O(1) space is optimal
4. Handles odd and even length palindromes

## Solution: Expand Around Centers

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

The key insight is that every palindrome expands from a center. For each position in the string, we can have:
1. **Odd-length palindromes**: Center at a single character (e.g., "aba" centered at 'b')
2. **Even-length palindromes**: Center between two characters (e.g., "abba" centered between two 'b's)

We iterate through each position and expand outward from both possible centers, counting all palindromic substrings found.

### Solution: Expand Around Centers

```cpp
class Solution {
private:
    int countPalindromesAroundCenter(const string& s, int low, int high) {
        int count = 0;
        while (low >= 0 && high < (int)s.size()) {
            if (s[low] != s[high]) break;
            low--;
            high++;
            count++;
        }
        return count;
    }

public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            // Count odd-length palindromes (center at i)
            count += countPalindromesAroundCenter(s, i, i);
            // Count even-length palindromes (center between i and i+1)
            count += countPalindromesAroundCenter(s, i, i + 1);
        }
        return count;
    }
};
```

## How the Algorithm Works

### Key Insight: Two Types of Centers

1. **Odd-length palindromes**: Center at index `i`
   - Example: "aba" with center at index 1 ('b')
   - Expand: `i-1` and `i+1`, then `i-2` and `i+2`, etc.

2. **Even-length palindromes**: Center between indices `i` and `i+1`
   - Example: "abba" with center between indices 1 and 2
   - Expand: `i` and `i+1`, then `i-1` and `i+2`, etc.

### Step-by-Step Example: `s = "abc"`

```
i = 0: 'a'
  Odd:  center at 0 → expand (0,0) → "a" ✓ count = 1
  Even: center between 0,1 → expand (0,1) → 'a' != 'b' ✗ count = 0
  Total: 1

i = 1: 'b'
  Odd:  center at 1 → expand (1,1) → "b" ✓ count = 1
  Even: center between 1,2 → expand (1,2) → 'b' != 'c' ✗ count = 0
  Total: 1

i = 2: 'c'
  Odd:  center at 2 → expand (2,2) → "c" ✓ count = 1
  Even: center between 2,3 → expand (2,3) → out of bounds ✗ count = 0
  Total: 1

Final count: 1 + 1 + 1 = 3
```

### Step-by-Step Example: `s = "aaa"`

```
i = 0: 'a'
  Odd:  center at 0 → expand (0,0) → "a" ✓
        expand (-1,1) → out of bounds
        count = 1
  Even: center between 0,1 → expand (0,1) → "aa" ✓
        expand (-1,2) → out of bounds
        count = 1
  Total: 2

i = 1: 'a'
  Odd:  center at 1 → expand (1,1) → "a" ✓
        expand (0,2) → "aaa" ✓
        expand (-1,3) → out of bounds
        count = 2
  Even: center between 1,2 → expand (1,2) → "aa" ✓
        expand (0,3) → out of bounds
        count = 1
  Total: 3

i = 2: 'a'
  Odd:  center at 2 → expand (2,2) → "a" ✓
        expand (1,3) → out of bounds
        count = 1
  Even: center between 2,3 → expand (2,3) → out of bounds
        count = 0
  Total: 1

Final count: 2 + 3 + 1 = 6
```

## Algorithm Breakdown

### Helper Function: `countPalindromesAroundCenter`

```cpp
int countPalindromesAroundCenter(const string& s, int low, int high) {
    int count = 0;
    while (low >= 0 && high < (int)s.size()) {
        if (s[low] != s[high]) break;
        low--;
        high++;
        count++;
    }
    return count;
}
```

**How it works:**
1. Start with `low` and `high` as the center (or centers for even-length)
2. Expand outward while characters match
3. Count each valid palindrome found
4. Stop when characters don't match or indices go out of bounds

**Why it works:**
- Each expansion creates a new palindromic substring
- We count all palindromes that can be formed from this center
- The function handles both odd and even-length palindromes based on initial `low` and `high`

### Main Function: `countSubstrings`

```cpp
int countSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        count += countPalindromesAroundCenter(s, i, i);      // Odd-length
        count += countPalindromesAroundCenter(s, i, i + 1); // Even-length
    }
    return count;
}
```

**How it works:**
1. For each position `i`, check both possible centers
2. Sum all palindromic substrings found
3. Return total count

## Complexity Analysis

**Time Complexity:** O(n²)
- We iterate through each position: O(n)
- For each position, we expand outward: O(n) in worst case
- Total: O(n²)

**Space Complexity:** O(1)
- Only using a few variables
- No extra data structures

## Alternative Approaches

### Approach 2: Dynamic Programming

**Time Complexity:** O(n²)  
**Space Complexity:** O(n²)

Use DP table `dp[i][j]` to track if substring `s[i..j]` is a palindrome.

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int count = 0;
        
        // Every single character is a palindrome
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }
        
        // Check for palindromes of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }
        
        // Check for palindromes of length >= 3
        for (int len = 3; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    count++;
                }
            }
        }
        
        return count;
    }
};
```

**Pros:**
- More intuitive for some
- Can be extended to find longest palindromic substring

**Cons:**
- Uses O(n²) space
- More complex implementation

### Approach 3: Manacher's Algorithm

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Advanced algorithm that finds all palindromes in linear time. More complex but optimal.

## Key Insights

1. **Two types of centers**: Every palindrome has either a single-character center (odd-length) or a two-character center (even-length)

2. **Expand outward**: For each center, expand while characters match

3. **Count incrementally**: Each successful expansion creates a new palindromic substring

4. **No overlap**: Each center is checked independently, so we count all palindromes exactly once

## Edge Cases

1. **Single character**: Returns 1 (the character itself is a palindrome)
2. **All same characters**: Returns n(n+1)/2 (all substrings are palindromes)
3. **No palindromes longer than 1**: Returns n (only single characters are palindromes)

## Common Mistakes

1. **Missing even-length palindromes**: Forgetting to check centers between characters
2. **Double counting**: Not properly handling boundaries
3. **Index out of bounds**: Not checking bounds before accessing array
4. **Wrong expansion logic**: Not expanding symmetrically from center

## Optimization Tips

1. **Early termination**: Can stop early if no more palindromes possible (not applicable here)
2. **Use expand-around-center**: More space-efficient than DP
3. **Cache results**: Not needed for this problem, but useful for related problems

## Related Problems

- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) - Find the longest palindrome (can use same technique) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-5-longest-palindromic-substring/)
- [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) - Find longest palindromic subsequence (DP)
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) - Check if string is palindrome
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) - Check if string can be palindrome after deleting at most one character

## Pattern Recognition

This problem demonstrates the **"Expand Around Centers"** pattern:

```
1. Identify possible centers (single char or between chars)
2. For each center, expand outward symmetrically
3. Count valid expansions
```

Similar problems:
- Longest palindromic substring
- Palindrome partitioning
- Palindrome-related string problems

## Real-World Applications

1. **String Analysis**: Finding palindromic patterns in DNA sequences
2. **Text Processing**: Detecting palindromic words or phrases
3. **Algorithm Design**: Understanding palindrome detection techniques
4. **Interview Preparation**: Common pattern in coding interviews

---

*This problem demonstrates the expand-around-centers technique, which is efficient for palindrome-related problems. The key is recognizing that every palindrome has a center and can be found by expanding outward from that center.*

