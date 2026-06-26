---
layout: post
title: "[Medium] 376. Wiggle Subsequence"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming, greedy]
permalink: /2026/01/04/medium-376-wiggle-subsequence/
---
A **wiggle sequence** is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative.

- For example, `[1, 7, 4, 9, 2, 5]` is a **wiggle sequence** because the differences `(6, -3, 5, -7, 3)` alternate between positive and negative.
- In contrast, `[1, 4, 7, 2, 5]` and `[1, 7, 4, 5, 5]` are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.

A **subsequence** is obtained by deleting some (possibly zero) elements from the original sequence, leaving the remaining elements in their original order.

Given an integer array `nums`, return *the length of the longest **wiggle subsequence** of* `nums`*.*

## Examples

**Example 1:**
```
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence because differences (6, -3, 5, -7, 3) alternate.
```

**Example 2:**
```
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1,17,10,13,10,16,8] with differences (16, -7, 3, -3, 6, -8).
```

**Example 3:**
```
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
Explanation: The longest wiggle subsequence is [1, 2] or [1, 9] with difference 1 or 8.
```

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`

## Thinking Process

A **wiggle sequence** is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative.

- For example, `[1, 7, 4, 9, 2, 5]` is a **wiggle sequence** because the differences `(6, -3, 5, -7, 3)` alternate between positive and negative.

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">1D DP recurrence</text>

  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

## Solution

### **Solution: Greedy with Difference Tracking**

```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        const int N = nums.size();
        if(N < 2) return N;

        int prevDiff = nums[1] - nums[0];
        int rtn = prevDiff != 0? 2 : 1;
        for(int i = 2; i < N; i++) {
            int diff = nums[i] - nums[i - 1];
            if((diff > 0 && prevDiff <= 0) ||
                diff < 0 && prevDiff >= 0) {
                    rtn++;
                    prevDiff = diff;
                }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** A **wiggle sequence** is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative.

**How the code works:**
- For example, `[1, 7, 4, 9, 2, 5]` is a **wiggle sequence** because the differences `(6, -3, 5, -7, 3)` alternate between positive and negative.
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `nums = [1,7,4,9,2,5]`, expected output `6`:

The entire sequence is a wiggle sequence because differences (6, -3, 5, -7, 3) alternate.

**Time:** O(n) where n is the length of `nums` · **Space:** O(1)

### **Algorithm Explanation:**

1. **Edge Case Check (Lines 4-5)**:
   - If array has less than 2 elements, return its length
   - Single element is always a valid wiggle sequence

2. **Initialize (Lines 7-8)**:
   - `prevDiff`: Difference between first two elements
   - `rtn`: Length of wiggle subsequence
     - If `prevDiff != 0`: Start with 2 elements (both are part of wiggle)
     - If `prevDiff == 0`: Start with 1 element (only first element counts)

3. **Process Remaining Elements (Lines 9-16)**:
   - **For each element** from index 2 to end:
     - **Calculate difference**: `diff = nums[i] - nums[i - 1]`
     - **Check sign alternation**:
       - **If `diff > 0` and `prevDiff <= 0`**: Sign changed from non-positive to positive
       - **If `diff < 0` and `prevDiff >= 0`**: Sign changed from non-negative to negative
     - **If sign alternates**:
       - Increment count: `rtn++`
       - Update previous difference: `prevDiff = diff`
     - **If sign doesn't alternate**: Skip this element (don't update `prevDiff`)

4. **Return (Line 17)**:
   - Return the length of the longest wiggle subsequence

### **Why This Works:**

**Key Insight**: We only need to count elements where the difference sign alternates. Elements that don't cause a sign change can be skipped.

**Greedy Choice**: 
- If the current difference has a different sign than the previous difference, include the element
- This locally optimal choice (include when sign changes) leads to a globally optimal solution

**Why Skip Equal Differences**:
- If `diff == 0`, there's no sign change, so we don't include the element
- We also don't update `prevDiff` when `diff == 0`, so we keep the last non-zero difference

**Example Walkthrough:**

**Example 1: `nums = [1,7,4,9,2,5]`**

