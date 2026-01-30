---
layout: post
title: "53. Maximum Subarray"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming, greedy, divide-and-conquer]
permalink: /2026/01/04/medium-53-maximum-subarray/
---

# 53. Maximum Subarray

## Problem Statement

Given an integer array `nums`, find the **subarray** with the largest sum, and return *its sum*.

A **subarray** is a contiguous non-empty sequence of elements within an array.

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Subarray definition**: Does a subarray need to be contiguous? (Assumption: Yes - subarray is contiguous by definition)

2. **Empty subarray**: Can an empty subarray be considered? (Assumption: No - subarray must be non-empty, at least one element)

3. **Negative values**: Can the array contain negative numbers? (Assumption: Yes - per constraints, values can be negative)

4. **Return value**: Should we return the sum or the subarray itself? (Assumption: Return the maximum sum - integer value)

5. **All negative**: What if all numbers are negative? (Assumption: Return the least negative number - the maximum element)

## Solution Approach

This is a classic **Kadane's Algorithm** problem, which can be solved using either **greedy** or **dynamic programming** approach. The key insight is to decide at each position whether to extend the previous subarray or start a new one.

### Key Insights:

1. **Local vs Global Maximum**: At each position, decide whether to extend the previous subarray or start fresh
2. **Greedy Choice**: If the current element alone is better than extending the previous subarray, start a new subarray
3. **Optimal Substructure**: The maximum subarray ending at position `i` depends on the maximum subarray ending at position `i-1`
4. **Single Pass**: Can solve in O(n) time with O(1) space

### Algorithm:

1. **Initialize**: `maxSum = nums[0]`, `currSum = nums[0]`
2. **For each element**: 
   - Update `currSum = max(nums[i], currSum + nums[i])`
   - Update `maxSum = max(maxSum, currSum)`
3. **Return**: `maxSum`

## Solution

### **Solution: Kadane's Algorithm (Greedy/DP)**

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0], currSum = nums[0];
        for(int i = 1; i < (int)nums.size(); i++) {
            currSum = max(nums[i], currSum + nums[i]);
            maxSum = max(maxSum, currSum);
        }
        return maxSum;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Line 4)**:
   - `maxSum`: Maximum subarray sum found so far (starts with first element)
   - `currSum`: Maximum subarray sum ending at current position (starts with first element)

2. **Process Each Element (Lines 5-7)**:
   - **For each element** from index 1 to end:
     - **Update `currSum`**: `currSum = max(nums[i], currSum + nums[i])`
       - **Option 1**: Start fresh with `nums[i]` alone
       - **Option 2**: Extend previous subarray by adding `nums[i]`
       - **Choose the maximum**: This is the greedy choice
     - **Update `maxSum`**: `maxSum = max(maxSum, currSum)`
       - Track the global maximum across all positions

3. **Return (Line 8)**:
   - Return the maximum subarray sum

### **Why This Works:**

**Key Insight**: At each position, we decide whether to extend the previous subarray or start a new one.

**Greedy Choice**: 
- If `currSum + nums[i] < nums[i]`, then `currSum` is negative
- Starting fresh with `nums[i]` is better than extending a negative sum
- This locally optimal choice leads to a globally optimal solution

**Optimal Substructure**:
- `currSum[i]` = maximum subarray sum ending at position `i`
- `currSum[i] = max(nums[i], currSum[i-1] + nums[i])`
- `maxSum = max(currSum[0], currSum[1], ..., currSum[n-1])`

**Example Walkthrough:**

**Example 1: `nums = [-2,1,-3,4,-1,2,1,-5,4]`**

