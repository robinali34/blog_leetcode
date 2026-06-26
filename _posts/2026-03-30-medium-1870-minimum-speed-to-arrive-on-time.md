---
layout: post
title: "[Medium] 1870. Minimum Speed to Arrive on Time"
date: 2026-03-30
categories: [leetcode, medium, binary-search]
tags: [leetcode, medium, binary-search, greedy]
permalink: /2026/03/30/medium-1870-minimum-speed-to-arrive-on-time/
---
You are given `n` train rides with distances `dist[i]`. Each train departs at an integer hour, so you must wait until the next whole hour to board the next train (except for the last ride). Given a time limit `hour`, return the **minimum positive integer speed** such that you can arrive on time, or `-1` if impossible.

## Examples

**Example 1:**

```
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1: ceil(1/1)=1 + ceil(3/1)=3 + 2/1=2 = 6 ≤ 6 ✓
```

**Example 2:**

```
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3: ceil(1/3)=1 + ceil(3/3)=1 + 2/3≈0.67 = 2.67 ≤ 2.7 ✓
```

**Example 3:**

```
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: Need at least n-1 = 2 hours for waiting, but 1.9 < 2.
```

## Constraints

- `1 <= n <= 10^5`
- `1 <= dist[i] <= 10^5`
- `1 <= hour <= 10^9`
- `hour` has at most two decimal places

## Thinking Process

### Impossible Case

We must take `n` trains. Between each pair we wait until the next integer hour, so we need **at least** `n - 1` hours just for the first `n - 1` rides (minimum 1 hour each). If `hour <= n - 1`, it's impossible.

### Monotonic Property

As speed increases, total time decreases. This means:

- If speed `k` is fast enough, any speed `> k` also works
- If speed `k` is too slow, any speed `< k` also fails

This is a **monotonic predicate** -- perfect for binary search on the answer.

### Feasibility Check

At speed `k`, the total time is:

$t = sum_{i=0}^{n-2} leftlceil frac{text{dist}[i]}{k} rightrceil + frac{text{dist}[n-1]}{k}

- First `n - 1` rides: round up (must wait for next integer hour)
- Last ride: exact time (no waiting after)

Integer ceiling trick: \lceil a/b \rceil = (a + b - 1) / b using integer division.

### Walk-through

```
dist = [1, 3, 2], hour = 2.7

Binary search: left=1, right=10^7

mid=5000000: t = 1 + 1 + 0.0000004 = 2.0 ≤ 2.7 → right=5000000
...converges...
mid=3: t = ceil(1/3) + ceil(3/3) + 2/3 = 1 + 1 + 0.67 = 2.67 ≤ 2.7 → right=3
mid=2: t = ceil(1/2) + ceil(3/2) + 2/2 = 1 + 2 + 1.0 = 4.0 > 2.7  → left=3

Answer: left = 3 ✓
```

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
| **Standard binary search** *(this problem)* | O(\log n) | O(1) | Sorted array, `left <= right` |
| Lower / upper bound | O(\log n) | O(1) | First/last position, insert index |
| Binary search on rotated array | O(\log n) | O(1) | Identify sorted half, discard other |
| Binary search on answer | O(n \log M) | O(1) | Monotonic predicate over search space |

## Solution
```cpp
class Solution {
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        int n = dist.size();
        if (hour <= n - 1) return -1;

        int left = 1, right = 1e7;
        while (left < right) {
            int mid = (left + right) / 2;
            if (can(dist, hour, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

private:
    bool can(const vector<int>& dist, double hour, int k) {
        double t = 0;
        int n = dist.size();
        for (int i = 0; i < n - 1; ++i) {
            t += (dist[i] + k - 1) / k;
        }
        t += (double)dist[n - 1] / k;
        return t <= hour;
    }
};
```

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** ### Impossible Case

**How the code works:**
- If speed `k` is fast enough, any speed `> k` also works
- If speed `k` is too slow, any speed `< k` also fails
- First `n - 1` rides: round up (must wait for next integer hour)
- Last ride: exact time (no waiting after)

**Walkthrough** — input `dist = [1,3,2], hour = 6`, expected output `1`:

At speed 1: ceil(1/1)=1 + ceil(3/1)=3 + 2/1=2 = 6 ≤ 6 ✓
## Why M = 10^7?

Maximum distance is 10^5 and `hour` can have two decimal places, so the last ride could need a speed up to 10^5 / 0.01 = 10^7$ in the worst case.

## Common Mistakes

- Not handling the impossible case (`hour <= n - 1`) -- leads to infinite binary search
- Using floating-point ceiling (`ceil(dist[i] / (double)k)`) instead of integer ceiling -- precision issues
- Applying ceiling to the **last** ride (the last ride doesn't need to round up)
- Wrong search range: upper bound too small misses edge cases with tight time limits

## Key Takeaways

- **"Find minimum X such that predicate holds"** with monotonic feasibility = binary search on the answer
- The integer ceiling trick `(a + b - 1) / b` avoids floating-point precision issues
- Treating the last element differently (no rounding) is a common pattern in scheduling/train problems

## Related Problems

- [875. Koko Eating Bananas](https://www.leetcode.com/problems/koko-eating-bananas/) -- binary search on speed with ceiling division
- [1011. Capacity To Ship Packages](https://www.leetcode.com/problems/capacity-to-ship-packages-within-d-days/) -- binary search on capacity
- [410. Split Array Largest Sum](https://www.leetcode.com/problems/split-array-largest-sum/) -- binary search on answer
- [774. Minimize Max Distance to Gas Station](https://www.leetcode.com/problems/minimize-max-distance-to-gas-station/) -- binary search on real-valued answer

## References

- [LC 1870: Minimum Speed to Arrive on Time on LeetCode](https://www.leetcode.com/problems/minimum-speed-to-arrive-on-time/)
- [LeetCode Discuss — LC 1870: Minimum Speed to Arrive on Time](https://www.leetcode.com/problems/minimum-speed-to-arrive-on-time/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-speed-to-arrive-on-time/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings — Binary Search on Answer](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
