---
layout: post
title: "[Medium] 53. Maximum Subarray"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming, greedy, divide-and-conquer]
permalink: /2026/01/04/medium-53-maximum-subarray/
---
Given an integer array `nums`, find the **subarray** with the largest sum, and return *its sum*.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Thinking Process

Given an integer array `nums`, find the **subarray** with the largest sum, and return *its sum*.

A **subarray** is a contiguous non-empty sequence of elements within an array.

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
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

## Examples

**Example 1:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

**Example 2:**
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

**Example 3:**
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Algorithm Breakdown

### **Why Kadane's Algorithm Works**

**Greedy Choice Property**: At each position, choosing the maximum between starting fresh and extending is optimal.

**Mathematical Proof**:
- Let `S[i]` be the maximum subarray sum ending at position `i`
- `S[i] = max(nums[i], S[i-1] + nums[i])`
- If `S[i-1] < 0`, then `S[i-1] + nums[i] < nums[i]`, so we should start fresh
- If `S[i-1] >= 0`, then `S[i-1] + nums[i] >= nums[i]`, so we should extend

**Optimal Substructure**:
- The maximum subarray ending at `i` depends only on the maximum subarray ending at `i-1`
- No need to reconsider previous choices
- This allows O(n) time complexity

### **Key Insight: When to Start Fresh**

**Condition**: Start a new subarray when `currSum < 0`

**Why**:
- If `currSum` is negative, adding it to `nums[i]` will only make the sum smaller
- Starting fresh with `nums[i]` alone is better
- This is equivalent to: `currSum + nums[i] < nums[i]` when `currSum < 0`

**Example**:
```
nums = [-2, 1, -3, 4]
        ↑   ↑
      currSum = -2 (negative)
      At position 1: max(1, -2 + 1) = max(1, -1) = 1
      Start fresh with 1
```

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the length of `nums`
  - Single pass through the array
  - Each iteration does O(1) work
- **Space Complexity**: O(1)
  - Only using two variables (`maxSum`, `currSum`)
  - No additional data structures

## Key Points

1. **Kadane's Algorithm**: Classic greedy/DP solution for maximum subarray
2. **Greedy Choice**: At each position, choose to extend or start fresh
3. **Optimal**: This greedy strategy finds the global maximum
4. **Efficient**: O(n) time, O(1) space
5. **Simple**: Straightforward implementation

## Common Mistakes

1. **Single element**: `[5]` → return 5
2. **All negative**: `[-2,-1,-3]` → return -1 (least negative)
3. **All positive**: `[1,2,3,4]` → return 10 (sum of all)
4. **Mixed**: `[-2,1,-3,4,-1,2,1,-5,4]` → return 6
5. **One positive**: `[-1,-2,5,-3]` → return 5

1. **Not initializing correctly**: Starting with 0 instead of `nums[0]`
2. **Wrong update**: Using `currSum += nums[i]` without checking if it's better to start fresh
3. **Not tracking global max**: Only returning `currSum` instead of `maxSum`
4. **Off-by-one errors**: Incorrect loop bounds
5. **Handling negatives**: Not understanding when to start fresh

## Related Problems

- [121. Best Time to Buy and Sell Stock](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Similar greedy approach
- [152. Maximum Product Subarray](https://www.leetcode.com/problems/maximum-product-subarray/) - Similar but for product
- [209. Minimum Size Subarray Sum](https://www.leetcode.com/problems/minimum-size-subarray-sum/) - Find minimum subarray with sum >= target
- [560. Subarray Sum Equals K](https://www.leetcode.com/problems/subarray-sum-equals-k/) - Find subarrays with sum k
- [918. Maximum Sum Circular Subarray](https://www.leetcode.com/problems/maximum-sum-circular-subarray/) - Extension to circular array

## Follow-Up: Finding the Subarray Indices

**Question**: How to find the actual subarray (not just the sum)?

**Answer**: Track the start and end indices:

```cpp
vector<int> maxSubArrayIndices(vector<int>& nums) {
    int maxSum = nums[0], currSum = nums[0];
    int start = 0, end = 0, currStart = 0;
    
    for(int i = 1; i < nums.size(); i++) {
        if(currSum < 0) {
            currSum = nums[i];
            currStart = i;
        } else {
            currSum += nums[i];
        }
        
        if(currSum > maxSum) {
            maxSum = currSum;
            start = currStart;
            end = i;
        }
    }
    
    return {start, end};  // Return indices of maximum subarray
}
```

## Tags

`Array`, `Dynamic Programming`, `Greedy`, `Divide and Conquer`, `Medium`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 53: Maximum Subarray on LeetCode](https://www.leetcode.com/problems/maximum-subarray/)
- [LeetCode Discuss — LC 53: Maximum Subarray](https://www.leetcode.com/problems/maximum-subarray/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/maximum-subarray/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
