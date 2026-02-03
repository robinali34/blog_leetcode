---
layout: post
title: "974. Subarray Sums Divisible by K"
date: 2026-02-02 00:00:00 -0700
categories: [leetcode, medium, array, hash-table, prefix-sum]
permalink: /2026/02/02/medium-974-subarray-sums-divisible-by-k/
tags: [leetcode, medium, array, hash-table, prefix-sum]
---

# 974. Subarray Sums Divisible by K

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**

```
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

**Example 2:**

```
Input: nums = [5], k = 9
Output: 0
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `2 <= k <= 10^4`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Subarray definition**: What constitutes a subarray? (Assumption: A contiguous non-empty sequence of elements - must be consecutive elements)

2. **Divisibility**: What does "divisible by k" mean? (Assumption: The sum of the subarray must be divisible by `k`, i.e., `sum % k == 0`)

3. **Negative numbers**: How do we handle negative numbers in modulo operations? (Assumption: Use `(num % k + k) % k` to ensure non-negative modulo result)

4. **Empty subarray**: Should we consider empty subarrays? (Assumption: No - subarray must be non-empty, so length is at least 1)

5. **Overlapping subarrays**: If multiple subarrays are divisible by `k`, should we count all of them? (Assumption: Yes - count all distinct subarrays that are divisible by `k`, even if they overlap)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For each starting position `i`, iterate through all ending positions `j >= i`, calculate the sum of subarray `nums[i..j]`, and increment count if `sum % k == 0`. This approach has O(n²) time complexity and O(1) space complexity.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use prefix sums to avoid recalculating subarray sums. For each position, we can compute the sum from index 0 to current position. However, we still need to check all pairs of positions, which is still O(n²) time.

**Step 3: Optimized Solution (8 minutes)**

Use prefix sum modulo with hash map/array. The key insight is: if `prefixMod[i] == prefixMod[j]`, then `sum(nums[i+1..j]) % k == 0`. We can use an array of size `k` to count occurrences of each modulo value. For each position, check how many previous positions have the same modulo value. This achieves O(n) time and O(k) space complexity.

## Solution Approach

This problem is a variation of the prefix sum technique, but uses modulo arithmetic to handle divisibility. The key insight is that if two prefix sums have the same modulo value, the subarray between them is divisible by `k`.

### Key Insights:

1. **Modulo Property**: If `prefixSum[i] % k == prefixSum[j] % k`, then `sum(nums[i+1..j]) % k == 0`
2. **Negative Modulo**: Use `(num % k + k) % k` to ensure non-negative modulo result
3. **Array Instead of Hash Map**: Since modulo values are in range `[0, k-1]`, we can use an array of size `k`
4. **Initial State**: Initialize with `prefixMods[0] = 1` to handle subarrays starting from index 0

## Solution: Prefix Sum Modulo with Array

```cpp
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int prefixMod = 0, cnt = 0;
        vector<int> prefixMods(k, 0);
        prefixMods[0] = 1; 
        for(int num: nums) {
            prefixMod = (prefixMod + num % k + k) % k;
            cnt += prefixMods[prefixMod];
            prefixMods[prefixMod]++;
        }
        return cnt;
    }
};
```

### Algorithm Breakdown:

1. **Initialize**: 
   - `prefixMod = 0`: Running prefix sum modulo
   - `cnt = 0`: Count of subarrays divisible by `k`
   - `prefixMods[k]`: Array to count occurrences of each modulo value
   - `prefixMods[0] = 1`: Initialize with prefix sum 0 (for subarrays starting at index 0)

2. **Iterate**: For each number in the array:
   - Update prefix modulo: `prefixMod = (prefixMod + num % k + k) % k`
     - `num % k`: Get modulo of current number
     - `+ k`: Handle negative numbers
     - `% k`: Ensure result is in range `[0, k-1]`
   - Add count: `cnt += prefixMods[prefixMod]` (number of previous positions with same modulo)
   - Increment count: `prefixMods[prefixMod]++`

3. **Return**: Total count of subarrays divisible by `k`

### Why This Works:

