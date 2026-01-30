---
layout: post
title: "[Medium] 2466. Count Ways To Build Good Strings"
date: 2025-10-16 20:01:57 -0700
categories: leetcode algorithm medium cpp dynamic-programming dp problem-solving
---

# [Medium] 2466. Count Ways To Build Good Strings

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Good string definition**: What is a "good string"? (Assumption: Binary string that can be built by appending "0" zero times and "1" one times - length must be between low and high)

2. **String construction**: How are strings built? (Assumption: Start with empty string, append "0" zero times or "1" one times repeatedly)

3. **Length requirement**: What length range should strings have? (Assumption: Length between low and high inclusive - [low, high])

4. **Return value**: What should we return? (Assumption: Count of ways to build good strings - integer, modulo 10^9 + 7)

5. **Empty string**: Is empty string considered? (Assumption: No - strings must have length >= low, so empty string not included)

## Solution 1: Bottom-Up Dynamic Programming

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

## Solution 2: Top-Down Dynamic Programming (Memoization)

**Time Complexity:** O(high)  
**Space Complexity:** O(high)

Use top-down DP with memoization to calculate the number of ways recursively.

```cpp
class Solution {
private:
    vector<int> dp;
    const int MOD = 1e9 + 7;

    int dfs(int zero, int one, int end) {
        if(dp[end] != -1) return dp[end];
        
        int cnt = 0;
        if(end >= one) cnt = (cnt + dfs(zero, one, end - one)) % MOD;
        if(end >= zero) cnt = (cnt + dfs(zero, one, end - zero)) % MOD;
        
        dp[end] = cnt;
        return dp[end];
    }
    
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        dp.resize(high + 1, -1);
        dp[0] = 1;  // Base case: empty string
        
        int rtn = 0;
        for(int len = low; len <= high; len++) {
            rtn = (rtn + dfs(zero, one, len)) % MOD; 
        }
        
        return rtn;
    }
};
```

## How the Algorithm Works

### Key Insight: Dynamic Programming

The problem can be solved using dynamic programming where `dp[i]` represents the number of ways to build a string of length `i`.

**Recurrence Relation:**
- `dp[i] = dp[i - zero] + dp[i - one]` (if both are valid)
- Base case: `dp[0] = 1` (empty string)

### Step-by-Step Example: `low = 2, high = 3, zero = 1, one = 2`

**Bottom-Up Approach:**

| Length | Ways to Build | Explanation |
|--------|---------------|-------------|
| 0 | 1 | Empty string (base case) |
| 1 | 1 | "0" (from length 0 + zero=1) |
| 2 | 2 | "00" (from length 1 + zero=1), "1" (from length 0 + one=2) |
| 3 | 3 | "000" (from length 2 + zero=1), "01" (from length 1 + one=2) |

**DP Table:**
```
dp = [1, 1, 2, 3]
```

**Answer:** Sum from length 2 to 3 = `dp[2] + dp[3] = 2 + 3 = 5`

### Visual Representation

```
Length 0: "" (1 way)
Length 1: "0" (1 way)
Length 2: "00", "1" (2 ways)
Length 3: "000", "01", "10" (3 ways)

Good strings (length 2-3): "00", "1", "000", "01", "10" = 5 ways
```

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

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Bottom-Up DP | O(high) | O(high) |
| Top-Down DP | O(high) | O(high) |

## Edge Cases

1. **Single length range:** `low = high = 1` → Check if `zero = 1` or `one = 1`
2. **Large values:** `high = 10^5` → Use modulo arithmetic
3. **Equal zero and one:** `zero = one = 1` → Standard binary strings
4. **Different zero and one:** `zero = 1, one = 2` → Mixed length increments

## Key Insights

1. **DP State:** `dp[i]` = number of ways to build string of length `i`
2. **Recurrence:** Add ways from previous valid lengths
3. **Base Case:** Empty string has 1 way
4. **Modulo:** Handle large numbers with `10^9 + 7`

## Common Mistakes

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

## Alternative Approaches

### Approach 1: Brute Force (DFS)
```cpp
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        return dfs(0, low, high, zero, one);
    }
    
private:
    int dfs(int len, int low, int high, int zero, int one) {
        if (len > high) return 0;
        int count = (len >= low) ? 1 : 0;
        count = (count + dfs(len + zero, low, high, zero, one)) % MOD;
        count = (count + dfs(len + one, low, high, zero, one)) % MOD;
        return count;
    }
    
    const int MOD = 1e9 + 7;
};
```

**Time Complexity:** O(2^high)  
**Space Complexity:** O(high)

### Approach 2: Mathematical Formula
```cpp
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        vector<int> dp(high + 1, 0);
        dp[0] = 1;
        
        for (int i = 1; i <= high; i++) {
            if (i >= zero) dp[i] = (dp[i] + dp[i - zero]) % MOD;
            if (i >= one) dp[i] = (dp[i] + dp[i - one]) % MOD;
        }
        
        int result = 0;
        for (int i = low; i <= high; i++) {
            result = (result + dp[i]) % MOD;
        }
        
        return result;
    }
    
private:
    const int MOD = 1e9 + 7;
};
```

## Related Problems

- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
- [139. Word Break](https://leetcode.com/problems/word-break/)

## Why These Solutions are Optimal

1. **Optimal Time Complexity:** O(high) is the best possible
2. **Space Efficient:** O(high) space usage
3. **Mathematical Insight:** Converts problem to counting paths
4. **Modulo Handling:** Properly handles large numbers
5. **Two Approaches:** Both bottom-up and top-down are valid
