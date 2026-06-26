---
layout: post
title: "[Medium] 307. Range Sum Query - Mutable"
date: 2026-01-16 00:00:00 -0700
categories: [leetcode, medium, array, segment-tree, binary-indexed-tree]
permalink: /2026/01/16/medium-307-range-sum-query-mutable/
tags: [leetcode, medium, array, segment-tree, binary-indexed-tree, data-structure]
---
Given an integer array `nums`, handle multiple queries of the following types:

1. **Update** the value of an element in `nums`.
2. **Calculate the sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `void update(int index, int val)` Updates the value of `nums[index]` to be `val`.
- `int sumRange(int left, int right)` Returns the sum of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

## Examples

**Example 1:**
```
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `0 <= index < nums.length`
- `-100 <= val <= 100`
- `0 <= left <= right < nums.length`
- At most `3 * 10^4` calls will be made to `update` and `sumRange`.

## Thinking Process

1. **0-Indexed vs 1-Indexed**: This solution uses 0-indexed (left child = `2*node+1`). 1-indexed uses `2*node` and `2*node+1`.

- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Prefix sum** *(this problem)* | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| Hash map counting | O(n) | O(n) | Frequency, two-sum variants |

## Solution

### **Solution: Segment Tree (0-Indexed Array Representation)**

```cpp
class NumArray {
public:
    NumArray(vector<int>& nums){
        n = nums.size();
        tree.resize(4 * n);
        build(0, 0, n - 1, nums);
    }
    
    void update(int index, int val) {
        update(0, 0, n - 1, index, val);
    }
    
    int sumRange(int left, int right) {
        return (int)query(0, 0, n - 1, left, right);
    }
private:
    vector<long long> tree;
    int n;

    void build(int node, int l, int r, vector<int>& nums) {
        if(l == r) {
            tree[node] = nums[l];
            return;
        }

        int mid = l + (r - l) / 2;
        build(2 * node + 1, l, mid, nums);
        build(2 * node + 2, mid + 1, r, nums);
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }

