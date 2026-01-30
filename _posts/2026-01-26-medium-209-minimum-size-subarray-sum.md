---
layout: post
title: "209. Minimum Size Subarray Sum"
date: 2026-01-26 00:00:00 -0700
categories: [leetcode, medium, array, sliding-window, binary-search, prefix-sum]
permalink: /2026/01/26/medium-209-minimum-size-subarray-sum/
tags: [leetcode, medium, array, sliding-window, binary-search, prefix-sum, two-pointers]
---

# 209. Minimum Size Subarray Sum

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a **subarray** whose sum is greater than or equal to* `target`. If there is no such subarray, return `0`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

**Example 3:**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Array values**: Are all numbers positive, or can they be negative/zero? (Assumption: All numbers are positive - this enables sliding window approach)

2. **No valid subarray**: What should we return if no subarray has sum >= target? (Assumption: Return `0`)

3. **Subarray definition**: Does a subarray need to be contiguous? (Assumption: Yes - subarray is contiguous by definition)

4. **Single element**: Can a single element form a valid subarray? (Assumption: Yes - if `nums[i] >= target`, length is 1)

5. **Target value**: Can target be larger than the sum of all elements? (Assumption: Yes - in this case return `0`)

## Solution Approach

This problem requires finding the minimum length subarray with sum >= target. Two main approaches:

1. **Prefix Sum + Binary Search**: Build prefix sums, then for each starting position, binary search for the minimum ending position
2. **Sliding Window**: Use two pointers to maintain a window with sum >= target, shrink from left when possible

### Key Insights:

1. **Prefix Sum**: Enables O(1) range sum queries
2. **Binary Search**: Finds minimum ending position in O(log n) time
3. **Sliding Window**: More intuitive, O(n) time with O(1) space
4. **Monotonic Property**: Prefix sums are non-decreasing (all positive numbers)

## Solution 1: Prefix Sum + Binary Search

```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if(nums.empty()) return 0;
        const int N = nums.size();
        int rtn = INT_MAX;
        vector<int> sums(N + 1, 0);
        for(int i = 1; i <= N; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }
        for(int i = 1; i <= N; i++) {
            int currTarget = target + sums[i - 1];
            auto it = lower_bound(sums.begin(), sums.end(), currTarget);
            if(it != sums.end()) {
                rtn = min(rtn, (int)(it - sums.begin()) - (i - 1));
            }
        }
        return rtn == INT_MAX? 0 : rtn;
    }
};
```

### Algorithm Explanation:

#### **Step 1: Build Prefix Sum Array**

```cpp
vector<int> sums(N + 1, 0);
for(int i = 1; i <= N; i++) {
    sums[i] = sums[i - 1] + nums[i - 1];
}
```

- `sums[i]` = sum of elements from index `0` to `i-1`
- `sums[0] = 0` (empty prefix)
- `sums[1] = nums[0]`
- `sums[2] = nums[0] + nums[1]`
- ...

#### **Step 2: For Each Starting Position, Binary Search**

```cpp
for(int i = 1; i <= N; i++) {
    int currTarget = target + sums[i - 1];
    auto it = lower_bound(sums.begin(), sums.end(), currTarget);
    if(it != sums.end()) {
        rtn = min(rtn, (int)(it - sums.begin()) - (i - 1));
    }
}
```

- **Starting at index `i-1`**: We want sum from `i-1` to some `j` >= target
- **Range sum**: `sums[j+1] - sums[i-1] >= target`
- **Rearranging**: `sums[j+1] >= target + sums[i-1]`
- **Binary search**: Find first `sums[k] >= target + sums[i-1]`
- **Length**: `k - (i-1)` = `(it - sums.begin()) - (i - 1)`

### Example Walkthrough:

**Input:** `target = 7`, `nums = [2,3,1,2,4,3]`

