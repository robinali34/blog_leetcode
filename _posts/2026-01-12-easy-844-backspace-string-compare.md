---
layout: post
title: "844. Backspace String Compare"
date: 2026-01-12 00:00:00 -0700
categories: [leetcode, easy, string, two-pointers, stack]
permalink: /2026/01/12/easy-844-backspace-string-compare/
tags: [leetcode, easy, string, two-pointers, stack, simulation]
---

# 844. Backspace String Compare

## Problem Statement

Given two strings `s` and `t`, return `true` *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

## Examples

**Example 1:**
```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
```

**Example 2:**
```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
```

**Example 3:**
```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```

## Constraints

- `1 <= s.length, t.length <= 200`
- `s` and `t` only contain lowercase letters and `'#'` characters.

## Solution Approach

This problem can be solved in two ways:
1. **Stack-based**: Build the final strings and compare (O(n) time, O(n) space)
2. **Two Pointers (Backwards)**: Process strings backwards, skipping characters based on backspaces (O(n) time, O(1) space)

The two-pointer approach is more space-efficient and processes strings in reverse to handle backspaces naturally.

### Key Insights:

1. **Backwards Processing**: Process from right to left to handle backspaces naturally
2. **Skip Counter**: Track how many characters to skip due to backspaces
3. **Character Matching**: Compare actual characters (after handling backspaces) from both strings
4. **Early Termination**: Return `false` if characters don't match

### Algorithm:

1. **Initialize**: Two pointers at end of both strings, skip counters for both
2. **While either string has characters**:
   - Process backspaces in `s`: skip `#` and characters to be deleted
   - Process backspaces in `t`: skip `#` and characters to be deleted
   - Compare current characters: if they don't match, return `false`
   - Move both pointers left
3. **Return**: `true` if both pointers reached `-1` (both strings processed)

## Solution

### **Solution: Two Pointers (Backwards)**

```cpp
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        // 1. string construct: ab#c backwards construct: ca
        // Request: O(n) time O(1) space -> in space update.
        // 2. backwars, 2 pointers: if # move 2 backwards,  then compare
        int i = s.length() -1, j = t.length() - 1;
        int skipS = 0, skipT = 0;
        while(i >= 0 || j >= 0) {
            while(i >= 0) {
                if(s[i] == '#') {skipS++; i--;}
                else if(skipS > 0) {skipS--; i--;}
                else break;
            }
            while(j >=0) {
                if(t[j] == '#') {skipT++; j--;}
                else if(skipT > 0) {skipT--; j--;}
                else break;
            }
            if(i >= 0 && j>= 0 && s[i] != t[j]) return false;
            i--;
            j--;
        }
        return i == j;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 6-7)**:
   - `i = s.length() - 1`, `j = t.length() - 1`: Start from end of both strings
   - `skipS = 0`, `skipT = 0`: Counters for characters to skip in each string

2. **Main Loop (Line 8)**: Continue while either string has unprocessed characters

3. **Process Backspaces in `s` (Lines 9-13)**:
   - **If `s[i] == '#'`**: Increment `skipS` and move left (backspace found)
   - **Else if `skipS > 0`**: Decrement `skipS` and move left (skip character due to backspace)
   - **Else**: Break (found actual character to compare)

4. **Process Backspaces in `t` (Lines 14-18)**: Same logic for string `t`

5. **Compare Characters (Lines 19-20)**:
   - If both pointers are valid (`i >= 0 && j >= 0`) and characters don't match, return `false`
   - Move both pointers left

6. **Return (Line 22)**: `i == j` ensures both strings are fully processed (both `-1`)

### **Why This Works:**

- **Backwards Processing**: Processing from right to left handles backspaces naturally
- **Skip Counter**: Tracks how many characters to skip due to backspaces encountered
- **Character Matching**: Only compares actual characters (after handling backspaces)
- **Space Efficient**: O(1) space, no need to build final strings

### **Example Walkthrough:**

**For `s = "ab#c"`, `t = "ad#c"`:**

```
Initial: i = 3, j = 3, skipS = 0, skipT = 0

Iteration 1:
  Process s: i=3, s[3]='c', skipS=0 → break, i=3
  Process t: j=3, t[3]='c', skipT=0 → break, j=3
  Compare: s[3]='c' == t[3]='c' ✓
  i=2, j=2

