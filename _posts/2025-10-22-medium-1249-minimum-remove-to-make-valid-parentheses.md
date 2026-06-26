---
layout: post
title: "[Medium] 1249. Minimum Remove to Make Valid Parentheses"
date: 2025-10-22 13:30:00 -0700
categories: leetcode medium string stack
permalink: /posts/2025-10-22-medium-1249-minimum-remove-to-make-valid-parentheses/
tags: [leetcode, medium, string, stack, parentheses, validation]
---
**Difficulty:** Medium  
**Category:** String, Stack  
**Companies:** Amazon, Facebook, Microsoft, Google


Given a string `s` of `'('`, `')'` and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting parentheses string is valid and return **any** valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

## Examples
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

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'('`, `')'`, or lowercase English letter.

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

### Solution Explanation

**Approach:** Parentheses matching (this problem)

**Key idea:** Difficulty:** Medium

**How the code works:**
**Difficulty:** Medium
**Category:** String, Stack
- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in $O(n)$.

**Walkthrough** — input `s = "lee(t(c)o)de)"`, expected output `"lee(t(c)o)de"`:

"lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [LC 20: Valid Parentheses](https://www.leetcode.com/problems/valid-parentheses/)
- [LC 22: Generate Parentheses](https://www.leetcode.com/problems/generate-parentheses/)
- [LC 301: Remove Invalid Parentheses](https://www.leetcode.com/problems/remove-invalid-parentheses/)

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

## Key Takeaways

- **Pattern:** Parentheses matching (this problem)
- Difficulty:** Medium
- Category:** String, Stack

## References

- [LC 1249: Minimum Remove to Make Valid Parentheses on LeetCode](https://www.leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)
- [LeetCode Discuss — LC 1249: Minimum Remove to Make Valid Parentheses](https://www.leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-remove-to-make-valid-parentheses/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)

## Thinking Process

**Difficulty:** Medium

**Category:** String, Stack

- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in $O(n)$.



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
| Monotonic stack | $O(n)$ | $O(n)$ | Next greater/smaller element |
| **Parentheses matching** *(this problem)* | $O(n)$ | $O(n)$ | Push open, pop on close |
| Expression evaluation | $O(n)$ | $O(n)$ | Operand + operator stacks |
| Stack simulation | $O(n)$ | $O(n)$ | Process in LIFO order |
