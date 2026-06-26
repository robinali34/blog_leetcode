---
layout: post
title: "[Medium] 274. H-Index"
date: 2026-04-17
categories: [leetcode, medium, sorting]
tags: [leetcode, medium, array, sorting, counting-sort, greedy]
permalink: /2026/04/17/medium-274-h-index/
---
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`-th paper, return the researcher's **h-index**.

The h-index is defined as: the maximum value of `h` such that the researcher has published at least `h` papers that have each been cited at least `h` times.

## Examples

**Example 1:**

```
Input: citations = [3, 0, 6, 1, 5]
Output: 3

Sort descending: [6, 5, 3, 1, 0]

  i (papers seen)   citations[i]   >= i+1 ?
  1                 6              >= 1  YES
  2                 5              >= 2  YES
  3                 3              >= 3  YES
  4                 1              >= 4  NO   ← stop

Answer = 3 (3 papers with >= 3 citations each)
```

**Example 2:**

```
Input: citations = [1, 3, 1]
Output: 1
```

## Constraints

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

## Thinking Process

### What Are We Really Looking For?

This is **not** about total citations. It's about finding a **balance point**: the largest `h` where at least `h` papers have `>= h` citations.

### Why Sorting Works

After sorting in descending order:
- **Position `i+1`** = number of papers we've seen so far
- **Value `citations[i]`** = the citation count of the current paper

At each position, we're asking: "Does this paper have enough citations to support the current count of papers?"

The moment `citations[i] < i + 1`, the balance breaks and we've found our answer.

```
Sorted: [6, 5, 3, 1, 0]

Index 0: 6 >= 1  →  at least 1 paper with >= 1 citations  ✓
Index 1: 5 >= 2  →  at least 2 papers with >= 2 citations ✓
Index 2: 3 >= 3  →  at least 3 papers with >= 3 citations ✓
Index 3: 1 >= 4  →  at least 4 papers with >= 4 citations ✗  ← STOP

h = 3
```

### Can We Do Better Than $O(n \log n)$?

Yes -- since `h` can be at most `n`, we can use counting sort to get $O(n)$.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | $O(n \log n)$ | $O(1)$ | Interval scheduling, assignment |
| Local greedy choice | $O(n)$ | $O(1)$ | Jump game, gas station |
| Greedy + heap | $O(n \log n)$ | $O(n)$ | Merge streams, room allocation |
| Exchange argument | $O(n)$ | $O(1)$ | Prove greedy choice is safe |

## Solution

{% raw %}
```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end(), greater<int>());
        for (int i = 0; i < citations.size(); ++i) {
            if (citations[i] < i + 1) return i;
        }
        return citations.size();
    }
};
```

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** ### What Are We Really Looking For?

**How the code works:**
- **Position `i+1`** = number of papers we've seen so far
- **Value `citations[i]`** = the citation count of the current paper

**Walkthrough** — input `citations = [3, 0, 6, 1, 5]`, expected output `3`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Comparison

| Aspect | Sorting | Counting Sort |
|---|---|---|
| Time | $O(n \log n)$ | $O(n)$ |
| Space | $O(1)$ (in-place sort) | $O(n)$ (frequency array) |
| Interview preference | Most common, easy to explain | Good follow-up for optimization |
| Key idea | Descending order gives "papers seen" naturally | Bucket citations, scan from top |

## Common Mistakes

- **Confusing h-index with max citations:** `h` is bounded by the number of papers, not the citation values
- **Off-by-one in sorting approach:** Position `i` means `i + 1` papers (0-indexed), so the check is `citations[i] < i + 1`
- **Forgetting the `min(c, n)` clamp in counting sort:** Any citation count `>= n` is equivalent since `h <= n`

## Key Takeaways

- The h-index is a **balance point** between quantity (number of papers) and quality (citation count)
- Sort descending and scan gives the most intuitive solution
- Counting sort exploits the fact that `h <= n` to achieve linear time
- This pattern of "find the largest k satisfying a threshold" appears in many problems

## Related Problems

- [275. H-Index II](https://www.leetcode.com/problems/h-index-ii/) -- sorted input, use binary search for $O(\log n)$
- [287. Find the Duplicate Number](https://www.leetcode.com/problems/find-the-duplicate-number/) -- counting / pigeonhole
- [169. Majority Element](https://www.leetcode.com/problems/majority-element/) -- finding a threshold in an array

## References

- [LC 274: H-Index on LeetCode](https://www.leetcode.com/problems/h-index/)
- [LeetCode Discuss — LC 274: H-Index](https://www.leetcode.com/problems/h-index/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/h-index/editorial/) *(may require premium)*

## Template Reference

- [Greedy (Sorting + Greedy)](/blog_leetcode/posts/2025-12-14-leetcode-templates-greedy/)
- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
