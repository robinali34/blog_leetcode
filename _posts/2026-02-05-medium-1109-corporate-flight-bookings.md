---
layout: post
title: "1109. Corporate Flight Bookings"
date: 2026-02-05 00:00:00 -0700
categories: [leetcode, medium, array, prefix-sum, difference-array]
permalink: /2026/02/05/medium-1109-corporate-flight-bookings/
tags: [leetcode, medium, array, prefix-sum, difference-array]
---

# 1109. Corporate Flight Bookings

## Problem Statement

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

## Clarification Questions

1. **Indexing**: Are flight numbers 1-indexed? (Yes — flights are 1 to n; answer[i] is for flight i+1.)
2. **Overlapping bookings**: Can the same flight appear in multiple bookings? (Yes — we sum all reserved seats.)
3. **Range**: Is [first, last] inclusive on both ends? (Yes.)

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

- **Difference array (range update, then prefix sum):** [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/), [1094. Car Pooling](https://leetcode.com/problems/car-pooling/), [798. Smallest Rotation with Highest Score](https://leetcode.com/problems/smallest-rotation-with-highest-score/), [1674. Minimum Moves to Make Array Complementary](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/).
- **Prefix sum (subarray sum / range query):** [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/), [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/), [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/), [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/), [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/).

---

## Interview Deduction Process

**Step 1: Brute force** — For each booking, loop from `first` to `last` and add `seats` to each index. Time O(bookings × range length), which can be O(n × m). Space O(n).

**Step 2: Optimized** — Use a difference array: for each `[first, last, seats]`, add `seats` at `first-1` and subtract `seats` at `last` (0-indexed: `last` is the index after the last flight). Then one pass of prefix sum (e.g. `partial_sum`) gives the answer. Time O(n + m), space O(n).

## Solution 1: Brute Force (Range Loop)

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

- **Time:** O(m × L), where m = bookings.length, L = average range length (worst O(n)).
- **Space:** O(n).

## Solution 2: Difference Array + `partial_sum`

Mark each range with a +d at the start and -d at the position after the end; then prefix sum recovers the counts.

```cpp
class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> rtn(n + 1);
        for (auto& b : bookings) {
            int first = b[0] - 1, last = b[1], seats = b[2];
            rtn[first] += seats;
            rtn[last] -= seats;
        }
        partial_sum(rtn.begin(), rtn.end(), rtn.begin());
        rtn.pop_back();
        return rtn;
    }
};
```

- **Indexing:** Flights 1..n → indices 0..n-1. Booking `[first, last]` (1-indexed) → indices `first-1 .. last-1`. We add at `first-1` and subtract at `last` so that the prefix sum at index `i` is the total seats for flight `i+1`. The extra `rtn[n]` is only used for the subtraction; we drop it with `pop_back()`.
- **Time:** O(n + m).
- **Space:** O(n).

### Algorithm breakdown

1. Allocate `rtn(n + 1)` (extra slot for the “after last” offset).
2. For each `[first, last, seats]`: `rtn[first-1] += seats`, `rtn[last] -= seats`.
3. `partial_sum(rtn.begin(), rtn.end(), rtn.begin())` to get cumulative counts.
4. `rtn.pop_back()` so the result has length `n`.

### Why it works

After all updates, the value at index `i` in the result is the sum of all +d and -d that apply to position `i`. Each booking adds +d at the start and -d just after the end, so the running sum at `i` equals the total seats reserved for flight `i+1`.

### Variant: `std::inclusive_scan` (C++17)

Same difference-array idea; use `inclusive_scan` instead of `partial_sum`. Both compute the inclusive prefix sum; `inclusive_scan` supports execution policies (e.g. `std::execution::par`) for parallel scan when needed.

```cpp
class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> rtn(n + 1);
        for (auto& b : bookings) {
            int first = b[0] - 1, last = b[1], seats = b[2];
            rtn[first] += seats;
            rtn[last] -= seats;
        }
        inclusive_scan(rtn.begin(), rtn.end(), rtn.begin());
        rtn.pop_back();
        return rtn;
    }
};
```

Include `<numeric>` (and optionally `<execution>` for `std::execution::par`). Time and space same as the `partial_sum` version.

### Variant: Length-`n` array + manual prefix sum (LeetCode China official)

Use a single array of length `n`. Only subtract at index `booking[1]` when `booking[1] < n`, so no extra slot is needed; then run a manual prefix-sum loop. No STL scan or `pop_back`.

```cpp
class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> nums(n);
        for (auto& booking : bookings) {
            nums[booking[0] - 1] += booking[2];
            if (booking[1] < n) {
                nums[booking[1]] -= booking[2];
            }
        }
        for (int i = 1; i < n; i++) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};
```

- **Indexing:** Add at `first - 1`; subtract at `last` only when `last < n` (so we never write to index `n`). Then `nums[i] += nums[i-1]` is the inclusive prefix sum in place.
- **Time:** O(n + m). **Space:** O(n).

*Source: [力扣官方题解](https://leetcode.cn/problems/corporate-flight-bookings/solutions/968214/hang-ban-yu-ding-tong-ji-by-leetcode-sol-5pv8/) (LeetCode China official solution).*

## Complexity Comparison

| Approach              | Time        | Space |
|-----------------------|-------------|--------|
| Brute force (range loop) | O(m × L)    | O(n)  |
| Difference + partial_sum / inclusive_scan | O(n + m) | O(n)  |

## Key Insights

1. **Difference array** turns “add d to [l, r]” into two point updates: +d at l, -d at r+1.
2. **Prefix sum** over the difference array recovers the final value at each index.
3. **C++ `partial_sum`** or **`inclusive_scan`** (C++17) compute prefix sums in one line; `inclusive_scan` can use execution policies for parallel scan.
4. Same pattern appears in Car Pooling (1094) and other “range update, single query pass” problems.

## Related Problems

- [1094. Car Pooling](https://leetcode.com/problems/car-pooling/) — Difference array on a timeline
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — Prefix sum + hash map
- [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) — Prefix sum for range queries
