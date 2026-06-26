---
layout: post
title: "[Medium] 155. Min Stack"
date: 2026-02-11
categories: [leetcode, medium, stack]
tags: [leetcode, medium, stack, data-structure-design]
permalink: /2026/02/11/medium-155-min-stack/
---
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

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

## Thinking Process

To achieve O(1) for `getMin()`, we need to keep track of the minimum value at every state of the stack.

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
- **Time Complexity**: O(1) for all operations.
- **Space Complexity**: O(N) to store N elements and their corresponding minimums.



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

### Solution Explanation

**Approach:** Monotonic stack (this problem)

**Key idea:** To achieve O(1) for `getMin()`, we need to keep track of the minimum value at every state of the stack.

**How the code works:**
- When `push(val)`:
- Push `val` to the main stack.
- If `minStk` is empty, push `val` to `minStk`.
- Otherwise, push `min(val, minStk.top())` to `minStk`. This ensures that `minStk.top()` always reflects the minimum of all elements currently in the main stack.
- When `pop()`:
- Pop from both the main stack and `minStk`.

- **Time Complexity**: O(1) for all operations.
- **Space Complexity**: O(N) to store N elements and their corresponding minimums.
## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

- **Pattern:** Monotonic stack (this problem)
- When `push(val)`:
- Push `val` to the main stack.

## References

- [LC 155: Min Stack on LeetCode](https://www.leetcode.com/problems/min-stack/)
- [LeetCode Discuss — LC 155: Min Stack](https://www.leetcode.com/problems/min-stack/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/min-stack/editorial/) *(may require premium)*

## Template Reference

- [Stack](/blog_leetcode/posts/2025-11-13-leetcode-templates-stack/)
- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
