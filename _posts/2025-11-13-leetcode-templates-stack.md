---
layout: post
title: "Algorithm Templates: Stack"
date: 2025-11-13 19:40:15 -0800
categories: leetcode templates stack data-structures
permalink: /posts/2025-11-13-leetcode-templates-stack/
tags: [leetcode, templates, stack, data-structures]
---

Minimal, copy-paste C++ for parentheses matching, expression evaluation, nested structures, and monotonic stack.

## Contents

- [Parentheses Matching](#parentheses-matching)
- [Expression Evaluation](#expression-evaluation)
- [Nested Structure Processing](#nested-structure-processing)
- [Monotonic Stack](#monotonic-stack)
- [Stack for State Management](#stack-for-state-management)

## Parentheses Matching

Use stack's LIFO property to match opening and closing brackets in reverse order.

```cpp
bool isValid(string s) {
    stack<char> st;
    unordered_map<char, char> map = {
        {'}', '{'}, {']', '['}, {')', '('}
    };
    
    for(char c: s) {
        if(c == '{' || c == '[' || c == '(') {
            st.push(c);
        } else {
            if(st.empty() || st.top() != map[c]) return false;
            st.pop();
        }
    }
    return st.empty();
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 20 | Valid Parentheses | [Link](https://leetcode.com/problems/valid-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-easy-20-valid-parentheses/) |
| 921 | Minimum Add to Make Valid Parentheses | [Link](https://leetcode.com/problems/minimum-add-to-make-valid-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-medium-921-minimum-add-to-make-valid-parentheses/) |
| 1249 | Minimum Remove to Make Valid Parentheses | [Link](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-22-medium-1249-minimum-remove-to-make-valid-parentheses/) |

## Expression Evaluation

Use stack to handle operator precedence and parentheses in mathematical expressions.

```cpp
int calculate(string s) {
    stack<int> stk;
    int result = 0, num = 0, sign = 1;
    
    for(char c: s) {
        if(isdigit(c)) {
            num = num * 10 + (c - '0');
        } else if(c == '+' || c == '-') {
            result += sign * num;
            sign = (c == '+') ? 1 : -1;
            num = 0;
        } else if(c == '(') {
            stk.push(result);
            stk.push(sign);
            result = 0;
            sign = 1;
        } else if(c == ')') {
            result += sign * num;
            result *= stk.top(); stk.pop();
            result += stk.top(); stk.pop();
            num = 0;
        }
    }
    return result + sign * num;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 150 | Evaluate Reverse Polish Notation | [Link](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/medium-150-evaluate-reverse-polish-notation/) |
| 224 | Basic Calculator | [Link](https://leetcode.com/problems/basic-calculator/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-medium-224-basic-calculator/) |
| 227 | Basic Calculator II | [Link](https://leetcode.com/problems/basic-calculator-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-medium-227-basic-calculator-ii/) |
| 772 | Basic Calculator III | [Link](https://leetcode.com/problems/basic-calculator-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-hard-772-basic-calculator-iii/) |

## Nested Structure Processing

Use stack to process nested structures like strings, expressions, or function calls.

```cpp
string decodeString(string s) {
    stack<string> st;
    string curr = "";
    int k = 0;
    
    for(char c: s) {
        if(isdigit(c)) {
            k = k * 10 + (c - '0');
        } else if(c == '[') {
            st.push(to_string(k));
            st.push(curr);
            curr = "";
            k = 0;
        } else if(c == ']') {
            string prev = st.top(); st.pop();
            int count = stoi(st.top()); st.pop();
            string temp = "";
            for(int i = 0; i < count; i++) temp += curr;
            curr = prev + temp;
        } else {
            curr += c;
        }
    }
    return curr;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 394 | Decode String | [Link](https://leetcode.com/problems/decode-string/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-394-decode-string/) |
| 636 | Exclusive Time of Functions | [Link](https://leetcode.com/problems/exclusive-time-of-functions/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-27-medium-636-exclusive-time-of-functions/) |
| 71 | Simplify Path | [Link](https://leetcode.com/problems/simplify-path/) | - |

## Monotonic Stack

Maintain a stack with elements in monotonic order (increasing or decreasing) to efficiently find next/previous greater/smaller elements.

```cpp
vector<int> nextGreater(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> st;
    
    for(int i = 0; i < n; i++) {
        while(!st.empty() && nums[st.top()] < nums[i]) {
            result[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 84 | Largest Rectangle in Histogram | [Link](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/hard-84-largest-rectangle-in-histogram/) |
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 496 | Next Greater Element I | [Link](https://leetcode.com/problems/next-greater-element-i/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/easy-496-next-greater-element-i/) |
| 503 | Next Greater Element II | [Link](https://leetcode.com/problems/next-greater-element-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-503-next-greater-element-ii/) |
| 316 | Remove Duplicate Letters | [Link](https://leetcode.com/problems/remove-duplicate-letters/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-316-remove-duplicate-letters/) |

## Stack for State Management

Use stack to save and restore state when processing nested or hierarchical structures.

```cpp
// Example: Tracking function call stack
void processLogs(vector<string>& logs) {
    stack<pair<int, int>> st;  // {function_id, start_time}
    vector<int> result(n, 0);
    
    for(string& log: logs) {
        // Parse log entry
        if(isStart) {
            st.push({id, time});
        } else {
            auto [funcId, startTime] = st.top();
            st.pop();
            int duration = time - startTime + 1;
            result[funcId] += duration;
            
            // Subtract from parent if exists
            if(!st.empty()) {
                result[st.top().first] -= duration;
            }
        }
    }
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 636 | Exclusive Time of Functions | [Link](https://leetcode.com/problems/exclusive-time-of-functions/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-27-medium-636-exclusive-time-of-functions/) |
| 394 | Decode String | [Link](https://leetcode.com/problems/decode-string/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-394-decode-string/) |

## Key Patterns

1. **LIFO Property**: Stack naturally handles reverse-order matching (parentheses, brackets)
2. **State Preservation**: Save state before entering nested structures, restore after exiting
3. **Operator Precedence**: Use stack to defer low-precedence operations
4. **Monotonic Order**: Maintain sorted order to efficiently find extrema
5. **Index Tracking**: Store indices instead of values when you need position information

## When to Use Stack

- ✅ Matching problems (parentheses, brackets, tags)
- ✅ Expression evaluation with precedence
- ✅ Nested structure processing
- ✅ Finding next/previous greater/smaller elements
- ✅ Reversing order or processing in reverse
- ✅ Undo/redo functionality
- ✅ Function call tracking

## Common Mistakes

1. **Forgetting to check empty stack** before `st.top()` or `st.pop()`
2. **Wrong stack order** when pushing/popping multiple values
3. **Not resetting state** after processing elements
4. **Index vs value** confusion in monotonic stack problems

## More templates

- **Data structures (monotonic stack/queue):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)

