---
layout: post
title: "LeetCode Templates: Trees"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates trees
permalink: /posts/2025-10-29-leetcode-templates-trees/
tags: [leetcode, templates, trees]
---

## Contents

- [Traversals (iterative)](#traversals-iterative)
- [LCA (Binary Lifting)](#lca-binary-lifting)
- [Segment Tree](#segment-tree)
- [HLD (Heavy-Light Decomposition)](#hld-heavy-light-decomposition-skeleton)

## Traversals (iterative)

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

| ID | Title | Link | Solution |
|---|---|---|---|
| 94 | Binary Tree Inorder Traversal | [Link](https://leetcode.com/problems/binary-tree-inorder-traversal/) | - |
| 102 | Binary Tree Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-102-binary-tree-level-order-traversal/) |

## LCA (Binary Lifting)

```cpp
const int K = 17; vector<int> depth; vector<array<int,K+1>> up;
void dfsLift(int u,int p,const vector<vector<int>>& g){ up[u][0]=p; for(int k=1;k<=K;++k) up[u][k]= up[u][k-1]<0?-1: up[up[u][k-1]][k-1];
    for(int v:g[u]) if(v!=p){ depth[v]=depth[u]+1; dfsLift(v,u,g);} }
int lift(int u,int k){ for(int i=0;i<=K;++i) if(k&(1<<i)) u = (u<0)?-1: up[u][i]; return u; }
int lca(int a,int b){ if(depth[a]<depth[b]) swap(a,b); a=lift(a, depth[a]-depth[b]); if(a==b) return a; for(int i=K;i>=0;--i) if(up[a][i]!=up[b][i]){ a=up[a][i]; b=up[b][i]; } return up[a][0]; }
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 236 | Lowest Common Ancestor of a Binary Tree | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | - |
| 235 | Lowest Common Ancestor of a BST | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | - |
| 270 | Closest Binary Search Tree Value | [Link](https://leetcode.com/problems/closest-binary-search-tree-value/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/easy-270-closest-binary-search-tree-value/) |
| 285 | Inorder Successor in BST | [Link](https://leetcode.com/problems/inorder-successor-in-bst/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/medium-285-inorder-successor-in-bst/) |

## Segment Tree

Segment Tree is a data structure that allows efficient range queries and range updates on an array. It's particularly useful for problems involving range sum, range minimum/maximum, and range updates.

**Reference:** [A Recursive Approach to Segment Trees, Range Sum Queries, and Lazy Propagation](https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/)

### Basic Segment Tree (Range Sum Query)

```cpp
class SegmentTree {
public:
    SegmentTree(vector<int>& nums) {
        n = nums.size();
        tree.resize(4 * n);
        build(nums, 1, 0, n - 1);
    }
    
    void update(int index, int val) {
        update(1, 0, n - 1, index, val);
    }
    
    int query(int left, int right) {
        return query(1, 0, n - 1, left, right);
    }
    
private:
    int n;
    vector<int> tree;
    
    void build(vector<int>& nums, int node, int l, int r) {
        if (l == r) {
            tree[node] = nums[l];
        } else {
            int mid = (l + r) / 2;
            build(nums, node * 2, l, mid);
            build(nums, node * 2 + 1, mid + 1, r);
            tree[node] = tree[node * 2] + tree[node * 2 + 1];
        }
    }
    
    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = val;
        } else {
            int mid = (l + r) / 2;
            if (idx <= mid) {
                update(node * 2, l, mid, idx, val);
            } else {
                update(node * 2 + 1, mid + 1, r, idx, val);
            }
            tree[node] = tree[node * 2] + tree[node * 2 + 1];
        }
    }
    
    int query(int node, int l, int r, int ql, int qr) {
        if (qr < l || ql > r) return 0;
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        return query(node * 2, l, mid, ql, qr) + 
               query(node * 2 + 1, mid + 1, r, ql, qr);
    }
};
```

### Segment Tree with Lazy Propagation (Range Update)

```cpp
class SegmentTreeLazy {
public:
    SegmentTreeLazy(vector<int>& nums) {
        n = nums.size();
        tree.resize(4 * n);
        lazy.resize(4 * n, 0);
        build(nums, 1, 0, n - 1);
    }
    
    void updateRange(int left, int right, int val) {
        updateRange(1, 0, n - 1, left, right, val);
    }
    
    int query(int left, int right) {
        return query(1, 0, n - 1, left, right);
    }
    
private:
    int n;
    vector<int> tree, lazy;
    
    void build(vector<int>& nums, int node, int l, int r) {
        if (l == r) {
            tree[node] = nums[l];
        } else {
            int mid = (l + r) / 2;
            build(nums, node * 2, l, mid);
            build(nums, node * 2 + 1, mid + 1, r);
            tree[node] = tree[node * 2] + tree[node * 2 + 1];
        }
    }
    
    void push(int node, int l, int r) {
        if (lazy[node] != 0) {
            tree[node] += lazy[node] * (r - l + 1);
            if (l != r) {
                lazy[node * 2] += lazy[node];
                lazy[node * 2 + 1] += lazy[node];
            }
            lazy[node] = 0;
        }
    }
    
    void updateRange(int node, int l, int r, int ql, int qr, int val) {
        push(node, l, r);
        if (qr < l || ql > r) return;
        if (ql <= l && r <= qr) {
            lazy[node] += val;
            push(node, l, r);
            return;
        }
        int mid = (l + r) / 2;
        updateRange(node * 2, l, mid, ql, qr, val);
        updateRange(node * 2 + 1, mid + 1, r, ql, qr, val);
        push(node * 2, l, mid);
        push(node * 2 + 1, mid + 1, r);
        tree[node] = tree[node * 2] + tree[node * 2 + 1];
    }
    
    int query(int node, int l, int r, int ql, int qr) {
        push(node, l, r);
        if (qr < l || ql > r) return 0;
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        return query(node * 2, l, mid, ql, qr) + 
               query(node * 2 + 1, mid + 1, r, ql, qr);
    }
};
```

### Generic Segment Tree Template

```cpp
template<typename T, typename Merge = plus<T>>
class SegmentTree {
public:
    SegmentTree(vector<T>& arr, T identity = T(), Merge merge = Merge()) 
        : n(arr.size()), tree(4 * n), identity(identity), merge(merge) {
        build(arr, 1, 0, n - 1);
    }
    
    void update(int index, T val) {
        update(1, 0, n - 1, index, val);
    }
    
    T query(int left, int right) {
        return query(1, 0, n - 1, left, right);
    }
    
private:
    int n;
    vector<T> tree;
    T identity;
    Merge merge;
    
    void build(vector<T>& arr, int node, int l, int r) {
        if (l == r) {
            tree[node] = arr[l];
        } else {
            int mid = (l + r) / 2;
            build(arr, node * 2, l, mid);
            build(arr, node * 2 + 1, mid + 1, r);
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
        }
    }
    
    void update(int node, int l, int r, int idx, T val) {
        if (l == r) {
            tree[node] = val;
        } else {
            int mid = (l + r) / 2;
            if (idx <= mid) {
                update(node * 2, l, mid, idx, val);
            } else {
                update(node * 2 + 1, mid + 1, r, idx, val);
            }
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
        }
    }
    
    T query(int node, int l, int r, int ql, int qr) {
        if (qr < l || ql > r) return identity;
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        return merge(query(node * 2, l, mid, ql, qr),
                     query(node * 2 + 1, mid + 1, r, ql, qr));
    }
};

// Usage examples:
// Range Sum: SegmentTree<int> st(arr, 0);
// Range Min: SegmentTree<int, function<int(int,int)>> st(arr, INT_MAX, [](int a, int b) { return min(a, b); });
// Range Max: SegmentTree<int, function<int(int,int)>> st(arr, INT_MIN, [](int a, int b) { return max(a, b); });
```

### Key Concepts

1. **Tree Structure**: Binary tree where each node represents a range `[l, r]`
2. **Build**: O(n) - Construct tree from array
3. **Point Update**: O(log n) - Update single element
4. **Range Query**: O(log n) - Query sum/min/max over range
5. **Lazy Propagation**: O(log n) - Defer range updates for efficiency
6. **Space Complexity**: O(4n) - Array-based representation

### When to Use

- **Range Queries**: Sum, min, max, gcd over ranges
- **Range Updates**: Add/subtract value to all elements in range
- **Frequent Updates**: When updates and queries are interleaved
- **Large Arrays**: When brute force is too slow

### Easy

| ID | Title | Link | Solution |
|---|---|---|---|
| 303 | Range Sum Query - Immutable | [Link](https://leetcode.com/problems/range-sum-query-immutable/) | - |
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/15/medium-307-range-sum-query-mutable/) |

### Medium

| ID | Title | Link | Solution |
|---|---|---|---|
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/15/medium-307-range-sum-query-mutable/) |
| 308 | Range Sum Query 2D - Mutable | [Link](https://leetcode.com/problems/range-sum-query-2d-mutable/) | - |
| 715 | Range Module | [Link](https://leetcode.com/problems/range-module/) | - |
| 729 | My Calendar I | [Link](https://leetcode.com/problems/my-calendar-i/) | - |
| 731 | My Calendar II | [Link](https://leetcode.com/problems/my-calendar-ii/) | - |
| 1177 | Can Make Palindrome from Substring | [Link](https://leetcode.com/problems/can-make-palindrome-from-substring/) | - |
| 1505 | Minimum Possible Integer After at Most K Swaps | [Link](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) | - |
| 1649 | Create Sorted Array through Instructions | [Link](https://leetcode.com/problems/create-sorted-array-through-instructions/) | - |
| 3477 | Number of Unplaced Fruits | [Link](https://leetcode.com/problems/number-of-unplaced-fruits/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/15/medium-3477-number-of-unplaced-fruits/) |

### Hard

| ID | Title | Link | Solution |
|---|---|---|---|
| 218 | The Skyline Problem | [Link](https://leetcode.com/problems/the-skyline-problem/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/05/hard-218-skyline-problem/) |
| 699 | Falling Squares | [Link](https://leetcode.com/problems/falling-squares/) | - |
| 715 | Range Module | [Link](https://leetcode.com/problems/range-module/) | - |
| 732 | My Calendar III | [Link](https://leetcode.com/problems/my-calendar-iii/) | - |
| 850 | Rectangle Area II | [Link](https://leetcode.com/problems/rectangle-area-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-16-hard-850-rectangle-area-ii/) |
| 1157 | Online Majority Element In Subarray | [Link](https://leetcode.com/problems/online-majority-element-in-subarray/) | - |
| 2407 | Longest Increasing Subsequence II | [Link](https://leetcode.com/problems/longest-increasing-subsequence-ii/) | - |

### References

- [LeetCode: A Recursive Approach to Segment Trees, Range Sum Queries, and Lazy Propagation](https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/) - Comprehensive guide to segment trees with examples

## HLD (Heavy-Light Decomposition) skeleton

```cpp
const int N = 200000; vector<int> gH[N]; int szH[N], parH[N], depH[N], heavyH[N], headH[N], inH[N], curT=0;
int dfs1(int u,int p){ parH[u]=p; depH[u]=(p==-1?0:depH[p]+1); szH[u]=1; heavyH[u]=-1; int best=0; for(int v:gH[u]) if(v!=p){ int s=dfs1(v,u); szH[u]+=s; if(s>best){best=s; heavyH[u]=v;} } return szH[u]; }
void dfs2(int u,int h){ headH[u]=h; inH[u]=curT++; if(heavyH[u]!=-1){ dfs2(heavyH[u],h); for(int v:gH[u]) if(v!=parH[u] && v!=heavyH[u]) dfs2(v,v);} }
```

> Note: HLD is rarely required on LeetCode.
