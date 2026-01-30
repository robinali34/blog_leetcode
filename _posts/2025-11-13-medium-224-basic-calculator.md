---
layout: post
title: "[Medium] 224. Basic Calculator"
date: 2025-11-13 19:33:45 -0800
categories: leetcode algorithm medium cpp string stack expression-evaluation problem-solving
permalink: /posts/2025-11-13-medium-224-basic-calculator/
tags: [leetcode, medium, string, stack, calculator, expression-evaluation, parentheses]
---

# [Medium] 224. Basic Calculator

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

## Examples

**Example 1:**
```
Input: s = "1 + 1"
Output: 2
```

**Example 2:**
```
Input: s = " 2-1 + 2 "
Output: 3
```

**Example 3:**
```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
- `s` represents a valid expression.
- `'+'` is not used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).
- `'-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Expression format**: What operations are supported? (Assumption: Addition '+', subtraction '-', parentheses '()' - no multiplication/division)

2. **Unary operators**: How should we handle unary operators? (Assumption: '-' can be unary (negative numbers), '+' cannot be unary)

3. **Parentheses**: How should parentheses be handled? (Assumption: Standard precedence - evaluate inner parentheses first)

4. **Return value**: What should we return? (Assumption: Integer result of evaluating the expression)

5. **Whitespace**: Should we ignore whitespace? (Assumption: Yes - spaces can be ignored)

## Solution 1: Stack-Based Approach

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Stack for parentheses

Use a stack to handle parentheses. When encountering `(`, push current result and sign onto stack. When encountering `)`, pop sign and previous result, then combine.

**Note:** Using `switch` instead of multiple `if-else` statements is cleaner and more efficient when handling multiple character cases, as the compiler can optimize switch statements better. The `switch` executes for all characters, but digits are handled before the switch, and non-operator characters (like spaces) simply fall through without matching any case.

```cpp
class Solution {
public:
    int calculate(string s) {
        const int len = s.length();
        if(len == 0) return 0;

        int rtn = 0, last = 0, curr = 0, sign = 1;
        stack<int> stk;

        for(int i = 0; i < len; i++) {
            char ch = s[i];
            if(isdigit(ch)) {
                curr = (10 * curr) + (ch - '0');
            }
            switch (ch) {
                case '+':
                    rtn += sign * curr;
                    sign = 1;
                    curr = 0;
                    break;
                case '-':
                    rtn += sign * curr;
                    sign = -1;
                    curr = 0;
                    break;
                case '(':
                    stk.push(rtn);
                    stk.push(sign);
                    sign = 1;
                    rtn = 0;
                    break;
                case ')':
                    rtn += sign * curr;
                    rtn *= stk.top();
                    stk.pop();
                    rtn += stk.top();
                    stk.pop();
                    curr = 0;
                    break;
            }
        }
        return rtn + (sign * curr);
    }
};
```

## Solution 2: Optimized Recursive Approach

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Recursion stack

Use recursion to naturally handle nested parentheses. This approach is cleaner and more intuitive.

```cpp
class Solution {
private:
    int parseExpr(const string& s, int& idx) {
        int result = 0;
        int sign = 1;
        int num = 0;
        
        while(idx < s.length()) {
            char c = s[idx];
            
            if(isdigit(c)) {
                num = num * 10 + (c - '0');
            } else if(c == '+') {
                result += sign * num;
                sign = 1;
                num = 0;
            } else if(c == '-') {
                result += sign * num;
                sign = -1;
                num = 0;
            } else if(c == '(') {
                idx++;  // Skip '('
                num = parseExpr(s, idx);  // Recursive call
            } else if(c == ')') {
                result += sign * num;
                return result;  // Return to parent
            }
            
            idx++;
        }
        
        return result + sign * num;
    }
    
public:
    int calculate(string s) {
        int idx = 0;
        return parseExpr(s, idx);
    }
};
```

## Solution 3: Simplified Iterative (No Stack for Numbers)

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Only for signs

A cleaner iterative approach that only uses stack for signs, not numbers.

```cpp
class Solution {
public:
    int calculate(string s) {
        stack<int> signs;
        int sign = 1;
        int result = 0;
        int num = 0;
        
        signs.push(1);  // Initial sign
        
        for(char c : s) {
            if(isdigit(c)) {
                num = num * 10 + (c - '0');
            } else if(c == '+' || c == '-') {
                result += signs.top() * sign * num;
                num = 0;
                sign = (c == '+') ? 1 : -1;
            } else if(c == '(') {
                signs.push(signs.top() * sign);
                sign = 1;
            } else if(c == ')') {
                result += signs.top() * sign * num;
                num = 0;
                signs.pop();
                sign = 1;
            }
        }
        
        result += signs.top() * sign * num;
        return result;
    }
};
```

## How the Algorithms Work

### Key Insight: Sign Propagation

Parentheses can flip the sign of the entire expression inside. We need to:
1. **Stack approach**: Save result and sign before `(`, restore after `)`
2. **Recursive approach**: Naturally handle nesting through recursion
3. **Sign stack**: Track cumulative sign changes through parentheses

### Solution 1: Stack-Based Step-by-Step

