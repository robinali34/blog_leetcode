---
layout: post
title: "[Medium] 739. Daily Temperatures"
date: 2026-01-29 00:00:00 -0700
categories: [leetcode, medium, array, stack, monotonic-stack]
permalink: /2026/01/29/medium-739-daily-temperatures/
tags: [leetcode, medium, array, stack, monotonic-stack]
---
Given an array of integers `temperatures` representing the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `i`-th *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Examples

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Explanation: 
- Day 0: temperature 73, wait 1 day for warmer (74)
- Day 1: temperature 74, wait 1 day for warmer (75)
- Day 2: temperature 75, wait 4 days for warmer (76)
- Day 3: temperature 71, wait 2 days for warmer (72)
- Day 4: temperature 69, wait 1 day for warmer (72)
- Day 5: temperature 72, wait 1 day for warmer (76)
- Day 6: temperature 76, no warmer day (0)
- Day 7: temperature 73, no warmer day (0)
```

**Example 2:**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Explanation: Each day has a warmer day the next day.
```

**Example 3:**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
Explanation: Day 0 waits 1 day, day 1 waits 1 day, day 2 has no warmer day.
```

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Thinking Process

1. **Monotonic Stack Pattern**: Classic pattern for "next greater element" problems - conceptually elegant
- Better cache locality: sequential array access vs random stack operations
- No stack overhead: avoids push/pop function calls
- Direct memory access: simpler access patterns for CPU

- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in O(n).

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

*Note: While this solution is conceptually elegant and easier to understand, Solution 2 is faster in practice due to better cache locality and avoiding stack overhead.*

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> rtn(n, 0);
        stack<int> s;

        for(int i = 0; i < n; i++) {
            while(!s.empty() && temperatures[i] > temperatures[s.top()]) {
                int prev = s.top();
                s.pop();
                rtn[prev] = i - prev;
            }
            s.push(i);
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Monotonic stack (this problem)

**Key idea:** 1. **Monotonic Stack Pattern**: Classic pattern for "next greater element" problems - conceptually elegant

**How the code works:**
1. **Monotonic Stack Pattern**: Classic pattern for "next greater element" problems - conceptually elegant
- Better cache locality: sequential array access vs random stack operations
- No stack overhead: avoids push/pop function calls
- Direct memory access: simpler access patterns for CPU
- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.

**Walkthrough** — input `temperatures = [73,74,75,71,69,72,76,73]`, expected output `[1,1,4,2,1,1,0,0]`:

- Day 0: temperature 73, wait 1 day for warmer (74)
- Day 1: temperature 74, wait 1 day for warmer (75)
- Day 2: temperature 75, wait 4 days for warmer (76)
- Day 3: temperature 71, wait 2 days for warmer (72)
- Day 4: temperature 69, wait 1 day for warmer (72)
- Day 5: temperature 72, wait 1 day for warmer (76)
- Day 6: temperature 76, no warmer day (0)
- Day 7: temperature 73, no warmer day (0)

### Solution 1: Monotonic Stack

- **Time Complexity:** O(n)
  - Each index is pushed onto the stack exactly once
  - Each index is popped from the stack at most once
  - Overall: O(n)

- **Space Complexity:** O(n)
  - Stack can contain at most n indices in worst case
  - Result array: O(n)
  - Total: O(n)

### Solution 2: Right-to-Left with DP Jumping

- **Time Complexity:** O(n)
  - Each index is visited once
  - Jumping forward skips already-processed days using DP information
  - Worst case: O(n) when temperatures are in decreasing order
  - **In practice, faster than Solution 1** due to better cache locality and no stack operations
  - Overall: O(n)

- **Space Complexity:** O(1) excluding output array
  - Only uses a few variables
  - Result array: O(n) required by problem
  - Total: O(1) extra space (vs O(n) for stack in Solution 1)
## Common Mistakes

1. **All increasing**: `[30,40,50,60]` → `[1,1,1,0]`
2. **All decreasing**: `[60,50,40,30]` → `[0,0,0,0]`
3. **Single element**: `[73]` → `[0]`
4. **Same temperatures**: `[30,30,30]` → `[0,0,0]`
5. **Mixed pattern**: `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`

1. **Wrong comparison**: Using `>=` instead of `>` (should be strictly greater)
2. **Index confusion**: Mixing up indices when calculating wait days
3. **Stack order**: Maintaining increasing instead of decreasing stack
4. **Not handling empty stack**: Forgetting to check if stack is empty before popping
5. **Jump logic error**: In Solution 2, not checking `rtn[j] == 0` before jumping

## Related Problems

- [LC 496: Next Greater Element I](https://www.leetcode.com/problems/next-greater-element-i/) - Similar next greater element problem
- [LC 503: Next Greater Element II](https://www.leetcode.com/problems/next-greater-element-ii/) - Circular array version
- [LC 84: Largest Rectangle in Histogram](https://www.leetcode.com/problems/largest-rectangle-in-histogram/) - Uses monotonic stack
- [LC 42: Trapping Rain Water](https://www.leetcode.com/problems/trapping-rain-water/) - Monotonic stack application
- [LC 901: Online Stock Span](https://www.leetcode.com/problems/online-stock-span/) - Similar pattern with stack

## Tags

`Array`, `Stack`, `Monotonic Stack`, `Medium`

## Key Takeaways

1. **Monotonic Stack Pattern**: Classic pattern for "next greater element" problems - conceptually elegant
2. **Decreasing Stack**: Stack maintains indices in decreasing temperature order
3. **Efficient Resolution**: When finding a warmer day, resolve all waiting colder days
4. **DP Jumping Approach**: Right-to-left processing with jumping reuses computed information - **faster in practice**
5. **Why DP Jumping is Faster**: 
   - Better cache locality: sequential array access vs random stack operations
   - No stack overhead: avoids push/pop function calls
   - Direct memory access: simpler access patterns for CPU
   - O(1) extra space: more memory-efficient
6. **Single Pass**: Both approaches achieve O(n) time with a single pass through the array

## References

- [LC 739: Daily Temperatures on LeetCode](https://www.leetcode.com/problems/daily-temperatures/)
- [LeetCode Discuss — LC 739: Daily Temperatures](https://www.leetcode.com/problems/daily-temperatures/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/daily-temperatures/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
