---
layout: post
title: "686. Repeated String Match"
date: 2025-12-30 14:30:00 -0700
categories: [leetcode, medium, string-matching, kmp, rabin-karp, rolling-hash]
permalink: /2025/12/30/medium-686-repeated-string-match/
---

# 686. Repeated String Match

## Problem Statement

Given two strings `a` and `b`, return the minimum number of times you should repeat string `a` so that string `b` is a substring of it. If it is impossible for `b` to be a substring of `a` after repeating it, return `-1`.

**Notice:** String `"abc"` repeated 0 times is `""`, repeated 1 time is `"abc"`, and repeated 2 times is `"abcabc"`.

## Examples

**Example 1:**
```
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
```

**Example 2:**
```
Input: a = "a", b = "aa"
Output: 2
```

**Example 3:**
```
Input: a = "a", b = "a"
Output: 1
```

**Example 4:**
```
Input: a = "abc", b = "wxyz"
Output: -1
```

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist of lowercase English letters.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Repetition definition**: What does "repeated string match" mean? (Assumption: Repeat string 'a' multiple times until 'b' becomes a substring of the repeated string)

2. **Minimum repetitions**: What are we trying to find? (Assumption: Minimum number of times to repeat 'a' so that 'b' is a substring)

3. **Substring matching**: Does 'b' need to be an exact substring? (Assumption: Yes - 'b' must appear as a contiguous substring in the repeated 'a')

4. **No match**: What should we return if 'b' can never be a substring? (Assumption: Return -1 - impossible to form 'b' as substring)

