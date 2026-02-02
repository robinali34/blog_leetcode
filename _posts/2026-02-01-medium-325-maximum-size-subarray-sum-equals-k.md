---
layout: post
title: "325. Maximum Size Subarray Sum Equals k"
date: 2026-02-01 00:00:00 -0700
categories: [leetcode, medium, array, hash-table, prefix-sum]
permalink: /2026/02/01/medium-325-maximum-size-subarray-sum-equals-k/
tags: [leetcode, medium, array, hash-table, prefix-sum]
---

# 325. Maximum Size Subarray Sum Equals k

## Problem Statement

Given an integer array `nums` and an integer `k`, return the maximum length of a subarray that sums to `k`. If there is no such subarray, return `0`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

```
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
```

**Example 2:**

```
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
```

**Example 3:**

```
Input: nums = [2,0,0,3], k = 3
Output: 3
Explanation: The subarray [0, 0, 3] sums to 3 and is the longest.
```

## Constraints

- `1 <= nums.length <= 2 * 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `-10^9 <= k <= 10^9`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Subarray definition**: What constitutes a subarray? (Assumption: A contiguous non-empty sequence of elements - must be consecutive elements)

2. **Target sum**: Can the target sum `k` be negative? (Assumption: Yes - `k` can be any integer, including negative values)

3. **Empty subarray**: Should we consider empty subarrays? (Assumption: No - subarray must be non-empty, so length is at least 1)

4. **Multiple solutions**: If multiple subarrays sum to `k`, what should we return? (Assumption: Return the maximum length among all such subarrays)

5. **No solution**: What should we return if no subarray sums to `k`? (Assumption: Return `0` - no valid subarray found)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For each starting position `i`, iterate through all ending positions `j >= i`, calculate the sum of subarray `nums[i..j]`, and check if it equals `k`. Keep track of the maximum length. This approach has O(n²) time complexity and O(1) space complexity.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use prefix sums to avoid recalculating subarray sums. For each position, we can compute the sum from index 0 to current position. However, we still need to check all pairs of positions, which is still O(n²) time.

**Step 3: Optimized Solution (8 minutes)**

Use prefix sum with hash map. The key insight is: if `prefixSum[i] - prefixSum[j] = k`, then `nums[j+1..i]` sums to `k`. We can use a hash map to store the first occurrence of each prefix sum. For each position, check if `prefixSum - k` exists in the map. This achieves O(n) time and O(n) space complexity.

## Solution Approach

This problem is a classic application of the prefix sum technique combined with hash map lookup. The key insight is that if we have prefix sums, we can find subarrays with a target sum efficiently.

### Key Insights:

1. **Prefix Sum Property**: `sum(nums[i..j]) = prefixSum[j] - prefixSum[i-1]`
2. **Hash Map Lookup**: Store the first occurrence of each prefix sum to maximize subarray length
3. **Early Update**: Only store the first occurrence of each prefix sum to ensure maximum length

## Solution 1: Brute-Force Approach

```cpp
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        int max_len = 0;
        for(int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for(int j = i; j < nums.size(); j++) {
                sum += nums[j];
                if(sum == k) {
                    max_len = max(max_len, j - i + 1);
                }
            }
        }
        return max_len;
    }
};
```

### Algorithm Breakdown:

1. **Outer Loop**: Iterate through all possible starting positions `i`
2. **Inner Loop**: For each starting position, iterate through all ending positions `j >= i`
3. **Sum Calculation**: Accumulate sum from `i` to `j`
4. **Check and Update**: If sum equals `k`, update maximum length

### Why This Works:

- **Exhaustive Search**: Checks all possible subarrays
- **Correctness**: Guaranteed to find the maximum length subarray
- **Simple Logic**: Straightforward implementation

### Complexity Analysis:

- **Time Complexity**: O(n²) - Two nested loops, each checking O(n) positions
- **Space Complexity**: O(1) - Only using a constant amount of extra space

## Solution 2: Prefix Sum with Hash Map

```cpp
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        long long prefixSum = 0;
        int maxLen = 0;
        const int N = nums.size();
        unordered_map<long long, int> cache;

        for(int i = 0; i < N; i++) {
            prefixSum += nums[i];
            if(prefixSum == k) {
                maxLen = i + 1;
            }
            if(cache.contains(prefixSum - k)) {
                maxLen = max(maxLen, i - cache[prefixSum - k]);
            }
            if(!cache.contains(prefixSum)) {
                cache[prefixSum] = i;
            }
        }
        return maxLen;
    }
};
```

### Algorithm Breakdown:

1. **Prefix Sum Tracking**: Maintain running sum `prefixSum` as we iterate
2. **Direct Match**: If `prefixSum == k`, subarray from index 0 to `i` sums to `k`
3. **Hash Map Lookup**: If `prefixSum - k` exists in map, subarray from `cache[prefixSum - k] + 1` to `i` sums to `k`
4. **First Occurrence**: Only store the first occurrence of each prefix sum to maximize length

### Why This Works:

- **Prefix Sum Property**: `sum(nums[j+1..i]) = prefixSum[i] - prefixSum[j] = k`
- **Rearranging**: `prefixSum[j] = prefixSum[i] - k`
- **First Occurrence**: Storing first occurrence ensures maximum subarray length
- **Long Type**: Using `long long` to prevent integer overflow

### Sample Test Case Run:

**Input:** `nums = [1,-1,5,-2,3]`, `k = 3`

```
Initial: prefixSum = 0, maxLen = 0, cache = {}

