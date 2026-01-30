---
layout: post
title: "[Easy] 485. Max Consecutive Ones"
date: 2025-11-04 21:14:45 -0800
categories: leetcode algorithm easy cpp arrays sliding-window problem-solving
permalink: /posts/2025-11-04-easy-485-max-consecutive-ones/
tags: [leetcode, easy, array, sliding-window, counting]
---

# [Easy] 485. Max Consecutive Ones

Given a binary array `nums`, return *the maximum number of consecutive `1`'s in the array*.

## Examples

**Example 1:**
```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

**Example 2:**
```
Input: nums = [1,0,1,1,0,1]
Output: 2
```

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Consecutive definition**: What does "consecutive ones" mean? (Assumption: Ones that appear next to each other without any zeros in between)

2. **Array modification**: Can we modify the array? (Assumption: No - just count, don't modify)

3. **Empty array**: What should we return for an empty array? (Assumption: Return 0 - no consecutive ones)

4. **All zeros**: What if array contains only zeros? (Assumption: Return 0 - no consecutive ones)

5. **All ones**: What if array contains only ones? (Assumption: Return array length - all ones are consecutive)

## Interview Deduction Process (10 minutes)

### Step 1: Brute-Force Approach (2 minutes)
**Initial Thought**: "I need to find the longest consecutive ones. Let me check all possible subarrays."

**Naive Solution**: Check all possible subarrays, count consecutive ones in each, return maximum.

**Complexity**: O(n²) time, O(1) space

**Issues**:
- Checks redundant subarrays
- Inefficient for large arrays
- More complex than needed

### Step 2: Semi-Optimized Approach (3 minutes)
**Insight**: "I can traverse once and track current consecutive count, updating maximum as I go."

**Improved Solution**: Single pass through array. Maintain current consecutive count and maximum count. Reset current count when encountering 0.

**Complexity**: O(n) time, O(1) space

**Improvements**:
- Single pass - optimal time complexity
- O(1) space - no extra data structures
- Simple and efficient
- Handles all edge cases

### Step 3: Optimized Solution (5 minutes)
**Final Optimization**: "The single-pass approach is already optimal. Let me verify edge cases."

**Best Solution**: Single-pass with counter is optimal. No further optimization needed.

**Key Realizations**:
1. Single pass is optimal - can't do better than O(n)
2. O(1) space is optimal - no extra storage needed
3. Simple counter approach is elegant and efficient
4. Handles all edge cases naturally

## Solution: Single Pass with Counter

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Use a simple counter to track consecutive ones. Reset the counter when encountering a zero, and update the maximum count whenever we see a one.

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCnt = 0, cnt = 0;
        
        for(int n : nums) {
            if(n == 1) {
                cnt++;
                maxCnt = max(maxCnt, cnt);
            } else {
                cnt = 0;
            }
        }
        
        return maxCnt;
    }
};
```

## How the Algorithm Works

### Step-by-Step Example: `nums = [1,1,0,1,1,1]`

| Step | n | cnt | maxCnt | Action |
|------|---|-----|--------|--------|
| Initial | - | 0 | 0 | - |
| 1 | 1 | 1 | 1 | Increment cnt, update maxCnt |
| 2 | 1 | 2 | 2 | Increment cnt, update maxCnt |
| 3 | 0 | 0 | 2 | Reset cnt to 0 |
| 4 | 1 | 1 | 2 | Increment cnt |
| 5 | 1 | 2 | 2 | Increment cnt |
| 6 | 1 | 3 | 3 | Increment cnt, update maxCnt |

**Final Answer:** 3

### Visual Representation

```
Array: [1, 1, 0, 1, 1, 1]
        ↑  ↑  ↑  ↑  ↑  ↑
        1  2  0  1  2  3
        
Current streak: 1 → 2 → reset → 1 → 2 → 3
Maximum streak: 1 → 2 → 2 → 2 → 2 → 3
```

## Key Insights

