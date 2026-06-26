---
layout: post
title: "[Medium] 875. Koko Eating Bananas"
date: 2026-02-06 00:00:00 -0700
categories: [leetcode, medium, array, binary-search]
permalink: /2026/02/06/medium-875-koko-eating-bananas/
tags: [leetcode, medium, array, binary-search]
---
Koko has `n` piles of bananas; the `i`-th pile has `piles[i]` bananas. The guards return in `h` hours. Koko can choose an integer eating speed `k` (bananas per hour). Each hour she picks one pile and eats `k` bananas from it; if the pile has fewer than `k`, she eats all of them and does not eat from another pile that hour. Return the **minimum** integer `k` such that she can finish all bananas within `h` hours.

## Examples

**Example 1:**

```
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation: At speed 4: (3/4 + 6/4 + 7/4 + 11/4) = 1+2+2+3 = 8 hours.
```

**Example 2:**

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: She must finish in 5 hours, so speed must be at least max(piles) = 30.
```

**Example 3:**

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Thinking Process

1. **Binary search on the answer:** When the answer is in a range and feasibility is easy to check, binary search on that range.

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

Try speed 1, 2, 3, ... until total hours ≤ h.

```cpp
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int speed = 1;
        while (true) {
            int hourSpend = 0;
            for (int pile : piles) {
                hourSpend += pile / speed + (pile % speed != 0);
                if (hourSpend > h) break;
            }
            if (hourSpend <= h) return speed;
            else speed++;
        }
    }
};
```

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Binary search on the answer:** When the answer is in a range and feasibility is easy to check, binary search on that range.

**How the code works:**
1. **Binary search on the answer:** When the answer is in a range and feasibility is easy to check, binary search on that range.
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

**Walkthrough** — input `piles = [3,6,7,11], h = 8`, expected output `4`:

At speed 4: (3/4 + 6/4 + 7/4 + 11/4) = 1+2+2+3 = 8 hours.

**Time:** O(n × max(piles)) in the worst case — too slow for large piles. · **Space:** O(1).
## Related Problems

- [1283. Find the Smallest Divisor Given a Threshold](https://www.leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) — Same “minimize value so sum of ceils ≤ limit” pattern
- [1552. Magnetic Force Between Two Balls](https://www.leetcode.com/problems/magnetic-force-between-two-balls/) — Binary search on answer

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Binary search on the answer:** When the answer is in a range and feasibility is easy to check, binary search on that range.
2. **Ceiling division:** `pile / k + (pile % k != 0)` or `(pile + k - 1) / k` gives hours per pile.
3. **Range:** Minimum speed is 1; maximum needed is `max(piles)` (one hour per pile).

## References

- [LC 875: Koko Eating Bananas on LeetCode](https://www.leetcode.com/problems/koko-eating-bananas/)
- [LeetCode Discuss — LC 875: Koko Eating Bananas](https://www.leetcode.com/problems/koko-eating-bananas/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/koko-eating-bananas/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
