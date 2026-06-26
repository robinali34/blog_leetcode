---
layout: post
title: "[Medium] 1488. Avoid Flood in The City"
date: 2026-02-07 00:00:00 -0700
categories: [leetcode, medium, array, greedy, binary-search, set]
permalink: /2026/02/07/medium-1488-avoid-flood-in-the-city/
tags: [leetcode, medium, array, greedy, binary-search, set]
---
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

## Thinking Process

1. **Last-rain index:** Knowing when each lake was last filled tells us we must dry it before the next rain on that lake.

- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 130" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary search: shrink [lo … hi]</text>

  <rect x="40" y="40" width="48" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="64" y="58" text-anchor="middle" font-size="12" fill="#3A3530">lo</text>
  <rect x="108" y="40" width="48" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="132" y="58" text-anchor="middle" font-size="12" fill="#3A3530">mid</text>
  <rect x="196" y="40" width="48" height="32" rx="4" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="220" y="58" text-anchor="middle" font-size="12" fill="#3A3530">hi</text>
  <rect x="60" y="90" width="160" height="28" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="140" y="108" text-anchor="middle" font-size="11" fill="#6B6560">discard half each step → O(log n)</text>
  <path d="M132 72v12M220 72v12" stroke="#9A9792" stroke-width="1.5" marker-end="url(#a)"/>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Standard binary search** *(this problem)* | $O(\log n)$ | $O(1)$ | Sorted array, `left <= right` |
| Lower / upper bound | $O(\log n)$ | $O(1)$ | First/last position, insert index |
| Binary search on rotated array | $O(\log n)$ | $O(1)$ | Identify sorted half, discard other |
| Binary search on answer | $O(n \log M)$ | $O(1)$ | Monotonic predicate over search space |

## Solution

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

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Last-rain index:** Knowing when each lake was last filled tells us we must dry it before the next rain on that lake.

**How the code works:**
1. **Last-rain index:** Knowing when each lake was last filled tells us we must dry it before the next rain on that lake.
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

**Walkthrough** — input `rains = [1,2,3,4]`, expected output `[-1,-1,-1,-1]`:

No lake rains twice, so no flood. Dry days don't appear.

**Time:** O(n log n) — each dry day is inserted and at most once erased from the set; at most n `lower_bound` calls. · **Space:** O(n).
## Related Problems

- [1642. Furthest Building You Can Reach](https://www.leetcode.com/problems/furthest-building-you-can-reach/) — Greedy with limited resources
- [871. Minimum Number of Refueling Stops](https://www.leetcode.com/problems/minimum-number-of-refueling-stops/) — Greedy + heap/set

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Last-rain index:** Knowing when each lake was last filled tells us we must dry it before the next rain on that lake.
2. **Earliest dry day:** `lower_bound(mp[lake])` on the set of dry days gives the first valid day to dry that lake.
3. **Default 1:** Dry days that are never needed can output any lake number; `1` is valid.

## References

- [LC 1488: Avoid Flood in The City on LeetCode](https://www.leetcode.com/problems/avoid-flood-in-the-city/)
- [LeetCode Discuss — LC 1488: Avoid Flood in The City](https://www.leetcode.com/problems/avoid-flood-in-the-city/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/avoid-flood-in-the-city/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