**Example:** `s = "(1+(4+5+2)-3)+(6+8)"`

```
Step 0: rtn=0, sign=1, curr=0, stk=[]

Step 1: '(' → push rtn(0) and sign(1)
  stk=[0, 1], rtn=0, sign=1, curr=0

Step 2: '1' → curr=1

Step 3: '+' → rtn += sign*curr = 0 + 1*1 = 1
  rtn=1, sign=1, curr=0

Step 4: '(' → push rtn(1) and sign(1)
  stk=[0, 1, 1, 1], rtn=0, sign=1, curr=0

Step 5-6: '4' → curr=4

Step 7: '+' → rtn += 1*4 = 4
  rtn=4, sign=1, curr=0

Step 8-9: '5' → curr=5

Step 10: '+' → rtn += 1*5 = 9
  rtn=9, sign=1, curr=0

Step 11-12: '2' → curr=2

Step 13: ')' → rtn += 1*2 = 11
  rtn *= stk.top() (1) = 11
  rtn += stk.top() (1) = 12
  stk=[0, 1], rtn=12, curr=0

Step 14: '-' → rtn += 1*0 = 12
  sign=-1, curr=0

Step 15-16: '3' → curr=3

Step 17: ')' → rtn += (-1)*3 = 9
  rtn *= stk.top() (1) = 9
  rtn += stk.top() (0) = 9
  stk=[], rtn=9, curr=0

Step 18: '+' → rtn += 1*0 = 9
  sign=1, curr=0

Step 19: '(' → push rtn(9) and sign(1)
  stk=[9, 1], rtn=0, sign=1, curr=0

Step 20-21: '6' → curr=6

Step 22: '+' → rtn += 1*6 = 6
  rtn=6, sign=1, curr=0

Step 23-24: '8' → curr=8

Step 25: ')' → rtn += 1*8 = 14
  rtn *= stk.top() (1) = 14
  rtn += stk.top() (9) = 23
  stk=[], rtn=23

Final: return 23 + 1*0 = 23 ✓
```

### Solution 3: Sign Stack Step-by-Step

**Example:** `s = "1 + (2 - 3)"`

```
Step 0: signs=[1], sign=1, result=0, num=0

Step 1: '1' → num=1

Step 2: '+' → result += 1*1*1 = 1
  sign=1, num=0

Step 3: '(' → signs.push(1*1) = [1, 1]
  sign=1

Step 4: '2' → num=2

Step 5: '-' → result += 1*1*(-1)*2 = 1 + (-2) = -1
  sign=-1, num=0

Step 6: '3' → num=3

Step 7: ')' → result += 1*(-1)*3 = -1 + (-3) = -4
  signs.pop() → [1]
  sign=1, num=0

Wait, let me recalculate more carefully:

Actually, the sign stack approach works differently. Let me trace correctly:

s = "1 + (2 - 3)"
signs = [1] initially

i=0: '1' → num=1
i=1: ' ' → skip
i=2: '+' → result += signs.top()*sign*num = 1*1*1 = 1
         sign=1, num=0
i=3: ' ' → skip
i=4: '(' → signs.push(signs.top()*sign) = signs.push(1*1) = [1, 1]
         sign=1
i=5: '2' → num=2
i=6: ' ' → skip
i=7: '-' → result += signs.top()*sign*num = 1*1*2 = 1+2 = 3
         sign=-1, num=0
i=8: ' ' → skip
i=9: '3' → num=3
i=10: ')' → result += signs.top()*sign*num = 1*(-1)*3 = 3+(-3) = 0
          signs.pop() → [1]
          sign=1, num=0

Final: result += signs.top()*sign*num = 0 + 1*1*0 = 0

But the answer should be 0, which is correct! (1 + (2-3) = 1 + (-1) = 0)
```

## Key Insights

1. **Stack for Parentheses**: Save state (result and sign) before `(`, restore after `)`
2. **Sign Handling**: Track current sign (1 or -1) for each number
3. **Number Building**: Accumulate multi-digit numbers
4. **Final Number**: Don't forget to add the last number at the end
5. **Recursion Alternative**: Natural way to handle nested parentheses

## Algorithm Breakdown

### Solution 1: Stack-Based

#### 1. Process Digits
```cpp
if(isdigit(ch)) {
    curr = (10 * curr) + (ch - '0');
}
```
- Build multi-digit numbers incrementally

#### 2. Process Operators
```cpp
switch(ch) {
    case '+':
        rtn += sign * curr;
        sign = 1;
        curr = 0;
        break;
    case '-':
        rtn += sign * curr;
        sign = -1;
        curr = 0;
        break;
    // ...
}
```
- Use `switch` for cleaner code when handling multiple character cases
- Add current number with sign to result
- Reset sign and current number

#### 3. Handle Opening Parenthesis
```cpp
case '(':
    stk.push(rtn);
    stk.push(sign);
    sign = 1;
    rtn = 0;
    curr = 0;
    break;
```
- Save current result and sign
- Reset for inner expression

