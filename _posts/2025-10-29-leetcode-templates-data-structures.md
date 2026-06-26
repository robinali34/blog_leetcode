---
layout: post
title: "Algorithm Templates: Data Structures & Core Algorithms"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates data-structures algorithms
permalink: /posts/2025-10-29-leetcode-templates-data-structures/
tags: [leetcode, templates, data-structures, algorithms]
---

This page is your toolbox of essential data structures for LeetCode. Each template is self-contained C++ you can copy directly into your solution. They range from beginner-friendly (binary search, prefix sum) to advanced (segment tree, sparse table) — start with what you need and come back for more as you level up.

> **This is the foundation.** These data structures are the building blocks that other templates (DFS, BFS, DP) build on. Master binary search and prefix sums first, then work outward — you'll see them appear inside graph, tree, and dynamic programming solutions.

<svg viewBox="0 0 740 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="370" y="22" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Which Data Structure Do I Need?</text>
  <rect x="30" y="40" width="150" height="44" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="105" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Sorted + search?</text>
  <text x="105" y="76" font-size="10" fill="#7A7772" text-anchor="middle">→ Binary Search</text>
  <rect x="200" y="40" width="150" height="44" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="275" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Range sums?</text>
  <text x="275" y="76" font-size="10" fill="#7A7772" text-anchor="middle">→ Prefix Sum / BIT</text>
  <rect x="370" y="40" width="150" height="44" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="445" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Next greater/smaller?</text>
  <text x="445" y="76" font-size="10" fill="#7A7772" text-anchor="middle">→ Monotonic Stack</text>
  <rect x="500" y="40" width="150" height="44" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="575" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Top-K / min cost?</text>
  <text x="575" y="76" font-size="10" fill="#7A7772" text-anchor="middle">→ Heap</text>
  <rect x="30" y="110" width="150" height="44" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="105" y="128" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Connected groups?</text>
  <text x="105" y="146" font-size="10" fill="#7A7772" text-anchor="middle">→ Union-Find (DSU)</text>
  <rect x="200" y="110" width="150" height="44" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="275" y="128" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Prefix of strings?</text>
  <text x="275" y="146" font-size="10" fill="#7A7772" text-anchor="middle">→ Trie</text>
  <rect x="370" y="110" width="150" height="44" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="445" y="128" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Range query + update?</text>
  <text x="445" y="146" font-size="10" fill="#7A7772" text-anchor="middle">→ Segment Tree</text>
  <rect x="500" y="110" width="150" height="44" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="575" y="128" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Static range min/max?</text>
  <text x="575" y="146" font-size="10" fill="#7A7772" text-anchor="middle">→ Sparse Table</text>
  <text x="370" y="185" font-size="10" fill="#9A9792" text-anchor="middle">Start with binary search + prefix sum — they appear inside most other patterns</text>
</svg>

## Contents

