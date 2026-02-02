---
layout: post
title: "44. Wildcard Matching"
date: 2026-02-01 00:00:00 -0700
categories: [leetcode, hard, string, dynamic-programming, greedy, two-pointers]
permalink: /2026/02/01/hard-44-wildcard-matching/
tags: [leetcode, hard, string, dynamic-programming, greedy, two-pointers]
---

# 44. Wildcard Matching

## Problem Statement

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'` where:

- `'?'` Matches any single character.
- `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

## Examples

**Example 1:**

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**

```
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
```

**Example 3:**

```
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

**Example 4:**

```
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, and the second '*' matches the substring "dce".
```

**Example 5:**

```
Input: s = "acdcb", p = "a*c?b"
Output: false
```

## Constraints

- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'?'` or `'*'`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Pattern matching scope**: Should the pattern match the entire string or just a substring? (Assumption: The pattern must match the entire input string, not just a substring)

2. **Wildcard behavior**: What does `'*'` match? (Assumption: `'*'` matches any sequence of characters, including the empty sequence - it can match zero or more characters)

3. **Single character match**: What does `'?'` match? (Assumption: `'?'` matches exactly one character - any single character)

4. **Multiple stars**: Can the pattern contain multiple `'*'` characters? (Assumption: Yes - multiple stars are allowed and each can match independently)

5. **Empty string**: What should we return for empty string and empty pattern? (Assumption: Empty pattern matches empty string only - return true if both are empty, false otherwise)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

Use recursion with backtracking. For each position, if pattern character is `'?'` or matches string character, advance both pointers. If pattern character is `'*'`, try matching zero, one, two, ... characters. This approach has exponential time complexity O(2^(m+n)) in worst case due to backtracking.

**Step 2: Semi-Optimized Approach (10 minutes)**

Use dynamic programming with memoization. Create a 2D DP table where `dp[i][j]` represents whether `s[0..i-1]` matches `p[0..j-1]`. Handle three cases: exact match or `'?'`, `'*'` matching zero or more characters. This reduces time complexity to O(m*n) with O(m*n) space.

**Step 3: Optimized Solution (12 minutes)**

Use a greedy two-pointer approach. When encountering `'*'`, record its position and the current string position. Try matching as few characters as possible with `'*'`, and if a mismatch occurs later, backtrack to the last `'*'` and let it match one more character. This achieves O(m*n) worst case but O(m+n) average case, with O(1) space complexity.

## Solution Approach

This problem is similar to regular expression matching but simpler. The key challenge is handling `'*'` which can match any sequence of characters.

### Key Insights:

1. **Greedy Matching**: For `'*'`, try matching as few characters as possible first
2. **Backtracking**: If a mismatch occurs after `'*'`, backtrack and let `'*'` match one more character
3. **Two Pointers**: Use two pointers to track current positions in string and pattern
4. **Star Tracking**: Keep track of the last `'*'` position and the string position after it

## Solution 1: Regex-Based Approach

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty()) return s.empty();

        string pat = "^";
        for(char c: p){
            if(c == '?') pat += '.';
            else if (c == '*') pat += ".*";
            else pat += c;
        }
        pat.push_back('$');
        return regex_search(s, regex(pat));
    }
};
```

### Algorithm Breakdown:

1. **Pattern Conversion**: Convert wildcard pattern to regex pattern
   - `'?'` → `'.'` (matches any single character in regex)
   - `'*'` → `".*"` (matches any sequence in regex)
   - Regular characters remain unchanged
2. **Anchoring**: Add `'^'` at start and `'$'` at end to ensure full string match
3. **Regex Search**: Use `regex_search` to check if the entire string matches the pattern

### Why This Works:

- **Regex Equivalence**: Wildcard matching is equivalent to regex matching with specific conversions
- **Full Match**: The `^` and `$` anchors ensure the pattern matches the entire string
- **Simple Implementation**: Leverages built-in regex functionality

### Complexity Analysis:

- **Time Complexity**: O(m*n) - Regex matching typically has this complexity
- **Space Complexity**: O(m) - For the converted pattern string

