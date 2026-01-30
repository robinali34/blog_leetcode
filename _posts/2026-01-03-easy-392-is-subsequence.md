---
layout: post
title: "392. Is Subsequence"
date: 2026-01-03 05:00:00 -0700
categories: [leetcode, easy, string, two-pointers, greedy, dynamic-programming]
permalink: /2026/01/03/easy-392-is-subsequence/
---

# 392. Is Subsequence

## Problem Statement

Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`*, or* `false` *otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Examples

**Example 1:**
```
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: "abc" is a subsequence of "ahbgdc" (characters at positions 0, 2, 5).
```

**Example 2:**
```
Input: s = "axc", t = "ahbgdc"
Output: false
Explanation: "axc" is not a subsequence of "ahbgdc" because 'x' is not found in "ahbgdc".
```

## Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Subsequence definition**: What is a subsequence? (Assumption: Sequence of characters that appear in same order in t, but not necessarily contiguous)

2. **Matching rules**: How do we check if s is subsequence of t? (Assumption: Match characters of s in order within t - maintain relative order)

3. **Return value**: What should we return? (Assumption: Boolean - true if s is subsequence of t, false otherwise)

4. **Empty strings**: What if s is empty? (Assumption: Return true - empty string is subsequence of any string)

5. **Character uniqueness**: Can characters repeat? (Assumption: Yes - characters can appear multiple times, match first occurrence)

## Solution Approach

This is a **two-pointer** problem that can be solved with a greedy approach. The key insight is to use two pointers to match characters of `s` in `t` while maintaining their relative order.

### Key Insights:

1. **Two Pointers**: Use one pointer for `s` and one for `t`
2. **Greedy Matching**: Match characters in order, always moving forward
3. **Order Preservation**: Characters must appear in the same order in `t`
4. **Simple Check**: If we match all characters in `s`, it's a subsequence

### Algorithm:

1. **Initialize**: Two pointers `i` (for `s`) and `j` (for `t`)
2. **Iterate**: While both pointers are within bounds:
   - If characters match, advance both pointers
   - Otherwise, only advance `j` (pointer in `t`)
3. **Check**: Return `true` if `i == N` (all characters in `s` matched)

## Solution

### **Solution: Two Pointers**

```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        const int N = s.length(), M = t.length();
        int i = 0, j = 0;
        while(i < N && j < M) {
            if(s[i] == t[j]) {
                i++;
                j++;
            }
            j++;
        }
        return i == N;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 4-5)**:
   - `N`: Length of string `s`
   - `M`: Length of string `t`
   - `i`: Pointer for string `s` (starts at 0)
   - `j`: Pointer for string `t` (starts at 0)

2. **Match Characters (Lines 6-11)**:
   - **While both pointers are valid**:
     - **If characters match**: `s[i] == t[j]`
       - Advance both pointers (`i++`, `j++`)
       - We found a match, move to next character in both strings
     - **Always advance `j`**: Move pointer in `t` forward
       - Whether match or not, we always check next character in `t`

3. **Check Result (Line 12)**:
   - Return `true` if `i == N` (all characters in `s` were matched)
   - Return `false` otherwise

### **Example Walkthrough:**

**Example 1: `s = "abc"`, `t = "ahbgdc"`**

```
Initial: i=0, j=0, N=3, M=6

Step 1: s[0]='a', t[0]='a'
  Match: i=1, j=1
  Then: j++ → j=2

Step 2: s[1]='b', t[2]='b'
  Match: i=2, j=3
  Then: j++ → j=4

Step 3: s[2]='c', t[4]='d'
  No match: j++ → j=5

Step 4: s[2]='c', t[5]='c'
  Match: i=3, j=6
  Then: j++ → j=7

Loop ends: i=3 == N
Return: true
```

**Example 2: `s = "axc"`, `t = "ahbgdc"`**

```
Initial: i=0, j=0, N=3, M=6

Step 1: s[0]='a', t[0]='a'
  Match: i=1, j=1
  Then: j++ → j=2

Step 2: s[1]='x', t[2]='b'
  No match: j++ → j=3

Step 3: s[1]='x', t[3]='g'
  No match: j++ → j=4

Step 4: s[1]='x', t[4]='d'
  No match: j++ → j=5

Step 5: s[1]='x', t[5]='c'
  No match: j++ → j=6

Loop ends: i=1 != N
Return: false ('x' not found)
```

**Example 3: `s = ""`, `t = "abc"`**

