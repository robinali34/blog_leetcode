---
layout: post
title: "[Hard] 1944. Number of Visible People in a Queue"
date: 2026-02-09 00:00:00 -0700
categories: [leetcode, hard, stack, monotonic-stack]
permalink: /2026/02/09/hard-1944-number-of-visible-people-in-a-queue/
tags: [leetcode, hard, stack, monotonic-stack]
---
There are `n` people standing in a queue numbered from `0` to `n - 1` from left to right. You are given an array `heights` of **distinct** integers where `heights[i]` represents the height of the `i-th` person.

A person `i` can see person `j` (where `i < j`) if everyone between them is **shorter** than both of them. More formally, person `i` can see person `j` if:
*   `i < j`, and
*   `min(heights[i], heights[j]) > max(heights[i + 1], heights[i + 2], ..., heights[j - 1])`.

Return an array `answer` where `answer[i]` is the **number of people** the `i-th` person can see to their **right** in the queue.

## Examples

**Example 1:**

```
Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Explanation:
- Person 0 can see person 1, 2, and 4.
  - Person 3 is blocked by person 2.
  - Person 5 is blocked by person 4.
- Person 1 can see person 2.
- Person 2 can see person 3 and 4.
- Person 3 can see person 4.
- Person 4 can see person 5.
- Person 5 can see no one since nobody is to the right of them.
```

**Example 2:**

```
Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]
```

## Constraints

*   `n == heights.length`
*   `1 <= n <= 10^5`
*   `1 <= heights[i] <= 10^5`
*   All the values of `heights` are **unique**.

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Monotonic stack** *(this problem)* | $O(n)$ | $O(n)$ | Next greater/smaller element |
| Parentheses matching | $O(n)$ | $O(n)$ | Push open, pop on close |
| Expression evaluation | $O(n)$ | $O(n)$ | Operand + operator stacks |
| Stack simulation | $O(n)$ | $O(n)$ | Process in LIFO order |

## Thinking Process

We maintain a **monotonic decreasing stack** from right to left.

1.  Iterate through the `heights` array from right to left ($n-1$ down to $0$).
2.  For each person $i$:
    *   While the stack is not empty and the current person `heights[i]` is taller than the person at the top of the stack `st.top()`:
        *   Person $i$ can see `st.top()`.
        *   Pop `st.top()` and increment the count for person $i$.
        *   Why? Because `st.top()` was the shortest person currently available to the right, and `heights[i]` blocks anyone behind them from seeing `st.top()`, but person $i$ sees them.
    *   If the stack is still not empty after the pops:
        *   Person $i$ can see the current `st.top()` (who is taller than `heights[i]`).
        *   Increment the count for person $i$.
        *   This person blocks person $i$ from seeing anyone further to the right.
    *   Push the current person `heights[i]` onto the stack.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Stack</text>

  <rect x="100" y="30" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="46" text-anchor="middle" font-size="10">top</text>
  <rect x="100" y="54" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="100" y="78" width="80" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="200" y="70" font-size="11" fill="#6B6560">push / pop</text>
  <path d="M90 42v60" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="115" text-anchor="middle" font-size="11" fill="#6B6560">LIFO — monotonic stack scans array</text>

</svg>

## Solution Code

