---
layout: post
title: "[Medium] 300. Longest Increasing Subsequence"
date: 2025-10-17 15:18:26 -0700
categories: leetcode algorithm medium cpp dynamic-programming dp binary-search problem-solving
---

# [Medium] 300. Longest Increasing Subsequence

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A **subsequence** is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Examples

**Example 1:**
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,18], therefore the length is 4.
```

**Example 2:**
```
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.
```

**Example 3:**
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
```

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Solution 1: Dynamic Programming

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

Use dynamic programming to track the length of the longest increasing subsequence ending at each position.

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        dp[0] = 1;
        int rtn = 1;
        
        for(int i = 1; i < (int) nums.size(); i++) {
            int max_pre = 0;
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j]) {
                    max_pre = max(max_pre, dp[j]);
                }
            }
            dp[i] = max_pre + 1;
            rtn = max(rtn, dp[i]);
        }
        
        return rtn;
    }
};
```

## Solution 2: Binary Search with Patience Sorting

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

Use binary search to maintain a sorted array representing the smallest tail element of all increasing subsequences of different lengths.

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> sub;
        sub.push_back(nums[0]);

        for(int i = 1; i < nums.size(); i++) {
            int num = nums[i];
            if(num > sub.back()) {
                sub.push_back(num);
            } else {
                auto it = lower_bound(sub.begin(), sub.end(), num);
                *it = num;
            }
        }
        
        return sub.size();
    }
};
```

## How the Algorithms Work

### Solution 1: Dynamic Programming Approach

**Key Insight:** For each position `i`, find the longest increasing subsequence ending at `i` by checking all previous positions.

**Steps:**
1. **Initialize DP array** with `dp[0] = 1`
2. **For each position `i`**, check all previous positions `j`
3. **If `nums[i] > nums[j]`**, update `max_pre` with `dp[j]`
4. **Set `dp[i] = max_pre + 1`** and update global maximum

### Solution 2: Binary Search Approach

**Key Insight:** Maintain an array where `sub[i]` represents the smallest tail element of all increasing subsequences of length `i+1`.

**Steps:**
1. **Initialize** with first element
2. **For each element**, if it's larger than last element, append it
3. **Otherwise**, use binary search to find position and replace
4. **Return** the size of the maintained array

## Step-by-Step Examples

### Solution 1 Example: `nums = [10,9,2,5,3,7,101,18]`

| i | nums[i] | Check j | max_pre | dp[i] | rtn |
|---|---------|----------|---------|-------|-----|
| 0 | 10 | - | - | 1 | 1 |
| 1 | 9 | j=0: 9≤10 | 0 | 1 | 1 |
| 2 | 2 | j=0,1: 2≤10,9 | 0 | 1 | 1 |
| 3 | 5 | j=0,1,2: 5≤10, 5≤9, 5>2 | dp[2]=1 | 2 | 2 |
| 4 | 3 | j=0,1,2,3: 3≤10, 3≤9, 3>2, 3≤5 | dp[2]=1 | 2 | 2 |
| 5 | 7 | j=0,1,2,3,4: 7≤10, 7≤9, 7>2, 7>5, 7>3 | max(dp[2],dp[3],dp[4])=2 | 3 | 3 |
| 6 | 101 | j=0,1,2,3,4,5: 101>10, 101>9, 101>2, 101>5, 101>3, 101>7 | max(dp[0],dp[1],dp[2],dp[3],dp[4],dp[5])=3 | 4 | 4 |
| 7 | 18 | j=0,1,2,3,4,5,6: 18>10, 18>9, 18>2, 18>5, 18>3, 18>7, 18≤101 | max(dp[0],dp[1],dp[2],dp[3],dp[4],dp[5])=3 | 4 | 4 |

**Final result:** 4

### Solution 2 Example: `nums = [10,9,2,5,3,7,101,18]`

| i | nums[i] | sub | Action |
|---|---------|-----|--------|
| 0 | 10 | [10] | Initialize |
| 1 | 9 | [9] | Replace 10 with 9 |
| 2 | 2 | [2] | Replace 9 with 2 |
| 3 | 5 | [2,5] | Append 5 |
| 4 | 3 | [2,3] | Replace 5 with 3 |
| 5 | 7 | [2,3,7] | Append 7 |
| 6 | 101 | [2,3,7,101] | Append 101 |
| 7 | 18 | [2,3,7,18] | Replace 101 with 18 |

**Final result:** 4

## Algorithm Breakdown

### Solution 1: Dynamic Programming

```cpp
vector<int> dp(nums.size(), -1);
dp[0] = 1;
int rtn = 1;

for(int i = 1; i < (int) nums.size(); i++) {
    int max_pre = 0;
    for(int j = 0; j < i; j++) {
        if(nums[i] > nums[j]) {
            max_pre = max(max_pre, dp[j]);
        }
    }
    dp[i] = max_pre + 1;
    rtn = max(rtn, dp[i]);
}
```

