---
layout: post
title: "[Hard] 32. Longest Valid Parentheses"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm hard cpp string dynamic-programming stack problem-solving
permalink: /posts/2025-11-24-hard-32-longest-valid-parentheses/
tags: [leetcode, hard, string, dynamic-programming, stack, two-pointers, greedy]
---

# [Hard] 32. Longest Valid Parentheses

Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

## Examples

**Example 1:**
```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

**Example 2:**
```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

**Example 3:**
```
Input: s = ""
Output: 0
Explanation: Empty string has no valid parentheses.
```

**Example 4:**
```
Input: s = "((()))"
Output: 6
Explanation: The entire string is a valid parentheses substring.
```

## Constraints

- `0 <= s.length <= 3 * 10^4`
- `s[i]` is `'('`, or `')'`.

## Solution Approaches

This problem requires finding the longest valid parentheses substring. A valid parentheses substring must have matching opening and closing parentheses.

### Solution 1: Dynamic Programming

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Use dynamic programming to track the length of the longest valid parentheses ending at each position.

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int maxCount = 0;
        int len = s.length();
        vector<int> dp(len);
        
        for (int i = 1; i < len; i++) {
            if (s[i] == ')') {
                // Case 1: Pattern "()" - simple match
                if (s[i - 1] == '(') {
                    dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
                } 
                // Case 2: Pattern "))" - nested or consecutive valid substrings
                else if (i - dp[i - 1] > 0 && s[i - dp[i - 1] - 1] == '(') {
                    dp[i] = dp[i - 1] + 
                        ((i - dp[i - 1]) >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2;
                }
                maxCount = max(maxCount, dp[i]);
            }
        }
        
        return maxCount;
    }
};
```

**How it works:**
1. `dp[i]` represents the length of the longest valid parentheses substring ending at index `i`
2. For each `')'` at position `i`:
   - **Case 1**: If previous character is `'('`, we have a simple match `"()"`. Add 2 plus any valid substring before it.
   - **Case 2**: If previous character is `')'`, check if there's a matching `'('` before the valid substring ending at `i-1`. If found, combine lengths.
3. Track the maximum length seen so far.

### Solution 2: Two-Pass Greedy (Space Optimized)

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Use two passes (left-to-right and right-to-left) to find the longest valid substring without extra space.

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int left = 0, right = 0, maxLen = 0;
        int len = s.length();
        
        // Left to right pass
        for (int i = 0; i < len; i++) {
            if (s[i] == '(') left++;
            else right++;
            
            if (left == right) {
                maxLen = max(maxLen, 2 * right);
            } else if (right > left) {
                // Invalid: more closing than opening, reset
                left = right = 0;
            }
        }
        
        // Right to left pass
        left = right = 0;
        for (int i = len - 1; i >= 0; i--) {
            if (s[i] == '(') left++;
            else right++;
            
            if (left == right) {
                maxLen = max(maxLen, 2 * left);
            } else if (left > right) {
                // Invalid: more opening than closing, reset
                left = right = 0;
            }
        }
        
        return maxLen;
    }
};
```

**How it works:**
1. **Left-to-right pass**: Count opening and closing parentheses. When counts are equal, we have a valid substring. If closing > opening, reset (invalid).
2. **Right-to-left pass**: Same logic but reversed. Catches cases where left-to-right misses valid substrings (e.g., `"(()"`).
3. The two passes together ensure we find all valid substrings.

## How the Algorithms Work

### Solution 1: Dynamic Programming Breakdown

**Key Insight:** `dp[i]` = length of longest valid parentheses substring ending at index `i`.

**Case 1: Pattern `"()"`**
```
Index:  i-2  i-1  i
String:  ?    (   )
dp:      x    0   2+x

If s[i-1] == '(' and s[i] == ')':
  dp[i] = dp[i-2] + 2
```

**Case 2: Pattern `"))"`**
```
Index:  i-dp[i-1]-2  ...  i-dp[i-1]-1  ...  i-1  i
String:      ?            (            ...   )   )
dp:          y            0            ...   x   x+y+2

If s[i-dp[i-1]-1] == '(':
  dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
```

### Step-by-Step Example: `s = ")()())"`

**DP Solution:**
```
s = ")()())"
    0123456

i=0: ')' → dp[0] = 0
i=1: '(' → dp[1] = 0
i=2: ')' → Case 1: s[1]=='(' → dp[2] = dp[0] + 2 = 0 + 2 = 2
i=3: '(' → dp[3] = 0
i=4: ')' → Case 1: s[3]=='(' → dp[4] = dp[2] + 2 = 2 + 2 = 4
i=5: ')' → Case 2: Check s[5-dp[4]-1] = s[0] = ')' → No match
           dp[5] = 0

maxCount = max(0, 0, 2, 0, 4, 0) = 4
```

**Two-Pass Solution:**
```
Left-to-right: ")()())"
i=0: ')' → left=0, right=1 → right>left → reset → left=0, right=0
i=1: '(' → left=1, right=0
i=2: ')' → left=1, right=1 → equal → maxLen = max(0, 2*1) = 2
i=3: '(' → left=2, right=1
i=4: ')' → left=2, right=2 → equal → maxLen = max(2, 2*2) = 4
i=5: ')' → left=2, right=3 → right>left → reset → left=0, right=0

Right-to-left: ")()())"
i=5: ')' → left=0, right=1
i=4: ')' → left=0, right=2 → right>left → reset → left=0, right=0
i=3: '(' → left=1, right=0
i=2: ')' → left=1, right=1 → equal → maxLen = max(4, 2*1) = 4
i=1: '(' → left=2, right=1 → left>right → reset → left=0, right=0
i=0: ')' → left=0, right=1

Final: maxLen = 4
```

