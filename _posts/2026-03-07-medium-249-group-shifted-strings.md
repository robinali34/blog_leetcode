---
layout: post
title: "[Medium] 249. Group Shifted Strings"
date: 2026-03-07
categories: [leetcode, medium, string, hash]
tags: [leetcode, medium, string, hash, canonical-form]
permalink: /2026/03/07/medium-249-group-shifted-strings/
---
We can "shift" a string by shifting each character to its successive character (with `z` wrapping to `a`). For example, `"abc"` can be shifted to `"bcd"`, ..., `"xyz"`, `"yza"`, `"zab"`.

Given an array of strings, group all strings that belong to the same shifting sequence.

## Examples

**Example 1:**

```
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
```

**Example 2:**

```
Input: strings = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strings.length <= 200`
- `1 <= strings[i].length <= 50`
- `strings[i]` consists of lowercase English letters

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Thinking Process

Two strings belong to the same shift group if their **consecutive character differences** are identical. For example:

```
"abc": b-a=1, c-b=1  → key: "1,1,"
"bcd": c-b=1, d-c=1  → key: "1,1,"  ← same group
"xyz": y-x=1, z-y=1  → key: "1,1,"  ← same group
```

The wrapping case: `"az"` and `"ba"`:

```
"az": z-a = 25       → key: "25,"
"ba": a-b = -1 → +26 = 25  → key: "25,"  ← same group
```

### Canonical Form

For each string, compute the difference between consecutive characters modulo 26. This difference sequence is the **canonical key** -- strings with the same key belong to the same group.

Use `(str[i] - str[i-1] + 26) % 26` to handle the wrap-around from `z` to `a`.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Approach: Difference Key Hashing -- O(n · k)

{% raw %}
```cpp
class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string, vector<string>> hm;

        for (string str : strings) {
            string key;
            for (int i = 1; i < (int)str.size(); i++) {
                int diff = (str[i] - str[i - 1] + 26) % 26;
                key += to_string(diff) + ",";
            }
            hm[key].push_back(str);
        }

        vector<vector<string>> rtn;
        for (auto& [key, strs] : hm)
            rtn.push_back(strs);

        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** Two strings belong to the same shift group if their **consecutive character differences** are identical. For example:

**Walkthrough** — input `strings = ["abc","bcd","acef","xyz","az","ba","a","z"]`, expected output `[["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Why `+26` Before `%26`?

In C++, the `%` operator can return negative values for negative operands. For example, `'a' - 'z' = -25`, and `-25 % 26 = -25` (implementation-defined but typically negative). Adding 26 first ensures the result is always in `[0, 25]`.

## Common Mistakes

- Forgetting the `+26` before `%26` -- negative differences break the key
- Not using a separator in the key -- `"1,12,"` vs `"11,2,"` would collide without separators
- Single-character strings: they all share the empty key `""` and correctly group together

## Key Takeaways

- This is a **"group by canonical form"** problem, same pattern as [LC 49 Group Anagrams](https://www.leetcode.com/problems/group-anagrams/) and [LC 893 Groups of Special-Equivalent Strings](/2026/02/15/easy-893-groups-of-special-equivalent-strings/)
- The canonical form here is the **difference sequence** rather than sorted characters
- Always use a separator when building composite keys from numbers to avoid collisions

## Related Problems

- [49. Group Anagrams](https://www.leetcode.com/problems/group-anagrams/) -- group by sorted canonical form
- [893. Groups of Special-Equivalent Strings](https://www.leetcode.com/problems/groups-of-special-equivalent-strings/) -- group by even/odd split
- [205. Isomorphic Strings](https://www.leetcode.com/problems/isomorphic-strings/) -- structural equivalence

## References

- [LC 249: Group Shifted Strings on LeetCode](https://www.leetcode.com/problems/group-shifted-strings/)
- [LeetCode Discuss — LC 249: Group Shifted Strings](https://www.leetcode.com/problems/group-shifted-strings/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/group-shifted-strings/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
