---
layout: post
title: "1488. Avoid Flood in The City"
date: 2026-02-07 00:00:00 -0700
categories: [leetcode, medium, array, greedy, binary-search, set]
permalink: /2026/02/07/medium-1488-avoid-flood-in-the-city/
tags: [leetcode, medium, array, greedy, binary-search, set]
---

# 1488. Avoid Flood in The City

## Problem Statement

You have infinitely many lakes, all initially empty. When it rains on lake `n`, that lake becomes full. If it rains on a lake that is already full, a flood happens. Your goal is to prevent all floods.

You are given an integer array `rains` where:

- `rains[i] > 0` means rain on lake `rains[i]` on day `i`
- `rains[i] == 0` means no rain on day `i`; you must choose **one** lake to dry (that lake becomes empty)

Return an array `ans` such that:

- `ans[i] == -1` if `rains[i] > 0`
- `ans[i]` is the lake number you choose to dry if `rains[i] == 0` (any valid lake is fine; typically 1 if no constraint)

Return an empty array if it is impossible to avoid a flood.

## Examples

**Example 1:**

```
Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: No lake rains twice, so no flood. Dry days don't appear.
```

**Example 2:**

```
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: Day 2: rain on lake 2. Day 3 (dry): dry lake 2 so it won't flood on day 5. Day 4 (dry): dry lake 1 so it won't flood on day 6.
```

**Example 3:**

```
Input: rains = [1,2,0,1,2]
Output: []
Explanation: Lakes 1 and 2 are full after day 2; only one dry day (day 3). We can dry at most one lake, so the second rain on 1 or 2 causes a flood.
```

## Constraints

- `1 <= rains.length <= 10^5`
- `0 <= rains[i] <= 10^9`

## Solution Approach

- **Track state:** For each lake, remember the **last day** it was filled (rained on). When we see rain on the same lake again, we must have dried it on some day **after** that last fill and **before** this day.
- **Dry days:** Store indices where `rains[i] == 0` in a **sorted set** so we can quickly find the earliest dry day in a given range (e.g. first dry day ≥ last fill day).
- **Greedy:** When lake `L` rains again, we need to use a dry day between `mp[L]` and `i`. Greedily pick the **earliest** such dry day (`lower_bound(mp[L])`) so we leave later dry days for other lakes. Assign that day to dry lake `L`, remove that day from the set, and update `mp[L] = i`. If no dry day exists in range, return `[]`.
- **Output:** Rain days: `ans[i] = -1`. Dry days: use the chosen lake (or default 1 for unused dry days).

## Solution: Greedy + Sorted Set

```cpp
class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        vector<int> rtn(rains.size(), 1);
        set<int> st;
        unordered_map<int, int> mp;
        for (int i = 0; i < rains.size(); i++) {
            if (rains[i] == 0) {
                st.insert(i);
            } else {
                rtn[i] = -1;
                if (mp.contains(rains[i])) {
                    auto it = st.lower_bound(mp[rains[i]]);
                    if (it == st.end()) return {};
                    rtn[*it] = rains[i];
                    st.erase(it);
                }
                mp[rains[i]] = i;
            }
        }
        return rtn;
    }
};
```

### Algorithm Breakdown

1. **`rtn`:** Result array; default `1` (any lake for dry days).
2. **`st`:** Sorted set of indices where `rains[i] == 0` (dry days available).
3. **`mp`:** Map lake → last index where it rained on that lake.
4. **Loop:**  
   - **Dry day (`rains[i] == 0`):** Add `i` to `st`.  
   - **Rain day (`rains[i] > 0`):** Set `rtn[i] = -1`. If this lake was already full (`mp.contains(rains[i])`), find the earliest dry day ≥ `mp[rains[i]]` with `lower_bound(mp[rains[i]])`. If none, return `[]`. Else assign that day to dry this lake: `rtn[*it] = rains[i]`, erase `*it` from `st`. Then set `mp[rains[i]] = i`.
5. Unused dry days remain as `1` (valid).

### Why Greedy Works

Using the **earliest** available dry day for a lake leaves more dry days for later lakes that might need to be dried before their next rain. If we used a later dry day, we might run out of dry days for another lake.

### Complexity

- **Time:** O(n log n) — each dry day is inserted and at most once erased from the set; at most n `lower_bound` calls.
- **Space:** O(n).

## Key Insights

1. **Last-rain index:** Knowing when each lake was last filled tells us we must dry it before the next rain on that lake.
2. **Earliest dry day:** `lower_bound(mp[lake])` on the set of dry days gives the first valid day to dry that lake.
3. **Default 1:** Dry days that are never needed can output any lake number; `1` is valid.

## Related Problems

- [1642. Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/) — Greedy with limited resources
- [871. Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) — Greedy + heap/set
