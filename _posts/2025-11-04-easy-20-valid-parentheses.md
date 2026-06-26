---
layout: post
title: "[Easy] 20. Valid Parentheses"
date: 2025-11-04 22:10:14 -0800
categories: leetcode algorithm easy cpp string stack problem-solving
permalink: /posts/2025-11-04-easy-20-valid-parentheses/
tags: [leetcode, easy, string, stack, parentheses, validation]
---
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

## Thinking Process

1. **Stack for LIFO**: Opening brackets must close in reverse order

- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in O(n).



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Stack</text>

  <rect x="100" y="30" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="46" text-anchor="middle" font-size="10">top</text>
  <rect x="100" y="54" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="100" y="78" width="80" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="200" y="70" font-size="11" fill="#6B6560">push / pop</text>
  <path d="M90 42v60" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="115" text-anchor="middle" font-size="11" fill="#6B6560">LIFO — monotonic stack scans array</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Monotonic stack | O(n) | O(n) | Next greater/smaller element |
| **Parentheses matching** *(this problem)* | O(n) | O(n) | Push open, pop on close |
| Expression evaluation | O(n) | O(n) | Operand + operator stacks |
| Stack simulation | O(n) | O(n) | Process in LIFO order |

## Solution

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

### Solution Explanation

**Approach:** Parentheses matching (this problem)

**Key idea:** 1. **Stack for LIFO**: Opening brackets must close in reverse order

**How the code works:**
1. **Stack for LIFO**: Opening brackets must close in reverse order
- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in O(n).

**Walkthrough** — input `s = "()"`, expected output `true`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Single pass through string, each operation is O(1) |
| **Space** | O(n) - Stack can hold at most n/2 opening brackets in worst case |
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

### Complexity
| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Single pass through string, each operation is O(1) |
| **Space** | O(n) - Stack can hold at most n/2 opening brackets in worst case |

## Common Mistakes

1. **Empty string**: `""` → `true` (valid by definition)
2. **Single bracket**: `"("` or `")"` → `false`
3. **Only opening**: `"((("` → `false`
4. **Only closing**: `")))"` → `false`
5. **Nested valid**: `"([{}])"` → `true`
6. **Interleaved invalid**: `"([)]"` → `false`
7. **Mixed valid**: `"()[]{}"` → `true`

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

- [22. Generate Parentheses](https://www.leetcode.com/problems/generate-parentheses/) - Generate all valid parentheses
- [32. Longest Valid Parentheses](https://www.leetcode.com/problems/longest-valid-parentheses/) - Find longest valid substring
- [301. Remove Invalid Parentheses](https://www.leetcode.com/problems/remove-invalid-parentheses/) - Remove minimum to make valid
- [1249. Minimum Remove to Make Valid Parentheses](https://www.leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) - Remove invalid characters
- [1541. Minimum Insertions to Balance a Parentheses String](https://www.leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) - Add minimum to balance

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

## Key Takeaways

1. **Stack for LIFO**: Opening brackets must close in reverse order
2. **Map for Matching**: Use hash map to map closing to opening brackets
3. **Empty Stack Check**: All brackets matched if stack is empty at end
4. **Early Return**: Return false immediately on mismatch or empty stack with closing bracket

## References

- [LC 20: Valid Parentheses on LeetCode](https://www.leetcode.com/problems/valid-parentheses/)
- [LeetCode Discuss — LC 20: Valid Parentheses](https://www.leetcode.com/problems/valid-parentheses/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/valid-parentheses/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
