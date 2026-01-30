---
layout: post
title: "739. Daily Temperatures"
date: 2026-01-29 00:00:00 -0700
categories: [leetcode, medium, array, stack, monotonic-stack]
permalink: /2026/01/29/medium-739-daily-temperatures/
tags: [leetcode, medium, array, stack, monotonic-stack]
---

# 739. Daily Temperatures

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Warmer temperature**: What does "warmer" mean? (Assumption: Temperature strictly greater than current day's temperature)

2. **Wait days**: How are wait days counted? (Assumption: Number of days until next warmer temperature - if warmer on next day, answer is 1)

3. **No warmer day**: What if there's no warmer day in the future? (Assumption: Return 0 for that day - no warmer temperature exists)

4. **Return format**: What should we return? (Assumption: Array of integers - same length as input, each element is wait days)

5. **Array modification**: Can we modify the input array? (Assumption: Typically no - should return a new array)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For each day `i`, scan forward through the array starting from `i+1` to find the first day `j` where `temperatures[j] > temperatures[i]`. Set `answer[i] = j - i`. If no warmer day is found, set `answer[i] = 0`. This approach has O(n²) time complexity: O(n) days, each requiring O(n) to scan forward, which is too slow for arrays up to 10^5 elements.

**Step 2: Semi-Optimized Approach (7 minutes)**

Process from right to left, maintaining information about warmer days seen so far. For each day, check if the next day is warmer. If not, use the answer from the next day to jump forward (if `temperatures[j] <= temperatures[i]` and `answer[j] > 0`, jump to `j + answer[j]`). This approach actually achieves O(n) time complexity because each day is visited at most once, and jumping forward reuses computed information efficiently. This is the optimized solution that performs better than the monotonic stack approach.

**Step 3: Alternative Optimized Solution (8 minutes)**

Use a monotonic stack: maintain a stack of indices where temperatures are in decreasing order. For each day, while the stack is not empty and current temperature is greater than the temperature at the top of the stack, pop the stack and set `answer[popped_index] = current_index - popped_index`. Then push the current index onto the stack. This achieves O(n) time complexity because each index is pushed and popped at most once. While this solution is conceptually elegant and easier to understand, the DP jumping approach from Step 2 is faster in practice due to better cache locality and no stack overhead.

## Solution Approach

This problem requires finding the next greater element for each position in the array. We can solve this efficiently using a **monotonic stack** (specifically, a decreasing stack) or by processing from right to left with smart jumping using dynamic programming.

### Key Insights:

1. **Monotonic Stack**: Use a stack to maintain indices of temperatures in decreasing order
2. **Next Greater Element**: When we find a warmer temperature, resolve all colder days waiting for it
3. **Right-to-Left Processing with DP**: Process backwards, using previously computed answers to jump forward efficiently - **this approach is faster in practice** due to better cache locality and no stack overhead

## Solution 1: Monotonic Stack (Standard Approach)

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

### Algorithm Explanation:

1. **Initialize**: Create result array `rtn` filled with zeros, and an empty stack `s`
2. **Process each day**: For each index `i`:
   - **Resolve waiting days**: While stack is not empty and current temperature is greater than temperature at stack top:
     - Pop the index from stack
     - Set `rtn[popped_index] = i - popped_index` (wait days)
   - **Add current day**: Push current index `i` onto stack
3. **Result**: Return `rtn` array

### Example Walkthrough:

**Input:** `temperatures = [73,74,75,71,69,72,76,73]`

```
i=0: temp=73, stack=[], push 0 → stack=[0]
i=1: temp=74, stack=[0], 74 > 73 → pop 0, rtn[0]=1, push 1 → stack=[1]
i=2: temp=75, stack=[1], 75 > 74 → pop 1, rtn[1]=1, push 2 → stack=[2]
i=3: temp=71, stack=[2], 71 <= 75 → push 3 → stack=[2,3]
i=4: temp=69, stack=[2,3], 69 <= 71 → push 4 → stack=[2,3,4]
i=5: temp=72, stack=[2,3,4], 72 > 69 → pop 4, rtn[4]=1
                     72 > 71 → pop 3, rtn[3]=2, push 5 → stack=[2,5]
i=6: temp=76, stack=[2,5], 76 > 72 → pop 5, rtn[5]=1
                     76 > 75 → pop 2, rtn[2]=4, push 6 → stack=[6]
i=7: temp=73, stack=[6], 73 <= 76 → push 7 → stack=[6,7]

Result: [1,1,4,2,1,1,0,0]
```

## Solution 2: Right-to-Left with DP Jumping (Faster in Practice) ⚡

*This approach is faster than the monotonic stack solution due to:*
- *Better cache locality: sequential array access patterns*
- *No stack overhead: avoids push/pop operations*
- *O(1) extra space: only uses a few variables*
- *Simpler memory access: direct array indexing*

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        const int N = temperatures.size();
        vector<int> rtn(N, 0);
        for(int i = N - 2; i >= 0; i--) {
            int j = i + 1;
            while(j < N && temperatures[j] <= temperatures[i]) {
                if(rtn[j] == 0) j = N;
                else j += rtn[j];
            }
            if(j < N) rtn[i] = j - i;
        }
        return rtn;
    }
};
```

### Algorithm Explanation:

1. **Process backwards**: Start from the second-to-last day and move left
2. **Jump forward**: For each day `i`:
   - Start checking from `j = i + 1`
   - If `temperatures[j] <= temperatures[i]`:
     - If `rtn[j] == 0`: no warmer day exists, set `j = N` to stop
     - Otherwise: jump forward by `rtn[j]` (use information from day `j`)
   - If `j < N`: found warmer day, set `rtn[i] = j - i`
3. **Result**: Return `rtn` array

### Example Walkthrough:

**Input:** `temperatures = [73,74,75,71,69,72,76,73]`

```
i=6: temp=76, last day → rtn[6]=0
i=5: temp=72, j=6, 76 > 72 → rtn[5]=1
i=4: temp=69, j=5, 72 > 69 → rtn[4]=1
i=3: temp=71, j=4, 69 <= 71, rtn[4]=1 → j=5, 72 > 71 → rtn[3]=2
i=2: temp=75, j=3, 71 <= 75, rtn[3]=2 → j=5, 72 <= 75, rtn[5]=1 → j=6, 76 > 75 → rtn[2]=4
i=1: temp=74, j=2, 75 > 74 → rtn[1]=1
i=0: temp=73, j=1, 74 > 73 → rtn[0]=1

