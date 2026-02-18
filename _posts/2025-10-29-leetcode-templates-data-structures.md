---
layout: post
title: "Algorithm Templates: Data Structures & Core Algorithms"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates data-structures algorithms
permalink: /posts/2025-10-29-leetcode-templates-data-structures/
tags: [leetcode, templates, data-structures, algorithms]
---

Minimal, copy-paste C++ templates for common structures and patterns. Each snippet is self-contained and uses standard indexing.

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

Half-open range `[lo, hi)`. Use when you need first ≥ x (lower_bound) or first > x (upper_bound).

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

Path compression + rank merge. `find(x)`, `unite(a,b)`.

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

Fixed alphabet (e.g. 26). Insert and search in O(|s|).

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

## More Templates

- **Graph (BFS, Dijkstra, Topo, DSU):** [Graph Templates](/posts/2025-10-29-leetcode-templates-graph/)
- **Binary search (rotated, 2D, answer space):** [Search Templates](/posts/2026-01-20-leetcode-templates-search/)
- **DP, Backtracking, Greedy, Stack:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