## Solution 2: Two-Pointer Greedy Approach

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0;
        int lastStar = -1, matchAfterStar = -1;
        const int M = s.size(), N = p.size();
        while(i < M) {
            if(j < N && (p[j] == s[i] || p[j] == '?')) {
                i++;
                j++;
            } else if(j < N && p[j] == '*') {
                lastStar = j;
                matchAfterStar = i;
                j++;
            } else if(lastStar != -1) {
                j = lastStar + 1; // Reset pattern after '*'
                matchAfterStar++; // let '*' match one more character
                i = matchAfterStar;
            } else {
                // Mismatch with no previous '*'
                return false;
            }
        }
        while(j < N && p[j] == '*') j++;
        return j == N;
    }
};
```

## Solution 3: Recursion with Memoization

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<int>> memo(m + 1, vector<int>(n + 1, -1));
        return dfs(s, p, 0, 0, memo);
    }

private:
    bool dfs(const string& s, const string& p, int i, int j, vector<vector<int>>& memo) {
        // Base cases
        if (j == p.size()) {
            return i == s.size();
        }
        if (i == s.size()) {
            // If string is exhausted, pattern must be all '*' to match
            for (int k = j; k < p.size(); k++) {
                if (p[k] != '*') return false;
            }
            return true;
        }

        // Check memoization
        if (memo[i][j] != -1) {
            return memo[i][j] == 1;
        }

        bool result = false;

        if (p[j] == '*') {
            // '*' can match zero or more characters
            // Option 1: Match zero characters (skip '*')
            // Option 2: Match one or more characters (consume one character from string)
            result = dfs(s, p, i, j + 1, memo) ||      // Match zero
                     dfs(s, p, i + 1, j, memo);       // Match one or more
        } else if (p[j] == '?' || s[i] == p[j]) {
            // '?' matches any single character, or characters match
            result = dfs(s, p, i + 1, j + 1, memo);
        } else {
            // Characters don't match
            result = false;
        }

        memo[i][j] = result ? 1 : 0;
        return result;
    }
};
```

### Algorithm Breakdown:

1. **Memoization Table**: `memo[i][j]` stores whether `s[i..]` matches `p[j..]`
   - `-1`: Not computed yet
   - `0`: False (doesn't match)
   - `1`: True (matches)

2. **Base Cases**:
   - If pattern is exhausted: return true only if string is also exhausted
   - If string is exhausted: pattern must be all `'*'` to match (empty sequence)

3. **Recursive Cases**:
   - If `p[j] == '*'`: Try matching zero characters (skip `'*'`) or one or more characters (consume one from string)
   - If `p[j] == '?'` or `s[i] == p[j]`: Both pointers advance
   - Otherwise: Mismatch, return false

4. **Memoization**: Store and reuse computed results to avoid redundant calculations

### Why This Works:

- **Exhaustive Search**: Explores all possible ways `'*'` can match
- **Memoization**: Avoids recomputing the same subproblems
- **Clear Logic**: Recursive structure makes the matching logic explicit

### Complexity Analysis:

- **Time Complexity**: O(m*n) - Each (i, j) pair is computed at most once
- **Space Complexity**: O(m*n) - For the memoization table and recursion stack

## Solution 4: Dynamic Programming (Bottom-Up)

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        // Base case: empty string matches empty pattern
        dp[0][0] = true;

        // Handle patterns starting with '*' (can match empty string)
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }

        // Fill the DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '*') {
                    // '*' can match zero or more characters
                    // Option 1: Match zero characters (dp[i][j-1])
                    // Option 2: Match one or more characters (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                } else if (p[j - 1] == '?' || s[i - 1] == p[j - 1]) {
                    // '?' matches any character, or characters match
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Characters don't match
                    dp[i][j] = false;
                }
            }
        }

        return dp[m][n];
    }
};
```

### Algorithm Breakdown:

1. **DP State**: `dp[i][j]` represents whether `s[0..i-1]` matches `p[0..j-1]`

2. **Base Cases**:
   - `dp[0][0] = true`: Empty string matches empty pattern
   - For `dp[0][j]`: Pattern starting with `'*'` can match empty string

3. **Transition**:
   - If `p[j-1] == '*'`: 
     - Match zero: `dp[i][j-1]` (skip `'*'`)
     - Match one or more: `dp[i-1][j]` (consume one character, keep `'*'`)
   - If `p[j-1] == '?'` or `s[i-1] == p[j-1]`: 
     - Both advance: `dp[i-1][j-1]`
   - Otherwise: `false`

4. **Result**: `dp[m][n]` indicates if entire string matches entire pattern

### Why This Works:

- **Bottom-Up Approach**: Builds solution from smaller subproblems
- **Systematic**: Processes all subproblems in order
- **Space Optimization Possible**: Can optimize to O(n) space since we only need previous row

### Complexity Analysis:

- **Time Complexity**: O(m*n) - Fill a 2D table of size m×n
- **Space Complexity**: O(m*n) - For the DP table (can be optimized to O(n))

### Space-Optimized DP (O(n) space):

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<bool> prev(n + 1, false);
        vector<bool> curr(n + 1, false);

        // Base case: empty string matches empty pattern
        prev[0] = true;

        // Handle patterns starting with '*'
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                prev[j] = prev[j - 1];
            }
        }

        // Fill the DP table
        for (int i = 1; i <= m; i++) {
            curr[0] = false; // Non-empty string doesn't match empty pattern
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '*') {
                    curr[j] = curr[j - 1] || prev[j];
                } else if (p[j - 1] == '?' || s[i - 1] == p[j - 1]) {
                    curr[j] = prev[j - 1];
                } else {
                    curr[j] = false;
                }
            }
            prev = curr;
        }

        return prev[n];
    }
};
```

