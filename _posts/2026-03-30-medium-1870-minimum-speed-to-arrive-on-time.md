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

$$t = \sum_{i=0}^{n-2} \left\lceil \frac{\text{dist}[i]}{k} \right\rceil + \frac{\text{dist}[n-1]}{k}$$

- First `n - 1` rides: round up (must wait for next integer hour)
- Last ride: exact time (no waiting after)

Integer ceiling trick: $\lceil a/b \rceil = (a + b - 1) / b$ using integer division.

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

## Solution: Binary Search on Answer -- $O(n \log M)$

{% raw %}
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
{% endraw %}

**Time**: $O(n \log M)$ where $M = 10^7$ (speed range)
**Space**: $O(1)$

## Why $M = 10^7$?

Maximum distance is $10^5$ and `hour` can have two decimal places, so the last ride could need a speed up to $10^5 / 0.01 = 10^7$ in the worst case.

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

- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) -- binary search on speed with ceiling division
- [1011. Capacity To Ship Packages](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) -- binary search on capacity
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) -- binary search on answer
- [774. Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) -- binary search on real-valued answer

## Template Reference

- [Arrays & Strings — Binary Search on Answer](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
