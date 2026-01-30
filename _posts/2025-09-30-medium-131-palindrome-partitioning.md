---
layout: post
title: "[Medium] 131. Palindrome Partitioning"
date: 2025-09-30 00:00:00 -0000
categories: leetcode algorithm backtracking data-structures string palindrome recursion medium cpp partitioning problem-solving
---

# [Medium] 131. Palindrome Partitioning

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

## Examples

**Example 1:**
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2:**
```
Input: s = "a"
Output: [["a"]]
```

## Constraints

- 1 <= s.length <= 16
- s contains only lowercase English letters

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Partition definition**: What is a palindrome partition? (Assumption: Split string into substrings where each substring is a palindrome)

2. **Partition requirement**: Must we partition the entire string? (Assumption: Yes - use all characters, no character left out)

3. **Palindrome definition**: What makes a substring a palindrome? (Assumption: Reads same forwards and backwards - symmetric string)

4. **Output format**: Should we return all partitions or just count? (Assumption: Return all possible palindrome partitions - list of lists)

5. **Order requirement**: Does the order of partitions matter? (Assumption: No - can return in any order)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to partition string into palindromes. Let me try all possible partitions."

**Naive Solution**: Generate all possible ways to partition string, check if each substring is palindrome, collect valid partitions.

**Complexity**: O(2^n × n) time, O(2^n × n) space

**Issues**:
- Exponential time - tries all partitions
- Repeats palindrome checking for same substrings
- Very inefficient
- Doesn't leverage memoization

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use backtracking with memoization for palindrome checking."

**Improved Solution**: Use backtracking to try all partitions. For each position, try all possible palindrome substrings starting there. Memoize palindrome checks to avoid recomputation.

**Complexity**: O(2^n × n) time worst case, O(n²) space

**Improvements**:
- Memoization reduces palindrome checking
- Backtracking explores all partitions
- Still exponential but better than brute-force
- Handles all cases correctly

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "Backtracking with memoized palindrome checking is optimal. Can optimize palindrome check with DP."

**Best Solution**: Backtracking with DP for palindrome checking. Precompute palindrome table using DP, then use backtracking to generate all valid partitions.

**Complexity**: O(2^n × n) time worst case, O(n²) space

**Key Realizations**:
1. Backtracking is natural for generating all partitions
2. DP palindrome checking optimizes repeated checks
3. O(2^n) time is inherent - exponential number of partitions
4. O(n²) space for palindrome table is acceptable

## Approach

The solution uses backtracking (DFS) with the following strategy:

1. **Base Case**: When we've processed the entire string, add the current partition to results
2. **Recursive Case**: For each possible end position, check if substring is palindrome
3. **Backtrack**: If palindrome, add to current partition and recurse, then remove
4. **Palindrome Check**: Verify if substring from start to end is a palindrome

## Solution in C++

**Time Complexity:** O(2^n × n) - Exponential due to backtracking, n for palindrome check  
**Space Complexity:** O(n) - For recursion stack and current partition

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<string> cur;
        vector<vector<string>> rtn;
        dfs(s, 0, cur, rtn);
        return rtn;
    }

private:
    void dfs(const string& str, int start, vector<string>& cur, vector<vector<string>>& rtn) {
        if(start >= str.length()) rtn.push_back(cur);
        for (int end = start; end < str.length(); end++) {
            if(isPalindrome(str, start, end)) {
                cur.push_back(str.substr(start, end - start + 1));
                dfs(str, end + 1, cur, rtn);
                cur.pop_back();
            }
        }
    }

    bool isPalindrome(const string& str, int start, int end) {
        string copy = str.substr(start, end - start + 1);
        reverse(copy.begin(), copy.end());
        return str.substr(start, end - start + 1) == copy;
    }
};
```

## Step-by-Step Example

For `s = "aab"`:

1. **Start at index 0:**
   - Check "a" (0,0): is palindrome → add to path: `["a"]`
   - Recurse with start=1

2. **Start at index 1:**
   - Check "a" (1,1): is palindrome → add to path: `["a","a"]`
   - Recurse with start=2

3. **Start at index 2:**
   - Check "b" (2,2): is palindrome → add to path: `["a","a","b"]`
   - Recurse with start=3 → base case → add `["a","a","b"]` to result

4. **Backtrack to index 1:**
   - Remove "a" from path: `["a"]`
   - Check "ab" (1,2): not palindrome → skip

5. **Backtrack to index 0:**
   - Remove "a" from path: `[]`
   - Check "aa" (0,1): is palindrome → add to path: `["aa"]`
   - Recurse with start=2

6. **Start at index 2:**
   - Check "b" (2,2): is palindrome → add to path: `["aa","b"]`
   - Recurse with start=3 → base case → add `["aa","b"]` to result

**Result:** `[["a","a","b"],["aa","b"]]`

## Key Insights

1. **Backtracking Pattern**: Add → Recurse → Remove
2. **Palindrome Check**: Verify each substring before adding to partition
3. **Index Management**: Use start and end indices to define substrings
4. **Base Case**: When start >= string length, we have a complete partition
5. **Pruning**: Only recurse if current substring is a palindrome

## Alternative Approaches

### 1. **Optimized Palindrome Check**
```cpp
bool isPalindrome(const string& str, int start, int end) {
    while (start < end) {
        if (str[start] != str[end]) return false;
        start++;
        end--;
    }
    return true;
}
```

### 2. **Precompute Palindrome Table**
```cpp
vector<vector<bool>> isPal;
// Precompute all palindrome substrings
// Time: O(n²), Space: O(n²)
```

## Common Mistakes

1. **Forgetting to backtrack**: Not removing elements after recursion
2. **Index errors**: Off-by-one errors in substring extraction
3. **Inefficient palindrome check**: Creating unnecessary string copies
4. **Missing base case**: Not handling empty string or single character
5. **Duplicate results**: Not properly managing the current partition

## Related Problems

- [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) - Minimum cuts
- [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) - Similar partitioning pattern

## Visual Representation

```
Input: "aab"

Backtracking Tree:
                    ""
                   /  \
                  "a"  "aa"
                 /      \
               "a"      "b"
              /
            "b"
           /
         [complete]

Results: ["a","a","b"] and ["aa","b"]
```

This problem demonstrates the classic backtracking pattern for generating all possible partitions with a constraint (palindrome check).
