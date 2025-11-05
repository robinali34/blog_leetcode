---
layout: post
title: "[Medium] 525. Contiguous Array"
date: 2025-11-04 22:03:10 -0800
categories: leetcode algorithm medium cpp arrays hash-map prefix-sum problem-solving
permalink: /posts/2025-11-04-medium-525-contiguous-array/
tags: [leetcode, medium, array, hash-map, prefix-sum, subarray]
---

# [Medium] 525. Contiguous Array

Given a binary array `nums`, return *the maximum length of a contiguous subarray with an equal number of `0` and `1`*.

## Examples

**Example 1:**
```
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
```

**Example 2:**
```
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] or [1, 0] is the longest contiguous subarray with an equal number of 0 and 1.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Solution: Prefix Sum with Hash Map

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Convert `0` to `-1` and `1` to `+1`, then use prefix sum. When we see a prefix sum we've encountered before, the subarray between those two positions has equal 0s and 1s (net sum of 0).

```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> map;
        map[0] = -1;  // Base case: prefix sum 0 at index -1
        int maxLen = 0, count = 0;
        
        for(int i = 0; i < (int)nums.size(); i++) {
            count = count + (nums[i] == 1 ? 1 : -1);
            
            if(map.contains(count)) {
                maxLen = max(maxLen, i - map[count]);
            } else {
                map[count] = i;
            }
        }
        
        return maxLen;
    }
};
```

## How the Algorithm Works

### Key Insight: Prefix Sum Transformation

1. **Convert to sum array:** `0` → `-1`, `1` → `+1`
2. **Calculate prefix sums:** Track cumulative count
3. **Find equal subarrays:** When prefix sum repeats, the subarray between has net sum 0 (equal 0s and 1s)

### Step-by-Step Example: `nums = [0,1,0,0,1,1,0]`

| i | nums[i] | Count | Prefix Sum | Map Contains? | Action | maxLen |
|---|---------|-------|------------|---------------|--------|--------|
| -1 | - | - | 0 | - | Initialize `map[0] = -1` | 0 |
| 0 | 0 | -1 | -1 | No | `map[-1] = 0` | 0 |
| 1 | 1 | +1 | 0 | Yes | `0 - (-1) = 1` → maxLen = 2 | 2 |
| 2 | 0 | -1 | -1 | Yes | `2 - 0 = 2` → maxLen = 2 | 2 |
| 3 | 0 | -1 | -2 | No | `map[-2] = 3` | 2 |
| 4 | 1 | +1 | -1 | Yes | `4 - 0 = 4` → maxLen = 4 | 4 |
| 5 | 1 | +1 | 0 | Yes | `5 - (-1) = 6` → maxLen = 6 | 6 |
| 6 | 0 | -1 | -1 | Yes | `6 - 0 = 6` → maxLen = 6 | 6 |

**Final Answer:** 6

**Hash Map State:**
```
map = {0: -1, -1: 0, -2: 3}
```

### Visual Representation

```
nums:    [0, 1, 0, 0, 1, 1, 0]
values:  [-1,+1,-1,-1,+1,+1,-1]
prefix:  [-1, 0,-1,-2,-1, 0, -1]
          ↑        ↑
          i=0      i=4
          count=-1 count=-1
          
Subarray [0,4]: [0,1,0,0,1]
  Count: -1 + 1 - 1 - 1 + 1 = -1 (not equal)

Wait, let me recalculate:
nums:    [0, 1, 0, 0, 1, 1, 0]
         0  1  2  3  4  5  6
values:  [-1,+1,-1,-1,+1,+1,-1]
prefix:  [-1, 0,-1,-2,-1, 0, -1]
          ↑        ↑
          i=-1     i=5
          count=0  count=0
          
Subarray [0,5]: [0,1,0,0,1,1]
  0s: 3 (indices 0,2,3)
  1s: 3 (indices 1,4,5)
  Equal! Length = 6
