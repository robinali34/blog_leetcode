---
layout: post
title: "[Medium] 93. Restore IP Addresses"
date: 2025-11-14 00:00:00 -0800
categories: leetcode algorithm medium cpp backtracking string problem-solving
---

# [Medium] 93. Restore IP Addresses

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (inclusive) and cannot have leading zeros.

- For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are **invalid** IP addresses.

Given a string `s` containing only digits, return *all possible valid IP addresses that can be formed by inserting dots into* `s`. You may **not** reorder or remove any digits in `s`. You may return the valid IP addresses in **any order**.

## Examples

**Example 1:**
```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

**Example 2:**
```
Input: s = "0000"
Output: ["0.0.0.0"]
```

**Example 3:**
```
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

## Constraints

- `1 <= s.length <= 20`
- `s` consists of digits only.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **IP address format**: What is a valid IP address? (Assumption: Four parts separated by dots, each part is 0-255, no leading zeros except "0")

2. **Restoration**: What does "restore" mean? (Assumption: Insert dots to split string into four valid IP address parts)

3. **Return format**: What should we return? (Assumption: List of all valid IP addresses - strings with dots inserted)

4. **Leading zeros**: How should we handle leading zeros? (Assumption: Not allowed - "01" is invalid, "0" is valid)

5. **All combinations**: Should we return all valid IPs? (Assumption: Yes - return all possible valid IP addresses)

## Solution: Backtracking with C++20 Optimizations

**Time Complexity:** O(1) - At most 3^4 = 81 combinations  
**Space Complexity:** O(1) - At most 19 characters per IP address

This solution uses backtracking to try all possible ways to split the string into 4 parts. We optimize with C++20 features including `string_view` for efficient substring operations and early pruning.

### Solution 1: Optimized C++20 Version

```cpp
using namespace std;

class Solution {
private:
    // Check if a segment is valid using string_view for efficiency
    bool isValid(string_view segment) {
        int len = segment.length();
        
        // Single digit is always valid (0-9)
        if (len == 1) return true;
        
        // Leading zero is invalid
        if (segment[0] == '0') return false;
        
        // Check if <= 255 using efficient comparison
        if (len == 2) return true;  // 10-99
        if (len == 3) {
            // Compare with "255" lexicographically
            return segment <= "255";
        }
        
        return false;  // len > 3 is invalid
    }

    void backtrack(
        string_view s,
        int start,
        vector<int>& dots,
        vector<string>& result
    ) {
        int remainingLen = (int)s.length() - start;
        int remainingCnt = 4 - (int)dots.size();

        // Early pruning: check if remaining digits can form valid segments
        if (remainingLen > remainingCnt * 3 || remainingLen < remainingCnt) {
            return;
        }

        // Base case: we have 3 dots, check if remaining segment is valid
        if (dots.size() == 3) {
            auto lastSegment = s.substr(start);
            if (isValid(lastSegment)) {
                // Build IP address efficiently
                string ip;
                ip.reserve(s.length() + 3);  // Reserve space for dots
                
                int last = 0;
                for (int dot : dots) {
                    ip.append(s.substr(last, dot));
                    last += dot;
                    ip.append(".");
                }
                ip.append(s.substr(start));
                result.push_back(move(ip));
            }
            return;
        }

        // Try segments of length 1, 2, or 3
        for (int curr = 1; curr <= 3 && curr <= remainingLen; curr++) {
            dots.push_back(curr);
            auto segment = s.substr(start, curr);
            if (isValid(segment)) {
                backtrack(s, start + curr, dots, result);
            }
            dots.pop_back();
        }
    }

public:
    vector<string> restoreIpAddresses(string s) {
        vector<int> dots;
        dots.reserve(3);  // At most 3 dots
        vector<string> result;
        
        // Use string_view to avoid copying
        string_view sv(s);
        backtrack(sv, 0, dots, result);
        
        return result;
    }
};
```

### Solution 2: Further Optimized with String Building

