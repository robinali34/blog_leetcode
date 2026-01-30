---
layout: post
title: "[Medium] 1762. Buildings With an Ocean View"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp array stack monotonic-stack problem-solving
permalink: /posts/2025-11-24-medium-1762-buildings-with-an-ocean-view/
tags: [leetcode, medium, array, stack, monotonic-stack, greedy, two-pointers]
---

# [Medium] 1762. Buildings With an Ocean View

There are `n` buildings in a line. You are given an integer array `heights` of size `n` that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an **ocean view** if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

## Examples

**Example 1:**
```
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building at index 1 (height 2) does not have an ocean view because building at index 2 (height 3) is taller.
```

**Example 2:**
```
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
```

**Example 3:**
```
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building at index 3 (height 4) has an ocean view.
```

**Example 4:**
```
Input: heights = [2,2,2,2]
Output: [3]
Explanation: Only the rightmost building has an ocean view (buildings of equal height block the view).
```

## Constraints

- `1 <= heights.length <= 10^5`
- `1 <= heights[i] <= 10^9`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Ocean view definition**: What gives a building an ocean view? (Assumption: Building has ocean view if no taller building to its right blocks the view)

2. **Building positions**: How are buildings positioned? (Assumption: Buildings are in a row, ocean is to the right - heights[i] is height of building at index i)

3. **Return format**: What should we return? (Assumption: Array of indices of buildings with ocean view, sorted in ascending order)

4. **Height comparison**: How do we check for blocking? (Assumption: Building at index i has ocean view if all buildings at indices > i have height <= heights[i])

5. **Rightmost building**: Does the rightmost building always have ocean view? (Assumption: Yes - no buildings to its right to block it)

## Solution Approaches

The key insight is that a building has an ocean view if it's taller than all buildings to its right. We can solve this by:

1. **Iterating from right to left**: Start from the rightmost building and track the maximum height seen so far
2. **Track maximum height**: If current building is taller than or equal to the maximum height seen, it has an ocean view
3. **Reverse result**: Since we iterate right-to-left, reverse the result to get indices in increasing order

### Solution 1: Simple Greedy (Recommended)

**Time Complexity:** O(n)  
**Space Complexity:** O(1) excluding output array

The simplest and most efficient approach: iterate from right to left, tracking the maximum height seen so far.

```cpp
class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        int n = heights.size();
        vector<int> rtn;
        int maxHeight = -1;
        
        for (int curr = n - 1; curr >= 0; curr--) {
            if (maxHeight < heights[curr]) {
                rtn.push_back(curr);
                maxHeight = heights[curr];
            }
        }
        
        reverse(rtn.begin(), rtn.end());
        return rtn;
    }
};
```

**How it works:**
1. Start from the rightmost building (index `n-1`)
2. Track `maxHeight` - the maximum height seen so far
3. If current building is taller than `maxHeight`, it has an ocean view
4. Update `maxHeight` to the current building's height
5. Reverse the result to get indices in increasing order

**Why this works:**
- A building has an ocean view if it's taller than all buildings to its right
- By iterating right-to-left, we can check this condition efficiently
- We only need to track the maximum height, not all buildings

### Solution 2: Monotonic Stack

**Time Complexity:** O(n)  
**Space Complexity:** O(n) for the stack

Uses a monotonic stack to maintain buildings in decreasing order of height.

```cpp
class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        int n = heights.size();
        vector<int> rtn;
        stack<int> stk;
        
        for (int curr = n - 1; curr >= 0; curr--) {
            // Remove buildings that are shorter than current
            while (!stk.empty() && heights[stk.top()] < heights[curr]) {
                stk.pop();
            }
            
            // If stack is empty, current building has ocean view
            if (stk.empty()) {
                rtn.push_back(curr);
            }
            
            stk.push(curr);
        }
        
        reverse(rtn.begin(), rtn.end());
        return rtn;
    }
};
```

**How it works:**
1. Iterate from right to left
2. Use a stack to maintain indices of buildings that could block the view
3. Pop buildings from stack that are shorter than current building
4. If stack is empty after popping, current building has ocean view
5. Push current building index to stack

**Why this works:**
- Stack maintains buildings in decreasing order of height
- If a building is shorter than current, it can't block current's view
- If stack is empty, no building to the right can block current's view

## How the Algorithm Works

### Key Insight: Right-to-Left Iteration

**Problem:** For each building, check if all buildings to its right are shorter.

**Solution:** Iterate from right to left, tracking the maximum height seen so far.

**Why right-to-left:**
- We need to know the maximum height of all buildings to the right
- By iterating right-to-left, we can maintain this information efficiently
- Each building only needs to compare with the maximum height seen so far

### Step-by-Step Example: `heights = [4,2,3,1]`

```
Initial: maxHeight = -1, rtn = []

i = 3: heights[3] = 1
  maxHeight = -1 < 1 → has ocean view
  rtn = [3], maxHeight = 1

i = 2: heights[2] = 3
  maxHeight = 1 < 3 → has ocean view
  rtn = [3, 2], maxHeight = 3

i = 1: heights[1] = 2
  maxHeight = 3 >= 2 → no ocean view
  rtn = [3, 2], maxHeight = 3

i = 0: heights[0] = 4
  maxHeight = 3 < 4 → has ocean view
  rtn = [3, 2, 0], maxHeight = 4

After reverse: rtn = [0, 2, 3]
```