- [Binary Search (Bounds)](#binary-search-bounds)
- [Prefix Sum & Difference Array](#prefix-sum--difference-array)
- [Monotonic Stack](#monotonic-stack)
- [Monotonic Queue](#monotonic-queue)
- [Heap / Priority Queue](#heap--priority-queue)
- [Union-Find (DSU)](#union-find-dsu)
- [Trie](#trie)
- [Segment Tree](#segment-tree)
- [Fenwick Tree (BIT)](#fenwick-tree-bit)
- [Sparse Table (Range Min/Max)](#sparse-table-range-minmax)

---

## Binary Search (Bounds)

**When to use:** The input is sorted (or the answer space is monotonic) and you need to find a boundary — first element ≥ x, last element ≤ x, or the minimum/maximum value satisfying a condition.

Half-open range `[lo, hi)`. Use when you need first ≥ x (lower_bound) or first > x (upper_bound).

<svg viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="340" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Binary Search on [2, 5, 8, 12, 16, 23, 38] — target = 23</text>
  <rect x="80" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="105" y="51" font-size="12" fill="#5A5752" text-anchor="middle">2</text>
  <rect x="130" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="155" y="51" font-size="12" fill="#5A5752" text-anchor="middle">5</text>
  <rect x="180" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="205" y="51" font-size="12" fill="#5A5752" text-anchor="middle">8</text>
  <rect x="230" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="255" y="51" font-size="12" fill="#5A5752" text-anchor="middle">12</text>
  <rect x="280" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="305" y="51" font-size="12" fill="#5A5752" text-anchor="middle">16</text>
  <rect x="330" y="30" width="50" height="32" rx="4" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="355" y="51" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">23</text>
  <rect x="380" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="405" y="51" font-size="12" fill="#5A5752" text-anchor="middle">38</text>
  <text x="105" y="78" font-size="10" fill="#7080A0" font-weight="600">lo</text>
  <text x="355" y="78" font-size="10" fill="#C08070" font-weight="600">mid ✓</text>
  <text x="405" y="78" font-size="10" fill="#7080A0" font-weight="600">hi</text>
  <text x="340" y="110" font-size="10" fill="#5A5752" text-anchor="middle">Step 1: lo=0, hi=6, mid=3 → 12 &lt; 23 → lo=4</text>
  <text x="340" y="128" font-size="10" fill="#5A5752" text-anchor="middle">Step 2: lo=4, hi=6, mid=5 → 23 = target → found!</text>
  <text x="340" y="150" font-size="10" fill="#3A6B3A" font-weight="600" text-anchor="middle">Key: half-open range [lo, hi) — mid never equals hi</text>
</svg>

```cpp
// First index where a[i] >= x (lower_bound)
int lower_bound(const vector<int>& a, int x) {
    int lo = 0, hi = a.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

// First index where a[i] > x (upper_bound)
int upper_bound(const vector<int>& a, int x) {
    int lo = 0, hi = a.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] <= x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

// Binary search on answer: smallest x in [lo, hi] such that ok(x)
template<class F>
int bsearch_ans(int lo, int hi, F ok) {
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

| ID | Title | Link |
|----|--------|------|
| 34 | Find First and Last Position | [Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 35 | Search Insert Position | [Link](https://leetcode.com/problems/search-insert-position/) |
| 875 | Koko Eating Bananas | [Link](https://leetcode.com/problems/koko-eating-bananas/) |

---

## Prefix Sum & Difference Array

**When to use:** You need to answer many "sum of subarray [l, r]" queries, or apply the same increment to many ranges efficiently.

Prefix sum: range sum in O(1). Difference array: range add in O(1), then one prefix sum to recover.

```cpp
// Prefix sum: ps[i] = a[0]+...+a[i-1], sum(l,r) = ps[r+1]-ps[l]
vector<long long> prefix(const vector<int>& a) {
    vector<long long> ps(a.size() + 1);
    for (int i = 0; i < (int)a.size(); i++) ps[i + 1] = ps[i] + a[i];
    return ps;
}

// Difference array: for [l,r] += d do diff[l]+=d, diff[r+1]-=d; then partial_sum(diff) = values
void range_add(vector<long long>& diff, int l, int r, long long d) {
    diff[l] += d;
    if (r + 1 < (int)diff.size()) diff[r + 1] -= d;
}
// After all updates: partial_sum(diff.begin(), diff.end(), diff.begin());
```

| ID | Title | Link |
|----|--------|------|
| 560 | Subarray Sum Equals K | [Link](https://leetcode.com/problems/subarray-sum-equals-k/) |
| 1109 | Corporate Flight Bookings | [Link](https://leetcode.com/problems/corporate-flight-bookings/) |
| 1094 | Car Pooling | [Link](https://leetcode.com/problems/car-pooling/) |

---

## Monotonic Stack

**When to use:** You need "next greater element", "next smaller element", "largest rectangle in histogram", or any problem where each element is compared to its neighbors in one direction.

Maintain indices with strictly increasing (or decreasing) values. Use for next greater/smaller, or histogram rectangle.

```cpp
// Next greater element (for each index)
vector<int> next_greater(const vector<int>& a) {
    int n = a.size();
    vector<int> ng(n, -1);
    vector<int> st;
    for (int i = 0; i < n; i++) {
        while (!st.empty() && a[st.back()] < a[i]) {
            ng[st.back()] = a[i];
            st.pop_back();
        }
        st.push_back(i);
    }
    return ng;
}

// Circular: wrap with 2*n and only push when i < n
vector<int> next_greater_circular(const vector<int>& a) {
    int n = a.size();
    vector<int> ng(n, -1);
    vector<int> st;
    for (int i = 0; i < 2 * n; i++) {
        int j = i % n;
        while (!st.empty() && a[st.back()] < a[j]) {
            ng[st.back()] = a[j];
            st.pop_back();
        }
        if (i < n) st.push_back(j);
    }
    return ng;
}
```

| ID | Title | Link |
|----|--------|------|
| 739 | Daily Temperatures | [Link](https://leetcode.com/problems/daily-temperatures/) |
| 42 | Trapping Rain Water | [Link](https://leetcode.com/problems/trapping-rain-water/) |
| 84 | Largest Rectangle in Histogram | [Link](https://leetcode.com/problems/largest-rectangle-in-histogram/) |
| 503 | Next Greater Element II | [Link](https://leetcode.com/problems/next-greater-element-ii/) |
| 1944 | Visible People in Queue | [Link](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) |

---

## Monotonic Queue

**When to use:** You need the maximum or minimum within a sliding window of fixed size, or need to maintain a monotonic property as elements enter and leave a window.

Deque of indices with values in monotonic order. Sliding window max/min.

```cpp
// Sliding window maximum (window size k)
vector<int> max_sliding_window(const vector<int>& a, int k) {
    deque<int> dq;
    vector<int> out;
    for (int i = 0; i < (int)a.size(); i++) {
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
        dq.push_back(i);
        if (dq.front() <= i - k) dq.pop_front();
        if (i >= k - 1) out.push_back(a[dq.front()]);
    }
    return out;
}
```

| ID | Title | Link |
|----|--------|------|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) |
| 1438 | Longest Continuous Subarray With Abs Diff ≤ Limit | [Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) |

---

## Heap / Priority Queue

**When to use:** You repeatedly need the smallest (or largest) element — merging k sorted lists, scheduling, median maintenance, or any "top K" problem.

Min-heap: `priority_queue<T, vector<T>, greater<T>>`. K-way merge: push heads, pop min, push next from same list.

```cpp
// K-way merge of sorted arrays (or list heads)
vector<int> merge_k_sorted(const vector<vector<int>>& lists) {
    using T = tuple<int, int, int>;
    priority_queue<T, vector<T>, greater<T>> pq;
    for (int i = 0; i < (int)lists.size(); i++)
        if (!lists[i].empty()) pq.emplace(lists[i][0], i, 0);
    vector<int> out;
    while (!pq.empty()) {
        auto [v, i, j] = pq.top();
        pq.pop();
        out.push_back(v);
        if (j + 1 < (int)lists[i].size()) pq.emplace(lists[i][j + 1], i, j + 1);
    }
    return out;
}
```

| ID | Title | Link |
|----|--------|------|
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) |
| 295 | Find Median from Data Stream | [Link](https://leetcode.com/problems/find-median-from-data-stream/) |

---

## Union-Find (DSU)

**When to use:** You need to track connected components, determine if two nodes are in the same group, or merge groups — common in graph connectivity, redundant edge detection, and "accounts merge" problems.

Path compression + rank merge. `find(x)`, `unite(a,b)`.

<svg viewBox="0 0 680 150" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="340" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Union-Find — unite(1,2), unite(3,4), unite(2,3)</text>
  <circle cx="120" cy="55" r="22" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="2"/><text x="120" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">0</text>
  <circle cx="220" cy="55" r="22" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/><text x="220" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">1</text>
  <circle cx="320" cy="55" r="22" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/><text x="320" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">2</text>
  <circle cx="480" cy="55" r="22" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="480" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">3</text>
  <circle cx="580" cy="55" r="22" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="580" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">4</text>
  <line x1="220" y1="55" x2="120" y2="55" stroke="#6B8B6B" stroke-width="2"/>
  <line x1="320" y1="55" x2="220" y2="55" stroke="#6B8B6B" stroke-width="2"/>
  <line x1="580" y1="55" x2="480" y2="55" stroke="#C08070" stroke-width="2"/>
  <text x="220" y="100" font-size="10" fill="#3A6B3A" text-anchor="middle">Group {0,1,2}</text>
  <text x="530" y="100" font-size="10" fill="#C08070" text-anchor="middle">Group {3,4}</text>
  <text x="340" y="130" font-size="10" fill="#5A5752" text-anchor="middle">find(x) returns root with path compression | unite merges two groups</text>
</svg>

```cpp
struct DSU {
    vector<int> p, r;
    DSU(int n) : p(n), r(n, 0) { iota(p.begin(), p.end(), 0); }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    bool unite(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (r[a] < r[b]) swap(a, b);
        p[b] = a;
        if (r[a] == r[b]) r[a]++;
        return true;
    }
};
```

| ID | Title | Link |
|----|--------|------|
| 684 | Redundant Connection | [Link](https://leetcode.com/problems/redundant-connection/) |
| 721 | Accounts Merge | [Link](https://leetcode.com/problems/accounts-merge/) |
| 1319 | Number of Operations to Make Network Connected | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) |

---

## Trie

**When to use:** Problems involve prefix matching, autocomplete, word search in a dictionary, or "find all words with prefix X". Also useful for XOR-maximization with a bitwise trie.

Fixed alphabet (e.g. 26). Insert and search in O(|s|).

<svg viewBox="0 0 600 180" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="300" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Trie for words: "cat", "car", "dog"</text>
  <circle cx="300" cy="45" r="18" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="2"/><text x="300" y="50" font-size="10" fill="#5A5752" text-anchor="middle">root</text>
  <line x1="280" y1="60" x2="200" y2="90" stroke="#B8B5B0"/><line x1="320" y1="60" x2="400" y2="90" stroke="#B8B5B0"/>
  <circle cx="200" cy="100" r="16" fill="#D4D8D0" stroke="#B8B5B0"/><text x="200" y="105" font-size="11" fill="#5A5752" text-anchor="middle">c</text>
  <circle cx="400" cy="100" r="16" fill="#E8D5D0" stroke="#B8B5B0"/><text x="400" y="105" font-size="11" fill="#5A5752" text-anchor="middle">d</text>
  <line x1="185" y1="115" x2="150" y2="140" stroke="#B8B5B0"/><line x1="215" y1="115" x2="250" y2="140" stroke="#B8B5B0"/>
  <circle cx="150" cy="150" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="150" y="155" font-size="10" fill="#5A5752" text-anchor="middle">a</text>
  <circle cx="250" cy="150" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="250" y="155" font-size="10" fill="#5A5752" text-anchor="middle">a</text>
  <line x1="140" y1="162" x2="120" y2="172" stroke="#B8B5B0"/><line x1="160" y1="162" x2="180" y2="172" stroke="#B8B5B0"/>
  <text x="120" y="176" font-size="9" fill="#3A6B3A" text-anchor="middle">t✓</text>
  <text x="180" y="176" font-size="9" fill="#3A6B3A" text-anchor="middle">r✓</text>
  <line x1="400" y1="115" x2="400" y2="150" stroke="#B8B5B0"/>
  <circle cx="400" cy="160" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="400" y="165" font-size="10" fill="#5A5752" text-anchor="middle">o</text>
  <line x1="400" y1="172" x2="400" y2="176" stroke="#B8B5B0"/><text x="400" y="176" font-size="9" fill="#3A6B3A" text-anchor="middle">g✓</text>
  <text x="300" y="176" font-size="9" fill="#9A9792" text-anchor="middle">Shared prefixes share nodes — "cat" and "car" share c→a</text>
</svg>

```cpp
struct Trie {
    struct Node {
        int nxt[26];
        bool end = false;
        Node() { memset(nxt, -1, sizeof nxt); }
    };
    vector<Node> t{1};
    void insert(const string& s) {
        int u = 0;
        for (char c : s) {
            int i = c - 'a';
            if (t[u].nxt[i] == -1) { t[u].nxt[i] = t.size(); t.emplace_back(); }
            u = t[u].nxt[i];
        }
        t[u].end = true;
    }
    bool search(const string& s) {
        int u = 0;
        for (char c : s) {
            u = t[u].nxt[c - 'a'];
            if (u == -1) return false;
        }
        return t[u].end;
    }
};
```

| ID | Title | Link |
|----|--------|------|
| 208 | Implement Trie | [Link](https://leetcode.com/problems/implement-trie-prefix-tree/) |
| 211 | Design Add and Search Words | [Link](https://leetcode.com/problems/design-add-and-search-words-data-structure/) |
| 212 | Word Search II | [Link](https://leetcode.com/problems/word-search-ii/) |

---

## Segment Tree

**When to use:** You need both range queries (sum, min, max) AND point or range updates on the same array. More powerful than Fenwick tree when you need lazy propagation or non-commutative operations.

0-indexed range [0, n-1]. Point update, range sum (or min/max). Recursive implementation.

```cpp
struct SegTree {
    int n;
    vector<long long> st;
    SegTree(int n) : n(n), st(4 * n, 0) {}
    void upd(int i, int l, int r, int p, long long v) {
        if (l == r) { st[i] = v; return; }
        int m = (l + r) / 2;
        if (p <= m) upd(2 * i, l, m, p, v);
        else upd(2 * i + 1, m + 1, r, p, v);
        st[i] = st[2 * i] + st[2 * i + 1];
    }
    long long qry(int i, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return st[i];
        int m = (l + r) / 2;
        return qry(2 * i, l, m, ql, qr) + qry(2 * i + 1, m + 1, r, ql, qr);
    }
    void upd(int p, long long v) { upd(1, 0, n - 1, p, v); }
    long long qry(int ql, int qr) { return qry(1, 0, n - 1, ql, qr); }
};
```

| ID | Title | Link |
|----|--------|------|
| 307 | Range Sum Query – Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) |
| 732 | My Calendar III | [Link](https://leetcode.com/problems/my-calendar-iii/) |

---

## Fenwick Tree (BIT)

**When to use:** You need prefix sums with point updates — simpler and faster constant than segment tree when you don't need lazy propagation. Great for counting inversions or "count of smaller numbers after self".

1-indexed. Point add, prefix sum. Range sum [l, r] = sum(r) - sum(l-1).

```cpp
struct BIT {
    int n;
    vector<long long> f;
    BIT(int n) : n(n), f(n + 1, 0) {}
    void add(int i, long long v) {
        for (; i <= n; i += i & -i) f[i] += v;
    }
    long long sum(int i) {
        long long s = 0;
        for (; i > 0; i -= i & -i) s += f[i];
        return s;
    }
    long long range_sum(int l, int r) { return sum(r) - sum(l - 1); }
};
```

| ID | Title | Link |
|----|--------|------|
| 307 | Range Sum Query – Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) |
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 308 | Range Sum Query 2D – Mutable | [Link](https://leetcode.com/problems/range-sum-query-2d-mutable/) |

---

## Sparse Table (Range Min/Max)

**When to use:** You need O(1) range min/max/gcd queries with NO updates. Perfect for static arrays where you precompute once and query many times.

O(n log n) build, O(1) range min/max. Idempotent only (min, max, gcd). 0-indexed.

```cpp
struct SparseTable {
    vector<vector<int>> st;
    vector<int> lg;
    int op(int a, int b) { return min(a, b); } // or max
    SparseTable(const vector<int>& a) {
        int n = a.size();
        lg.assign(n + 1, 0);
        for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
        int k = lg[n] + 1;
        st.assign(n, vector<int>(k));
        for (int i = 0; i < n; i++) st[i][0] = a[i];
        for (int j = 1; j < k; j++)
            for (int i = 0; i + (1 << j) <= n; i++)
                st[i][j] = op(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
    }
    int qry(int l, int r) {
        int j = lg[r - l + 1];
        return op(st[l][j], st[r - (1 << j) + 1][j]);
    }
};
```

| ID | Title | Link |
|----|--------|------|
| — | Range min/max, GCD (no update) | — |

---

---

## Quick Reference

| Structure | When to Use | Operations | Time |
|---|---|---|---|
| Binary Search | Sorted data, find boundary | lower/upper bound | O(log n) |
| Prefix Sum | Range sum queries | build + query | O(n) + O(1) |
| Monotonic Stack | Next greater/smaller | push/pop | O(n) |
| DSU | Connected components, union | find/union | O(α(n)) |
| Trie | Prefix search, autocomplete | insert/search | O(L) |
| Segment Tree | Range query + update | build/query/update | O(n) + O(log n) |
| Fenwick Tree | Prefix sums + point update | update/query | O(log n) |

## More Templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Graph (BFS, Dijkstra, Topo, DSU):** [Graph Templates](/posts/2025-10-29-leetcode-templates-graph/)
- **Binary search (rotated, 2D, answer space):** [Search Templates](/posts/2026-01-20-leetcode-templates-search/)
- **DP, Backtracking, Greedy, Stack:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
