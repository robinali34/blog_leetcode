---
layout: post
title: "[Medium] 394. Decode String"
date: 2025-10-19 17:24:19 -0700
categories: leetcode algorithm medium cpp stack string-processing problem-solving
---
Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there won't be input like `3a` or `2[4]`.

## Examples

**Example 1:**
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Explanation: 
- "3[a]" decodes to "aaa"
- "2[bc]" decodes to "bcbc"
- Combined: "aaabcbc"
```

**Example 2:**
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
Explanation: 
- "3[a2[c]]" decodes to "accaccacc"
- Inner "2[c]" decodes to "cc"
- Outer "3[a...]" decodes to "accaccacc"
```

**Example 3:**
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Explanation: 
- "2[abc]" decodes to "abcabc"
- "3[cd]" decodes to "cdcdcd"
- "ef" remains as "ef"
- Combined: "abcabccdcdcdef"
```

## Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'['` and `']'`.
- `s` is a valid encoded string, that is always possible to decode.
- All the integers in `s` are in the range `[1, 300]`.

## Thinking Process

1. **Two stacks:** One for counts, one for strings
1. **Current string:** Maintains the string being built

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
| **Monotonic stack** *(this problem)* | $O(n)$ | $O(n)$ | Next greater/smaller element |
| Parentheses matching | $O(n)$ | $O(n)$ | Push open, pop on close |
| Expression evaluation | $O(n)$ | $O(n)$ | Operand + operator stacks |
| Stack simulation | $O(n)$ | $O(n)$ | Process in LIFO order |

## Solution

**Time Complexity:** O(n) where n is the length of the decoded string  
**Space Complexity:** O(n) for the stack and result string

Use two stacks to handle nested encoded strings: one for counts and one for strings.

```cpp
class Solution {
public:
    string decodeString(string s) {
        stack<int> counts;
        stack<string> strings;
        string curr;
        int k = 0;
        
        for(auto ch: s) {
            if(isdigit(ch)) {
                k = k * 10 + ch - '0';
            } else if(ch == '[') {
                counts.push(k);
                strings.push(curr);
                curr = "";
                k = 0;
            } else if(ch == ']') {
                string decode = strings.top();
                strings.pop();
                int count = counts.top();
                while(count--) decode += curr;
                counts.pop();
                curr = decode;
            } else {
                curr += ch;
            }
        }
        return curr;
    }
};
```

### Solution Explanation
**Key Insight:** Use two stacks to handle nested encoded strings and maintain the current string being built.

**Steps:**
1. **Process each character** in the input string
2. **For digits:** Build the count number
3. **For '[':** Push count and current string to stacks, reset for nested processing
4. **For ']':** Pop from stacks, repeat current string, and update current string
5. **For letters:** Add to current string
6. **Return final** decoded string

## Step-by-Step Example

### Example: `s = "3[a2[c]]"`

| Character | Action | Counts Stack | Strings Stack | Current String | Explanation |
|-----------|--------|--------------|---------------|----------------|-------------|
| '3' | Build count | [] | [] | "" | k = 3 |
| '[' | Push to stacks | [3] | [""] | "" | Save state, reset |
| 'a' | Add to current | [3] | [""] | "a" | Add letter |
| '2' | Build count | [3] | [""] | "a" | k = 2 |
| '[' | Push to stacks | [3,2] | ["","a"] | "" | Save state, reset |
| 'c' | Add to current | [3,2] | ["","a"] | "c" | Add letter |
| ']' | Decode | [3] | [""] | "cc" | Repeat "c" 2 times |
| ']' | Decode | [] | [] | "accaccacc" | Repeat "cc" 3 times |

**Final result:** `"accaccacc"`

## Algorithm Breakdown

### Character Processing:
```cpp
for(auto ch: s) {
    if(isdigit(ch)) {
        k = k * 10 + ch - '0';
    } else if(ch == '[') {
        counts.push(k);
        strings.push(curr);
        curr = "";
        k = 0;
    } else if(ch == ']') {
        string decode = strings.top();
        strings.pop();
        int count = counts.top();
        while(count--) decode += curr;
        counts.pop();
        curr = decode;
    } else {
        curr += ch;
    }
}
```

**Process:**
1. **Digit:** Build multi-digit count
2. **'[':** Save current state to stacks
3. **']':** Decode by repeating current string
4. **Letter:** Add to current string

### Stack Operations:

