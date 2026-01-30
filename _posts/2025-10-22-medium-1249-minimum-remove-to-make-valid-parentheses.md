---
layout: post
title: "LC 1249: Minimum Remove to Make Valid Parentheses"
date: 2025-10-22 13:30:00 -0700
categories: leetcode medium string stack
permalink: /posts/2025-10-22-medium-1249-minimum-remove-to-make-valid-parentheses/
tags: [leetcode, medium, string, stack, parentheses, validation]
---

# LC 1249: Minimum Remove to Make Valid Parentheses

**Difficulty:** Medium  
**Category:** String, Stack  
**Companies:** Amazon, Facebook, Microsoft, Google

## Problem Statement

Given a string `s` of `'('`, `')'` and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting parentheses string is valid and return **any** valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

### Examples

**Example 1:**
```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

**Example 2:**
```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

**Example 3:**
```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

### Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is either `'('`, `')'`, or lowercase English letter.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Valid parentheses**: What makes parentheses valid? (Assumption: Every opening '(' has matching closing ')', properly nested)

2. **Optimization goal**: What are we optimizing for? (Assumption: Minimum number of removals to make parentheses valid)

3. **Return format**: What should we return? (Assumption: String - valid parentheses string after minimum removals)

4. **Multiple solutions**: Are there multiple valid solutions? (Assumption: Yes - can return any valid string with minimum removals)

5. **Non-parentheses characters**: How should we handle letters? (Assumption: Keep all letters - only remove invalid parentheses)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Try removing different combinations of parentheses and check if the resulting string is valid. This requires trying all subsets of parentheses to remove, which has exponential complexity. For each combination, validate the parentheses string, which takes O(n) time. This is too slow for large strings.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a stack to identify unmatched parentheses. First pass: mark all unmatched opening and closing parentheses. Second pass: build result string excluding marked characters. However, identifying which parentheses to remove requires careful tracking. Alternatively, count opening and closing parentheses, but handling the minimum removal constraint is tricky.

**Step 3: Optimized Solution (8 minutes)**

Use two passes: First pass (left to right): track balance, mark excess closing parentheses for removal. Second pass (right to left): track balance, mark excess opening parentheses for removal. Then build result string excluding marked characters. This achieves O(n) time with O(n) space. Alternatively, use a single pass with a stack to track indices of problematic parentheses, then remove them. The key insight is that we can identify invalid parentheses in two passes: excess closing parentheses are identified going left-to-right, and excess opening parentheses going right-to-left.

## Solution Approaches

### Approach 1: Stack-Based Validation (Recommended)

**Key Insight:** Use a stack to track unmatched parentheses and remove them from the string.

**Algorithm:**
1. Use stack to track indices of unmatched parentheses
2. For each character, push `'('` indices and pop for matching `')'`
3. Remove all indices remaining in stack (unmatched parentheses)
4. Return the modified string

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> stk;
        for(int idx = 0; idx < (int)s.size(); idx++) {
            if(s[idx] == '(') stk.push(idx);
            if(s[idx] == ')') {
                if(!stk.empty() && s[stk.top()] == '(') {
                    stk.pop();
                } else {
                    stk.push(idx);
                }
            }
        }
        string rtn = s;
        while(!stk.empty()) {
            rtn.erase(stk.top(), 1);
            stk.pop();
        }
        return rtn;
    }
};
```

### Approach 2: Two-Pass String Building

**Algorithm:**
1. First pass: Remove unmatched `')'` by tracking balance
2. Second pass: Remove unmatched `'('` by tracking balance in reverse
3. Build result string

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        // First pass: remove unmatched ')'
        string result = "";
        int balance = 0;
        for(char c : s) {
            if(c == '(') {
                balance++;
                result += c;
            } else if(c == ')') {
                if(balance > 0) {
                    balance--;
                    result += c;
                }
                // Skip unmatched ')'
            } else {
                result += c;
            }
        }
        
        // Second pass: remove unmatched '('
        string final_result = "";
        balance = 0;
        for(int i = result.length() - 1; i >= 0; i--) {
            char c = result[i];
            if(c == ')') {
                balance++;
                final_result = c + final_result;
            } else if(c == '(') {
                if(balance > 0) {
                    balance--;
                    final_result = c + final_result;
                }
                // Skip unmatched '('
            } else {
                final_result = c + final_result;
            }
        }
        
        return final_result;
    }
};
```

### Approach 3: Set-Based Tracking

**Algorithm:**
1. Use two passes to identify invalid parentheses
2. Use a set to track indices to remove
3. Build result string excluding tracked indices

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        unordered_set<int> to_remove;
        stack<int> stk;
        
        // Find unmatched parentheses
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '(') {
                stk.push(i);
            } else if(s[i] == ')') {
                if(stk.empty()) {
                    to_remove.insert(i);
                } else {
                    stk.pop();
                }
            }
        }
        
        // Add remaining unmatched '(' to removal set
        while(!stk.empty()) {
            to_remove.insert(stk.top());
            stk.pop();
        }
        
        // Build result string
        string result = "";
        for(int i = 0; i < s.length(); i++) {
            if(to_remove.find(i) == to_remove.end()) {
                result += s[i];
            }
        }
        
        return result;
    }
};
```

## Algorithm Analysis

### Approach Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Stack-Based | O(n) | O(n) | Simple, intuitive | String erasure overhead |
| Two-Pass | O(n) | O(n) | No string modification | More complex logic |
| Set-Based | O(n) | O(n) | Clear separation of concerns | Extra space for set |

### Key Insights

1. **Stack Validation**: Use stack to track parentheses matching
2. **Index Tracking**: Store indices instead of characters for removal
3. **Two-Pass Strategy**: Handle unmatched parentheses in both directions
4. **Minimal Removal**: Remove only the minimum required parentheses

## Implementation Details

### Stack-Based Approach
```cpp
// Track indices of unmatched parentheses
if(s[idx] == '(') stk.push(idx);
if(s[idx] == ')') {
    if(!stk.empty() && s[stk.top()] == '(') {
        stk.pop();  // Match found
    } else {
        stk.push(idx);  // Unmatched ')'
    }
}
```

### String Modification
```cpp
// Remove unmatched parentheses from string
string rtn = s;
while(!stk.empty()) {
    rtn.erase(stk.top(), 1);
    stk.pop();
}
```

## Edge Cases

1. **Empty String**: `""` → `""`
2. **No Parentheses**: `"abc"` → `"abc"`
3. **All Unmatched**: `"))(("` → `""`
4. **Nested Valid**: `"(a(b)c)"` → `"(a(b)c)"`
5. **Mixed Characters**: `"a)b(c)d"` → `"ab(c)d"`

## Follow-up Questions

- What if you needed to return all possible valid strings?
- How would you handle multiple types of brackets?
- What if you needed to minimize the number of removals?
- How would you optimize for very large strings?

## Related Problems

- [LC 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [LC 22: Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [LC 301: Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)

## Optimization Techniques

1. **Stack Index Tracking**: Store indices instead of characters
2. **Single Pass**: Use stack to identify all unmatched parentheses
3. **String Building**: Avoid multiple string modifications
4. **Memory Efficiency**: Use minimal extra space

## Code Quality Notes

1. **Readability**: Stack approach is most intuitive
2. **Performance**: All approaches have O(n) time complexity
3. **Space Efficiency**: O(n) space for stack/set storage
4. **Robustness**: Handles all edge cases correctly

---

*This problem demonstrates the power of stack-based validation for parentheses matching and shows how to efficiently remove invalid characters while preserving valid structure.*
