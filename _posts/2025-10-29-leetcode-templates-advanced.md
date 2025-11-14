---
layout: post
title: "LeetCode Templates: Advanced Techniques"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates advanced
permalink: /posts/2025-10-29-leetcode-templates-advanced/
tags: [leetcode, templates, advanced]
---

## Contents

- [Coordinate Compression](#coordinate-compression)
- [Meet-in-the-Middle (subset sums)](#meet-in-the-middle-subset-sums)
- [Manacher (LPS O(n))](#manacher-longest-palindromic-substring-on)
- [Z-Algorithm](#z-algorithm-pattern-occurrences)
- [Bitwise Trie (Max XOR Pair)](#bitwise-trie-max-xor-pair)

## Coordinate Compression

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

```cpp
vector<int> zfunc(const string& s){ int n=s.size(); vector<int> z(n); int l=0,r=0; for(int i=1;i<n;++i){ if(i<=r) z[i]=min(r-i+1, z[i-l]); while(i+z[i]<n && s[z[i]]==s[i+z[i]]) ++z[i]; if(i+z[i]-1>r){ l=i; r=i+z[i]-1; } } return z; }
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1392 | Longest Happy Prefix | [Link](https://leetcode.com/problems/longest-happy-prefix/) | - |

## Bitwise Trie (Max XOR Pair)

```cpp
struct BitTrie{ struct Node{int ch[2]; Node(){ch[0]=ch[1]=-1;}}; vector<Node> t{Node()};
    void insert(int x){ int u=0; for(int b=31;b>=0;--b){ int bit=(x>>b)&1; if(t[u].ch[bit]==-1){ t[u].ch[bit]=t.size(); t.push_back(Node()); } u=t[u].ch[bit]; } }
    int maxXor(int x){ int u=0, ans=0; for(int b=31;b>=0;--b){ int bit=(x>>b)&1, want=bit^1; if(t[u].ch[want]!=-1){ ans |= 1<<b; u=t[u].ch[want]; } else u=t[u].ch[bit]; } return ans; }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 421 | Maximum XOR of Two Numbers in an Array | [Link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | - |
