---
layout: post
title: "[Hard] 772. Basic Calculator III"
date: 2025-11-13 19:15:52 -0800
categories: leetcode algorithm hard cpp string stack recursion expression-evaluation problem-solving
permalink: /posts/2025-11-13-hard-772-basic-calculator-iii/
tags: [leetcode, hard, string, stack, calculator, recursion, expression-evaluation, parentheses]
---

# [Hard] 772. Basic Calculator III

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, **non-negative** integers and empty spaces.

The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators, open `(` and closing parentheses `)` and empty spaces. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

## Examples

**Example 1:**
```
Input: s = "1+1"
Output: 2
```

**Example 2:**
```
Input: s = "6-4/2"
Output: 4
```

**Example 3:**
```
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
```

**Example 4:**
```
Input: s = "(2+6*3+5-(3*14/7+2)*5)+3"
Output: -12
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of digits, `'+'`, `'-'`, `'*'`, `'/'`, `'('`, `')'`, and `' '`.
- `s` is a valid expression.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Expression format**: What operations are supported? (Assumption: Addition '+', subtraction '-', multiplication '*', division '/', parentheses '()')

2. **Operator precedence**: What is the precedence? (Assumption: Standard - parentheses first, then multiplication/division, then addition/subtraction)

3. **Division handling**: How should division be handled? (Assumption: Integer division - truncate toward zero)

4. **Return value**: What should we return? (Assumption: Integer result of evaluating the expression)

5. **Whitespace**: Should we ignore whitespace? (Assumption: Yes - spaces can be ignored)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

Use a recursive descent parser: parse the expression by handling parentheses recursively. For each level, evaluate expressions inside parentheses first, then replace them with their results. Handle operator precedence by doing multiple passes: first evaluate all multiplications/divisions, then all additions/subtractions. This approach works but requires multiple passes and can be inefficient, especially with deeply nested parentheses.

**Step 2: Semi-Optimized Approach (10 minutes)**

Convert the infix expression to postfix (RPN) using the shunting yard algorithm, then evaluate the postfix expression. This handles operator precedence correctly but requires two passes: one for conversion and one for evaluation. The conversion step uses a stack to handle operators and parentheses, which adds complexity. Alternatively, use two stacks (operands and operators) and evaluate on-the-fly, but managing operator precedence with two stacks can be tricky.

**Step 3: Optimized Solution (12 minutes)**

Use a single-pass approach with recursion for parentheses and a stack for operator precedence. When encountering '(', recursively evaluate the subexpression. For operators, use a stack to maintain operators in order of precedence: when encountering a lower-precedence operator, evaluate all higher-precedence operators first. Alternatively, use a cleaner approach: maintain a stack of numbers and signs, processing multiplication/division immediately and addition/subtraction by maintaining a running result. This achieves O(n) time with O(n) space for the recursion stack, handling nested parentheses naturally through recursion and operator precedence through immediate evaluation of high-precedence operations.

## Solution 1: Recursive Approach

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Recursion stack depth

Use recursion to handle nested parentheses. When encountering `(`, recursively evaluate the expression inside. Use a stack to handle operator precedence: evaluate `*` and `/` immediately, defer `+` and `-` until the end.

```cpp
class Solution {
private:
    int parseExpr(const string& s, int& idx) {
        char op = '+';
        vector<int> stk;
        
        for(; idx < (int)s.size(); idx++) {
            if(iswspace(s[idx])) continue;
            
            long num = 0;
            if(s[idx] == '(') {
                num = parseExpr(s, ++idx);
            } else if(isdigit(s[idx])) {
                num = parseNum(s, idx);
                idx--;
            } else if(s[idx] == ')') {
                break;
            } else {
                continue;
            }
            
            switch(op) {
                case '+': stk.push_back(num); break;
                case '-': stk.push_back(-num); break;
                case '*': stk.back() *= num; break;
                case '/': stk.back() /= num; break;
            }
            
            if (idx + 1 < s.size()) {
                op = s[idx + 1];
            }
        }
        
        int rtn = 0;
        for(int num: stk) rtn += num;
        return rtn;
    }
    
    long parseNum(const string& s, int& idx) {
        long num = 0;
        while(idx < (int)s.size() && isdigit(s[idx])) {
            num = (num * 10) + (s[idx] - '0');
            idx++;
        }
        return num;
    }
    
public:
    int calculate(string s) {
        int idx = 0;
        return parseExpr(s, idx);
    }
};
```

## Solution 2: Optimized Iterative Approach

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Stack for parentheses

Use an iterative approach with a stack to handle parentheses. When encountering `(`, push current state onto stack. When encountering `)`, pop and combine with previous state.

```cpp
class Solution {
public:
    int calculate(string s) {
        stack<int> nums;
        stack<char> ops;
        int num = 0;
        char op = '+';
        
        for(int i = 0; i < s.size(); i++) {
            char c = s[i];
            
            if(isdigit(c)) {
                num = num * 10 + (c - '0');
            }
            
            if((!isdigit(c) && !isspace(c)) || i == s.size() - 1) {
                if(c == '(') {
                    nums.push(0);
                    ops.push(op);
                    num = 0;
                    op = '+';
                } else {
                    // Apply current operation
                    if(op == '+') {
                        nums.push(num);
                    } else if(op == '-') {
                        nums.push(-num);
                    } else if(op == '*') {
                        int top = nums.top();
                        nums.pop();
                        nums.push(top * num);
                    } else if(op == '/') {
                        int top = nums.top();
                        nums.pop();
                        nums.push(top / num);
                    }
                    
                    if(c == ')') {
                        // Evaluate expression inside parentheses
                        int sum = 0;
                        while(!ops.empty() && ops.top() != '(') {
                            sum += nums.top();
                            nums.pop();
                        }
                        ops.pop(); // Remove '('
                        num = sum;
                        op = ops.empty() ? '+' : ops.top();
                    } else {
                        op = c;
                        num = 0;
                    }
                }
            }
        }
        
        int result = 0;
        while(!nums.empty()) {
            result += nums.top();
            nums.pop();
        }
        return result;
    }
};
```

## Solution 3: Simplified Optimized Approach

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Stack for parentheses

A cleaner iterative solution that uses a single stack to track both numbers and operators, with special handling for parentheses.

```cpp
class Solution {
public:
    int calculate(string s) {
        stack<int> stk;
        int num = 0;
        char sign = '+';
        
        for(int i = 0; i < s.size(); i++) {
            char c = s[i];
            
            if(isdigit(c)) {
                num = num * 10 + (c - '0');
            }
            
            if(c == '(') {
                // Push current state
                stk.push(0);
                stk.push(sign == '+' ? 1 : -1);
                num = 0;
                sign = '+';
            } else if(c == ')') {
                // Evaluate expression inside parentheses
                int val = num;
                int multiplier = stk.top(); stk.pop();
                int prevSum = stk.top(); stk.pop();
                num = prevSum + multiplier * val;
                sign = '+';
            } else if(c == '+' || c == '-' || c == '*' || c == '/') {
                // Process previous operation
                if(sign == '+') {
                    stk.push(num);
                } else if(sign == '-') {
                    stk.push(-num);
                } else if(sign == '*') {
                    int top = stk.top();
                    stk.pop();
                    stk.push(top * num);
                } else if(sign == '/') {
                    int top = stk.top();
                    stk.pop();
                    stk.push(top / num);
                }
                
                sign = c;
                num = 0;
            }
        }
        
        // Process last number
        if(sign == '+') {
            stk.push(num);
        } else if(sign == '-') {
            stk.push(-num);
        } else if(sign == '*') {
            int top = stk.top();
            stk.pop();
            stk.push(top * num);
        } else if(sign == '/') {
            int top = stk.top();
            stk.pop();
            stk.push(top / num);
        }
        
        int result = 0;
        while(!stk.empty()) {
            result += stk.top();
            stk.pop();
        }
        return result;
    }
};
```

## How the Algorithms Work

### Key Insight: Handling Parentheses

Parentheses change the evaluation order. We need to:
1. **Recursive approach**: When seeing `(`, recursively evaluate the inner expression
2. **Iterative approach**: Use stack to save state before `(` and restore after `)`

### Solution 1: Recursive Step-by-Step

**Example:** `s = "2*(5+5*2)/3"`

```
parseExpr("2*(5+5*2)/3", idx=0)
  op = '+', stk = []
  
  idx=0: '2' → num = 2
    op='+': stk.push_back(2) → stk = [2]
    op = '*'
  
  idx=1: '*' → skip (handled above)
  
  idx=2: '(' → recursive call
    parseExpr("5+5*2)/3", idx=3)
      op = '+', stk = []
      
      idx=3: '5' → num = 5
        op='+': stk.push_back(5) → stk = [5]
        op = '+'
      
      idx=4: '+' → skip
      
      idx=5: '5' → num = 5
        op='+': stk.push_back(5) → stk = [5, 5]
        op = '*'
      
      idx=6: '*' → skip
      
      idx=7: '2' → num = 2
        op='*': stk.back() *= 2 → stk = [5, 10]
        op = ')'
      
      idx=8: ')' → break, return sum([5, 10]) = 15
    
    num = 15
    op='*': stk.back() *= 15 → stk = [30]
    op = '/'
  
  idx=9: '/' → skip
  
  idx=10: '3' → num = 3
    op='/': stk.back() /= 3 → stk = [10]
  
  Return sum([10]) = 10
```

### Solution 3: Simplified Iterative Step-by-Step

**Example:** `s = "2*(5+5*2)/3"`

```
Step 0: num=0, sign='+', stk=[]

Step 1: '2' → num=2
Step 2: '*' → process sign='+'
  stk.push(2) → stk=[2]
  sign='*', num=0

Step 3: '(' → push state
  stk.push(0), stk.push(1) → stk=[2, 0, 1]
  num=0, sign='+'

Step 4-5: '5' → num=5
Step 6: '+' → process sign='+'
  stk.push(5) → stk=[2, 0, 1, 5]
  sign='+', num=0

Step 7-8: '5' → num=5
Step 9: '*' → process sign='+'
  stk.push(5) → stk=[2, 0, 1, 5, 5]
  sign='*', num=0

Step 10-11: '2' → num=2
Step 12: ')' → evaluate parentheses
  Process sign='*': stk.top() *= 2 → stk=[2, 0, 1, 5, 10]
  multiplier = 1, prevSum = 0
  num = 0 + 1 * (5+10) = 15
  sign='+'

Step 13: '/' → process sign='*'
  stk.top() *= 15 → stk=[2, 30]
  sign='/', num=0

Step 14-15: '3' → num=3
End: process sign='/'
  stk.top() /= 3 → stk=[10]

Result: sum([10]) = 10
```

## Key Insights

1. **Recursion for Parentheses**: Natural way to handle nested structures
2. **Stack for State**: Save evaluation state before entering parentheses
3. **Operator Precedence**: Evaluate `*` and `/` immediately, defer `+` and `-`
4. **Index Management**: Careful index tracking in recursive approach
5. **Number Building**: Accumulate multi-digit numbers correctly

## Algorithm Breakdown

### Solution 1: Recursive

#### 1. Parse Expression
```cpp
int parseExpr(const string& s, int& idx) {
    char op = '+';
    vector<int> stk;
    // Process characters...
}
```

#### 2. Handle Parentheses
```cpp
if(s[idx] == '(') {
    num = parseExpr(s, ++idx);  // Recursive call
} else if(s[idx] == ')') {
    break;  // Return from recursion
}
```

#### 3. Handle Numbers
```cpp
else if(isdigit(s[idx])) {
    num = parseNum(s, idx);
    idx--;  // Adjust because parseNum advances idx
}
```

#### 4. Apply Operations
```cpp
switch(op) {
    case '+': stk.push_back(num); break;
    case '-': stk.push_back(-num); break;
    case '*': stk.back() *= num; break;
    case '/': stk.back() /= num; break;
}
```

### Solution 3: Simplified Iterative

#### 1. Handle Opening Parenthesis
```cpp
if(c == '(') {
    stk.push(0);  // Push current sum
    stk.push(sign == '+' ? 1 : -1);  // Push multiplier
    num = 0;
    sign = '+';
}
```

#### 2. Handle Closing Parenthesis
```cpp
else if(c == ')') {
    int val = num;
    int multiplier = stk.top(); stk.pop();
    int prevSum = stk.top(); stk.pop();
    num = prevSum + multiplier * val;  // Combine with outer expression
    sign = '+';
}
```

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive** | O(n) | O(n) | Natural for nested structures |
| **Iterative (2 stacks)** | O(n) | O(n) | More explicit state management |
| **Simplified Iterative** | O(n) | O(n) | Cleaner code, single stack |

## Edge Cases

1. **Nested parentheses**: `"((1+2)*3)"` → `9`
2. **No parentheses**: `"1+2*3"` → `7`
3. **Single number**: `"42"` → `42`
4. **Negative results**: `"1-2"` → `-1`
5. **Division truncation**: `"5/2"` → `2`
6. **Multiple spaces**: `"1 + 2"` → `3`

## Common Mistakes

1. **Index management**: Not adjusting index after `parseNum` or after recursive call
2. **Operator precedence**: Evaluating `+` before `*`
3. **Parentheses handling**: Not properly saving/restoring state
4. **Number building**: Not handling multi-digit numbers
5. **Sign handling**: Forgetting to push negative for `-`

## Detailed Example Walkthrough

### Example: `s = "2*(5+5*2)/3"`

**Solution 1 (Recursive):**

```
Main call: parseExpr("2*(5+5*2)/3", idx=0)
  op='+', stk=[]
  
  idx=0: '2' → num=2
    op='+': stk=[2]
    op='*'
  
  idx=2: '(' → recursive call
    parseExpr("5+5*2)/3", idx=3)
      op='+', stk=[]
      
      idx=3: '5' → num=5
        op='+': stk=[5]
        op='+'
      
      idx=5: '5' → num=5
        op='+': stk=[5, 5]
        op='*'
      
      idx=7: '2' → num=2
        op='*': stk=[5, 10]
        op=')'
      
      idx=8: ')' → break
      Return: 5+10 = 15
    
    num=15
    op='*': stk=[30]
    op='/'
  
  idx=10: '3' → num=3
    op='/': stk=[10]
  
  Return: 10
```

## Related Problems

- [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/) - Only `+`, `-`, parentheses
- [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) - `+`, `-`, `*`, `/` (no parentheses)
- [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) - This problem (all operators + parentheses)
- [394. Decode String](https://leetcode.com/problems/decode-string/) - Nested structure evaluation

## Pattern Recognition

This problem demonstrates the **Expression Evaluation with Parentheses** pattern:
- Use recursion or stack to handle nested structures
- Maintain operator precedence
- Save/restore evaluation state at parentheses boundaries
- Process operators based on precedence

**Key Insight:**
- Parentheses create nested evaluation contexts
- Recursion naturally handles nesting
- Stack can simulate recursion iteratively

## Optimization Tips

### Recursive vs Iterative

- **Recursive**: More intuitive, natural for nested structures
- **Iterative**: Avoids recursion stack overhead, more control

### Index Management

In recursive approach, be careful with index:
- `parseNum` advances `idx`, so need `idx--` after
- Recursive call uses `++idx` to skip `(`
- `)` naturally breaks the loop

## Code Quality Notes

1. **Readability**: Recursive approach is more intuitive
2. **Efficiency**: Both approaches are O(n) time and space
3. **Correctness**: Both handle operator precedence and parentheses correctly
4. **Maintainability**: Simplified iterative approach is cleaner

---

*This problem combines expression evaluation with nested parentheses handling. The recursive approach naturally handles nesting, while the iterative approach provides more control over the evaluation process.*

