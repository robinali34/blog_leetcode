---
layout: post
title: "1400. Construct K Palindrome Strings"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, medium, string, greedy, hash-table]
permalink: /2026/01/04/medium-1400-construct-k-palindrome-strings/
---

# 1400. Construct K Palindrome Strings

## Problem Statement

Given a string `s` and an integer `k`, return `true` *if you can use all the characters in `s` to construct `k` palindrome strings or `false` otherwise*.

## Examples

**Example 1:**
```
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", etc.
```

**Example 2:**
```
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
```

**Example 3:**
```
Input: s = "true", k = 4
Output: true
Explanation: All the characters in s can be used to construct 4 palindromes: "t", "r", "u", "e".
```

## Constraints

- `1 <= s.length <= 10^5`
- `1 <= k <= 10^5`
- `s` consists of lowercase English letters.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Palindrome construction**: What does "construct k palindromes" mean? (Assumption: Split string s into k non-empty palindromic substrings)

2. **Character usage**: Can we use each character only once? (Assumption: Yes - must use all characters from s exactly once)

3. **Palindrome requirement**: What makes a substring a palindrome? (Assumption: Reads same forwards and backwards - symmetric string)

4. **Return value**: What should we return? (Assumption: Boolean - true if can construct k palindromes, false otherwise)

5. **K value**: What is the range of k? (Assumption: Per constraints, 1 <= k <= s.length - can have 1 to s.length palindromes)

## Solution Approach

This is a **greedy algorithm** problem with a key mathematical insight about palindromes. The crucial observation is that a palindrome can have **at most one character with odd frequency** (the center character).

### Key Insights:

1. **Palindrome Property**: Each palindrome can have at most 1 character with odd frequency
2. **Minimum Palindromes**: Need at least as many palindromes as characters with odd frequency
3. **Maximum Palindromes**: Can create at most `n` palindromes (one per character)
4. **Feasibility Check**: Can construct `k` palindromes if `min_palindromes <= k <= max_palindromes`

### Algorithm:

1. **Count Frequencies**: Count occurrence of each character in `s`
2. **Count Odd Frequencies**: Count how many characters have odd frequency
3. **Determine Bounds**:
   - **Minimum**: `max(odd_count, 1)` - need at least one palindrome, and at least as many as odd-frequency characters
   - **Maximum**: `n` - can create one palindrome per character
4. **Check Feasibility**: Return `true` if `min <= k <= max`

## Solution

### **Solution: Greedy with Frequency Counting**

```cpp
class Solution {
public:
    bool canConstruct(string s, int k) {
        int right = s.length();
        int occ[26] = {0};
        for(char ch: s) {
            occ[ch - 'a']++;
        }
        int left = 0;
        for(int i = 0; i < 26; i++) {
            if(occ[i] % 2 == 1) {
                left++;
            }
        }
        left = max(left, 1);
        return left <= k && k <= right;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Line 4)**:
   - `right`: Maximum number of palindromes = string length `n`
   - Each character can be its own palindrome

2. **Count Character Frequencies (Lines 5-8)**:
   - **Initialize array**: `occ[26]` to count occurrences of each letter
   - **For each character** in `s`:
     - Increment count for that character: `occ[ch - 'a']++`

3. **Count Odd Frequencies (Lines 9-13)**:
   - **Initialize**: `left = 0` (minimum number of palindromes needed)
   - **For each character**:
     - **If frequency is odd**: `occ[i] % 2 == 1`
       - Increment `left` (need at least one palindrome for each odd-frequency character)
   - **Why**: Each palindrome can have at most 1 character with odd frequency (the center)
   - **Minimum**: Need at least `left` palindromes to accommodate all odd-frequency characters

4. **Set Minimum Bound (Line 14)**:
   - `left = max(left, 1)`
   - **Why**: Need at least 1 palindrome (even if all frequencies are even)
   - If all frequencies are even, `left = 0`, but we still need at least 1 palindrome

5. **Check Feasibility (Line 15)**:
   - Return `true` if `left <= k <= right`
   - **Meaning**: Can construct `k` palindromes if `k` is between minimum and maximum

### **Why This Works:**

**Key Insight**: A palindrome can have at most 1 character with odd frequency.

**Strategy**:
1. **Count Odd Frequencies**: Characters with odd frequency need to be centers of palindromes
2. **Minimum Palindromes**: Need at least `max(odd_count, 1)` palindromes
   - At least one for each odd-frequency character
   - At least 1 total (even if all even)
3. **Maximum Palindromes**: Can create at most `n` palindromes (one per character)
4. **Feasibility**: If `k` is between min and max, it's possible

**Example Walkthrough:**

**Example 1: `s = "annabelle"`, `k = 2`**

**Count frequencies:**
```
a: 2 (even)
n: 2 (even)
b: 1 (odd)
e: 2 (even)
l: 2 (even)

