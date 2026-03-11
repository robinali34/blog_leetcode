---
layout: post
title: "LeetCode 1202. Smallest String With Swaps"
date: 2026-03-09
categories: [leetcode, medium, string, graph, dsu]
tags: [leetcode, medium, string, graph, dsu, union-find, sorting]
permalink: /2026/03/09/medium-1202-smallest-string-with-swaps/
---

You are given a string `s` and an array of index pairs `pairs` where `pairs[i] = [a, b]` indicates you can swap the characters at indices `a` and `b` **any number of times**. Return the lexicographically smallest string achievable after performing the swaps.

## Examples

**Example 1:**

```
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explanation: Swap s[0] and s[3] → "bcad", swap s[1] and s[2] → "bacd"
```

**Example 2:**

```
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explanation: Indices 0,1,2,3 are all connected → sort all characters → "abcd"
```

**Example 3:**

```
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
```

## Constraints

- `1 <= s.length <= 10^5`
- `0 <= pairs.length <= 10^5`
- `0 <= pairs[i][0], pairs[i][1] < s.length`
- `s` contains only lowercase English letters

## Thinking Process

### Key Insight: Transitive Swaps

If you can swap indices `(a, b)` and `(b, c)`, then you can effectively swap `(a, c)` too (via a chain of swaps). This means all indices connected through swap pairs form a **group** where characters can be freely rearranged.

This is a **connectivity** problem -- use DSU (Union-Find) to find connected components.

### Algorithm

1. **Union** all pairs -- indices that can swap (directly or transitively) end up in the same component
2. **Group** indices by their root parent
3. **Sort** the characters within each group
4. **Place** sorted characters back into the sorted indices

Within each connected component, we can achieve any permutation. The lexicographically smallest result comes from sorting the characters and placing them in index order.

## Approach: DSU + Group Sort -- $O(n \log n)$

{% raw %}
```cpp
class DSU {
public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 1);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank[px] < rank[py]) swap(px, py);
        parent[py] = px;
        rank[px] += rank[py];
        return true;
    }

private:
    vector<int> parent, rank;
};

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.size();
        DSU dsu(n);

        for (auto& p : pairs) dsu.unite(p[0], p[1]);

        unordered_map<int, vector<int>> groups;
        for (int i = 0; i < n; i++)
            groups[dsu.find(i)].push_back(i);

        string res = s;
        for (auto& [parent, idxs] : groups) {
            string chars = "";
            for (int i : idxs) chars += s[i];
            sort(chars.begin(), chars.end());
            sort(idxs.begin(), idxs.end());
            for (int i = 0; i < (int)idxs.size(); i++)
                res[idxs[i]] = chars[i];
        }

        return res;
    }
};
```
{% endraw %}

**Time**: $O(n \log n)$ -- sorting within groups dominates (all groups together have $n$ elements total)
**Space**: $O(n)$ for DSU and grouping

## Walk-Through: s = "dcab", pairs = [[0,3],[1,2],[0,2]]

```
Step 1 — Union pairs:
  unite(0,3) → {0,3}
  unite(1,2) → {1,2}
  unite(0,2) → {0,1,2,3}   ← all connected

Step 2 — Group by root:
  root 0 → indices [0,1,2,3]

Step 3 — Sort chars at those indices:
  chars = "dcab" → sorted: "abcd"
  indices = [0,1,2,3]

Step 4 — Place back:
  res[0]='a', res[1]='b', res[2]='c', res[3]='d'
  result = "abcd" ✓
```

## Common Mistakes

- Treating swap pairs as independent (missing transitivity -- if `(0,1)` and `(1,2)` exist, `(0,2)` is implicitly available)
- Forgetting to sort both the indices and the characters before reassigning
- Not using path compression in DSU (causes TLE on large inputs)

## Key Takeaways

- **"Can swap any number of times"** = connectivity problem = DSU
- Within a connected component, any permutation is reachable, so just **sort** for the optimal result
- This pattern generalizes: whenever elements can be freely rearranged within groups, union the groups and sort independently

## Related Problems

- [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) -- DSU for MST
- [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) -- DSU to group connected accounts
- [839. Similar String Groups](https://leetcode.com/problems/similar-string-groups/) -- DSU on string similarity

## Template Reference

- [Graph (DSU)](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
- [Data Structures (DSU)](/blog_leetcode/posts/2025-10-29-leetcode-templates-data-structures/)
