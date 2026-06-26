---
layout: post
title: "Algorithm Templates: Arrays & Strings"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates arrays strings
permalink: /posts/2025-10-29-leetcode-templates-arrays-strings/
tags: [leetcode, templates, arrays, strings]
---
Arrays and strings are the foundation of coding interviews — you'll encounter them in nearly every problem set. This page provides battle-tested C++ templates for the most important patterns: sliding window, two pointers, binary search on answer, prefix sum, hash maps, and string algorithms like KMP and Manacher. Master these and you'll have the tools to solve a huge fraction of Medium-level problems.

> **This template covers the fundamental patterns for array and string problems.** Sliding window, two pointers, and prefix sum together solve a huge fraction of Medium problems.

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)

## Contents

- [Sliding Window (fixed/variable)](#sliding-window-fixedvariable)
- [Two Pointers (sorted arrays/strings)](#two-pointers-sorted-arraysstrings)
- [Binary Search on Answer](#binary-search-on-answer-monotonic-predicate)
- [Prefix Sum / Difference Array](#prefix-sum--difference-array)
- [Hash Map Frequencies](#hash-map-frequencies)
- [KMP (Substring Search)](#kmp-substring-search)
- [Manacher](#manacher-longest-palindromic-substring-on)
- [Z-Algorithm](#z-algorithm-pattern-occurrences)
- [String Rolling Hash](#string-rolling-hash-rabin–karp)

## Sliding Window (fixed/variable)

**When to use:** "longest substring", "shortest subarray", "at most k distinct", or any problem asking for a contiguous subrange that satisfies a constraint.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 260" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <rect width="700" height="260" rx="12" fill="#FAF8F5"/>
  <text x="350" y="22" text-anchor="middle" font-size="14" font-weight="bold" fill="#3A3530">Sliding Window — Longest Substring Without Repeating</text>
  <g font-size="8" fill="#9A9792" text-anchor="middle">
    <text x="72" y="40">0</text><text x="109" y="40">1</text><text x="146" y="40">2</text><text x="183" y="40">3</text>
    <text x="220" y="40">4</text><text x="257" y="40">5</text><text x="294" y="40">6</text><text x="331" y="40">7</text>
  </g>
  <g transform="translate(0, 44)">
    <text x="20" y="18" font-size="10" fill="#7A7772">#1</text>
    <rect x="55" y="0" width="34" height="26" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="72" y="18" text-anchor="middle" font-size="12" fill="#3A3530">a</text>
    <rect x="92" y="0" width="34" height="26" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="109" y="18" text-anchor="middle" font-size="12" fill="#3A3530">b</text>
    <rect x="129" y="0" width="34" height="26" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="146" y="18" text-anchor="middle" font-size="12" fill="#3A3530">c</text>
    <rect x="166" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="183" y="18" text-anchor="middle" font-size="12" fill="#9A9792">a</text>
    <rect x="203" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="220" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="240" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="257" y="18" text-anchor="middle" font-size="12" fill="#9A9792">c</text>
    <rect x="277" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="294" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="314" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="331" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="53" y="-4" width="112" height="34" rx="5" fill="none" stroke="#8B8680" stroke-width="1.5" stroke-dasharray="5,3"/>
    <text x="380" y="12" font-size="11" fill="#5A5752">expand → window "abc", len = 3</text>
    <text x="380" y="26" font-size="10" fill="#7A7772">seen: {a, b, c}</text>
  </g>
  <g transform="translate(0, 99)">
    <text x="20" y="18" font-size="10" fill="#7A7772">#2</text>
    <rect x="55" y="0" width="34" height="26" rx="3" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="72" y="18" text-anchor="middle" font-size="12" fill="#3A3530">a</text>
    <rect x="92" y="0" width="34" height="26" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="109" y="18" text-anchor="middle" font-size="12" fill="#3A3530">b</text>
    <rect x="129" y="0" width="34" height="26" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="146" y="18" text-anchor="middle" font-size="12" fill="#3A3530">c</text>
    <rect x="166" y="0" width="34" height="26" rx="3" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="183" y="18" text-anchor="middle" font-size="12" fill="#3A3530">a</text>
    <rect x="203" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="220" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="240" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="257" y="18" text-anchor="middle" font-size="12" fill="#9A9792">c</text>
    <rect x="277" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="294" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="314" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="331" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="53" y="-4" width="149" height="34" rx="5" fill="none" stroke="#B8B5B0" stroke-width="1.5" stroke-dasharray="5,3"/>
    <text x="380" y="12" font-size="11" fill="#5A5752">expand → "abca" — 'a' repeats!</text>
    <text x="380" y="26" font-size="10" fill="#7A7772">shrink left to remove duplicate</text>
  </g>
  <g transform="translate(0, 154)">
    <text x="20" y="18" font-size="10" fill="#7A7772">#3</text>
    <rect x="55" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="72" y="18" text-anchor="middle" font-size="12" fill="#9A9792">a</text>
    <rect x="92" y="0" width="34" height="26" rx="3" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="109" y="18" text-anchor="middle" font-size="12" fill="#3A3530">b</text>
    <rect x="129" y="0" width="34" height="26" rx="3" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="146" y="18" text-anchor="middle" font-size="12" fill="#3A3530">c</text>
    <rect x="166" y="0" width="34" height="26" rx="3" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="183" y="18" text-anchor="middle" font-size="12" fill="#3A3530">a</text>
    <rect x="203" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="220" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="240" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="257" y="18" text-anchor="middle" font-size="12" fill="#9A9792">c</text>
    <rect x="277" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="294" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="314" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="331" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="90" y="-4" width="112" height="34" rx="5" fill="none" stroke="#8B8680" stroke-width="1.5" stroke-dasharray="5,3"/>
    <text x="380" y="12" font-size="11" fill="#5A5752">shrink → "bca", len = 3</text>
    <text x="380" y="26" font-size="10" fill="#7A7772">no duplicates, continue expanding</text>
  </g>
  <g transform="translate(0, 209)">
    <text x="20" y="18" font-size="10" fill="#7A7772">#4</text>
    <rect x="55" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="72" y="18" text-anchor="middle" font-size="12" fill="#9A9792">a</text>
    <rect x="92" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="109" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="129" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="146" y="18" text-anchor="middle" font-size="12" fill="#9A9792">c</text>
    <rect x="166" y="0" width="34" height="26" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="183" y="18" text-anchor="middle" font-size="12" fill="#3A3530">a</text>
    <rect x="203" y="0" width="34" height="26" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="220" y="18" text-anchor="middle" font-size="12" fill="#3A3530">b</text>
    <rect x="240" y="0" width="34" height="26" rx="3" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="257" y="18" text-anchor="middle" font-size="12" fill="#3A3530">c</text>
    <rect x="277" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="294" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="314" y="0" width="34" height="26" rx="3" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
    <text x="331" y="18" text-anchor="middle" font-size="12" fill="#9A9792">b</text>
    <rect x="164" y="-4" width="112" height="34" rx="5" fill="none" stroke="#8B8680" stroke-width="1.5" stroke-dasharray="5,3"/>
    <text x="380" y="12" font-size="11" fill="#5A5752">expand → "abc", len = 3</text>
    <text x="380" y="26" font-size="10" fill="#3A3530" font-weight="bold">max length = 3</text>
  </g>
</svg>
</div>

```cpp
// Variable-size window (e.g., longest substring without repeating)
int longestNoRepeat(const string& s){
    vector<int> cnt(256, 0);
    int dup = 0, best = 0;
    for (int l = 0, r = 0; r < (int)s.size(); ++r){
        dup += (++cnt[(unsigned char)s[r]] == 2);
        while (dup > 0){
            dup -= (--cnt[(unsigned char)s[l++]] == 1);
        }
        best = max(best, r - l + 1);
    }
    return best;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 3 | Longest Substring Without Repeating Characters | [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) |
| 76 | Minimum Window Substring | [Link](https://leetcode.com/problems/minimum-window-substring/) | - |
| 392 | Is Subsequence | [Link](https://leetcode.com/problems/is-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/easy-392-is-subsequence/) |
| 424 | Longest Repeating Character Replacement | [Link](https://leetcode.com/problems/longest-repeating-character-replacement/) | - |
| 616 | Add Bold Tag in String | [Link](https://leetcode.com/problems/add-bold-tag-in-string/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/medium-616-add-bold-tag-in-string/) |
| 681 | Next Closest Time | [Link](https://leetcode.com/problems/next-closest-time/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/medium-681-next-closest-time/) |
| 713 | Subarray Product Less Than K | [Link](https://leetcode.com/problems/subarray-product-less-than-k/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/21/medium-713-subarray-product-less-than-k/) |
| 2461 | Maximum Sum of Distinct Subarrays With Length K | [Link](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/09/medium-2461-maximum-sum-of-distinct-subarrays-with-length-k/) |

## Two Pointers (sorted arrays/strings)

**When to use:** "pair with target sum in sorted array", "container with most water", "valid palindrome", or when the array is sorted and you can shrink the search space from both ends.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 210" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <rect width="700" height="210" rx="12" fill="#FAF8F5"/>
  <text x="350" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#3A3530">Two Pointers — Find Pair with Target Sum = 9</text>
  <g font-size="14" text-anchor="middle">
    <rect x="154" y="42" width="48" height="40" rx="5" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="178" y="68" fill="#9A9792">1</text>
    <text x="178" y="94" font-size="9" fill="#9A9792">0</text>
    <rect x="210" y="42" width="48" height="40" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
    <text x="234" y="68" fill="#3A3530" font-weight="bold">2</text>
    <text x="234" y="94" font-size="9" fill="#5A5752">1</text>
    <rect x="266" y="42" width="48" height="40" rx="5" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="290" y="68" fill="#5A5752">3</text>
    <text x="290" y="94" font-size="9" fill="#9A9792">2</text>
    <rect x="322" y="42" width="48" height="40" rx="5" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="346" y="68" fill="#5A5752">4</text>
    <text x="346" y="94" font-size="9" fill="#9A9792">3</text>
    <rect x="378" y="42" width="48" height="40" rx="5" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="402" y="68" fill="#5A5752">5</text>
    <text x="402" y="94" font-size="9" fill="#9A9792">4</text>
    <rect x="434" y="42" width="48" height="40" rx="5" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="458" y="68" fill="#5A5752">6</text>
    <text x="458" y="94" font-size="9" fill="#9A9792">5</text>
    <rect x="490" y="42" width="48" height="40" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
    <text x="514" y="68" fill="#3A3530" font-weight="bold">7</text>
    <text x="514" y="94" font-size="9" fill="#5A5752">6</text>
  </g>
  <polygon points="234,104 228,114 240,114" fill="#8B8680"/>
  <text x="234" y="128" text-anchor="middle" font-size="11" fill="#5A5752" font-weight="bold">left</text>
  <polygon points="514,104 508,114 520,114" fill="#8B8680"/>
  <text x="514" y="128" text-anchor="middle" font-size="11" fill="#5A5752" font-weight="bold">right</text>
  <path d="M178,40 Q178,30 206,30 Q234,30 234,40" fill="none" stroke="#B8B5B0" stroke-width="1.2" stroke-dasharray="4,2"/>
  <polygon points="232,38 234,44 236,38" fill="#B8B5B0"/>
  <text x="206" y="26" text-anchor="middle" font-size="9" fill="#9A9792">move →</text>
  <g font-size="12">
    <text x="120" y="156" fill="#7A7772">Step 1:</text>
    <text x="178" y="156" fill="#5A5752">left=0, right=6 → 1 + 7 = 8 &lt; 9 → move left</text>
    <text x="120" y="180" fill="#7A7772">Step 2:</text>
    <text x="178" y="180" fill="#3A3530" font-weight="bold">left=1, right=6 → 2 + 7 = 9 = target ✓</text>
  </g>
</svg>
</div>

```cpp
bool twoSumSorted(const vector<int>& a, int target){
    int l = 0, r = (int)a.size() - 1;
    while (l < r){
        long long sum = (long long)a[l] + a[r];
        if (sum == target) return true;
        if (sum < target) ++l; else --r;
    }
    return false;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 15 | 3Sum | [Link](https://leetcode.com/problems/3sum/) | - |
| 11 | Container With Most Water | [Link](https://leetcode.com/problems/container-with-most-water/) | - |
| 125 | Valid Palindrome | [Link](https://leetcode.com/problems/valid-palindrome/) | - |
| 1768 | Merge Strings Alternately | [Link](https://leetcode.com/problems/merge-strings-alternately/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/27/easy-1768-merge-strings-alternately/) |

## Binary Search on Answer (monotonic predicate)

**When to use:** "minimize the maximum", "feasibility check", "minimum speed/capacity", or when the answer has a monotonic property (if x works, then x+1 also works).

```cpp
long long binsearch(long long lo, long long hi){ // [lo, hi]
    auto good = [&](long long x){ /* check feasibility */ return true; };
    while (lo < hi){
        long long mid = (lo + hi) >> 1;
        if (good(mid)) hi = mid; else lo = mid + 1;
    }
    return lo;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 33 | Search in Rotated Sorted Array | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/23/medium-33-search-in-rotated-sorted-array/) |
| 34 | Find First and Last Position of Element in Sorted Array | [Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | - |
| 162 | Find Peak Element | [Link](https://leetcode.com/problems/find-peak-element/) | - |
| 875 | Koko Eating Bananas | [Link](https://leetcode.com/problems/koko-eating-bananas/) | - |
| 1870 | Minimum Speed to Arrive on Time | [Link](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/30/medium-1870-minimum-speed-to-arrive-on-time/) |

## Prefix Sum / Difference Array

**When to use:** "range sum query", "subarray sum equals k", "number of subarrays with sum", or when you need O(1) range queries after O(n) preprocessing.

```cpp
vector<int> prefix(const vector<int>& a){
    vector<int> ps(a.size()+1);
    for (int i = 0; i < (int)a.size(); ++i) ps[i+1] = ps[i] + a[i];
    return ps;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 303 | Range Sum Query - Immutable | [Link](https://leetcode.com/problems/range-sum-query-immutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/01/easy-303-range-sum-query-immutable/) |
| 523 | Continuous Subarray Sum | [Link](https://leetcode.com/problems/continuous-subarray-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/04/medium-523-continuous-subarray-sum/) |
| 560 | Subarray Sum Equals K | [Link](https://leetcode.com/problems/subarray-sum-equals-k/) | - |
| 238 | Product of Array Except Self | [Link](https://leetcode.com/problems/product-of-array-except-self/) | - |
| 525 | Contiguous Array | [Link](https://leetcode.com/problems/contiguous-array/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-medium-525-contiguous-array/) |
| 1177 | Can Make Palindrome from Substring | [Link](https://leetcode.com/problems/can-make-palindrome-from-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/01/medium-1177-can-make-palindrome-from-substring/) |
| 370 | Range Addition | [Link](https://leetcode.com/problems/range-addition/) | - |
| 134 | Gas Station | [Link](https://leetcode.com/problems/gas-station/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/22/medium-134-gas-station/) |
| 2270 | Number of Ways to Split Array | [Link](https://leetcode.com/problems/number-of-ways-to-split-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/06/medium-2270-number-of-ways-to-split-array/) |

## Hash Map Frequencies

**When to use:** "two sum", "group anagrams", "frequency count", "contains duplicate", or any problem where you need O(1) lookups by value.

```cpp
unordered_map<int,int> freq;
for (int x: nums) ++freq[x];
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1 | Two Sum | [Link](https://leetcode.com/problems/two-sum/) | - |
| 49 | Group Anagrams | [Link](https://leetcode.com/problems/group-anagrams/) | - |
| 242 | Valid Anagram | [Link](https://leetcode.com/problems/valid-anagram/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/07/easy-242-valid-anagram/) |
| 217 | Contains Duplicate | [Link](https://leetcode.com/problems/contains-duplicate/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/07/easy-217-contains-duplicate/) |
| 219 | Contains Duplicate II | [Link](https://leetcode.com/problems/contains-duplicate-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/07/easy-219-contains-duplicate-ii/) |
| 383 | Ransom Note | [Link](https://leetcode.com/problems/ransom-note/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/07/easy-383-ransom-note/) |
| 981 | Time Based Key-Value Store | [Link](https://leetcode.com/problems/time-based-key-value-store/) | - |
| 359 | Logger Rate Limiter | [Link](https://leetcode.com/problems/logger-rate-limiter/) | - |
| 2365 | Task Scheduler II | [Link](https://leetcode.com/problems/task-scheduler-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/10/medium-2365-task-scheduler-ii/) |
| 2342 | Max Sum of a Pair With Equal Sum of Digits | [Link](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/11/medium-2342-max-sum-of-a-pair-with-equal-sum-of-digits/) |

## KMP (Substring Search)

**When to use:** "find pattern in string", "shortest palindrome by prepending", "repeated string match", or when you need O(n + m) exact pattern matching.

KMP is a pattern matching algorithm that finds occurrences of a pattern string P within a text string T efficiently — without re-checking characters that are already known to match.

While a naive substring search checks character-by-character and backtracks when a mismatch occurs (worst case O(n * m)),
KMP preprocesses the pattern to know how far it can safely skip ahead when mismatches happen.

It does this using a “prefix function” (also called LPS — longest prefix which is also suffix).

### Steps

Preprocess the pattern to build the lps[] array.

* lps[i] = the length of the longest proper prefix of the substring P[0..i] which is also a suffix of this substring.

* Proper prefix = prefix ≠ the string itself.

Use the LPS array during the search

* When mismatch occurs, instead of resetting j = 0, we move j back to lps[j-1].

```cpp
vector<int> kmpPi(const string& s) {
    int n = s.size();
    vector<int> pi(n);
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    return pi;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | [Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | - |
| 214 | Shortest Palindrome | [Link](https://leetcode.com/problems/shortest-palindrome/) | - |
| 686 | Repeated String Match | [Link](https://leetcode.com/problems/repeated-string-match/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/medium-686-repeated-string-match/) |

## Manacher (Longest Palindromic Substring, O(n))

**When to use:** "longest palindromic substring" when O(n) time is required, or counting all palindromic substrings efficiently.

```cpp
string manacher(const string& s) {
    string t = "|";
    for (char c : s) { t.push_back(c); t.push_back('|'); }
    int n = t.size();
    vector<int> p(n);
    int c = 0, r = 0, best = 0, center = 0;
    for (int i = 0; i < n; i++) {
        int mir = 2 * c - i;
        if (i < r) p[i] = min(r - i, p[mir]);
        while (i - 1 - p[i] >= 0 && i + 1 + p[i] < n && t[i - 1 - p[i]] == t[i + 1 + p[i]]) p[i]++;
        if (i + p[i] > r) { c = i; r = i + p[i]; }
        if (p[i] > best) { best = p[i]; center = i; }
    }
    int start = (center - best) / 2;
    return s.substr(start, best);
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 5 | Longest Palindromic Substring | [Link](https://leetcode.com/problems/longest-palindromic-substring/) | - |

## Z-Algorithm (Pattern occurrences)

**When to use:** "find all pattern occurrences", "longest happy prefix", or as an alternative to KMP for pattern matching.

```cpp
vector<int> zfunc(const string& s) {
    int n = s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i <= r) z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) { l = i; r = i + z[i] - 1; }
    }
    return z;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1392 | Longest Happy Prefix | [Link](https://leetcode.com/problems/longest-happy-prefix/) | - |

## String Rolling Hash (Rabin–Karp)

**When to use:** "repeated DNA sequences", "longest duplicate substring", or when you need to compare many substrings in O(1) each after O(n) preprocessing.

```cpp
struct RH {
    static const long long B = 911382323, M = 972663749;
    vector<long long> p, h;
    RH(const string& s) {
        int n = s.size();
        p.assign(n + 1, 1);
        h.assign(n + 1, 0);
        for (int i = 0; i < n; i++) {
            p[i + 1] = p[i] * B % M;
            h[i + 1] = (h[i] * B + s[i]) % M;
        }
    }
    long long get(int l, int r) {  // [l, r)
        return (h[r] - h[l] * p[r - l] % M + M) % M;
    }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 187 | Repeated DNA Sequences | [Link](https://leetcode.com/problems/repeated-dna-sequences/) | - |
| 686 | Repeated String Match | [Link](https://leetcode.com/problems/repeated-string-match/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/medium-686-repeated-string-match/) |
| 1044 | Longest Duplicate Substring | [Link](https://leetcode.com/problems/longest-duplicate-substring/) | - |

## Summary

| Pattern | Signal Phrases | Time |
|---|---|---|
| Sliding Window | "substring", "subarray", "at most k" | O(n) |
| Two Pointers | "sorted", "pair", "container" | O(n) |
| Binary Search on Answer | "minimize max", "feasibility" | O(n log range) |
| Prefix Sum | "range sum", "subarray sum" | O(n) build, O(1) query |
| Hash Map | "frequency", "group", "two sum" | O(n) |
| KMP | "pattern in string" | O(n + m) |

## More templates

- **Data structures (prefix sum, monotonic stack):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
