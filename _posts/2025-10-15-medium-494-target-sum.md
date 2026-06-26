---
layout: post
title: "[Medium] 494. Target Sum"
date: 2025-10-15 15:28:04 -0700
categories: leetcode algorithm medium cpp dynamic-programming dp subset-sum problem-solving
---
You are given an integer array `nums` and an integer `target`.

You want to build an expression out of `nums` by adding one of the symbols `+` and `-` before each integer in `nums` and then concatenate all the integers.

For example, if `nums = [2, 1]`, you can add a `+` before `2` and a `-` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different expressions that you can build, which evaluates to `target`.

## Examples

**Example 1:**
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums equal to target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

**Example 2:**
```
Input: nums = [1], target = 1
Output: 1
```

## Constraints

- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

## Thinking Process

1. **Mathematical Transformation:** Convert to subset sum problem

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

**Time Complexity:** O(n × sum)  
**Space Complexity:** O(sum)

Convert the problem to a subset sum problem using mathematical transformation.

```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        
        // Check if target is achievable
        if((target + totalSum) % 2 != 0 || abs(target) > totalSum) {
            return 0;
        }
        
        int subsetSum = (target + totalSum) / 2;
        vector<int> dp(subsetSum + 1, 0);
        dp[0] = 1;
        
        for(int num : nums) {
            for(int i = subsetSum; i >= num; i--) {
                dp[i] += dp[i - num];
            }
        }
        
        return dp[subsetSum];
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **Mathematical Transformation:** Convert to subset sum problem

**How the code works:**
1. **Mathematical Transformation:** Convert to subset sum problem
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `nums = [1,1,1,1,1], target = 3`, expected output `5`:

There are 5 ways to assign symbols to make the sum of nums equal to target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(2^n) | O(n) |
| Memoization | O(n × sum) | O(n × sum) |
| DP (Subset Sum) | O(n × sum) | O(sum) |
## Algorithm Breakdown

### 1. Validation Check
```cpp
if((target + totalSum) % 2 != 0 || abs(target) > totalSum) {
    return 0;
}
```

**Why this check?**
- If `(target + totalSum)` is odd, `subsetSum` would be fractional (impossible)
- If `abs(target) > totalSum`, it's impossible to achieve the target

### 2. Subset Sum Calculation
```cpp
int subsetSum = (target + totalSum) / 2;
```

**Mathematical proof:**
- `S+ - S- = target` (equation 1)
- `S+ + S- = totalSum` (equation 2)
- Adding equations: `2S+ = target + totalSum`
- Therefore: `S+ = (target + totalSum) / 2`

### 3. DP Array Initialization
```cpp
vector<int> dp(subsetSum + 1, 0);
dp[0] = 1;  // One way to make sum 0 (empty subset)
```

### 4. Bottom-Up DP
```cpp
for(int num : nums) {
    for(int i = subsetSum; i >= num; i--) {
        dp[i] += dp[i - num];
    }
}
```

**Why iterate backwards?**
- Prevents using the same number twice in one iteration
- Ensures we only use numbers from previous iterations

### Complexity
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(2^n) | O(n) |
| Memoization | O(n × sum) | O(n × sum) |
| DP (Subset Sum) | O(n × sum) | O(sum) |

## Common Mistakes

1. **Impossible target:** `nums = [1], target = 2` → `0`
2. **Single element:** `nums = [1], target = 1` → `1`
3. **Zero target:** `nums = [1,1], target = 0` → `2`
4. **Large numbers:** `nums = [1000], target = 1000` → `1`

1. **Forgetting validation:** Not checking if target is achievable
2. **Wrong iteration order:** Using forward iteration in DP
3. **Incorrect subset sum formula:** Wrong calculation of `subsetSum`
4. **Array bounds:** Not handling edge cases properly

## Related Problems

- [416. Partition Equal Subset Sum](https://www.leetcode.com/problems/partition-equal-subset-sum/)
- [1049. Last Stone Weight II](https://www.leetcode.com/problems/last-stone-weight-ii/)
- [474. Ones and Zeroes](https://www.leetcode.com/problems/ones-and-zeroes/)
- [322. Coin Change](https://www.leetcode.com/problems/coin-change/)

## Why This Solution is Optimal

1. **Mathematical Insight:** Transforms exponential problem to polynomial
2. **Space Efficient:** Uses 1D DP array instead of 2D
3. **Early Termination:** Validates feasibility before computation
4. **Optimal Complexity:** O(n × sum) is the best possible for this problem

## References

- [LC 494: Target Sum on LeetCode](https://www.leetcode.com/problems/target-sum/)
- [LeetCode Discuss — LC 494: Target Sum](https://www.leetcode.com/problems/target-sum/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/target-sum/editorial/) *(may require premium)*

## Key Takeaways

1. **Mathematical Transformation:** Convert to subset sum problem
2. **DP Optimization:** Use 1D array instead of 2D
3. **Backward Iteration:** Prevents double counting
4. **Early Validation:** Check feasibility before computation