```cpp
class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        int n = heights.size();
        vector<int> rtn(n, 0);
        stack<int> st;
        
        // Iterate from right to left
        for(int i = n - 1; i >= 0; i--) {
            // Person i can see everyone in the stack that is shorter than them
            while(!st.empty() && heights[i] > st.top()) {
                st.pop();
                rtn[i]++;
            }
            // If there's someone left in the stack, they are taller than person i
            // Person i can see this taller person, but no one beyond them
            if(!st.empty()) {
                rtn[i]++;
            }
            // Push current height to maintain monotonic decreasing stack (from top)
            st.push(heights[i]);
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Monotonic stack (this problem)

**Key idea:** We maintain a **monotonic decreasing stack** from right to left.

**How the code works:**
1.  Iterate through the `heights` array from right to left ($n-1$ down to $0$).
2.  For each person $i$:
*   While the stack is not empty and the current person `heights[i]` is taller than the person at the top of the stack `st.top()`:
*   Person $i$ can see `st.top()`.
*   Pop `st.top()` and increment the count for person $i$.
*   Why? Because `st.top()` was the shortest person currently available to the right, and `heights[i]` blocks anyone behind them from seeing `st.top()`, but person $i$ sees them.

**Walkthrough** — input `heights = [10,6,8,5,11,9]`, expected output `[3,1,2,1,1,0]`:

- Person 0 can see person 1, 2, and 4.
  - Person 3 is blocked by person 2.
  - Person 5 is blocked by person 4.
- Person 1 can see person 2.
- Person 2 can see person 3 and 4.
- Person 3 can see person 4.
- Person 4 can see person 5.
- Person 5 can see no one since nobody is to the right of them.

*   **Time Complexity**: $O(n)$. Each element is pushed and popped from the stack at most once.
*   **Space Complexity**: $O(n)$ for the stack and the result array.
## Example Walkthrough

Let's walk through **Example 1**: `heights = [10, 6, 8, 5, 11, 9]`

We process from **right to left** ($i = 5 \to 0$):

| Step ($i$) | Height | Stack (top at right) | Logic | Pop Count | Visible | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | 9 | `[]` | Stack is empty | 0 | **0** | Push 9 |
| 4 | 11 | `[9]` | 11 > 9, pop 9 | 1 | 1 + 0 = **1** | Push 11 |
| 3 | 5 | `[11]` | 5 < 11, don't pop | 0 | 0 + 1 = **1** | Push 5 |
| 2 | 8 | `[11, 5]` | 8 > 5, pop 5 | 1 | 1 + 1 = **2** | Push 8 |
| 1 | 6 | `[11, 8]` | 6 < 8, don't pop | 0 | 0 + 1 = **1** | Push 6 |
| 0 | 10 | `[11, 8, 6]` | 10 > 6, 10 > 8, pop both | 2 | 2 + 1 = **3** | Push 10 |

**Final Result**: `[3, 1, 2, 1, 1, 0]`

### Why this works:
1.  **Popping shorter people**: If current person $i$ is taller than person $j$ on the stack, person $i$ can definitely see person $j$. Person $j$ is then removed because anyone to the left of person $i$ will have their view of person $j$ blocked by person $i$.
2.  **The "+1" logic**: After popping everyone shorter, if the stack isn't empty, the person at the top is the first person taller than current person $i$. Person $i$ can see this person, but they block person $i$ from seeing anyone further right.

### Complexity
*   **Time Complexity**: $O(n)$. Each element is pushed and popped from the stack at most once.
*   **Space Complexity**: $O(n)$ for the stack and the result array.

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

*   [739. Daily Temperatures](https://www.leetcode.com/problems/daily-temperatures/)
*   [496. Next Greater Element I](https://www.leetcode.com/problems/next-greater-element-i/)
*   [84. Largest Rectangle in Histogram](https://www.leetcode.com/problems/largest-rectangle-in-histogram/)

## Key Takeaways

- **Pattern:** Monotonic stack (this problem)
- While the stack is not empty and the current person `heights[i]` is taller than the person at the top of the stack `st.top()`:
- Person $i$ can see `st.top()`.

## References

- [LC 1944: Number of Visible People in a Queue on LeetCode](https://www.leetcode.com/problems/number-of-visible-people-in-a-queue/)
- [LeetCode Discuss — LC 1944: Number of Visible People in a Queue](https://www.leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/number-of-visible-people-in-a-queue/editorial/) *(may require premium)*

## Template Reference

See [Monotonic Stack Templates](/posts/2025-10-29-leetcode-templates-data-structures/#monotonic-stack) for more patterns.
