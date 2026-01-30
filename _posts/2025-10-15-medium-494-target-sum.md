---
layout: post
title: "[Medium] 494. Target Sum"
date: 2025-10-15 15:28:04 -0700
categories: leetcode algorithm medium cpp dynamic-programming dp subset-sum problem-solving
---

# [Medium] 494. Target Sum

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Operation definition**: What operations can we perform? (Assumption: Add '+' or '-' before each number - assign sign to each number)

2. **Expression evaluation**: How is the expression evaluated? (Assumption: Sum all numbers with their assigned signs - standard arithmetic)

3. **All numbers**: Must we use all numbers? (Assumption: Yes - must assign sign to every number in the array)

4. **Order preservation**: Can we reorder numbers? (Assumption: No - must maintain original order, only assign signs)

5. **Return value**: What should we return? (Assumption: Count of ways to assign signs to get target sum - integer)

## Solution: Dynamic Programming (Subset Sum)

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

## How the Algorithm Works

### Mathematical Transformation

The key insight is to transform the problem into a subset sum problem:

1. **Original Problem:** Find ways to assign `+` or `-` to each number
2. **Transformation:** Let `S+` be the sum of numbers with `+` and `S-` be the sum of numbers with `-`
3. **Equations:**
   - `S+ - S- = target`
   - `S+ + S- = totalSum`
4. **Solving:** `S+ = (target + totalSum) / 2`

### Step-by-Step Example: `nums = [1,1,1,1,1], target = 3`

| Step | Calculation | Value |
|------|-------------|-------|
| 1 | `totalSum = 1+1+1+1+1` | `5` |
| 2 | `subsetSum = (3+5)/2` | `4` |
| 3 | Find ways to make sum `4` | `5` ways |

**DP Table for subsetSum = 4:**
```
nums = [1,1,1,1,1], target subsetSum = 4

Initial: dp = [1,0,0,0,0]

After num=1: dp = [1,1,0,0,0]
After num=1: dp = [1,2,1,0,0]  
After num=1: dp = [1,3,3,1,0]
After num=1: dp = [1,4,6,4,1]
After num=1: dp = [1,5,10,10,5]

Answer: dp[4] = 5
```

### Visual Representation

```
Original Problem: [1,1,1,1,1] with target = 3

Possible combinations:
+1 +1 +1 +1 -1 = 3  ✓
+1 +1 +1 -1 +1 = 3  ✓  
+1 +1 -1 +1 +1 = 3  ✓
+1 -1 +1 +1 +1 = 3  ✓
-1 +1 +1 +1 +1 = 3  ✓

Total: 5 ways
```

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

## Alternative Approaches

### Approach 1: Brute Force (DFS)
```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        return dfs(nums, 0, target);
    }
    
private:
    int dfs(vector<int>& nums, int index, int target) {
        if (index == nums.size()) {
            return target == 0 ? 1 : 0;
        }
        
        return dfs(nums, index + 1, target - nums[index]) +
               dfs(nums, index + 1, target + nums[index]);
    }
};
```

**Time Complexity:** O(2^n)  
**Space Complexity:** O(n)

### Approach 2: Memoization
```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        unordered_map<string, int> memo;
        return dfs(nums, 0, target, memo);
    }
    
private:
    int dfs(vector<int>& nums, int index, int target, unordered_map<string, int>& memo) {
        if (index == nums.size()) {
            return target == 0 ? 1 : 0;
        }
        
        string key = to_string(index) + "," + to_string(target);
        if (memo.count(key)) {
            return memo[key];
        }
        
        int result = dfs(nums, index + 1, target - nums[index], memo) +
                     dfs(nums, index + 1, target + nums[index], memo);
        
        memo[key] = result;
        return result;
    }
};
```

**Time Complexity:** O(n × sum)  
**Space Complexity:** O(n × sum)

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(2^n) | O(n) |
| Memoization | O(n × sum) | O(n × sum) |
| DP (Subset Sum) | O(n × sum) | O(sum) |

## Edge Cases

1. **Impossible target:** `nums = [1], target = 2` → `0`
2. **Single element:** `nums = [1], target = 1` → `1`
3. **Zero target:** `nums = [1,1], target = 0` → `2`
4. **Large numbers:** `nums = [1000], target = 1000` → `1`

## Key Insights

1. **Mathematical Transformation:** Convert to subset sum problem
2. **DP Optimization:** Use 1D array instead of 2D
3. **Backward Iteration:** Prevents double counting
4. **Early Validation:** Check feasibility before computation

## Common Mistakes

1. **Forgetting validation:** Not checking if target is achievable
2. **Wrong iteration order:** Using forward iteration in DP
3. **Incorrect subset sum formula:** Wrong calculation of `subsetSum`
4. **Array bounds:** Not handling edge cases properly

## Related Problems

- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [1049. Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)
- [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)
- [322. Coin Change](https://leetcode.com/problems/coin-change/)

## Why This Solution is Optimal

1. **Mathematical Insight:** Transforms exponential problem to polynomial
2. **Space Efficient:** Uses 1D DP array instead of 2D
3. **Early Termination:** Validates feasibility before computation
4. **Optimal Complexity:** O(n × sum) is the best possible for this problem
