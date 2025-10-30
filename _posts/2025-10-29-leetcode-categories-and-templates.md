---
layout: post
title: "LeetCode Categories and Solution Templates"
date: 2025-10-29 00:00:00 -0700
categories: leetcode algorithm problem-solving templates
permalink: /posts/2025-10-29-leetcode-categories-and-templates/
tags: [leetcode, templates, patterns, dp, graph, sliding-window, two-pointers, binary-search]
---

{% raw %}
# LeetCode Categories and Solution Templates

A quick reference to the most common LeetCode categories and battle‑tested C++ templates to speed up implementation.

> This guide is now split into category posts:
> - Arrays & Strings: [/posts/2025-10-29-leetcode-templates-arrays-strings/](/posts/2025-10-29-leetcode-templates-arrays-strings/)
> - Data Structures: [/posts/2025-10-29-leetcode-templates-data-structures/](/posts/2025-10-29-leetcode-templates-data-structures/)
> - Graph: [/posts/2025-10-29-leetcode-templates-graph/](/posts/2025-10-29-leetcode-templates-graph/)
> - Trees: [/posts/2025-10-29-leetcode-templates-trees/](/posts/2025-10-29-leetcode-templates-trees/)
> - Dynamic Programming: [/posts/2025-10-29-leetcode-templates-dp/](/posts/2025-10-29-leetcode-templates-dp/)
> - Math & Geometry: [/posts/2025-10-29-leetcode-templates-math-geometry/](/posts/2025-10-29-leetcode-templates-math-geometry/)
> - Advanced Techniques: [/posts/2025-10-29-leetcode-templates-advanced/](/posts/2025-10-29-leetcode-templates-advanced/)

## Contents

