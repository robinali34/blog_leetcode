---
layout: post
title: "[Easy] 844. Backspace String Compare"
date: 2026-01-12 00:00:00 -0700
categories: [leetcode, easy, string, two-pointers, stack]
permalink: /2026/01/12/easy-844-backspace-string-compare/
tags: [leetcode, easy, string, two-pointers, stack, simulation]
---
Given two strings `s` and `t`, return `true` *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

## Thinking Process

1. **Backwards Processing**: Processing from right to left handles backspaces naturally

- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in $O(n)$.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Monotonic stack** *(this problem)* | $O(n)$ | $O(n)$ | Next greater/smaller element |
| Parentheses matching | $O(n)$ | $O(n)$ | Push open, pop on close |
| Expression evaluation | $O(n)$ | $O(n)$ | Operand + operator stacks |
| Stack simulation | $O(n)$ | $O(n)$ | Process in LIFO order |

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

## Common Mistakes

1. **All backspaces**: `s = "###"`, `t = "##"` → both become `""`, return `true`
2. **Empty strings**: `s = ""`, `t = ""` → return `true`
3. **Backspace at start**: `s = "#a"`, `t = "a"` → both become `"a"`, return `true`
4. **Different lengths**: `s = "a#b"`, `t = "b"` → both become `"b"`, return `true`
5. **No backspaces**: `s = "abc"`, `t = "abc"` → return `true`

1. **Wrong skip logic**: Not properly handling consecutive backspaces
2. **Index errors**: Off-by-one errors when moving pointers
3. **Missing break**: Not breaking from inner loops when finding actual character
4. **Wrong comparison**: Comparing before processing all backspaces
5. **Return condition**: Not checking `i == j` correctly (both should be `-1`)

## Related Problems

- [LC 1047: Remove All Adjacent Duplicates In String](https://www.leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) - Similar stack-based pattern
- [LC 1209: Remove All Adjacent Duplicates in String II](https://www.leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) - K duplicates version
- [LC 1544: Make The String Great](https://www.leetcode.com/problems/make-the-string-great/) - Similar character removal pattern

## Key Takeaways

1. **Backwards Processing**: Processing from right to left handles backspaces naturally
2. **Skip Counter**: Tracks characters to skip due to backspaces
3. **Character Matching**: Only compares actual characters after handling backspaces
4. **Space Efficiency**: Two-pointer approach achieves O(1) space

## References

- [LC 844: Backspace String Compare on LeetCode](https://www.leetcode.com/problems/backspace-string-compare/)
- [LeetCode Discuss — LC 844: Backspace String Compare](https://www.leetcode.com/problems/backspace-string-compare/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/backspace-string-compare/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
