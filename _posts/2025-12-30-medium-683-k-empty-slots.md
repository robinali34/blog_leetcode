---
layout: post
title: "683. K Empty Slots"
date: 2025-12-30 15:30:00 -0700
categories: [leetcode, medium, sliding-window, two-pointers, array]
permalink: /2025/12/30/medium-683-k-empty-slots/
---

# 683. K Empty Slots

## Problem Statement

You have `n` bulbs in a row numbered from `1` to `n`. Initially, all the bulbs are turned off. On day `i` (for `i` from `0` to `n-1`), we turn on exactly one bulb. The position of this bulb is given by `bulbs[i]`.

Given an integer `k`, return the **minimum day number** such that there exist two turned-on bulbs that have **exactly `k` bulbs between them** that are all turned off. If there isn't such day, return `-1`.

## Examples

**Example 1:**
```
Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
On day 1: bulbs[0] = 1, first bulb is turned on: [1, 0, 0]
On day 2: bulbs[1] = 3, third bulb is turned on: [1, 0, 1]
On day 3: bulbs[2] = 2, second bulb is turned on: [1, 1, 1]
We return 2 because on day 2, there were two on bulbs with one off bulb between them.
```

**Example 2:**
```
Input: bulbs = [1,2,3], k = 1
Output: -1
Explanation: No such day exists where two bulbs are on with exactly one bulb off between them.
```

## Constraints

- `n == bulbs.length`
- `1 <= n <= 2 * 10^4`
- `1 <= bulbs[i] <= n`
- All values in `bulbs` are **unique**.
- `0 <= k <= n`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Bulb activation**: How are bulbs activated? (Assumption: bulbs[i] represents the day when bulb at position i+1 is turned on - day 1 activates bulb at position bulbs[0])

2. **K-empty slots definition**: What does "k empty slots" mean? (Assumption: Two bulbs are on with exactly k bulbs off between them - k consecutive off bulbs)

3. **Optimization goal**: What are we optimizing for? (Assumption: Find the earliest day when k-empty slots condition is satisfied)

4. **Return value**: What should we return? (Assumption: Integer - earliest day number, or -1 if condition never satisfied)

5. **Position indexing**: How are positions indexed? (Assumption: Positions are 1-indexed - n bulbs at positions 1 to n)

## Solution Approach

This problem requires finding the earliest day when there exist two blooming bulbs with exactly `k` empty slots between them. We can solve this efficiently using a **sliding window approach** with position-to-day mapping.

### Key Insights:

1. **Position-to-Day Mapping**: Convert `bulbs[i] = position` to `days[position] = day` to know when each position blooms
2. **Sliding Window**: Use a window of size `k + 2` (two blooming bulbs + k empty slots)
3. **Validation**: Check if all bulbs between the two endpoints bloom later than both endpoints
4. **Early Termination**: If a bulb between endpoints blooms earlier, it invalidates the window

### Algorithm:

1. **Build days array**: `days[i]` = day when position `i+1` blooms
2. **Sliding window**: Check windows of size `k + 2`
3. **Validation**: Ensure all middle bulbs bloom after both endpoints
4. **Track minimum**: Keep track of minimum day when valid window found

## Solution

### **Solution: Sliding Window with Position Mapping**

```cpp
class Solution {
public:
    int kEmptySlots(vector<int>& bulbs, int k) {
        const int n = bulbs.size();
        vector<int> days(n, 0);
        for(int day = 0; day < n; day++) {
            days[bulbs[day] - 1] = day + 1;
        }
        int rtn = INT_MAX;
        int left = 0, right = k + 1;
        while(right < days.size()) {
            bool valid = true;
            for(int i = left + 1; i < right; i++) {
                if(days[i] < days[left] || days[i] < days[right]) {
                    left = i;
                    right = i + k + 1;
                    valid = false;
                    break;
                }
            }
            if(valid) {
                rtn = min(rtn, max(days[left], days[right]));
                left = right;
                right = left + k + 1;
            }
        }
        return rtn != INT_MAX ? rtn : -1;
    }
};
```

### **Algorithm Explanation:**