    void update(int node, int l, int r, int idx, int val) {
        if(l == r){
            tree[node] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if(idx <= mid){
            update(2 * node + 1, l, mid, idx, val);
        } else {
            update(2 * node + 2, mid + 1, r, idx, val);
        }
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }

    long long query(int node, int l, int r, int ql, int qr) {
        if(qr < l || r < ql) return 0;
        if(ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        return query(2 * node + 1, l, mid, ql, qr) + query(2* node + 2, mid + 1, r, ql, qr);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** 1. **0-Indexed vs 1-Indexed**: This solution uses 0-indexed (left child = `2*node+1`). 1-indexed uses `2*node` and `2*node+1`.

**How the code works:**
1. **0-Indexed vs 1-Indexed**: This solution uses 0-indexed (left child = `2*node+1`). 1-indexed uses `2*node` and `2*node+1`.
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

### **Algorithm Explanation:**

#### **NumArray Class:**

1. **Constructor (Lines 3-7)**:
   - Initialize segment tree with size `4 * n`
   - Build tree from `nums` array starting at root node (index 0)

2. **build() (Lines 15-25)**:
   - Recursively build segment tree
   - **Base Case**: Leaf node (`l == r`) stores `nums[l]`
   - **Recursive Case**: 
     - Build left subtree: `2 * node + 1` for range `[l, mid]`
     - Build right subtree: `2 * node + 2` for range `[mid + 1, r]`
     - Parent node stores sum of children: `tree[node] = tree[left] + tree[right]`

3. **update() (Lines 5-6, 27-37)**:
   - Public method delegates to private recursive method
   - Update element at index `idx` to value `val`
   - **Base Case**: Leaf node (`l == r`) → update directly
   - **Recursive Case**: 
     - Navigate to appropriate child based on `idx <= mid`
     - Update child subtree
     - Recalculate parent: `tree[node] = tree[left] + tree[right]`

4. **query() (Lines 8-9, 39-45)**:
   - Public method delegates to private recursive method
   - Query sum over range `[ql, qr]`
   - **No Overlap**: `qr < l || r < ql` → return 0
   - **Complete Overlap**: `ql <= l && r <= qr` → return `tree[node]`
   - **Partial Overlap**: Query both children and sum results

### **Tree Structure (0-Indexed):**

For array `[1, 3, 5]`:

```
        [9]          ]  ← node 0
       /   \
    [4]     [5]      ← nodes 1, 2
   /   \   /   \
  [1] [3] [5] [0]    ← nodes 3, 4, 5, 6 (leaves)
   0   1   2   3     ← array indices
```

**Node Indexing:**
- Root: `node = 0`
- Left child: `2 * node + 1`
- Right child: `2 * node + 2`
- Parent: `(node - 1) / 2` (if node > 0)

### **Example Walkthrough:**

**Input:** `nums = [1, 3, 5]`

```
Step 1: Build Tree
  build(0, 0, 2, [1, 3, 5]):
    - Left: build(1, 0, 1, ...)
      - Left: build(3, 0, 0, ...) → tree[3] = 1
      - Right: build(4, 1, 1, ...) → tree[4] = 3
      - tree[1] = tree[3] + tree[4] = 1 + 3 = 4
    - Right: build(2, 2, 2, ...) → tree[5] = 5
    - tree[0] = tree[1] + tree[2] = 4 + 5 = 9

Step 2: Query [0, 2]
  query(0, 0, 2, 0, 2):
    - Complete overlap → return tree[0] = 9 ✓

Step 3: Update index 1 to 2
  update(0, 0, 2, 1, 2):
    - idx=1 <= mid=1 → go left
    - update(1, 0, 1, 1, 2):
      - idx=1 > mid=0 → go right
      - update(4, 1, 1, 1, 2):
        - Leaf → tree[4] = 2
      - tree[1] = tree[3] + tree[4] = 1 + 2 = 3
    - tree[0] = tree[1] + tree[2] = 3 + 5 = 8

Step 4: Query [0, 2]
  query(0, 0, 2, 0, 2):
    - Complete overlap → return tree[0] = 8 ✓
```

### **Complexity Analysis:**

- **Time Complexity:**
  - **Build**: O(n) - Visit each element once
  - **Update**: O(log n) - Traverse from root to leaf
  - **Query**: O(log n) - Traverse tree height
  - **Overall**: O(n) build + O(k log n) for k operations

- **Space Complexity:** O(4n) = O(n)
  - Segment tree array: `4 * n` (worst case)
  - Recursion stack: O(log n)
  - Overall: O(n)
## Common Mistakes

1. **Single element**: `nums = [5]` → tree stores single value
2. **Negative numbers**: `nums = [-1, -2, -3]` → sum works correctly
3. **Large array**: Up to 30,000 elements → segment tree handles efficiently
4. **Many queries**: Up to 30,000 queries → O(log n) per query is essential
5. **Update same index multiple times**: Each update is independent

1. **Wrong array size**: Using `2 * n` instead of `4 * n` → index out of bounds
2. **Index calculation errors**: Wrong child indices (off-by-one)
3. **Not updating parent**: Forgetting to recalculate parent after update
4. **Query boundary errors**: Incorrect overlap checking logic
5. **Integer overflow**: Not using `long long` for large sums

## Related Problems

- [LC 303: Range Sum Query - Immutable](https://www.leetcode.com/problems/range-sum-query-immutable/) - Prefix sum (no updates)
- [LC 308: Range Sum Query 2D - Mutable](https://www.leetcode.com/problems/range-sum-query-2d-mutable/) - 2D segment tree
- [LC 850: Rectangle Area II](https://robinali34.github.io/blog_leetcode/posts/2025-12-16-hard-850-rectangle-area-ii/) - Segment tree with coordinate compression
- [LC 3477: Number of Unplaced Fruits](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-3477-number-of-unplaced-fruits/) - Segment tree for leftmost query
- [LC 699: Falling Squares](https://www.leetcode.com/problems/falling-squares/) - Segment tree for range max updates

## Key Takeaways

1. **0-Indexed vs 1-Indexed**: This solution uses 0-indexed (left child = `2*node+1`). 1-indexed uses `2*node` and `2*node+1`.
2. **Array Size**: Allocate `4 * n` to handle worst-case tree structure
3. **Long Long**: Use `long long` to prevent integer overflow for large sums
4. **Recursive vs Iterative**: Recursive is cleaner; iterative can avoid stack overflow
5. **Range Query Logic**: Three cases: no overlap, complete overlap, partial overlap

## References

- [LC 307: Range Sum Query - Mutable on LeetCode](https://www.leetcode.com/problems/range-sum-query-mutable/)
- [LeetCode Discuss — LC 307: Range Sum Query - Mutable](https://www.leetcode.com/problems/range-sum-query-mutable/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/range-sum-query-mutable/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
