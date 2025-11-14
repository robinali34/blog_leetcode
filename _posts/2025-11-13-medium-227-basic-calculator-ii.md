---
layout: post
title: "[Medium] 227. Basic Calculator II"
date: 2025-11-13 18:42:10 -0800
categories: leetcode algorithm medium cpp string stack expression-evaluation problem-solving
permalink: /posts/2025-11-13-medium-227-basic-calculator-ii/
tags: [leetcode, medium, string, stack, calculator, expression-evaluation]
---

# [Medium] 227. Basic Calculator II

Given a string `s` which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

## Examples

**Example 1:**
```
Input: s = "3+2*2"
Output: 7
```

**Example 2:**
```
Input: s = " 3/2 "
Output: 1
```

**Example 3:**
```
Input: s = " 3+5 / 2 "
Output: 5
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.
- `s` represents a valid expression.
- All the integers in the expression are non-negative integers in the range `[0, 2^31 - 1]`.
- The answer is guaranteed to fit in a 32-bit integer.

## Solution 1: Stack-Based Approach

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Use a stack to store numbers. When encountering `+` or `-`, push the number (with sign for `-`). When encountering `*` or `/`, immediately compute with the top of stack and push the result. Finally, sum all elements in the stack.

```cpp
class Solution {
public:
    int calculate(string s) {
        const int len = s.length();
        if(len == 0) return 0;

        stack<int> stk;
        char operation = '+';
        int curr = 0;
        
        for(int i = 0; i < len; i++) {
            char ch = s[i];
            
            if(isdigit(ch)) {
                curr = (curr * 10) + (ch - '0');
            }
            
            if (!isdigit(ch) && !isspace(ch) || i == len - 1) {
                if(operation == '-') {
                    stk.push(-curr);
                } else if(operation == '+') {
                    stk.push(curr);
                } else if(operation == '*') {
                    int stkTop = stk.top();
                    stk.pop();
                    stk.push(stkTop * curr);
                } else if(operation == '/') {
                    int stkTop = stk.top();
                    stk.pop();
                    stk.push(stkTop / curr);
                }
                
                operation = ch;
                curr = 0;
            }
        }
        
        int rtn = 0;
        while(!stk.empty()) {
            rtn += stk.top();
            stk.pop();
        }
        
        return rtn;
    }
};
```

## Solution 2: Optimized Without Stack

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Instead of using a stack, use variables to track the last value and current result. This avoids the need for a stack since we process `*` and `/` immediately and only need to remember the last value for `+` and `-`.

```cpp
class Solution {
public:
    int calculate(string s) {
        const int len = s.length();
        if (len == 0) return 0;
        
        int curr = 0, last = 0, rtn = 0;
        char sign = '+';
        
        for(int i = 0; i < len; i++) {
            char ch = s[i];
            
            if(isdigit(ch)) {
                curr = (curr * 10) + (ch - '0');
            }
            
            if(!isdigit(ch) && !isspace(ch) || i == len - 1) {
                if(sign == '+' || sign == '-') {
                    rtn += last;
                    last = (sign == '+') ? curr : -curr;
                } else if(sign == '*') {
                    last = last * curr;
                } else if(sign == '/') {
                    last = last / curr;
                }
                
                sign = ch;
                curr = 0;
            }
        }
        
        rtn += last;
        return rtn;
    }
};
```

## How the Algorithms Work

### Key Insight: Operator Precedence

- **`*` and `/`**: Higher precedence - must be evaluated immediately
- **`+` and `-`**: Lower precedence - can be deferred until the end

### Solution 1: Stack-Based Step-by-Step

**Example:** `s = "3+2*2"`

| Step | Char | `curr` | `operation` | Stack | Action |
|------|------|--------|-------------|-------|--------|
| 0 | - | 0 | '+' | [] | Initialize |
| 1 | '3' | 3 | '+' | [] | Build number |
| 2 | '+' | 0 | '+' | [3] | Push 3, set op |
| 3 | '2' | 2 | '+' | [3] | Build number |
| 4 | '*' | 0 | '*' | [3] | Set op to * |
| 5 | '2' | 2 | '*' | [3] | Build number |
| 6 | End | 0 | - | [3, 4] | Pop 3, calc 3*2=4, push 4 |
| Final | - | - | - | [3, 4] | Sum: 3+4=7 |

**Visual Representation:**
```
"3+2*2"
 3 + 2 * 2
 ↑   ↑   ↑
 |   |   |
 |   |   Process: 2*2 = 4, push 4
 |   |
 |   Push: 3
 |
 Sum all: 3 + 4 = 7