1. **Single Pass**: Process each element exactly once
2. **Counter Reset**: Reset counter to 0 when encountering 0
3. **Track Maximum**: Update maximum count whenever we see a 1
4. **Simple Logic**: No complex data structures needed

## Algorithm Breakdown

### 1. Initialize Variables
```cpp
int maxCnt = 0, cnt = 0;
```
- `maxCnt`: Tracks the maximum consecutive ones seen so far
- `cnt`: Tracks the current consecutive ones streak

### 2. Iterate Through Array
```cpp
for(int n : nums) {
```
Process each element in the array.

### 3. Handle Ones
```cpp
if(n == 1) {
    cnt++;
    maxCnt = max(maxCnt, cnt);
}
```
- Increment current streak counter
- Update maximum if current streak is longer

### 4. Handle Zeros
```cpp
else {
    cnt = 0;
}
```
Reset the current streak counter to 0.

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Single pass through the array |
| **Space** | O(1) - Only using two integer variables |

## Edge Cases

1. **All zeros**: `[0,0,0]` → `0`
2. **All ones**: `[1,1,1]` → `3`
3. **Single element (one)**: `[1]` → `1`
4. **Single element (zero)**: `[0]` → `0`
5. **Alternating**: `[1,0,1,0,1]` → `1`

## Alternative Approaches

### Approach 1: Two Pointers (Sliding Window)

While not necessary for this problem, we can use two pointers to explicitly track window boundaries:

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCnt = 0;
        int left = 0;
        
        for(int right = 0; right < nums.size(); right++) {
            if(nums[right] == 0) {
                left = right + 1;  // Reset window start
            } else {
                maxCnt = max(maxCnt, right - left + 1);
            }
        }
        
        return maxCnt;
    }
};
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

### Approach 2: Using accumulate (More Functional)

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCnt = 0, cnt = 0;
        
        for(int n : nums) {
            cnt = (n == 1) ? cnt + 1 : 0;
            maxCnt = max(maxCnt, cnt);
        }
        
        return maxCnt;
    }
};
```

## Why This Solution is Optimal

1. **Single Pass**: Each element is visited exactly once - O(n) time
2. **Constant Space**: Only uses two integer variables - O(1) space
3. **Simple Logic**: Easy to understand and implement
4. **No Extra Data Structures**: No need for arrays, maps, or sets

## Common Mistakes

1. **Not resetting counter**: Forgetting to reset `cnt` when encountering 0
2. **Not updating maxCnt during loop**: Only updating maxCnt at the end
3. **Off-by-one errors**: Incorrectly calculating the streak length
4. **Edge case handling**: Not considering arrays with all zeros or all ones

## Optimization Tips

### Early Termination (if applicable)
If we know the array size and maximum possible, we could potentially terminate early, but for this problem, we need to check all elements.

### Branchless Version
```cpp
int findMaxConsecutiveOnes(vector<int>& nums) {
    int maxCnt = 0, cnt = 0;
    for(int n : nums) {
        cnt = (n == 1) ? cnt + 1 : 0;
        maxCnt = max(maxCnt, cnt);
    }
    return maxCnt;
}
```

## Related Problems

- [487. Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) - Can flip at most one 0
- [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) - Can flip at most k 0s
- [1446. Consecutive Characters](https://leetcode.com/problems/consecutive-characters/) - Similar problem with strings
- [1869. Longer Contiguous Segments of Ones than Zeros](https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/) - Compare consecutive segments

## Pattern Recognition

This problem demonstrates the **"Consecutive Elements"** pattern:
- Track current streak
- Reset streak when condition breaks
- Maintain maximum streak seen

This pattern appears in many problems:
- Longest increasing subsequence
- Longest palindrome substring
- Maximum subarray sum

## Code Quality Notes

1. **Readability**: The solution is clear and self-documenting
2. **Efficiency**: Optimal time and space complexity
3. **Maintainability**: Simple logic that's easy to modify
4. **Robustness**: Handles all edge cases correctly

---

*This problem is a great introduction to the "consecutive elements" pattern, which is fundamental for many array and string problems.*