Result: [1,1,4,2,1,1,0,0]
```

## Complexity Analysis

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

## Key Insights

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

## Edge Cases

1. **All increasing**: `[30,40,50,60]` → `[1,1,1,0]`
2. **All decreasing**: `[60,50,40,30]` → `[0,0,0,0]`
3. **Single element**: `[73]` → `[0]`
4. **Same temperatures**: `[30,30,30]` → `[0,0,0]`
5. **Mixed pattern**: `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`

## Comparison of Approaches

| Approach | Time | Space | Performance | Best For |
|----------|------|-------|-------------|----------|
| **Monotonic Stack** | O(n) | O(n) | Slower (stack overhead) | Easier to understand, standard pattern |
| **Right-to-Left DP Jumping** | O(n) | O(1) extra | **Faster** (better cache locality) | Production code, performance-critical scenarios |

**Performance Analysis:**
- **Solution 1 (Monotonic Stack)**: Requires stack operations (push/pop) which have function call overhead and less cache-friendly memory access patterns
- **Solution 2 (DP Jumping)**: Uses direct array indexing with sequential access patterns, resulting in better CPU cache utilization and faster execution in practice

## Common Mistakes

1. **Wrong comparison**: Using `>=` instead of `>` (should be strictly greater)
2. **Index confusion**: Mixing up indices when calculating wait days
3. **Stack order**: Maintaining increasing instead of decreasing stack
4. **Not handling empty stack**: Forgetting to check if stack is empty before popping
5. **Jump logic error**: In Solution 2, not checking `rtn[j] == 0` before jumping

## Related Problems

- [LC 496: Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) - Similar next greater element problem
- [LC 503: Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) - Circular array version
- [LC 84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) - Uses monotonic stack
- [LC 42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) - Monotonic stack application
- [LC 901: Online Stock Span](https://leetcode.com/problems/online-stock-span/) - Similar pattern with stack

## Tags

`Array`, `Stack`, `Monotonic Stack`, `Medium`

---

*This problem demonstrates two efficient approaches for finding the next greater element: the **monotonic stack** pattern (conceptually elegant) and **DP jumping** (faster in practice). While both achieve O(n) time complexity, the DP jumping approach is faster due to better cache locality and avoiding stack overhead. The key insight in Solution 2 is reusing previously computed answers to jump forward efficiently, eliminating redundant comparisons.*
