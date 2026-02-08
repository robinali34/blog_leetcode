---
layout: post
title: "Algorithm Templates: Search"
date: 2026-01-20 00:00:00 -0700
categories: leetcode templates search binary-search
permalink: /posts/2026-01-20-leetcode-templates-search/
tags: [leetcode, templates, search, binary-search, divide-and-conquer]
---

{% raw %}
Minimal, copy-paste C++ for binary search, rotated arrays, 2D search, and answer-space search. Matches [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/#binary-search-bounds) lower/upper bound style.

## Contents

- [Basic binary search](#basic-binary-search)
- [Binary search on rotated array](#binary-search-on-rotated-array)
- [Binary search on answer](#binary-search-on-answer)
- [Search in 2D matrix](#search-in-2d-matrix)
- [Advanced](#advanced)
- [More templates](#more-templates)

## Basic binary search

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

## More templates

- **Data structures (binary search bounds, prefix sum, segment tree, BIT):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph (BFS, Dijkstra, topo):** [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)

{% endraw %}