**Process:**
1. **Initialize** DP array with first element
2. **For each position**, check all previous positions
3. **Find maximum** length of subsequence ending at previous positions
4. **Update** current position and global maximum

### Solution 2: Binary Search

```cpp
vector<int> sub;
sub.push_back(nums[0]);

for(int i = 1; i < nums.size(); i++) {
    int num = nums[i];
    if(num > sub.back()) {
        sub.push_back(num);
    } else {
        auto it = lower_bound(sub.begin(), sub.end(), num);
        *it = num;
    }
}
```

**Process:**
1. **Initialize** with first element
2. **If current element** is larger than last, append it
3. **Otherwise**, find position using binary search and replace
4. **Return** size of maintained array

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Dynamic Programming | O(n²) | O(n) |
| Binary Search | O(n log n) | O(n) |

## Edge Cases

1. **Single element:** `nums = [1]` → `1`
2. **All same elements:** `nums = [7,7,7,7]` → `1`
3. **Decreasing sequence:** `nums = [5,4,3,2,1]` → `1`
4. **Increasing sequence:** `nums = [1,2,3,4,5]` → `5`

## Key Insights

### Solution 1 (DP):
1. **Subproblem:** Length of LIS ending at each position
2. **Overlapping subproblems:** Previous positions contribute to current
3. **Optimal substructure:** Optimal solution contains optimal solutions to subproblems
4. **Bottom-up approach:** Build solution from smaller subproblems

### Solution 2 (Binary Search):
1. **Patience sorting:** Maintain smallest tail elements
2. **Binary search:** Efficiently find insertion position
3. **Greedy approach:** Always maintain smallest possible tail elements
4. **Length tracking:** Size of array equals LIS length

## Common Mistakes

1. **Wrong DP definition:** Not considering all previous positions
2. **Incorrect initialization:** Not setting `dp[0] = 1`
3. **Missing global maximum:** Not tracking maximum across all positions
4. **Binary search errors:** Wrong comparison in `lower_bound`

## Detailed Example Walkthrough

### Solution 1: `nums = [0,1,0,3,2,3]`

**DP Table:**
```
i | nums[i] | dp[i] | Explanation
0 | 0       | 1     | Base case
1 | 1       | 2     | Can extend from dp[0] (0 < 1)
2 | 0       | 1     | Cannot extend from any previous
3 | 3       | 3     | Can extend from dp[0] and dp[1] (0 < 3, 1 < 3)
4 | 2       | 3     | Can extend from dp[0] and dp[1] (0 < 2, 1 < 2)
5 | 3       | 4     | Can extend from dp[0], dp[1], dp[2], dp[4] (0 < 3, 1 < 3, 0 < 3, 2 < 3)
```

**Final result:** 4

### Solution 2: `nums = [0,1,0,3,2,3]`

**Sub Array Evolution:**
```
i=0: [0]
i=1: [0,1]
i=2: [0,1] (0 ≤ 0, no change)
i=3: [0,1,3]
i=4: [0,1,2] (replace 3 with 2)
i=5: [0,1,2,3]
```

**Final result:** 4

## Alternative Approaches

### Approach 1: Recursive with Memoization
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> memo(nums.size(), -1);
        int maxLen = 0;
        for(int i = 0; i < nums.size(); i++) {
            maxLen = max(maxLen, dfs(nums, i, memo));
        }
        return maxLen;
    }
    
private:
    int dfs(vector<int>& nums, int index, vector<int>& memo) {
        if(memo[index] != -1) return memo[index];
        
        int maxLen = 1;
        for(int i = index + 1; i < nums.size(); i++) {
            if(nums[i] > nums[index]) {
                maxLen = max(maxLen, 1 + dfs(nums, i, memo));
            }
        }
        
        memo[index] = maxLen;
        return maxLen;
    }
};
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

## Related Problems

- [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)
- [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)
- [646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)
- [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)

## Why These Solutions Work

### Solution 1 (DP):
1. **Correct recurrence:** `dp[i] = max(dp[j]) + 1` for all `j < i` where `nums[j] < nums[i]`
2. **Optimal substructure:** LIS ending at position `i` contains LIS ending at some `j < i`
3. **Complete search:** Checks all possible previous positions
4. **Efficient for small inputs:** O(n²) is acceptable for n ≤ 2500

### Solution 2 (Binary Search):
1. **Patience sorting:** Maintains smallest tail elements correctly
2. **Binary search optimization:** O(log n) per element instead of O(n)
3. **Greedy correctness:** Always maintains optimal tail elements
4. **Optimal complexity:** O(n log n) is optimal for this problem
