---
layout: post
title: "LeetCode Templates: Calculator Problems"
date: 2025-11-13 19:40:15 -0800
categories: leetcode templates calculator expression-evaluation
permalink: /posts/2025-11-13-leetcode-templates-calculator/
tags: [leetcode, templates, calculator, expression-evaluation, stack]
---

## Contents

- [Basic Calculator (+, -, parentheses)](#basic-calculator---parentheses)
- [Basic Calculator II (+, -, *, /)](#basic-calculator-ii---)
- [Basic Calculator III (All operators + parentheses)](#basic-calculator-iii-all-operators--parentheses)
- [Common Patterns](#common-patterns)
- [Comparison Table](#comparison-table)

## Basic Calculator (+, -, parentheses)

Handles addition, subtraction, and parentheses. Use stack to save state before entering parentheses.

```cpp
int calculate(string s) {
    stack<int> stk;
    int result = 0, num = 0, sign = 1;
    
    for(char c: s) {
        if(isdigit(c)) {
            num = num * 10 + (c - '0');
        }
        switch(c) {
            case '+':
                result += sign * num;
                sign = 1;
                num = 0;
                break;
            case '-':
                result += sign * num;
                sign = -1;
                num = 0;
                break;
            case '(':
                stk.push(result);
                stk.push(sign);
                sign = 1;
                result = 0;
                break;
            case ')':
                result += sign * num;
                result *= stk.top(); stk.pop();
                result += stk.top(); stk.pop();
                num = 0;
                break;
        }
    }
    return result + (sign * num);
}
```

**Key Points:**
- Save `result` and `sign` before `(`
- Apply saved `sign` and add to saved `result` after `)`
- Track current `sign` for each number

| ID | Title | Link | Solution |
|---|---|---|---|
| 224 | Basic Calculator | [Link](https://leetcode.com/problems/basic-calculator/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-medium-224-basic-calculator/) |

## Basic Calculator II (+, -, *, /)

Handles all four operators without parentheses. Evaluate `*` and `/` immediately, defer `+` and `-`.

```cpp
int calculate(string s) {
    stack<int> stk;
    char operation = '+';
    int curr = 0;
    
    for(int i = 0; i < s.length(); i++) {
        char ch = s[i];
        
        if(isdigit(ch)) {
            curr = (curr * 10) + (ch - '0');
        }
        
        if((!isdigit(ch) && !isspace(ch)) || i == s.length() - 1) {
            switch(operation) {
                case '+':
                    stk.push(curr);
                    break;
                case '-':
                    stk.push(-curr);
                    break;
                case '*':
                    stk.top() *= curr;
                    break;
                case '/':
                    stk.top() /= curr;
                    break;
            }
            operation = ch;
            curr = 0;
        }
    }
    
    int result = 0;
    while(!stk.empty()) {
        result += stk.top();
        stk.pop();
    }
    return result;
}
```

**Key Points:**
- Evaluate `*` and `/` immediately (high precedence)
- Defer `+` and `-` by pushing to stack
- Sum all stack elements at the end

**Optimized Version (O(1) space):**
```cpp
int calculate(string s) {
    int curr = 0, last = 0, result = 0;
    char sign = '+';
    
    for(int i = 0; i < s.length(); i++) {
        char c = s[i];
        if(isdigit(c)) {
            curr = curr * 10 + (c - '0');
        }
        
        if((!isdigit(c) && !isspace(c)) || i == s.length() - 1) {
            if(sign == '+' || sign == '-') {
                result += last;
                last = (sign == '+') ? curr : -curr;
            } else if(sign == '*') {
                last = last * curr;
            } else if(sign == '/') {
                last = last / curr;
            }
            sign = c;
            curr = 0;
        }
    }
    return result + last;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 227 | Basic Calculator II | [Link](https://leetcode.com/problems/basic-calculator-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-medium-227-basic-calculator-ii/) |

## Basic Calculator III (All operators + parentheses)

Combines all operators with parentheses. Use recursion or stack to handle nesting.

```cpp
class Solution {
private:
    int parseExpr(const string& s, int& idx) {
        char op = '+';
        vector<int> stk;
        
        for(; idx < s.size(); idx++) {
            if(isspace(s[idx])) continue;
            
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
            
            if(idx + 1 < s.size()) {
                op = s[idx + 1];
            }
        }
        
        int result = 0;
        for(int num: stk) result += num;
        return result;
    }
    
    long parseNum(const string& s, int& idx) {
        long num = 0;
        while(idx < s.size() && isdigit(s[idx])) {
            num = num * 10 + (s[idx] - '0');
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

**Key Points:**
- Recursion naturally handles nested parentheses
- Combine stack approach for operators with recursive approach for parentheses
- Evaluate `*` and `/` immediately, defer `+` and `-`

| ID | Title | Link | Solution |
|---|---|---|---|
| 772 | Basic Calculator III | [Link](https://leetcode.com/problems/basic-calculator-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-hard-772-basic-calculator-iii/) |

## Common Patterns

### 1. Number Building
```cpp
int num = 0;
for(char c: s) {
    if(isdigit(c)) {
        num = num * 10 + (c - '0');
    }
}
```

### 2. Sign Tracking
```cpp
int sign = 1;  // 1 for positive, -1 for negative
// Apply: result += sign * num;
```

### 3. Operator Precedence
```cpp
// High precedence: evaluate immediately
if(op == '*' || op == '/') {
    // Immediate evaluation
} else {
    // Defer to stack
}
```

### 4. Parentheses Handling
```cpp
// Stack approach
if(c == '(') {
    stk.push(result);
    stk.push(sign);
    result = 0;
    sign = 1;
} else if(c == ')') {
    result += sign * num;
    result *= stk.top(); stk.pop();
    result += stk.top(); stk.pop();
}

// Recursive approach
if(c == '(') {
    num = parseExpr(s, ++idx);
}
```

## Comparison Table

| Problem | Operators | Parentheses | Approach | Complexity |
|---------|-----------|-------------|----------|------------|
| **224** | `+`, `-` | ✅ | Stack (save state) | O(n) time, O(n) space |
| **227** | `+`, `-`, `*`, `/` | ❌ | Stack or variables | O(n) time, O(n) or O(1) space |
| **772** | `+`, `-`, `*`, `/` | ✅ | Recursion + Stack | O(n) time, O(n) space |

## Key Insights

1. **Operator Precedence**: `*` and `/` have higher precedence than `+` and `-`
2. **Immediate vs Deferred**: High precedence operators are evaluated immediately
3. **Parentheses**: Create nested evaluation contexts - use stack or recursion
4. **Sign Propagation**: Track signs through parentheses using stack
5. **Number Building**: Accumulate digits to form multi-digit numbers

## Related Problems

- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) - Postfix notation
- [394. Decode String](https://leetcode.com/problems/decode-string/) - Nested structure processing
- [71. Simplify Path](https://leetcode.com/problems/simplify-path/) - Path processing with stack

## Common Mistakes

1. **Forgetting final number**: Not adding `sign * num` at the end
2. **Wrong operator precedence**: Evaluating `+` before `*`
3. **Stack order**: Pushing/popping in wrong order for parentheses
4. **Sign handling**: Not applying saved sign correctly after `)`
5. **Number reset**: Not resetting `num` after processing operators

