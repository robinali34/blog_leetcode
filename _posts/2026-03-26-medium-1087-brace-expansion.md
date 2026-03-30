---
layout: post
title: "LeetCode 1087. Brace Expansion"
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

## Solution: Parse + Backtracking -- $O(k^n)$

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
{% endraw %}

**Time**: $O(k^m \cdot m)$ where $m$ = number of groups, $k$ = max options per group, and $m$ for string copy
**Space**: $O(m)$ recursion depth + $O(k^m \cdot m)$ output

## Key Details

**Parsing**: Skip commas by only collecting `isalpha(s[i])` characters inside braces. Characters outside braces become single-element groups.

**Sorted output without post-sort**: Sorting each group during parsing ensures DFS explores characters in order. Since groups are processed left-to-right, the lexicographic order is maintained throughout.

**Backtracking pattern**: Push → recurse → pop. Identical to subset/permutation generation, except here we pick exactly one from each group.

## Common Mistakes

- Forgetting to skip commas during parsing (adding `,` as a character option)
- Not sorting groups, then needing to sort the entire output ($O(k^m \cdot m \log(k^m))$ instead of $O(k^m \cdot m)$)
- Off-by-one: not incrementing `i` past the closing `}`

## Key Takeaways

- **"Generate all combinations from groups of choices"** = backtracking over groups
- Parsing into an intermediate representation (groups) cleanly separates concerns from the combinatorial generation
- Sorting inputs early often eliminates the need to sort outputs

## Related Problems

- [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) -- same pattern: groups of choices → backtrack
- [78. Subsets](https://leetcode.com/problems/subsets/) -- backtracking enumeration
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) -- constrained backtracking
- [394. Decode String](https://leetcode.com/problems/decode-string/) -- string parsing with brackets

## Template Reference

- [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/)