```

## Key Insights

1. **Transformation**: `0 → -1`, `1 → +1` converts the problem to finding subarrays with sum 0
2. **Prefix Sum**: Track cumulative count from start
3. **Hash Map**: Store first occurrence of each prefix sum for longest subarray
4. **Base Case**: `map[0] = -1` handles subarrays starting from index 0
5. **Repeated Prefix**: If `prefix[i] == prefix[j]`, then `subarray[i+1..j]` has sum 0

## Algorithm Breakdown

### 1. Initialize Hash Map
```cpp
unordered_map<int, int> map;
map[0] = -1;  // Base case
int maxLen = 0, count = 0;
```
- **`map[0] = -1`**: Represents prefix sum 0 before the array starts
- This allows us to handle subarrays starting at index 0
- **`count`**: Tracks the current prefix sum

### 2. Transform and Calculate Prefix Sum
```cpp
count = count + (nums[i] == 1 ? 1 : -1);
```
- **Convert**: `0` → `-1`, `1` → `+1`
- **Accumulate**: Add to running count

### 3. Check for Repeated Prefix Sum
```cpp
if(map.contains(count)) {
    maxLen = max(maxLen, i - map[count]);
}
```
- **If prefix sum seen before**: Subarray from `map[count] + 1` to `i` has sum 0
- **Length**: `i - map[count]` (we don't add 1 because `map[count]` is the index before the subarray starts)

### 4. Store First Occurrence
```cpp
else {
    map[count] = i;
}
```
- **Store only first occurrence**: To maximize subarray length
- **Later occurrences**: Would give shorter subarrays

## Why This Works

### Mathematical Proof

For a subarray `nums[i+1..j]` to have equal 0s and 1s:
- Number of 1s = Number of 0s
- Sum of transformed values = 0
- `prefix[j] - prefix[i] = 0`
- `prefix[j] = prefix[i]`

Therefore, if `prefix[j] == prefix[i]`, the subarray `nums[i+1..j]` has equal 0s and 1s.

### Example Explanation

```
nums = [0, 1, 0, 0, 1, 1, 0]
       0  1  2  3  4  5  6

Transformed: [-1, +1, -1, -1, +1, +1, -1]

Prefix sums:
i=-1: prefix = 0 (base case)
i=0:  prefix = -1
i=1:  prefix = 0  ← Same as i=-1!
i=2:  prefix = -1 ← Same as i=0!
i=3:  prefix = -2
i=4:  prefix = -1 ← Same as i=0!
i=5:  prefix = 0   ← Same as i=-1!
i=6:  prefix = -1   ← Same as i=0!

Subarray [0,5]: prefix[5] = 0 = prefix[-1]
  Length = 5 - (-1) = 6 ✓
  
Subarray [1,5]: prefix[5] = 0 = prefix[1]
  Length = 5 - 1 = 4 ✓
```

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Single pass through array, hash map operations are O(1) |
| **Space** | O(n) - Hash map stores at most n prefix sums |

## Alternative Approaches

### Approach 1: Brute Force (TLE)

```cpp
int findMaxLength(vector<int>& nums) {
    int maxLen = 0;
    for(int i = 0; i < nums.size(); i++) {
        int zeros = 0, ones = 0;
        for(int j = i; j < nums.size(); j++) {
            if(nums[j] == 0) zeros++;
            else ones++;
            
            if(zeros == ones) {
                maxLen = max(maxLen, j - i + 1);
            }
        }
    }
    return maxLen;
}
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

### Approach 2: Using Array Instead of Hash Map

Since prefix sums can only range from `-n` to `n`, we can use an array:

```cpp
int findMaxLength(vector<int>& nums) {
    int n = nums.size();
    vector<int> map(2 * n + 1, -2);  // Offset by n
    map[n] = -1;  // map[0] = -1 with offset
    int maxLen = 0, count = 0;
    
    for(int i = 0; i < n; i++) {
        count += (nums[i] == 1 ? 1 : -1);
        int idx = count + n;  // Offset to positive index
        
        if(map[idx] != -2) {
            maxLen = max(maxLen, i - map[idx]);
        } else {
            map[idx] = i;
        }
    }
    
    return maxLen;
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - But fixed size array instead of hash map

## Comparison of Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n²) | O(1) | Simple but inefficient |
| Hash Map | O(n) | O(n) | Flexible, handles any range |
| Array | O(n) | O(n) | Fixed size, faster lookups |

## Edge Cases

1. **All zeros or all ones**: `[0,0,0]` or `[1,1,1]` → `0` (no equal subarray)
2. **Single element**: `[0]` or `[1]` → `0`
3. **Perfect balance**: `[0,1]` → `2`
4. **Multiple valid subarrays**: `[0,1,0,1,0,1]` → `6`

## Common Mistakes

1. **Missing base case**: Forgetting `map[0] = -1` causes issues with subarrays starting at index 0
2. **Wrong length calculation**: Using `i - map[count] + 1` instead of `i - map[count]`
3. **Updating map incorrectly**: Updating map even when count exists (should only store first occurrence)
4. **Wrong transformation**: Using `0 → 0` and `1 → 1` instead of `0 → -1` and `1 → +1`

## Detailed Example Walkthrough

### Example: `nums = [0,1,0,0,1,1,0]`

```
Step 0: Initialize
  map = {0: -1}
  count = 0
  maxLen = 0