**Execution:**
```
Initial: N = 6
prevDiff = nums[1] - nums[0] = 7 - 1 = 6 (positive)
rtn = 2 (since prevDiff != 0)

i=2: nums[2]=4
  diff = 4 - 7 = -3 (negative)
  Check: diff < 0 && prevDiff >= 0? Yes (-3 < 0 && 6 >= 0)
  rtn = 2 + 1 = 3
  prevDiff = -3
  State: rtn=3, prevDiff=-3

i=3: nums[3]=9
  diff = 9 - 4 = 5 (positive)
  Check: diff > 0 && prevDiff <= 0? Yes (5 > 0 && -3 <= 0)
  rtn = 3 + 1 = 4
  prevDiff = 5
  State: rtn=4, prevDiff=5

i=4: nums[4]=2
  diff = 2 - 9 = -7 (negative)
  Check: diff < 0 && prevDiff >= 0? Yes (-7 < 0 && 5 >= 0)
  rtn = 4 + 1 = 5
  prevDiff = -7
  State: rtn=5, prevDiff=-7

i=5: nums[5]=5
  diff = 5 - 2 = 3 (positive)
  Check: diff > 0 && prevDiff <= 0? Yes (3 > 0 && -7 <= 0)
  rtn = 5 + 1 = 6
  prevDiff = 3
  State: rtn=6, prevDiff=3

Result: 6
Wiggle sequence: [1, 7, 4, 9, 2, 5]
Differences: (6, -3, 5, -7, 3) - all alternate
```

**Example 2: `nums = [1,17,5,10,13,15,10,5,16,8]`**

**Execution:**
```
Initial: N = 10
prevDiff = 17 - 1 = 16 (positive)
rtn = 2

i=2: nums[2]=5
  diff = 5 - 17 = -12 (negative)
  Check: diff < 0 && prevDiff >= 0? Yes
  rtn = 3, prevDiff = -12

i=3: nums[3]=10
  diff = 10 - 5 = 5 (positive)
  Check: diff > 0 && prevDiff <= 0? Yes
  rtn = 4, prevDiff = 5

i=4: nums[4]=13
  diff = 13 - 10 = 3 (positive)
  Check: diff > 0 && prevDiff <= 0? No (both positive)
  Skip (don't update prevDiff)

i=5: nums[5]=15
  diff = 15 - 13 = 2 (positive)
  Check: diff > 0 && prevDiff <= 0? No (prevDiff is still 5, positive)
  Skip

i=6: nums[6]=10
  diff = 10 - 15 = -5 (negative)
  Check: diff < 0 && prevDiff >= 0? Yes (prevDiff is 5, positive)
  rtn = 5, prevDiff = -5

i=7: nums[7]=5
  diff = 5 - 10 = -5 (negative)
  Check: diff < 0 && prevDiff >= 0? No (both negative)
  Skip

i=8: nums[8]=16
  diff = 16 - 5 = 11 (positive)
  Check: diff > 0 && prevDiff <= 0? Yes
  rtn = 6, prevDiff = 11

i=9: nums[9]=8
  diff = 8 - 16 = -8 (negative)
  Check: diff < 0 && prevDiff >= 0? Yes
  rtn = 7, prevDiff = -8

Result: 7
Wiggle sequence: [1, 17, 5, 10, 13, 10, 16, 8] (or similar)
```

**Example 3: `nums = [1,2,3,4,5,6,7,8,9]`**

**Execution:**
```
Initial: N = 9
prevDiff = 2 - 1 = 1 (positive)
rtn = 2

i=2: nums[2]=3
  diff = 3 - 2 = 1 (positive)
  Check: diff > 0 && prevDiff <= 0? No (both positive)
  Skip

i=3: nums[3]=4
  diff = 4 - 3 = 1 (positive)
  Check: diff > 0 && prevDiff <= 0? No
  Skip

... (all differences are positive, so no sign changes)

Result: 2
Wiggle sequence: [1, 2] or [1, 9]
```
## Algorithm Breakdown

### **Why Greedy Works**

**Greedy Choice Property**: At each position, if the sign of the difference alternates, include the element. This is optimal because:
1. **No Regret**: Including an element that causes a sign change always increases the wiggle length
2. **Optimal Substructure**: The longest wiggle subsequence ending at position `i` depends only on the last sign
3. **Local Optimality**: Making the locally optimal choice (include when sign changes) leads to global optimum

### **Why Skip Equal Differences**

**Zero Difference**: When `diff == 0`, there's no sign change, so:
- We don't include the element in the wiggle sequence
- We don't update `prevDiff` (keep the last non-zero difference)
- This allows us to "skip" equal elements and wait for the next sign change

