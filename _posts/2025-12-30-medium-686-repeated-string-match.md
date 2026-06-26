---
layout: post
title: "[Medium] 686. Repeated String Match"
date: 2025-12-30 14:30:00 -0700
categories: [leetcode, medium, string-matching, kmp, rabin-karp, rolling-hash]
permalink: /2025/12/30/medium-686-repeated-string-match/
---
Given two strings `a` and `b`, return the minimum number of times you should repeat string `a` so that string `b` is a substring of it. If it is impossible for `b` to be a substring of `a` after repeating it, return `-1`.

**Notice:** String `"abc"` repeated 0 times is `""`, repeated 1 time is `"abc"`, and repeated 2 times is `"abcabc"`.

## Thinking Process

Given two strings `a` and `b`, return the minimum number of times you should repeat string `a` so that string `b` is a substring of it. If it is impossible for `b` to be a substring of `a` after repeating it, return `-1`.

**Notice:** String `"abc"` repeated 0 times is `""`, repeated 1 time is `"abc"`, and repeated 2 times is `"abcabc"`.

- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute force** *(this problem)* | Often O(n^2) or O(2^n) | O(n) | Baseline; clarifies the optimization target |
| Sort + scan | O(n log n) | O(1) | Pairs, intervals, greedy ordering |
| Hash map / set | O(n) | O(n) | Frequency, membership, two-sum style |
| Single-pass linear | O(n) | O(1) | Two pointers, sliding window, Kadane |

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

### Complexity
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

## Key Takeaways

- Notice:** String `"abc"` repeated 0 times is `""`, repeated 1 time is `"abc"`, and repeated 2 times is `"abcabc"`.
- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.

## References

- [LC 686: Repeated String Match on LeetCode](https://www.leetcode.com/problems/repeated-string-match/)
- [LeetCode Discuss — LC 686: Repeated String Match](https://www.leetcode.com/problems/repeated-string-match/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/repeated-string-match/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [28. Find the Index of the First Occurrence in a String](https://www.leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) - KMP application
- [214. Shortest Palindrome](https://www.leetcode.com/problems/shortest-palindrome/) - KMP for palindrome
- [1392. Longest Happy Prefix](https://www.leetcode.com/problems/longest-happy-prefix/) - Prefix function
- [187. Repeated DNA Sequences](https://www.leetcode.com/problems/repeated-dna-sequences/) - Rolling hash

## Tags

`String Matching`, `KMP`, `Knuth-Morris-Pratt`, `Rabin-Karp`, `Rolling Hash`, `Prefix Function`, `Medium`
