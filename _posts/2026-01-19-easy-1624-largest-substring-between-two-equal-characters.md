---
layout: post
title: "1624. Largest Substring Between Two Equal Characters"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, string, hash-table]
permalink: /2026/01/19/easy-1624-largest-substring-between-two-equal-characters/
tags: [leetcode, easy, string, hash-table, substring, two-pointers]
---

# 1624. Largest Substring Between Two Equal Characters

## Problem Statement

Given a string `s`, return the **length of the longest substring** between two equal characters, **excluding** the two equal characters themselves. If no such substring exists, return `-1`.

A **substring** is a contiguous sequence of characters within a string.

## Examples

**Example 1:**
```
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
```

**Example 2:**
```
Input: s = "abca"
Output: 2
Explanation: The optimal substring is "bc" which is of length 2.
```

**Example 3:**
```
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
```

**Example 4:**
```
Input: s = "cabbac"
Output: 4
Explanation: The optimal substring is "abba" which is of length 4.
```

## Constraints

- `1 <= s.length <= 300`
- `s` contains only lowercase English letters.

## Solution Approach

This problem requires finding the maximum distance between two occurrences of the same character. The key insight is:

1. **Track First and Last Occurrences**: For each character, track its leftmost and rightmost positions
2. **Calculate Distance**: The substring length between two equal characters is `right_index - left_index - 1`
3. **Find Maximum**: Return the maximum such distance, or `-1` if no character appears twice

### Key Insights:

1. **Character Tracking**: Use hash maps to store first and last occurrence indices
2. **Distance Calculation**: Length between indices `i` and `j` is `j - i - 1` (excluding both endpoints)
3. **Single Pass**: Can track first occurrence, then update last occurrence as we iterate
4. **Edge Case**: Return `-1` if no character appears twice

### Algorithm:

1. Initialize hash maps for leftmost and rightmost indices
2. First pass: Record leftmost index for each character
3. Second pass: Record rightmost index for characters that appeared before
4. Calculate maximum distance: `right - left - 1` for all characters with both indices
5. Return maximum or `-1`

## Solution

```cpp
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        unordered_map<char, int> LeftIdx, RightIdx;
        int maxLen = -1;
        for(int i = 0; i < (int)s.length(); i++) {
            if(!LeftIdx.contains(s[i])) {
                LeftIdx[s[i]] = i;
            } else {
                RightIdx[s[i]] = i;
            }
        }
        for(auto& [c, idx]: RightIdx) {
            maxLen = max(maxLen, RightIdx[c] - LeftIdx[c] - 1);
        }
        return maxLen;
    }
};
```

### Algorithm Explanation:

1. **Initialize Maps**:
   - `LeftIdx`: Stores the first occurrence index of each character
   - `RightIdx`: Stores the last occurrence index (only for characters appearing multiple times)
   - `maxLen`: Tracks maximum substring length, initialized to `-1`

2. **First Pass - Track Indices**:
   - Iterate through string with index `i`
   - If character `s[i]` not seen before (`!LeftIdx.contains(s[i])`):
     - Record its first occurrence: `LeftIdx[s[i]] = i`
   - Else (character seen before):
     - Update its last occurrence: `RightIdx[s[i]] = i`

3. **Second Pass - Calculate Maximum**:
   - Iterate through `RightIdx` (characters that appear at least twice)
   - For each character `c`:
     - Calculate substring length: `RightIdx[c] - LeftIdx[c] - 1`
     - Update `maxLen` if this length is greater

4. **Return Result**:
   - Returns `maxLen` (will be `-1` if no character appears twice)

### Example Walkthrough:

**Input:** `s = "abca"`

```
Step 1: First pass
  i=0, s[0]='a': LeftIdx['a'] = 0
  i=1, s[1]='b': LeftIdx['b'] = 1
  i=2, s[2]='c': LeftIdx['c'] = 2
  i=3, s[3]='a': 'a' already in LeftIdx → RightIdx['a'] = 3

Step 2: Calculate maximum
  For 'a': RightIdx['a'] - LeftIdx['a'] - 1 = 3 - 0 - 1 = 2
  maxLen = max(-1, 2) = 2

Return: 2 ✓
```

**Input:** `s = "cabbac"`

