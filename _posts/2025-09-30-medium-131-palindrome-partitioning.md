---
layout: post
title: "[Medium] 131. Palindrome Partitioning"
date: 2025-09-30 00:00:00 -0000
categories: leetcode algorithm backtracking data-structures string palindrome recursion medium cpp partitioning problem-solving
---
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

## Thinking Process

The solution uses backtracking (DFS) with the following strategy:

1. **Base Case**: When we've processed the entire string, add the current partition to results
2. **Recursive Case**: For each possible end position, check if substring is palindrome
3. **Backtrack**: If palindrome, add to current partition and recurse, then remove
4. **Palindrome Check**: Verify if substring from start to end is a palindrome



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Backtracking tree</text>

  <circle cx="140" cy="30" r="12" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="34" text-anchor="middle" font-size="9">start</text>
  <line x1="140" y1="42" x2="90" y2="65" stroke="#9A9792"/><line x1="140" y1="42" x2="190" y2="65" stroke="#9A9792"/>
  <circle cx="90" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/><circle cx="190" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/>
  <line x1="90" y1="82" x2="60" y2="100" stroke="#9A9792" stroke-dasharray="3"/><line x1="190" y1="82" x2="220" y2="100" stroke="#9A9792" stroke-dasharray="3"/>
  <text x="140" y="118" text-anchor="middle" font-size="11" fill="#6B6560">choose → explore → undo (prune)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Choose / explore / unchoose** *(this problem)* | $O(2^n)$ | $O(n)$ | Subsets, combinations |
| Constraint pruning | Reduced search | $O(n)$ | Early exit on invalid partial |
| Sort + skip duplicates | $O(2^n)$ | $O(n)$ | Combination sum II style |
| Path recording | $O(n!)$ worst | $O(n)$ | Permutations |

## Solution
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

### Solution Explanation

**Approach:** Choose / explore / unchoose (this problem)

**Key idea:** The solution uses backtracking (DFS) with the following strategy:

**How the code works:**
1. **Base Case**: When we've processed the entire string, add the current partition to results
2. **Recursive Case**: For each possible end position, check if substring is palindrome
3. **Backtrack**: If palindrome, add to current partition and recurse, then remove
4. **Palindrome Check**: Verify if substring from start to end is a palindrome

**Walkthrough** — input `s = "aab"`, expected output `[["a","a","b"],["aa","b"]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
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

## Common Mistakes

1. **Forgetting to backtrack**: Not removing elements after recursion
2. **Index errors**: Off-by-one errors in substring extraction
3. **Inefficient palindrome check**: Creating unnecessary string copies
4. **Missing base case**: Not handling empty string or single character
5. **Duplicate results**: Not properly managing the current partition

## Related Problems

- [132. Palindrome Partitioning II](https://www.leetcode.com/problems/palindrome-partitioning-ii/) - Minimum cuts
- [5. Longest Palindromic Substring](https://www.leetcode.com/problems/longest-palindromic-substring/)
- [647. Palindromic Substrings](https://www.leetcode.com/problems/palindromic-substrings/)
- [93. Restore IP Addresses](https://www.leetcode.com/problems/restore-ip-addresses/) - Similar partitioning pattern

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

## References

- [LC 131: Palindrome Partitioning on LeetCode](https://www.leetcode.com/problems/palindrome-partitioning/)
- [LeetCode Discuss — LC 131: Palindrome Partitioning](https://www.leetcode.com/problems/palindrome-partitioning/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/palindrome-partitioning/editorial/) *(may require premium)*

## Key Takeaways

1. **Backtracking Pattern**: Add → Recurse → Remove
2. **Palindrome Check**: Verify each substring before adding to partition
3. **Index Management**: Use start and end indices to define substrings
4. **Base Case**: When start >= string length, we have a complete partition
5. **Pruning**: Only recurse if current substring is a palindrome