```

### Solution 2: Optimized Step-by-Step

**Example:** `s = "3+2*2"`

| Step | Char | `curr` | `sign` | `last` | `rtn` | Action |
|------|------|--------|--------|--------|-------|--------|
| 0 | - | 0 | '+' | 0 | 0 | Initialize |
| 1 | '3' | 3 | '+' | 0 | 0 | Build number |
| 2 | '+' | 0 | '+' | 3 | 0 | Add last to rtn, set last=3 |
| 3 | '2' | 2 | '+' | 3 | 0 | Build number |
| 4 | '*' | 0 | '*' | 3 | 0 | Set sign to * |
| 5 | '2' | 2 | '*' | 6 | 0 | Build number, calc last=3*2=6 |
| 6 | End | 0 | - | 6 | 0 | Add last to rtn: 0+6=6 |

Wait, let me recalculate:

Actually, at step 2 (when we see '+'), we should:
- `rtn += last` → `rtn = 0 + 0 = 0`
- `last = (sign == '+') ? curr : -curr` → `last = 3`

At step 5 (when we see '2' and sign is '*'):
- We process the previous sign '*'
- `last = last * curr` → `last = 3 * 2 = 6`

At the end:
- `rtn += last` → `rtn = 0 + 6 = 6`

But the answer should be 7, not 6. Let me trace more carefully:

Actually, the issue is that when we see the operator, we need to process the previous operator. Let me trace correctly:

```
"3+2*2"
 i=0: '3' → curr = 3
 i=1: '+' → process '+' with curr=3
        sign was '+', so rtn += last (0), last = 3
        sign = '+', curr = 0
 i=2: '2' → curr = 2
 i=3: '*' → process '*' with curr=2
        sign was '*', so last = last * curr = 3 * 2 = 6
        sign = '*', curr = 0
 i=4: '2' → curr = 2
 i=5: end → process '*' with curr=2
        sign was '*', so last = last * curr = 6 * 2 = 12
        Then rtn += last = 0 + 12 = 12
```

This is still wrong. The issue is that we're processing the operator when we see the NEXT operator or end. Let me look at the code again:

```cpp
if(!isdigit(ch) && !isspace(ch) || i == len - 1) {
    // Process previous operation
    if(sign == '+' || sign == '-') {
        rtn += last;
        last = (sign == '+') ? curr : -curr;
    } else if(sign == '*') {
        last = last * curr;
    } else if(sign == '/') {
        last = last / curr;
    }
    sign = ch;  // Update sign for next operation
    curr = 0;
}
```

I see - when we see an operator, we process the PREVIOUS operator with the current number. Let me trace again:

```
"3+2*2"
 i=0: '3' → curr = 3
 i=1: '+' → process previous sign '+' with curr=3
        sign was '+' (initial), so rtn += last (0), last = 3
        sign = '+', curr = 0
 i=2: '2' → curr = 2
 i=3: '*' → process previous sign '+' with curr=2
        sign was '+', so rtn += last (3), last = 2
        sign = '*', curr = 0
 i=4: '2' → curr = 2
 i=5: end → process previous sign '*' with curr=2
        sign was '*', so last = last * curr = 2 * 2 = 4
        Then rtn += last = 3 + 4 = 7 ✓
```

Yes! That's correct now.

## Key Insights

1. **Operator Precedence**: `*` and `/` have higher precedence than `+` and `-`
2. **Immediate Evaluation**: Evaluate `*` and `/` immediately when encountered
3. **Deferred Evaluation**: Defer `+` and `-` until the end
4. **Number Building**: Build multi-digit numbers by `curr = curr * 10 + digit`
5. **Sign Handling**: For `-`, push negative number or set `last` to negative

## Algorithm Breakdown

### Solution 1: Stack-Based

#### 1. Build Numbers
```cpp
if(isdigit(ch)) {
    curr = (curr * 10) + (ch - '0');
}
```
- Accumulate digits to form multi-digit numbers

#### 2. Process Operators
```cpp
if (!isdigit(ch) && !isspace(ch) || i == len - 1) {
    if(operation == '-') {
        stk.push(-curr);  // Push negative for subtraction
    } else if(operation == '+') {
        stk.push(curr);
    } else if(operation == '*') {
        int stkTop = stk.top();
        stk.pop();
        stk.push(stkTop * curr);  // Immediate evaluation
    } else if(operation == '/') {
        int stkTop = stk.top();
        stk.pop();
        stk.push(stkTop / curr);  // Immediate evaluation
    }
    operation = ch;
    curr = 0;
}
```

#### 3. Sum Stack
```cpp
int rtn = 0;
while(!stk.empty()) {
    rtn += stk.top();
    stk.pop();
}
```

### Solution 2: Optimized

#### 1. Track Last Value
```cpp
int curr = 0, last = 0, rtn = 0;
char sign = '+';
```
- **`last`**: Stores the value that might be multiplied/divided
- **`rtn`**: Accumulates final result

#### 2. Process Operators
```cpp
if(sign == '+' || sign == '-') {
    rtn += last;  // Add previous last to result
    last = (sign == '+') ? curr : -curr;  // Set new last
} else if(sign == '*') {
    last = last * curr;  // Immediate evaluation
} else if(sign == '/') {
    last = last / curr;  // Immediate evaluation
}
```

#### 3. Final Addition
```cpp
rtn += last;  // Add remaining last value
```

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| **Stack-Based** | O(n) | O(n) | Clear logic, uses stack |
| **Optimized** | O(n) | O(1) | No stack needed |

## Why Solution 2 Works

### Key Observation

For expressions like `a + b * c`:
- We can't evaluate `a + b` first (wrong precedence)
- We evaluate `b * c` first, then add to `a`
- So we keep `a` separate and combine `b * c` immediately

### Variable Roles

- **`last`**: Holds the value that's part of a `*` or `/` chain, or a single `+`/`-` operand
- **`rtn`**: Accumulates values that are completely processed (added/subtracted)

### Example: `"3+2*2"`

```
Step 1: Process '3' with sign '+'
  rtn += last (0) → rtn = 0
  last = 3