```
Step 1: First pass
  i=0, s[0]='c': LeftIdx['c'] = 0
  i=1, s[1]='a': LeftIdx['a'] = 1
  i=2, s[2]='b': LeftIdx['b'] = 2
  i=3, s[3]='b': 'b' already in LeftIdx → RightIdx['b'] = 3
  i=4, s[4]='a': 'a' already in LeftIdx → RightIdx['a'] = 4
  i=5, s[5]='c': 'c' already in LeftIdx → RightIdx['c'] = 5

Step 2: Calculate maximum
  For 'c': 5 - 0 - 1 = 4
  For 'a': 4 - 1 - 1 = 2
  For 'b': 3 - 2 - 1 = 0
  maxLen = max(-1, 4, 2, 0) = 4

Return: 4 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - First pass: O(n) to iterate through string
  - Second pass: O(k) where k = number of unique characters appearing multiple times (≤ 26)
  - Total: O(n)

- **Space Complexity:** O(1)
  - `LeftIdx` and `RightIdx` store at most 26 entries (lowercase letters)
  - Constant space regardless of input size

## Key Insights

1. **Two-Pass Approach**: First pass tracks indices, second pass calculates distances
2. **Hash Map Efficiency**: O(1) lookup and insertion for character tracking
3. **Distance Formula**: Length between indices `i` and `j` is `j - i - 1` (excluding endpoints)
4. **Edge Case Handling**: Return `-1` when no character appears twice
5. **Optimization**: Only track rightmost index for characters that appear multiple times

## Edge Cases

1. **No duplicate characters**: `s = "abc"` → return `-1`
2. **Adjacent duplicates**: `s = "aa"` → return `0` (empty substring)
3. **Single character**: `s = "a"` → return `-1`
4. **All same character**: `s = "aaaa"` → return `2` (between first and last)
5. **Multiple pairs**: `s = "cabbac"` → return `4` (between first and last 'c')
6. **Overlapping pairs**: `s = "abba"` → return `2` (between first and last 'a')

## Common Mistakes

1. **Incorrect distance calculation**: Using `right - left` instead of `right - left - 1`
2. **Not handling single occurrence**: Forgetting to return `-1` when no duplicates
3. **Off-by-one errors**: Incorrect substring length calculation
4. **Not updating rightmost**: Only tracking first occurrence, missing last occurrence
5. **Initialization**: Not initializing `maxLen` to `-1` correctly

## Alternative Approaches

### Single Pass with Array

```cpp
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        vector<int> first(26, -1);
        int maxLen = -1;
        for(int i = 0; i < (int)s.length(); i++) {
            int c = s[i] - 'a';
            if(first[c] == -1) {
                first[c] = i;
            } else {
                maxLen = max(maxLen, i - first[c] - 1);
            }
        }
        return maxLen;
    }
};
```

**Pros**: More efficient, single pass, uses array instead of hash map  
**Cons**: Assumes lowercase letters only (which matches constraints)

### Two-Pass with Last Index Only

```cpp
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        unordered_map<char, int> lastIdx;
        for(int i = 0; i < (int)s.length(); i++) {
            lastIdx[s[i]] = i;
        }
        
        int maxLen = -1;
        for(int i = 0; i < (int)s.length(); i++) {
            if(lastIdx[s[i]] != i) {
                maxLen = max(maxLen, lastIdx[s[i]] - i - 1);
            }
        }
        return maxLen;
    }
};
```

**Pros**: Clear separation of tracking and calculation  
**Cons**: Two full passes, slightly more complex

## Comparison of Approaches

| Approach | Time | Space | Passes | Pros |
|----------|------|-------|--------|------|
| **Hash Map (Provided)** | O(n) | O(1) | 2 | Flexible, handles any characters |
| **Array Single Pass** | O(n) | O(1) | 1 | Most efficient, single pass |
| **Last Index Only** | O(n) | O(1) | 2 | Clear logic, easy to understand |

## When to Use This Pattern

1. **Substring Problems**: Finding distances between character occurrences
2. **Character Frequency**: Tracking first/last occurrence positions
3. **Range Queries**: Calculating lengths between specific positions
4. **String Analysis**: Analyzing character distribution patterns
5. **Optimization Problems**: Finding maximum/minimum distances

## Related Problems

- [LC 3: Longest Substring Without Repeating Characters](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) - Finding longest substring with unique characters
- [LC 159: Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) - Substring with character constraints
- [LC 340: Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) - Generalization of LC 159
- [LC 424: Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) - Substring with replacements
- [LC 904: Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) - Similar sliding window pattern

---

*This problem demonstrates **efficient character tracking** using hash maps to find the maximum distance between equal characters. The key insight is tracking first and last occurrences, then calculating the substring length between them.*

