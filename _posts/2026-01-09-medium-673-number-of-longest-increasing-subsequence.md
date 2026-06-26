---
layout: post
title: "[Medium] 673. Number of Longest Increasing Subsequence"
date: 2026-01-09 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming]
permalink: /2026/01/09/medium-673-number-of-longest-increasing-subsequence/
tags: [leetcode, medium, array, dynamic-programming, longest-increasing-subsequence]
---
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

## Thinking Process

1. **Dual DP Arrays**: Need both length (`dp`) and count (`cnt`) arrays
- Longer subsequence → reset count
- Equal-length subsequence → accumulate count

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">1D DP recurrence</text>

  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

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

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **Dual DP Arrays**: Need both length (`dp`) and count (`cnt`) arrays

**How the code works:**
1. **Dual DP Arrays**: Need both length (`dp`) and count (`cnt`) arrays
- Longer subsequence → reset count
- Equal-length subsequence → accumulate count
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `nums = [1,3,5,4,7]`, expected output `2`:

The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

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
## Common Mistakes

1. **All same elements**: `nums = [2,2,2,2,2]` → return `5` (each element is a subsequence of length 1)
2. **Strictly increasing**: `nums = [1,2,3,4,5]` → return `1` (only one LIS)
3. **Single element**: `nums = [1]` → return `1`
4. **Multiple paths**: `nums = [1,3,5,4,7]` → return `2` (two ways to form length 4)

1. **Not resetting count**: When finding longer subsequence, must reset `cnt[i] = cnt[j]`, not add
2. **Wrong accumulation**: Only accumulate when lengths are equal, not when longer
3. **Missing final sum**: Must sum all `cnt[i]` where `dp[i] == maxLen`
4. **Initialization error**: Both `dp` and `cnt` should be initialized to 1

## Related Problems

- [LC 300: Longest Increasing Subsequence](https://www.leetcode.com/problems/longest-increasing-subsequence/) - Find length of LIS
- [LC 354: Russian Doll Envelopes](https://www.leetcode.com/problems/russian-doll-envelopes/) - 2D version of LIS
- [LC 646: Maximum Length of Pair Chain](https://www.leetcode.com/problems/maximum-length-of-pair-chain/) - Similar pattern
- [LC 334: Increasing Triplet Subsequence](https://www.leetcode.com/problems/increasing-triplet-subsequence/) - Check if triplet exists

---

*This problem extends LC 300 by adding count tracking. The key is maintaining both length and count information, and correctly handling the two cases: when a longer subsequence is found (reset count) and when an equal-length subsequence is found (accumulate count).*

## Key Takeaways

1. **Dual DP Arrays**: Need both length (`dp`) and count (`cnt`) arrays
2. **Two Update Cases**: 
   - Longer subsequence → reset count
   - Equal-length subsequence → accumulate count
3. **Count Accumulation**: When multiple paths lead to same length, sum their counts
4. **Final Sum**: Sum all counts for positions with maximum length

## References

- [LC 673: Number of Longest Increasing Subsequence on LeetCode](https://www.leetcode.com/problems/number-of-longest-increasing-subsequence/)
- [LeetCode Discuss — LC 673: Number of Longest Increasing Subsequence](https://www.leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/number-of-longest-increasing-subsequence/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