- [Arrays & Strings](#arrays--strings) – core array/string patterns
  - [Sliding Window](#sliding-window-fixedvariable) – subarray/substring constraints
  - [Two Pointers](#two-pointers-sorted-arraysstrings) – ends converge/partition/merge
  - [Binary Search on Answer](#binary-search-on-answer-monotonic-predicate) – monotonic feasibility
  - [Prefix Sum / Difference](#prefix-sum--difference-array) – range totals and updates
  - [Hash Map Frequencies](#hash-map-frequencies) – counting/indexing by value
- [Data Structures](#data-structures) – reusable structures for queries
  - [Monotonic Stack](#monotonic-stack-next-greater--histogram) – next greater/histogram
  - [Monotonic Queue](#monotonic-queue-sliding-window-max) – sliding window extrema
  - [Heap / K-way Merge](#heap--k-way-merge) – merging streams/medians
  - [Union-Find](#union-find-disjoint-set-union) – connectivity/components
  - [Trie](#trie-prefix-tree) – prefix lookup
  - [Segment Tree](#segment-tree-range-querypoint-update) – range queries/point updates
  - [Fenwick Tree](#fenwick-tree-binary-indexed-tree) – prefix sums/inversions
- [Graph](#graph) – traversal and shortest paths
  - [BFS / Shortest Path](#bfs--shortest-path-unweighted) – unweighted shortest paths
  - [Multi-source BFS](#multi-source-bfs-gridsgraphs) – simultaneous wavefronts
  - [BFS on Bitmask State](#bfs-on-bitmask-state-eg-visit-all-keys) – state-space BFS
  - [Topological Sort](#topological-sort-kahn--dfs) – DAG ordering/cycle detect
  - [Dijkstra](#dijkstra-shortest-path-with-weights--0) – nonnegative weights
  - [0-1 BFS](#0-1-bfs-edge-weights-0-or-1) – 0/1 weighted graphs
  - [Tarjan SCC](#tarjan-scc-strongly-connected-components) – strongly connected comps
  - [Bridges & Articulation](#bridges-and-articulation-points-tarjan) – critical edges/nodes
- [Trees](#trees) – hierarchical structures
  - [Traversals](#tree-traversals-iterative) – inorder/level-order
  - [LCA](#lca-binary-lifting) – ancestor queries
  - [HLD](#heavy-light-decomposition-hld-skeleton) – path queries
- [Dynamic Programming](#dynamic-programming) – optimal substructure
  - [1D DP](#1d-dp-knapsacklinear) – knapsack/linear transitions
  - [2D DP](#2d-dp-gridpath) – grid paths/obstacles
  - [Digit DP](#digit-dp-count-numbers-with-property) – per-digit states
  - [Bitmask DP](#bitmask-dp-tsp--subsets) – subsets/TSP
- [Math & Geometry](#math--geometry) – combinatorics and 2D ops
  - [Combinatorics](#math--combinatorics-nck-mod-p) – nCk, factorials, mod math
  - [Geometry Primitives](#geometry-primitives-2d) – cross/segments/areas
- [Advanced Techniques](#advanced-techniques) – specialized patterns
  - [Coordinate Compression](#coordinate-compression) – map values to ranks
  - [Meet-in-the-Middle](#meet-in-the-middle-subset-sums) – split/merge subsets
  - [Manacher](#manacher-longest-palindromic-substring-on) – palindromes in O(n)
  - [Z-Algorithm](#z-algorithm-pattern-occurrences) – pattern occurrences
  - [Bitwise Trie](#bitwise-trie-max-xor-pair) – max XOR pairs

## Arrays & Strings

## Sliding Window (fixed/variable)

Use for subarray/substring with constraints (distinct count, sum/k, length).

```cpp
// Variable-size window (e.g., longest substring without repeating)
int solve(const string& s){
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

Examples: 3 Longest Substring Without Repeating Characters; 76 Minimum Window Substring; 424 Longest Repeating Character Replacement.

| ID | Title | Link |
|---|---|---|
| 3 | Longest Substring Without Repeating Characters | https://leetcode.com/problems/longest-substring-without-repeating-characters/ |
| 76 | Minimum Window Substring | https://leetcode.com/problems/minimum-window-substring/ |
| 424 | Longest Repeating Character Replacement | https://leetcode.com/problems/longest-repeating-character-replacement/ |

## Two Pointers (sorted arrays/strings)

```cpp
// Classic: two-sum on sorted array, or merging
bool twoSum(const vector<int>& a, int target){
    int l = 0, r = (int)a.size() - 1;
    while (l < r){
        long long sum = (long long)a[l] + a[r];
        if (sum == target) return true;
        if (sum < target) ++l; else --r;
    }
    return false;
}
```

Examples: 15 3Sum; 11 Container With Most Water; 125 Valid Palindrome.

| ID | Title | Link |
|---|---|---|
| 15 | 3Sum | https://leetcode.com/problems/3sum/ |
| 11 | Container With Most Water | https://leetcode.com/problems/container-with-most-water/ |
| 125 | Valid Palindrome | https://leetcode.com/problems/valid-palindrome/ |

## Binary Search on Answer (monotonic predicate)

```cpp
// find minimum x s.t. predicate(x) == true
long long binsearch(long long lo, long long hi){ // [lo, hi]
    auto good = [&](long long x){ /* check feasibility */ return true; };
    while (lo < hi){
        long long mid = (lo + hi) >> 1;
        if (good(mid)) hi = mid; else lo = mid + 1;
    }
    return lo;
}
```

Examples: 33 Search in Rotated Sorted Array; 34 First/Last Position; 162 Find Peak Element; 875 Koko Eating Bananas.

| ID | Title | Link |
|---|---|---|
| 33 | Search in Rotated Sorted Array | https://leetcode.com/problems/search-in-rotated-sorted-array/ |
| 34 | Find First and Last Position of Element in Sorted Array | https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ |
| 162 | Find Peak Element | https://leetcode.com/problems/find-peak-element/ |
| 875 | Koko Eating Bananas | https://leetcode.com/problems/koko-eating-bananas/ |

## Prefix Sum / Difference Array

```cpp
// range sum queries
vector<int> prefix(const vector<int>& a){
    vector<int> ps(a.size()+1);
    for (int i = 0; i < (int)a.size(); ++i) ps[i+1] = ps[i] + a[i];
    return ps;
}
```

Examples: 560 Subarray Sum Equals K; 238 Product of Array Except Self; 525 Contiguous Array; 370 Range Addition.

| ID | Title | Link |
|---|---|---|
| 560 | Subarray Sum Equals K | https://leetcode.com/problems/subarray-sum-equals-k/ |
| 238 | Product of Array Except Self | https://leetcode.com/problems/product-of-array-except-self/ |
| 525 | Contiguous Array | https://leetcode.com/problems/contiguous-array/ |
| 370 | Range Addition | https://leetcode.com/problems/range-addition/ |

## Hash Map Frequencies

```cpp
// count frequencies and check uniqueness, etc.
unordered_map<int,int> freq;
for (int x: nums) ++freq[x];
```

Examples: 1 Two Sum; 49 Group Anagrams; 981 Time Based Key-Value Store; 359 Logger Rate Limiter.

| ID | Title | Link |
|---|---|---|
| 1 | Two Sum | https://leetcode.com/problems/two-sum/ |
| 49 | Group Anagrams | https://leetcode.com/problems/group-anagrams/ |
| 981 | Time Based Key-Value Store | https://leetcode.com/problems/time-based-key-value-store/ |
| 359 | Logger Rate Limiter | https://leetcode.com/problems/logger-rate-limiter/ |

## Monotonic Stack (next greater / histogram)

```cpp
// Next Greater Element (circular if needed)
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

Examples: 739 Daily Temperatures; 84 Largest Rectangle in Histogram; 239 Sliding Window Maximum.

| ID | Title | Link |
|---|---|---|
| 739 | Daily Temperatures | https://leetcode.com/problems/daily-temperatures/ |
| 84 | Largest Rectangle in Histogram | https://leetcode.com/problems/largest-rectangle-in-histogram/ |
| 239 | Sliding Window Maximum | https://leetcode.com/problems/sliding-window-maximum/ |

## Monotonic Queue (Sliding Window Max)

| ID | Title | Link |
|---|---|---|
| 239 | Sliding Window Maximum | https://leetcode.com/problems/sliding-window-maximum/ |
| 1438 | Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit | https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/ |
| 862 | Shortest Subarray with Sum at Least K | https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/ |

## Graph

## BFS / Shortest Path (unweighted)

// Grid BFS template (4-direction)
```cpp
int bfsGrid(vector<string>& g, pair<int,int> s, pair<int,int> t){
    int m=g.size(), n=g[0].size();
    queue<pair<int,int>> q; vector<vector<int>> dist(m, vector<int>(n, -1));
    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    q.push(s); dist[s.first][s.second] = 0;
    while(!q.empty()){
        auto [x,y] = q.front(); q.pop();
        if (make_pair(x,y) == t) return dist[x][y];
        for (auto& d: dirs){
            int nx=x+d[0], ny=y+d[1];
            if (nx>=0&&nx<m&&ny>=0&&ny<n && g[nx][ny] != '#' && dist[nx][ny]==-1){
                dist[nx][ny] = dist[x][y] + 1; q.push({nx,ny});
            }
        }
    }
    return -1;
}
```

| ID | Title | Link |
|---|---|---|
| 200 | Number of Islands | https://leetcode.com/problems/number-of-islands/ |
| 417 | Pacific Atlantic Water Flow | https://leetcode.com/problems/pacific-atlantic-water-flow/ |
| 542 | 01 Matrix | https://leetcode.com/problems/01-matrix/ |

## DFS / Backtracking

```cpp
// Subsets
void dfs(int i, vector<int>& nums, vector<int>& cur, vector<vector<int>>& out){
    if (i == (int)nums.size()){ out.push_back(cur); return; }
    dfs(i+1, nums, cur, out);           // skip
    cur.push_back(nums[i]);
    dfs(i+1, nums, cur, out);           // take
    cur.pop_back();
}
```

| ID | Title | Link |
|---|---|---|
| 78 | Subsets | https://leetcode.com/problems/subsets/ |
| 46 | Permutations | https://leetcode.com/problems/permutations/ |
| 39 | Combination Sum | https://leetcode.com/problems/combination-sum/ |
| 77 | Combinations | https://leetcode.com/problems/combinations/ |

## Trees

## Tree Traversals (iterative)

// Inorder (iterative)
```cpp
vector<int> inorder(TreeNode* root){
    vector<int> ans; stack<TreeNode*> st; auto cur = root;
    while (cur || !st.empty()){
        while (cur){ st.push(cur); cur = cur->left; }
        cur = st.top(); st.pop(); ans.push_back(cur->val); cur = cur->right;
    }
    return ans;
}
```

// Level-order (BFS)
```cpp
vector<vector<int>> levelOrder(TreeNode* root){
    vector<vector<int>> res; if(!root) return res; queue<TreeNode*> q; q.push(root);
    while(!q.empty()){
        int sz=q.size(); res.emplace_back();
        while(sz--){ auto* u=q.front(); q.pop(); res.back().push_back(u->val);
            if(u->left) q.push(u->left); if(u->right) q.push(u->right);
        }
    }
    return res;
}
```

## LCA (Binary Lifting)

```cpp
const int K = 17; // adjust for n (e.g., 17 for n<=1e5)
vector<int> depth;
vector<array<int, K+1>> up;

void dfsLift(int u, int p, const vector<vector<int>>& g){
    up[u][0] = p;
    for(int k=1;k<=K;++k)
        up[u][k] = (up[u][k-1] < 0) ? -1 : up[ up[u][k-1] ][k-1];
    for(int v: g[u]) if(v != p){
        depth[v] = depth[u] + 1;
        dfsLift(v, u, g);
    }
}

int lift(int u, int k){
    for(int i=0;i<=K;++i)
        if(k & (1<<i)) u = (u<0) ? -1 : up[u][i];
    return u;
}

int lca(int a, int b){
    if(depth[a] < depth[b]) swap(a,b);
    a = lift(a, depth[a]-depth[b]);
    if(a == b) return a;
    for(int i=K;i>=0;--i)
        if(up[a][i] != up[b][i]){ a = up[a][i]; b = up[b][i]; }
    return up[a][0];
}
```

| ID | Title | Link |
|---|---|---|
| 236 | Lowest Common Ancestor of a Binary Tree | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ |
| 235 | Lowest Common Ancestor of a BST | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ |

## HLD (Heavy-Light Decomposition) skeleton

```cpp
// Heavy-Light Decomposition for path queries on a tree
// Build: dfs1 (sizes, heavy child), dfs2 (head/in), then segtree over in[]
const int N = 200000;
vector<int> gH[N];
int szH[N], parH[N], depH[N], heavyH[N], headH[N], inH[N], curT=0;

int dfs1(int u, int p){
    parH[u]=p; depH[u]=(p==-1?0:depH[p]+1); szH[u]=1; heavyH[u]=-1; int best=0;
    for(int v: gH[u]) if(v!=p){
        int s = dfs1(v,u); szH[u]+=s;
        if (s > best){ best=s; heavyH[u]=v; }
    }
    return szH[u];
}

void dfs2(int u, int h){
    headH[u]=h; inH[u]=curT++;
    if (heavyH[u]!=-1){
        dfs2(heavyH[u], h);
        for(int v: gH[u]) if(v!=parH[u] && v!=heavyH[u]) dfs2(v, v);
    }
}

// Example segment tree over values on nodes (mapped by inH[])
struct Seg{ int n; vector<long long> st; Seg(int n):n(n),st(4*n,0){}
    void upd(int p,long long v,int i,int l,int r){ if(l==r){ st[i]=v; return; }
        int m=(l+r)/2; if(p<=m) upd(p,v,2*i,l,m); else upd(p,v,2*i+1,m+1,r);
        st[i]=st[2*i]+st[2*i+1]; }
    long long qry(int ql,int qr,int i,int l,int r){ if(qr<l||r<ql) return 0; if(ql<=l&&r<=qr) return st[i];
        int m=(l+r)/2; return qry(ql,qr,2*i,l,m)+qry(ql,qr,2*i+1,m+1,r); }
};

long long queryPath(int a,int b, Seg& seg){
    long long res=0;
    while(headH[a]!=headH[b]){
        if(depH[ headH[a] ] < depH[ headH[b] ]) swap(a,b);
        res += seg.qry(inH[ headH[a] ], inH[a], 1, 0, seg.n-1);
        a = parH[ headH[a] ];
    }
    if (depH[a] > depH[b]) swap(a,b);
    res += seg.qry(inH[a], inH[b], 1, 0, seg.n-1);
    return res;
}
```

| ID | Title | Link |
|---|---|---|
| — | (Rare in LC; use for path queries if needed) | — |

## Union-Find (Disjoint Set Union)

```cpp
struct DSU{
    vector<int> p, r;
    DSU(int n): p(n), r(n,0){ iota(p.begin(), p.end(), 0); }
    int find(int x){ return p[x]==x?x:p[x]=find(p[x]); }
    bool unite(int a, int b){ a=find(a); b=find(b); if (a==b) return false; if (r[a]<r[b]) swap(a,b); p[b]=a; if (r[a]==r[b]) ++r[a]; return true; }
};
```

| ID | Title | Link |
|---|---|---|
| 684 | Redundant Connection | https://leetcode.com/problems/redundant-connection/ |
| 721 | Accounts Merge | https://leetcode.com/problems/accounts-merge/ |
| 1319 | Number of Operations to Make Network Connected | https://leetcode.com/problems/number-of-operations-to-make-network-connected/ |

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

| ID | Title | Link |
|---|---|---|
| 23 | Merge k Sorted Lists | https://leetcode.com/problems/merge-k-sorted-lists/ |
| 295 | Find Median from Data Stream | https://leetcode.com/problems/find-median-from-data-stream/ |

## Topological Sort (Kahn / DFS)

```cpp
vector<int> topoKahn(int n, const vector<vector<int>>& g){
    vector<int> indeg(n); for(int u=0;u<n;++u) for(int v:g[u]) ++indeg[v];
    queue<int> q; for(int i=0;i<n;++i) if(!indeg[i]) q.push(i);
    vector<int> order;
    while(!q.empty()){ int u=q.front(); q.pop(); order.push_back(u);
        for(int v:g[u]) if(--indeg[v]==0) q.push(v);
    }
    if ((int)order.size()!=n) order.clear();
    return order;
}
```

| ID | Title | Link |
|---|---|---|
| 207 | Course Schedule | https://leetcode.com/problems/course-schedule/ |
| 210 | Course Schedule II | https://leetcode.com/problems/course-schedule-ii/ |
| 269 | Alien Dictionary | https://leetcode.com/problems/alien-dictionary/ |

## Dijkstra (Shortest Path with Weights ≥ 0)

```cpp
vector<long long> dijkstra(int n, const vector<vector<pair<int,int>>>& g, int s){
    const long long INF = (1LL<<60);
    vector<long long> dist(n, INF); dist[s]=0;
    using P=pair<long long,int>; priority_queue<P, vector<P>, greater<P>> pq; pq.push({0,s});
    while(!pq.empty()){
        auto [d,u]=pq.top(); pq.pop(); if(d!=dist[u]) continue;
        for(auto [v,w]: g[u]) if(dist[v]>d+w){ dist[v]=d+w; pq.push({dist[v],v}); }
    }
    return dist;
}
```

| ID | Title | Link |
|---|---|---|
| 743 | Network Delay Time | https://leetcode.com/problems/network-delay-time/ |
| 1631 | Path With Minimum Effort | https://leetcode.com/problems/path-with-minimum-effort/ |

## 0-1 BFS (Edge Weights 0 or 1)

| ID | Title | Link |
|---|---|---|
| 1293 | Shortest Path in a Grid with Obstacles Elimination | https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/ |
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |

## Trie (Prefix Tree)

| ID | Title | Link |
|---|---|---|
| 208 | Implement Trie (Prefix Tree) | https://leetcode.com/problems/implement-trie-prefix-tree/ |
| 211 | Design Add and Search Words Data Structure | https://leetcode.com/problems/design-add-and-search-words-data-structure/ |
| 212 | Word Search II | https://leetcode.com/problems/word-search-ii/ |

## KMP (Substring Search)

| ID | Title | Link |
|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ |
| 214 | Shortest Palindrome | https://leetcode.com/problems/shortest-palindrome/ |

## LIS (Patience Sorting, O(n log n))

| ID | Title | Link |
|---|---|---|
| 300 | Longest Increasing Subsequence | https://leetcode.com/problems/longest-increasing-subsequence/ |
| 354 | Russian Doll Envelopes | https://leetcode.com/problems/russian-doll-envelopes/ |

## Segment Tree (Range Query/Point Update)

| ID | Title | Link |
|---|---|---|
| 307 | Range Sum Query – Mutable | https://leetcode.com/problems/range-sum-query-mutable/ |
| 732 | My Calendar III | https://leetcode.com/problems/my-calendar-iii/ |

## Fenwick Tree (Binary Indexed Tree)

| ID | Title | Link |
|---|---|---|
| 315 | Count of Smaller Numbers After Self | https://leetcode.com/problems/count-of-smaller-numbers-after-self/ |
| 307 | Range Sum Query – Mutable | https://leetcode.com/problems/range-sum-query-mutable/ |

## Bitmask DP (TSP / subsets)

| ID | Title | Link |
|---|---|---|
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |
| 698 | Partition to K Equal Sum Subsets | https://leetcode.com/problems/partition-to-k-equal-sum-subsets/ |

## Math & Geometry

## Math / Combinatorics (nCk mod P)

| ID | Title | Link |
|---|---|---|
| 62 | Unique Paths | https://leetcode.com/problems/unique-paths/ |
| 172 | Factorial Trailing Zeroes | https://leetcode.com/problems/factorial-trailing-zeroes/ |

## Geometry Primitives (2D)

| ID | Title | Link |
|---|---|---|
| 149 | Max Points on a Line | https://leetcode.com/problems/max-points-on-a-line/ |
| 223 | Rectangle Area | https://leetcode.com/problems/rectangle-area/ |

## Manacher (Longest Palindromic Substring, O(n))

| ID | Title | Link |
|---|---|---|
| 5 | Longest Palindromic Substring | https://leetcode.com/problems/longest-palindromic-substring/ |

## Z-Algorithm (Pattern occurrences)

| ID | Title | Link |
|---|---|---|
| 1392 | Longest Happy Prefix | https://leetcode.com/problems/longest-happy-prefix/ |

## Coordinate Compression

| ID | Title | Link |
|---|---|---|
| 315 | Count of Smaller Numbers After Self | https://leetcode.com/problems/count-of-smaller-numbers-after-self/ |
| 327 | Count of Range Sum | https://leetcode.com/problems/count-of-range-sum/ |

## Meet-in-the-Middle (subset sums)

| ID | Title | Link |
|---|---|---|
| 1755 | Closest Subsequence Sum | https://leetcode.com/problems/closest-subsequence-sum/ |
| 805 | Split Array With Same Average | https://leetcode.com/problems/split-array-with-same-average/ |

## Bitwise Trie (Max XOR Pair)

| ID | Title | Link |
|---|---|---|
| 421 | Maximum XOR of Two Numbers in an Array | https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/ |

## Advanced Techniques

## Tarjan SCC (Strongly Connected Components)

```cpp
// Tarjan's algorithm: O(N+M) to label each node with SCC id
struct TarjanSCC {
    int n, timer = 0, compCnt = 0;
    vector<vector<int>> g;
    vector<int> tin, low, comp, st;
    vector<char> in;

    TarjanSCC(int n): n(n), g(n), tin(n, -1), low(n), comp(n, -1), in(n, 0) {}
    void addEdge(int u, int v) { g[u].push_back(v); }

    void dfs(int u) {
        tin[u] = low[u] = timer++;
        st.push_back(u); in[u] = 1;
        for (int v : g[u]) {
            if (tin[v] == -1) { dfs(v); low[u] = min(low[u], low[v]); }
            else if (in[v])     low[u] = min(low[u], tin[v]);
        }
        if (low[u] == tin[u]) {
            for (;;) {
                int v = st.back(); st.pop_back(); in[v] = 0; comp[v] = compCnt;
                if (v == u) break;
            }
            ++compCnt;
        }
    }

    int run() { for (int i = 0; i < n; ++i) if (tin[i] == -1) dfs(i); return compCnt; }
};
```

| ID | Title | Link |
|---|---|---|
| 1192 | Critical Connections in a Network | https://leetcode.com/problems/critical-connections-in-a-network/ |
| 802 | Find Eventual Safe States (SCC/topo variant) | https://leetcode.com/problems/find-eventual-safe-states/ |

## Sweep Line (Intervals)

| ID | Title | Link |
|---|---|---|
| 218 | The Skyline Problem | https://leetcode.com/problems/the-skyline-problem/ |
| 253 | Meeting Rooms II | https://leetcode.com/problems/meeting-rooms-ii/ |

## Greedy

| ID | Title | Link |
|---|---|---|
| 435 | Non-overlapping Intervals | https://leetcode.com/problems/non-overlapping-intervals/ |
| 56 | Merge Intervals | https://leetcode.com/problems/merge-intervals/ |
| 621 | Task Scheduler | https://leetcode.com/problems/task-scheduler/ |

```cpp
// Interval scheduling: select max non-overlapping
int schedule(vector<pair<int,int>>& iv){
    sort(iv.begin(), iv.end(), [](auto& a, auto& b){return a.second<b.second;});
    int cnt=0, end=-1e9;
    for (auto& [s,e]: iv){ if (s>=end){ ++cnt; end=e; } }
    return cnt;
}
```
{% endraw %}