Odd frequencies: b (1 character)
```

**Execution:**
```
Step 1: Count frequencies
  occ['a'-'a'] = 2
  occ['n'-'a'] = 2
  occ['b'-'a'] = 1
  occ['e'-'a'] = 2
  occ['l'-'a'] = 2

Step 2: Count odd frequencies
  left = 0
  'a': occ[0] % 2 = 0 (even) → skip
  'b': occ[1] % 2 = 1 (odd) → left++ → left = 1
  'e': occ[4] % 2 = 0 (even) → skip
  'l': occ[11] % 2 = 0 (even) → skip
  'n': occ[13] % 2 = 0 (even) → skip

Step 3: Set bounds
  left = max(1, 1) = 1
  right = 9 (length of "annabelle")

Step 4: Check feasibility
  1 <= 2 <= 9 ✓
  Return: true
```

**Example 2: `s = "leetcode"`, `k = 3`**

**Count frequencies:**
```
l: 1 (odd)
e: 3 (odd)
t: 1 (odd)
c: 1 (odd)
o: 1 (odd)
d: 1 (odd)

Odd frequencies: l, e, t, c, o, d (6 characters)
```

**Execution:**
```
Step 1: Count frequencies
  occ['l'-'a'] = 1
  occ['e'-'a'] = 3
  occ['t'-'a'] = 1
  occ['c'-'a'] = 1
  occ['o'-'a'] = 1
  occ['d'-'a'] = 1

Step 2: Count odd frequencies
  left = 0
  'l': occ[11] % 2 = 1 (odd) → left++ → left = 1
  'e': occ[4] % 2 = 1 (odd) → left++ → left = 2
  't': occ[19] % 2 = 1 (odd) → left++ → left = 3
  'c': occ[2] % 2 = 1 (odd) → left++ → left = 4
  'o': occ[14] % 2 = 1 (odd) → left++ → left = 5
  'd': occ[3] % 2 = 1 (odd) → left++ → left = 6

Step 3: Set bounds
  left = max(6, 1) = 6
  right = 8 (length of "leetcode")

Step 4: Check feasibility
  6 <= 3 <= 8 ✗
  Return: false
```

**Example 3: `s = "true"`, `k = 4`**

**Count frequencies:**
```
t: 1 (odd)
r: 1 (odd)
u: 1 (odd)
e: 1 (odd)

Odd frequencies: t, r, u, e (4 characters)
```

**Execution:**
```
Step 1: Count frequencies
  occ['t'-'a'] = 1
  occ['r'-'a'] = 1
  occ['u'-'a'] = 1
  occ['e'-'a'] = 1

Step 2: Count odd frequencies
  left = 0
  't': occ[19] % 2 = 1 (odd) → left++ → left = 1
  'r': occ[17] % 2 = 1 (odd) → left++ → left = 2
  'u': occ[20] % 2 = 1 (odd) → left++ → left = 3
  'e': occ[4] % 2 = 1 (odd) → left++ → left = 4

Step 3: Set bounds
  left = max(4, 1) = 4
  right = 4 (length of "true")

Step 4: Check feasibility
  4 <= 4 <= 4 ✓
  Return: true
