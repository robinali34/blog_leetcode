---
layout: post
title: "1944. Number of Visible People in a Queue"
date: 2026-02-09 00:00:00 -0700
categories: [leetcode, hard, stack, monotonic-stack]
permalink: /2026/02/09/hard-1944-number-of-visible-people-in-a-queue/
tags: [leetcode, hard, stack, monotonic-stack]
---

# 1944. Number of Visible People in a Queue

## Problem Statement

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

## Clarification Questions

1.  **Strictly shorter?**: Does "everyone between them is shorter" mean strictly shorter? (Assumption: Yes, and since all heights are unique, this is simplified)
2.  **Can someone see themselves?**: No, only people to their right ($i < j$).
3.  **Does height[j] block people behind them?**: Yes, if someone to the right of person $j$ is being viewed by person $i$, person $j$ must be shorter than person $i$.

## Interview Deduction Process

1.  **Understand the constraint**: For person $i$ to see person $j$, every person in between $[i+1, j-1]$ must be shorter than both $i$ and $j$.
2.  **Monotonic Property**: 
    *   If person $i$ is looking to the right, they can see a sequence of people with increasing heights (from their perspective).
    *   Once they encounter someone taller than themselves, they can't see anyone beyond that person.
    *   Also, any person $j$ that is shorter than a person already seen by $i$ *and* located further right won't be seen by $i$ because that intermediate person blocks the view.
3.  **Choosing the Tool**: This "next greater" or "range visibility" pattern strongly suggests a **Monotonic Stack**.
4.  **Processing Order**: Processing from **right to left** allows us to maintain a stack of people to the right of the current person $i$ that could potentially be seen.

## Solution Approach

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

## Complexity Analysis

*   **Time Complexity**: $O(n)$. Each element is pushed and popped from the stack at most once.
*   **Space Complexity**: $O(n)$ for the stack and the result array.

## Related Problems

*   [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
*   [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
*   [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Template Reference

See [Monotonic Stack Templates](/posts/2025-10-29-leetcode-templates-data-structures/#monotonic-stack) for more patterns.