5. **Case sensitivity**: Are character comparisons case-sensitive? (Assumption: Based on constraints, only lowercase letters, so case doesn't matter)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to find minimum repetitions. Let me try repeating string a and checking if b is substring."

**Naive Solution**: Repeat string a multiple times, check if b is substring using simple string matching. Try repetitions from 1 to some upper bound.

**Complexity**: O(n × m) per repetition check, where n = len(a), m = len(b)

**Issues**:
- Simple substring matching is inefficient
- May need many repetitions
- Doesn't leverage string matching algorithms
- Timeout for large strings

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use KMP algorithm for efficient substring matching, or optimize repetition checking."

**Improved Solution**: Use KMP algorithm for substring matching. Repeat a until length >= b, then check if b is substring. Can also use Rabin-Karp for alternative.

**Complexity**: O(n + m) per check with KMP, but need multiple repetitions

**Improvements**:
- KMP makes substring matching efficient
- Still need to determine upper bound for repetitions
- Much faster than naive matching

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "I can determine upper bound: need at most ceil(m/n) + 1 repetitions. Use KMP for matching."

**Best Solution**: Calculate upper bound: need at most ceil(len(b)/len(a)) + 1 repetitions. Use KMP algorithm for efficient substring matching. Can also use Rabin-Karp as alternative.

**Complexity**: O(n + m) time with KMP, O(n + m) space

**Key Realizations**:
1. Upper bound is ceil(m/n) + 1 repetitions
2. KMP algorithm is optimal for substring matching
3. O(n + m) time is optimal for string matching
4. Rabin-Karp is alternative with similar complexity

## Solution Approach

This problem requires finding the minimum number of repetitions of string `a` such that string `b` becomes a substring. This is a **string matching problem** that can be efficiently solved using advanced algorithms like **Knuth-Morris-Pratt (KMP)** or **Rabin-Karp**.

### Key Insights:

1. **Minimum Repetitions**: Need at least `⌈b.length / a.length⌉` repetitions
2. **Maximum Repetitions**: At most `⌈b.length / a.length⌉ + 1` repetitions needed
3. **Circular Matching**: Since `a` is repeated, we can use circular string matching
4. **Efficient Algorithms**: KMP or Rabin-Karp provide O(n + m) time complexity

### Algorithm Options:

1. **KMP Algorithm**: Preprocess pattern to avoid backtracking
2. **Rabin-Karp**: Use rolling hash for efficient substring matching
3. **Naive Approach**: O(n × m) - check each position

## String Matching Algorithms

### **Knuth-Morris-Pratt (KMP) Algorithm**

KMP is an efficient string-searching algorithm that preprocesses the pattern to create a **prefix function** (also called LPS - Longest Proper Prefix which is also a Suffix). This allows skipping unnecessary comparisons.

#### **Key Concepts:**

1. **Prefix Function (π/LPS)**: For each position `i` in pattern, `π[i]` is the length of the longest proper prefix that is also a suffix of `pattern[0..i]`
2. **No Backtracking**: When a mismatch occurs, we don't reset to the beginning but use the prefix function to determine the next position
3. **Time Complexity**: O(n + m) where n = text length, m = pattern length

#### **How KMP Works:**

1. **Preprocessing Phase**: Build prefix function for pattern
   - For each position, find longest prefix-suffix match
   - Use previous values to compute current value efficiently

2. **Search Phase**: Match pattern in text
   - Compare characters from left to right
   - On mismatch, use prefix function to skip ahead
   - Never backtrack in text

#### **Prefix Function Example:**

For pattern `"ababaca"`:
```
Pattern:  a  b  a  b  a  c  a
Index:     0  1  2  3  4  5  6
π[i]:     0  0  1  2  3  0  1

Explanation:
- π[0] = 0 (no proper prefix)
- π[1] = 0 ("ab" has no prefix-suffix match)
- π[2] = 1 ("aba" has "a" as prefix-suffix)
- π[3] = 2 ("abab" has "ab" as prefix-suffix)
- π[4] = 3 ("ababa" has "aba" as prefix-suffix)
- π[5] = 0 ("ababac" has no prefix-suffix match)
- π[6] = 1 ("ababaca" has "a" as prefix-suffix)
```

### **Rabin-Karp Algorithm**

Rabin-Karp uses **rolling hash** to efficiently compute hash values for substrings. It compares hash values first, then verifies with character-by-character comparison if hashes match.

#### **Key Concepts:**

1. **Rolling Hash**: Compute hash of substring in O(1) time using previous hash
2. **Hash Function**: Use polynomial rolling hash: `hash = (hash * base + char) % mod`
3. **Collision Handling**: When hashes match, verify with actual string comparison
4. **Time Complexity**: Average O(n + m), worst case O(n × m) if many hash collisions

#### **How Rabin-Karp Works:**

1. **Precompute Pattern Hash**: Calculate hash of pattern string
2. **Rolling Hash in Text**: 
   - Compute hash of first window
   - Slide window and update hash in O(1)
   - Compare hashes, verify if match
3. **Base and Modulo**: Use large base and prime modulo to reduce collisions

#### **Rolling Hash Formula:**

```
For substring s[i..i+m-1]:
hash = (s[i] * base^(m-1) + s[i+1] * base^(m-2) + ... + s[i+m-1]) % mod

To slide window from i to i+1:
new_hash = ((old_hash - s[i] * base^(m-1)) * base + s[i+m]) % mod
```

## Solution 1: KMP Algorithm (Recommended)

### **Solution: KMP with Circular String Matching**

```cpp
class Solution {
private:
    int strStr(string &haystack, string &needle) {
        const int n = haystack.size(), m = needle.size();
        if(m == 0) return 0;
        vector<int> pi(m);
        for(int i = 1, j = 0; i < m; i++) {
            while(j > 0 && needle[i] != needle[j]) {
                j = pi[j - 1];
            }
            if(needle[i] == needle[j]) {
                j++;
            }
            pi[i] = j;
        }
        for(int i = 0, j = 0; i - j < n; i++) {
            while(j > 0 && haystack[i % n] != needle[j]) {
                j = pi[j - 1];
            }
            if(haystack[i % n] == needle[j]) {
                j++;
            }
            if(j == m) {
                return i - m + 1;
            }
        }
        return -1;
    }
public:
    int repeatedStringMatch(string a, string b) {
        const int an = a.size(), bn = b.size();
        int idx = strStr(a, b);
        if(idx == -1) return -1;
        if(an - idx >= bn) {
            return 1;
        }
        return (bn + idx - an - 1) / an + 2;
    }
};
```

### **Algorithm Explanation:**

1. **Prefix Function Construction (Lines 7-15)**:
   - Build `pi` array for pattern `needle`
   - `pi[i]` = length of longest prefix-suffix for `needle[0..i]`
   - Use previous values to compute efficiently

2. **KMP Search with Circular Matching (Lines 16-28)**:
   - Search for `needle` in circular `haystack`
   - Use `i % n` to handle circular indexing
   - On mismatch: `j = pi[j - 1]` (skip using prefix function)
   - On match: increment `j`
   - When `j == m`: pattern found at position `i - m + 1`

3. **Calculate Minimum Repetitions (Lines 30-38)**:
   - If pattern found at `idx`:
     - If remaining characters in first repetition ≥ `bn`: return 1
     - Otherwise: calculate repetitions needed
     - Formula: `(bn + idx - an - 1) / an + 2`

### **Example Walkthrough:**

**For `a = "abcd", b = "cdabcdab"`:**

```
Step 1: Build prefix function for "cdabcdab"
Pattern: c  d  a  b  c  d  a  b
π[i]:    0  0  0  0  1  2  3  4

Step 2: KMP search in circular "abcd"
Text (circular): a b c d a b c d a b c d ...
Pattern:         c d a b c d a b

i=0: 'a' vs 'c' → mismatch, j=0
i=1: 'b' vs 'c' → mismatch, j=0
i=2: 'c' vs 'c' → match, j=1
i=3: 'd' vs 'd' → match, j=2
i=4: 'a' vs 'a' → match, j=3
i=5: 'b' vs 'b' → match, j=4
i=6: 'c' vs 'c' → match, j=5
i=7: 'd' vs 'd' → match, j=6
i=8: 'a' vs 'a' → match, j=7
i=9: 'b' vs 'b' → match, j=8 → FOUND!

idx = 9 - 8 + 1 = 2
an = 4, bn = 8
an - idx = 4 - 2 = 2 < 8
repetitions = (8 + 2 - 4 - 1) / 4 + 2 = 5/4 + 2 = 1 + 2 = 3
```

## Solution 2: Rabin-Karp Algorithm

### **Solution: Rabin-Karp with Rolling Hash**

```cpp
class Solution {
private:
    const long long BASE = 256;
    const long long MOD = 1e9 + 7;
    
    long long computeHash(const string& s, int start, int len) {
        long long hash = 0;
        for(int i = 0; i < len; i++) {
            hash = (hash * BASE + s[start + i]) % MOD;
        }
        return hash;
    }
    
    long long updateHash(long long oldHash, char remove, char add, long long power) {
        oldHash = (oldHash - (remove * power) % MOD + MOD) % MOD;
        oldHash = (oldHash * BASE + add) % MOD;
        return oldHash;
    }
    
    bool verifyMatch(const string& text, int start, const string& pattern) {
        for(int i = 0; i < pattern.size(); i++) {
            if(text[start + i] != pattern[i]) return false;
        }
        return true;
    }
    
    int rabinKarpSearch(const string& text, const string& pattern, bool circular) {
        int n = text.size(), m = pattern.size();
        if(m == 0) return 0;
        if(n < m) return -1;
        
        // Compute pattern hash
        long long patternHash = computeHash(pattern, 0, m);
        
        // Compute power for rolling hash
        long long power = 1;
        for(int i = 0; i < m - 1; i++) {
            power = (power * BASE) % MOD;
        }
        
        // Compute initial window hash
        long long textHash = computeHash(text, 0, m);
        
        // Check first window
        if(textHash == patternHash && verifyMatch(text, 0, pattern)) {
            return 0;
        }
        
        // Rolling hash
        int maxIterations = circular ? n + m - 1 : n - m + 1;
        for(int i = 1; i < maxIterations; i++) {
            int removeIdx = (i - 1) % n;
            int addIdx = (i + m - 1) % n;
            
            textHash = updateHash(textHash, text[removeIdx], text[addIdx], power);
            
            if(textHash == patternHash) {
                int start = i % n;
                if(verifyMatch(text, start, pattern)) {
                    return i;
                }
            }
        }
        
        return -1;
    }
    
public:
    int repeatedStringMatch(string a, string b) {
        int an = a.size(), bn = b.size();
        
        // Try circular search
        int idx = rabinKarpSearch(a, b, true);
        if(idx == -1) return -1;
        
        if(an - idx >= bn) {
            return 1;
        }
        return (bn + idx - an - 1) / an + 2;
    }
};
```

### **Algorithm Explanation:**

1. **Hash Computation (Lines 6-11)**:
   - Compute hash for substring using polynomial rolling hash
   - Formula: `hash = (hash * BASE + char) % MOD`

2. **Rolling Hash Update (Lines 13-17)**:
   - Remove leftmost character: subtract `remove * power`
   - Add rightmost character: multiply by BASE and add
   - Handle modulo arithmetic correctly

3. **Verification (Lines 19-24)**:
   - When hashes match, verify with character-by-character comparison
   - Prevents false positives from hash collisions

4. **Rabin-Karp Search (Lines 26-58)**:
   - Precompute pattern hash and power value
   - Slide window and update hash in O(1)
   - Check hash matches, verify if needed
   - Support circular string matching

## KMP Template

Here's the general template for KMP algorithm:

```cpp
class KMP {
private:
    // Build prefix function (LPS array)
    vector<int> buildPrefixFunction(const string& pattern) {
        int m = pattern.size();
        vector<int> pi(m, 0);
        
        for(int i = 1, j = 0; i < m; i++) {
            // Mismatch: backtrack using prefix function
            while(j > 0 && pattern[i] != pattern[j]) {
                j = pi[j - 1];
            }
            // Match: extend prefix
            if(pattern[i] == pattern[j]) {
                j++;
            }
            pi[i] = j;
        }
        return pi;
    }
    
public:
    // Search for pattern in text
    int search(const string& text, const string& pattern) {
        int n = text.size(), m = pattern.size();
        if(m == 0) return 0;
        
        vector<int> pi = buildPrefixFunction(pattern);
        
        for(int i = 0, j = 0; i < n; i++) {
            // Mismatch: use prefix function to skip
            while(j > 0 && text[i] != pattern[j]) {
                j = pi[j - 1];
            }
            // Match: advance both pointers
            if(text[i] == pattern[j]) {
                j++;
            }
            // Pattern found
            if(j == m) {
                return i - m + 1; // Return starting index
            }
        }
        return -1; // Not found
    }
};
```

### **Key Template Components:**

1. **Prefix Function (π/LPS)**:
   - `pi[i]` = longest prefix-suffix length for `pattern[0..i]`
   - Built in O(m) time

2. **Search Algorithm**:
   - No backtracking in text
   - Use prefix function to skip on mismatch
   - Time complexity: O(n + m)

3. **Circular Matching**:
   - Use `i % n` for circular text
   - Adjust loop condition: `i - j < n`

## Rabin-Karp Template

Here's the general template for Rabin-Karp algorithm:

```cpp
class RabinKarp {
private:
    const long long BASE = 256;
    const long long MOD = 1e9 + 7;
    
    long long computeHash(const string& s, int start, int len) {
        long long hash = 0;
        for(int i = 0; i < len; i++) {
            hash = (hash * BASE + s[start + i]) % MOD;
        }
        return hash;
    }
    
    long long updateHash(long long oldHash, char remove, char add, long long power) {
        oldHash = (oldHash - (remove * power) % MOD + MOD) % MOD;
        oldHash = (oldHash * BASE + add) % MOD;
        return oldHash;
    }
    
public:
    int search(const string& text, const string& pattern) {
        int n = text.size(), m = pattern.size();
        if(m == 0) return 0;
        if(n < m) return -1;
        
        // Precompute pattern hash
        long long patternHash = computeHash(pattern, 0, m);
        
        // Precompute BASE^(m-1) for rolling hash
        long long power = 1;
        for(int i = 0; i < m - 1; i++) {
            power = (power * BASE) % MOD;
        }
        
        // Initial window hash
        long long textHash = computeHash(text, 0, m);
        
        // Check first window
        if(textHash == patternHash) {
            if(text.substr(0, m) == pattern) return 0;
        }
        
        // Rolling hash: slide window
        for(int i = 1; i <= n - m; i++) {
            textHash = updateHash(textHash, text[i-1], text[i+m-1], power);
            
            if(textHash == patternHash) {
                if(text.substr(i, m) == pattern) return i;
            }
        }
        
        return -1;
    }
};
```

### **Key Template Components:**

1. **Hash Function**:
   - Polynomial rolling hash: `hash = (hash * BASE + char) % MOD`
   - BASE = 256 (for ASCII), MOD = large prime

2. **Rolling Hash**:
   - Update hash in O(1) when sliding window
   - Remove left char, add right char

3. **Collision Handling**:
   - Always verify hash matches with actual string comparison
   - Prevents false positives

## Complexity Analysis

### **Solution 1: KMP**

**Time Complexity:** O(n + m)
- **Prefix function**: O(m) - build LPS array
- **Search phase**: O(n) - each character visited at most twice
- **Total**: O(n + m) where n = a.length, m = b.length

**Space Complexity:** O(m)
- **Prefix function array**: O(m)
- **Total**: O(m)

### **Solution 2: Rabin-Karp**

**Time Complexity:** O(n + m) average, O(n × m) worst case
- **Hash computation**: O(m) for pattern
- **Rolling hash**: O(n) for text (O(1) per window)
- **Verification**: O(m) per hash match (rare collisions)
- **Total**: O(n + m) average, O(n × m) worst case with many collisions

**Space Complexity:** O(1)
- **Hash variables**: O(1)
- **Total**: O(1) excluding input strings

## Key Points

1. **KMP is Optimal**: Guaranteed O(n + m) time, no worst-case degradation
2. **Rabin-Karp**: Average O(n + m), but can degrade with hash collisions
3. **Circular Matching**: Use modulo arithmetic for repeated strings
4. **Minimum Repetitions**: At least `⌈b.length / a.length⌉`, at most `⌈b.length / a.length⌉ + 1`
5. **Prefix Function**: Key to KMP's efficiency - avoids backtracking
6. **Rolling Hash**: Key to Rabin-Karp's efficiency - O(1) hash updates

## Comparison: KMP vs Rabin-Karp

| Aspect | KMP | Rabin-Karp |
|--------|-----|------------|
| **Time Complexity** | O(n + m) guaranteed | O(n + m) average, O(n × m) worst |
| **Space Complexity** | O(m) | O(1) |
| **Preprocessing** | O(m) for prefix function | O(m) for pattern hash |
| **Backtracking** | None (no text backtracking) | None (sliding window) |
| **Collision Handling** | Not needed | Required (verify matches) |
| **Implementation** | More complex | Simpler |
| **Recommended** | ✅ Yes (guaranteed performance) | ⚠️ Good for average case |

## Alternative Approaches

### **Approach 1: KMP (Current Solution 1)**
- **Time**: O(n + m)
- **Space**: O(m)
- **Best for**: Guaranteed performance, no worst-case degradation

### **Approach 2: Rabin-Karp (Current Solution 2)**
- **Time**: O(n + m) average
- **Space**: O(1)
- **Use case**: When space is limited, average case is acceptable

### **Approach 3: Naive String Matching**
- **Time**: O(n × m)
- **Space**: O(1)
- **Use case**: Simple but inefficient for large inputs

## Related Problems

- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) - KMP application
- [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) - KMP for palindrome
- [1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) - Prefix function
- [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) - Rolling hash

## Tags

`String Matching`, `KMP`, `Knuth-Morris-Pratt`, `Rabin-Karp`, `Rolling Hash`, `Prefix Function`, `Medium`

