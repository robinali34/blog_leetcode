---
layout: post
title: "Algorithm Templates: Advanced Techniques"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates advanced
permalink: /posts/2025-10-29-leetcode-templates-advanced/
tags: [leetcode, templates, advanced]
---

This page covers specialized algorithmic techniques that appear in Hard-level LeetCode problems and competitive programming. These are not everyday patterns — most interviews won't require them — but when a problem does call for one of these techniques, knowing the template can turn an impossible problem into a straightforward implementation.

> **These are specialized techniques for hard problems.** You won't need them for most interviews, but they appear in competitive programming and occasional Hard-level LeetCode problems.

<svg viewBox="0 0 700 180" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="350" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Meet-in-the-Middle — split n=40 into two halves of 20</text>
  <rect x="40" y="35" width="280" height="70" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="170" y="55" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Left half (20 elements)</text>
  <text x="170" y="75" font-size="10" fill="#7A7772" text-anchor="middle">Generate all 2^20 subset sums</text>
  <text x="170" y="90" font-size="10" fill="#7A7772" text-anchor="middle">Store in array L</text>
  <rect x="380" y="35" width="280" height="70" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="530" y="55" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Right half (20 elements)</text>
  <text x="530" y="75" font-size="10" fill="#7A7772" text-anchor="middle">Generate all 2^20 subset sums</text>
  <text x="530" y="90" font-size="10" fill="#7A7772" text-anchor="middle">Store in array R (sorted)</text>
  <text x="350" y="120" font-size="11" fill="#5A5752" text-anchor="middle">For each sum x in L: find T-x in R using binary search</text>
  <text x="350" y="145" font-size="10" fill="#3A6B3A" font-weight="600" text-anchor="middle">2^40 brute force → 2^20 + 2^20 log(2^20) ≈ 2^21 — tractable!</text>
  <text x="350" y="168" font-size="10" fill="#9A9792" text-anchor="middle">Use when n ≤ 40 and brute force 2^n is too slow</text>
</svg>

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)

## Contents

- [Coordinate Compression](#coordinate-compression)
- [Meet-in-the-Middle (subset sums)](#meet-in-the-middle-subset-sums)
- [Manacher (LPS O(n))](#manacher-longest-palindromic-substring-on)
- [Z-Algorithm](#z-algorithm-pattern-occurrences)
- [Bitwise Trie (Max XOR Pair)](#bitwise-trie-max-xor-pair)

## Coordinate Compression

**When to use:** values are too large for direct array indexing (e.g., values up to 10^9 but only n ≤ 10^5 distinct values), or you need to map sparse values into a dense range.

```cpp
template<class T>
struct Compressor{
    vector<T> vals; template<class It> void add(It b, It e){ vals.insert(vals.end(), b, e); }
    void build(){ sort(vals.begin(), vals.end()); vals.erase(unique(vals.begin(), vals.end()), vals.end()); }
    int get(const T& x) const { return int(lower_bound(vals.begin(), vals.end(), x)-vals.begin()); }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | - |
| 327 | Count of Range Sum | [Link](https://leetcode.com/problems/count-of-range-sum/) | - |

## Meet-in-the-Middle (subset sums)

**When to use:** "subset sum" with n ≤ 40 (too large for 2^n but feasible as 2^(n/2)), or when brute-force is exponential but splitting the input in half makes it tractable.

```cpp
long long countSubsets(vector<int>& a, long long T){
    int n=a.size(), m=n/2; vector<long long> L,R; L.reserve(1<<m); R.reserve(1<<(n-m));
    auto go=[&](int l,int r, vector<long long>& out){ int k=r-l; for(int mask=0; mask<(1<<k); ++mask){ long long s=0; for(int i=0;i<k;++i) if(mask>>i & 1) s+=a[l+i]; out.push_back(s); } };
    go(0,m,L); go(m,n,R); sort(R.begin(), R.end()); long long ans=0; for(long long x: L){ auto pr=equal_range(R.begin(), R.end(), T-x); ans += pr.second - pr.first; } return ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1755 | Closest Subsequence Sum | [Link](https://leetcode.com/problems/closest-subsequence-sum/) | - |
| 805 | Split Array With Same Average | [Link](https://leetcode.com/problems/split-array-with-same-average/) | - |

## Manacher (Longest Palindromic Substring, O(n))

**When to use:** "longest palindromic substring" when O(n) is required, or when you need all palindrome radii in linear time.

```cpp
string manacher(const string& s){ string t="|"; for(char c:s){ t.push_back(c); t.push_back('|'); }
    int n=t.size(); vector<int> p(n); int c=0,r=0, best=0, center=0;
    for(int i=0;i<n;++i){ int mir=2*c-i; if(i<r) p[i]=min(r-i,p[mir]); while(i-1-p[i]>=0 && i+1+p[i]<n && t[i-1-p[i]]==t[i+1+p[i]]) ++p[i]; if(i+p[i]>r){ c=i; r=i+p[i]; } if(p[i]>best){ best=p[i]; center=i; } }
    int start=(center-best)/2; return s.substr(start, best);
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 5 | Longest Palindromic Substring | [Link](https://leetcode.com/problems/longest-palindromic-substring/) | - |

## Z-Algorithm (Pattern occurrences)

**When to use:** "find all occurrences of pattern in string", or when you need the longest prefix match at each position (alternative to KMP).

```cpp
vector<int> zfunc(const string& s){ int n=s.size(); vector<int> z(n); int l=0,r=0; for(int i=1;i<n;++i){ if(i<=r) z[i]=min(r-i+1, z[i-l]); while(i+z[i]<n && s[z[i]]==s[i+z[i]]) ++z[i]; if(i+z[i]-1>r){ l=i; r=i+z[i]-1; } } return z; }
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1392 | Longest Happy Prefix | [Link](https://leetcode.com/problems/longest-happy-prefix/) | - |

## Bitwise Trie (Max XOR Pair)

**When to use:** "maximum XOR of two numbers", or when you need to greedily pick bits to maximize/minimize a bitwise operation.

```cpp
struct BitTrie{ struct Node{int ch[2]; Node(){ch[0]=ch[1]=-1;}}; vector<Node> t{Node()};
    void insert(int x){ int u=0; for(int b=31;b>=0;--b){ int bit=(x>>b)&1; if(t[u].ch[bit]==-1){ t[u].ch[bit]=t.size(); t.push_back(Node()); } u=t[u].ch[bit]; } }
    int maxXor(int x){ int u=0, ans=0; for(int b=31;b>=0;--b){ int bit=(x>>b)&1, want=bit^1; if(t[u].ch[want]!=-1){ ans |= 1<<b; u=t[u].ch[want]; } else u=t[u].ch[bit]; } return ans; }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 421 | Maximum XOR of Two Numbers in an Array | [Link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | - |

## Summary

| Technique | When to Use | Time |
|---|---|---|
| Coordinate Compression | Values too large for array indexing | O(n log n) |
| Meet-in-the-Middle | Subset sum with n ≤ 40 | O(2^(n/2)) |
| Manacher | Longest palindromic substring in O(n) | O(n) |
| Z-Algorithm | Pattern matching | O(n + m) |
| Bitwise Trie | Maximum XOR pair | O(n × 32) |

## More templates

- **Arrays & Strings (Manacher, Z, rolling hash):** [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/)
- **Data structures (Trie):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Search (divide and conquer):** [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
