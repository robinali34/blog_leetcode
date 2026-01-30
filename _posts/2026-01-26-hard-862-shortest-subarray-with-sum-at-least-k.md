---
layout: post
title: "862. Shortest Subarray with Sum at Least K"
date: 2026-01-26 00:00:00 -0700
categories: [leetcode, hard, array, sliding-window, deque, prefix-sum, monotonic-deque]
permalink: /2026/01/26/hard-862-shortest-subarray-with-sum-at-least-k/
tags: [leetcode, hard, array, sliding-window, deque, prefix-sum, monotonic-deque]
---

# 862. Shortest Subarray with Sum at Least K

## Problem Statement

Given an integer array `nums` and an integer `k`, return *the **length** of the shortest non-empty **subarray** of* `nums` *with a sum of at least* `k`. If there is no such subarray, return `-1`.

A **subarray** is a contiguous part of an array.

## Examples

**Example 1:**

```
Input: nums = [1], k = 1
Output: 1
```

**Example 2:**

```
Input: nums = [1,2], k = 4
Output: -1
```

**Example 3:**

```
Input: nums = [2,-1,2], k = 3
Output: 3
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Subarray definition**: What is a subarray? (Assumption: Contiguous elements - must be consecutive elements)

2. **Sum requirement**: What does "sum at least k" mean? (Assumption: Sum of subarray elements >= k - greater than or equal to k)

3. **Optimization goal**: What are we optimizing for? (Assumption: Shortest subarray length with sum >= k)

4. **Return value**: What should we return? (Assumption: Integer - length of shortest subarray, or -1 if no such subarray exists)

5. **Negative numbers**: Can array contain negative numbers? (Assumption: Yes - per constraints, nums[i] can be negative)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

Try all possible subarrays by checking all pairs of start and end indices. For each subarray, calculate its sum and track the shortest one with sum >= k. This approach has O(n²) time complexity for checking all subarrays and O(n) for calculating each sum, giving O(n³) overall. For arrays up to 50,000 elements, this is too slow.

**Step 2: Semi-Optimized Approach (10 minutes)**

Use prefix sums to calculate subarray sums in O(1) time. Precompute prefix[i] = sum of nums[0...i-1]. Then subarray sum from i to j is prefix[j+1] - prefix[i]. For each starting index i, find the smallest ending index j such that prefix[j+1] - prefix[i] >= k. This reduces to O(n²) time complexity, which is still too slow for large inputs. The challenge is that negative numbers prevent using simple two-pointer or sliding window techniques.

**Step 3: Optimized Solution (12 minutes)**

Use a monotonic deque with prefix sums. Maintain a deque of prefix sum indices in increasing order of prefix sum values. For each prefix sum, remove indices from the front whose prefix sums are too small (can't form valid subarrays), and remove indices from the back whose prefix sums are larger (they're worse candidates since we want the shortest subarray). The key insight is that if prefix[i] <= prefix[j] and i < j, then i is always a better starting point than j. This achieves O(n) time complexity because each index is added and removed at most once. The monotonic deque maintains candidates efficiently, handling negative numbers correctly.

## Solution Approach

This problem is similar to [LC 209: Minimum Size Subarray Sum](https://robinali34.github.io/blog_leetcode/2026/01/26/medium-209-minimum-size-subarray-sum/), but with a critical difference: **the array can contain negative numbers**.

The key challenge is that with negative numbers, a simple sliding window approach fails because:
- Removing elements from the left might not decrease the sum (negative numbers can increase sum)
- We cannot use binary search on prefix sums (they're not monotonic)

### Key Insights:

1. **Prefix Sum**: Enables O(1) range sum queries
2. **Monotonic Deque**: Maintains indices with increasing prefix sums
3. **Why Deque?**: We need to remove from both ends efficiently
4. **Why Monotonic?**: If `preSum[i] <= preSum[j]` and `i < j`, then `i` is always better than `j` as a starting point

## Solution: Monotonic Deque with Prefix Sum

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        if(nums.empty()) return -1;
        const int N = nums.size();
        vector<long> preSum(N + 1);
        for(int i = 0; i < N; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        int rtn = INT_MAX;
        deque<int> q;
        for(int i = 0; i <= N; i++) {
            long curSum = preSum[i];
            while(!q.empty() && curSum - preSum[q.front()] >= k) {
                rtn = min(rtn, i - q.front());
                q.pop_front();
            }
            while(!q.empty() && preSum[q.back()] >= curSum) {
                q.pop_back();
            }
            q.push_back(i);
        }
        return rtn == INT_MAX? -1: rtn;
    }
};
```

### Algorithm Explanation:

#### **Step 1: Build Prefix Sum Array**

```cpp
vector<long> preSum(N + 1);
for(int i = 0; i < N; i++) {
    preSum[i + 1] = preSum[i] + nums[i];
}
```

- `preSum[i]` = sum of elements from index `0` to `i-1`
- `preSum[0] = 0` (empty prefix)
- `preSum[1] = nums[0]`
- `preSum[2] = nums[0] + nums[1]`
- ...

**Note:** Using `long` to prevent integer overflow.

#### **Step 2: Maintain Monotonic Deque**

```cpp
deque<int> q;  // Stores indices of prefix sums
for(int i = 0; i <= N; i++) {
    long curSum = preSum[i];
    
    // Check if we can form a valid subarray ending at i
    while(!q.empty() && curSum - preSum[q.front()] >= k) {
        rtn = min(rtn, i - q.front());
        q.pop_front();
    }
    
    // Maintain monotonic property: remove larger prefix sums
    while(!q.empty() && preSum[q.back()] >= curSum) {
        q.pop_back();
    }
    
    q.push_back(i);
}
```

