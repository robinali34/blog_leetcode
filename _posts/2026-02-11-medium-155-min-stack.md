---
layout: post
title: "LeetCode 155. Min Stack"
date: 2026-02-11
categories: [leetcode, medium, stack]
tags: [leetcode, medium, stack, data-structure-design]
permalink: /2026/02/11/medium-155-min-stack/
---

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

## Problem Description

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

## Examples

**Example 1:**

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top`, and `getMin` will always be called on **non-empty** stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## Approach

To achieve $O(1)$ for `getMin()`, we need to keep track of the minimum value at every state of the stack.

### Two Stacks Approach
We can use an auxiliary stack called `minStk` to store the minimum value encountered so far.
- When `push(val)`: 
    - Push `val` to the main stack.
    - If `minStk` is empty, push `val` to `minStk`.
    - Otherwise, push `min(val, minStk.top())` to `minStk`. This ensures that `minStk.top()` always reflects the minimum of all elements currently in the main stack.
- When `pop()`:
    - Pop from both the main stack and `minStk`.
- When `top()`:
    - Return the top of the main stack.
- When `getMin()`:
    - Return the top of `minStk`.

### Complexity
- **Time Complexity**: $O(1)$ for all operations.
- **Space Complexity**: $O(N)$ to store $N$ elements and their corresponding minimums.

## Solution

{% raw %}
```cpp
class MinStack {
public:
    MinStack() {
    }
    
    void push(int val) {
        stk.push(val);
        // If minStk is empty, the first value is the minimum
        if (minStk.empty()) {
            minStk.push(val);
        } else {
            // Push the current minimum (either existing top or new val)
            minStk.push(min(minStk.top(), val));
        }
    }
    
    void pop() {
        stk.pop();
        minStk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minStk.top();
    }

private:
    stack<int> stk;
    stack<int> minStk;
};
```
{% endraw %}

## Template Reference

- [Stack](/blog_leetcode/posts/2025-11-13-leetcode-templates-stack/)
- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