- **Modulo Property**: If `prefixMod[i] == prefixMod[j]`, then `(prefixSum[j] - prefixSum[i]) % k == 0`
- **Negative Handling**: `(num % k + k) % k` ensures non-negative modulo for negative numbers
- **Counting**: For each position, count how many previous positions have the same modulo value
- **Initial State**: `prefixMods[0] = 1` handles the case where subarray starts at index 0

### Sample Test Case Run:

**Input:** `nums = [4,5,0,-2,-3,1]`, `k = 5`

```
Initial: prefixMod = 0, cnt = 0, prefixMods = [1, 0, 0, 0, 0]

Iteration 0 (num = 4):
  prefixMod = (0 + 4 % 5 + 5) % 5 = (0 + 4 + 5) % 5 = 9 % 5 = 4
  prefixMods[4] = 0, cnt = 0 + 0 = 0
  prefixMods[4] = 1
  State: prefixMod=4, cnt=0, prefixMods=[1,0,0,0,1]

Iteration 1 (num = 5):
  prefixMod = (4 + 5 % 5 + 5) % 5 = (4 + 0 + 5) % 5 = 9 % 5 = 4
  prefixMods[4] = 1, cnt = 0 + 1 = 1
  prefixMods[4] = 2
  State: prefixMod=4, cnt=1, prefixMods=[1,0,0,0,2]

Iteration 2 (num = 0):
  prefixMod = (4 + 0 % 5 + 5) % 5 = (4 + 0 + 5) % 5 = 9 % 5 = 4
  prefixMods[4] = 2, cnt = 1 + 2 = 3
  prefixMods[4] = 3
  State: prefixMod=4, cnt=3, prefixMods=[1,0,0,0,3]

Iteration 3 (num = -2):
  prefixMod = (4 + (-2) % 5 + 5) % 5 = (4 + 3 + 5) % 5 = 12 % 5 = 2
  prefixMods[2] = 0, cnt = 3 + 0 = 3
  prefixMods[2] = 1
  State: prefixMod=2, cnt=3, prefixMods=[1,0,1,0,3]

Iteration 4 (num = -3):
  prefixMod = (2 + (-3) % 5 + 5) % 5 = (2 + 2 + 5) % 5 = 9 % 5 = 4
  prefixMods[4] = 3, cnt = 3 + 3 = 6
  prefixMods[4] = 4
  State: prefixMod=4, cnt=6, prefixMods=[1,0,1,0,4]

Iteration 5 (num = 1):
  prefixMod = (4 + 1 % 5 + 5) % 5 = (4 + 1 + 5) % 5 = 10 % 5 = 0
  prefixMods[0] = 1, cnt = 6 + 1 = 7
  prefixMods[0] = 2
  State: prefixMod=0, cnt=7, prefixMods=[2,0,1,0,4]

Return: cnt = 7 ✓
```

**Verification:**
- Subarrays divisible by 5:
  - `[5]` (indices 1-1): sum = 5 ✓
  - `[5,0]` (indices 1-2): sum = 5 ✓
  - `[0]` (indices 2-2): sum = 0 ✓
  - `[5,0,-2,-3]` (indices 1-4): sum = 0 ✓
  - `[0,-2,-3]` (indices 2-4): sum = -5 ✓ (divisible by 5)
  - `[-2,-3]` (indices 3-4): sum = -5 ✓ (divisible by 5)
  - `[4,5,0,-2,-3,1]` (indices 0-5): sum = 5 ✓
- Total count = 7 ✓

**Output:** `7` ✓

---

**Another Example:** `nums = [5]`, `k = 9`

```
Initial: prefixMod = 0, cnt = 0, prefixMods = [1, 0, 0, 0, 0, 0, 0, 0, 0]

Iteration 0 (num = 5):
  prefixMod = (0 + 5 % 9 + 9) % 9 = (0 + 5 + 9) % 9 = 14 % 9 = 5
  prefixMods[5] = 0, cnt = 0 + 0 = 0
  prefixMods[5] = 1
  State: prefixMod=5, cnt=0, prefixMods=[1,0,0,0,0,1,0,0,0]

Return: cnt = 0 ✓
```