1. **Build Days Array (Lines 5-8)**:
   - Convert position-based input to day-based array
   - `days[i]` = day when bulb at position `i+1` blooms
   - Example: `bulbs = [1,3,2]` → `days = [1,3,2]` (position 1 blooms on day 1, position 2 on day 3, position 3 on day 2)

2. **Sliding Window (Lines 9-25)**:
   - Window size: `k + 2` (left endpoint, k empty slots, right endpoint)
   - `left = 0`, `right = k + 1`
   - Check if all bulbs between `left` and `right` bloom **after** both endpoints

3. **Validation (Lines 12-19)**:
   - For each position `i` between `left` and `right`:
     - If `days[i] < days[left]` or `days[i] < days[right]`: invalid window
     - Bulb `i` blooms before one of the endpoints → cannot have k empty slots
     - Move `left` to `i` and update `right` accordingly

4. **Update Result (Lines 20-23)**:
   - If window is valid: both endpoints are on, k bulbs between are off
   - Day when both are on: `max(days[left], days[right])`
   - Track minimum day across all valid windows

### **Example Walkthrough:**

**For `bulbs = [1,3,2], k = 1`:**

```
Step 1: Build days array
bulbs = [1, 3, 2]  (position 1 on day 1, position 3 on day 2, position 2 on day 3)
days  = [1, 3, 2]  (days[0]=1, days[1]=3, days[2]=2)

Step 2: Initialize sliding window
left = 0, right = k + 1 = 2
Window: positions [0, 2] with 1 empty slot at position 1

Step 3: Validate window [0, 2]
Check position 1 (between 0 and 2):
- days[1] = 3
- days[0] = 1, days[2] = 2
- days[1] > days[0] ✓ and days[1] > days[2] ✓
- Valid window!

Step 4: Calculate result
Both endpoints bloom on: max(days[0], days[2]) = max(1, 2) = 2
rtn = min(INT_MAX, 2) = 2

Step 5: Move to next window
left = 2, right = 2 + 1 + 1 = 4 (out of bounds)
Stop.

Result: 2
```

**Visual Representation:**

```
Day 1: [1, 0, 0]  Position 1 blooms
Day 2: [1, 0, 1]  Position 3 blooms → Valid! Positions 1 and 3 are on, position 2 is off
Day 3: [1, 1, 1]  Position 2 blooms (too late, already found answer)
```

### **Another Example: `bulbs = [1,2,3], k = 1`**

```
Step 1: Build days array
bulbs = [1, 2, 3]
days  = [1, 2, 3]

Step 2: Check window [0, 2]
Check position 1:
- days[1] = 2
- days[0] = 1, days[2] = 3
- days[1] = 2 > days[0] = 1 ✓
- days[1] = 2 < days[2] = 3 ✗ (position 1 blooms before position 3)
- Invalid window!

Step 3: Move left to position 1
left = 1, right = 1 + 1 + 1 = 3 (out of bounds)
No valid window found.

Result: -1
```

## Algorithm Breakdown

### **Key Insight: Window Validation**

The algorithm checks if a window `[left, right]` is valid by ensuring:
- Both endpoints (`left` and `right`) are blooming bulbs
- All bulbs between them (`left+1` to `right-1`) are **off** (bloom later)

**Validation Condition:**
```cpp
for(int i = left + 1; i < right; i++) {
    if(days[i] < days[left] || days[i] < days[right]) {
        // Invalid: bulb i blooms before one of the endpoints
    }
}
```

**Why this works:**
- If `days[i] < days[left]`: bulb `i` blooms before left endpoint → cannot have k empty slots
- If `days[i] < days[right]`: bulb `i` blooms before right endpoint → cannot have k empty slots
- Only if all `days[i] > max(days[left], days[right])`: all middle bulbs bloom after both endpoints → valid window

### **Optimization: Early Termination**

When an invalid bulb is found, we don't need to check positions before it:
```cpp
if(days[i] < days[left] || days[i] < days[right]) {
    left = i;  // Move left to invalid position
    right = i + k + 1;  // Update right accordingly
    break;  // Stop checking this window
}
```

This optimization ensures we don't check redundant windows.

