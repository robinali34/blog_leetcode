---
layout: post
title: "673. Number of Longest Increasing Subsequence"
date: 2026-01-09 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming]
permalink: /2026/01/09/medium-673-number-of-longest-increasing-subsequence/
tags: [leetcode, medium, array, dynamic-programming, longest-increasing-subsequence]
---

# 673. Number of Longest Increasing Subsequence

## Problem Statement

Given an integer array `nums`, return *the number of longest increasing subsequences*.

**Notice** that the sequence has to be **strictly increasing**.

## Examples

**Example 1:**
```
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
```

**Example 2:**
```
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The longest increasing subsequence is of length 1, and there are 5 subsequences of length 1, so return 5.
```

## Constraints

- `1 <= nums.length <= 2000`
- `-10^6 <= nums[i] <= 10^6`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Subsequence definition**: What is a subsequence? (Assumption: Subsequence maintains relative order but doesn't need to be contiguous - can skip elements)

2. **Increasing definition**: What makes a subsequence increasing? (Assumption: Strictly increasing - each element must be greater than the previous one)

3. **Count requirement**: Do we need to count all LIS or just find the length? (Assumption: Count how many longest increasing subsequences exist - not just the length)

4. **Duplicate values**: How should we handle duplicate values? (Assumption: Based on "increasing", duplicates don't count - need strictly greater values)

5. **Output format**: What should we return - count or list of subsequences? (Assumption: Return count - integer representing number of LIS)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to count LIS. Let me generate all subsequences and count longest ones."

**Naive Solution**: Generate all possible subsequences, check if each is increasing, find maximum length, count subsequences with that length.

**Complexity**: O(2^n × n) time, O(n) space

**Issues**:
- Exponential time complexity
- Generates many invalid subsequences
- Very inefficient
- Doesn't leverage optimal substructure

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use DP to track both length and count of LIS ending at each position."

**Improved Solution**: Use DP where dp[i] = length of LIS ending at i, count[i] = number of LIS ending at i. For each i, check previous positions j where nums[j] < nums[i], update length and count.

**Complexity**: O(n²) time, O(n) space

**Improvements**:
- Leverages optimal substructure
- O(n²) time instead of exponential
- Tracks both length and count
- Handles all cases correctly

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "DP approach is optimal. Can optimize with binary search but more complex."

**Best Solution**: DP approach is optimal. Track length and count separately. For each position, find all previous positions that can extend LIS, sum their counts if they have maximum length.

**Complexity**: O(n²) time, O(n) space

**Key Realizations**:
1. DP is natural approach - optimal substructure
2. Track both length and count
3. O(n²) time is optimal for DP approach
4. Sum counts for positions with maximum length

## Solution Approach

This is a follow-up to [LC 300: Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/). Instead of just finding the length, we need to **count** how many longest increasing subsequences exist.

### Key Insights:

1. **Two DP Arrays**: 
   - `dp[i]`: Length of longest increasing subsequence ending at position `i`
   - `cnt[i]`: Number of longest increasing subsequences ending at position `i`

2. **Update Logic**:
   - If we find a longer subsequence: update `dp[i]` and reset `cnt[i] = cnt[j]`
   - If we find an equal-length subsequence: add `cnt[j]` to `cnt[i]`

3. **Final Count**: Sum all `cnt[i]` where `dp[i] == maxLen`

### Algorithm:

1. **Initialize**: `dp[i] = 1`, `cnt[i] = 1` for all positions
2. **For each position `i`**, check all previous positions `j`:
   - If `nums[i] > nums[j]`:
     - If `dp[j] + 1 > dp[i]`: Found longer subsequence → update `dp[i]` and `cnt[i] = cnt[j]`
     - Else if `dp[j] + 1 == dp[i]`: Found equal-length subsequence → add `cnt[j]` to `cnt[i]`
3. **Track maximum length** and sum counts for positions with maximum length

## Solution

### **Solution: Dynamic Programming with Count Tracking**

```cpp
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        const int N = nums.size();
        if(N == 0) return 0;

        vector<int> dp(N, 1), cnt(N, 1);
        int maxLen = 1, rtn = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j]) {
                    if(dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        cnt[i] = cnt[j];
                    } else if (dp[j] + 1 == dp[i]) {
                        cnt[i] += cnt[j];
                    }
                }
            }
            if(dp[i] > maxLen) {
                maxLen = dp[i];
                rtn = cnt[i];
            } else if(dp[i] == maxLen) {
                rtn += cnt[i];
            }            
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 5-7)**:
   - `dp[i] = 1`: Each element forms a subsequence of length 1
   - `cnt[i] = 1`: Each element has 1 subsequence ending at it
   - `maxLen = 1`: Track maximum length found so far
   - `rtn = 0`: Accumulate count of longest subsequences

2. **For Each Position `i` (Lines 8-22)**:
   - **Check all previous positions `j` (Lines 9-18)**:
     - If `nums[i] > nums[j]` (can extend subsequence):
       - **If `dp[j] + 1 > dp[i]` (Line 11)**: Found longer subsequence
         - Update `dp[i] = dp[j] + 1`
         - Reset `cnt[i] = cnt[j]` (new longest, so count comes from `j`)
       - **Else if `dp[j] + 1 == dp[i]` (Line 14)**: Found equal-length subsequence
         - Add `cnt[j]` to `cnt[i]` (accumulate counts)
   - **Update Global Maximum (Lines 19-23)**:
     - If `dp[i] > maxLen`: Found longer subsequence → update `maxLen` and reset `rtn = cnt[i]`
     - Else if `dp[i] == maxLen`: Add `cnt[i]` to `rtn`

3. **Return (Line 24)**: Total count of longest increasing subsequences

### **Why This Works:**

- **Length Tracking**: `dp[i]` tracks the length of LIS ending at position `i` (same as LC 300)
- **Count Accumulation**: `cnt[i]` accumulates the number of ways to form LIS of length `dp[i]` ending at `i`
- **Two Cases**:
  - **Longer subsequence found**: Reset count (only count the longest ones)
  - **Equal-length subsequence found**: Add counts (multiple ways to reach same length)
- **Final Sum**: Sum all counts for positions with maximum length

### **Example Walkthrough:**

**For `nums = [1,3,5,4,7]`:**

```
Initial: dp = [1,1,1,1,1], cnt = [1,1,1,1,1], maxLen = 1, rtn = 0

i=0: nums[0]=1
  - No previous positions
  - dp[0]=1, maxLen=1, rtn=1

i=1: nums[1]=3
  - j=0: 3 > 1 → dp[0]+1=2 > dp[1]=1
    - dp[1] = 2, cnt[1] = cnt[0] = 1
  - dp[1]=2 > maxLen=1 → maxLen=2, rtn=cnt[1]=1

i=2: nums[2]=5
  - j=0: 5 > 1 → dp[0]+1=2 > dp[2]=1
    - dp[2] = 2, cnt[2] = cnt[0] = 1
  - j=1: 5 > 3 → dp[1]+1=3 > dp[2]=2
    - dp[2] = 3, cnt[2] = cnt[1] = 1
  - dp[2]=3 > maxLen=2 → maxLen=3, rtn=cnt[2]=1

i=3: nums[3]=4
  - j=0: 4 > 1 → dp[0]+1=2 > dp[3]=1
    - dp[3] = 2, cnt[3] = cnt[0] = 1
  - j=1: 4 > 3 → dp[1]+1=3 == dp[3]=2
    - dp[3] = 3, cnt[3] += cnt[1] = 1 + 1 = 2
  - j=2: 4 ≤ 5 (skip)
  - dp[3]=3 == maxLen=3 → rtn += cnt[3] = 1 + 2 = 3

i=4: nums[4]=7
  - j=0: 7 > 1 → dp[0]+1=2 > dp[4]=1
    - dp[4] = 2, cnt[4] = cnt[0] = 1
  - j=1: 7 > 3 → dp[1]+1=3 > dp[4]=2
    - dp[4] = 3, cnt[4] = cnt[1] = 1
  - j=2: 7 > 5 → dp[2]+1=4 > dp[4]=3
    - dp[4] = 4, cnt[4] = cnt[2] = 1
  - j=3: 7 > 4 → dp[3]+1=4 == dp[4]=4
    - dp[4] = 4, cnt[4] += cnt[3] = 1 + 2 = 3
  - dp[4]=4 > maxLen=3 → maxLen=4, rtn=cnt[4]=3

Wait, let me recalculate. Actually, the longest should be length 4, and there should be 2 subsequences:
[1,3,4,7] and [1,3,5,7]

Let me trace more carefully:

i=0: dp[0]=1, cnt[0]=1, maxLen=1, rtn=1
i=1: dp[1]=2 (from 0), cnt[1]=1, maxLen=2, rtn=1
i=2: dp[2]=3 (from 1), cnt[2]=1, maxLen=3, rtn=1
i=3: dp[3]=3 (from 1), cnt[3]=1, maxLen=3, rtn=1+1=2
i=4: dp[4]=4 (from 2 or 3), cnt[4]=cnt[2]+cnt[3]=1+1=2, maxLen=4, rtn=2

Actually, let me verify with the code logic more carefully.
```

Let me provide a clearer walkthrough:

**For `nums = [1,3,5,4,7]`:**

| i | nums[i] | j | nums[j] | Condition | dp[j]+1 vs dp[i] | dp[i] | cnt[i] | maxLen | rtn |
|---|---------|---|---------|-----------|------------------|-------|--------|--------|-----|
| 0 | 1 | - | - | - | - | 1 | 1 | 1 | 1 |
| 1 | 3 | 0 | 1 | 3>1 | 2 > 1 | 2 | 1 | 2 | 1 |
| 2 | 5 | 0 | 1 | 5>1 | 2 > 1 | 2 | 1 | 2 | 1 |
| 2 | 5 | 1 | 3 | 5>3 | 3 > 2 | 3 | 1 | 3 | 1 |
| 3 | 4 | 0 | 1 | 4>1 | 2 > 1 | 2 | 1 | 3 | 1 |
| 3 | 4 | 1 | 3 | 4>3 | 3 == 2 | 3 | 1+1=2 | 3 | 1+2=3 |
| 3 | 4 | 2 | 5 | 4≤5 | skip | 3 | 2 | 3 | 3 |
| 4 | 7 | 0 | 1 | 7>1 | 2 > 1 | 2 | 1 | 3 | 3 |
| 4 | 7 | 1 | 3 | 7>3 | 3 > 2 | 3 | 1 | 3 | 3 |
| 4 | 7 | 2 | 5 | 7>5 | 4 > 3 | 4 | 1 | 4 | 1 |
| 4 | 7 | 3 | 4 | 7>4 | 4 == 4 | 4 | 1+2=3 | 4 | 1+3=4 |

Wait, this doesn't match the expected output of 2. Let me reconsider...

Actually, the issue is that when we check j=2 and j=3 for i=4, both can extend to length 4:
- From j=2 (5): [1,3,5,7] → length 4
- From j=3 (4): [1,3,4,7] → length 4

So cnt[4] should be cnt[2] + cnt[3] = 1 + 2 = 3? But the expected answer is 2.

Let me think about this differently. The actual longest subsequences are:
- [1,3,5,7] (one way)
- [1,3,4,7] (one way)

So there are 2 subsequences. But why would cnt[3]=2? Let me check...

For i=3 (value 4):
- Can extend from j=0 (1): [1,4] → length 2
- Can extend from j=1 (3): [1,3,4] → length 3

So dp[3]=3, and there's only 1 way: [1,3,4]. So cnt[3] should be 1, not 2.

Let me recalculate more carefully:

```
i=0: dp[0]=1, cnt[0]=1
i=1: 
  - j=0: 3>1, dp[0]+1=2 > dp[1]=1 → dp[1]=2, cnt[1]=cnt[0]=1
i=2:
  - j=0: 5>1, dp[0]+1=2 > dp[2]=1 → dp[2]=2, cnt[2]=cnt[0]=1
  - j=1: 5>3, dp[1]+1=3 > dp[2]=2 → dp[2]=3, cnt[2]=cnt[1]=1
i=3:
  - j=0: 4>1, dp[0]+1=2 > dp[3]=1 → dp[3]=2, cnt[3]=cnt[0]=1
  - j=1: 4>3, dp[1]+1=3 == dp[3]=2 → dp[3]=3, cnt[3]=cnt[1]=1
  - j=2: 4≤5, skip
i=4:
  - j=0: 7>1, dp[0]+1=2 > dp[4]=1 → dp[4]=2, cnt[4]=cnt[0]=1
  - j=1: 7>3, dp[1]+1=3 > dp[4]=2 → dp[4]=3, cnt[4]=cnt[1]=1
  - j=2: 7>5, dp[2]+1=4 > dp[4]=3 → dp[4]=4, cnt[4]=cnt[2]=1
  - j=3: 7>4, dp[3]+1=4 == dp[4]=4 → dp[4]=4, cnt[4]=cnt[2]+cnt[3]=1+1=2
```

So final: maxLen=4, rtn=2. This matches!

### **Complexity Analysis:**

- **Time Complexity:** O(n²)
  - For each of n positions, check all previous positions
  - Total: O(n × n) = O(n²)
- **Space Complexity:** O(n)
  - Two arrays `dp` and `cnt` of size n
  - O(1) extra variables

### **Example Walkthrough (Corrected):**

**For `nums = [1,3,5,4,7]`:**

```
Step-by-step:

i=0: nums[0]=1
  dp[0]=1, cnt[0]=1
  maxLen=1, rtn=1

i=1: nums[1]=3
  j=0: 3 > 1 → dp[0]+1=2 > dp[1]=1
    dp[1]=2, cnt[1]=cnt[0]=1
  dp[1]=2 > maxLen=1 → maxLen=2, rtn=1

i=2: nums[2]=5
  j=0: 5 > 1 → dp[0]+1=2 > dp[2]=1
    dp[2]=2, cnt[2]=cnt[0]=1
  j=1: 5 > 3 → dp[1]+1=3 > dp[2]=2
    dp[2]=3, cnt[2]=cnt[1]=1
  dp[2]=3 > maxLen=2 → maxLen=3, rtn=1

i=3: nums[3]=4
  j=0: 4 > 1 → dp[0]+1=2 > dp[3]=1
    dp[3]=2, cnt[3]=cnt[0]=1
  j=1: 4 > 3 → dp[1]+1=3 == dp[3]=2
    dp[3]=3, cnt[3]=cnt[1]=1
  j=2: 4 ≤ 5 (skip)
  dp[3]=3 == maxLen=3 → rtn += cnt[3] = 1 + 1 = 2

i=4: nums[4]=7
  j=0: 7 > 1 → dp[0]+1=2 > dp[4]=1
    dp[4]=2, cnt[4]=cnt[0]=1
  j=1: 7 > 3 → dp[1]+1=3 > dp[4]=2
    dp[4]=3, cnt[4]=cnt[1]=1
  j=2: 7 > 5 → dp[2]+1=4 > dp[4]=3
    dp[4]=4, cnt[4]=cnt[2]=1
  j=3: 7 > 4 → dp[3]+1=4 == dp[4]=4
    dp[4]=4, cnt[4]=cnt[2]+cnt[3]=1+1=2
  dp[4]=4 > maxLen=3 → maxLen=4, rtn=cnt[4]=2

Final result: 2
```

The two longest increasing subsequences are:
- `[1,3,5,7]` (extending from position 2)
- `[1,3,4,7]` (extending from position 3)

## Solution 2: Binary Search with Patience Sorting

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

This approach uses binary search similar to the patience sorting technique from LC 300, but extends it to track counts.

```cpp
class Solution {
    int binarySearch(int n, function<bool(int)> f) {
        int l = 0, r = n;
        while (l < r) {
            int mid = (l + r) / 2;
            if (f(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }

public:
    int findNumberOfLIS(vector<int> &nums) {
        vector<vector<int>> d, cnt;
        for (int v : nums) {
            int i = binarySearch(d.size(), [&](int i) { return d[i].back() >= v; });
            int c = 1;
            if (i > 0) {
                int k = binarySearch(d[i - 1].size(), [&](int k) { return d[i - 1][k] < v; });
                c = cnt[i - 1].back() - cnt[i - 1][k];
            }
            if (i == d.size()) {
                d.push_back({v});
                cnt.push_back({0, c});
            } else {
                d[i].push_back(v);
                cnt[i].push_back(cnt[i].back() + c);
            }
        }
        return cnt.back().back();
    }
};
```

### **Algorithm Explanation:**

1. **Data Structures**:
   - `d[i]`: Array of ending values for subsequences of length `i+1` (maintained in sorted order)
   - `cnt[i]`: Prefix sum array where `cnt[i][j]` = total count of subsequences of length `i+1` ending with values up to `d[i][j]`

2. **For each value `v`**:
   - **Find length `i`**: Binary search to find where `v` should be inserted (first position where `d[i].back() >= v`)
   - **Calculate count `c`**: 
     - If `i == 0`: `c = 1` (new subsequence of length 1)
     - If `i > 0`: Find how many subsequences of length `i` end with value < `v`
       - Binary search in `d[i-1]` to find first position `k` where `d[i-1][k] >= v`
       - Count = `cnt[i-1].back() - cnt[i-1][k]` (prefix sum difference)
   - **Update structures**:
     - If `i == d.size()`: New length discovered, create new arrays
     - Otherwise: Append `v` to `d[i]` and update prefix sum in `cnt[i]`

3. **Return**: `cnt.back().back()` (total count of longest subsequences)

### **Key Insights:**

- **Patience Sorting**: Similar to LC 300, maintains smallest tail elements for each length
- **Prefix Sums**: `cnt[i]` uses prefix sums to efficiently count subsequences ending with values < `v`
- **Binary Search**: Uses binary search twice per element (O(log n) each) for O(n log n) total
- **Sorted Arrays**: `d[i]` arrays are maintained in sorted order as we process elements

### **How It Works:**

The algorithm maintains:
- `d[i]`: Sorted array of ending values for subsequences of length `i+1`
- `cnt[i]`: Prefix sum array where `cnt[i][j]` represents the cumulative count

For each value `v`:
1. Find the length `i` where `v` should be placed (using binary search)
2. Calculate the count by finding how many subsequences of length `i-1` end with values < `v`
3. Update the arrays accordingly

**Note**: The binary search solution is more complex and requires careful understanding of the prefix sum logic. The DP solution (Solution 1) is recommended for interviews due to its clarity and correctness.

### **Complexity Analysis:**

- **Time Complexity:** O(n log n)
  - For each of n elements: two binary searches (O(log n) each)
  - Total: O(n × log n) = O(n log n)
- **Space Complexity:** O(n)
  - `d` and `cnt` arrays store at most n elements total
  - O(n) space

## Key Insights

1. **Dual DP Arrays**: Need both length (`dp`) and count (`cnt`) arrays
2. **Two Update Cases**: 
   - Longer subsequence → reset count
   - Equal-length subsequence → accumulate count
3. **Count Accumulation**: When multiple paths lead to same length, sum their counts
4. **Final Sum**: Sum all counts for positions with maximum length

## Edge Cases

1. **All same elements**: `nums = [2,2,2,2,2]` → return `5` (each element is a subsequence of length 1)
2. **Strictly increasing**: `nums = [1,2,3,4,5]` → return `1` (only one LIS)
3. **Single element**: `nums = [1]` → return `1`
4. **Multiple paths**: `nums = [1,3,5,4,7]` → return `2` (two ways to form length 4)

## Common Mistakes

1. **Not resetting count**: When finding longer subsequence, must reset `cnt[i] = cnt[j]`, not add
2. **Wrong accumulation**: Only accumulate when lengths are equal, not when longer
3. **Missing final sum**: Must sum all `cnt[i]` where `dp[i] == maxLen`
4. **Initialization error**: Both `dp` and `cnt` should be initialized to 1

## Related Problems

- [LC 300: Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) - Find length of LIS
- [LC 354: Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) - 2D version of LIS
- [LC 646: Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) - Similar pattern
- [LC 334: Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) - Check if triplet exists

---

*This problem extends LC 300 by adding count tracking. The key is maintaining both length and count information, and correctly handling the two cases: when a longer subsequence is found (reset count) and when an equal-length subsequence is found (accumulate count).*

