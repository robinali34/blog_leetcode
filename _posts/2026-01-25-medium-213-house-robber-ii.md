---
layout: post
title: "213. House Robber II"
date: 2026-01-25 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming]
permalink: /2026/01/25/medium-213-house-robber-ii/
tags: [leetcode, medium, array, dynamic-programming, dp, circular-array]
---

# 213. House Robber II

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. **All houses at this place are arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

## Examples

**Example 1:**

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent.
```

**Example 2:**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 3:**

```
Input: nums = [1,2,3]
Output: 3
Explanation: Rob house 2 (money = 2) or house 3 (money = 3).
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Circular constraint**: Since houses are arranged in a circle, what happens if we rob the first and last house? (Assumption: Cannot rob both first and last house simultaneously - they're adjacent in the circle)

2. **Empty array**: What should we return if the array is empty? (Assumption: Based on constraints, array length is at least 1)

3. **Single house**: What if there's only one house? (Assumption: Rob that single house, return `nums[0]`)

4. **Negative values**: Can house values be negative? (Assumption: No - constraints show `0 <= nums[i]`, all non-negative)

5. **Adjacent houses**: Can we rob two adjacent houses? (Assumption: No - robbing adjacent houses triggers alarm)

## Solution Approach

This is a **circular version** of House Robber (LC 198). The key difference is that the first and last houses are adjacent, so we cannot rob both.

### Key Insights:

1. **Circular Constraint**: Cannot rob both first and last house simultaneously
2. **Break into Two Linear Problems**:
   - Case 1: Rob houses `[0..N-2]` (exclude last house)
   - Case 2: Rob houses `[1..N-1]` (exclude first house)
3. **Take Maximum**: Return `max(case1, case2)`
4. **Reuse Linear Solution**: Use the same DP logic from House Robber for each case

### Algorithm:

1. **Edge Case**: If `N == 1`, return `nums[0]`
2. **Two Cases**:
   - `rob(nums, 0, N-2)`: Rob from first to second-to-last
   - `rob(nums, 1, N-1)`: Rob from second to last
3. **Return Maximum**: `max(case1, case2)`

## Solution

```cpp
class Solution {
/*
Cycle: rtn max(robLinear(0.. N - 2), robLinear(1,.. N - 1))
dp[i] = max(dp[i-2] + nums[i], dp[i - 1])
*/
public:
    int rob(vector<int>& nums) {
        const int N = nums.size();
        if(N == 1) return nums[0];
        return max(
            rob(nums, 0, N - 2),
            rob(nums, 1, N - 1)
        );
    }
private:
    int rob(vector<int>& nums, int l, int r) {
        int prev2 = 0, prev1 = 0;
        for(int i = l; i <= r; i++) {
            int curr = max(prev2 + nums[i], prev1);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};
```

### Algorithm Explanation:

#### **Main Function `rob(nums)`:**

1. **Edge Case Handling**:
   - If `N == 1`, return `nums[0]` (only one house)

2. **Two Cases**:
   - **Case 1**: `rob(nums, 0, N-2)` - Rob houses from index 0 to N-2 (exclude last)
   - **Case 2**: `rob(nums, 1, N-1)` - Rob houses from index 1 to N-1 (exclude first)

3. **Return Maximum**: Take the maximum of both cases

#### **Helper Function `rob(nums, l, r)`:**

This implements the linear House Robber algorithm for the range `[l, r]`:

1. **State Variables**:
   - `prev2`: Maximum money up to two houses ago
   - `prev1`: Maximum money up to one house ago

2. **Iterate Through Range**:
   - For each house `i` from `l` to `r`:
     - `curr = max(prev2 + nums[i], prev1)`
       - **Rob current**: `prev2 + nums[i]` (can't rob previous)
       - **Skip current**: `prev1` (keep previous maximum)
     - Update: `prev2 = prev1`, `prev1 = curr`

3. **Return**: `prev1` (maximum for the range)

### Example Walkthrough:

**Input:** `nums = [2,3,2]`

```
Step 1: Edge case check
  N = 3, not 1 → continue

Step 2: Case 1 - rob(nums, 0, 1) = rob([2,3])
  i=0: curr = max(0+2, 0) = 2
    prev2=0, prev1=2
  i=1: curr = max(0+3, 2) = 3
    prev2=2, prev1=3
  Result: 3

Step 3: Case 2 - rob(nums, 1, 2) = rob([3,2])
  i=1: curr = max(0+3, 0) = 3
    prev2=0, prev1=3
  i=2: curr = max(0+2, 3) = 3
    prev2=3, prev1=3
  Result: 3

Step 4: Return max(3, 3) = 3 ✓
```

**Input:** `nums = [1,2,3,1]`

```
Step 1: N = 4, not 1 → continue

Step 2: Case 1 - rob(nums, 0, 2) = rob([1,2,3])
  i=0: curr = max(0+1, 0) = 1 → prev2=0, prev1=1
  i=1: curr = max(0+2, 1) = 2 → prev2=1, prev1=2
  i=2: curr = max(1+3, 2) = 4 → prev2=2, prev1=4
  Result: 4

Step 3: Case 2 - rob(nums, 1, 3) = rob([2,3,1])
  i=1: curr = max(0+2, 0) = 2 → prev2=0, prev1=2
  i=2: curr = max(0+3, 2) = 3 → prev2=2, prev1=3
  i=3: curr = max(2+1, 3) = 3 → prev2=3, prev1=3
  Result: 3

Step 4: Return max(4, 3) = 4 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Two linear passes: O(n) each
  - Overall: O(n)

- **Space Complexity:** O(1)
  - Only two variables (`prev2`, `prev1`) needed
  - No extra array required
  - Overall: O(1)

## Key Insights

1. **Circular Constraint**: First and last houses are adjacent, so we can't rob both
2. **Break into Two Cases**: 
   - Exclude last house: `[0..N-2]`
   - Exclude first house: `[1..N-1]`
3. **Reuse Linear Solution**: Use the same DP logic from House Robber
4. **Space Optimization**: O(1) space using two variables instead of array
5. **Edge Case**: Single house doesn't need splitting

## Edge Cases

1. **Single house**: `nums = [5]` → return `5`
2. **Two houses**: `nums = [2,3]` → return `max(2,3) = 3`
3. **Three houses**: `nums = [2,3,2]` → return `3` (can't rob first and last)
4. **All same**: `nums = [1,1,1,1]` → return `2` (rob two non-adjacent)
5. **First and last are large**: `nums = [10,1,1,10]` → return `10` (rob either first or last)

## Common Mistakes

1. **Not handling single house**: Forgetting edge case `N == 1`
2. **Wrong range**: Using `[0..N-1]` and `[1..N]` instead of `[0..N-2]` and `[1..N-1]`
3. **Including both endpoints**: Trying to include both first and last in one case
4. **Not taking maximum**: Forgetting to compare both cases
5. **Index out of bounds**: Not checking bounds when `N == 1` or `N == 2`

## Why This Works

### Circular Constraint:

Since houses are arranged in a circle, if we rob house 0, we cannot rob house N-1. This creates two mutually exclusive cases:

1. **Case 1**: Rob houses `[0..N-2]`
   - We can rob house 0, but not house N-1
   - This is a linear problem

2. **Case 2**: Rob houses `[1..N-1]`
   - We cannot rob house 0, but can rob house N-1
   - This is also a linear problem

By taking the maximum of both cases, we ensure we get the optimal solution while respecting the circular constraint.

### Visual Representation:

```
Case 1: [0..N-2] (exclude last)
  [0] [1] [2] ... [N-2] [N-1]
   ✓   ?   ?   ...   ?    ✗

Case 2: [1..N-1] (exclude first)
  [0] [1] [2] ... [N-2] [N-1]
   ✗   ?   ?   ...   ?    ✓

Result: max(case1, case2)
```

## Alternative Approaches

### Approach 2: Using Array-Based DP

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return nums[0];
        if(n == 2) return max(nums[0], nums[1]);
        
        return max(
            robLinear(nums, 0, n - 2),
            robLinear(nums, 1, n - 1)
        );
    }
    
private:
    int robLinear(vector<int>& nums, int start, int end) {
        vector<int> dp(end - start + 1);
        dp[0] = nums[start];
        dp[1] = max(nums[start], nums[start + 1]);
        
        for(int i = 2; i <= end - start; i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[start + i]);
        }
        
        return dp[end - start];
    }
};
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

**When to Use:** When you need to trace back the optimal path

## Comparison with House Robber (LC 198)

| Aspect | House Robber (LC 198) | House Robber II (LC 213) |
|--------|----------------------|--------------------------|
| **Structure** | Linear array | Circular array |
| **Constraint** | Adjacent houses | Adjacent + first/last adjacent |
| **Solution** | Single DP pass | Two DP passes, take max |
| **Complexity** | O(n) time, O(1) space | O(n) time, O(1) space |
| **Edge Case** | Empty array | Single house |

## Related Problems

- [LC 198: House Robber](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-198-house-robber/) - Linear version
- [LC 337: House Robber III](https://leetcode.com/problems/house-robber-iii/) - Binary tree structure
- [LC 740: Delete and Earn](https://leetcode.com/problems/delete-and-earn/) - Similar DP pattern
- [LC 256: Paint House](https://leetcode.com/problems/paint-house/) - Similar constraint pattern

---

*This problem extends House Robber to a circular arrangement. The key insight is breaking the circular constraint into two linear subproblems and taking the maximum, effectively reducing a circular problem to two linear problems.*