```cpp
using namespace std;

class Solution {
private:
    bool isValid(string_view segment) {
        int len = segment.length();
        if (len == 1) return true;
        if (segment[0] == '0') return false;
        if (len == 2) return true;
        return len == 3 && segment <= "255";
    }

    void backtrack(
        string_view s,
        int start,
        vector<int>& segments,
        vector<string>& result
    ) {
        int remainingLen = (int)s.length() - start;
        int remainingCnt = 4 - (int)segments.size();

        if (remainingLen > remainingCnt * 3 || remainingLen < remainingCnt) {
            return;
        }

        if (segments.size() == 3) {
            auto lastSegment = s.substr(start);
            if (isValid(lastSegment)) {
                // Build IP more efficiently by pre-calculating size
                string ip;
                int totalLen = (int)s.length() + 3;
                ip.reserve(totalLen);
                
                int pos = 0;
                for (int segLen : segments) {
                    ip.append(s.substr(pos, segLen));
                    pos += segLen;
                    ip += '.';
                }
                ip.append(s.substr(start));
                result.push_back(move(ip));
            }
            return;
        }

        for (int len = 1; len <= 3 && len <= remainingLen; len++) {
            segments.push_back(len);
            if (isValid(s.substr(start, len))) {
                backtrack(s, start + len, segments, result);
            }
            segments.pop_back();
        }
    }

public:
    vector<string> restoreIpAddresses(string s) {
        vector<int> segments;
        segments.reserve(3);
        vector<string> result;
        
        backtrack(string_view(s), 0, segments, result);
        return result;
    }
};
```

## Key Optimizations (C++20)

1. **`string_view`**: Avoids string copying when checking segments and building results
2. **`reserve()`**: Pre-allocates memory for vectors and strings to avoid reallocations
3. **Early Pruning**: Checks if remaining digits can form valid segments before recursing
4. **Move Semantics**: Uses `move()` when pushing to result vector
5. **Efficient String Building**: Pre-calculates size and uses `append()` for better performance

## How the Algorithm Works

### Step-by-Step Example: `s = "25525511135"`

1. **Try first segment "2"** (length 1)
   - Valid: `2` (0-255)
   - Recursively try remaining: `"5525511135"`

2. **Try second segment "5"** (length 1)
   - Valid: `5`
   - Continue: `"525511135"`

3. **Continue building...**
   - Eventually find: `"255.255.11.135"` and `"255.255.111.35"`

### Visual Representation

```
"25525511135"
│
├─ "2" (valid)
│  ├─ "5" (valid)
│  │  ├─ "5" (valid)
│  │  │  └─ "25511135" → try "255", "2551", "25511"...
│  │  └─ "55" (valid)
│  │     └─ ...
│  └─ "55" (valid)
│     └─ ...
└─ "25" (valid)
   └─ ...
```

## Algorithm Breakdown

### 1. Validation Function

```cpp
bool isValid(std::string_view segment) {
    if (segment.length() == 1) return true;  // 0-9
    if (segment[0] == '0') return false;     // Leading zero
    if (segment.length() == 2) return true;  // 10-99
    return segment <= "255";                  // 100-255
}
```

### 2. Backtracking Function

```cpp
void backtrack(string_view s, int start, vector<int>& segments, ...) {
    // Early pruning
    if (remainingLen > remainingCnt * 3 || remainingLen < remainingCnt) {
        return;
    }
    
    // Base case: 3 segments placed
    if (segments.size() == 3) {
        // Check last segment and build IP
    }
    
    // Try segments of length 1, 2, 3
    for (int len = 1; len <= 3; ++len) {
        if (isValid(s.substr(start, len))) {
            backtrack(s, start + len, segments, result);
        }
    }
}
```

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time** | O(1) - At most 3^4 = 81 combinations |
| **Space** | O(1) - At most 19 characters per IP address |
| **Recursion Depth** | O(4) - Maximum 4 segments |

## Edge Cases

1. **All zeros**: `"0000"` → `["0.0.0.0"]`
2. **Leading zeros**: `"010010"` → `["0.10.0.10","0.100.1.0"]`
3. **Long string**: `"255255255255"` → `["255.255.255.255"]`
4. **Short string**: `"1111"` → `["1.1.1.1"]`

## Why This Solution is Optimal

1. **Early Pruning**: Eliminates invalid branches immediately
2. **String View**: Avoids unnecessary string copies
3. **Memory Pre-allocation**: Reduces reallocations
4. **Constant Time**: Bounded by maximum 81 combinations
5. **Clean Backtracking**: Simple and maintainable

## Common Mistakes

1. **Not checking leading zeros**: `"010"` is invalid
2. **Not checking range**: Numbers must be 0-255
3. **Not pruning early**: Should check remaining length
4. **String copying**: Use `string_view` for efficiency
5. **Forgetting base case**: Must have exactly 4 segments

## Related Problems

- [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
- [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

