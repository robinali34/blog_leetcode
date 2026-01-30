---
layout: post
title: "409. Longest Palindrome"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, string, hash-table, greedy]
permalink: /2026/01/19/easy-409-longest-palindrome/
tags: [leetcode, easy, string, hash-table, greedy, bit-manipulation, palindrome]
---

# 409. Longest Palindrome

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Palindrome construction**: What can we construct? (Assumption: Longest palindrome using characters from s - can rearrange characters freely)

2. **Character usage**: Can we use each character only once? (Assumption: Yes - can use each character at most as many times as it appears in s)

3. **Palindrome properties**: What makes a palindrome? (Assumption: Reads same forwards and backwards - symmetric string)

4. **Return value**: What should we return? (Assumption: Integer - length of longest palindrome that can be constructed)

5. **Case sensitivity**: Are 'a' and 'A' different? (Assumption: Yes - per constraints, case matters, lowercase and uppercase are different)

## Solution Approach

This problem asks us to find the longest palindrome we can construct from the given characters. The key insight is:

1. **Even Counts**: Characters with even counts can all be used (pairs on both sides)
2. **Odd Counts**: Characters with odd counts can contribute `count - 1` pairs, plus potentially 1 in the center
3. **Center Character**: At most one character can be placed in the center (if any odd counts exist)

### Key Insights:

1. **Character Frequency**: Track how many times each character appears
2. **Pair Counting**: Count pairs (each pair contributes 2 to length)
3. **Center Placement**: If any character has odd count, we can add 1 more for center
4. **Bit Manipulation**: Use bit masks to efficiently track odd/even counts

### Algorithm:

1. Track character frequencies using bit masks (or hash map)
2. For each character, toggle its bit
3. When bit goes from 1→0, we found a pair → add 2 to result
4. If any bits remain set (odd counts), add 1 for center

## Solution 1: Bit Manipulation (Optimal Space)

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

### Algorithm Explanation:

1. **Two Bit Masks**: 
   - `maskl`: Tracks lowercase letters (a-z) using bits 0-25
   - `maskU`: Tracks uppercase letters (A-Z) using bits 0-25

2. **Character Processing**:
   - For each character, calculate its bit position
   - Toggle the corresponding bit using XOR (`^`)
   - If bit was already set (odd count), we found a pair → add 2

3. **Pair Detection**:
   - When `mask & bit` is true, character appeared odd times before
   - Toggling makes it even → we found a complete pair
   - Add 2 to result (one character on each side)

4. **Final Check**:
   - If any bits remain set (`maskl || maskU`), there's at least one odd count
   - Add 1 for center character placement

### Example Walkthrough:

**Input:** `s = "abccccdd"`