## Complexity Analysis

### **Time Complexity:** O(n)
- **Build days array**: O(n) - single pass through bulbs
- **Sliding window**: O(n) - each position visited at most once
  - When invalid bulb found, we skip to that position
  - Each position is checked at most once
- **Total**: O(n)

### **Space Complexity:** O(n)
- **Days array**: O(n) - stores day for each position
- **Total**: O(n)

## Key Points

1. **Position-to-Day Mapping**: Convert problem from "which position blooms on day i" to "which day does position i bloom"
2. **Window Size**: Use window of size `k + 2` (two endpoints + k empty slots)
3. **Validation Logic**: All middle bulbs must bloom after both endpoints
4. **Early Termination**: Skip invalid windows efficiently
5. **Result Calculation**: Day when both endpoints are on = `max(days[left], days[right])`

## Alternative Approaches

### **Approach 1: Sliding Window (Current Solution)**
- **Time**: O(n)
- **Space**: O(n)
- **Best for**: Efficient single-pass solution

### **Approach 2: Brute Force**
- **Time**: O(n²)
- **Space**: O(n)
- **Check all pairs**: For each pair of positions with k slots between, check if valid

### **Approach 3: TreeSet/Ordered Set**
- **Time**: O(n log n)
- **Space**: O(n)
- **Maintain active bulbs**: Use ordered set to track blooming bulbs and check gaps

## Detailed Example Walkthrough

### **Example: `bulbs = [6,5,8,9,7,1,10,2,3,4], k = 2`**

```
Step 1: Build days array
bulbs = [6, 5, 8, 9, 7, 1, 10, 2, 3, 4]
days  = [6, 8, 9, 10, 2, 3, 4, 5, 7, 1]
        (position 1 blooms on day 6, position 2 on day 8, etc.)

Step 2: Check window [0, 3] (positions 1 and 4, k=2 means positions 2,3 between)
Check positions 1, 2 (between 0 and 3):
- days[1] = 8, days[2] = 9
- days[0] = 6, days[3] = 10
- days[1] = 8 > days[0] = 6 ✓ and days[1] = 8 < days[3] = 10 ✗
- Invalid! Position 2 blooms before position 4

Step 3: Move to window [1, 4]
Check positions 2, 3 (between 1 and 4):
- days[2] = 9, days[3] = 10
- days[1] = 8, days[4] = 2
- days[2] = 9 > days[1] = 8 ✓ but days[2] = 9 > days[4] = 2 ✗
- Invalid! Position 3 blooms before position 5

Step 4: Move to window [4, 7]
Check positions 5, 6 (between 4 and 7):
- days[5] = 3, days[6] = 4
- days[4] = 2, days[7] = 5
- days[5] = 3 > days[4] = 2 ✓ but days[5] = 3 < days[7] = 5 ✗
- Invalid! Position 6 blooms before position 8

Step 5: Move to window [5, 8]
Check positions 6, 7 (between 5 and 8):
- days[6] = 4, days[7] = 5
- days[5] = 3, days[8] = 7
- days[6] = 4 > days[5] = 3 ✓ and days[6] = 4 < days[8] = 7 ✗
- Invalid! Position 7 blooms before position 9

Step 6: Move to window [6, 9]
Check positions 7, 8 (between 6 and 9):
- days[7] = 5, days[8] = 7
- days[6] = 4, days[9] = 1
- days[7] = 5 > days[6] = 4 ✓ but days[7] = 5 > days[9] = 1 ✗
- Invalid! Position 8 blooms before position 10

No valid window found → Return -1
```

## Edge Cases

1. **k = 0**: Two adjacent bulbs must both be on
2. **k = n-2**: First and last bulbs with all middle bulbs off
3. **No solution**: All bulbs bloom in order, no valid window
4. **Single valid window**: Only one pair of positions satisfies condition

## Related Problems

- [683. K Empty Slots](https://leetcode.com/problems/k-empty-slots/) - Current problem
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Sliding window technique
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Variable sliding window
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Sliding window

## Tags

`Sliding Window`, `Two Pointers`, `Array`, `Medium`