**Example**: `nums = [1, 2, 2, 3]`
- Differences: `(1, 0, 1)`
- We skip the middle `2` (diff = 0)
- Result: `[1, 2, 3]` with differences `(1, 1)` - but wait, that's not a wiggle...

Actually, let me reconsider. If we have `[1, 2, 2, 3]`:
- `prevDiff = 1` (positive)
- At `2, 2`: `diff = 0`, we skip, `prevDiff` stays `1`
- At `2, 3`: `diff = 1` (positive), same sign as `prevDiff`, so we skip
- Result: `[1, 2, 3]` is not a wiggle, but the algorithm returns 2 (correct: `[1, 2]` or `[1, 3]`)

### **Sign Alternation Logic**

**Condition**: `(diff > 0 && prevDiff <= 0) || (diff < 0 && prevDiff >= 0)`

**Why `<=` and `>=` instead of `<` and `>`?**
- We want to count when sign changes from non-positive to positive, or non-negative to negative
- This handles the case where `prevDiff == 0` (we want to count the first non-zero difference after zeros)
- Example: `[1, 1, 2]` → differences: `(0, 1)`
  - `prevDiff = 0`, `diff = 1`
  - `diff > 0 && prevDiff <= 0` → true, so we count it

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the length of `nums`
  - Single pass through the array
  - Each iteration does O(1) work
- **Space Complexity**: O(1)
  - Only using a few variables (`prevDiff`, `rtn`, `diff`, `i`)
  - No additional data structures

## Key Points

1. **Greedy Algorithm**: Count elements where difference sign alternates
2. **Difference Tracking**: Track the sign of differences, not the values
3. **Skip Zeros**: Don't count elements with zero difference
4. **Sign Alternation**: Use `<=` and `>=` to handle zero differences correctly
5. **Optimal**: This greedy strategy finds the longest wiggle subsequence

## Common Mistakes

1. **Single element**: `[1]` → return 1
2. **Two elements (different)**: `[1, 2]` → return 2
3. **Two elements (same)**: `[1, 1]` → return 1
4. **All increasing**: `[1,2,3,4,5]` → return 2
5. **All decreasing**: `[5,4,3,2,1]` → return 2
6. **All equal**: `[1,1,1,1]` → return 1
7. **Perfect wiggle**: `[1,7,4,9,2,5]` → return 6

1. **Wrong sign check**: Using `>` and `<` instead of `>=` and `<=`
2. **Not handling zeros**: Forgetting to skip elements with zero difference
3. **Not updating prevDiff**: Updating `prevDiff` even when sign doesn't change
4. **Wrong initialization**: Not handling the case where first difference is zero
5. **Off-by-one errors**: Incorrect loop bounds or initialization

## Related Problems

- [300. Longest Increasing Subsequence](https://www.leetcode.com/problems/longest-increasing-subsequence/) - Similar subsequence problem
- [53. Maximum Subarray](https://www.leetcode.com/problems/maximum-subarray/) - Subarray problem
- [392. Is Subsequence](https://www.leetcode.com/problems/is-subsequence/) - Subsequence matching
- [121. Best Time to Buy and Sell Stock](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Similar pattern

## Follow-Up: Why `<=` and `>=` Instead of `<` and `>`?

**Question**: Why do we use `prevDiff <= 0` and `prevDiff >= 0` instead of `prevDiff < 0` and `prevDiff > 0`?

**Answer**:
- We want to count the **first non-zero difference** after a sequence of zeros
- If `prevDiff == 0`, we haven't established a sign yet
- When we see the first non-zero difference, we should count it
- Example: `[1, 1, 2]` → differences: `(0, 1)`
  - `prevDiff = 0`, `diff = 1`
  - With `prevDiff <= 0`: `1 > 0 && 0 <= 0` → true, count it ✓
  - With `prevDiff < 0`: `1 > 0 && 0 < 0` → false, don't count ✗

**Therefore**: Using `<=` and `>=` correctly handles the transition from zero to non-zero differences.

## Tags

`Array`, `Dynamic Programming`, `Greedy`, `Medium`

## Key Takeaways

- For example, `[1, 7, 4, 9, 2, 5]` is a **wiggle sequence** because the differences `(6, -3, 5, -7, 3)` alternate between positive and negative.
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?

## References

- [LC 376: Wiggle Subsequence on LeetCode](https://www.leetcode.com/problems/wiggle-subsequence/)
- [LeetCode Discuss — LC 376: Wiggle Subsequence](https://www.leetcode.com/problems/wiggle-subsequence/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/wiggle-subsequence/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