```
Character: 'a' (lowercase)
  bit = 1 << ('a' - 'a') = 1 << 0 = 1
  maskl & bit = 0 (not set) → toggle maskl = 1
  rtn = 0

Character: 'b' (lowercase)
  bit = 1 << ('b' - 'a') = 1 << 1 = 2
  maskl & bit = 0 → toggle maskl = 1 | 2 = 3
  rtn = 0

Character: 'c' (lowercase)
  bit = 1 << ('c' - 'a') = 1 << 2 = 4
  maskl & bit = 0 → toggle maskl = 3 | 4 = 7
  rtn = 0

Character: 'c' (lowercase)
  bit = 4
  maskl & bit = 4 (set!) → found pair!
  rtn = 2, toggle maskl = 3

Character: 'c' (lowercase)
  bit = 4
  maskl & bit = 0 → toggle maskl = 3 | 4 = 7
  rtn = 2

Character: 'c' (lowercase)
  bit = 4
  maskl & bit = 4 (set!) → found pair!
  rtn = 4, toggle maskl = 3

Character: 'd' (lowercase)
  bit = 1 << ('d' - 'a') = 1 << 3 = 8
  maskl & bit = 0 → toggle maskl = 3 | 8 = 11
  rtn = 4

Character: 'd' (lowercase)
  bit = 8
  maskl & bit = 8 (set!) → found pair!
  rtn = 6, toggle maskl = 3

Final: maskl = 3 (bits for 'a' and 'b' are set)
  maskl || maskU = true → add 1
  Return: 6 + 1 = 7 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Single pass through the string
  - Bit operations are O(1)

- **Space Complexity:** O(1)
  - Only two integers for bit masks
  - Constant space regardless of input size

## Solution 2: Hash Map / Frequency Array

```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> count;
        for(char c: s) {
            count[c]++;
        }
        
        int result = 0;
        bool hasOdd = false;
        
        for(auto& [ch, freq]: count) {
            result += (freq / 2) * 2;  // Add pairs
            if(freq % 2 == 1) {
                hasOdd = true;
            }
        }
        
        return hasOdd ? result + 1 : result;
    }
};
```

### Algorithm Explanation:

1. **Count Frequencies**: Use hash map to count each character
2. **Sum Pairs**: For each character, add `(freq / 2) * 2` (largest even number ≤ freq)
3. **Check Odd**: Track if any character has odd frequency
4. **Add Center**: If odd exists, add 1 for center placement

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Count frequencies: O(n)
  - Process counts: O(k) where k = unique characters (≤ 52)

- **Space Complexity:** O(k)
  - Hash map stores at most 52 entries (26 lowercase + 26 uppercase)

## Solution 3: Frequency Array (Optimized)

```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        int count[128] = {};  // ASCII covers all characters
        for(char c: s) {
            count[c]++;
        }
        
        int result = 0;
        bool hasOdd = false;
        
        for(int i = 0; i < 128; i++) {
            result += (count[i] / 2) * 2;
            if(count[i] % 2 == 1) {
                hasOdd = true;
            }
        }
        
        return hasOdd ? result + 1 : result;
    }
};
```

**Pros**: Simple, direct array access  
**Cons**: Uses more space than bit manipulation (128 vs 2 integers)

## Key Insights

1. **Palindrome Structure**: Symmetric pairs + optional center
2. **Pair Counting**: Each pair contributes 2 to length
3. **Odd Handling**: At most one character can be in center
4. **Bit Manipulation**: Efficient way to track odd/even counts
5. **Case Sensitivity**: Must handle uppercase and lowercase separately

## Edge Cases

1. **Single character**: `s = "a"` → return 1
2. **All pairs**: `s = "bb"` → return 2
3. **All same character**: `s = "aaaa"` → return 4
4. **Mixed case**: `s = "Aa"` → return 1 (case sensitive)
5. **No pairs**: `s = "abc"` → return 1 (one character in center)
6. **All unique**: `s = "abcdef"` → return 1

## Common Mistakes

1. **Case sensitivity**: Treating 'A' and 'a' as same
2. **Center placement**: Forgetting to add 1 when odd counts exist
3. **Pair counting**: Incorrectly counting pairs
4. **Bit manipulation**: Off-by-one errors in bit shifting
5. **Empty string**: Not handling edge case (but constraints guarantee length ≥ 1)

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Bit Manipulation** | O(n) | O(1) | Optimal space, elegant | Slightly complex logic |
| **Hash Map** | O(n) | O(k) | Simple, readable | More memory overhead |
| **Frequency Array** | O(n) | O(1)* | Simple, fast access | Fixed size array |

*O(1) in terms of input size, but uses 128 integers

## When to Use Each Approach

- **Bit Manipulation**: When space optimization is critical, or for interview demonstration
- **Hash Map**: When readability is priority, or when character set is unknown
- **Frequency Array**: When character set is bounded and known (like ASCII)

## Related Problems

- [LC 5: Longest Palindromic Substring](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-5-longest-palindromic-substring/) - Find longest palindrome substring
- [LC 125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) - Check if string is palindrome
- [LC 131: Palindrome Partitioning](https://robinali34.github.io/blog_leetcode/2025/09/30/medium-131-palindrome-partitioning/) - Partition into palindromes
- [LC 647: Palindromic Substrings](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-647-palindromic-substrings/) - Count palindromic substrings
- [LC 1177: Can Make Palindrome from Substring](https://robinali34.github.io/blog_leetcode/2026/01/01/medium-1177-can-make-palindrome-from-substring/) - Check if substring can form palindrome
- [LC 1400: Construct K Palindrome Strings](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-1400-construct-k-palindrome-strings/) - Construct multiple palindromes

---

*This problem demonstrates **efficient character frequency tracking** using **bit manipulation**. The key insight is that palindromes consist of pairs plus an optional center character, making frequency counting the core of the solution.*