Iteration 2:
  Process s: i=2, s[2]='#', skipS++ → skipS=1, i=1
            i=1, s[1]='b', skipS>0 → skipS--, skipS=0, i=0
            i=0, s[0]='a', skipS=0 → break, i=0
  Process t: j=2, t[2]='#', skipT++ → skipT=1, j=1
            j=1, t[1]='d', skipT>0 → skipT--, skipT=0, j=0
            j=0, t[0]='a', skipT=0 → break, j=0
  Compare: s[0]='a' == t[0]='a' ✓
  i=-1, j=-1

Loop ends: i=-1, j=-1
Return: i == j → -1 == -1 → true
```

**For `s = "ab##"`, `t = "c#d#"`:**

```
Initial: i = 3, j = 3, skipS = 0, skipT = 0

Iteration 1:
  Process s: i=3, s[3]='#', skipS++ → skipS=1, i=2
            i=2, s[2]='#', skipS++ → skipS=2, i=1
            i=1, s[1]='b', skipS>0 → skipS--, skipS=1, i=0
            i=0, s[0]='a', skipS>0 → skipS--, skipS=0, i=-1
  Process t: j=3, t[3]='#', skipT++ → skipT=1, j=2
            j=2, t[2]='d', skipT>0 → skipT--, skipT=0, j=1
            j=1, t[1]='#', skipT++ → skipT=1, j=0
            j=0, t[0]='c', skipT>0 → skipT--, skipT=0, j=-1
  Compare: i=-1, j=-1 (both exhausted)
  i=-1, j=-1

Loop ends: i=-1, j=-1
Return: i == j → -1 == -1 → true
```

### **Complexity Analysis:**

- **Time Complexity:** O(n + m) where n and m are lengths of `s` and `t`
  - Each character is visited at most once
  - Total: O(n + m)
- **Space Complexity:** O(1)
  - Only using a few variables: `i`, `j`, `skipS`, `skipT`
  - No additional data structures

## Alternative Approach: Stack-Based

```cpp
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return buildString(s) == buildString(t);
    }
    
private:
    string buildString(string& str) {
        string result;
        for(char c : str) {
            if(c == '#') {
                if(!result.empty()) {
                    result.pop_back();
                }
            } else {
                result.push_back(c);
            }
        }
        return result;
    }
};
```

**Time Complexity:** O(n + m)  
**Space Complexity:** O(n + m)

**Comparison:**
- **Stack-based**: Simpler to understand, but uses O(n + m) space
- **Two Pointers**: More complex, but O(1) space - better for large inputs

## Key Insights

1. **Backwards Processing**: Processing from right to left handles backspaces naturally
2. **Skip Counter**: Tracks characters to skip due to backspaces
3. **Character Matching**: Only compares actual characters after handling backspaces
4. **Space Efficiency**: Two-pointer approach achieves O(1) space

## Edge Cases

1. **All backspaces**: `s = "###"`, `t = "##"` → both become `""`, return `true`
2. **Empty strings**: `s = ""`, `t = ""` → return `true`
3. **Backspace at start**: `s = "#a"`, `t = "a"` → both become `"a"`, return `true`
4. **Different lengths**: `s = "a#b"`, `t = "b"` → both become `"b"`, return `true`
5. **No backspaces**: `s = "abc"`, `t = "abc"` → return `true`

## Common Mistakes

1. **Wrong skip logic**: Not properly handling consecutive backspaces
2. **Index errors**: Off-by-one errors when moving pointers
3. **Missing break**: Not breaking from inner loops when finding actual character
4. **Wrong comparison**: Comparing before processing all backspaces
5. **Return condition**: Not checking `i == j` correctly (both should be `-1`)

## Related Problems

- [LC 1047: Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) - Similar stack-based pattern
- [LC 1209: Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) - K duplicates version
- [LC 1544: Make The String Great](https://leetcode.com/problems/make-the-string-great/) - Similar character removal pattern

---

*This problem demonstrates the two-pointer technique with backwards processing. The key insight is that processing from right to left makes handling backspaces straightforward, and using skip counters allows O(1) space complexity.*

