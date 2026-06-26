---
layout: post
title: "[Hard] 84. Largest Rectangle in Histogram"
date: 2025-10-20 13:40:00 -0700
categories: leetcode algorithm hard stack monotonic-stack
permalink: /2025/10/20/hard-84-largest-rectangle-in-histogram/
---
**Difficulty:** Hard  
**Category:** Stack, Monotonic Stack


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

## Thinking Process

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

### Solution Explanation

This is a classic **Monotonic Stack** problem. The key insight is that for each bar, we need to find the largest rectangle that can be formed with that bar as the height.

See **Complexity** below for time and space analysis.
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

### Complexity
**Time Complexity:** O(n) where n is the length of heights array
- Each element is pushed and popped from stack exactly once
- Each element is processed once

**Space Complexity:** O(n) for the stack
- In worst case, all elements could be in increasing order

## References

- [LC 84: Largest Rectangle in Histogram on LeetCode](https://www.leetcode.com/problems/largest-rectangle-in-histogram/)
- [LeetCode Discuss — LC 84: Largest Rectangle in Histogram](https://www.leetcode.com/problems/largest-rectangle-in-histogram/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/largest-rectangle-in-histogram/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Monotonic Stack:** Maintains bars in increasing height order
2. **Sentinel Value:** Adding 0 at end ensures all bars are processed
3. **Area Calculation:** Width = distance between smaller bars on left and right
4. **Index Tracking:** Store indices in stack, not values, to calculate width
5. **Greedy Approach:** Process each bar as soon as we find a smaller bar