#### 4. Handle Closing Parenthesis
```cpp
case ')':
    rtn += sign * curr;
    rtn *= stk.top();  // Apply saved sign
    stk.pop();
    rtn += stk.top();  // Add saved result
    stk.pop();
    curr = 0;
    break;
```
- Complete inner expression
- Apply saved sign
- Add to saved result

#### 5. Final Addition
```cpp
return rtn + (sign * curr);
```
- Add the last number if any

### Solution 2: Recursive

#### 1. Recursive Parsing
```cpp
int parseExpr(const string& s, int& idx) {
    int result = 0;
    int sign = 1;
    int num = 0;
    
    while(idx < s.length()) {
        // Process characters...
        if(c == '(') {
            idx++;  // Skip '('
            num = parseExpr(s, idx);  // Recursive call
        } else if(c == ')') {
            result += sign * num;
            return result;  // Return to parent
        }
        idx++;
    }
    
    return result + sign * num;
}
```

### Solution 3: Sign Stack

#### 1. Sign Propagation
```cpp
stack<int> signs;
signs.push(1);  // Initial sign

if(c == '(') {
    signs.push(signs.top() * sign);  // Cumulative sign
    sign = 1;
}
```

#### 2. Apply Cumulative Sign
```cpp
result += signs.top() * sign * num;
```
- `signs.top()`: Cumulative sign from all outer parentheses
- `sign`: Current operator sign
- `num`: Current number

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| **Stack-Based** | O(n) | O(n) | Explicit state management |
| **Recursive** | O(n) | O(n) | Natural for nesting |
| **Sign Stack** | O(n) | O(n) | Only stores signs |

## Edge Cases

1. **Single number**: `"42"` → `42`
2. **Negative start**: `"-1"` → `-1` (unary minus)
3. **Nested parentheses**: `"((1+2))"` → `3`
4. **Only spaces**: `"   "` → `0`
5. **Multiple spaces**: `"1  +  2"` → `3`
6. **Empty parentheses**: `"()"` → `0` (handled by current number being 0)

## Common Mistakes

1. **Forgetting final number**: Not adding `sign * curr` at the end
2. **Wrong stack order**: Pushing/popping in wrong order
3. **Sign handling**: Not applying saved sign correctly
4. **Number building**: Not resetting `curr` after processing
5. **Unary minus**: The problem allows `-` as unary, but the solution handles it naturally

## Detailed Example Walkthrough

### Example: `s = "1 + (2 - 3)"`

**Solution 1 (Stack):**

```
Step 0: rtn=0, sign=1, curr=0, stk=[]

Step 1: '1' → curr=1

Step 2: '+' → rtn += 1*1 = 1
  rtn=1, sign=1, curr=0

Step 3: '(' → push rtn(1) and sign(1)
  stk=[1, 1], rtn=0, sign=1, curr=0

Step 4: '2' → curr=2

Step 5: '-' → rtn += 1*2 = 2
  rtn=2, sign=-1, curr=0

Step 6: '3' → curr=3

Step 7: ')' → rtn += (-1)*3 = -1
  rtn *= stk.top() (1) = -1
  rtn += stk.top() (1) = 0
  stk=[], rtn=0, curr=0

Final: return 0 + 1*0 = 0 ✓
```

## Why Solution 1 Works

### Stack State Management

When we see `(`, we save:
1. **Current result** (`rtn`): What we've calculated so far
2. **Current sign** (`sign`): The sign that will apply to the inner expression

When we see `)`, we:
1. Complete the inner expression: `rtn += sign * curr`
2. Apply the saved sign: `rtn *= saved_sign`
3. Add to saved result: `rtn += saved_result`

### Example: `"1 + (2 - 3)"`

```
Before '(': rtn=1, sign=1
  Save: stk=[1, 1]
  Reset: rtn=0, sign=1

Inside '()': Calculate 2-3 = -1
  rtn = -1

After ')': 
  rtn *= 1 (saved sign) = -1
  rtn += 1 (saved result) = 0
  Final: 0 ✓
```

## Related Problems

- [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) - Adds `*` and `/`
- [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) - All operators + parentheses
- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) - Postfix notation
- [394. Decode String](https://leetcode.com/problems/decode-string/) - Nested structure evaluation

## Pattern Recognition

This problem demonstrates the **Expression Evaluation with Parentheses** pattern:
- Use stack or recursion to handle nested structures
- Track signs and results separately
- Save state before entering parentheses
- Restore state after exiting parentheses

**Key Insight:**
- Parentheses create nested evaluation contexts
- Stack naturally handles the LIFO nature of parentheses
- Recursion provides a natural way to handle nesting

## Optimization Tips

### Recursive vs Iterative

- **Recursive**: More intuitive, natural for nested structures
- **Iterative**: Avoids recursion overhead, more control

### Sign Stack Optimization

Solution 3 only stores signs, not results, which can be more memory-efficient in some cases.

## Code Quality Notes

1. **Readability**: Recursive approach is most intuitive
2. **Efficiency**: All approaches are O(n) time and space
3. **Correctness**: All handle parentheses and signs correctly
4. **Maintainability**: Stack approach is most explicit about state

---

*This problem is the foundation for more complex calculator problems. Understanding how to handle parentheses with a stack is crucial for expression evaluation.*

