---
layout: post
title: "[Medium] 1124. Longest Well-Performing Interval"
date: 2025-10-16 15:04:54 -0700
categories: leetcode algorithm medium cpp hash-map prefix-sum problem-solving
---
We are given `hours`, a list of the number of hours worked per day for a given employee.

A day is considered to be a **tiring day** if and only if the number of hours worked is (strictly) greater than 8.

A **well-performing interval** is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

## Examples

**Example 1:**
```
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
```

**Example 2:**
```
Input: hours = [6,6,6]
Output: 0
Explanation: All intervals have more non-tiring days than tiring days.
```

## Constraints

- `1 <= hours.length <= 10^4`
- `0 <= hours[i] <= 16`

## Thinking Process

1. **Prefix Sum Transformation:** Convert to binary scoring system

- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Intervals on timeline</text>

  <line x1="30" y1="60" x2="250" y2="60" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="50" y="48" width="60" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="100" y="48" width="50" height="24" rx="3" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="160" y="48" width="70" height="24" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="95" text-anchor="middle" font-size="11" fill="#6B6560">sort by start → scan overlaps</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute force** *(this problem)* | Often $O(n^2)$ or $O(2^n)$ | $O(n)$ | Baseline; clarifies the optimization target |
| Sort + scan | $O(n \log n)$ | $O(1)$ | Pairs, intervals, greedy ordering |
| Hash map / set | $O(n)$ | $O(n)$ | Frequency, membership, two-sum style |
| Single-pass linear | $O(n)$ | $O(1)$ | Two pointers, sliding window, Kadane |

## Solution

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Use a hash map to track the first occurrence of each prefix sum and find the longest interval where tiring days > non-tiring days.

```cpp
class Solution {
public:
    int longestWPI(vector<int>& hours) {
        unordered_map<int, int> seen;
        int score = 0, res = 0;
        
        for(int i = 0; i < (int)hours.size(); i++) {
            if(hours[i] > 8) score++;
            else score--;
            
            if(score > 0) res = i + 1;
            else if (seen.contains(score - 1)) res = max(res, i - seen[score - 1]);
            
            if(!seen.contains(score)) seen[score] = i;
        }
        
        return res;
    }
};
```

### Solution Explanation

**Approach:** Brute force (this problem)

**Key idea:** 1. **Prefix Sum Transformation:** Convert to binary scoring system

**How the code works:**
1. **Prefix Sum Transformation:** Convert to binary scoring system
- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.

**Walkthrough** — input `hours = [9,9,6,0,6,6,9]`, expected output `3`:

The longest well-performing interval is [9,9,6].

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Prefix Sum Array | O(n²) | O(n) |
| Hash Map (Optimal) | O(n) | O(n) |
## Algorithm Breakdown

### 1. Score Calculation
```cpp
if(hours[i] > 8) score++;
else score--;
```

**Transformation:**
- `hours[i] > 8` → `+1` (tiring day)
- `hours[i] ≤ 8` → `-1` (non-tiring day)

### 2. Direct Positive Sum Check
```cpp
if(score > 0) res = i + 1;
```

**Why this works:**
- If `score > 0`, the entire interval from start to current position is well-performing
- Length = `i + 1` (0-indexed to 1-indexed conversion)

### 3. Hash Map Lookup
```cpp
else if (seen.contains(score - 1)) res = max(res, i - seen[score - 1]);
```

**Mathematical reasoning:**
- We want `prefix[j] - prefix[i] > 0`
- If current `score = k`, we look for `score - 1 = k - 1`
- This ensures `prefix[j] - prefix[k-1] = k - (k-1) = 1 > 0`

### 4. Hash Map Update
```cpp
if(!seen.contains(score)) seen[score] = i;
```

**Why only store first occurrence:**
- We want the longest interval
- First occurrence gives us the earliest starting point
- Later occurrences would give shorter intervals

