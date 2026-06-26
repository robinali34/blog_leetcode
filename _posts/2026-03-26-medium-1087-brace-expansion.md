---
layout: post
title: "[Medium] 1087. Brace Expansion"
date: 2026-03-26
categories: [leetcode, medium, backtracking, string]
tags: [leetcode, medium, backtracking, string, parsing]
permalink: /2026/03/26/medium-1087-brace-expansion/
---
Given a string `s` representing a list of words, where each letter can be replaced by a group of letters inside braces `{a,b,c}`, return all possible words in **sorted** order.

For example, `"{a,b}c{d,e}f"` means the first letter can be `a` or `b`, the second is `c`, the third can be `d` or `e`, and the fourth is `f`.

## Examples

**Example 1:**

```
Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
```

**Example 2:**

```
Input: s = "abcd"
Output: ["abcd"]
```

## Constraints

- `1 <= s.length <= 50`
- `s` consists of `{`, `}`, `,`, and lowercase English letters
- `s` is guaranteed to be a valid brace expression

## Thinking Process

### Two-Phase Approach

**Phase 1: Parse** the string into a list of "groups." Each group is either:
- A single character (literal like `c`)
- A sorted list of characters (options like `{a,b}`)

**Phase 2: Backtrack** through the groups, picking one character from each, to generate all combinations.

### Why Sort Each Group?

The problem requires the output in sorted order. If we sort each group's options during parsing, then the DFS generates results in lexicographic order naturally -- no post-sort needed.

### Walk-through

```
s = "{a,b}c{d,e}f"

Parse → groups = [[a,b], [c], [d,e], [f]]

DFS tree:
  [a,b] → a → [c] → c → [d,e] → d → [f] → f → "acdf"
                                → e → [f] → f → "acef"
        → b → [c] → c → [d,e] → d → [f] → f → "bcdf"
                                → e → [f] → f → "bcef"

Output: ["acdf", "acef", "bcdf", "bcef"]
```



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

{% raw %}
```cpp
class Solution {
public:
    vector<string> expand(string s) {
        vector<vector<char>> groups;
        int n = s.size();

        for (int i = 0; i < n; ) {
            if (s[i] == '{') {
                vector<char> curr;
                i++;
                while (i < n && s[i] != '}') {
                    if (isalpha(s[i])) curr.push_back(s[i]);
                    i++;
                }
                sort(curr.begin(), curr.end());
                groups.push_back(curr);
                i++;
            } else {
                groups.push_back({s[i]});
                i++;
            }
        }

        vector<string> rtn;
        string path;
        dfs(0, groups, path, rtn);
        return rtn;
    }

private:
    void dfs(int idx, const vector<vector<char>>& groups, string& path, vector<string>& rtn) {
        if (idx == (int)groups.size()) {
            rtn.push_back(path);
            return;
        }
        for (char c : groups[idx]) {
            path.push_back(c);
            dfs(idx + 1, groups, path, rtn);
            path.pop_back();
        }
    }
};
```

### Solution Explanation

**Approach:** Choose / explore / unchoose (this problem)

**Key idea:** ### Two-Phase Approach

**How the code works:**
**Phase 1: Parse** the string into a list of "groups." Each group is either:
- A single character (literal like `c`)
- A sorted list of characters (options like `{a,b}`)
**Phase 2: Backtrack** through the groups, picking one character from each, to generate all combinations.

**Walkthrough** — input `s = "{a,b}c{d,e}f"`, expected output `["acdf","acef","bcdf","bcef"]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- Forgetting to skip commas during parsing (adding `,` as a character option)
- Not sorting groups, then needing to sort the entire output ($O(k^m \cdot m \log(k^m))$ instead of $O(k^m \cdot m)$)
- Off-by-one: not incrementing `i` past the closing `}`

## Key Takeaways

- **"Generate all combinations from groups of choices"** = backtracking over groups
- Parsing into an intermediate representation (groups) cleanly separates concerns from the combinatorial generation
- Sorting inputs early often eliminates the need to sort outputs

## Related Problems

- [17. Letter Combinations of a Phone Number](https://www.leetcode.com/problems/letter-combinations-of-a-phone-number/) -- same pattern: groups of choices → backtrack
- [78. Subsets](https://www.leetcode.com/problems/subsets/) -- backtracking enumeration
- [22. Generate Parentheses](https://www.leetcode.com/problems/generate-parentheses/) -- constrained backtracking
- [394. Decode String](https://www.leetcode.com/problems/decode-string/) -- string parsing with brackets

## References

- [LC 1087: Brace Expansion on LeetCode](https://www.leetcode.com/problems/brace-expansion/)
- [LeetCode Discuss — LC 1087: Brace Expansion](https://www.leetcode.com/problems/brace-expansion/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/brace-expansion/editorial/) *(may require premium)*

## Template Reference

- [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/)