Iteration 0 (i=0, nums[0]=1):
  prefixSum = 0 + 1 = 1
  prefixSum (1) != k (3) ✗
  cache.contains(1 - 3 = -2)? No ✗
  cache[1] = 0 (first occurrence)
  State: prefixSum=1, maxLen=0, cache={1:0}

Iteration 1 (i=1, nums[1]=-1):
  prefixSum = 1 + (-1) = 0
  prefixSum (0) != k (3) ✗
  cache.contains(0 - 3 = -3)? No ✗
  cache[0] = 1 (first occurrence)
  State: prefixSum=0, maxLen=0, cache={1:0, 0:1}

Iteration 2 (i=2, nums[2]=5):
  prefixSum = 0 + 5 = 5
  prefixSum (5) != k (3) ✗
  cache.contains(5 - 3 = 2)? No ✗
  cache[5] = 2 (first occurrence)
  State: prefixSum=5, maxLen=0, cache={1:0, 0:1, 5:2}

Iteration 3 (i=3, nums[3]=-2):
  prefixSum = 5 + (-2) = 3
  prefixSum (3) == k (3) ✓
  maxLen = max(0, 3 + 1) = 4
  cache.contains(3 - 3 = 0)? Yes ✓ (cache[0]=1)
  maxLen = max(4, 3 - 1) = max(4, 2) = 4
  cache.contains(3)? No, cache[3] = 3
  State: prefixSum=3, maxLen=4, cache={1:0, 0:1, 5:2, 3:3}

Iteration 4 (i=4, nums[4]=3):
  prefixSum = 3 + 3 = 6
  prefixSum (6) != k (3) ✗
  cache.contains(6 - 3 = 3)? Yes ✓ (cache[3]=3)
  maxLen = max(4, 4 - 3) = max(4, 1) = 4
  cache.contains(6)? No, cache[6] = 4
  State: prefixSum=6, maxLen=4, cache={1:0, 0:1, 5:2, 3:3, 6:4}

Return: maxLen = 4 ✓
```

**Verification:**
- Subarray `[1, -1, 5, -2]` (indices 0-3): sum = 1 + (-1) + 5 + (-2) = 3 ✓
- Length = 4 ✓
- This is the maximum length subarray summing to 3 ✓

**Output:** `4` ✓

---

**Another Example:** `nums = [-2,-1,2,1]`, `k = 1`

```
Initial: prefixSum = 0, maxLen = 0, cache = {}

Iteration 0 (i=0, nums[0]=-2):
  prefixSum = 0 + (-2) = -2
  prefixSum != k ✗
  cache.contains(-2 - 1 = -3)? No ✗
  cache[-2] = 0
  State: prefixSum=-2, maxLen=0, cache={-2:0}

Iteration 1 (i=1, nums[1]=-1):
  prefixSum = -2 + (-1) = -3
  prefixSum != k ✗
  cache.contains(-3 - 1 = -4)? No ✗
  cache[-3] = 1
  State: prefixSum=-3, maxLen=0, cache={-2:0, -3:1}

