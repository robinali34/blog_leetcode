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
- [Monotonic Stack & Deque Patterns](#monotonic-stack--deque-patterns)
  - [Pattern 1: Next Greater Element](#pattern-1-next-greater-element)
  - [Pattern 2: Next Smaller Element](#pattern-2-next-smaller-element)
  - [Pattern 3: Previous Greater / Smaller Element](#pattern-3-previous-greater--smaller-element)
  - [Pattern 4: Histogram Expansion](#pattern-4-histogram-expansion)
  - [Pattern 5: Matrix → Histogram Trick](#pattern-5-matrix--histogram-trick)
  - [Pattern 6: Monotonic Deque (Sliding Window)](#pattern-6-monotonic-deque-sliding-window-maxmin)
  - [Pattern 7: Greedy Stack](#pattern-7-greedy-stack-remove-digits--lexicographic-optimization)
  - [Pattern 8: Prefix Sum + Monotonic Deque](#pattern-8-prefix-sum--monotonic-deque)
  - [Practice Roadmap](#practice-roadmap)
- [Stack for State Management](#stack-for-state-management)
- [Stack Design](#stack-design-minmax-stack)

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

## Monotonic Stack & Deque Patterns

Eight common patterns that cover nearly all monotonic stack / deque problems. Recognize the pattern by this clue: *"find the next/previous smaller/greater element, or determine how far an element can extend."*

---

### Pattern 1: Next Greater Element

Find the first element **to the right** that is strictly greater. Use a **monotonic decreasing** stack (top is smallest).

```cpp
vector<int> nextGreater(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, -1);
    stack<int> st;

    for (int i = 0; i < n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i]) {
            ans[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    return ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 496 | Next Greater Element I | [Link](https://leetcode.com/problems/next-greater-element-i/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/easy-496-next-greater-element-i/) |
| 739 | Daily Temperatures | [Link](https://leetcode.com/problems/daily-temperatures/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/29/medium-739-daily-temperatures/) |
| 503 | Next Greater Element II | [Link](https://leetcode.com/problems/next-greater-element-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-503-next-greater-element-ii/) |
| 901 | Online Stock Span | [Link](https://leetcode.com/problems/online-stock-span/) | - |
| 1944 | Visible People in Queue | [Link](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/09/hard-1944-number-of-visible-people-in-a-queue/) |

---

### Pattern 2: Next Smaller Element

Same idea but reversed comparison. Use a **monotonic increasing** stack (top is largest).

```cpp
vector<int> nextSmaller(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, -1);
    stack<int> st;

    for (int i = 0; i < n; i++) {
        while (!st.empty() && nums[st.top()] > nums[i]) {
            ans[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    return ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1475 | Final Prices With Special Discount | [Link](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) | - |
| 84 | Largest Rectangle in Histogram | [Link](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/hard-84-largest-rectangle-in-histogram/) |

---

### Pattern 3: Previous Greater / Smaller Element

Instead of looking right, find the **left boundary**. Scan left-to-right, the stack top is the previous greater/smaller.

Finding both **previous smaller** and **next smaller** defines the range where an element is the minimum -- critical for range-based counting.

```cpp
// Previous smaller element (strictly)
vector<int> prevSmaller(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, -1);
    stack<int> st;

    for (int i = 0; i < n; i++) {
        while (!st.empty() && nums[st.top()] >= nums[i])
            st.pop();
        if (!st.empty()) ans[i] = st.top();
        st.push(i);
    }
    return ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 907 | Sum of Subarray Minimums | [Link](https://leetcode.com/problems/sum-of-subarray-minimums/) | - |
| 2104 | Sum of Subarray Ranges | [Link](https://leetcode.com/problems/sum-of-subarray-ranges/) | - |

---

### Pattern 4: Histogram Expansion

Each bar expands left and right until hitting a shorter bar. Width = `right_smaller - left_smaller - 1`.

Combine **next smaller** (right boundary) and **previous smaller** (left boundary) to compute the maximum rectangle.

```cpp
int largestRectangleArea(vector<int>& heights) {
    int n = heights.size(), ans = 0;
    stack<int> st;

    for (int i = 0; i <= n; i++) {
        int h = (i == n) ? 0 : heights[i];
        while (!st.empty() && heights[st.top()] > h) {
            int height = heights[st.top()]; st.pop();
            int width = st.empty() ? i : i - st.top() - 1;
            ans = max(ans, height * width);
        }
        st.push(i);
    }
    return ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 84 | Largest Rectangle in Histogram | [Link](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/hard-84-largest-rectangle-in-histogram/) |
| 42 | Trapping Rain Water | [Link](https://leetcode.com/problems/trapping-rain-water/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/17/hard-42-trapping-rain-water/) |

---

### Pattern 5: Matrix → Histogram Trick

Convert each row of a binary matrix into a histogram of heights, then run the histogram algorithm on each row.

```cpp
int maximalRectangle(vector<vector<char>>& matrix) {
    if (matrix.empty()) return 0;
    int m = matrix.size(), n = matrix[0].size(), ans = 0;
    vector<int> heights(n, 0);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++)
            heights[j] = (matrix[i][j] == '1') ? heights[j] + 1 : 0;
        ans = max(ans, largestRectangleArea(heights));
    }
    return ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 85 | Maximal Rectangle | [Link](https://leetcode.com/problems/maximal-rectangle/) | - |

---

### Pattern 6: Monotonic Deque (Sliding Window Max/Min)

Maintain a **monotonic decreasing deque** of indices for sliding window maximum. Remove smaller elements from back, remove out-of-window elements from front.

```cpp
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;
    vector<int> ans;

    for (int i = 0; i < (int)nums.size(); i++) {
        while (!dq.empty() && nums[dq.back()] <= nums[i])
            dq.pop_back();
        dq.push_back(i);
        if (dq.front() <= i - k) dq.pop_front();
        if (i >= k - 1) ans.push_back(nums[dq.front()]);
    }
    return ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |

---

### Pattern 7: Greedy Stack (Remove Digits / Lexicographic Optimization)

Use the stack to maintain an optimal ordering. While the stack top is worse than the current element and we still have removals left, pop it.

```cpp
string removeKdigits(string num, int k) {
    string st;
    for (char c : num) {
        while (k > 0 && !st.empty() && st.back() > c) {
            st.pop_back();
            k--;
        }
        st.push_back(c);
    }
    while (k-- > 0) st.pop_back();

    // strip leading zeros
    int start = 0;
    while (start < (int)st.size() && st[start] == '0') start++;
    string ans = st.substr(start);
    return ans.empty() ? "0" : ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 402 | Remove K Digits | [Link](https://leetcode.com/problems/remove-k-digits/) | - |
| 316 | Remove Duplicate Letters | [Link](https://leetcode.com/problems/remove-duplicate-letters/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-316-remove-duplicate-letters/) |

---

### Pattern 8: Prefix Sum + Monotonic Deque

Find the shortest subarray with sum at least `k`. Combine prefix sums with an **increasing deque** to efficiently find the closest valid left boundary.

```cpp
int shortestSubarray(vector<int>& nums, int k) {
    int n = nums.size(), ans = n + 1;
    vector<long long> pre(n + 1, 0);
    for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + nums[i];

    deque<int> dq;
    for (int i = 0; i <= n; i++) {
        while (!dq.empty() && pre[i] - pre[dq.front()] >= k) {
            ans = min(ans, i - dq.front());
            dq.pop_front();
        }
        while (!dq.empty() && pre[dq.back()] >= pre[i])
            dq.pop_back();
        dq.push_back(i);
    }
    return ans <= n ? ans : -1;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 862 | Shortest Subarray with Sum at Least K | [Link](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/26/hard-862-shortest-subarray-with-sum-at-least-k/) |

---

### Practice Roadmap

Follow this progression from basics to advanced:

| Step | Focus | Problems |
|---|---|---|
| 1 | Basics | Next Greater Element I (496), Daily Temperatures (739) |
| 2 | Core Stack Mastery | Next Greater Element II (503), Online Stock Span (901) |
| 3 | Histogram | Largest Rectangle in Histogram (84), Maximal Rectangle (85) |
| 4 | Advanced Range Counting | Sum of Subarray Minimums (907), Sum of Subarray Ranges (2104) |
| 5 | Deque + Advanced | Sliding Window Maximum (239), Shortest Subarray with Sum at Least K (862) |

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

## Stack Design (Min/Max Stack)

Maintaining extra information (like minimums or frequencies) alongside the primary stack data.

```cpp
class MinStack {
    stack<int> stk, minStk;
public:
    void push(int val) {
        stk.push(val);
        if (minStk.empty()) minStk.push(val);
        else minStk.push(min(minStk.top(), val));
    }
    void pop() { stk.pop(); minStk.pop(); }
    int top() { return stk.top(); }
    int getMin() { return minStk.top(); }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 155 | Min Stack | [Link](https://leetcode.com/problems/min-stack/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/11/medium-155-min-stack/) |
| 716 | Max Stack | [Link](https://leetcode.com/problems/max-stack/) | - |

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

