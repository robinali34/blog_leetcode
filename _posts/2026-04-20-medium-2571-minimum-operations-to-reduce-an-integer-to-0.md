---
layout: post
title: "[Medium] 2571. Minimum Operations to Reduce an Integer to 0"
date: 2026-04-20
categories: [leetcode, medium, bit-manipulation]
tags: [leetcode, medium, bit-manipulation, greedy, bfs, math]
permalink: /2026/04/20/medium-2571-minimum-operations-to-reduce-an-integer-to-0/
---

Given a positive integer `n`, you can add or subtract any power of 2 in one operation. Return the **minimum number of operations** to reduce `n` to `0`.

## Examples

**Example 1:**

```
Input: n = 39
Output: 3

39 = 100111₂
  39 + 1 = 40 (101000₂)     op 1: +2⁰
  40 - 8 = 32 (100000₂)     op 2: -2³
  32 - 32 = 0               op 3: -2⁵
```

**Example 2:**

```
Input: n = 54
Output: 3

54 = 110110₂
  54 + 2 = 56 (111000₂)     op 1: +2¹
  56 + 8 = 64 (1000000₂)    op 2: +2³
  64 - 64 = 0               op 3: -2⁶
```

## Constraints

- `1 <= n <= 10^5`

## Thinking Process

### Binary Perspective

Every number is already a sum of powers of 2 (its binary representation). Each `1` bit could be removed by subtracting that power -- that's the naive approach, costing `popcount(n)` operations.

But we can do **better** by adding a power of 2 to create carries that collapse consecutive `1`s.

### When to Add vs Subtract

```
n = 7 = 111₂

Naive (subtract each bit): 4 + 2 + 1 → 3 ops
Smart: 7 + 1 = 8 (1000₂), then 8 - 8 = 0 → 2 ops
```

Adding `1` to a block of consecutive `1`s collapses them all into a single `1` at a higher position.

### The Greedy Rule

Scan from LSB to MSB:
- **Bit is 0** -- shift right, nothing to do
- **Bit is 1:**
  - If the next bit is also `1` (i.e., `n & 3 == 3`) -- **add 1** (carry forward to collapse the block)
  - Otherwise (isolated `1`) -- **subtract 1** (cheaper to just remove it)

Each add/subtract counts as one operation. Shifting doesn't count (we're just moving to the next bit position).

## Solution 1: Greedy Bit Manipulation -- $O(\log n)$ time, $O(1)$ space

{% raw %}
```cpp
class Solution {
public:
    int minOperations(int n) {
        int ops = 0;
        while (n > 0) {
            if ((n & 1) == 0) {
                n >>= 1;
            } else if (n == 1) {
                return ops + 1;
            } else if ((n & 3) == 3) {
                n += 1;
                ops++;
            } else {
                n -= 1;
                ops++;
            }
        }
        return ops;
    }
};
```
{% endraw %}

### Walk-through: `n = 23 (10111₂)`

```
Step   n (binary)   Action     ops
─────  ───────────  ─────────  ───
  1    10111        n&3=11 → +1   1
  2    11000        shift >>
  3    1100         shift >>
  4    110          shift >>
  5    11           n&3=11 → +1   2
  6    100          shift >>
  7    10           shift >>
  8    1            n==1 → +1     3
```

Result: **3 operations** (not 6 -- the earlier walkthrough in the problem had a bug; let's verify: 23 + 1 = 24 = 11000₂, then 24 + 8 = 32 = 100000₂, then 32 - 32 = 0. That's 3 ops.)

### Walk-through: `n = 7 (111₂)`

```
Step   n (binary)   Action     ops
─────  ───────────  ─────────  ───
  1    111          n&3=11 → +1   1
  2    1000         shift >>
  3    100          shift >>
  4    10           shift >>
  5    1            n==1 → +1     2
```

Result: **2 operations** (7 + 1 = 8, 8 - 8 = 0)

## Solution 2: BFS -- $O(n \log n)$ time, $O(n)$ space

BFS explores all reachable states layer by layer, guaranteeing the shortest path. From any value, try adding or subtracting every power of 2.

{% raw %}
```cpp
class Solution {
public:
    int minOperations(int n) {
        if (n == 0) return 0;

        unordered_set<int> visited;
        queue<int> q;
        q.push(n);
        visited.insert(n);
        int ops = 0;

        while (!q.empty()) {
            int size = q.size();
            ops++;
            for (int i = 0; i < size; ++i) {
                int cur = q.front();
                q.pop();

                for (int p = 1; p <= 1 << 17; p <<= 1) {
                    for (int next : {cur + p, cur - p}) {
                        if (next == 0) return ops;
                        if (next > 0 && next < (1 << 18) && !visited.count(next)) {
                            visited.insert(next);
                            q.push(next);
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```
{% endraw %}

### Why the Bound `1 << 18`?

Since `n <= 10^5 < 2^17`, adding a power of 2 can at most double the value. We cap the search space at `2^18` to prevent exploring irrelevant large numbers. In practice BFS terminates very quickly since the greedy answer is at most $O(\log n)$ operations.

## Comparison

| Aspect | Greedy (Bit Manipulation) | BFS |
|---|---|---|
| Time | $O(\log n)$ | $O(n \log n)$ |
| Space | $O(1)$ | $O(n)$ |
| Correctness proof | Requires greedy argument | Guaranteed (shortest path) |
| Interview value | Shows deep bit intuition | Shows BFS modeling skill |
| Best for | Production / follow-up optimization | Proving correctness / verification |

BFS is useful as a **verification tool**: run it on small inputs to confirm the greedy produces optimal results. In interviews, mentioning BFS as a brute-force baseline before presenting the greedy shows strong problem-solving structure.

## Why the Greedy is Optimal

Consider a block of $k$ consecutive `1`s:

| Strategy | Operations |
|---|---|
| Subtract each bit individually | $k$ |
| Add 1 to collapse, then subtract the resulting bit | $2$ |

For $k \ge 3$, adding is strictly better. For $k = 2$ (like `11₂ = 3`), both cost 2 operations:
- Add: $3 + 1 = 4$, $4 - 4 = 0$ (2 ops)
- Subtract: $3 - 1 = 2$, $2 - 2 = 0$ (2 ops)

The greedy chooses to add for `k >= 2`, which is safe since it never costs more.

## Common Mistakes

- **Treating `n = 1` separately:** After all shifts, `n == 1` is the base case (isolated single bit). Forgetting this causes infinite loops.
- **Using `n & 1 == 1` instead of `n & 3 == 3`:** The decision depends on whether the **next** bit is also set, not just the current bit
- **Counting shifts as operations:** Shifting is just moving to the next bit position, not an actual add/subtract operation
- **BFS without bounds:** Without capping the search space, BFS explodes in memory

## Key Takeaways

- **Think in binary** when the problem involves powers of 2
- **Consecutive `1`s can be collapsed** by adding 1 -- this is the core greedy insight
- Check `n & 3 == 3` (two lowest bits both set) to decide add vs subtract
- BFS gives a provably optimal baseline; greedy gives $O(\log n)$ performance
- The pattern "add to create carry, then subtract" appears in many bit manipulation problems

## Related Problems

- [397. Integer Replacement](https://leetcode.com/problems/integer-replacement/) -- similar greedy on even/odd with bit analysis
- [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) -- popcount baseline
- [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) -- simpler version with only divide/subtract
- [260. Single Number III](https://leetcode.com/problems/single-number-iii/) -- bit manipulation with XOR

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
