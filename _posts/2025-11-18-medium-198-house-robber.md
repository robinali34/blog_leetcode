---
layout: post
title: "[Medium] 198. House Robber"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp dynamic-programming dp problem-solving
permalink: /posts/2025-11-18-medium-198-house-robber/
tags: [leetcode, medium, dynamic-programming, dp, array, optimization]
---

# [Medium] 198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Robbery rules**: What are the robbery rules? (Assumption: Cannot rob two adjacent houses - must skip at least one house between robberies)

2. **Optimization goal**: What are we optimizing for? (Assumption: Maximum money that can be robbed without alerting police)

3. **Return value**: What should we return? (Assumption: Integer - maximum money that can be robbed)

4. **House values**: What do nums[i] represent? (Assumption: Amount of money in house i - positive integers)

5. **Empty array**: What if array is empty? (Assumption: Return 0 - no houses to rob)

## Solution: Dynamic Programming

**Time Complexity:** O(n) - Single pass through the array  
**Space Complexity:** O(n) - DP array (can be optimized to O(1))

This is a classic dynamic programming problem. The key insight is that for each house, we have two choices:
1. **Rob it**: Add its value to the maximum from two houses ago
2. **Skip it**: Take the maximum from the previous house

### Solution: DP Array Approach

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() <= 0) return 0;
        if(nums.size() == 1) return nums[0];
        
        vector<int> dp(nums.size() + 1);
        dp[0] = 0;
        dp[1] = nums[0];
        
        for(int i = 1; i < (int)nums.size(); i++) {
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i]);
        } 
        
        return dp[nums.size()];
    }
};
```

## How the Algorithm Works

### Step-by-Step Example: `nums = [2,7,9,3,1]`

```
Initial: dp[0] = 0, dp[1] = nums[0] = 2

i=1 (nums[1]=7):
  Option 1: Rob house 2 → dp[0] + nums[1] = 0 + 7 = 7
  Option 2: Skip house 2 → dp[1] = 2
  dp[2] = max(7, 2) = 7

i=2 (nums[2]=9):
  Option 1: Rob house 3 → dp[1] + nums[2] = 2 + 9 = 11
  Option 2: Skip house 3 → dp[2] = 7
  dp[3] = max(11, 7) = 11

i=3 (nums[3]=3):
  Option 1: Rob house 4 → dp[2] + nums[3] = 7 + 3 = 10
  Option 2: Skip house 4 → dp[3] = 11
  dp[4] = max(10, 11) = 11

i=4 (nums[4]=1):
  Option 1: Rob house 5 → dp[3] + nums[4] = 11 + 1 = 12
  Option 2: Skip house 5 → dp[4] = 11
  dp[5] = max(12, 11) = 12

Result: dp[5] = 12
```

### Visual Representation

```
Houses:    [2]  [7]  [9]  [3]  [1]
Indices:    0    1    2    3    4

DP State:
dp[0] = 0                    (no houses)
dp[1] = 2                    (rob house 0)
dp[2] = max(0+7, 2) = 7      (rob house 1, skip house 0)
dp[3] = max(2+9, 7) = 11     (rob house 2, skip house 1)
dp[4] = max(7+3, 11) = 11    (skip house 3, keep previous)
dp[5] = max(11+1, 11) = 12   (rob house 4)

Optimal path: Rob houses 0, 2, 4 → 2 + 9 + 1 = 12
```

## Key Insights

1. **DP State Definition**: `dp[i]` represents the maximum money robbed up to house `i-1` (1-indexed)
2. **Recurrence Relation**: `dp[i+1] = max(dp[i-1] + nums[i], dp[i])`
   - `dp[i-1] + nums[i]`: Rob current house (can't rob previous)
   - `dp[i]`: Skip current house (keep previous maximum)
3. **Base Cases**: 
   - `dp[0] = 0` (no houses)
   - `dp[1] = nums[0]` (only first house)
4. **1-Indexed DP Array**: Using `dp[i+1]` makes indexing cleaner and avoids edge cases

## Algorithm Breakdown

```cpp
int rob(vector<int>& nums) {
    // Edge cases
    if(nums.size() <= 0) return 0;
    if(nums.size() == 1) return nums[0];
    
    // DP array: dp[i] = max money up to house i-1
    vector<int> dp(nums.size() + 1);
    dp[0] = 0;        // No houses
    dp[1] = nums[0];  // Only first house
    
    // For each house starting from index 1
    for(int i = 1; i < (int)nums.size(); i++) {
        // Choose: rob current house OR skip it
        dp[i + 1] = max(
            dp[i - 1] + nums[i],  // Rob current (skip previous)
            dp[i]                  // Skip current (keep previous max)
        );
    }
    
    return dp[nums.size()];  // Maximum for all houses
}
```

## Edge Cases

1. **Empty array**: `nums = []` → return `0`
2. **Single house**: `nums = [5]` → return `5`
3. **Two houses**: `nums = [2,1]` → return `max(2,1) = 2`
4. **All zeros**: `nums = [0,0,0]` → return `0`
5. **Alternating pattern**: `nums = [1,2,1,2]` → return `max(1+1, 2+2) = 4`

## Alternative Approaches

### Approach 2: Space-Optimized O(1) Space

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Instead of storing the entire DP array, we only need the previous two values:

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.empty()) return 0;
        if(nums.size() == 1) return nums[0];
        
        int prev2 = 0;        // dp[i-2]
        int prev1 = nums[0];  // dp[i-1]
        
        for(int i = 1; i < (int)nums.size(); i++) {
            int current = max(prev2 + nums[i], prev1);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
};
```

