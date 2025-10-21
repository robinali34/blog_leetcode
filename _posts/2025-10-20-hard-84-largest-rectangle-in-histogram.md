---
layout: post
title: "84. Largest Rectangle in Histogram"
date: 2025-10-20 13:40:00 -0700
categories: leetcode algorithm hard stack monotonic-stack
permalink: /2025/10/20/hard-84-largest-rectangle-in-histogram/
---

# 84. Largest Rectangle in Histogram

**Difficulty:** Hard  
**Category:** Stack, Monotonic Stack

## Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

## Examples

### Example 1:
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

### Example 2:
```
Input: heights = [2,4]
Output: 4
```

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Approach

This is a classic **Monotonic Stack** problem. The key insight is that for each bar, we need to find the largest rectangle that can be formed with that bar as the height.

### Algorithm:
1. **Use a stack** to store indices of bars in increasing order of height
2. **For each bar**, pop all bars from stack that are taller than current bar
3. **Calculate area** for each popped bar using its height and the width it can extend
4. **Add a sentinel** (height 0) at the end to ensure all bars are processed
5. **Track maximum area** found so far

### Key Insight:
- For each bar at index `i`, the largest rectangle with height `heights[i]` extends from the previous smaller bar to the next smaller bar
- The width = `right_boundary - left_boundary - 1`

## Solution

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int max_area = 0;
        heights.push_back(0); 
        int n = heights.size();
        stack<int> stk;
        for(int i = 0; i < n; i++) {
            while(!stk.empty() && heights[i] < heights[stk.top()]) {
                int height = heights[stk.top()];
                stk.pop();
                int width = stk.empty()? i: i - stk.top() - 1;
                max_area = max(max_area, height * width);
            }
            stk.push(i);
        }
        return max_area;
    }
};
```

## Explanation

### Step-by-Step Process:

1. **Add Sentinel:** Append `0` to heights to ensure all bars are processed
2. **Initialize:** Empty stack and max_area = 0
3. **For each bar:**
   - **Pop taller bars:** While stack is not empty and current bar is shorter than stack top
   - **Calculate area:** For each popped bar, calculate area = height × width
   - **Update max:** Keep track of maximum area found
   - **Push current:** Add current index to stack

### Width Calculation:
- **If stack is empty:** Width extends from start to current position = `i`
- **If stack not empty:** Width extends from previous smaller bar to current = `i - stk.top() - 1`

### Example Walkthrough:
For `heights = [2,1,5,6,2,3]` with sentinel `[2,1,5,6,2,3,0]`:

- **i=0, height=2:** Stack=[0]
- **i=1, height=1:** Pop 0, area=2×1=2, Stack=[1]
- **i=2, height=5:** Stack=[1,2]
- **i=3, height=6:** Stack=[1,2,3]
- **i=4, height=2:** Pop 3, area=6×1=6; Pop 2, area=5×2=10; Stack=[1,4]
- **i=5, height=3:** Stack=[1,4,5]
- **i=6, height=0:** Pop all, calculate remaining areas

**Maximum area = 10**

## Complexity Analysis

**Time Complexity:** O(n) where n is the length of heights array
- Each element is pushed and popped from stack exactly once
- Each element is processed once

**Space Complexity:** O(n) for the stack
- In worst case, all elements could be in increasing order

## Key Insights

1. **Monotonic Stack:** Maintains bars in increasing height order
2. **Sentinel Value:** Adding 0 at end ensures all bars are processed
3. **Area Calculation:** Width = distance between smaller bars on left and right
4. **Index Tracking:** Store indices in stack, not values, to calculate width
5. **Greedy Approach:** Process each bar as soon as we find a smaller bar

## Alternative Approaches

### Brute Force (O(n²)):
```cpp
int largestRectangleArea(vector<int>& heights) {
    int max_area = 0;
    for(int i = 0; i < heights.size(); i++) {
        int min_height = heights[i];
        for(int j = i; j < heights.size(); j++) {
            min_height = min(min_height, heights[j]);
            max_area = max(max_area, min_height * (j - i + 1));
        }
    }
    return max_area;
}
```

### Divide and Conquer (O(n log n)):
```cpp
int largestRectangleArea(vector<int>& heights) {
    return divideConquer(heights, 0, heights.size() - 1);
}

int divideConquer(vector<int>& heights, int left, int right) {
    if(left > right) return 0;
    if(left == right) return heights[left];
    
    int min_idx = left;
    for(int i = left; i <= right; i++) {
        if(heights[i] < heights[min_idx]) min_idx = i;
    }
    
    int area = heights[min_idx] * (right - left + 1);
    int left_area = divideConquer(heights, left, min_idx - 1);
    int right_area = divideConquer(heights, min_idx + 1, right);
    
    return max({area, left_area, right_area});
}
```

The monotonic stack approach is the most efficient solution for this problem, demonstrating the power of this data structure for solving range-based problems.
