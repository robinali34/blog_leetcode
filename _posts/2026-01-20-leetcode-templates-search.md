---
layout: post
title: "Algorithm Templates: Search"
date: 2026-01-20 00:00:00 -0700
categories: leetcode templates search binary-search
permalink: /posts/2026-01-20-leetcode-templates-search/
tags: [leetcode, templates, search, binary-search, divide-and-conquer]
---

{% raw %}
This page collects ready-to-use C++ templates for every major binary search pattern you'll encounter on LeetCode — from basic sorted-array lookup to rotated arrays, 2D matrices, and "search on the answer" optimization problems. Each section includes the template, a quick "when to use" guide, and a curated problem list so you can drill the pattern immediately. Templates match the [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/#binary-search-bounds) lower/upper bound style.

> **New to Binary Search?** Binary search cuts the search space in half at each step, giving O(log n) time. The key: you need a *monotonic condition* — some property that's false on one side and true on the other.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 290" style="max-width:640px;font-family:system-ui,sans-serif;margin:1.5em auto;display:block">
<style>
.c{fill:#E8E0D8;stroke:#B8ACA0;stroke-width:1.5}
.v{font-size:14px;fill:#5A5252;text-anchor:middle;dominant-baseline:central}
.lb{font-size:11px;font-weight:600;text-anchor:middle}
.st{font-size:12px;fill:#5A5252;font-weight:600}
.nt{font-size:11px;fill:#8A7E7E;font-style:italic}
.lo{fill:#8EA4B8}.hi{fill:#C4A4A4}.mi{fill:#B8A4B8}.fd{fill:#A4B8A4}
.dm{opacity:.35}
</style>
<text x="320" y="18" class="v" font-size="15" font-weight="700">Binary Search: find 15 in [2, 5, 8, 11, 15, 18, 22]</text>
<text x="10" y="55" class="st">Step 1</text>
<g transform="translate(80,35)">
  <rect class="c lo" width="58" height="30" rx="4"/><rect class="c" x="66" width="58" height="30" rx="4"/>
  <rect class="c" x="132" width="58" height="30" rx="4"/><rect class="c mi" x="198" width="58" height="30" rx="4"/>
  <rect class="c" x="264" width="58" height="30" rx="4"/><rect class="c" x="330" width="58" height="30" rx="4"/>
  <rect class="c hi" x="396" width="58" height="30" rx="4"/>
  <text class="v" x="29" y="15">2</text><text class="v" x="95" y="15">5</text><text class="v" x="161" y="15">8</text>
  <text class="v" x="227" y="15">11</text><text class="v" x="293" y="15">15</text>
  <text class="v" x="359" y="15">18</text><text class="v" x="425" y="15">22</text>
  <text class="lb lo" x="29" y="46">lo</text><text class="lb mi" x="227" y="46">mid</text><text class="lb hi" x="425" y="46">hi</text>
</g>
<text x="560" y="55" class="nt">11 &lt; 15 → right</text>
<text x="10" y="145" class="st">Step 2</text>
<g transform="translate(80,125)">
  <rect class="c dm" width="58" height="30" rx="4"/><rect class="c dm" x="66" width="58" height="30" rx="4"/>
  <rect class="c dm" x="132" width="58" height="30" rx="4"/><rect class="c dm" x="198" width="58" height="30" rx="4"/>
  <rect class="c lo" x="264" width="58" height="30" rx="4"/><rect class="c mi" x="330" width="58" height="30" rx="4"/>
  <rect class="c hi" x="396" width="58" height="30" rx="4"/>
  <text class="v dm" x="29" y="15">2</text><text class="v dm" x="95" y="15">5</text><text class="v dm" x="161" y="15">8</text>
  <text class="v dm" x="227" y="15">11</text><text class="v" x="293" y="15">15</text>
  <text class="v" x="359" y="15">18</text><text class="v" x="425" y="15">22</text>
  <text class="lb lo" x="293" y="46">lo</text><text class="lb mi" x="359" y="46">mid</text><text class="lb hi" x="425" y="46">hi</text>
</g>
<text x="560" y="145" class="nt">18 &gt; 15 → left</text>
<text x="10" y="235" class="st">Step 3</text>
<g transform="translate(80,215)">
  <rect class="c dm" width="58" height="30" rx="4"/><rect class="c dm" x="66" width="58" height="30" rx="4"/>
  <rect class="c dm" x="132" width="58" height="30" rx="4"/><rect class="c dm" x="198" width="58" height="30" rx="4"/>
  <rect class="c fd" x="264" width="58" height="30" rx="4" stroke="#7A9E7A" stroke-width="2.5"/>
  <rect class="c dm" x="330" width="58" height="30" rx="4"/><rect class="c dm" x="396" width="58" height="30" rx="4"/>
  <text class="v dm" x="29" y="15">2</text><text class="v dm" x="95" y="15">5</text><text class="v dm" x="161" y="15">8</text>
  <text class="v dm" x="227" y="15">11</text><text class="v" x="293" y="15" font-weight="700">15</text>
  <text class="v dm" x="359" y="15">18</text><text class="v dm" x="425" y="15">22</text>
  <text class="lb" x="293" y="46" fill="#5A8A5A" font-weight="700">found!</text>
</g>
<text x="560" y="235" class="nt">15 = target ✓</text>
<g transform="translate(140,270)">
  <rect class="lo" width="12" height="12" rx="2"/><text class="v" x="22" y="6" text-anchor="start" font-size="11">lo</text>
  <rect class="mi" x="55" width="12" height="12" rx="2"/><text class="v" x="77" y="6" text-anchor="start" font-size="11">mid</text>
  <rect class="hi" x="120" width="12" height="12" rx="2"/><text class="v" x="142" y="6" text-anchor="start" font-size="11">hi</text>
  <rect class="fd" x="185" width="12" height="12" rx="2"/><text class="v" x="207" y="6" text-anchor="start" font-size="11">found</text>
</g>
</svg>

## Contents

- [Basic binary search](#basic-binary-search)
- [Binary search on rotated array](#binary-search-on-rotated-array)
- [Binary search on answer](#binary-search-on-answer)
- [Search in 2D matrix](#search-in-2d-matrix)
- [Advanced](#advanced)
- [Quick Reference](#quick-reference)
- [More templates](#more-templates)

## Basic binary search

**When to use:** You see "find target in sorted array", "first/last occurrence", "search insert position", or need the boundary of a condition in a sorted sequence.

Standard: `[0, n-1]`, `left <= right`. Lower/upper bound: `[0, n]`, `left < right` — same as [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/#binary-search-bounds).

```cpp
int bsearch(const vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

int lower_bound(const vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int upper_bound(const vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] <= target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

vector<int> searchRange(vector<int>& nums, int target) {
    int first = lower_bound(nums, target);
    if (first == (int)nums.size() || nums[first] != target) return {-1, -1};
    return {first, upper_bound(nums, target) - 1};
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 704 | Binary Search | [Link](https://leetcode.com/problems/binary-search/) | - |
| 34 | Find First and Last Position | [Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | - |
| 35 | Search Insert Position | [Link](https://leetcode.com/problems/search-insert-position/) | - |
| 528 | Random Pick with Weight | [Link](https://leetcode.com/problems/random-pick-with-weight/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-528-random-pick-with-weight/) |
| 300 | Longest Increasing Subsequence | [Link](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-300-longest-increasing-subsequence/) |
| 673 | Number of Longest Increasing Subsequence | [Link](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/09/medium-673-number-of-longest-increasing-subsequence/) |

## Binary search on rotated array

**When to use:** Problem says "rotated sorted array", or you need to find a target or minimum in an array that was sorted then rotated.

```cpp
int search_rotated(const vector<int>& nums, int target) {
    int lo = 0, hi = (int)nums.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] >= nums[lo]) {
            if (target >= nums[lo] && target < nums[mid]) hi = mid - 1;
            else lo = mid + 1;
        } else {
            if (target > nums[mid] && target <= nums[hi]) lo = mid + 1;
            else hi = mid - 1;
        }
    }
    return -1;
}

int findMin_rotated(const vector<int>& nums) {
    int lo = 0, hi = (int)nums.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] > nums[hi]) lo = mid + 1;
        else hi = mid;
    }
    return nums[lo];
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 33 | Search in Rotated Sorted Array | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/23/medium-33-search-in-rotated-sorted-array/) |
| 81 | Search in Rotated Sorted Array II | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | - |
| 153 | Find Minimum in Rotated Sorted Array | [Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | - |
| 154 | Find Minimum in Rotated Sorted Array II | [Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | - |

## Binary search on answer

**When to use:** You see "minimize maximum", "maximum minimum", "minimum capacity/speed", or any optimization where you can check feasibility for a given answer value.

Min valid: `lo < hi`, `hi = mid` when valid. Max valid: `lo < hi`, `mid = lo + (hi - lo + 1) / 2`, `lo = mid` when valid.

```cpp
int minValid(int lo, int hi) {
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (valid(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}

int maxValid(int lo, int hi) {
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        if (valid(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}

// Example: Koko Eating Bananas (875)
int minEatingSpeed(vector<int>& piles, int h) {
    int lo = 1, hi = *max_element(piles.begin(), piles.end());
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int hours = 0;
        for (int p : piles) hours += (p + mid - 1) / mid;
        if (hours <= h) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 875 | Koko Eating Bananas | [Link](https://leetcode.com/problems/koko-eating-bananas/) | - |
| 1011 | Capacity To Ship Packages | [Link](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | - |
| 410 | Split Array Largest Sum | [Link](https://leetcode.com/problems/split-array-largest-sum/) | - |

## Search in 2D matrix

**When to use:** Problem says "search in matrix" or "sorted matrix". Use staircase for row/col sorted matrices, flatten-to-1D for fully sorted row-major layouts.

Row/col sorted (240): start top-right, move left or down. Fully sorted row-major (74): flatten to 1D and binary search.

```cpp
bool search2D_rc(const vector<vector<int>>& mat, int target) {
    int m = mat.size(), n = mat[0].size();
    int r = 0, c = n - 1;
    while (r < m && c >= 0) {
        if (mat[r][c] == target) return true;
        if (mat[r][c] > target) c--;
        else r++;
    }
    return false;
}

bool search2D_flat(const vector<vector<int>>& mat, int target) {
    int m = mat.size(), n = mat[0].size();
    int lo = 0, hi = m * n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int v = mat[mid / n][mid % n];
        if (v == target) return true;
        if (v < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return false;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 74 | Search a 2D Matrix | [Link](https://leetcode.com/problems/search-a-2d-matrix/) | - |
| 240 | Search a 2D Matrix II | [Link](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/07/medium-240-search-a-2d-matrix-ii/) |
| 270 | Closest Binary Search Tree Value | [Link](https://leetcode.com/problems/closest-binary-search-tree-value/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/easy-270-closest-binary-search-tree-value/) |

## Advanced

**When to use:** Standard binary search won't cut it — you need divide-and-conquer counting (inversions, range sums), ternary search on unimodal functions, or exponential search on unbounded arrays.

**Merge sort on prefix sums (327, 315):** Build prefix array, divide-and-conquer merge sort; for each right-half index j count left-half indices i with `prefix[j]-upper <= prefix[i] <= prefix[j]-lower` using two pointers. O(n log n).

**Divide-and-conquer with counting:** Recurse left/right, count cross pairs (e.g. inversions, reverse pairs), merge. See 493 Reverse Pairs, 315 Count Smaller.

**Ternary search (unimodal):** Split range in thirds; for max, move toward the higher side. Integer: when range ≤ 3, scan. E.g. 1515 Best Position for a Service Centre.

**Exponential search (702):** Double index until past target, then binary search in `[i/2, min(i,n-1)]`.

**Tree-based:** Segment tree / Fenwick: [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/), [Trees](/posts/2025-10-29-leetcode-templates-trees/) (tree walk, lazy segment, BIT).

| ID | Title | Link |
|----|--------|------|
| 327 | Count of Range Sum | [Link](https://leetcode.com/problems/count-of-range-sum/) |
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 493 | Reverse Pairs | [Link](https://leetcode.com/problems/reverse-pairs/) |
| 702 | Search in a Sorted Array of Unknown Size | [Link](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) |

## Quick Reference

| Pattern | Signal Phrases | Key Insight |
|---|---|---|
| Basic | "find target in sorted array" | Standard lo/hi convergence |
| Lower/Upper Bound | "first/last occurrence" | `lo < hi` with half-open range |
| Rotated Array | "rotated sorted array" | One half is always sorted |
| Search on Answer | "minimize maximum", "capacity" | Binary search on the answer value |
| 2D Matrix | "search in matrix" | Treat as 1D or staircase search |

## More templates

- **Data structures (binary search bounds, prefix sum, segment tree, BIT):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph (BFS, Dijkstra, topo):** [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)

{% endraw %}