**Execution:**
```
Initial: maxSum = -2, currSum = -2

i=1: nums[1] = 1
  currSum = max(1, -2 + 1) = max(1, -1) = 1
  maxSum = max(-2, 1) = 1
  State: maxSum=1, currSum=1

i=2: nums[2] = -3
  currSum = max(-3, 1 + (-3)) = max(-3, -2) = -2
  maxSum = max(1, -2) = 1
  State: maxSum=1, currSum=-2

i=3: nums[3] = 4
  currSum = max(4, -2 + 4) = max(4, 2) = 4
  maxSum = max(1, 4) = 4
  State: maxSum=4, currSum=4

i=4: nums[4] = -1
  currSum = max(-1, 4 + (-1)) = max(-1, 3) = 3
  maxSum = max(4, 3) = 4
  State: maxSum=4, currSum=3

i=5: nums[5] = 2
  currSum = max(2, 3 + 2) = max(2, 5) = 5
  maxSum = max(4, 5) = 5
  State: maxSum=5, currSum=5

i=6: nums[6] = 1
  currSum = max(1, 5 + 1) = max(1, 6) = 6
  maxSum = max(5, 6) = 6
  State: maxSum=6, currSum=6

i=7: nums[7] = -5
  currSum = max(-5, 6 + (-5)) = max(-5, 1) = 1
  maxSum = max(6, 1) = 6
  State: maxSum=6, currSum=1

i=8: nums[8] = 4
  currSum = max(4, 1 + 4) = max(4, 5) = 5
  maxSum = max(6, 5) = 6
  State: maxSum=6, currSum=5

Result: 6
Subarray: [4, -1, 2, 1] (indices 3-6)
```

**Example 2: `nums = [1]`**

**Execution:**
```
Initial: maxSum = 1, currSum = 1
No iterations (array size 1)

Result: 1
Subarray: [1]
```

**Example 3: `nums = [5,4,-1,7,8]`**

**Execution:**
```
Initial: maxSum = 5, currSum = 5

i=1: nums[1] = 4
  currSum = max(4, 5 + 4) = 9
  maxSum = max(5, 9) = 9

i=2: nums[2] = -1
  currSum = max(-1, 9 + (-1)) = 8
  maxSum = max(9, 8) = 9

i=3: nums[3] = 7
  currSum = max(7, 8 + 7) = 15
  maxSum = max(9, 15) = 15

i=4: nums[4] = 8
  currSum = max(8, 15 + 8) = 23
  maxSum = max(15, 23) = 23

Result: 23
Subarray: [5, 4, -1, 7, 8] (entire array)
```

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

## Alternative Approaches

### **Approach 1: Kadane's Algorithm (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Optimal solution, most efficient

### **Approach 2: Dynamic Programming (Explicit DP Array)**
- **Time**: O(n)
- **Space**: O(n)
- **Idea**: Store `dp[i]` = maximum subarray sum ending at `i`
- **Code**:
```cpp
int maxSubArray(vector<int>& nums) {
    vector<int> dp(nums.size());
    dp[0] = nums[0];
    int maxSum = nums[0];
    for(int i = 1; i < nums.size(); i++) {
        dp[i] = max(nums[i], dp[i-1] + nums[i]);
        maxSum = max(maxSum, dp[i]);
    }
    return maxSum;
}
```

### **Approach 3: Divide and Conquer**
- **Time**: O(n log n)
- **Space**: O(log n) for recursion
- **Idea**: 
  - Divide array into two halves
  - Maximum subarray is either in left half, right half, or crosses the middle
  - Recurse and combine results
- **Overkill**: Not needed, Kadane's is simpler and faster

### **Approach 4: Brute Force**
- **Time**: O(n²)
- **Space**: O(1)
- **Idea**: Try all possible subarrays
- **Not practical**: Too slow for large inputs

## Edge Cases

1. **Single element**: `[5]` → return 5
2. **All negative**: `[-2,-1,-3]` → return -1 (least negative)
3. **All positive**: `[1,2,3,4]` → return 10 (sum of all)
4. **Mixed**: `[-2,1,-3,4,-1,2,1,-5,4]` → return 6
5. **One positive**: `[-1,-2,5,-3]` → return 5

## Common Mistakes

1. **Not initializing correctly**: Starting with 0 instead of `nums[0]`
2. **Wrong update**: Using `currSum += nums[i]` without checking if it's better to start fresh
3. **Not tracking global max**: Only returning `currSum` instead of `maxSum`
4. **Off-by-one errors**: Incorrect loop bounds
5. **Handling negatives**: Not understanding when to start fresh

## Related Problems

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Similar greedy approach
- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) - Similar but for product
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) - Find minimum subarray with sum >= target
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) - Find subarrays with sum k
- [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) - Extension to circular array

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