### Step-by-Step Example: `s = "(()"`

**DP Solution:**
```
s = "(()"
    012

i=0: '(' → dp[0] = 0
i=1: '(' → dp[1] = 0
i=2: ')' → Case 2: Check s[2-dp[1]-1] = s[1] = '(' → Match!
           dp[2] = dp[1] + dp[2-dp[1]-2] + 2
                 = 0 + dp[-1] + 2
                 = 0 + 0 + 2 = 2

maxCount = 2
```

**Two-Pass Solution:**
```
Left-to-right: "(()"
i=0: '(' → left=1, right=0
i=1: '(' → left=2, right=0
i=2: ')' → left=2, right=1 → left>right → continue
maxLen = 0 (no equal counts)

Right-to-left: "(()"
i=2: ')' → left=0, right=1
i=1: '(' → left=1, right=1 → equal → maxLen = max(0, 2*1) = 2
i=0: '(' → left=2, right=1 → left>right → reset

Final: maxLen = 2
```

## Algorithm Breakdown

### Solution 1: Dynamic Programming

**Base Case:**
- `dp[0] = 0` (no valid substring ending at index 0 if it's not part of a match)

**Case 1: Simple Match `"()"`**
```cpp
if (s[i - 1] == '(') {
    dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
}
```
- If previous character is `'('`, we have a match
- Add 2 for the current match
- Add any valid substring before `i-2`

**Case 2: Nested/Consecutive `"))"`**
```cpp
else if (i - dp[i - 1] > 0 && s[i - dp[i - 1] - 1] == '(') {
    dp[i] = dp[i - 1] + 
        ((i - dp[i - 1]) >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2;
}
```
- Check if there's a matching `'('` before the valid substring ending at `i-1`
- If found, combine:
  - Length of valid substring ending at `i-1`: `dp[i-1]`
  - Length of valid substring before the match: `dp[i-dp[i-1]-2]`
  - Current match: `2`

### Solution 2: Two-Pass Greedy

**Left-to-Right Pass:**
```cpp
for (int i = 0; i < len; i++) {
    if (s[i] == '(') left++;
    else right++;
    
    if (left == right) {
        maxLen = max(maxLen, 2 * right);
    } else if (right > left) {
        left = right = 0;  // Reset: invalid state
    }
}
```
- Count opening and closing parentheses
- When equal, we have a valid substring
- If closing > opening, reset (can't form valid substring)

**Right-to-Left Pass:**
```cpp
for (int i = len - 1; i >= 0; i--) {
    if (s[i] == '(') left++;
    else right++;
    
    if (left == right) {
        maxLen = max(maxLen, 2 * left);
    } else if (left > right) {
        left = right = 0;  // Reset: invalid state
    }
}
```
- Same logic but reversed
- Catches cases where left-to-right misses valid substrings

**Why Two Passes?**
- Left-to-right misses cases like `"(()"` where we never get `left == right`
- Right-to-left catches these cases
- Together, they find all valid substrings

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Dynamic Programming** | O(n) | O(n) | Clear logic, handles all cases | Extra space |
| **Two-Pass Greedy** | O(n) | O(1) | Optimal space, simple | Two passes needed |

## Edge Cases

1. **Empty string**: Returns 0
2. **No valid parentheses**: Returns 0 (e.g., `"))"` or `"(("`)
3. **All valid**: Returns string length (e.g., `"()()()"`)
4. **Nested valid**: Returns string length (e.g., `"((()))"`)
5. **Single character**: Returns 0 (no pair possible)

## Key Insights

1. **DP State Definition**: `dp[i]` = longest valid substring ending at `i`
2. **Two Cases**: Simple match `"()"` and nested/consecutive `"))"`
3. **Greedy Approach**: Count parentheses and reset when invalid
4. **Two Passes**: Needed to catch all valid substrings

## Common Mistakes

1. **Missing Case 2 in DP**: Forgetting to handle nested/consecutive valid substrings
2. **Index Out of Bounds**: Not checking `i - dp[i-1] > 0` before accessing
3. **Single Pass Greedy**: Missing valid substrings that don't balance in one direction
4. **Wrong Reset Condition**: Resetting at wrong times in greedy approach

## Alternative Approaches

### Approach 3: Stack-Based

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk;
        stk.push(-1);  // Base for calculation
        int maxLen = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else {
                stk.pop();
                if (stk.empty()) {
                    stk.push(i);  // New base
                } else {
                    maxLen = max(maxLen, i - stk.top());
                }
            }
        }
        
        return maxLen;
    }
};
```

**How it works:**
- Use stack to track indices of unmatched `'('`
- When `')'` is found, pop and calculate length
- If stack is empty after pop, push current index as new base

## Related Problems

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Check if entire string is valid
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - Generate all valid combinations
- [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) - Remove minimum to make valid
- [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) - Minimum additions needed

## Pattern Recognition

This problem demonstrates:

1. **Dynamic Programming with String Matching**: Building solution incrementally
2. **Greedy with Two Passes**: Ensuring all cases are covered
3. **Parentheses Matching**: Classic pattern in string problems

## Real-World Applications

1. **Code Parsing**: Validating syntax in compilers
2. **Expression Evaluation**: Checking balanced expressions
3. **Text Processing**: Finding well-formed structures
4. **Algorithm Design**: Understanding DP and greedy patterns

## Why Two Solutions?

**Use DP when:**
- Need to understand the problem structure clearly
- Want to see all intermediate results
- Space is not a concern

**Use Two-Pass Greedy when:**
- Space is constrained
- Need O(1) space solution
- Want simpler code (though requires two passes)

---

*This problem demonstrates both dynamic programming and greedy approaches to solve the same problem, with different space-time trade-offs.*

