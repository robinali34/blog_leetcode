---
layout: post
title: "[Medium] 150. Evaluate Reverse Polish Notation"
date: 2025-09-24 20:00:00 -0000
categories: leetcode algorithm stack data-structures mathematical-expression medium cpp reverse-polish-notation rpn problem-solving
---

# [Medium] 150. Evaluate Reverse Polish Notation

This is a classic stack problem that requires evaluating mathematical expressions written in Reverse Polish Notation (RPN). The key insight is using a stack to process operands and operators in the correct order.

## Problem Description

Given an array of strings representing a valid Reverse Polish Notation expression, evaluate the expression and return the result.

In Reverse Polish Notation:
- Operands come before operators
- Each operator takes its two preceding operands
- Division truncates toward zero

### Examples

**Example 1:**
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:**
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
```

### Constraints
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200]

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **RPN definition**: What is Reverse Polish Notation? (Assumption: Postfix notation - operators come after operands, e.g., "2 3 +" means 2 + 3)

2. **Evaluation order**: How is the expression evaluated? (Assumption: Process left to right, when operator encountered, apply to two most recent operands)

3. **Division handling**: How should we handle division? (Assumption: Integer division - truncate toward zero, e.g., 13/5 = 2)

4. **Valid expression**: Is the expression guaranteed to be valid? (Assumption: Yes - per problem statement, expression is always valid)

5. **Return value**: What should we return? (Assumption: Integer result of evaluating the RPN expression)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to evaluate RPN expression. Let me parse and compute manually."

**Naive Solution**: Parse expression, manually track operands and operators, compute step by step without using stack structure.

**Complexity**: O(n) time, O(n) space

**Issues**:
- Complex parsing logic
- Doesn't leverage stack structure naturally
- Hard to handle operator precedence correctly
- More error-prone

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "RPN is designed for stack evaluation. When I see an operator, pop two operands, compute, push result."

**Improved Solution**: Use stack. Traverse tokens left to right. If token is number, push to stack. If operator, pop two operands, compute, push result.

**Complexity**: O(n) time, O(n) space

**Improvements**:
- Stack naturally models RPN evaluation
- Clean and intuitive
- Handles all operators correctly
- O(n) time is optimal

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "Stack approach is already optimal. Can optimize space by using vector as stack or handle edge cases better."

**Best Solution**: Stack-based evaluation is optimal. Can use vector as stack for better cache locality, but std::stack is clearer. Handle integer division truncation correctly.

**Complexity**: O(n) time, O(n) space

**Key Realizations**:
1. Stack is perfect data structure for RPN
2. O(n) time is optimal - must process each token
3. O(n) space is optimal - worst case all numbers before operators
4. Integer division truncation is important detail

## Approach

The solution uses a stack-based approach:

1. **Stack Processing**: Use a stack to store operands
2. **Operator Detection**: Check if current token is an operator
3. **Operation Execution**: Pop two operands, perform operation, push result
4. **Final Result**: The remaining element in stack is the answer

## Solution 1: Using std::stack

**Time Complexity:** O(n) - Process each token once  
**Space Complexity:** O(n) - Stack can hold up to n/2 operands

```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        unordered_set<string> ops = {"+", "-", "*", "/"};
        const int n = tokens.size();
        for (const auto& token : tokens) {
            if (!ops.count(token)){
                stk.push(stoi(token));
            } else {
                int num2 = stk.top();
                stk.pop();
                int num1 = stk.top();
                stk.pop();
                int rtn = 0;
                switch (token[0]) {
                    case '+': rtn = num1 + num2; break;
                    case '-': rtn = num1 - num2; break;
                    case '*': rtn = num1 * num2; break;
                    case '/': rtn = num1 / num2; break;
                }
                stk.push(rtn);
            }
        }
        return stk.top();
    }
};
```

## Solution 2: Using Vector as Stack

**Time Complexity:** O(n) - Process each token once  
**Space Complexity:** O(n) - Vector can hold up to n/2 operands

```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        const int n = tokens.size();
        vector<int> stk((n + 1) / 2);
        int idx = -1;
        unordered_set<string> ops = {"+", "-", "*", "/"};
        for (const auto& token : tokens) {
            if (token.length() > 1 || !ops.count(token)){
                idx++;
                stk[idx] = stoi(token);
            } else {
                switch (token[0]) {
                    case '+': idx--; stk[idx] += stk[idx + 1]; break;
                    case '-': idx--; stk[idx] -= stk[idx + 1]; break;
                    case '*': idx--; stk[idx] *= stk[idx + 1]; break;
                    case '/': idx--; stk[idx] /= stk[idx + 1]; break;
                }
            }
        }
        return stk[idx];
    }
};
```

## Step-by-Step Example

Let's trace through Solution 1 with tokens = `["2","1","+","3","*"]`:

**Step 1:** Process "2"
- Not an operator, push to stack: `[2]`

**Step 2:** Process "1"  
- Not an operator, push to stack: `[2, 1]`

**Step 3:** Process "+"
- Operator detected, pop two operands: `num2=1, num1=2`
- Perform addition: `2 + 1 = 3`
- Push result to stack: `[3]`

**Step 4:** Process "3"
- Not an operator, push to stack: `[3, 3]`

**Step 5:** Process "*"
- Operator detected, pop two operands: `num2=3, num1=3`
- Perform multiplication: `3 * 3 = 9`
- Push result to stack: `[9]`

**Result:** `9`

## Key Insights

1. **Stack LIFO**: Last In, First Out property matches RPN evaluation order
2. **Operator Precedence**: RPN eliminates need for operator precedence rules
3. **Operand Order**: First popped operand is the second operand in the operation
4. **Integer Division**: Division truncates toward zero (C++ behavior)

## Solution Comparison

| Approach | Pros | Cons |
|----------|------|------|
| **std::stack** | Clean API, easy to understand | Slight overhead from function calls |
| **Vector Stack** | More efficient, direct array access | Manual index management |

## Edge Cases

- **Single Operand**: Expression with only one number
- **Negative Numbers**: Tokens like "-11" (length > 1)
- **Division by Zero**: Not possible with valid RPN
- **Large Numbers**: Integer overflow considerations

## Common Mistakes

- **Operand Order**: Swapping the order of popped operands
- **Negative Number Detection**: Not handling multi-character tokens correctly
- **Stack Underflow**: Not checking if stack has enough operands
- **Integer Division**: Forgetting that division truncates toward zero

---