Step 2: Process '2' with sign '*'
  last = last * 2 = 3 * 2 = 6

Step 3: End, process with sign '*'
  last = last * 2 = 6 * 2 = 12
  rtn += last = 0 + 12 = 12
```

Wait, that's still wrong. Let me re-read the code logic:

Actually, when we see an operator, we process the PREVIOUS operator. So:

```
"3+2*2"
 i=0: '3' → curr=3
 i=1: '+' → process sign='+' (initial) with curr=3
        rtn += last (0), last = 3, sign='+', curr=0
 i=2: '2' → curr=2
 i=3: '*' → process sign='+' with curr=2
        rtn += last (3), last = 2, sign='*', curr=0
 i=4: '2' → curr=2
 i=5: end → process sign='*' with curr=2
        last = last * curr = 2 * 2 = 4
        rtn += last = 3 + 4 = 7 ✓
```

Perfect!

## Edge Cases

1. **Single number**: `"42"` → `42`
2. **Only spaces**: `"   "` → `0` (handled by initial check)
3. **Division truncation**: `"3/2"` → `1` (not 1.5)
4. **Negative results**: `"1-2"` → `-1`
5. **Multiple spaces**: `"3  +  2"` → `5` (spaces are ignored)
6. **Consecutive operators**: Not possible (given expression is valid)

## Common Mistakes

1. **Wrong operator precedence**: Evaluating `+` before `*`
2. **Number building**: Not handling multi-digit numbers correctly
3. **Sign handling**: Forgetting to push negative for `-` or set `last` negative
4. **End of string**: Not processing the last number when string ends
5. **Division truncation**: Using floating point instead of integer division

## Detailed Example Walkthrough

### Example: `s = " 3+5 / 2 "`

**Solution 1 (Stack):**

```
Step 0: Initialize
  stk = []
  operation = '+'
  curr = 0

Step 1-2: ' 3' → curr = 3
Step 3: '+' → process operation='+' with curr=3
  stk.push(3)
  operation = '+', curr = 0
  stk = [3]

Step 4-5: ' 5' → curr = 5
Step 6: ' ' → skip
Step 7: '/' → process operation='+' with curr=5
  stk.push(5)
  operation = '/', curr = 0
  stk = [3, 5]

Step 8: ' ' → skip
Step 9: '2' → curr = 2
Step 10: ' ' → skip
Step 11: end → process operation='/' with curr=2
  top = 5, stk.pop()
  stk.push(5 / 2) = stk.push(2)
  stk = [3, 2]

Final: Sum stack = 3 + 2 = 5 ✓
```

**Solution 2 (Optimized):**

```
Step 0: Initialize
  curr = 0, last = 0, rtn = 0
  sign = '+'

Step 1-2: ' 3' → curr = 3
Step 3: '+' → process sign='+' with curr=3
  rtn += last (0) → rtn = 0
  last = 3
  sign = '+', curr = 0

Step 4-5: ' 5' → curr = 5
Step 6: ' ' → skip
Step 7: '/' → process sign='+' with curr=5
  rtn += last (3) → rtn = 3
  last = 5
  sign = '/', curr = 0

Step 8: ' ' → skip
Step 9: '2' → curr = 2
Step 10: ' ' → skip
Step 11: end → process sign='/' with curr=2
  last = last / curr = 5 / 2 = 2
  rtn += last = 3 + 2 = 5 ✓
```

## Related Problems

- [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/) - With parentheses
- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) - Postfix notation
- [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) - With parentheses and all operators
- [394. Decode String](https://leetcode.com/problems/decode-string/) - Nested structure evaluation

## Pattern Recognition

This problem demonstrates the **Expression Evaluation** pattern:
- Process operators based on precedence
- Use stack or variables to defer lower-precedence operations
- Build numbers incrementally
- Handle spaces and edge cases

**Key Insight:**
- Higher precedence operators (`*`, `/`) are evaluated immediately
- Lower precedence operators (`+`, `-`) are deferred
- Stack or variables can track deferred values

## Optimization Tips

### Solution 2 Advantages
- **O(1) space**: No stack needed
- **Fewer operations**: Direct variable updates
- **Better cache performance**: No stack memory access

### When to Use Each
- **Stack-based**: Easier to understand and extend (e.g., for parentheses)
- **Optimized**: Better for space-constrained scenarios

## Code Quality Notes

1. **Readability**: Stack approach is more intuitive
2. **Efficiency**: Optimized approach uses O(1) space
3. **Correctness**: Both handle operator precedence correctly
4. **Maintainability**: Stack approach is easier to extend

---

*This problem demonstrates how to handle operator precedence in expression evaluation. The key is to evaluate high-precedence operators immediately while deferring low-precedence operators.*

