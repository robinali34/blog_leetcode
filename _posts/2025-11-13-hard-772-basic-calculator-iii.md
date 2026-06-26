---
layout: post
title: "[Hard] 772. Basic Calculator III"
date: 2025-11-13 19:15:52 -0800
categories: leetcode algorithm hard cpp string stack recursion expression-evaluation problem-solving
permalink: /posts/2025-11-13-hard-772-basic-calculator-iii/
tags: [leetcode, hard, string, stack, calculator, recursion, expression-evaluation, parentheses]
---
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

## Thinking Process

1. **Recursion for Parentheses**: Natural way to handle nested structures

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
| **Monotonic stack** *(this problem)* | O(n) | O(n) | Next greater/smaller element |
| Parentheses matching | O(n) | O(n) | Push open, pop on close |
| Expression evaluation | O(n) | O(n) | Operand + operator stacks |
| Stack simulation | O(n) | O(n) | Process in LIFO order |

## Solution

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

### Solution Explanation

**Approach:** Monotonic stack (this problem)

**Key idea:** 1. **Recursion for Parentheses**: Natural way to handle nested structures

**How the code works:**
1. **Recursion for Parentheses**: Natural way to handle nested structures
- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in O(n).

**Walkthrough** — input `s = "1+1"`, expected output `2`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive** | O(n) | O(n) | Natural for nested structures |
| **Iterative (2 stacks)** | O(n) | O(n) | More explicit state management |
| **Simplified Iterative** | O(n) | O(n) | Cleaner code, single stack |
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

### Complexity
| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive** | O(n) | O(n) | Natural for nested structures |
| **Iterative (2 stacks)** | O(n) | O(n) | More explicit state management |
| **Simplified Iterative** | O(n) | O(n) | Cleaner code, single stack |

## Common Mistakes

1. **Nested parentheses**: `"((1+2)*3)"` → `9`
2. **No parentheses**: `"1+2*3"` → `7`
3. **Single number**: `"42"` → `42`
4. **Negative results**: `"1-2"` → `-1`
5. **Division truncation**: `"5/2"` → `2`
6. **Multiple spaces**: `"1 + 2"` → `3`

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

- [224. Basic Calculator](https://www.leetcode.com/problems/basic-calculator/) - Only `+`, `-`, parentheses
- [227. Basic Calculator II](https://www.leetcode.com/problems/basic-calculator-ii/) - `+`, `-`, `*`, `/` (no parentheses)
- [772. Basic Calculator III](https://www.leetcode.com/problems/basic-calculator-iii/) - This problem (all operators + parentheses)
- [394. Decode String](https://www.leetcode.com/problems/decode-string/) - Nested structure evaluation

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

## Key Takeaways

1. **Recursion for Parentheses**: Natural way to handle nested structures
2. **Stack for State**: Save evaluation state before entering parentheses
3. **Operator Precedence**: Evaluate `*` and `/` immediately, defer `+` and `-`
4. **Index Management**: Careful index tracking in recursive approach
5. **Number Building**: Accumulate multi-digit numbers correctly

## References

- [LC 772: Basic Calculator III on LeetCode](https://www.leetcode.com/problems/basic-calculator-iii/)
- [LeetCode Discuss — LC 772: Basic Calculator III](https://www.leetcode.com/problems/basic-calculator-iii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/basic-calculator-iii/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