```
Step 1: Build prefix sums
  sums = [0, 2, 5, 6, 8, 12, 15]

Step 2: For each starting position
  i=1 (start at index 0):
    currTarget = 7 + sums[0] = 7 + 0 = 7
    lower_bound finds sums[4] = 8 >= 7
    length = 4 - 0 = 4
    
  i=2 (start at index 1):
    currTarget = 7 + sums[1] = 7 + 2 = 9
    lower_bound finds sums[5] = 12 >= 9
    length = 5 - 1 = 4
    
  i=3 (start at index 2):
    currTarget = 7 + sums[2] = 7 + 5 = 12
    lower_bound finds sums[5] = 12 >= 12
    length = 5 - 2 = 3
    
  i=4 (start at index 3):
    currTarget = 7 + sums[3] = 7 + 6 = 13
    lower_bound finds sums[5] = 12 >= 13? No, try next
    lower_bound finds sums[6] = 15 >= 13
    length = 6 - 3 = 3
    
  i=5 (start at index 4):
    currTarget = 7 + sums[4] = 7 + 8 = 15
    lower_bound finds sums[6] = 15 >= 15
    length = 6 - 4 = 2 ✓ (minimum)
    
  i=6 (start at index 5):
    currTarget = 7 + sums[5] = 7 + 12 = 19
    lower_bound finds sums[7] (end) → not found

Result: min(4, 4, 3, 3, 2) = 2 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n log n)
  - Building prefix sums: O(n)
  - For each starting position: O(log n) binary search
  - Overall: O(n log n)

- **Space Complexity:** O(n)
  - Prefix sum array: O(n)
  - Overall: O(n)

## Solution 2: Sliding Window

```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if(nums.empty()) return 0;
        const int N = nums.size();
        int rtn = INT_MAX;
        int start = 0, end = 0, sum = 0;
        while(end < N) {
            sum += nums[end];
            while(sum >= target) {
                rtn = min(rtn, end - start + 1);
                sum -= nums[start];
                start++;
            }
            end++;
        }
        return rtn == INT_MAX ? 0: rtn;
    }
};
```

### Algorithm Explanation:

#### **Two Pointers Technique:**

1. **`start`**: Left boundary of window (inclusive)
2. **`end`**: Right boundary of window (inclusive)
3. **`sum`**: Current sum of window `[start, end]`

#### **Algorithm Steps:**

1. **Expand Window**: Move `end` right, add `nums[end]` to `sum`
2. **Shrink Window**: While `sum >= target`:
   - Update minimum length: `rtn = min(rtn, end - start + 1)`
   - Remove `nums[start]` from `sum`
   - Move `start` right
3. **Continue**: Move `end` right and repeat

### Example Walkthrough:

**Input:** `target = 7`, `nums = [2,3,1,2,4,3]`

```
Initial: start=0, end=0, sum=0, rtn=INT_MAX

end=0: sum=2, 2<7 → continue
  window=[2], sum=2

end=1: sum=5, 5<7 → continue
  window=[2,3], sum=5

end=2: sum=6, 6<7 → continue
  window=[2,3,1], sum=6

end=3: sum=8, 8>=7 → shrink
  rtn=min(INT_MAX, 4-0+1)=4
  start=1, sum=6
  window=[3,1,2], sum=6<7 → stop shrinking

end=4: sum=10, 10>=7 → shrink
  rtn=min(4, 4-1+1)=4
  start=2, sum=7
  rtn=min(4, 4-2+1)=3
  start=3, sum=6
  window=[2,4], sum=6<7 → stop

end=5: sum=9, 9>=7 → shrink
  rtn=min(3, 5-3+1)=3
  start=4, sum=7
  rtn=min(3, 5-4+1)=2 ✓
  start=5, sum=3
  window=[3], sum=3<7 → stop

Result: return 2 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Each element added once (end pointer)
  - Each element removed at most once (start pointer)
  - Overall: O(n)

- **Space Complexity:** O(1)
  - Only three variables: `start`, `end`, `sum`
  - Overall: O(1)

## Key Insights

1. **Prefix Sum + Binary Search**:
   - Good when you need to query multiple ranges
   - O(n log n) time, O(n) space
   - More complex but flexible

2. **Sliding Window**:
   - More intuitive and efficient
   - O(n) time, O(1) space
   - Preferred for single query problems

3. **Monotonic Property**: Prefix sums are non-decreasing (all positive), enabling binary search

4. **Window Shrinking**: Once sum >= target, shrink from left to find minimum length

## Edge Cases

1. **Empty array**: `nums = []` → return `0`
2. **No valid subarray**: `nums = [1,1,1]`, `target = 10` → return `0`
3. **Single element**: `nums = [5]`, `target = 5` → return `1`
4. **Entire array needed**: `nums = [1,2,3]`, `target = 6` → return `3`
5. **First element**: `nums = [10,1,1]`, `target = 10` → return `1`

## Common Mistakes

1. **Wrong binary search target**: Forgetting to add `sums[i-1]` to target
2. **Index calculation**: Wrong length calculation `(it - sums.begin()) - (i - 1)`
3. **Not checking bounds**: Not checking if `it != sums.end()`
4. **Sliding window**: Not shrinking window when sum >= target
5. **Return value**: Returning `INT_MAX` instead of `0` when no solution

## Comparison of Approaches

| Aspect | Prefix Sum + Binary Search | Sliding Window |
|--------|---------------------------|----------------|
| **Time** | O(n log n) | O(n) |
| **Space** | O(n) | O(1) |
| **Code Complexity** | More complex | Simpler |
| **Intuition** | Less intuitive | More intuitive |
| **Best For** | Multiple queries | Single query |

## Related Problems

- [LC 3: Longest Substring Without Repeating Characters](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) - Sliding window pattern
- [LC 76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Similar sliding window
- [LC 209: Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) - This problem
- [LC 862: Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) - Similar with negative numbers
- [LC 53: Maximum Subarray](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-53-maximum-subarray/) - Maximum sum subarray

---

*This problem demonstrates two powerful techniques: **prefix sum with binary search** for range queries and **sliding window** for efficient subarray processing. The sliding window approach is generally preferred for its simplicity and optimal O(n) time complexity.*