Step 1: i=0, nums[0]=0
  count = 0 + (-1) = -1
  map.contains(-1)? No
  map[-1] = 0
  map = {0: -1, -1: 0}
  maxLen = 0

Step 2: i=1, nums[1]=1
  count = -1 + 1 = 0
  map.contains(0)? Yes (at index -1)
  maxLen = max(0, 1 - (-1)) = max(0, 2) = 2
  map = {0: -1, -1: 0}
  maxLen = 2

Step 3: i=2, nums[2]=0
  count = 0 + (-1) = -1
  map.contains(-1)? Yes (at index 0)
  maxLen = max(2, 2 - 0) = max(2, 2) = 2
  map = {0: -1, -1: 0}
  maxLen = 2

Step 4: i=3, nums[3]=0
  count = -1 + (-1) = -2
  map.contains(-2)? No
  map[-2] = 3
  map = {0: -1, -1: 0, -2: 3}
  maxLen = 2

Step 5: i=4, nums[4]=1
  count = -2 + 1 = -1
  map.contains(-1)? Yes (at index 0)
  maxLen = max(2, 4 - 0) = max(2, 4) = 4
  map = {0: -1, -1: 0, -2: 3}
  maxLen = 4

Step 6: i=5, nums[5]=1
  count = -1 + 1 = 0
  map.contains(0)? Yes (at index -1)
  maxLen = max(4, 5 - (-1)) = max(4, 6) = 6
  map = {0: -1, -1: 0, -2: 3}
  maxLen = 6

Step 7: i=6, nums[6]=0
  count = 0 + (-1) = -1
  map.contains(-1)? Yes (at index 0)
  maxLen = max(6, 6 - 0) = max(6, 6) = 6
  map = {0: -1, -1: 0, -2: 3}
  maxLen = 6

Final result: 6
```

## Why Store Only First Occurrence?

To maximize subarray length, we want the earliest starting position for each prefix sum.

**Example:**
```
prefix sums: [0, -1, 0, -1, 0, -1]
              ↑   ↑   ↑   ↑   ↑   ↑
            i=-1 0   1   2   3   4

For prefix sum 0:
- First occurrence: i = -1
- Later occurrence: i = 1

Subarray ending at i=3:
- Using i=-1: length = 3 - (-1) = 4 ✓
- Using i=1:  length = 3 - 1 = 2 ✗

Therefore, we should store only the first occurrence.
```

## Related Problems

- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) - Find subarrays with sum k
- [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) - Similar prefix sum pattern
- [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) - Very similar
- [1124. Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/) - Similar technique
- [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) - Check for multiples

## Pattern Recognition

This problem demonstrates the **Prefix Sum + Hash Map** pattern:
- Transform problem into finding subarrays with target sum
- Use prefix sums to calculate subarray sums efficiently
- Hash map stores first occurrence of each prefix sum
- Look for repeated prefix sums to find valid subarrays

**Key Insight:**
- Subarray `nums[i+1..j]` has sum 0 if `prefix[j] == prefix[i]`
- This extends to any target sum: subarray has sum k if `prefix[j] - prefix[i] == k`

**Applications:**
- Finding subarrays with specific sum
- Finding subarrays with equal elements
- Finding subarrays with specific properties (balanced, etc.)

## Optimization Tips

### Early Exit (Not Applicable)
Since we need to check all positions, early exit isn't possible.

### Memory Optimization
For very large arrays, consider using array instead of hash map if prefix sum range is bounded.

### Use `contains()` vs `find()`
```cpp
// Modern C++20 (your code)
if(map.contains(count)) { ... }

// Alternative (C++17 and earlier)
if(map.find(count) != map.end()) { ... }
```

Both are O(1) average case, but `contains()` is more readable.

## Code Quality Notes

1. **Readability**: Clear variable names and logic
2. **Efficiency**: Optimal O(n) time and space
3. **Correctness**: Handles all edge cases properly
4. **Modern C++**: Uses `contains()` method (C++20)

---

*This problem is a classic example of transforming a problem into a prefix sum problem. The key insight is converting the "equal 0s and 1s" constraint into "sum equals 0" after transformation.*

