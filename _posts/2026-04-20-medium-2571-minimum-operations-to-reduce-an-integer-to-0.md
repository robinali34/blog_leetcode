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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Queue BFS** *(this problem)* | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| Level-order BFS | O(n) | O(w) | Process by depth/layer |

## Solution
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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** ### Binary Perspective

**How the code works:**
- **Bit is 0** -- shift right, nothing to do
- **Bit is 1:**
- If the next bit is also `1` (i.e., `n & 3 == 3`) -- **add 1** (carry forward to collapse the block)
- Otherwise (isolated `1`) -- **subtract 1** (cheaper to just remove it)

**Walkthrough** — input `n = 39`, expected output `3`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Comparison

| Aspect | Greedy (Bit Manipulation) | BFS |
|---|---|---|
| Time | O(log n) | O(n log n) |
| Space | O(1) | O(n) |
| Correctness proof | Requires greedy argument | Guaranteed (shortest path) |
| Interview value | Shows deep bit intuition | Shows BFS modeling skill |
| Best for | Production / follow-up optimization | Proving correctness / verification |

BFS is useful as a **verification tool**: run it on small inputs to confirm the greedy produces optimal results. In interviews, mentioning BFS as a brute-force baseline before presenting the greedy shows strong problem-solving structure.

## Why the Greedy is Optimal

Consider a block of k consecutive `1`s:

| Strategy | Operations |
|---|---|
| Subtract each bit individually | k |
| Add 1 to collapse, then subtract the resulting bit | 2 |

For k ge 3, adding is strictly better. For k = 2 (like `11₂ = 3`), both cost 2 operations:
- Add: 3 + 1 = 4, 4 - 4 = 0 (2 ops)
- Subtract: 3 - 1 = 2, 2 - 2 = 0 (2 ops)

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
- BFS gives a provably optimal baseline; greedy gives O(log n) performance
- The pattern "add to create carry, then subtract" appears in many bit manipulation problems

## Related Problems

- [397. Integer Replacement](https://www.leetcode.com/problems/integer-replacement/) -- similar greedy on even/odd with bit analysis
- [191. Number of 1 Bits](https://www.leetcode.com/problems/number-of-1-bits/) -- popcount baseline
- [1342. Number of Steps to Reduce a Number to Zero](https://www.leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) -- simpler version with only divide/subtract
- [260. Single Number III](https://www.leetcode.com/problems/single-number-iii/) -- bit manipulation with XOR

## References

- [LC 2571: Minimum Operations to Reduce an Integer to 0 on LeetCode](https://www.leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/)
- [LeetCode Discuss — LC 2571: Minimum Operations to Reduce an Integer to 0](https://www.leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/editorial/) *(may require premium)*

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