### Algorithm Breakdown:

1. **Two Pointers**: `i` tracks position in string `s`, `j` tracks position in pattern `p`
2. **Star Tracking**: 
   - `lastStar`: Position of the last `'*'` encountered
   - `matchAfterStar`: Position in string where we started matching after the last `'*'`
3. **Matching Logic**:
   - If characters match or pattern has `'?'`: advance both pointers
   - If pattern has `'*'`: record its position, try matching zero characters first (advance pattern pointer only)
   - If mismatch occurs: backtrack to last `'*'`, let it match one more character, and retry
4. **Final Check**: After processing all string characters, skip any remaining `'*'` in pattern and check if we've consumed the entire pattern

### Why This Works:

- **Greedy Strategy**: Try matching as few characters as possible with `'*'` first
- **Backtracking**: When a mismatch occurs, backtrack to the last `'*'` and expand its match
- **Efficient**: Avoids exponential backtracking by only backtracking to the last `'*'`

### Sample Test Case Run:

**Input:** `s = "adceb"`, `p = "*a*b"`

```
Initial: i = 0, j = 0, lastStar = -1, matchAfterStar = -1

Iteration 1:
  p[0] = '*', s[0] = 'a'
  Encounter '*', record position
  lastStar = 0, matchAfterStar = 0
  j = 1 (try matching zero characters with '*')
  State: i = 0, j = 1

Iteration 2:
  p[1] = 'a', s[0] = 'a'
  Characters match ✓
  i = 1, j = 2
  State: i = 1, j = 2

Iteration 3:
  p[2] = '*', s[1] = 'd'
  Encounter '*', record position
  lastStar = 2, matchAfterStar = 1
  j = 3 (try matching zero characters with '*')
  State: i = 1, j = 3

Iteration 4:
  p[3] = 'b', s[1] = 'd'
  Mismatch! Backtrack to last '*'
  j = lastStar + 1 = 3
  matchAfterStar = 2 (let '*' match one more character)
  i = matchAfterStar = 2
  State: i = 2, j = 3

Iteration 5:
  p[3] = 'b', s[2] = 'c'
  Mismatch! Backtrack to last '*'
  j = lastStar + 1 = 3
  matchAfterStar = 3 (let '*' match one more character)
  i = matchAfterStar = 3
  State: i = 3, j = 3

Iteration 6:
  p[3] = 'b', s[3] = 'e'
  Mismatch! Backtrack to last '*'
  j = lastStar + 1 = 3
  matchAfterStar = 4 (let '*' match one more character)
  i = matchAfterStar = 4
  State: i = 4, j = 3

Iteration 7:
  p[3] = 'b', s[4] = 'b'
  Characters match ✓
  i = 5, j = 4
  State: i = 5, j = 4

Loop condition: i (5) < M (5) is false, exit loop

Final check:
  j = 4, N = 4
  j == N ✓

Return: true ✓
```

**Verification:**
- `'*'` at position 0 matches empty sequence (or "a")
- `'a'` matches `'a'` at position 0
- `'*'` at position 2 matches "dce"
- `'b'` matches `'b'` at position 4
- Entire string matched ✓

**Output:** `true` ✓

---

**Another Example:** `s = "acdcb"`, `p = "a*c?b"`

```
Initial: i = 0, j = 0, lastStar = -1, matchAfterStar = -1

Iteration 1:
  p[0] = 'a', s[0] = 'a'
  Characters match ✓
  i = 1, j = 1
  State: i = 1, j = 1

Iteration 2:
  p[1] = '*', s[1] = 'c'
  Encounter '*', record position
  lastStar = 1, matchAfterStar = 1
  j = 2 (try matching zero characters with '*')
  State: i = 1, j = 2

Iteration 3:
  p[2] = 'c', s[1] = 'c'
  Characters match ✓
  i = 2, j = 3
  State: i = 2, j = 3

Iteration 4:
  p[3] = '?', s[2] = 'd'
  '?' matches any character ✓
  i = 3, j = 4
  State: i = 3, j = 4

Iteration 5:
  p[4] = 'b', s[3] = 'c'
  Mismatch! Backtrack to last '*'
  j = lastStar + 1 = 2
  matchAfterStar = 2 (let '*' match one more character)
  i = matchAfterStar = 2
  State: i = 2, j = 2

Iteration 6:
  p[2] = 'c', s[2] = 'd'
  Mismatch! Backtrack to last '*'
  j = lastStar + 1 = 2
  matchAfterStar = 3 (let '*' match one more character)
  i = matchAfterStar = 3
  State: i = 3, j = 2

Iteration 7:
  p[2] = 'c', s[3] = 'c'
  Characters match ✓
  i = 4, j = 3
  State: i = 4, j = 3

Iteration 8:
  p[3] = '?', s[4] = 'b'
  '?' matches any character ✓
  i = 5, j = 4
  State: i = 5, j = 4

Loop condition: i (5) < M (5) is false, exit loop

Final check:
  j = 4, N = 5
  j != N ✗

Return: false ✓
```

