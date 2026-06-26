---
layout: post
title: "[Medium] 487. Max Consecutive Ones II"
date: 2025-12-30 19:30:00 -0700
categories: [leetcode, medium, array, dynamic-programming, sliding-window]
permalink: /2025/12/30/medium-487-max-consecutive-ones-ii/
---
Given a binary array `nums`, return *the maximum number of consecutive `1`'s in the array if you can flip at most one `0`*.

## Thinking Process

Given a binary array `nums`, return *the maximum number of consecutive `1`'s in the array if you can flip at most one `0`*.

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



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
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

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

### Complexity
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [485. Max Consecutive Ones](https://www.leetcode.com/problems/max-consecutive-ones/) - Without flipping
- [487. Max Consecutive Ones II](https://www.leetcode.com/problems/max-consecutive-ones-ii/) - Current problem (flip at most 1)
- [1004. Max Consecutive Ones III](https://www.leetcode.com/problems/max-consecutive-ones-iii/) - Flip at most k zeros
- [424. Longest Repeating Character Replacement](https://www.leetcode.com/problems/longest-repeating-character-replacement/) - Similar sliding window

## Tags

`Array`, `Dynamic Programming`, `Sliding Window`, `Medium`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 487: Max Consecutive Ones II on LeetCode](https://www.leetcode.com/problems/max-consecutive-ones-ii/)
- [LeetCode Discuss — LC 487: Max Consecutive Ones II](https://www.leetcode.com/problems/max-consecutive-ones-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/max-consecutive-ones-ii/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