```
Initial: i=0, j=0, N=0, M=3

Loop condition: 0 < 0 && 0 < 3 → false
Loop doesn't execute

Check: i=0 == N=0
Return: true (empty string is subsequence of any string)
```

## Algorithm Breakdown

### **Why Two Pointers Work**

The two-pointer approach is optimal because:
1. **Order Preservation**: We only advance `i` when we find a match, ensuring order
2. **Greedy Choice**: Always match the first occurrence in `t` (greedy)
3. **Linear Time**: Single pass through both strings
4. **Optimal**: O(n + m) time complexity

### **Pointer Movement Logic**

- **When characters match** (`s[i] == t[j]`):
  - Advance `i` (found character in `s`)
  - Advance `j` (move past matched character in `t`)
  - Then advance `j` again (check next character in `t`)

- **When characters don't match** (`s[i] != t[j]`):
  - Keep `i` unchanged (still looking for this character)
  - Advance `j` (skip this character in `t`)

**Note**: The code increments `j` twice when there's a match (once in the `if` block, once after). This is equivalent to:
```cpp
if(s[i] == t[j]) {
    i++;
}
j++;  // Always advance j
```

### **Subsequence Property**

A subsequence maintains the **relative order** of characters:
- `"ace"` is a subsequence of `"abcde"` (positions 0, 2, 4)
- `"aec"` is NOT a subsequence of `"abcde"` (can't get 'e' before 'c')

## Time & Space Complexity

- **Time Complexity**: O(m) where m is the length of `t`
  - We iterate through `t` at most once
  - Pointer `i` can only advance up to `n` (length of `s`)
  - In worst case, we scan all of `t`
- **Space Complexity**: O(1)
  - Only using a few variables
  - No additional data structures

## Key Points

1. **Two Pointers**: Efficient matching technique
2. **Greedy Matching**: Match first occurrence in `t`
3. **Order Preservation**: Characters must appear in same order
4. **Simple Check**: All characters matched if `i == N`
5. **Edge Case**: Empty string `s` is always a subsequence

## Alternative Approaches

### **Approach 1: Two Pointers (Current Solution)**
- **Time**: O(m)
- **Space**: O(1)
- **Best for**: Optimal solution, most efficient

### **Approach 2: Dynamic Programming (LCS)**
- **Time**: O(n × m)
- **Space**: O(n × m)
- **Use when**: Need to find longest common subsequence
- **Overkill**: Not needed for this problem

### **Approach 3: Binary Search (For Multiple Queries)**
- **Time**: O(m + n log m) per query
- **Space**: O(m)
- **Use when**: Need to check many strings `s` against same `t`
- **Idea**: Preprocess `t` to store character positions, use binary search

## Edge Cases

1. **Empty `s`**: `s = ""` → return `true` (empty is subsequence of any string)
2. **Empty `t`**: `s = "a"`, `t = ""` → return `false`
3. **Same strings**: `s = "abc"`, `t = "abc"` → return `true`
4. **Single character**: `s = "a"`, `t = "abc"` → return `true`
5. **No match**: `s = "x"`, `t = "abc"` → return `false`
6. **Repeated characters**: `s = "aa"`, `t = "abac"` → return `true`

## Common Mistakes

1. **Wrong pointer logic**: Not advancing `j` when no match
2. **Order violation**: Matching characters out of order
3. **Off-by-one**: Wrong loop condition or index checking
4. **Empty string**: Forgetting that empty string is always subsequence
5. **Not checking all characters**: Returning early before checking all of `s`

## Related Problems

- [524. Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) - Find longest subsequence
- [792. Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) - Count subsequences
- [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) - Find LCS (DP)
- [727. Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/) - Find minimum window containing subsequence

## Follow-Up: Multiple Queries

If we need to check many strings `s` against the same `t`, we can optimize:

```cpp
// Preprocess t to store character positions
unordered_map<char, vector<int>> charPositions;
for(int i = 0; i < t.length(); i++) {
    charPositions[t[i]].push_back(i);
}

// For each query s, use binary search
bool isSubsequence(string s, unordered_map<char, vector<int>>& pos) {
    int prev = -1;
    for(char c : s) {
        auto it = upper_bound(pos[c].begin(), pos[c].end(), prev);
        if(it == pos[c].end()) return false;
        prev = *it;
    }
    return true;
}
```

**Time**: O(m + n log m) per query (better when many queries)

## Tags

`String`, `Two Pointers`, `Greedy`, `Dynamic Programming`, `Easy`