**Key Operations:**

1. **Check Valid Subarray**: `curSum - preSum[q.front()] >= k`
   - If true, we found a valid subarray from `q.front()` to `i-1`
   - Update minimum length and remove `q.front()` (it's been processed)

2. **Maintain Monotonic Property**: `preSum[q.back()] >= curSum`
   - If `preSum[j] >= preSum[i]` and `j < i`, then `j` is always worse than `i`
   - Why? For any future `k`, if `preSum[k] - preSum[j] >= k`, then `preSum[k] - preSum[i] >= k` too
   - And `k - i < k - j`, so `i` gives shorter subarray
   - Remove `q.back()` to maintain increasing prefix sums

3. **Add Current Index**: Always add `i` to deque

### Example Walkthrough:

**Input:** `nums = [2,-1,2]`, `k = 3`

```
Step 1: Build prefix sums
  preSum = [0, 2, 1, 3]

Step 2: Process with deque
  i=0: curSum=0
    q=[], add 0 → q=[0]
    
  i=1: curSum=2
    Check: 2 - preSum[0] = 2 - 0 = 2 < 3 → no valid subarray
    Monotonic: preSum[0]=0 < 2 → keep
    q=[0], add 1 → q=[0,1]
    
  i=2: curSum=1
    Check: 1 - preSum[0] = 1 - 0 = 1 < 3 → no valid subarray
    Monotonic: preSum[1]=2 >= 1 → remove 1
    q=[0], add 2 → q=[0,2]
    
  i=3: curSum=3
    Check: 3 - preSum[0] = 3 - 0 = 3 >= 3 ✓
      rtn = min(INT_MAX, 3-0) = 3
      q.pop_front() → q=[2]
    Check: 3 - preSum[2] = 3 - 1 = 2 < 3 → stop
    Monotonic: preSum[2]=1 < 3 → keep
    q=[2], add 3 → q=[2,3]

Result: return 3 ✓
```

**Why remove larger prefix sums?**

Consider `preSum = [0, 5, 3, 4]`:
- At index 2, `preSum[2] = 3 < preSum[1] = 5`
- For any future index `i`, if `preSum[i] - preSum[1] >= k`, then `preSum[i] - preSum[2] >= k` too
- And `i - 2 < i - 1`, so index 2 is always better than index 1
- We can safely remove index 1

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Each element added once to deque
  - Each element removed at most once from deque
  - Overall: O(n)

- **Space Complexity:** O(n)
  - Prefix sum array: O(n)
  - Deque: O(n) in worst case
  - Overall: O(n)

## Key Insights

1. **Negative Numbers Break Simple Sliding Window**: Cannot shrink window from left when sum >= k

2. **Prefix Sum Enables Range Queries**: `preSum[j+1] - preSum[i]` = sum from `i` to `j`

3. **Monotonic Deque**: Maintains indices with increasing prefix sums
   - If `preSum[i] <= preSum[j]` and `i < j`, then `i` is always better

4. **Why Deque?**: Need O(1) operations on both ends
   - Remove from front: processed starting positions
   - Remove from back: maintain monotonic property

5. **Two While Loops**:
   - First loop: find valid subarrays ending at current position
   - Second loop: maintain monotonic property for future positions

## Edge Cases

1. **Empty array**: `nums = []` → return `-1`
2. **No valid subarray**: `nums = [1,2]`, `k = 4` → return `-1`
3. **Single element**: `nums = [1]`, `k = 1` → return `1`
4. **Negative numbers**: `nums = [2,-1,2]`, `k = 3` → return `3`
5. **All negative**: `nums = [-1,-2,-3]`, `k = 1` → return `-1`
6. **Large k**: `nums = [1,2]`, `k = 10^9` → return `-1`

## Common Mistakes

1. **Using simple sliding window**: Fails with negative numbers
2. **Not maintaining monotonic property**: Leads to incorrect results
3. **Wrong deque operations**: Removing from wrong end
4. **Integer overflow**: Not using `long` for prefix sums
5. **Index confusion**: Mixing 0-indexed and 1-indexed arrays
6. **Not checking empty deque**: Accessing `q.front()` or `q.back()` without checking

## Comparison with LC 209

| Aspect | LC 209 (All Positive) | LC 862 (Can Have Negatives) |
|--------|----------------------|----------------------------|
| **Approach** | Simple sliding window | Monotonic deque |
| **Time** | O(n) | O(n) |
| **Space** | O(1) | O(n) |
| **Complexity** | Simpler | More complex |
| **Key Insight** | Shrink window when sum >= k | Maintain monotonic deque |

## Related Problems

- [LC 209: Minimum Size Subarray Sum](https://robinali34.github.io/blog_leetcode/2026/01/26/medium-209-minimum-size-subarray-sum/) - Similar but all positive numbers
- [LC 3: Longest Substring Without Repeating Characters](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) - Sliding window pattern
- [LC 76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Similar sliding window
- [LC 53: Maximum Subarray](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-53-maximum-subarray/) - Maximum sum subarray
- [LC 239: Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Monotonic deque pattern

---

*This problem demonstrates the **monotonic deque** technique, which is essential when dealing with subarray problems involving negative numbers. The key insight is maintaining a deque with increasing prefix sums to efficiently find the shortest valid subarray.*
