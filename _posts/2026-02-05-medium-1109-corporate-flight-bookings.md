---
layout: post
title: "[Medium] 1109. Corporate Flight Bookings"
date: 2026-02-05 00:00:00 -0700
categories: [leetcode, medium, array, prefix-sum, difference-array]
permalink: /2026/02/05/medium-1109-corporate-flight-bookings/
tags: [leetcode, medium, array, prefix-sum, difference-array]
---
There are `n` flights labeled from `1` to `n`. You are given an array of flight bookings where `bookings[i] = [firsti, lasti, seatsi]` represents a booking for flights `firsti` through `lasti` (inclusive) with `seatsi` seats reserved for each flight in that range.

Return an array `answer` of length `n`, where `answer[i]` is the total number of seats reserved for flight `i + 1`.

## Examples

**Example 1:**

```
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight 1: 10 seats
Flight 2: 10 + 20 + 25 = 55 seats
Flight 3: 20 + 25 = 45 seats
Flight 4: 25 seats
Flight 5: 25 seats
```

**Example 2:**

```
Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight 1: 10 seats
Flight 2: 10 + 15 = 25 seats
```

## Constraints

- `1 <= n <= 2 * 10^4`
- `1 <= bookings.length <= 2 * 10^4`
- `1 <= firsti <= lasti <= n`
- `1 <= seatsi <= 10^4`

## Intro: Partial Sum and Difference Array

### Partial sum (prefix sum)

- **Idea**: For an array `A`, the partial sum at index `i` is `S[i] = A[0] + A[1] + ... + A[i]`. Then the sum of any contiguous segment `[l, r]` is `S[r] - S[l-1]` (with `S[-1] = 0`).
- **Use**: Range-sum queries in O(1) after O(n) preprocessing; also the basis for many “subarray sum” problems.

### Difference array (range update trick)

- **Idea**: Instead of updating every index in `[l, r]` by `+d`, we can:
  - Add `d` at index `l`
  - Subtract `d` at index `r+1` (if in bounds)
  Then one **prefix sum** over this “difference” array recovers the actual values after all range updates.
- **Why it works**: Prefix sum at `i` equals the sum of all “+d” and “-d” that affect position `i`; that sum is exactly the total change for position `i`.

### C++ `std::partial_sum`

From `<numeric>`:

```cpp
// Computes prefix sums in-place: out[i] = in[0] + in[1] + ... + in[i]
partial_sum(first, last, d_first);

// With custom binary op (e.g. multiply): out[i] = in[0] * in[1] * ... * in[i]
partial_sum(first, last, d_first, std::multiplies<>());
```

For this problem we build a difference array (add at `first`, subtract at `last+1`), then run `partial_sum` or `inclusive_scan` (C++17) to get the final seat counts.

### Common LeetCode problems using partial sum / difference array

- **Difference array (range update, then prefix sum):** [1109. Corporate Flight Bookings](https://www.leetcode.com/problems/corporate-flight-bookings/), [1094. Car Pooling](https://www.leetcode.com/problems/car-pooling/), [798. Smallest Rotation with Highest Score](https://www.leetcode.com/problems/smallest-rotation-with-highest-score/), [1674. Minimum Moves to Make Array Complementary](https://www.leetcode.com/problems/minimum-moves-to-make-array-complementary/).
- **Prefix sum (subarray sum / range query):** [560. Subarray Sum Equals K](https://www.leetcode.com/problems/subarray-sum-equals-k/), [325. Maximum Size Subarray Sum Equals k](https://www.leetcode.com/problems/maximum-size-subarray-sum-equals-k/), [974. Subarray Sums Divisible by K](https://www.leetcode.com/problems/subarray-sums-divisible-by-k/), [525. Contiguous Array](https://www.leetcode.com/problems/contiguous-array/), [303. Range Sum Query - Immutable](https://www.leetcode.com/problems/range-sum-query-immutable/).

---

## Thinking Process

1. **Difference array** turns “add d to [l, r]” into two point updates: +d at l, -d at r+1.

- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Prefix sum** *(this problem)* | $O(n)$ | $O(n)$ | Range queries, subarray sum |
| Sort + scan | $O(n \log n)$ | $O(1)$ | Intervals, meeting rooms |
| Kadane's algorithm | $O(n)$ | $O(1)$ | Maximum subarray |
| Hash map counting | $O(n)$ | $O(n)$ | Frequency, two-sum variants |

## Solution

For each booking, add `seats` to every flight in `[first, last]`.

```cpp
class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> rtn(n);
        for (auto& booking : bookings) {
            int left = booking[0] - 1, right = booking[1] - 1, seats = booking[2];
            while (left <= right) {
                rtn[left++] += seats;
            }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** 1. **Difference array** turns “add d to [l, r]” into two point updates: +d at l, -d at r+1.

**How the code works:**
1. **Difference array** turns “add d to [l, r]” into two point updates: +d at l, -d at r+1.
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

**Walkthrough** — input `bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5`, expected output `[10,55,45,25,25]`:

Flight 1: 10 seats
Flight 2: 10 + 20 + 25 = 55 seats
Flight 3: 20 + 25 = 45 seats
Flight 4: 25 seats
Flight 5: 25 seats

**Time:** O(m × L), where m = bookings.length, L = average range length (worst O(n)). · **Space:** O(n).
## Complexity Comparison

| Approach              | Time        | Space |
|-----------------------|-------------|--------|
| Brute force (range loop) | O(m × L)    | O(n)  |
| Difference + partial_sum / inclusive_scan | O(n + m) | O(n)  |

## Related Problems

- [1094. Car Pooling](https://www.leetcode.com/problems/car-pooling/) — Difference array on a timeline
- [560. Subarray Sum Equals K](https://www.leetcode.com/problems/subarray-sum-equals-k/) — Prefix sum + hash map
- [303. Range Sum Query - Immutable](https://www.leetcode.com/problems/range-sum-query-immutable/) — Prefix sum for range queries

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Difference array** turns “add d to [l, r]” into two point updates: +d at l, -d at r+1.
2. **Prefix sum** over the difference array recovers the final value at each index.
3. **C++ `partial_sum`** or **`inclusive_scan`** (C++17) compute prefix sums in one line; `inclusive_scan` can use execution policies for parallel scan.
4. Same pattern appears in Car Pooling (1094) and other “range update, single query pass” problems.

## References

- [LC 1109: Corporate Flight Bookings on LeetCode](https://www.leetcode.com/problems/corporate-flight-bookings/)
- [LeetCode Discuss — LC 1109: Corporate Flight Bookings](https://www.leetcode.com/problems/corporate-flight-bookings/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/corporate-flight-bookings/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
