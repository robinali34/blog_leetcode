---
layout: post
title: "131. Palindrome Partitioning"
categories: leetcode algorithm backtracking
tags: [leetcode, medium, backtracking, palindrome, string]
---

# 131. Palindrome Partitioning

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