### Complexity
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Prefix Sum Array | O(n²) | O(n) |
| Hash Map (Optimal) | O(n) | O(n) |

## Common Mistakes

1. **All tiring days:** `hours = [9,9,9]` → `3`
2. **All non-tiring days:** `hours = [6,6,6]` → `0`
3. **Single element:** `hours = [9]` → `1`
4. **Mixed but no valid interval:** `hours = [6,6,9]` → `1`

1. **Wrong score calculation:** Not handling the binary transformation correctly
2. **Incorrect hash map lookup:** Looking for wrong score value
3. **Missing edge case:** Not handling `score > 0` directly
4. **Wrong interval length:** Off-by-one errors in length calculation

## Detailed Example Walkthrough

### Example: `hours = [9,9,6,0,6,6,9]`

```
Step 0: i=0, hours[0]=9, score=1, seen={}, res=0
- score > 0 → res = 1
- seen[1] = 0
- seen = {1: 0}

Step 1: i=1, hours[1]=9, score=2, seen={1: 0}, res=1  
- score > 0 → res = 2
- seen[2] = 1
- seen = {1: 0, 2: 1}

Step 2: i=2, hours[2]=6, score=1, seen={1: 0, 2: 1}, res=2
- score > 0 → res = 3
- seen[1] already exists, skip
- seen = {1: 0, 2: 1}

Step 3: i=3, hours[3]=0, score=0, seen={1: 0, 2: 1}, res=3
- score = 0, check seen[0-1] = seen[-1] → not found
- seen[0] = 3
- seen = {1: 0, 2: 1, 0: 3}

Step 4: i=4, hours[4]=6, score=-1, seen={1: 0, 2: 1, 0: 3}, res=3
- score < 0, check seen[-1-1] = seen[-2] → not found
- seen[-1] = 4
- seen = {1: 0, 2: 1, 0: 3, -1: 4}

Step 5: i=5, hours[5]=6, score=-2, seen={1: 0, 2: 1, 0: 3, -1: 4}, res=3
- score < 0, check seen[-2-1] = seen[-3] → not found
- seen[-2] = 5
- seen = {1: 0, 2: 1, 0: 3, -1: 4, -2: 5}

Step 6: i=6, hours[6]=9, score=-1, seen={1: 0, 2: 1, 0: 3, -1: 4, -2: 5}, res=3
- score < 0, check seen[-1-1] = seen[-2] → found at index 5
- res = max(3, 6-5) = max(3, 1) = 3
- seen[-1] already exists, skip
- seen = {1: 0, 2: 1, 0: 3, -1: 4, -2: 5}

Final result: 3
```

## Related Problems

- [560. Subarray Sum Equals K](https://www.leetcode.com/problems/subarray-sum-equals-k/)
- [974. Subarray Sums Divisible by K](https://www.leetcode.com/problems/subarray-sums-divisible-by-k/)
- [325. Maximum Size Subarray Sum Equals k](https://www.leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
- [209. Minimum Size Subarray Sum](https://www.leetcode.com/problems/minimum-size-subarray-sum/)

## Why This Solution is Optimal

1. **Single Pass:** Each element processed exactly once
2. **Hash Map Lookup:** O(1) average case for score lookup
3. **Mathematical Insight:** Elegant transformation to prefix sum problem
4. **Space Efficient:** Only stores necessary prefix sum positions

## References

- [LC 1124: Longest Well-Performing Interval on LeetCode](https://www.leetcode.com/problems/longest-well-performing-interval/)
- [LeetCode Discuss — LC 1124: Longest Well-Performing Interval](https://www.leetcode.com/problems/longest-well-performing-interval/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/longest-well-performing-interval/editorial/) *(may require premium)*

## Key Takeaways

1. **Prefix Sum Transformation:** Convert to binary scoring system
2. **Hash Map Optimization:** Store first occurrence for longest interval
3. **Mathematical Insight:** Look for `score - 1` to ensure positive difference
4. **Single Pass:** Process each element exactly once
