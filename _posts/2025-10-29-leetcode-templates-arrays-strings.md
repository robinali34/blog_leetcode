---
layout: post
title: "Algorithm Templates: Arrays & Strings"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates arrays strings
permalink: /posts/2025-10-29-leetcode-templates-arrays-strings/
tags: [leetcode, templates, arrays, strings]
---

{% raw %}
Minimal, copy-paste C++ for sliding window, two pointers, prefix sum, KMP, Manacher, and rolling hash.

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

## Two Pointers (sorted arrays/strings)

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

## Binary Search on Answer (monotonic predicate)

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

## Prefix Sum / Difference Array

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
| 560 | Subarray Sum Equals K | [Link](https://leetcode.com/problems/subarray-sum-equals-k/) | - |
| 238 | Product of Array Except Self | [Link](https://leetcode.com/problems/product-of-array-except-self/) | - |
| 525 | Contiguous Array | [Link](https://leetcode.com/problems/contiguous-array/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-medium-525-contiguous-array/) |
| 1177 | Can Make Palindrome from Substring | [Link](https://leetcode.com/problems/can-make-palindrome-from-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/01/medium-1177-can-make-palindrome-from-substring/) |
| 370 | Range Addition | [Link](https://leetcode.com/problems/range-addition/) | - |

## Hash Map Frequencies

```cpp
unordered_map<int,int> freq;
for (int x: nums) ++freq[x];
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1 | Two Sum | [Link](https://leetcode.com/problems/two-sum/) | - |
| 49 | Group Anagrams | [Link](https://leetcode.com/problems/group-anagrams/) | - |
| 981 | Time Based Key-Value Store | [Link](https://leetcode.com/problems/time-based-key-value-store/) | - |
| 359 | Logger Rate Limiter | [Link](https://leetcode.com/problems/logger-rate-limiter/) | - |

## KMP (Substring Search)
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

## More templates

- **Data structures (prefix sum, monotonic stack):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
