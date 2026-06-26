---
layout: post
title: "Algorithm Templates: Stack"
date: 2025-11-13 19:40:15 -0800
categories: leetcode templates stack data-structures
permalink: /posts/2025-11-13-leetcode-templates-stack/
tags: [leetcode, templates, stack, data-structures]
---

The stack is one of the most versatile data structures in coding interviews. Whether you're matching parentheses, evaluating expressions, or finding the next greater element in an array, a stack gives you an elegant O(n) solution. This guide collects the essential C++ templates you'll need, organized by pattern so you can quickly find the right approach for any stack problem.

> **New to Stack problems?** A stack is Last-In-First-Out (LIFO). The key insight: whenever a problem asks you to match, nest, or find the "next greater/smaller" element, think stack.

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

> **When to use:** matching brackets, nested structures

Use stack's LIFO property to match opening and closing brackets in reverse order.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 220" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="360" y="20" text-anchor="middle" fill="#3A3530" font-size="14" font-weight="bold">Parentheses Matching — Step-by-Step for ({[]})</text>
  <!-- Input: ( { [ ] } ) -->
  <rect x="262" y="30" width="28" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="276" y="46" text-anchor="middle" fill="#3A3530" font-size="13">(</text>
  <rect x="294" y="30" width="28" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="308" y="46" text-anchor="middle" fill="#3A3530" font-size="13">{</text>
  <rect x="326" y="30" width="28" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="340" y="46" text-anchor="middle" fill="#3A3530" font-size="13">[</text>
  <rect x="358" y="30" width="28" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="372" y="46" text-anchor="middle" fill="#3A3530" font-size="13">]</text>
  <rect x="390" y="30" width="28" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="404" y="46" text-anchor="middle" fill="#3A3530" font-size="13">}</text>
  <rect x="422" y="30" width="28" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="436" y="46" text-anchor="middle" fill="#3A3530" font-size="13">)</text>
  <!-- Step 1: push ( -->
  <text x="60" y="76" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 1: (</text>
  <text x="60" y="90" text-anchor="middle" fill="#7A7772" font-size="10">push</text>
  <rect x="37" y="150" width="46" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="60" y="165" text-anchor="middle" fill="#3A3530" font-size="12">(</text>
  <line x1="32" y1="174" x2="88" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <!-- Step 2: push { -->
  <text x="180" y="76" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 2: {</text>
  <text x="180" y="90" text-anchor="middle" fill="#7A7772" font-size="10">push</text>
  <rect x="157" y="126" width="46" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="180" y="141" text-anchor="middle" fill="#3A3530" font-size="12">{</text>
  <rect x="157" y="150" width="46" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="180" y="165" text-anchor="middle" fill="#3A3530" font-size="12">(</text>
  <line x1="152" y1="174" x2="208" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <!-- Step 3: push [ -->
  <text x="300" y="76" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 3: [</text>
  <text x="300" y="90" text-anchor="middle" fill="#7A7772" font-size="10">push</text>
  <rect x="277" y="102" width="46" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="300" y="117" text-anchor="middle" fill="#3A3530" font-size="12">[</text>
  <rect x="277" y="126" width="46" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="300" y="141" text-anchor="middle" fill="#3A3530" font-size="12">{</text>
  <rect x="277" y="150" width="46" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="300" y="165" text-anchor="middle" fill="#3A3530" font-size="12">(</text>
  <line x1="272" y1="174" x2="328" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <!-- Step 4: ] matches [ -->
  <text x="420" y="76" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 4: ]</text>
  <text x="420" y="90" text-anchor="middle" fill="#7A7772" font-size="10">match [ → pop ✓</text>
  <rect x="397" y="126" width="46" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="420" y="141" text-anchor="middle" fill="#3A3530" font-size="12">{</text>
  <rect x="397" y="150" width="46" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="420" y="165" text-anchor="middle" fill="#3A3530" font-size="12">(</text>
  <line x1="392" y1="174" x2="448" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <!-- Step 5: } matches { -->
  <text x="540" y="76" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 5: }</text>
  <text x="540" y="90" text-anchor="middle" fill="#7A7772" font-size="10">match { → pop ✓</text>
  <rect x="517" y="150" width="46" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="540" y="165" text-anchor="middle" fill="#3A3530" font-size="12">(</text>
  <line x1="512" y1="174" x2="568" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <!-- Step 6: ) matches ( -->
  <text x="660" y="76" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 6: )</text>
  <text x="660" y="90" text-anchor="middle" fill="#7A7772" font-size="10">match ( → pop ✓</text>
  <line x1="632" y1="174" x2="688" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <text x="660" y="190" text-anchor="middle" fill="#9A9792" font-size="10">empty</text>
  <!-- Result -->
  <text x="360" y="212" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">Result: Valid ✓ — Stack is empty after processing all characters</text>
</svg>

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

> **When to use:** calculate expression, operator precedence

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

> **When to use:** next greater/smaller element, histogram problems

Eight common patterns that cover nearly all monotonic stack / deque problems. Recognize the pattern by this clue: *"find the next/previous smaller/greater element, or determine how far an element can extend."*

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 260" style="max-width:720px;font-family:monospace">
  <text x="360" y="22" text-anchor="middle" fill="#5A5752" font-size="14" font-weight="bold">Monotonic Stack — Next Greater Element for [2, 1, 4, 3]</text>
  <rect x="230" y="32" width="56" height="28" rx="4" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="258" y="51" text-anchor="middle" fill="#5A5752" font-size="13">2</text>
  <rect x="290" y="32" width="56" height="28" rx="4" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="318" y="51" text-anchor="middle" fill="#5A5752" font-size="13">1</text>
  <rect x="350" y="32" width="56" height="28" rx="4" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="378" y="51" text-anchor="middle" fill="#5A5752" font-size="13">4</text>
  <rect x="410" y="32" width="56" height="28" rx="4" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="438" y="51" text-anchor="middle" fill="#5A5752" font-size="13">3</text>
  <text x="90" y="86" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 1: push 2</text>
  <rect x="65" y="94" width="50" height="28" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="90" y="113" text-anchor="middle" fill="#5A5752" font-size="12">2</text>
  <text x="90" y="138" text-anchor="middle" fill="#5A5752" font-size="10">stack: [2]</text>
  <text x="270" y="86" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 2: push 1</text>
  <text x="270" y="100" text-anchor="middle" fill="#5A5752" font-size="10">(1 &lt; 2, no pop)</text>
  <rect x="245" y="108" width="50" height="28" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="270" y="127" text-anchor="middle" fill="#5A5752" font-size="12">1</text>
  <rect x="245" y="136" width="50" height="28" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="270" y="155" text-anchor="middle" fill="#5A5752" font-size="12">2</text>
  <text x="270" y="180" text-anchor="middle" fill="#5A5752" font-size="10">stack: [2, 1]</text>
  <text x="450" y="86" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 3: push 4</text>
  <text x="450" y="100" text-anchor="middle" fill="#5A5752" font-size="10">4 &gt; 1 → pop, ans[1]=4</text>
  <text x="450" y="113" text-anchor="middle" fill="#5A5752" font-size="10">4 &gt; 2 → pop, ans[0]=4</text>
  <rect x="425" y="122" width="50" height="28" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="450" y="141" text-anchor="middle" fill="#5A5752" font-size="12">4</text>
  <text x="450" y="166" text-anchor="middle" fill="#5A5752" font-size="10">stack: [4]</text>
  <text x="630" y="86" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Step 4: push 3</text>
  <text x="630" y="100" text-anchor="middle" fill="#5A5752" font-size="10">(3 &lt; 4, no pop)</text>
  <rect x="605" y="108" width="50" height="28" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="630" y="127" text-anchor="middle" fill="#5A5752" font-size="12">3</text>
  <rect x="605" y="136" width="50" height="28" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="630" y="155" text-anchor="middle" fill="#5A5752" font-size="12">4</text>
  <text x="630" y="180" text-anchor="middle" fill="#5A5752" font-size="10">stack: [4, 3]</text>
  <text x="360" y="210" text-anchor="middle" fill="#5A5752" font-size="13" font-weight="bold">Result: [4, 4, -1, -1]</text>
  <text x="360" y="228" text-anchor="middle" fill="#5A5752" font-size="11">Elements left on the stack have no next greater element → -1</text>
</svg>

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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 270" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="340" y="20" text-anchor="middle" fill="#3A3530" font-size="14" font-weight="bold">Largest Rectangle in Histogram — [2, 1, 5, 6, 2, 3]</text>
  <!-- Bar 0: h=2 -->
  <rect x="110" y="174" width="68" height="56" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="144" y="168" text-anchor="middle" fill="#5A5752" font-size="11">2</text>
  <!-- Bar 1: h=1 -->
  <rect x="178" y="202" width="68" height="28" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="212" y="196" text-anchor="middle" fill="#5A5752" font-size="11">1</text>
  <!-- Bar 2: h=5 (highlighted) -->
  <rect x="246" y="90" width="68" height="140" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="280" y="84" text-anchor="middle" fill="#5A5752" font-size="11">5</text>
  <!-- Bar 3: h=6 (highlighted) -->
  <rect x="314" y="62" width="68" height="168" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="348" y="56" text-anchor="middle" fill="#5A5752" font-size="11">6</text>
  <!-- Bar 4: h=2 -->
  <rect x="382" y="174" width="68" height="56" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="416" y="168" text-anchor="middle" fill="#5A5752" font-size="11">2</text>
  <!-- Bar 5: h=3 -->
  <rect x="450" y="146" width="68" height="84" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="484" y="140" text-anchor="middle" fill="#5A5752" font-size="11">3</text>
  <!-- Baseline -->
  <line x1="105" y1="230" x2="523" y2="230" stroke="#8B8680" stroke-width="1.5"/>
  <!-- Largest rectangle outline: bars 2-3, height=5 -->
  <rect x="246" y="90" width="136" height="140" fill="none" stroke="#8B8680" stroke-width="2.5" stroke-dasharray="6,3"/>
  <!-- Area label -->
  <text x="314" y="165" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">area = 10</text>
  <!-- Index labels -->
  <text x="144" y="246" text-anchor="middle" fill="#9A9792" font-size="10">0</text>
  <text x="212" y="246" text-anchor="middle" fill="#9A9792" font-size="10">1</text>
  <text x="280" y="246" text-anchor="middle" fill="#9A9792" font-size="10">2</text>
  <text x="348" y="246" text-anchor="middle" fill="#9A9792" font-size="10">3</text>
  <text x="416" y="246" text-anchor="middle" fill="#9A9792" font-size="10">4</text>
  <text x="484" y="246" text-anchor="middle" fill="#9A9792" font-size="10">5</text>
  <!-- Width annotation -->
  <line x1="246" y1="253" x2="382" y2="253" stroke="#5A5752" stroke-width="1"/>
  <line x1="246" y1="249" x2="246" y2="257" stroke="#5A5752" stroke-width="1"/>
  <line x1="382" y1="249" x2="382" y2="257" stroke="#5A5752" stroke-width="1"/>
  <text x="314" y="268" text-anchor="middle" fill="#5A5752" font-size="11">width = 2</text>
  <!-- Height annotation -->
  <line x1="540" y1="90" x2="540" y2="230" stroke="#5A5752" stroke-width="1"/>
  <line x1="536" y1="90" x2="544" y2="90" stroke="#5A5752" stroke-width="1"/>
  <line x1="536" y1="230" x2="544" y2="230" stroke="#5A5752" stroke-width="1"/>
  <text x="554" y="164" text-anchor="start" fill="#5A5752" font-size="11">height = 5</text>
</svg>

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

> **When to use:** sliding window maximum/minimum

Maintain a **monotonic decreasing deque** of indices for sliding window maximum. Remove smaller elements from back, remove out-of-window elements from front.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 210" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="360" y="18" text-anchor="middle" fill="#3A3530" font-size="14" font-weight="bold">Sliding Window Maximum — k = 3</text>
  <!-- Full array -->
  <rect x="206" y="30" width="36" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="224" y="45" text-anchor="middle" fill="#3A3530" font-size="11">1</text>
  <rect x="245" y="30" width="36" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="263" y="45" text-anchor="middle" fill="#3A3530" font-size="11">3</text>
  <rect x="284" y="30" width="36" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="302" y="45" text-anchor="middle" fill="#3A3530" font-size="11">-1</text>
  <rect x="323" y="30" width="36" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="341" y="45" text-anchor="middle" fill="#3A3530" font-size="11">-3</text>
  <rect x="362" y="30" width="36" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="380" y="45" text-anchor="middle" fill="#3A3530" font-size="11">5</text>
  <rect x="401" y="30" width="36" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="419" y="45" text-anchor="middle" fill="#3A3530" font-size="11">3</text>
  <rect x="440" y="30" width="36" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="458" y="45" text-anchor="middle" fill="#3A3530" font-size="11">6</text>
  <rect x="479" y="30" width="36" height="22" rx="3" fill="#F0EBE6" stroke="#B8B5B0"/>
  <text x="497" y="45" text-anchor="middle" fill="#3A3530" font-size="11">7</text>
  <!-- Index labels -->
  <text x="224" y="63" text-anchor="middle" fill="#9A9792" font-size="9">0</text>
  <text x="263" y="63" text-anchor="middle" fill="#9A9792" font-size="9">1</text>
  <text x="302" y="63" text-anchor="middle" fill="#9A9792" font-size="9">2</text>
  <text x="341" y="63" text-anchor="middle" fill="#9A9792" font-size="9">3</text>
  <text x="380" y="63" text-anchor="middle" fill="#9A9792" font-size="9">4</text>
  <text x="419" y="63" text-anchor="middle" fill="#9A9792" font-size="9">5</text>
  <text x="458" y="63" text-anchor="middle" fill="#9A9792" font-size="9">6</text>
  <text x="497" y="63" text-anchor="middle" fill="#9A9792" font-size="9">7</text>
  <!-- Window 1: indices [0..2], elements [1, 3, -1], max=3 -->
  <text x="90" y="85" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Window [0..2]</text>
  <rect x="32" y="95" width="36" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="50" y="110" text-anchor="middle" fill="#3A3530" font-size="11">1</text>
  <rect x="72" y="95" width="36" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="90" y="110" text-anchor="middle" fill="#3A3530" font-size="11">3</text>
  <rect x="112" y="95" width="36" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="130" y="110" text-anchor="middle" fill="#3A3530" font-size="11">-1</text>
  <text x="90" y="136" text-anchor="middle" fill="#7A7772" font-size="10">deque:</text>
  <rect x="52" y="143" width="36" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="70" y="158" text-anchor="middle" fill="#3A3530" font-size="11">3</text>
  <rect x="92" y="143" width="36" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="110" y="158" text-anchor="middle" fill="#3A3530" font-size="11">-1</text>
  <text x="90" y="183" text-anchor="middle" fill="#3A3530" font-size="12" font-weight="bold">max = 3</text>
  <!-- Window 2: indices [1..3], elements [3, -1, -3], max=3 -->
  <text x="270" y="85" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Window [1..3]</text>
  <rect x="212" y="95" width="36" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="230" y="110" text-anchor="middle" fill="#3A3530" font-size="11">3</text>
  <rect x="252" y="95" width="36" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="270" y="110" text-anchor="middle" fill="#3A3530" font-size="11">-1</text>
  <rect x="292" y="95" width="36" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="310" y="110" text-anchor="middle" fill="#3A3530" font-size="11">-3</text>
  <text x="270" y="136" text-anchor="middle" fill="#7A7772" font-size="10">deque:</text>
  <rect x="212" y="143" width="36" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="230" y="158" text-anchor="middle" fill="#3A3530" font-size="11">3</text>
  <rect x="252" y="143" width="36" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="270" y="158" text-anchor="middle" fill="#3A3530" font-size="11">-1</text>
  <rect x="292" y="143" width="36" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="310" y="158" text-anchor="middle" fill="#3A3530" font-size="11">-3</text>
  <text x="270" y="183" text-anchor="middle" fill="#3A3530" font-size="12" font-weight="bold">max = 3</text>
  <!-- Window 3: indices [2..4], elements [-1, -3, 5], max=5 -->
  <text x="450" y="85" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Window [2..4]</text>
  <rect x="392" y="95" width="36" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="410" y="110" text-anchor="middle" fill="#3A3530" font-size="11">-1</text>
  <rect x="432" y="95" width="36" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="450" y="110" text-anchor="middle" fill="#3A3530" font-size="11">-3</text>
  <rect x="472" y="95" width="36" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="490" y="110" text-anchor="middle" fill="#3A3530" font-size="11">5</text>
  <text x="450" y="136" text-anchor="middle" fill="#7A7772" font-size="10">deque:</text>
  <rect x="432" y="143" width="36" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="450" y="158" text-anchor="middle" fill="#3A3530" font-size="11">5</text>
  <text x="450" y="183" text-anchor="middle" fill="#3A3530" font-size="12" font-weight="bold">max = 5</text>
  <!-- Window 4: indices [3..5], elements [-3, 5, 3], max=5 -->
  <text x="630" y="85" text-anchor="middle" fill="#5A5752" font-size="11" font-weight="bold">Window [3..5]</text>
  <rect x="572" y="95" width="36" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="590" y="110" text-anchor="middle" fill="#3A3530" font-size="11">-3</text>
  <rect x="612" y="95" width="36" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="630" y="110" text-anchor="middle" fill="#3A3530" font-size="11">5</text>
  <rect x="652" y="95" width="36" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="670" y="110" text-anchor="middle" fill="#3A3530" font-size="11">3</text>
  <text x="630" y="136" text-anchor="middle" fill="#7A7772" font-size="10">deque:</text>
  <rect x="592" y="143" width="36" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="610" y="158" text-anchor="middle" fill="#3A3530" font-size="11">5</text>
  <rect x="632" y="143" width="36" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="650" y="158" text-anchor="middle" fill="#3A3530" font-size="11">3</text>
  <text x="630" y="183" text-anchor="middle" fill="#3A3530" font-size="12" font-weight="bold">max = 5</text>
  <!-- Output -->
  <text x="360" y="205" text-anchor="middle" fill="#5A5752" font-size="12">Output: [3, 3, 5, 5, 6, 7]</text>
</svg>

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

> **When to use:** remove digits, lexicographic optimization

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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 230" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="330" y="20" text-anchor="middle" fill="#3A3530" font-size="14" font-weight="bold">Min Stack — Parallel Main and Min Stacks</text>
  <!-- Separator lines -->
  <line x1="220" y1="35" x2="220" y2="200" stroke="#E8E3D8" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="440" y1="35" x2="440" y2="200" stroke="#E8E3D8" stroke-width="1" stroke-dasharray="4,3"/>
  <!-- State 1: push(5) -->
  <text x="110" y="48" text-anchor="middle" fill="#5A5752" font-size="12" font-weight="bold">push(5)</text>
  <text x="75" y="68" text-anchor="middle" fill="#7A7772" font-size="10">main</text>
  <text x="145" y="68" text-anchor="middle" fill="#7A7772" font-size="10">min</text>
  <rect x="53" y="150" width="44" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="75" y="165" text-anchor="middle" fill="#3A3530" font-size="12">5</text>
  <line x1="48" y1="174" x2="102" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <rect x="123" y="150" width="44" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="145" y="165" text-anchor="middle" fill="#3A3530" font-size="12">5</text>
  <line x1="118" y1="174" x2="172" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <!-- State 2: push(3) -->
  <text x="330" y="48" text-anchor="middle" fill="#5A5752" font-size="12" font-weight="bold">push(3)</text>
  <text x="295" y="68" text-anchor="middle" fill="#7A7772" font-size="10">main</text>
  <text x="365" y="68" text-anchor="middle" fill="#7A7772" font-size="10">min</text>
  <rect x="273" y="126" width="44" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="295" y="141" text-anchor="middle" fill="#3A3530" font-size="12">3</text>
  <rect x="273" y="150" width="44" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="295" y="165" text-anchor="middle" fill="#3A3530" font-size="12">5</text>
  <line x1="268" y1="174" x2="322" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <rect x="343" y="126" width="44" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="365" y="141" text-anchor="middle" fill="#3A3530" font-size="12">3</text>
  <rect x="343" y="150" width="44" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="365" y="165" text-anchor="middle" fill="#3A3530" font-size="12">5</text>
  <line x1="338" y1="174" x2="392" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <!-- State 3: push(7) -->
  <text x="550" y="48" text-anchor="middle" fill="#5A5752" font-size="12" font-weight="bold">push(7)</text>
  <text x="515" y="68" text-anchor="middle" fill="#7A7772" font-size="10">main</text>
  <text x="585" y="68" text-anchor="middle" fill="#7A7772" font-size="10">min</text>
  <rect x="493" y="102" width="44" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="515" y="117" text-anchor="middle" fill="#3A3530" font-size="12">7</text>
  <rect x="493" y="126" width="44" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="515" y="141" text-anchor="middle" fill="#3A3530" font-size="12">3</text>
  <rect x="493" y="150" width="44" height="22" rx="3" fill="#D4D8E0" stroke="#B8B5B0"/>
  <text x="515" y="165" text-anchor="middle" fill="#3A3530" font-size="12">5</text>
  <line x1="488" y1="174" x2="542" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <rect x="563" y="102" width="44" height="22" rx="3" fill="#E8D5D0" stroke="#B8B5B0"/>
  <text x="585" y="117" text-anchor="middle" fill="#3A3530" font-size="12">3</text>
  <rect x="563" y="126" width="44" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="585" y="141" text-anchor="middle" fill="#3A3530" font-size="12">3</text>
  <rect x="563" y="150" width="44" height="22" rx="3" fill="#D4D8D0" stroke="#B8B5B0"/>
  <text x="585" y="165" text-anchor="middle" fill="#3A3530" font-size="12">5</text>
  <line x1="558" y1="174" x2="612" y2="174" stroke="#B8B5B0" stroke-width="2"/>
  <!-- Key insight annotation -->
  <text x="550" y="196" text-anchor="middle" fill="#5A5752" font-size="11">↑ min(7, 3) = 3 → push 3</text>
  <text x="330" y="222" text-anchor="middle" fill="#7A7772" font-size="11">Each push records min(val, minStk.top()) — getMin() is always O(1)</text>
</svg>

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

## Quick Reference

| Pattern | Signal Phrases | Key Idea |
|---|---|---|
| Parentheses | "valid brackets", "minimum remove" | Match open/close pairs |
| Expression | "calculate", "evaluate" | Operator precedence via stack |
| Next Greater | "next greater", "next warmer day" | Monotonic decreasing stack |
| Next Smaller | "next smaller", "stock span" | Monotonic increasing stack |
| Histogram | "largest rectangle", "maximal rectangle" | Expand left/right using stack |
| Sliding Window Max | "maximum in window" | Monotonic deque |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures (monotonic stack/queue):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
