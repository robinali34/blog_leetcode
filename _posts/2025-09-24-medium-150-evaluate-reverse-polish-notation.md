---
layout: post
title: "[Medium] 150. Evaluate Reverse Polish Notation"
date: 2025-09-24 20:00:00 -0000
categories: leetcode algorithm stack data-structures mathematical-expression medium cpp reverse-polish-notation rpn problem-solving
---
This is a classic stack problem that requires evaluating mathematical expressions written in Reverse Polish Notation (RPN). The key insight is using a stack to process operands and operators in the correct order.

Given an array of strings representing a valid Reverse Polish Notation expression, evaluate the expression and return the result.

In Reverse Polish Notation:
- Operands come before operators
- Each operator takes its two preceding operands
- Division truncates toward zero

## Examples
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

## Constraints
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200]

## Thinking Process

The solution uses a stack-based approach:

1. **Stack Processing**: Use a stack to store operands
2. **Operator Detection**: Check if current token is an operator
3. **Operation Execution**: Pop two operands, perform operation, push result
4. **Final Result**: The remaining element in stack is the answer

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
| **Monotonic stack** *(this problem)* | O(n) | O(n) | Next greater/smaller element |
| Parentheses matching | O(n) | O(n) | Push open, pop on close |
| Expression evaluation | O(n) | O(n) | Operand + operator stacks |
| Stack simulation | O(n) | O(n) | Process in LIFO order |

## Solution

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

### Solution Explanation

**Approach:** Monotonic stack (this problem)

**Key idea:** The solution uses a stack-based approach:

**How the code works:**
1. **Stack Processing**: Use a stack to store operands
2. **Operator Detection**: Check if current token is an operator
3. **Operation Execution**: Pop two operands, perform operation, push result
4. **Final Result**: The remaining element in stack is the answer

**Walkthrough** — input `tokens = ["2","1","+","3","*"]`, expected output `9`:

((2 + 1) * 3) = 9
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

## Common Mistakes

- **Single Operand**: Expression with only one number
- **Negative Numbers**: Tokens like "-11" (length > 1)
- **Division by Zero**: Not possible with valid RPN
- **Large Numbers**: Integer overflow considerations

- **Operand Order**: Swapping the order of popped operands
- **Negative Number Detection**: Not handling multi-character tokens correctly
- **Stack Underflow**: Not checking if stack has enough operands
- **Integer Division**: Forgetting that division truncates toward zero

---

## References

- [LC 150: Evaluate Reverse Polish Notation on LeetCode](https://www.leetcode.com/problems/evaluate-reverse-polish-notation/)
- [LeetCode Discuss — LC 150: Evaluate Reverse Polish Notation](https://www.leetcode.com/problems/evaluate-reverse-polish-notation/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/evaluate-reverse-polish-notation/editorial/) *(may require premium)*

## Key Takeaways

1. **Stack LIFO**: Last In, First Out property matches RPN evaluation order
2. **Operator Precedence**: RPN eliminates need for operator precedence rules
3. **Operand Order**: First popped operand is the second operand in the operation
4. **Integer Division**: Division truncates toward zero (C++ behavior)