**Pros:**
- O(1) space complexity
- Same time complexity
- More memory efficient

**Cons:**
- Slightly less intuitive
- Can't trace back the optimal path

### Approach 3: 0-Indexed DP Array

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Standard 0-indexed approach:

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.empty()) return 0;
        if(nums.size() == 1) return nums[0];
        
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        for(int i = 2; i < (int)nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        return dp[nums.size() - 1];
    }
};
```

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **DP Array (1-indexed)** | O(n) | O(n) | Clear indexing, easy to understand | O(n) space |
| **Space-Optimized** | O(n) | O(1) | Optimal space usage | Can't trace path |
| **DP Array (0-indexed)** | O(n) | O(n) | Standard DP pattern | Requires base case handling |

## Recurrence Relation Explanation

The core recurrence relation is:

```
dp[i+1] = max(dp[i-1] + nums[i], dp[i])
```

**Why this works:**
- **`dp[i-1] + nums[i]`**: If we rob house `i`, we can't rob house `i-1`, so we take the maximum from `i-2` (stored in `dp[i-1]`) and add current house value
- **`dp[i]`**: If we skip house `i`, we keep the maximum from all previous houses up to `i-1`

This ensures we never rob two adjacent houses while maximizing the total amount.

## Implementation Details

### 1-Indexed vs 0-Indexed

**1-Indexed (Your Solution):**
```cpp
dp[0] = 0;           // No houses
dp[1] = nums[0];     // First house
dp[i+1] = max(...);  // Current house at index i
```

**0-Indexed (Standard):**
```cpp
dp[0] = nums[0];     // First house
dp[1] = max(nums[0], nums[1]);  // First two houses
dp[i] = max(...);    // Current house at index i
```

Both approaches are correct; 1-indexed makes base cases simpler.

### Type Casting

```cpp
for(int i = 1; i < (int)nums.size(); i++)
```

The `(int)` cast prevents comparison warnings between `int` and `size_t`. Alternatively:
```cpp
for(size_t i = 1; i < nums.size(); i++)
```

## Common Mistakes

1. **Forgetting edge cases**: Empty array or single element
2. **Wrong recurrence**: Using `dp[i-2]` instead of `dp[i-1]` for 1-indexed
3. **Index out of bounds**: Not handling base cases properly
4. **Wrong return value**: Returning `dp[nums.size()-1]` instead of `dp[nums.size()]` for 1-indexed
5. **Not considering skip option**: Only considering robbing current house

## Optimization Tips

1. **Space Optimization**: Use two variables instead of array for O(1) space
2. **Early Termination**: Can add checks for special cases
3. **Memoization**: For recursive approach, use memoization to avoid recomputation
4. **Bottom-Up DP**: Preferred over top-down for better cache performance

## Related Problems

- [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) - Houses arranged in a circle
- [337. House Robber III](https://leetcode.com/problems/house-robber-iii/) - Binary tree structure
- [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/) - Similar DP pattern
- [1980. Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/) - Different problem but similar constraint pattern

## Real-World Applications

1. **Resource Allocation**: Maximizing profit with constraints
2. **Scheduling**: Selecting non-overlapping intervals with maximum value
3. **Network Optimization**: Routing with constraints
4. **Game Theory**: Optimal strategy selection
5. **Financial Planning**: Investment decisions with restrictions

## Pattern Recognition

This problem follows the **"Pick or Skip"** DP pattern:

```
For each element:
  Option 1: Pick it (with constraints)
  Option 2: Skip it
  
Choose the option that maximizes/minimizes the objective
```

Similar problems:
- Maximum Subarray (Kadane's algorithm)
- Climbing Stairs
- Coin Change
- Knapsack problems

---

*This problem is a fundamental introduction to dynamic programming, teaching the "pick or skip" decision pattern that appears in many optimization problems.*

