---
layout: post
title: "[Easy] 485. Max Consecutive Ones"
date: 2025-11-04 21:14:45 -0800
categories: leetcode algorithm easy cpp arrays sliding-window problem-solving
permalink: /posts/2025-11-04-easy-485-max-consecutive-ones/
tags: [leetcode, easy, array, sliding-window, counting]
---
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

## Thinking Process

1. **Single Pass**: Process each element exactly once

- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Sliding window</text>

  <rect x="20" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="36" y="63" text-anchor="middle" font-size="11">a</text>
  <rect x="52" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="68" y="63" text-anchor="middle" font-size="11">b</text>
  <rect x="84" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="63" text-anchor="middle" font-size="11">c</text>
  <rect x="116" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="132" y="63" text-anchor="middle" font-size="11">d</text>
  <rect x="148" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="164" y="63" text-anchor="middle" font-size="11">e</text>
  <rect x="52" y="38" width="64" height="42" rx="4" fill="none" stroke="#C4956A" stroke-width="2" stroke-dasharray="4"/>
  <text x="84" y="32" text-anchor="middle" font-size="10" fill="#C4956A" font-weight="600">window</text>
  <text x="110" y="105" text-anchor="middle" font-size="11" fill="#6B6560">expand right, shrink left when invalid</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Fixed-size window** *(this problem)* | O(n) | O(1) | Window size known upfront |
| Variable-size window | O(n) | O(1) | Expand/shrink until valid |
| Window + hash map | O(n) | O(k) | Track character/count frequencies |
| Deque window max | O(n) | O(k) | Monotonic deque for max/min in window |

## Solution

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

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** 1. **Single Pass**: Process each element exactly once

**How the code works:**
1. **Single Pass**: Process each element exactly once
- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

**Walkthrough** — input `nums = [1,1,0,1,1,1]`, expected output `3`:

The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Single pass through the array |
| **Space** | O(1) - Only using two integer variables |
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

### Complexity
| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Single pass through the array |
| **Space** | O(1) - Only using two integer variables |

## Why This Solution is Optimal

1. **Single Pass**: Each element is visited exactly once - O(n) time
2. **Constant Space**: Only uses two integer variables - O(1) space
3. **Simple Logic**: Easy to understand and implement
4. **No Extra Data Structures**: No need for arrays, maps, or sets

## Common Mistakes

1. **All zeros**: `[0,0,0]` → `0`
2. **All ones**: `[1,1,1]` → `3`
3. **Single element (one)**: `[1]` → `1`
4. **Single element (zero)**: `[0]` → `0`
5. **Alternating**: `[1,0,1,0,1]` → `1`

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

- [487. Max Consecutive Ones II](https://www.leetcode.com/problems/max-consecutive-ones-ii/) - Can flip at most one 0
- [1004. Max Consecutive Ones III](https://www.leetcode.com/problems/max-consecutive-ones-iii/) - Can flip at most k 0s
- [1446. Consecutive Characters](https://www.leetcode.com/problems/consecutive-characters/) - Similar problem with strings
- [1869. Longer Contiguous Segments of Ones than Zeros](https://www.leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/) - Compare consecutive segments

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

## Key Takeaways

1. **Single Pass**: Process each element exactly once
2. **Counter Reset**: Reset counter to 0 when encountering 0
3. **Track Maximum**: Update maximum count whenever we see a 1
4. **Simple Logic**: No complex data structures needed

## References

- [LC 485: Max Consecutive Ones on LeetCode](https://www.leetcode.com/problems/max-consecutive-ones/)
- [LeetCode Discuss — LC 485: Max Consecutive Ones](https://www.leetcode.com/problems/max-consecutive-ones/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/max-consecutive-ones/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
