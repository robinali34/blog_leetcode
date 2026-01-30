---
layout: post
title: "[Medium] 3. Longest Substring Without Repeating Characters"
date: 2025-10-09 21:47:51 -0700
categories: leetcode algorithm medium cpp sliding-window hash-map string two-pointers problem-solving
---

# [Medium] 3. Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without repeating characters.

## Examples

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Substring vs subsequence**: Do we need a contiguous substring or can it be a subsequence? (Assumption: Substring - must be contiguous characters)

2. **Character uniqueness**: What makes characters "repeating"? (Assumption: No character should appear more than once in the substring)

3. **Empty string**: What should we return for an empty string? (Assumption: Return 0 - no substring exists)

4. **Case sensitivity**: Are character comparisons case-sensitive? (Assumption: Yes - 'A' and 'a' are different characters)

5. **Return value**: Should we return length or the substring itself? (Assumption: Return length - integer representing longest substring length)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to find longest substring. Let me check all possible substrings."

**Naive Solution**: Check all possible substrings, for each check if it has no repeating characters, track maximum length.

**Complexity**: O(n³) time, O(n) space

**Issues**:
- O(n³) time - very inefficient
- Checks many redundant substrings
- Repeats character checking for overlapping substrings
- Doesn't leverage sliding window property

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use sliding window. Expand window until duplicate found, then shrink from left."

**Improved Solution**: Use sliding window with two pointers. Expand right pointer, when duplicate found, move left pointer until duplicate removed. Track maximum window size.

**Complexity**: O(n) time, O(min(n, charset)) space

**Improvements**:
- O(n) time - much better
- Sliding window avoids redundant checks
- Hash map/set tracks characters in window
- Handles all cases correctly

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "The sliding window approach is already optimal. Can optimize by storing last occurrence index."

**Best Solution**: Sliding window with hash map storing last occurrence index of each character. When duplicate found, jump left pointer to last occurrence + 1. This avoids unnecessary shrinking.

**Complexity**: O(n) time, O(min(n, charset)) space

**Key Realizations**:
1. Sliding window is optimal approach
2. O(n) time is optimal - must check each character
3. Storing last occurrence optimizes left pointer movement
4. O(min(n, charset)) space is optimal

## Solution: Sliding Window with Hash Map

**Time Complexity:** O(n)  
**Space Complexity:** O(min(m, n)) where m is the size of the charset

Use a sliding window approach with a hash map to track character positions and efficiently update the window boundaries.

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_len = 0;
        unordered_map<char, int> hashmap;

        for (int start = 0, end = 0; end < s.length(); end++) {
            char cur = s[end];
            
            // If character exists and is within current window
            if (hashmap.find(cur) != hashmap.end() && hashmap[cur] >= start) {
                start = hashmap[cur] + 1;  // Move start past the duplicate
            }
            
            hashmap[cur] = end;  // Update character position
            max_len = max(max_len, end - start + 1);  // Update max length
        }
        return max_len;
    }
};
```

## How the Algorithm Works

### Step-by-Step Example: `s = "abcabcbb"`

| Step | end | cur | hashmap | start | window | max_len |
|------|-----|-----|---------|-------|--------|---------|
| 1 | 0 | 'a' | {'a': 0} | 0 | "a" | 1 |
| 2 | 1 | 'b' | {'a': 0, 'b': 1} | 0 | "ab" | 2 |
| 3 | 2 | 'c' | {'a': 0, 'b': 1, 'c': 2} | 0 | "abc" | 3 |
| 4 | 3 | 'a' | {'a': 3, 'b': 1, 'c': 2} | 1 | "bca" | 3 |
| 5 | 4 | 'b' | {'a': 3, 'b': 4, 'c': 2} | 2 | "cab" | 3 |
| 6 | 5 | 'c' | {'a': 3, 'b': 4, 'c': 5} | 3 | "abc" | 3 |
| 7 | 6 | 'b' | {'a': 3, 'b': 6, 'c': 5} | 5 | "cb" | 3 |
| 8 | 7 | 'b' | {'a': 3, 'b': 7, 'c': 5} | 7 | "b" | 3 |

**Final Answer:** 3

### Visual Representation

```
String: "abcabcbb"
        01234567

Step 1-3: "abc" (length 3)
Step 4:   "bca" (length 3) 
Step 5:   "cab" (length 3)
Step 6:   "abc" (length 3)
Step 7:   "cb"  (length 2)
Step 8:   "b"   (length 1)

Maximum length: 3
```

## Key Insights

1. **Sliding Window**: Use two pointers (`start` and `end`) to maintain a valid window
2. **Hash Map Tracking**: Store the last position of each character
3. **Efficient Updates**: When a duplicate is found, move `start` to `hashmap[cur] + 1`
4. **Single Pass**: Process each character exactly once

## Algorithm Breakdown

### 1. Initialize Variables
```cpp
int max_len = 0;
unordered_map<char, int> hashmap;
```

### 2. Expand Window
```cpp
for (int start = 0, end = 0; end < s.length(); end++) {
    char cur = s[end];
```

### 3. Handle Duplicates
```cpp
if (hashmap.find(cur) != hashmap.end() && hashmap[cur] >= start) {
    start = hashmap[cur] + 1;  // Move start past duplicate
}
```

### 4. Update and Track
```cpp
hashmap[cur] = end;  // Update character position
max_len = max(max_len, end - start + 1);  // Update max length
```

## Alternative Approaches

### Approach 1: Brute Force
```cpp
// Check all possible substrings - O(n³)
for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
        if (isUnique(s, i, j)) {
            max_len = max(max_len, j - i + 1);
        }
    }
}
```

### Approach 2: Sliding Window with Set
```cpp
// Use set to track characters in current window
unordered_set<char> window;
int start = 0;
for (int end = 0; end < s.length(); end++) {
    while (window.count(s[end])) {
        window.erase(s[start]);
        start++;
    }
    window.insert(s[end]);
    max_len = max(max_len, end - start + 1);
}
```

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n³) | O(min(m, n)) |
| Sliding Window + Set | O(n) | O(min(m, n)) |
| Sliding Window + Hash Map | O(n) | O(min(m, n)) |

## Edge Cases

1. **Empty string**: `s = ""` → `0`
2. **Single character**: `s = "a"` → `1`
3. **All same characters**: `s = "aaaa"` → `1`
4. **No duplicates**: `s = "abcdef"` → `6`

## Why This Solution is Optimal

1. **Single Pass**: Each character is visited exactly once
2. **Efficient Lookup**: Hash map provides O(1) character position lookup
3. **Smart Window Adjustment**: Directly jumps to the correct position instead of sliding one by one
4. **Minimal Space**: Only stores character positions, not the entire substring

## Common Mistakes

1. **Not checking if duplicate is within current window**
2. **Using `start = end` instead of `start = hashmap[cur] + 1`**
3. **Forgetting to update `max_len` after each iteration**
4. **Not handling edge cases like empty string**

## Related Problems

- [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
- [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
- [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