```

## Algorithm Breakdown

### **Why Odd Frequencies Matter**

**Palindrome Property**: A palindrome can have at most 1 character with odd frequency (the center).

**Examples**:
- `"aba"`: 'a' appears 2 times (even), 'b' appears 1 time (odd) → valid
- `"abba"`: 'a' appears 2 times (even), 'b' appears 2 times (even) → valid
- `"abcba"`: 'a' appears 2 times (even), 'b' appears 2 times (even), 'c' appears 1 time (odd) → valid
- `"abc"`: 'a', 'b', 'c' each appear 1 time (all odd) → invalid (can't be palindrome)

### **Minimum Number of Palindromes**

**Why `max(odd_count, 1)`?**
- **If `odd_count > 0`**: Need at least `odd_count` palindromes (one center per odd-frequency character)
- **If `odd_count == 0`**: All frequencies are even, but we still need at least 1 palindrome to use all characters

**Example**:
- `s = "aabb"`: All even frequencies → `left = 0`, but `max(0, 1) = 1` (need at least 1 palindrome)
- `s = "aabbc"`: 'c' has odd frequency → `left = 1` (need at least 1 palindrome for 'c')

### **Maximum Number of Palindromes**

**Why `n` (string length)?**
- Each character can be its own palindrome
- Example: `s = "abc"` → can create 3 palindromes: `"a"`, `"b"`, `"c"`

### **Feasibility Check**

**Why `left <= k <= right`?**
- **If `k < left`**: Not enough palindromes to accommodate all odd-frequency characters → impossible
- **If `k > right`**: More palindromes than characters → impossible
- **If `left <= k <= right`**: Can construct `k` palindromes by:
  - Using `left` palindromes for odd-frequency characters (as centers)
  - Distributing remaining characters among palindromes
  - Creating additional single-character palindromes if needed

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the length of `s`
  - Count frequencies: O(n) - single pass through string
  - Count odd frequencies: O(26) = O(1) - constant time (26 letters)
  - **Total**: O(n)
- **Space Complexity**: O(1)
  - Only using fixed-size array `occ[26]` (constant space)
  - A few variables (`left`, `right`, `i`)

## Key Points

1. **Palindrome Property**: At most 1 odd-frequency character per palindrome
2. **Minimum Palindromes**: `max(odd_count, 1)` - need at least one for each odd-frequency character
3. **Maximum Palindromes**: `n` - one per character
4. **Feasibility**: Check if `k` is between min and max
5. **Simple Solution**: Just count frequencies and check bounds

## Alternative Approaches

### **Approach 1: Frequency Counting (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Optimal solution, most efficient

### **Approach 2: Hash Map**
- **Time**: O(n)
- **Space**: O(26) = O(1)
- **Similar**: Use `unordered_map` instead of array (same complexity)

### **Approach 3: Greedy Construction**
- **Time**: O(n)
- **Space**: O(n)
- **Overkill**: Try to actually construct palindromes (not needed, bounds check is sufficient)

## Edge Cases

1. **All even frequencies**: `s = "aabb"`, `k = 1` → return `true` (left = 1, right = 4)
2. **All odd frequencies**: `s = "abc"`, `k = 3` → return `true` (left = 3, right = 3)
3. **k equals minimum**: `s = "aabbc"`, `k = 1` → return `true` (left = 1, right = 5)
4. **k equals maximum**: `s = "abc"`, `k = 3` → return `true` (left = 3, right = 3)
5. **k less than minimum**: `s = "leetcode"`, `k = 3` → return `false` (left = 6, right = 8)
6. **k greater than maximum**: `s = "abc"`, `k = 4` → return `false` (left = 3, right = 3)

## Common Mistakes

1. **Forgetting minimum bound**: Not using `max(left, 1)` when all frequencies are even
2. **Wrong odd count**: Not counting all characters with odd frequency
3. **Wrong bounds**: Confusing minimum and maximum
4. **Off-by-one errors**: Incorrect calculation of bounds
5. **Not understanding palindrome property**: Not realizing each palindrome can have at most 1 odd-frequency character

## Related Problems

- [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) - Check if string can be palindrome
- [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) - Build longest palindrome
- [1177. Can Make Palindrome from Substring](https://leetcode.com/problems/can-make-palindrome-from-substring/) - Check if substring can be palindrome
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) - Can make palindrome with 1 deletion

## Follow-Up: Why Minimum is `max(odd_count, 1)`

**Question**: Why do we need `max(odd_count, 1)` instead of just `odd_count`?

**Answer**:
- **If `odd_count > 0`**: Need at least `odd_count` palindromes (one center per odd-frequency character)
- **If `odd_count == 0`**: All frequencies are even, but we still need at least 1 palindrome to use all characters
- **Example**: `s = "aabb"` (all even) → `odd_count = 0`, but we need at least 1 palindrome to use all 4 characters
- **Therefore**: `left = max(odd_count, 1)` ensures we always have at least 1 palindrome

## Tags

`String`, `Greedy`, `Hash Table`, `Medium`