**Verification:**
- Subarray `[5]`: sum = 5, 5 % 9 = 5 ≠ 0 ✗
- No subarray divisible by 9 ✓

**Output:** `0` ✓

---

**Edge Case:** `nums = [1,2,3,4,5]`, `k = 3`

```
Initial: prefixMod = 0, cnt = 0, prefixMods = [1, 0, 0]

Iteration 0 (num = 1):
  prefixMod = (0 + 1 % 3 + 3) % 3 = (0 + 1 + 3) % 3 = 4 % 3 = 1
  prefixMods[1] = 0, cnt = 0
  prefixMods[1] = 1
  State: prefixMod=1, cnt=0, prefixMods=[1,1,0]

Iteration 1 (num = 2):
  prefixMod = (1 + 2 % 3 + 3) % 3 = (1 + 2 + 3) % 3 = 6 % 3 = 0
  prefixMods[0] = 1, cnt = 0 + 1 = 1
  prefixMods[0] = 2
  State: prefixMod=0, cnt=1, prefixMods=[2,1,0]

Iteration 2 (num = 3):
  prefixMod = (0 + 3 % 3 + 3) % 3 = (0 + 0 + 3) % 3 = 3 % 3 = 0
  prefixMods[0] = 2, cnt = 1 + 2 = 3
  prefixMods[0] = 3
  State: prefixMod=0, cnt=3, prefixMods=[3,1,0]

Iteration 3 (num = 4):
  prefixMod = (0 + 4 % 3 + 3) % 3 = (0 + 1 + 3) % 3 = 4 % 3 = 1
  prefixMods[1] = 1, cnt = 3 + 1 = 4
  prefixMods[1] = 2
  State: prefixMod=1, cnt=4, prefixMods=[3,2,0]

Iteration 4 (num = 5):
  prefixMod = (1 + 5 % 3 + 3) % 3 = (1 + 2 + 3) % 3 = 6 % 3 = 0
  prefixMods[0] = 3, cnt = 4 + 3 = 7
  prefixMods[0] = 4
  State: prefixMod=0, cnt=7, prefixMods=[4,2,0]

Return: cnt = 7 ✓
```

**Verification:**
- Subarrays divisible by 3:
  - `[1,2]` (indices 0-1): sum = 3 ✓
  - `[3]` (indices 2-2): sum = 3 ✓
  - `[1,2,3]` (indices 0-2): sum = 6 ✓
  - `[2,3,4]` (indices 1-3): sum = 9 ✓
  - `[3,4,5]` (indices 2-4): sum = 12 ✓
  - `[1,2,3,4,5]` (indices 0-4): sum = 15 ✓
  - `[4,5]` (indices 3-4): sum = 9 ✓
- Total count = 7 ✓

**Output:** `7` ✓

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(k) - Array of size `k` to store modulo counts (more efficient than O(n) hash map)

## Key Insights

1. **Modulo Property**: If two prefix sums have the same modulo value, the subarray between them is divisible by `k`
2. **Negative Modulo Handling**: Use `(num % k + k) % k` to ensure non-negative modulo for negative numbers
3. **Array vs Hash Map**: Since modulo values are in range `[0, k-1]`, we can use an array instead of a hash map, saving space
4. **Initial State**: Initialize with `prefixMods[0] = 1` to handle subarrays starting from index 0
5. **Integer Overflow Prevention**: The modulo operation naturally prevents integer overflow by keeping values in range `[0, k-1]`

## Comparison with Related Problems

| Problem | Goal | Technique | Space Complexity |
|---------|------|-----------|------------------|
| LC 560 | Count subarrays with sum = k | Prefix Sum + Hash Map | O(n) |
| LC 325 | Maximum length subarray with sum = k | Prefix Sum + Hash Map | O(n) |
| LC 974 | Count subarrays divisible by k | Prefix Modulo + Array | O(k) |

## Related Problems

- [1. Two Sum](https://leetcode.com/problems/two-sum/) - Hash map lookup for target sum
- [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) - Find maximum length subarray
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) - Count subarrays with sum k
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) - Check for subarray sum divisible by k
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) - Find minimum length subarray
