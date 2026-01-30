---
layout: post
title: "[Easy] 20. Valid Parentheses"
date: 2025-11-04 22:10:14 -0800
categories: leetcode algorithm easy cpp string stack problem-solving
permalink: /posts/2025-11-04-easy-20-valid-parentheses/
tags: [leetcode, easy, string, stack, parentheses, validation]
---

# [Easy] 20. Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Example 4:**
```
Input: s = "([)]"
Output: false
```

**Example 5:**
```
Input: s = "{[]}"
Output: true
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Valid parentheses definition**: What makes parentheses valid? (Assumption: Every opening bracket has matching closing bracket, properly nested - no cross-nesting)

2. **Bracket types**: What bracket types are there? (Assumption: Three types - '()', '[]', '{}' - each must match its own type)

3. **Nesting rules**: Can brackets be nested? (Assumption: Yes - but must be properly nested, e.g., "([])" is valid, "([)]" is not)

4. **Return value**: What should we return? (Assumption: Boolean - true if valid, false otherwise)

5. **Empty string**: What if string is empty? (Assumption: Return true - empty string is valid)

## Solution: Stack-Based Matching

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Use a stack to track opening brackets. When encountering a closing bracket, check if it matches the most recent opening bracket. If stack is empty at the end, all brackets are matched.

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> map = {
            {'}', '{'},
            {']', '['},
            {')', '('}
        };

        for(char c: s) {
            if(c == '{' || c == '[' || c == '(') {
                st.push(c);
            } else {
                if(st.empty() || st.top() != map[c]) return false;
                st.pop();
            }
        }
        return st.empty();
    }
};
```

## How the Algorithm Works

### Key Insight: LIFO (Last In, First Out)

Parentheses must be closed in the reverse order they were opened. This matches the stack's LIFO property perfectly.

### Step-by-Step Example: `s = "([{}])"`

| Step | Char | Action | Stack | Valid? |
|------|------|--------|-------|--------|
| 0 | - | Initialize | [] | - |
| 1 | `(` | Push | `['(']` | - |
| 2 | `[` | Push | `['(', '[']` | - |
| 3 | `{` | Push | `['(', '[', '{']` | - |
| 4 | `}` | Pop: `{` matches | `['(', '[']` | Yes |
| 5 | `]` | Pop: `[` matches | `['(']` | Yes |
| 6 | `)` | Pop: `(` matches | `[]` | Yes |

**Final Check:** Stack is empty → `true`

### Step-by-Step Example: `s = "([)]"`

| Step | Char | Action | Stack | Valid? |
|------|------|--------|-------|--------|
| 1 | `(` | Push | `['(']` | - |
| 2 | `[` | Push | `['(', '[']` | - |
| 3 | `)` | Check: `(` matches | `['[']` | Yes |
| 4 | `]` | Check: `[` matches | `[]` | Yes |

Wait, that's incorrect. Let me recalculate:

| Step | Char | Action | Stack | Valid? |
|------|------|--------|-------|--------|
| 1 | `(` | Push | `['(']` | - |
| 2 | `[` | Push | `['(', '[']` | - |
| 3 | `)` | Check: top is `[`, not `(` | `['(', '[']` | **No** → Return false |

**Final Answer:** `false`

### Visual Representation

```
Valid: "([{}])"
        ( [ { } ] )
        ↑ ↑ ↑ ↑ ↑ ↑
        1 2 3 4 5 6
        
Stack progression:
1: ['(']
2: ['(', '[']
3: ['(', '[', '{']
4: ['(', '[']      (matched {})
5: ['(']           (matched [])
6: []              (matched ())
Result: true ✓

Invalid: "([)]"
          ( [ ) ]
          ↑ ↑ ↑ ↑
          1 2 3 4
          
Stack progression:
1: ['(']
2: ['(', '[']
3: ['(', '[']      (trying to match ) with [, fails!)
Result: false ✗
```

## Key Insights

1. **Stack for LIFO**: Opening brackets must close in reverse order
2. **Map for Matching**: Use hash map to map closing to opening brackets
3. **Empty Stack Check**: All brackets matched if stack is empty at end
4. **Early Return**: Return false immediately on mismatch or empty stack with closing bracket

## Algorithm Breakdown

### 1. Initialize Stack and Map
```cpp
stack<char> st;
unordered_map<char, char> map = {
    {'}', '{'},
    {']', '['},
    {')', '('}
};
```
- **Stack**: Stores opening brackets
- **Map**: Maps closing brackets to their corresponding opening brackets

### 2. Process Opening Brackets
```cpp
if(c == '{' || c == '[' || c == '(') {
    st.push(c);
}
```
- Push opening brackets onto stack
- They will be matched later when closing brackets appear

### 3. Process Closing Brackets
```cpp
else {
    if(st.empty() || st.top() != map[c]) return false;
    st.pop();
}
```
- **Check if stack is empty**: No opening bracket to match
- **Check if top matches**: Most recent opening bracket must match current closing bracket
- **Pop if matched**: Remove the matched opening bracket

### 4. Final Validation
```cpp
return st.empty();
```
- If stack is empty, all brackets were matched
- If stack has remaining elements, some opening brackets were never closed

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Single pass through string, each operation is O(1) |
| **Space** | O(n) - Stack can hold at most n/2 opening brackets in worst case |

## Alternative Approaches

### Approach 1: Without Hash Map (Explicit Checks)

