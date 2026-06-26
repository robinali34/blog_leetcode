---
layout: post
title: "[Easy] 893. Groups of Special-Equivalent Strings"
date: 2026-02-15
categories: [leetcode, easy, string, hash]
tags: [leetcode, easy, string, hash, canonical-form]
permalink: /2026/02/15/easy-893-groups-of-special-equivalent-strings/
---
Two strings are **special-equivalent** if you can swap characters at even indices among themselves and swap characters at odd indices among themselves, any number of times. Return the number of groups of special-equivalent strings.

## Examples

**Example 1:**

```
Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: Groups are ["abcd","cdab","cbad"], ["xyzz","zzxy"], ["zzyx"].
```

**Example 2:**

```
Input: words = ["abc","acb","bac","bca","cab","cba"]
Output: 3
```

## Constraints

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 20`
- `words[i]` consist of lowercase English letters
- All `words[i]` have the same length

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Thinking Process

Swapping within even positions and within odd positions means:

- **Order inside even positions doesn't matter**
- **Order inside odd positions doesn't matter**

So what actually matters is:
- The **multiset** of even-index characters
- The **multiset** of odd-index characters

Two strings are equivalent if and only if:

```
sorted(even chars) == sorted(even chars)
AND
sorted(odd chars) == sorted(odd chars)
```

### Canonical Form

For each word, build a **signature**:
1. Extract even-index characters
2. Extract odd-index characters
3. Sort both
4. Concatenate with a separator

Example: `"abcd"` -- even: `ac`, odd: `bd` -- signature: `"ac|bd"`

All strings with the same signature belong to one group. The answer is the number of distinct signatures.

### Formal View

Each string defines a pair `(E_multiset, O_multiset)`. Swaps only permute within E and within O. So equivalence class = identical pair of multisets. This is a classic **"group by canonical representation under allowed transformations"** pattern, similar to Group Anagrams (LC 49).



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

## Approach 1: Sort-Based Signature -- O(nk log k)

For each word, sort even-index and odd-index characters separately, concatenate into a key, and insert into a set.

{% raw %}
```cpp
class Solution {
public:
    int numSpecialEquivGroups(vector<string>& words) {
        unordered_set<string> groups;

        for (auto& w : words) {
            string even = "", odd = "";

            for (int i = 0; i < (int)w.size(); i++) {
                if (i % 2 == 0) even += w[i];
                else odd += w[i];
            }

            sort(even.begin(), even.end());
            sort(odd.begin(), odd.end());

            groups.insert(even + "|" + odd);
        }

        return groups.size();
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** Swapping within even positions and within odd positions means:

**How the code works:**
- **Order inside even positions doesn't matter**
- **Order inside odd positions doesn't matter**
- The **multiset** of even-index characters
- The **multiset** of odd-index characters
1. Extract even-index characters
2. Extract odd-index characters

**Walkthrough** — input `words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]`, expected output `3`:

Groups are ["abcd","cdab","cbad"], ["xyzz","zzxy"], ["zzyx"].
## Approach 2: Frequency Count -- O(nk)

Since characters are lowercase letters (only 26), we can avoid sorting by counting character frequencies instead.

{% raw %}
```cpp
class Solution {
public:
    int numSpecialEquivGroups(vector<string>& words) {
        unordered_set<string> groups;

        for (auto& w : words) {
            int even[26] = {0};
            int odd[26] = {0};

            for (int i = 0; i < (int)w.size(); i++) {
                if (i % 2 == 0) even[w[i] - 'a']++;
                else odd[w[i] - 'a']++;
            }

            string key = "";
            for (int i = 0; i < 26; i++) key += to_string(even[i]) + "#";
            for (int i = 0; i < 26; i++) key += to_string(odd[i]) + "#";

            groups.insert(key);
        }

        return groups.size();
    }
};
```
{% endraw %}

**Time**: O(nk)
**Space**: O(nk)

## Common Mistakes

- Only sorting the whole string (ignores even/odd split)
- Forgetting the parity split entirely
- Not using a separator in the key (causes hash collisions, e.g., counts `12` vs `1` + `2`)
- Using `vector<int>` as key without a custom hash

## Key Takeaways

This problem tests:
- **Canonical representation** -- reduce equivalence to a signature
- **Parity-based partitioning** -- even vs odd index awareness
- **Frequency counting** as an alternative to sorting for small alphabets

## Related Problems

- [49. Group Anagrams](https://www.leetcode.com/problems/group-anagrams/) -- group by sorted canonical form
- [205. Isomorphic Strings](https://www.leetcode.com/problems/isomorphic-strings/) -- transformation invariant

## References

- [LC 893: Groups of Special-Equivalent Strings on LeetCode](https://www.leetcode.com/problems/groups-of-special-equivalent-strings/)
- [LeetCode Discuss — LC 893: Groups of Special-Equivalent Strings](https://www.leetcode.com/problems/groups-of-special-equivalent-strings/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/groups-of-special-equivalent-strings/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
