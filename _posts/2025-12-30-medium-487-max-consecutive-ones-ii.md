---
layout: post
title: "487. Max Consecutive Ones II"
date: 2025-12-30 19:30:00 -0700
categories: [leetcode, medium, array, dynamic-programming, sliding-window]
permalink: /2025/12/30/medium-487-max-consecutive-ones-ii/
---

# 487. Max Consecutive Ones II

## Problem Statement

Given a binary array `nums`, return *the maximum number of consecutive `1`'s in the array if you can flip at most one `0`*.

## Examples

**Example 1:**
```
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The maximum number of consecutive ones is 4.
```

**Example 2:**
```
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
Flipping the zero at index 4 gives us [1,0,1,1,1,1] with 4 consecutive ones.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Flip operation**: What does "flip at most one 0" mean? (Assumption: Can change at most one 0 to 1 - can flip zero or one zero)

2. **Consecutive definition**: What does "consecutive ones" mean? (Assumption: Ones that appear next to each other without any zeros in between)

3. **Optimization goal**: What are we optimizing for? (Assumption: Maximum length of consecutive ones after flipping at most one 0)

4. **Array modification**: Can we modify the array? (Assumption: No - just find the maximum length, don't actually modify)

5. **All ones**: What if array contains only ones? (Assumption: Return array length - all ones are consecutive, no flip needed)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to find maximum consecutive ones. Let me try flipping each 0."

**Naive Solution**: For each 0, flip it to 1, find maximum consecutive ones, track maximum across all flips.

**Complexity**: O(n²) time, O(1) space

**Issues**:
- O(n²) time - inefficient
- Repeats consecutive ones counting
- Doesn't leverage sliding window
- Can be optimized

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use sliding window that allows at most one 0."

**Improved Solution**: Use sliding window with two pointers. Expand right pointer, when encountering second 0, shrink left pointer until window contains at most one 0.

**Complexity**: O(n) time, O(1) space

**Improvements**:
- Sliding window avoids redundant counting
- O(n) time is much better
- Handles at most one flip correctly
- Clean and efficient

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "Sliding window approach is optimal. Track last zero position."

**Best Solution**: Sliding window approach is optimal. Track last zero position. When encountering second zero, move left pointer to after last zero. Window always contains at most one zero.

**Complexity**: O(n) time, O(1) space

**Key Realizations**:
1. Sliding window is perfect for consecutive problems
2. O(n) time is optimal - single pass
3. Track last zero position for efficient shrinking
4. O(1) space is optimal

## Solution Approach

This problem requires finding the longest sequence of consecutive 1s when we can flip at most one 0 to 1. We can solve this using **dynamic programming** with two states: one without flipping and one with at most one flip.

### Key Insights:

1. **Two States**: Track two values for each position:
   - `dp0`: Max consecutive ones ending here **without** flipping
   - `dp1`: Max consecutive ones ending here **with at most one flip**

2. **State Transitions**:
   - If current is `1`: Both states increment
   - If current is `0`: `dp1` uses previous `dp0` + 1 (flip this 0), `dp0` resets to 0

3. **Result**: Track maximum of `dp0` and `dp1` at each position

### Algorithm:

1. **Initialize**: `dp0 = 0`, `dp1 = 0` (no consecutive ones initially)
2. **Iterate**: For each element, update both states
3. **Update result**: Track maximum across all positions
4. **Return**: Maximum consecutive ones found

## Solution

### **Solution: Dynamic Programming with Two States**

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        const int n = nums.size();
        int rtn = 0, dp0 = 0, dp1 = 0;
        for(int i = 0; i < n; i++) {
            if(nums[i]) {
                dp1++;
                dp0++;
            } else {
                dp1 = dp0 + 1;
                dp0 = 0;
            }
            rtn = max(rtn, max(dp0, dp1));
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Initialization (Line 4)**:
   - `rtn`: Maximum consecutive ones found so far
   - `dp0`: Max consecutive ones ending at current position **without flipping**
   - `dp1`: Max consecutive ones ending at current position **with at most one flip**

2. **Process Each Element (Lines 5-13)**:
   - **If `nums[i] == 1` (Lines 6-8)**:
     - `dp1++`: Extend sequence with flip (or continue without needing flip)
     - `dp0++`: Extend sequence without flip
   - **If `nums[i] == 0` (Lines 9-11)**:
     - `dp1 = dp0 + 1`: Use previous sequence without flip, flip this 0
     - `dp0 = 0`: Reset sequence without flip

3. **Update Result (Line 12)**:
   - Track maximum of `dp0` and `dp1` at each position

### **Example Walkthrough:**

**For `nums = [1,0,1,1,0]`:**

```
Step 1: i=0, nums[0]=1
  dp0 = 0 + 1 = 1  (extend without flip)
  dp1 = 0 + 1 = 1  (extend, no flip needed)
  rtn = max(0, max(1, 1)) = 1

