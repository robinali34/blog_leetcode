---
layout: post
title: "LeetCode Templates: Data Structures"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates data-structures
permalink: /posts/2025-10-29-leetcode-templates-data-structures/
tags: [leetcode, templates, data-structures]
---

## Contents

- [Monotonic Stack](#monotonic-stack-next-greater--histogram)
- [Monotonic Queue](#monotonic-queue-sliding-window-extrema)
- [Heap / K-way Merge](#heap--k-way-merge)
- [Union-Find (DSU)](#union-find-disjoint-set-union)
- [Trie (Prefix Tree)](#trie-prefix-tree)
- [Segment Tree](#segment-tree-range-query--point-update)
- [Fenwick Tree](#fenwick-tree-binary-indexed-tree)

## Monotonic Stack (next greater / histogram)

```cpp
vector<int> nextGreater(vector<int>& a){
    int n = a.size(); vector<int> ans(n, -1); vector<int> st;
    for (int i = 0; i < 2*n; ++i){
        int idx = i % n;
        while (!st.empty() && a[st.back()] < a[idx]){
            ans[st.back()] = a[idx]; st.pop_back();
        }
        if (i < n) st.push_back(idx);
    }
    return ans;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 739 | Daily Temperatures | [Link](https://leetcode.com/problems/daily-temperatures/) | - |
| 84 | Largest Rectangle in Histogram | [Link](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/hard-84-largest-rectangle-in-histogram/) |
| 496 | Next Greater Element I | [Link](https://leetcode.com/problems/next-greater-element-i/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/easy-496-next-greater-element-i/) |
| 503 | Next Greater Element II | [Link](https://leetcode.com/problems/next-greater-element-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-503-next-greater-element-ii/) |

## Monotonic Queue (sliding window extrema)

```cpp
vector<int> maxWindow(const vector<int>& a, int k){
    deque<int> dq; vector<int> out;
    for (int i=0;i<(int)a.size();++i){
        while(!dq.empty() && a[dq.back()]<=a[i]) dq.pop_back();
        dq.push_back(i);
        if (dq.front() <= i-k) dq.pop_front();
        if (i>=k-1) out.push_back(a[dq.front()]);
    }
    return out;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 1438 | Longest Continuous Subarray With Absolute Diff <= Limit | [Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | - |

## Heap / K-way Merge

```cpp
vector<int> mergeK(vector<vector<int>>& lists){
    using T = tuple<int,int,int>; // val, list idx, pos
    priority_queue<T, vector<T>, greater<T>> pq;
    for (int i=0;i<(int)lists.size();++i) if (!lists[i].empty()) pq.emplace(lists[i][0], i, 0);
    vector<int> out;
    while(!pq.empty()){
        auto [v,i,j]=pq.top(); pq.pop(); out.push_back(v);
        if (j+1 < (int)lists[i].size()) pq.emplace(lists[i][j+1], i, j+1);
    }
    return out;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | - |
| 295 | Find Median from Data Stream | [Link](https://leetcode.com/problems/find-median-from-data-stream/) | - |

## Union-Find (Disjoint Set Union)

```cpp
struct DSU{
    vector<int> p, r; DSU(int n): p(n), r(n,0){ iota(p.begin(), p.end(), 0);} 
    int find(int x){ return p[x]==x?x:p[x]=find(p[x]); }
    bool unite(int a,int b){ a=find(a); b=find(b); if(a==b) return false; if(r[a]<r[b]) swap(a,b); p[b]=a; if(r[a]==r[b]) ++r[a]; return true; }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 684 | Redundant Connection | [Link](https://leetcode.com/problems/redundant-connection/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/29/medium-684-redundant-connection/) |
| 721 | Accounts Merge | [Link](https://leetcode.com/problems/accounts-merge/) | - |
| 1319 | Number of Operations to Make Network Connected | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | - |

## Trie (Prefix Tree)

```cpp
struct Trie{
    struct Node{ int nxt[26]; bool end; Node(){ memset(nxt,-1,sizeof nxt); end=false; } };
    vector<Node> t{1};
    void insert(const string& s){ int u=0; for(char c:s){ int i=c-'a'; if(t[u].nxt[i]==-1){ t[u].nxt[i]=t.size(); t.emplace_back(); } u=t[u].nxt[i]; } t[u].end=true; }
    bool search(const string& s){ int u=0; for(char c:s){ int i=c-'a'; if((u=t[u].nxt[i])==-1) return false; } return t[u].end; }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 208 | Implement Trie | [Link](https://leetcode.com/problems/implement-trie-prefix-tree/) | - |
| 211 | Add and Search Word | [Link](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | - |
| 212 | Word Search II | [Link](https://leetcode.com/problems/word-search-ii/) | - |

## Segment Tree (range query / point update)

```cpp
struct Seg{ int n; vector<long long> st; Seg(int n):n(n),st(4*n,0){}
    void upd(int p,long long v,int i,int l,int r){ if(l==r){ st[i]=v; return; }
        int m=(l+r)/2; if(p<=m) upd(p,v,2*i,l,m); else upd(p,v,2*i+1,m+1,r);
        st[i]=st[2*i]+st[2*i+1]; }
    long long qry(int ql,int qr,int i,int l,int r){ if(qr<l||r<ql) return 0; if(ql<=l&&r<=qr) return st[i];
        int m=(l+r)/2; return qry(ql,qr,2*i,l,m)+qry(ql,qr,2*i+1,m+1,r); }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 307 | Range Sum Query – Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | - |
| 732 | My Calendar III | [Link](https://leetcode.com/problems/my-calendar-iii/) | - |

## Fenwick Tree (Binary Indexed Tree)

```cpp
struct BIT{ int n; vector<long long> f; BIT(int n):n(n),f(n+1,0){}
    void add(int i,long long v){ for(; i<=n; i+=i&-i) f[i]+=v; }
    long long sum(int i){ long long s=0; for(; i>0; i-=i&-i) s+=f[i]; return s; }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | - |
| 307 | Range Sum Query – Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | - |
| 308 | Range Sum Query 2D - Mutable | [Link](https://leetcode.com/problems/range-sum-query-2d-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/hard-308-range-sum-query-2d-mutable/) |
| 715 | Range Module | [Link](https://leetcode.com/problems/range-module/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/hard-715-range-module/) |
