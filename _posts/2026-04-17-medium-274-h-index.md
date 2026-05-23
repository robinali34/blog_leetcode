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

## Solution 1: Sort Descending -- $O(n \log n)$ time, $O(1)$ space

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
{% endraw %}

If every paper has enough citations, the loop finishes without returning, and `h = n`.

## Solution 2: Counting Sort -- $O(n)$ time, $O(n)$ space

{% raw %}
```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int> count(n + 1, 0);

        for (int c : citations) {
            count[min(c, n)]++;
        }

        int total = 0;
        for (int h = n; h >= 0; --h) {
            total += count[h];
            if (total >= h) return h;
        }
        return 0;
    }
};
```
{% endraw %}

### How It Works

1. **Build a frequency array** `count[i]` = number of papers with exactly `i` citations. Papers with `>= n` citations are bucketed into `count[n]` since `h` can never exceed `n`.

2. **Scan from `h = n` down to 0**, accumulating the total number of papers with `>= h` citations. The first `h` where `total >= h` is the answer.

```
citations = [3, 0, 6, 1, 5],  n = 5

count:  index  0  1  2  3  4  5
        value  1  1  0  1  0  2   (6 and 5 both go into bucket 5)

Scan from h=5:  total=2, 2 >= 5?  no
      h=4:  total=2, 2 >= 4?  no
      h=3:  total=3, 3 >= 3?  YES → return 3
```

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

- [275. H-Index II](https://leetcode.com/problems/h-index-ii/) -- sorted input, use binary search for $O(\log n)$
- [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) -- counting / pigeonhole
- [169. Majority Element](https://leetcode.com/problems/majority-element/) -- finding a threshold in an array
