---
layout: post
title: "LeetCode Templates: Arrays & Strings"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates arrays strings
permalink: /posts/2025-10-29-leetcode-templates-arrays-strings/
tags: [leetcode, templates, arrays, strings]
---

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

| ID | Title | Link |
|---|---|---|
| 3 | Longest Substring Without Repeating Characters | https://leetcode.com/problems/longest-substring-without-repeating-characters/ |
| 76 | Minimum Window Substring | https://leetcode.com/problems/minimum-window-substring/ |
| 424 | Longest Repeating Character Replacement | https://leetcode.com/problems/longest-repeating-character-replacement/ |

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

| ID | Title | Link |
|---|---|---|
| 15 | 3Sum | https://leetcode.com/problems/3sum/ |
| 11 | Container With Most Water | https://leetcode.com/problems/container-with-most-water/ |
| 125 | Valid Palindrome | https://leetcode.com/problems/valid-palindrome/ |

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

| ID | Title | Link |
|---|---|---|
| 33 | Search in Rotated Sorted Array | https://leetcode.com/problems/search-in-rotated-sorted-array/ |
| 34 | Find First and Last Position of Element in Sorted Array | https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ |
| 162 | Find Peak Element | https://leetcode.com/problems/find-peak-element/ |
| 875 | Koko Eating Bananas | https://leetcode.com/problems/koko-eating-bananas/ |

## Prefix Sum / Difference Array

```cpp
vector<int> prefix(const vector<int>& a){
    vector<int> ps(a.size()+1);
    for (int i = 0; i < (int)a.size(); ++i) ps[i+1] = ps[i] + a[i];
    return ps;
}
```

| ID | Title | Link |
|---|---|---|
| 560 | Subarray Sum Equals K | https://leetcode.com/problems/subarray-sum-equals-k/ |
| 238 | Product of Array Except Self | https://leetcode.com/problems/product-of-array-except-self/ |
| 525 | Contiguous Array | https://leetcode.com/problems/contiguous-array/ |
| 370 | Range Addition | https://leetcode.com/problems/range-addition/ |

## Hash Map Frequencies

```cpp
unordered_map<int,int> freq;
for (int x: nums) ++freq[x];
```

| ID | Title | Link |
|---|---|---|
| 1 | Two Sum | https://leetcode.com/problems/two-sum/ |
| 49 | Group Anagrams | https://leetcode.com/problems/group-anagrams/ |
| 981 | Time Based Key-Value Store | https://leetcode.com/problems/time-based-key-value-store/ |
| 359 | Logger Rate Limiter | https://leetcode.com/problems/logger-rate-limiter/ |

## KMP (Substring Search)

```cpp
vector<int> kmpPi(const string& s){
    int n=s.size(); vector<int> pi(n);
    for(int i=1;i<n;++i){ int j=pi[i-1];
        while(j>0 && s[i]!=s[j]) j=pi[j-1];
        if(s[i]==s[j]) ++j; pi[i]=j;
    }
    return pi;
}
```

| ID | Title | Link |
|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ |
| 214 | Shortest Palindrome | https://leetcode.com/problems/shortest-palindrome/ |

## Manacher (Longest Palindromic Substring, O(n))

```cpp
string manacher(const string& s){ string t="|"; for(char c:s){ t.push_back(c); t.push_back('|'); }
    int n=t.size(); vector<int> p(n); int c=0,r=0, best=0, center=0;
    for(int i=0;i<n;++i){ int mir=2*c-i; if(i<r) p[i]=min(r-i,p[mir]); while(i-1-p[i]>=0 && i+1+p[i]<n && t[i-1-p[i]]==t[i+1+p[i]]) ++p[i]; if(i+p[i]>r){ c=i; r=i+p[i]; } if(p[i]>best){ best=p[i]; center=i; } }
    int start=(center-best)/2; return s.substr(start, best);
}
```

| ID | Title | Link |
|---|---|---|
| 5 | Longest Palindromic Substring | https://leetcode.com/problems/longest-palindromic-substring/ |

## Z-Algorithm (Pattern occurrences)

```cpp
vector<int> zfunc(const string& s){ int n=s.size(); vector<int> z(n); int l=0,r=0; for(int i=1;i<n;++i){ if(i<=r) z[i]=min(r-i+1, z[i-l]); while(i+z[i]<n && s[z[i]]==s[i+z[i]]) ++z[i]; if(i+z[i]-1>r){ l=i; r=i+z[i]-1; } } return z; }
```

| ID | Title | Link |
|---|---|---|
| 1392 | Longest Happy Prefix | https://leetcode.com/problems/longest-happy-prefix/ |

## String Rolling Hash (Rabin–Karp)

```cpp
struct RH{
    static const long long B=911382323, M=972663749; // example
    vector<long long> p,h; RH(const string& s){ int n=s.size(); p.assign(n+1,1); h.assign(n+1,0);
        for(int i=0;i<n;++i){ p[i+1]=p[i]*B%M; h[i+1]=(h[i]*B + s[i])%M; } }
    long long get(int l,int r){ // [l,r)
        return (h[r] - h[l]*p[r-l])%M;
    }
};
```

| ID | Title | Link |
|---|---|---|
| 187 | Repeated DNA Sequences | https://leetcode.com/problems/repeated-dna-sequences/ |
| 1044 | Longest Duplicate Substring | https://leetcode.com/problems/longest-duplicate-substring/ |
