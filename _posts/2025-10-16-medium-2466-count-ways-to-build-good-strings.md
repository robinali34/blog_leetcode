---
layout: post
title: "[Medium] 2466. Count Ways To Build Good Strings"
date: 2025-10-16 20:01:57 -0700
categories: leetcode algorithm medium cpp dynamic-programming dp problem-solving
---
Given the integers `zero`, `one`, `low`, and `high`, we can construct a string by starting with an empty string, and then at each step perform either of the following:

- Append the character `'0'` `zero` times.
- Append the character `'1'` `one` times.

This can be performed any number of times.

A **good string** is a string constructed by the above process having a **length** between `low` and `high` (inclusive).

Return the number of different **good strings** you can construct satisfying these properties. Since the answer can be large, return it **modulo** `10^9 + 7`.

## Examples

**Example 1:**
```
Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
```

**Example 2:**
```
Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".
```

## Constraints

- `1 <= low <= high <= 10^5`
- `1 <= zero, one <= high`

## Thinking Process

1. **DP State:** `dp[i]` = number of ways to build string of length `i`

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
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

## Solution

**Time Complexity:** O(high)  
**Space Complexity:** O(high)

Use bottom-up DP to calculate the number of ways to build strings of each length.

```cpp
class Solution {
private:
    vector<int> dp;
    const int MOD = 1e9 + 7;
    
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        dp.resize(high + 1, 0);
        dp[0] = 1;  // Base case: empty string
        
        for(int i = 1; i <= high; i++) {
            if(i - zero >= 0) dp[i] = (dp[i] + dp[i - zero]) % MOD;
            if(i - one >= 0) dp[i] = (dp[i] + dp[i - one]) % MOD;
        }
        
        int rtn = 0;
        for(int i = low; i <= high; i++) {
            rtn = (rtn + dp[i]) % MOD;
        }
        
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** 1. **DP State:** `dp[i]` = number of ways to build string of length `i`

**How the code works:**
1. **DP State:** `dp[i]` = number of ways to build string of length `i`
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `low = 3, high = 3, zero = 1, one = 1`, expected output `8`:

One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Bottom-Up DP | O(high) | O(high) |
| Top-Down DP | O(high) | O(high) |
## Algorithm Breakdown

### Solution 1: Bottom-Up DP

```cpp
dp.resize(high + 1, 0);
dp[0] = 1;  // Base case

for(int i = 1; i <= high; i++) {
    if(i - zero >= 0) dp[i] = (dp[i] + dp[i - zero]) % MOD;
    if(i - one >= 0) dp[i] = (dp[i] + dp[i - one]) % MOD;
}
```

**Process:**
1. Initialize DP array with size `high + 1`
2. Set base case: `dp[0] = 1`
3. For each length `i`, add ways from `i - zero` and `i - one`
4. Sum all valid lengths from `low` to `high`

### Solution 2: Top-Down DP (Memoization)

```cpp
int dfs(int zero, int one, int end) {
    if(dp[end] != -1) return dp[end];  // Memoization check
    
    int cnt = 0;
    if(end >= one) cnt = (cnt + dfs(zero, one, end - one)) % MOD;
    if(end >= zero) cnt = (cnt + dfs(zero, one, end - zero)) % MOD;
    
    dp[end] = cnt;  // Store result
    return dp[end];
}
```

**Process:**
1. Initialize DP array with `-1` (unvisited)
2. Set base case: `dp[0] = 1`
3. For each length, recursively calculate using memoization
4. Sum all valid lengths from `low` to `high`

### Complexity
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Bottom-Up DP | O(high) | O(high) |
| Top-Down DP | O(high) | O(high) |

## Common Mistakes

1. **Single length range:** `low = high = 1` → Check if `zero = 1` or `one = 1`
2. **Large values:** `high = 10^5` → Use modulo arithmetic
3. **Equal zero and one:** `zero = one = 1` → Standard binary strings
4. **Different zero and one:** `zero = 1, one = 2` → Mixed length increments

1. **Missing base case:** Forgetting `dp[0] = 1`
2. **Wrong recurrence:** Not checking bounds `i - zero >= 0`
3. **Modulo errors:** Not applying modulo consistently
4. **Index bounds:** Accessing `dp[i]` without checking bounds

## Detailed Example Walkthrough

### Example: `low = 2, high = 3, zero = 1, one = 2`

**Bottom-Up DP:**

```
Step 1: Initialize
dp = [1, 0, 0, 0]

Step 2: Calculate dp[1]
i = 1, zero = 1, one = 2
- i - zero = 0 >= 0 → dp[1] += dp[0] = 1
- i - one = -1 < 0 → skip
dp = [1, 1, 0, 0]

Step 3: Calculate dp[2]
i = 2, zero = 1, one = 2
- i - zero = 1 >= 0 → dp[2] += dp[1] = 1
- i - one = 0 >= 0 → dp[2] += dp[0] = 1
dp = [1, 1, 2, 0]

Step 4: Calculate dp[3]
i = 3, zero = 1, one = 2
- i - zero = 2 >= 0 → dp[3] += dp[2] = 2
- i - one = 1 >= 0 → dp[3] += dp[1] = 1
dp = [1, 1, 2, 3]

Step 5: Sum from low to high
Sum = dp[2] + dp[3] = 2 + 3 = 5
```

**Top-Down DP:**

```
dfs(1, 2, 2):
- dp[2] = -1, calculate
- dfs(1, 2, 1) + dfs(1, 2, 0) = 1 + 1 = 2
- dp[2] = 2

dfs(1, 2, 3):
- dp[3] = -1, calculate  
- dfs(1, 2, 2) + dfs(1, 2, 1) = 2 + 1 = 3
- dp[3] = 3

Sum = dp[2] + dp[3] = 2 + 3 = 5
```

## Related Problems

- [70. Climbing Stairs](https://www.leetcode.com/problems/climbing-stairs/)
- [322. Coin Change](https://www.leetcode.com/problems/coin-change/)
- [377. Combination Sum IV](https://www.leetcode.com/problems/combination-sum-iv/)
- [139. Word Break](https://www.leetcode.com/problems/word-break/)

## Why These Solutions are Optimal

1. **Optimal Time Complexity:** O(high) is the best possible
2. **Space Efficient:** O(high) space usage
3. **Mathematical Insight:** Converts problem to counting paths
4. **Modulo Handling:** Properly handles large numbers
5. **Two Approaches:** Both bottom-up and top-down are valid

## References

- [LC 2466: Count Ways To Build Good Strings on LeetCode](https://www.leetcode.com/problems/count-ways-to-build-good-strings/)
- [LeetCode Discuss — LC 2466: Count Ways To Build Good Strings](https://www.leetcode.com/problems/count-ways-to-build-good-strings/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/count-ways-to-build-good-strings/editorial/) *(may require premium)*

## Key Takeaways

1. **DP State:** `dp[i]` = number of ways to build string of length `i`
2. **Recurrence:** Add ways from previous valid lengths
3. **Base Case:** Empty string has 1 way
4. **Modulo:** Handle large numbers with `10^9 + 7`