**Verification:**
- Pattern requires 5 characters: `'a'`, `'*'`, `'c'`, `'?'`, `'b'`
- String has 5 characters: `"acdcb"`
- After matching, pattern pointer is at position 4, but pattern length is 5
- Pattern not fully consumed ✗

**Output:** `false` ✓

---

**Edge Case:** `s = "aa"`, `p = "*"`

```
Initial: i = 0, j = 0, lastStar = -1, matchAfterStar = -1

Iteration 1:
  p[0] = '*', s[0] = 'a'
  Encounter '*', record position
  lastStar = 0, matchAfterStar = 0
  j = 1 (try matching zero characters with '*')
  State: i = 0, j = 1

Loop condition: i (0) < M (2) is true, continue

Iteration 2:
  j (1) >= N (1), but i (0) < M (2)
  lastStar != -1, backtrack
  j = lastStar + 1 = 1
  matchAfterStar = 1 (let '*' match one more character)
  i = matchAfterStar = 1
  State: i = 1, j = 1

Loop condition: i (1) < M (2) is true, continue

Iteration 3:
  j (1) >= N (1), but i (1) < M (2)
  lastStar != -1, backtrack
  j = lastStar + 1 = 1
  matchAfterStar = 2 (let '*' match one more character)
  i = matchAfterStar = 2
  State: i = 2, j = 1

Loop condition: i (2) < M (2) is false, exit loop

Final check:
  j = 1, N = 1
  j == N ✓

Return: true ✓
```

**Verification:**
- `'*'` matches any sequence, including "aa" ✓
- Entire string matched ✓

**Output:** `true` ✓

## Complexity Analysis

### Solution 1 (Regex):
- **Time Complexity**: O(m*n) - Regex matching typically has this complexity
- **Space Complexity**: O(m) - For the converted pattern string

### Solution 2 (Two-Pointer Greedy):
- **Time Complexity**: O(m*n) worst case, O(m+n) average case - In worst case, we may backtrack for each character
- **Space Complexity**: O(1) - Only using a constant amount of extra space

### Solution 3 (Recursion with Memoization):
- **Time Complexity**: O(m*n) - Each (i, j) pair is computed at most once
- **Space Complexity**: O(m*n) - For the memoization table and recursion stack

### Solution 4 (Dynamic Programming):
- **Time Complexity**: O(m*n) - Fill a 2D table of size m×n
- **Space Complexity**: O(m*n) - For the DP table (can be optimized to O(n) with space-optimized version)

## Key Insights

1. **Greedy Strategy**: Try matching as few characters as possible with `'*'` first, then expand if needed
2. **Backtracking**: When a mismatch occurs, backtrack to the last `'*'` and let it match one more character
3. **Star Consolidation**: Multiple consecutive `'*'` can be treated as a single `'*'`
4. **Pattern Completion**: After processing the string, skip any remaining `'*'` and check if pattern is fully consumed
5. **Regex Alternative**: For simplicity, can convert wildcard pattern to regex pattern, though less efficient
6. **DP State Definition**: `dp[i][j]` = whether `s[0..i-1]` matches `p[0..j-1]`
7. **Star Matching**: `'*'` can match zero characters (`dp[i][j-1]`) or one or more characters (`dp[i-1][j]`)
8. **Memoization**: Recursive approach with memoization avoids recomputing the same subproblems

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Regex | O(m*n) | O(m) | Simple but uses regex library |
| Two-Pointer Greedy | O(m*n) worst, O(m+n) avg | O(1) | Most space-efficient, best for large inputs |
| Recursion with Memoization | O(m*n) | O(m*n) | Clear recursive logic, easy to understand |
| Dynamic Programming | O(m*n) | O(m*n) or O(n) | Systematic bottom-up approach, can optimize space |

## Related Problems

- [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) - Similar problem with more complex patterns
- [72. Edit Distance](https://leetcode.com/problems/edit-distance/) - Dynamic programming with string matching
- [97. Interleaving String](https://leetcode.com/problems/interleaving-string/) - String matching with constraints
- [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) - Pattern matching with counting