Step 2: i=1, nums[1]=0
  dp1 = dp0 + 1 = 1 + 1 = 2  (flip this 0, use previous sequence)
  dp0 = 0  (reset, can't extend without flip)
  rtn = max(1, max(0, 2)) = 2

Step 3: i=2, nums[2]=1
  dp1 = 2 + 1 = 3  (extend sequence with flip)
  dp0 = 0 + 1 = 1  (start new sequence without flip)
  rtn = max(2, max(1, 3)) = 3

Step 4: i=3, nums[3]=1
  dp1 = 3 + 1 = 4  (extend sequence with flip)
  dp0 = 1 + 1 = 2  (extend sequence without flip)
  rtn = max(3, max(2, 4)) = 4

Step 5: i=4, nums[4]=0
  dp1 = dp0 + 1 = 2 + 1 = 3  (flip this 0, use sequence from dp0)
  dp0 = 0  (reset)
  rtn = max(4, max(0, 3)) = 4

Result: 4
```

**Visual Representation:**

```
nums:  [1, 0, 1, 1, 0]
        ↑  ↑  ↑  ↑  ↑
        i=0 i=1 i=2 i=3 i=4

dp0:   [1, 0, 1, 2, 0]  (without flip)
dp1:   [1, 2, 3, 4, 3]  (with at most one flip)
rtn:   [1, 2, 3, 4, 4]  (maximum so far)
```

## Algorithm Breakdown

### **Key Insight: Two-State DP**

The solution uses two states to track different scenarios:

**State 0 (`dp0`)**: Maximum consecutive ones ending at current position **without flipping any 0**
- If current is `1`: Extend sequence → `dp0++`
- If current is `0`: Reset sequence → `dp0 = 0`

**State 1 (`dp1`)**: Maximum consecutive ones ending at current position **with at most one flip**
- If current is `1`: Extend sequence → `dp1++` (no flip needed or already flipped)
- If current is `0`: Flip this 0, use previous `dp0` → `dp1 = dp0 + 1`

### **State Transition Logic**

```cpp
if(nums[i] == 1) {
    // Both states can extend
    dp1++;  // Continue with/without flip
    dp0++;  // Continue without flip
} else {
    // nums[i] == 0
    dp1 = dp0 + 1;  // Flip this 0, use previous sequence
    dp0 = 0;        // Can't extend without flip
}
```

### **Why This Works**

1. **`dp0` tracks pure sequences**: Only counts consecutive 1s without any flips
2. **`dp1` tracks sequences with one flip**: Can use one flip to extend sequence
3. **When we see a 0**: 
   - We can't extend `dp0` (would require flip)
   - We can extend `dp1` by flipping this 0 and using the previous `dp0` sequence
4. **Result**: Maximum of both states gives us the answer

## Complexity Analysis

### **Time Complexity:** O(n)
- **Single pass**: Iterate through array once
- **Each iteration**: O(1) operations
- **Total**: O(n) where n = array length

### **Space Complexity:** O(1)
- **Variables**: Only `dp0`, `dp1`, and `rtn` (constant space)
- **No extra arrays**: Space-efficient solution
- **Total**: O(1)

## Key Points

1. **Two-State DP**: Track sequences with and without flip
2. **State Transitions**: Clear logic for extending or resetting sequences
3. **Space Efficient**: O(1) space, only track current states
4. **Single Pass**: O(n) time, process each element once
5. **Optimal**: Finds maximum consecutive ones with at most one flip

## Alternative Approaches

### **Approach 1: Two-State DP (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Space-efficient solution

### **Approach 2: Sliding Window**
- **Time**: O(n)
- **Space**: O(1)
- **Maintain window**: Keep at most one 0 in window
- **Expand/Shrink**: Adjust window based on zero count

### **Approach 3: Track Zero Indices**
- **Time**: O(n)
- **Space**: O(k) where k = number of zeros
- **Store indices**: Keep track of zero positions
- **Calculate**: Max window with at most one zero

## Detailed Example Walkthrough

### **Example: `nums = [1,0,1,1,0,1]`**

```
Position:  0  1  2  3  4  5
nums:     [1, 0, 1, 1, 0, 1]

i=0: nums[0]=1
  dp0 = 1, dp1 = 1
  rtn = 1

i=1: nums[1]=0
  dp1 = dp0 + 1 = 1 + 1 = 2  (flip 0 at index 1)
  dp0 = 0  (reset)
  rtn = max(1, 2) = 2

i=2: nums[2]=1
  dp1 = 2 + 1 = 3  (extend with flip)
  dp0 = 0 + 1 = 1  (new sequence)
  rtn = max(2, 3) = 3

i=3: nums[3]=1
  dp1 = 3 + 1 = 4  (extend with flip)
  dp0 = 1 + 1 = 2  (extend without flip)
  rtn = max(3, 4) = 4

i=4: nums[4]=0
  dp1 = dp0 + 1 = 2 + 1 = 3  (flip 0 at index 4, use dp0 sequence)
  dp0 = 0  (reset)
  rtn = max(4, 3) = 4

i=5: nums[5]=1
  dp1 = 3 + 1 = 4  (extend with flip)
  dp0 = 0 + 1 = 1  (new sequence)
  rtn = max(4, 4) = 4

Result: 4
```

### **Visual Explanation:**

```
nums:     [1, 0, 1, 1, 0, 1]
           ↑  ↑  ↑  ↑  ↑  ↑
           |  |  |  |  |  |
           |  |  |  |  |  └─ dp0=1, dp1=4
           |  |  |  |  └──── dp0=0, dp1=3 (flip at index 4)
           |  |  |  └─────── dp0=2, dp1=4
           |  |  └───────── dp0=1, dp1=3
           |  └──────────── dp0=0, dp1=2 (flip at index 1)
           └─────────────── dp0=1, dp1=1

Best sequence: [1,0,1,1] with flip at index 1 → [1,1,1,1] = 4 consecutive ones
```

## Edge Cases

1. **All ones**: `[1,1,1,1]` → Return length (4)
2. **All zeros**: `[0,0,0]` → Return 1 (flip one zero)
3. **Single element**: `[1]` → Return 1
4. **Single zero**: `[0]` → Return 1 (flip it)
5. **Alternating**: `[1,0,1,0,1]` → Return 3 (flip one zero)

## Related Problems

- [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) - Without flipping
- [487. Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) - Current problem (flip at most 1)
- [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) - Flip at most k zeros
- [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) - Similar sliding window

## Tags

`Array`, `Dynamic Programming`, `Sliding Window`, `Medium`