**Push Operation (on '['):**
```cpp
counts.push(k);
strings.push(curr);
curr = "";
k = 0;
```

**Pop Operation (on ']'):**
```cpp
string decode = strings.top();
strings.pop();
int count = counts.top();
while(count--) decode += curr;
counts.pop();
curr = decode;
```

### Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Character processing | O(n) | O(n) |
| Stack operations | O(n) | O(n) |
| String concatenation | O(m) | O(m) |
| **Total** | **O(n + m)** | **O(n + m)** |

Where n is the input length and m is the decoded string length.

## Detailed Example Walkthrough

### Example: `s = "2[abc]3[cd]ef"`

| Character | Action | Counts Stack | Strings Stack | Current String | Explanation |
|-----------|--------|--------------|---------------|----------------|-------------|
| '2' | Build count | [] | [] | "" | k = 2 |
| '[' | Push to stacks | [2] | [""] | "" | Save state |
| 'a' | Add to current | [2] | [""] | "a" | Add letter |
| 'b' | Add to current | [2] | [""] | "ab" | Add letter |
| 'c' | Add to current | [2] | [""] | "abc" | Add letter |
| ']' | Decode | [] | [] | "abcabc" | Repeat "abc" 2 times |
| '3' | Build count | [] | [] | "abcabc" | k = 3 |
| '[' | Push to stacks | [3] | ["abcabc"] | "" | Save state |
| 'c' | Add to current | [3] | ["abcabc"] | "c" | Add letter |
| 'd' | Add to current | [3] | ["abcabc"] | "cd" | Add letter |
| ']' | Decode | [] | [] | "abcabccdcdcd" | Repeat "cd" 3 times |
| 'e' | Add to current | [] | [] | "abcabccdcdcde" | Add letter |
| 'f' | Add to current | [] | [] | "abcabccdcdcdef" | Add letter |

**Final result:** `"abcabccdcdcdef"`

## Common Mistakes

1. **Single letter:** `s = "a"` → `"a"`
2. **Single repetition:** `s = "2[a]"` → `"aa"`
3. **No nesting:** `s = "3[a]2[b]"` → `"aaabb"`
4. **Deep nesting:** `s = "2[3[4[a]]]"` → `"aaaaaaaaaaaaaaaaaaaaaaaa"`

1. **Wrong count handling:** Not building multi-digit numbers correctly
2. **Stack order:** Pushing/popping in wrong order
3. **String concatenation:** Not handling nested repetitions properly
4. **Edge cases:** Not handling single characters or no brackets

## Related Problems

- [71. Simplify Path](https://www.leetcode.com/problems/simplify-path/)
- [150. Evaluate Reverse Polish Notation](https://www.leetcode.com/problems/evaluate-reverse-polish-notation/)
- [224. Basic Calculator](https://www.leetcode.com/problems/basic-calculator/)
- [227. Basic Calculator II](https://www.leetcode.com/problems/basic-calculator-ii/)

## Why This Solution Works

### Stack-Based Approach:
1. **Two stacks:** Efficiently handle nested structures
2. **State preservation:** Save current state when entering brackets
3. **State restoration:** Restore state when exiting brackets
4. **Arbitrary nesting:** Handle any level of nesting

### String Processing:
1. **Character by character:** Process input incrementally
2. **Count building:** Handle multi-digit numbers
3. **String repetition:** Efficiently repeat strings
4. **Memory efficient:** Build result incrementally

### Key Algorithm Properties:
1. **Correctness:** Always produces valid decoded string
2. **Efficiency:** O(n + m) time complexity
3. **Simplicity:** Easy to understand and implement
4. **Scalability:** Handles arbitrary nesting levels

## References

- [LC 394: Decode String on LeetCode](https://www.leetcode.com/problems/decode-string/)
- [LeetCode Discuss — LC 394: Decode String](https://www.leetcode.com/problems/decode-string/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/decode-string/editorial/) *(may require premium)*

## Key Takeaways

### Stack-Based Approach:
1. **Two stacks:** One for counts, one for strings
2. **State preservation:** Save current state when entering nested brackets
3. **State restoration:** Restore state when exiting nested brackets
4. **Efficient processing:** Handle arbitrary nesting levels

### String Building:
1. **Current string:** Maintains the string being built
2. **Repetition:** Repeat current string by count
3. **Concatenation:** Build final result incrementally
4. **Memory efficient:** Process character by character
