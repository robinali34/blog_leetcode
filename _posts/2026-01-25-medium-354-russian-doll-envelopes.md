---
layout: post
title: "[Medium] 354. Russian Doll Envelopes"
date: 2026-01-25 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming, binary-search, sorting]
permalink: /2026/01/25/medium-354-russian-doll-envelopes/
tags: [leetcode, medium, array, dynamic-programming, binary-search, sorting, longest-increasing-subsequence]
---
You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi, hi]` represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return *the maximum number of envelopes you can Russian doll* (i.e., put one inside the other).

**Note:** You cannot rotate an envelope.

## Examples

**Example 1:**

```
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

**Example 2:**

```
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
Explanation: No envelope can fit into another envelope.
```

## Constraints

- `1 <= envelopes.length <= 10^5`
- `envelopes[i].length == 2`
- `1 <= wi, hi <= 10^5`

## Thinking Process

1. **2D LIS Problem**: This is essentially finding LIS in 2D space

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
| **Standard binary search** *(this problem)* | O(log n) | O(1) | Sorted array, `left <= right` |
| Lower / upper bound | O(log n) | O(1) | First/last position, insert index |
| Binary search on rotated array | O(log n) | O(1) | Identify sorted half, discard other |
| Binary search on answer | O(n log M) | O(1) | Monotonic predicate over search space |

## Solution

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if(envelopes.empty()) return 0;
        const int N = envelopes.size();
        sort(envelopes.begin(), envelopes.end(), [](const auto& e1, const auto& e2) {
            return e1[0] < e2[0] || (e1[0] == e2[0] && e1[1] > e2[1]);
        });

        vector<int> dp = {envelopes[0][1]};
        for(int i = 1; i < N; i++) {
            int num = envelopes[i][1];
            if(num > dp.back()) {
                dp.push_back(num);
            } else {
                auto it = lower_bound(dp.begin(), dp.end(), num);
                *it = num;
            }
        }
        return dp.size();
    }
};
```

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **2D LIS Problem**: This is essentially finding LIS in 2D space

**How the code works:**
1. **2D LIS Problem**: This is essentially finding LIS in 2D space
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

**Walkthrough** — input `envelopes = [[5,4],[6,4],[6,7],[2,3]]`, expected output `3`:

The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
## Common Mistakes

1. **Empty input**: `envelopes = []` → return `0`
2. **Single envelope**: `envelopes = [[1,1]]` → return `1`
3. **All same size**: `envelopes = [[1,1],[1,1],[1,1]]` → return `1`
4. **No valid chain**: All envelopes have same width → return `1`
5. **Perfect chain**: Envelopes form a perfect chain → return `n`

1. **Wrong sorting order**: Not sorting heights descending for equal widths
2. **Using strict inequality**: Must use `>` not `>=` for fitting condition
3. **Not handling empty input**: Should return `0` for empty array
4. **Wrong LIS implementation**: Not using binary search optimization
5. **Forgetting equal width constraint**: Multiple envelopes with same width can't be in chain

## Related Problems

- [LC 300: Longest Increasing Subsequence](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-300-longest-increasing-subsequence/) - 1D LIS problem
- [LC 673: Number of Longest Increasing Subsequence](https://robinali34.github.io/blog_leetcode/2026/01/09/medium-673-number-of-longest-increasing-subsequence/) - Count number of LIS
- [LC 646: Maximum Length of Pair Chain](https://www.leetcode.com/problems/maximum-length-of-pair-chain/) - Similar interval chaining
- [LC 334: Increasing Triplet Subsequence](https://www.leetcode.com/problems/increasing-triplet-subsequence/) - Check if triplet exists

## Key Takeaways

1. **2D LIS Problem**: This is essentially finding LIS in 2D space
2. **Sorting Strategy**: Sort by one dimension, then find LIS on the other
3. **Equal Width Handling**: Sort heights descending for equal widths to prevent invalid chains
4. **Binary Search Optimization**: Use `lower_bound` for O(log n) insertion
5. **Greedy Approach**: Maintain smallest tail elements for each subsequence length

## References

- [LC 354: Russian Doll Envelopes on LeetCode](https://www.leetcode.com/problems/russian-doll-envelopes/)
- [LeetCode Discuss — LC 354: Russian Doll Envelopes](https://www.leetcode.com/problems/russian-doll-envelopes/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/russian-doll-envelopes/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