**Visual Representation:**
```
Buildings: [4, 2, 3, 1]
Indices:    0  1  2  3
            │  │  │  │
            │  │  └──┴──> Ocean
            │  │     │
            │  └─────┼──> Blocked by building 2
            └────────┼──> Ocean view (tallest)
                     │
            Ocean view: [0, 2, 3]
```

### Step-by-Step Example: `heights = [1,3,2,4]`

```
Initial: maxHeight = -1, rtn = []

i = 3: heights[3] = 4
  maxHeight = -1 < 4 → has ocean view
  rtn = [3], maxHeight = 4

i = 2: heights[2] = 2
  maxHeight = 4 >= 2 → no ocean view
  rtn = [3], maxHeight = 4

i = 1: heights[1] = 3
  maxHeight = 4 >= 3 → no ocean view
  rtn = [3], maxHeight = 4

i = 0: heights[0] = 1
  maxHeight = 4 >= 1 → no ocean view
  rtn = [3], maxHeight = 4

After reverse: rtn = [3]
```

## Algorithm Breakdown

### Solution 1: Simple Greedy

```cpp
vector<int> findBuildings(vector<int>& heights) {
    int n = heights.size();
    vector<int> rtn;
    int maxHeight = -1;
    
    for (int curr = n - 1; curr >= 0; curr--) {
        if (maxHeight < heights[curr]) {
            rtn.push_back(curr);
            maxHeight = heights[curr];
        }
    }
    
    reverse(rtn.begin(), rtn.end());
    return rtn;
}
```

**Key Points:**
- **Right-to-left iteration**: Start from the rightmost building
- **Track maximum**: Maintain maximum height seen so far
- **Compare and update**: If current is taller, add to result and update max
- **Reverse result**: Get indices in increasing order

### Solution 2: Monotonic Stack

```cpp
vector<int> findBuildings(vector<int>& heights) {
    int n = heights.size();
    vector<int> rtn;
    stack<int> stk;
    
    for (int curr = n - 1; curr >= 0; curr--) {
        while (!stk.empty() && heights[stk.top()] < heights[curr]) {
            stk.pop();
        }
        
        if (stk.empty()) {
            rtn.push_back(curr);
        }
        
        stk.push(curr);
    }
    
    reverse(rtn.begin(), rtn.end());
    return rtn;
}
```

**Key Points:**
- **Monotonic stack**: Maintains buildings in decreasing order
- **Pop shorter buildings**: Remove buildings that can't block current
- **Check if empty**: Empty stack means no blocking buildings
- **Push current**: Add current building to stack

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Simple Greedy** | O(n) | O(1) | Simple, efficient, no extra space | - |
| **Monotonic Stack** | O(n) | O(n) | More general pattern | Extra space, more complex |

## Edge Cases

1. **All buildings same height**: Only rightmost building has ocean view
   - `heights = [2,2,2,2]` → `[3]`

2. **Increasing heights**: All buildings have ocean view
   - `heights = [1,2,3,4]` → `[0,1,2,3]`

3. **Decreasing heights**: Only leftmost building has ocean view
   - `heights = [4,3,2,1]` → `[0,1,2,3]` (all have view since all to right are shorter)

4. **Single building**: Always has ocean view
   - `heights = [5]` → `[0]`

## Key Insights

1. **Right-to-left iteration**: Essential for efficiently checking if buildings to the right are shorter

2. **Track maximum only**: We only need the maximum height, not all heights

3. **Greedy approach**: Local optimal (taller than max) leads to global optimal

4. **Equal heights**: Buildings of equal height block each other (use `<` not `<=`)

## Common Mistakes

1. **Left-to-right iteration**: Can't efficiently check if buildings to right are shorter
2. **Wrong comparison**: Using `<=` instead of `<` for equal heights
3. **Forgetting to reverse**: Result indices should be in increasing order
4. **Not handling edge cases**: Single building, all same height, etc.

## Optimization Tips

1. **Use Solution 1**: Simpler and more space-efficient
2. **Reserve space**: Can reserve space for result vector if needed
3. **Early termination**: Not applicable here (need to check all buildings)

## Related Problems

- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) - Similar monotonic stack pattern
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) - Monotonic stack
- [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) - Monotonic stack with circular array
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) - Monotonic stack, water trapping
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) - Monotonic stack

## Pattern Recognition

This problem demonstrates the **"Monotonic Stack"** and **"Greedy"** patterns:

```
1. Iterate from right to left
2. Track maximum (or use stack) to maintain order
3. Compare current with tracked value
4. Update result based on comparison
```

Similar problems:
- Next greater/smaller element
- Trapping rain water
- Largest rectangle in histogram
- Problems requiring "next" or "previous" element information

## Real-World Applications

1. **City Planning**: Determining which buildings have unobstructed views
2. **Real Estate**: Identifying properties with ocean/mountain views
3. **Signal Processing**: Finding peaks in signal data
4. **Algorithm Design**: Understanding monotonic stack patterns

## Why Solution 1 is Better

**Advantages of Simple Greedy:**
- **O(1) extra space**: Only uses a single variable
- **Simpler code**: Easier to understand and maintain
- **Same time complexity**: O(n) in both cases
- **More efficient**: No stack operations overhead

**When to use Monotonic Stack:**
- Need to track multiple values, not just maximum
- Need to answer queries about "next greater/smaller"
- Problem requires maintaining order of elements

For this problem, Solution 1 (Simple Greedy) is the optimal choice.

---

*This problem demonstrates the importance of choosing the right direction for iteration and the power of simple greedy approaches over more complex data structures when the problem allows it.*

