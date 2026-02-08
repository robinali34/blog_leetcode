---
layout: post
title: "875. Koko Eating Bananas"
date: 2026-02-06 00:00:00 -0700
categories: [leetcode, medium, array, binary-search]
permalink: /2026/02/06/medium-875-koko-eating-bananas/
tags: [leetcode, medium, array, binary-search]
---

# 875. Koko Eating Bananas

## Problem Statement

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

## Solution Approach

- **Feasibility:** For speed `k`, hours needed = sum over piles of `ceil(pile / k)` = `pile / k` if divisible, else `pile / k + 1`. In code: `pile / k + (pile % k != 0)`.
- **Minimize k:** We want the smallest `k` such that total hours ≤ `h`. Speed is in range `[1, max(piles)]`.
- **Brute force:** Try `k = 1, 2, 3, ...` until feasible. Too slow when `max(piles)` is large.
- **Optimized:** Binary search on `k` in `[1, max(piles)]`. For each `mid`, compute hours; if `hours <= h` then `mid` is feasible, so search left (right = mid), else search right (left = mid + 1). Return the smallest feasible `k` (the leftmost that works).

## Solution 1: Linear Search (Brute Force)

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

- **Time:** O(n × max(piles)) in the worst case — too slow for large piles.
- **Space:** O(1).

## Solution 2: Binary Search on Answer

Binary search on `k` in `[1, max(piles)]`; for each `mid`, compute total hours and narrow the range.

```cpp
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1, right = *max_element(piles.begin(), piles.end());
        while (left < right) {
            int mid = left + (right - left) / 2;
            int hourSpend = 0;
            for (int pile : piles) {
                hourSpend += pile / mid + (pile % mid != 0);
            }
            if (hourSpend <= h) right = mid;
            else left = mid + 1;
        }
        return right;
    }
};
```

- **Invariant:** `right` is always feasible; we look for the smallest feasible `k`, which is `right` when `left == right`.
- **Time:** O(n log(max(piles))). **Space:** O(1).

## Key Insights

1. **Binary search on the answer:** When the answer is in a range and feasibility is easy to check, binary search on that range.
2. **Ceiling division:** `pile / k + (pile % k != 0)` or `(pile + k - 1) / k` gives hours per pile.
3. **Range:** Minimum speed is 1; maximum needed is `max(piles)` (one hour per pile).

## Related Problems

- [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) — Same “minimize value so sum of ceils ≤ limit” pattern
- [1552. Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/) — Binary search on answer
