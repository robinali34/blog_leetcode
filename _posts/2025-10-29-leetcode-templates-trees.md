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
- [Binary Search on Segment Tree (Tree Walking)](#binary-search-on-segment-tree-tree-walking)
- [Fenwick Tree (Binary Indexed Tree)](#fenwick-tree-binary-indexed-tree)
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
| 103 | Binary Tree Zigzag Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/06/medium-103-binary-tree-zigzag-level-order-traversal/) |
| 429 | N-ary Tree Level Order Traversal | [Link](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-429-n-ary-tree-level-order-traversal/) |
| 314 | Binary Tree Vertical Order Traversal | [Link](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-314-binary-tree-vertical-order-traversal/) |

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
| 236 | Lowest Common Ancestor of a Binary Tree | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/medium-236-lowest-common-ancestor-of-a-binary-tree/) |
| 235 | Lowest Common Ancestor of a BST | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | - |
| 1650 | Lowest Common Ancestor of a Binary Tree III | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-1650-lowest-common-ancestor-of-a-binary-tree-iii/) |
| 270 | Closest Binary Search Tree Value | [Link](https://leetcode.com/problems/closest-binary-search-tree-value/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/easy-270-closest-binary-search-tree-value/) |
| 285 | Inorder Successor in BST | [Link](https://leetcode.com/problems/inorder-successor-in-bst/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/medium-285-inorder-successor-in-bst/) |
| 426 | Convert Binary Search Tree to Sorted Doubly Linked List | [Link](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-22-medium-426-convert-binary-search-tree-to-sorted-doubly-linked-list/) |
| 938 | Range Sum of BST | [Link](https://leetcode.com/problems/range-sum-of-bst/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-938-range-sum-of-bst/) |
| 100 | Same Tree | [Link](https://leetcode.com/problems/same-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-100-same-tree/) |
| 101 | Symmetric Tree | [Link](https://leetcode.com/problems/symmetric-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-101-symmetric-tree/) |
| 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-104-maximum-depth-of-binary-tree/) |
| 111 | Minimum Depth of Binary Tree | [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-111-minimum-depth-of-binary-tree/) |
| 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-112-path-sum/) |
| 226 | Invert Binary Tree | [Link](https://leetcode.com/problems/invert-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-226-invert-binary-tree/) |
| 437 | Path Sum III | [Link](https://leetcode.com/problems/path-sum-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-437-path-sum-iii/) |
| 129 | Sum Root to Leaf Numbers | [Link](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-129-sum-root-to-leaf-numbers/) |
| 863 | All Nodes Distance K in Binary Tree | [Link](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-25-medium-863-all-nodes-distance-k-in-binary-tree/) |
| 545 | Boundary of Binary Tree | [Link](https://leetcode.com/problems/boundary-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-545-boundary-of-binary-tree/) |
| 993 | Cousins in Binary Tree | [Link](https://leetcode.com/problems/cousins-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/easy-993-cousins-in-binary-tree/) |
| 1443 | Minimum Time to Collect All Apples in a Tree | [Link](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-1443-minimum-time-to-collect-all-apples-in-a-tree/) |

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

### Binary Search on Segment Tree (Tree Walking)

Instead of doing a binary search over an index and then a segment tree query ($O(\log^2 N)$), we descend the segment tree directly to find the first element satisfying a condition in $O(\log N)$.

#### Template: Find First Index >= X

```cpp
int findFirst(Node* node, int l, int r, int x) {
    if (node->maxVal < x) return -1;
    if (l == r) return l;
    
    int mid = l + (r - l) / 2;
    int res = findFirst(node->left, l, mid, x);
    if (res == -1) {
        res = findFirst(node->right, mid + 1, r, x);
    }
    return res;
}
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
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-307-range-sum-query-mutable/) |

### Medium

| ID | Title | Link | Solution |
|---|---|---|---|
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-307-range-sum-query-mutable/) |
| 308 | Range Sum Query 2D - Mutable | [Link](https://leetcode.com/problems/range-sum-query-2d-mutable/) | - |
| 715 | Range Module | [Link](https://leetcode.com/problems/range-module/) | - |
| 729 | My Calendar I | [Link](https://leetcode.com/problems/my-calendar-i/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/17/medium-729-my-calendar-i/) |
| 731 | My Calendar II | [Link](https://leetcode.com/problems/my-calendar-ii/) | - |
| 1177 | Can Make Palindrome from Substring | [Link](https://leetcode.com/problems/can-make-palindrome-from-substring/) | - |
| 1505 | Minimum Possible Integer After at Most K Swaps | [Link](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) | - |
| 1649 | Create Sorted Array through Instructions | [Link](https://leetcode.com/problems/create-sorted-array-through-instructions/) | - |
| 3477 | Number of Unplaced Fruits | [Link](https://leetcode.com/problems/number-of-unplaced-fruits/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-3477-number-of-unplaced-fruits/) |

### Hard

| ID | Title | Link | Solution |
|---|---|---|---|
| 218 | The Skyline Problem | [Link](https://leetcode.com/problems/the-skyline-problem/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/05/hard-218-skyline-problem/) |
| 699 | Falling Squares | [Link](https://leetcode.com/problems/falling-squares/) | - |
| 715 | Range Module | [Link](https://leetcode.com/problems/range-module/) | - |
| 732 | My Calendar III | [Link](https://leetcode.com/problems/my-calendar-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/18/hard-732-my-calendar-iii/) |
| 850 | Rectangle Area II | [Link](https://leetcode.com/problems/rectangle-area-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-16-hard-850-rectangle-area-ii/) |
| 1157 | Online Majority Element In Subarray | [Link](https://leetcode.com/problems/online-majority-element-in-subarray/) | - |
| 2407 | Longest Increasing Subsequence II | [Link](https://leetcode.com/problems/longest-increasing-subsequence-ii/) | - |

### References

- [LeetCode: A Recursive Approach to Segment Trees, Range Sum Queries, and Lazy Propagation](https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/) - Comprehensive guide to segment trees with examples

## Fenwick Tree (Binary Indexed Tree)

Fenwick Tree (also known as Binary Indexed Tree or BIT) is a data structure that provides efficient methods for calculating prefix sums and updating array elements. It's more space-efficient than Segment Tree but less flexible.

### Basic Fenwick Tree (1-Indexed)

```cpp
class FenwickTree {
public:
    FenwickTree(int size) : n(size), BIT(size + 1, 0) {}
    
    // Add delta to element at index i (0-indexed)
    void add(int i, int delta) {
        i++; // Convert to 1-indexed
        while (i <= n) {
            BIT[i] += delta;
            i += (i & -i); // Move to next node
        }
    }
    
    // Get prefix sum from [0, i] (0-indexed)
    int prefixSum(int i) {
        int sum = 0;
        i++; // Convert to 1-indexed
        while (i > 0) {
            sum += BIT[i];
            i -= (i & -i); // Move to parent
        }
        return sum;
    }
    
    // Get range sum from [l, r] (0-indexed)
    int rangeSum(int l, int r) {
        return prefixSum(r) - (l > 0 ? prefixSum(l - 1) : 0);
    }
    
private:
    int n;
    vector<int> BIT;
};
```

### Fenwick Tree for Range Sum Query

```cpp
class NumArray {
private:
    vector<int> BIT;
    vector<int> nums;
    int n;
    
    void add(int i, int delta) {
        i++;
        while (i <= n) {
            BIT[i] += delta;
            i += (i & -i);
        }
    }
    
    int prefixSum(int i) {
        int sum = 0;
        i++;
        while (i > 0) {
            sum += BIT[i];
            i -= (i & -i);
        }
        return sum;
    }
    
public:
    NumArray(vector<int>& nums) : nums(nums) {
        n = nums.size();
        BIT.assign(n + 1, 0);
        for (int i = 0; i < n; i++) {
            add(i, nums[i]);
        }
    }
    
    void update(int index, int val) {
        int delta = val - nums[index];
        nums[index] = val;
        add(index, delta);
    }
    
    int sumRange(int left, int right) {
        return prefixSum(right) - (left > 0 ? prefixSum(left - 1) : 0);
    }
};
```

### 2D Fenwick Tree

```cpp
class FenwickTree2D {
public:
    FenwickTree2D(int rows, int cols) 
        : m(rows), n(cols), BIT(rows + 1, vector<int>(cols + 1, 0)) {}
    
    void add(int row, int col, int delta) {
        row++; col++;
        for (int i = row; i <= m; i += (i & -i)) {
            for (int j = col; j <= n; j += (j & -j)) {
                BIT[i][j] += delta;
            }
        }
    }
    
    int prefixSum(int row, int col) {
        int sum = 0;
        row++; col++;
        for (int i = row; i > 0; i -= (i & -i)) {
            for (int j = col; j > 0; j -= (j & -j)) {
                sum += BIT[i][j];
            }
        }
        return sum;
    }
    
    int rangeSum(int r1, int c1, int r2, int c2) {
        return prefixSum(r2, c2) 
             - prefixSum(r1 - 1, c2) 
             - prefixSum(r2, c1 - 1) 
             + prefixSum(r1 - 1, c1 - 1);
    }
    
private:
    int m, n;
    vector<vector<int>> BIT;
};
```

### Key Concepts

1. **1-Indexed Array**: BIT uses 1-indexed array internally (index 0 is unused)
2. **Lowest Set Bit**: `i & -i` extracts the lowest set bit
3. **Update**: Add delta to node and all ancestors: `i += (i & -i)`
4. **Query**: Sum from node to root: `i -= (i & -i)`
5. **Space Complexity**: O(n) - More efficient than Segment Tree's O(4n)
6. **Time Complexity**: O(log n) for both update and query

### How It Works

- **Tree Structure**: Each node stores sum of a range ending at that index
- **Update Path**: When updating index `i`, update all nodes that include `i`
- **Query Path**: When querying prefix sum up to `i`, sum all nodes on path to root
- **Range Query**: `rangeSum(l, r) = prefixSum(r) - prefixSum(l-1)`

### When to Use

- **Prefix Sum Queries**: Efficient prefix sum calculations
- **Point Updates**: Single element updates
- **Space Constraint**: When O(n) space is preferred over O(4n)
- **Range Sum**: When only range sum is needed (not min/max)
- **Not Suitable For**: Range updates, min/max queries, complex range operations

### Comparison: Segment Tree vs Fenwick Tree

| Aspect | Segment Tree | Fenwick Tree |
|--------|-------------|--------------|
| **Space** | O(4n) | O(n) |
| **Build Time** | O(n) | O(n log n) |
| **Update** | O(log n) | O(log n) |
| **Range Query** | O(log n) | O(log n) |
| **Range Update** | O(log n) with lazy | Not directly supported |
| **Min/Max Query** | Supported | Not directly supported |
| **Code Complexity** | More verbose | Simpler |
| **Flexibility** | High | Limited to prefix/range sum |

### Example Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-307-range-sum-query-mutable/) |
| 308 | Range Sum Query 2D - Mutable | [Link](https://leetcode.com/problems/range-sum-query-2d-mutable/) | - |
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/17/hard-315-count-of-smaller-numbers-after-self/) |
| 327 | Count of Range Sum | [Link](https://leetcode.com/problems/count-of-range-sum/) | - |
| 493 | Reverse Pairs | [Link](https://leetcode.com/problems/reverse-pairs/) | - |
| 1649 | Create Sorted Array through Instructions | [Link](https://leetcode.com/problems/create-sorted-array-through-instructions/) | - |

### References

- [TopCoder: Binary Indexed Trees](https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees) - Comprehensive tutorial on Fenwick Trees
- [GeeksforGeeks: Binary Indexed Tree](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/) - Implementation and examples

## HLD (Heavy-Light Decomposition) skeleton

```cpp
const int N = 200000; vector<int> gH[N]; int szH[N], parH[N], depH[N], heavyH[N], headH[N], inH[N], curT=0;
int dfs1(int u,int p){ parH[u]=p; depH[u]=(p==-1?0:depH[p]+1); szH[u]=1; heavyH[u]=-1; int best=0; for(int v:gH[u]) if(v!=p){ int s=dfs1(v,u); szH[u]+=s; if(s>best){best=s; heavyH[u]=v;} } return szH[u]; }
void dfs2(int u,int h){ headH[u]=h; inH[u]=curT++; if(heavyH[u]!=-1){ dfs2(heavyH[u],h); for(int v:gH[u]) if(v!=parH[u] && v!=heavyH[u]) dfs2(v,v);} }
```

> Note: HLD is rarely required on LeetCode.