Iteration 2 (i=2, nums[2]=2):
  prefixSum = -3 + 2 = -1
  prefixSum != k ✗
  cache.contains(-1 - 1 = -2)? Yes ✓ (cache[-2]=0)
  maxLen = max(0, 2 - 0) = 2
  cache.contains(-1)? No, cache[-1] = 2
  State: prefixSum=-1, maxLen=2, cache={-2:0, -3:1, -1:2}

Iteration 3 (i=3, nums[3]=1):
  prefixSum = -1 + 1 = 0
  prefixSum != k ✗
  cache.contains(0 - 1 = -1)? Yes ✓ (cache[-1]=2)
  maxLen = max(2, 3 - 2) = max(2, 1) = 2
  cache.contains(0)? No, cache[0] = 3
  State: prefixSum=0, maxLen=2, cache={-2:0, -3:1, -1:2, 0:3}

Return: maxLen = 2 ✓
```

**Verification:**
- Subarray `[-1, 2]` (indices 1-2): sum = -1 + 2 = 1 ✓
- Length = 2 ✓
- This is the maximum length subarray summing to 1 ✓

**Output:** `2` ✓

---

**Edge Case:** `nums = [2,0,0,3]`, `k = 3`

```
Initial: prefixSum = 0, maxLen = 0, cache = {}

Iteration 0 (i=0, nums[0]=2):
  prefixSum = 0 + 2 = 2
  prefixSum != k ✗
  cache.contains(2 - 3 = -1)? No ✗
  cache[2] = 0
  State: prefixSum=2, maxLen=0, cache={2:0}

Iteration 1 (i=1, nums[1]=0):
  prefixSum = 2 + 0 = 2
  prefixSum != k ✗
  cache.contains(2 - 3 = -1)? No ✗
  cache.contains(2)? Yes, skip (keep first occurrence)
  State: prefixSum=2, maxLen=0, cache={2:0}

Iteration 2 (i=2, nums[2]=0):
  prefixSum = 2 + 0 = 2
  prefixSum != k ✗
  cache.contains(2 - 3 = -1)? No ✗
  cache.contains(2)? Yes, skip
  State: prefixSum=2, maxLen=0, cache={2:0}

Iteration 3 (i=3, nums[3]=3):
  prefixSum = 2 + 3 = 5
  prefixSum != k ✗
  cache.contains(5 - 3 = 2)? Yes ✓ (cache[2]=0)
  maxLen = max(0, 3 - 0) = 3
  cache.contains(5)? No, cache[5] = 3
  State: prefixSum=5, maxLen=3, cache={2:0, 5:3}

Return: maxLen = 3 ✓
```

**Verification:**
- Subarray `[0, 0, 3]` (indices 1-3): sum = 0 + 0 + 3 = 3 ✓
- Length = 3 ✓
- This is the maximum length subarray summing to 3 ✓

**Output:** `3` ✓

## Complexity Analysis

### Solution 1 (Brute-Force):
- **Time Complexity**: O(n²) - Two nested loops, each checking O(n) positions
- **Space Complexity**: O(1) - Only using a constant amount of extra space

### Solution 2 (Prefix Sum with Hash Map):
- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(n) - Hash map can store up to n distinct prefix sums

## Key Insights

1. **Prefix Sum Technique**: Convert subarray sum problem to prefix sum difference problem
2. **Hash Map Lookup**: Use hash map to find previous prefix sums in O(1) time
3. **First Occurrence**: Store only the first occurrence of each prefix sum to maximize subarray length
4. **Direct Match**: Check if current prefix sum equals `k` (subarray from index 0)
5. **Overflow Prevention**: Use `long long` to handle large sums and prevent integer overflow
6. **Edge Cases**: Handle cases where prefix sum equals `k` directly, and cases with zeros in the array

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Brute-Force | O(n²) | O(1) | Simple but inefficient for large inputs |
| Prefix Sum + Hash Map | O(n) | O(n) | Optimal solution, handles all cases efficiently |

## Related Problems

- [1. Two Sum](https://leetcode.com/problems/two-sum/) - Hash map lookup for target sum
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) - Count subarrays with sum k
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) - Find minimum length subarray
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) - Check for subarray sum divisible by k
- [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) - Count subarrays divisible by k