```cpp
bool isValid(string s) {
    stack<char> st;
    
    for(char c: s) {
        if(c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if(st.empty()) return false;
            
            char top = st.top();
            st.pop();
            
            if((c == ')' && top != '(') ||
               (c == ']' && top != '[') ||
               (c == '}' && top != '{')) {
                return false;
            }
        }
    }
    
    return st.empty();
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

### Approach 2: Using String as Stack

```cpp
bool isValid(string s) {
    string stack = "";
    
    for(char c: s) {
        if(c == '(' || c == '[' || c == '{') {
            stack += c;
        } else {
            if(stack.empty()) return false;
            
            char last = stack.back();
            stack.pop_back();
            
            if((c == ')' && last != '(') ||
               (c == ']' && last != '[') ||
               (c == '}' && last != '{')) {
                return false;
            }
        }
    }
    
    return stack.empty();
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

**Note:** This is less efficient due to string operations, but uses less code.

### Approach 3: Counter-Based (Only for Single Type)

```cpp
// Only works for single bracket type like "()"
bool isValid(string s) {
    int count = 0;
    for(char c: s) {
        if(c == '(') count++;
        else count--;
        if(count < 0) return false;
    }
    return count == 0;
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Limitation:** Doesn't work for multiple bracket types like `"([)]"`.

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Stack + Map** | O(n) | O(n) | Clean, extensible | Slight overhead |
| **Stack + Explicit** | O(n) | O(n) | No map needed | More verbose |
| **String Stack** | O(n) | O(n) | Simple code | Less efficient |
| **Counter** | O(n) | O(1) | Space optimal | Only single type |

## Edge Cases

1. **Empty string**: `""` → `true` (valid by definition)
2. **Single bracket**: `"("` or `")"` → `false`
3. **Only opening**: `"((("` → `false`
4. **Only closing**: `")))"` → `false`
5. **Nested valid**: `"([{}])"` → `true`
6. **Interleaved invalid**: `"([)]"` → `false`
7. **Mixed valid**: `"()[]{}"` → `true`

## Common Mistakes

1. **Not checking stack empty**: Forgetting to check `st.empty()` before `st.top()`
2. **Wrong map direction**: Mapping opening → closing instead of closing → opening
3. **Not returning false immediately**: Continuing after finding a mismatch
4. **Forgetting final check**: Not checking if stack is empty at the end
5. **Using wrong comparison**: Comparing `st.top() == c` instead of `st.top() == map[c]`

## Detailed Example Walkthrough

### Example 1: `s = "([{}])"`

```
Step 0: Initialize
  st = []
  map = {')': '(', ']': '[', '}': '{'}

Step 1: c = '('
  Opening bracket → push
  st = ['(']

Step 2: c = '['
  Opening bracket → push
  st = ['(', '[']

Step 3: c = '{'
  Opening bracket → push
  st = ['(', '[', '{']

Step 4: c = '}'
  Closing bracket → check
  st.empty()? No
  st.top() = '{'
  map['}'] = '{'
  '{' == '{'? Yes → pop
  st = ['(', '[']

Step 5: c = ']'
  Closing bracket → check
  st.empty()? No
  st.top() = '['
  map[']'] = '['
  '[' == '['? Yes → pop
  st = ['(']

Step 6: c = ')'
  Closing bracket → check
  st.empty()? No
  st.top() = '('
  map[')'] = '('
  '(' == '('? Yes → pop
  st = []

Final: st.empty()? Yes → return true ✓
```

### Example 2: `s = "([)]"`

```
Step 0: Initialize
  st = []

Step 1: c = '('
  Opening bracket → push
  st = ['(']

Step 2: c = '['
  Opening bracket → push
  st = ['(', '[']

Step 3: c = ')'
  Closing bracket → check
  st.empty()? No
  st.top() = '['
  map[')'] = '('
  '[' == '('? No → return false ✗
```

## Why Stack Works

### LIFO Property

Parentheses matching requires **Last In, First Out**:
- Most recent opening bracket must match the next closing bracket
- Stack naturally provides LIFO behavior

### Example: `"([{}])"`

```
Opening order:  ( [ {
Closing order:    } ] )
                  ↑
              Must close in reverse order
```

### Counter Example: `"([)]"`

```
Opening order:  ( [
Closing order:    ) ]
                  ↑
              Wrong order! Can't close ')' before ']'
```

## Optimization Tips

### Early Exit
Already optimized - we return false immediately on mismatch.

### Memory Optimization
For very large strings, consider using a string as stack (if your use case allows) to potentially reduce allocations.

### Branch Prediction
The hash map lookup is very fast, but explicit checks might be slightly faster due to branch prediction:
```cpp
if(c == ')') {
    if(st.empty() || st.top() != '(') return false;
    st.pop();
}
```

## Related Problems

- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - Generate all valid parentheses
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) - Find longest valid substring
- [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) - Remove minimum to make valid
- [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) - Remove invalid characters
- [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) - Add minimum to balance

## Pattern Recognition

This problem demonstrates the **Stack for Matching** pattern:
- Use stack when you need to match elements in reverse order
- Perfect for nested structures (parentheses, brackets, tags)
- LIFO property naturally handles nested matching

**Key Insight:**
- Opening brackets → push
- Closing brackets → pop and verify match
- Stack empty at end → all matched

**Applications:**
- HTML/XML tag validation
- Expression evaluation
- Function call tracking
- Nested structure parsing

## Code Quality Notes

1. **Readability**: Hash map makes code clean and extensible
2. **Efficiency**: Optimal O(n) time and space
3. **Correctness**: Handles all edge cases properly
4. **Maintainability**: Easy to add new bracket types

## Extending to More Bracket Types

The solution easily extends to other bracket types:

```cpp
unordered_map<char, char> map = {
    {'}', '{'},
    {']', '['},
    {')', '('},
    {'>', '<'}  // Add new type
};

// Check also includes '<'
if(c == '{' || c == '[' || c == '(' || c == '<') {
    st.push(c);
}
```

---

*This is a fundamental stack problem that demonstrates the LIFO property perfectly. It's an excellent introduction to stack-based algorithms and pattern matching.*

