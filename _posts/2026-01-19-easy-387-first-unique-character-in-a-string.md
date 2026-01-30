---
layout: post
title: "387. First Unique Character in a String"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, string, hash-table]
permalink: /2026/01/19/easy-387-first-unique-character-in-a-string/
tags: [leetcode, easy, string, hash-table, bit-manipulation, frequency-counting]
---

# 387. First Unique Character in a String

## Problem Statement

Given a string `s`, find the **first non-repeating character** in it and return its **index**. If it does not exist, return `-1`.

## Examples

**Example 1:**
```
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not repeat.
```

**Example 2:**
```
Input: s = "loveleetcode"
Output: 2
Explanation: The character 'v' at index 2 is the first character that does not repeat.
```

**Example 3:**
```
Input: s = "aabb"
Output: -1
Explanation: All characters repeat, so return -1.
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Unique definition**: What makes a character unique? (Assumption: A character that appears exactly once in the string)

2. **Return value**: What should we return if no unique character exists? (Assumption: Return -1 - no unique character found)

3. **Case sensitivity**: Are characters case-sensitive? (Assumption: Based on constraints, only lowercase letters, so case doesn't matter)

4. **Index format**: Should we return 0-indexed or 1-indexed position? (Assumption: 0-indexed - standard array indexing)

5. **Character set**: What characters can appear in the string? (Assumption: Only lowercase English letters 'a'-'z' - 26 characters)

## Solution Approach

This problem requires finding the first character that appears exactly once. There are several approaches:

1. **Bit Manipulation**: Use bitsets to track characters seen once vs multiple times
2. **Count Array**: Count occurrences, then find first character with count 1
3. **Hash Map**: Similar to count array but using hash map
4. **Two-Pass**: Count first, then scan for first unique

### Key Insights:

1. **Frequency Counting**: Track how many times each character appears
2. **Order Preservation**: Need to maintain order to find "first" unique
3. **Bit Manipulation**: Efficient way to track seen-once vs seen-multiple
4. **Early Exit**: Can optimize by tracking first occurrence indices

## Solution 1: Bit Manipulation (Efficient)

```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        int once = 0, multi = 0;
        int idx = -1;
        for(char ch : s) {
            int bit = 1 << (ch - 'a');
            multi |= once & bit;
            once ^= bit;
            once &= ~multi;
        }

        for(int i = 0; i < (int)s.length(); i++) {
            int bit = 1 << (s[i] - 'a');
            if(once & bit) {
                return i;
            }
        }
        return -1;
    }
};
```

### Algorithm Explanation:

1. **Initialize Bitsets**:
   - `once`: Bits set for characters seen exactly once
   - `multi`: Bits set for characters seen multiple times

2. **First Pass - Track Frequencies**:
   - For each character, calculate its bit position: `bit = 1 << (ch - 'a')`
   - **Update `multi`**: `multi |= once & bit` - if character already in `once`, mark it in `multi`
   - **Toggle `once`**: `once ^= bit` - toggle the bit (XOR)
   - **Remove from `once`**: `once &= ~multi` - remove characters that appear multiple times

3. **Second Pass - Find First Unique**:
   - Scan string from start
   - Check if character's bit is set in `once`
   - Return first index where `once & bit` is true

### Example Walkthrough:

**Input:** `s = "leetcode"`

```
First Pass:
  'l': bit = 1 << ('l' - 'a') = 1 << 11 = 2048
    multi |= once & 2048 = 0 (once is 0)
    once ^= 2048 → once = 2048
    once &= ~multi = 2048 & ~0 = 2048

  'e': bit = 1 << ('e' - 'a') = 1 << 4 = 16
    multi |= once & 16 = 0 (once doesn't have bit 16)
    once ^= 16 → once = 2048 | 16 = 2064
    once &= ~multi = 2064 & ~0 = 2064

  'e': bit = 16 (second 'e')
    multi |= once & 16 = 2064 & 16 = 16 → multi = 16
    once ^= 16 → once = 2048 (removed 'e')
    once &= ~multi = 2048 & ~16 = 2048

  ... continue for all characters ...

After first pass: once contains bits for characters seen exactly once

Second Pass:
  i=0, 'l': bit = 2048, once & 2048 = 2048 (set!) → return 0 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - First pass: O(n) to process all characters
  - Second pass: O(n) to find first unique
  - Total: O(n)

- **Space Complexity:** O(1)
  - Only two integers (`once` and `multi`) for bit manipulation
  - Constant space regardless of input size

## Solution 2: Count Array with Index Tracking

```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> cnt(26, 0);
        vector<int> idx(26, -1);
        for(int i = 0; i < (int)s.length(); i++) {
            // log first idx
            int curr = s[i] - 'a';
            if(cnt[curr] == 0) {
                idx[curr] = i;
            }
            cnt[curr]++;
        }
        int minIdx = INT_MAX;
        for(int i = 0; i < 26; i++){
            if(cnt[i] == 1) {
                minIdx = min(minIdx, idx[i]);
            }
        }
        return minIdx == INT_MAX ? -1: minIdx;
    }
};
```

### Algorithm Explanation:

1. **Initialize Arrays**:
   - `cnt[26]`: Count occurrences of each character
   - `idx[26]`: Store first occurrence index of each character

2. **First Pass - Count and Track Indices**:
   - For each character at index `i`:
     - Calculate character index: `curr = s[i] - 'a'`
     - If first time seeing character (`cnt[curr] == 0`), record index: `idx[curr] = i`
     - Increment count: `cnt[curr]++`

3. **Second Pass - Find Minimum Index**:
   - Iterate through all 26 characters
   - If character appears exactly once (`cnt[i] == 1`):
     - Update minimum index: `minIdx = min(minIdx, idx[i])`
   - Return `minIdx` (or `-1` if no unique character)

### Example Walkthrough:

**Input:** `s = "loveleetcode"`

```
First Pass:
  i=0, 'l': curr=11, cnt[11]=0 → idx[11]=0, cnt[11]=1
  i=1, 'o': curr=14, cnt[14]=0 → idx[14]=1, cnt[14]=1
  i=2, 'v': curr=21, cnt[21]=0 → idx[21]=2, cnt[21]=1
  i=3, 'e': curr=4, cnt[4]=0 → idx[4]=3, cnt[4]=1
  i=4, 'l': curr=11, cnt[11]=1 → skip idx update, cnt[11]=2
  i=5, 'e': curr=4, cnt[4]=1 → skip idx update, cnt[4]=2
  ... continue ...

After first pass:
  cnt: ['e'=4, 'l'=2, 'o'=1, 't'=1, 'c'=1, 'd'=1, 'v'=1, ...]
  idx: ['l'=0, 'o'=1, 'v'=2, 'e'=3, 't'=7, 'c'=8, 'd'=9, ...]

Second Pass:
  Check all 26 characters:
    'o': cnt[14]=1 → minIdx = min(INT_MAX, 1) = 1
    'v': cnt[21]=1 → minIdx = min(1, 2) = 1
    't': cnt[19]=1 → minIdx = min(1, 7) = 1
    'c': cnt[2]=1 → minIdx = min(1, 8) = 1
    'd': cnt[3]=1 → minIdx = min(1, 9) = 1

  But wait, 'v' appears at index 2, which is before 'o' at index 1...
  Actually, 'v' is at index 2, 'o' is at index 1, so 'o' comes first.
  Wait, let me recalculate: 'l'=0, 'o'=1, 'v'=2, so 'v' is at index 2.

  Actually, the correct answer should be 2 ('v'), but the algorithm finds 'o' at 1.
  Let me check: 'o' appears only once? Yes. So minIdx = 1.

  But the expected output is 2 for 'v'. Let me check the string again:
  "loveleetcode" - positions: l=0, o=1, v=2, e=3, l=4, e=5, e=6, t=7, c=8, o=9, d=10, e=11
  
  So 'o' appears at positions 1 and 9, so cnt['o'] = 2, not 1!
  'v' appears only at position 2, so cnt['v'] = 1, idx['v'] = 2.
  
  So minIdx should be 2 for 'v'. The algorithm is correct.
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - First pass: O(n) to count and track indices
  - Second pass: O(26) = O(1) to find minimum
  - Total: O(n)

- **Space Complexity:** O(1)
  - Two arrays of size 26 (constant)
  - O(1) space regardless of input size

## Key Insights

1. **Bit Manipulation**: Efficient way to track seen-once vs seen-multiple using XOR and AND operations
2. **Index Tracking**: Store first occurrence index to find minimum later
3. **Two-Pass Approach**: Count first, then find first unique
4. **Early Exit**: Can optimize by scanning string in second pass instead of all 26 characters

## Edge Cases

1. **All unique**: `s = "abc"` → return `0`
2. **All duplicate**: `s = "aabb"` → return `-1`
3. **Single character**: `s = "a"` → return `0`
4. **Unique at end**: `s = "aabbc"` → return `4`
5. **Unique in middle**: `s = "aabcc"` → return `2` ('b')
6. **Long string**: All characters unique, return `0`

## Common Mistakes

1. **Wrong bit operations**: Incorrect XOR/AND logic in bit manipulation
2. **Index confusion**: Not tracking first occurrence correctly
3. **Off-by-one**: Incorrect character to index conversion
4. **Not handling all duplicates**: Forgetting to return `-1`
5. **Wrong order**: Returning last unique instead of first

## Alternative Approaches

### Simple Count Array (Standard)

```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> count(26, 0);
        for(char c : s) {
            count[c - 'a']++;
        }
        for(int i = 0; i < s.length(); i++) {
            if(count[s[i] - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
};
```

**Pros**: Simple, clear, easy to understand  
**Cons**: Two passes through string (though still O(n))

### Hash Map Approach

```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> count;
        for(char c : s) {
            count[c]++;
        }
        for(int i = 0; i < s.length(); i++) {
            if(count[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};
```

**Pros**: Works for any character set  
**Cons**: Slightly more overhead than array

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Bit Manipulation** | O(n) | O(1) | Most space-efficient, elegant | Complex logic, harder to understand |
| **Count Array + Index** | O(n) | O(1) | Clear logic, tracks indices | Two arrays needed |
| **Simple Count Array** | O(n) | O(1) | Simplest, most readable | Two passes through string |
| **Hash Map** | O(n) | O(k) | Flexible, works for any charset | More overhead |

## When to Use Each Approach

- **Bit Manipulation**: When space optimization is critical, or demonstrating bit manipulation skills
- **Count Array + Index**: When you need to track both frequency and position efficiently
- **Simple Count Array**: When clarity and simplicity are priority (most common)
- **Hash Map**: When character set is unknown or not limited to lowercase letters

## Related Problems

- [LC 383: Ransom Note](https://leetcode.com/problems/ransom-note/) - Character frequency counting
- [LC 389: Find the Difference](https://leetcode.com/problems/find-the-difference/) - Find extra character
- [LC 451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) - Sort by frequency
- [LC 438: Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) - Character frequency matching
- [LC 567: Permutation in String](https://leetcode.com/problems/permutation-in-string/) - Sliding window with frequency

---

*This problem demonstrates **efficient character frequency tracking** using **bit manipulation** or **count arrays**. The bit manipulation approach is particularly elegant, using XOR to toggle bits and track characters seen once vs multiple times.*

