---
layout: post
title: "307. Range Sum Query - Mutable"
date: 2026-01-16 00:00:00 -0700
categories: [leetcode, medium, array, segment-tree, binary-indexed-tree]
permalink: /2026/01/16/medium-307-range-sum-query-mutable/
tags: [leetcode, medium, array, segment-tree, binary-indexed-tree, data-structure]
---

# 307. Range Sum Query - Mutable

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Range inclusivity**: Are both `left` and `right` indices inclusive in the range? (Assumption: Yes - range `[left, right]` is inclusive on both ends)

2. **Update operation**: What does update do - replace value or add to existing? (Assumption: Replace the value at index with new value - `nums[index] = val`)

3. **Index bounds**: Are indices guaranteed to be valid? (Assumption: Yes - constraints ensure `0 <= index < nums.length`)

4. **Operation frequency**: What's the ratio of updates vs queries? (Assumption: Both operations are frequent, so we need O(log n) for both)

5. **Data structure choice**: Can we use a simple array with O(n) queries? (Assumption: No - with many queries, we need efficient range queries, so Segment Tree or Fenwick Tree is needed)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Store the array as-is. For `update`, simply modify `nums[index] = val` in O(1) time. For `sumRange`, iterate through the range `[left, right]` and sum all elements, which takes O(n) time. This approach is simple but inefficient for queries, especially with many query operations.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use prefix sums: precompute a prefix sum array where `prefix[i]` represents the sum of elements from index 0 to i. This allows O(1) range queries using `prefix[right] - prefix[left-1]`. However, each update requires recomputing all prefix sums from the updated index to the end, which takes O(n) time. This is better for query-heavy scenarios but still slow for updates.

**Step 3: Optimized Solution (8 minutes)**

Use Fenwick Tree (Binary Indexed Tree) or Segment Tree: both support O(log n) updates and O(log n) range queries. Fenwick Tree is simpler to implement and uses less space. The key operations are: `update(index, val)` updates the tree in O(log n), and `sumRange(left, right)` computes range sum in O(log n) by querying prefix sums. This achieves O(log n) for both operations, which is optimal for this problem structure. The key insight is that we need a data structure that supports efficient point updates and range queries, which Fenwick Tree or Segment Tree provides.

## Solution Approach

This is a classic **Segment Tree** problem. We need to support:
- **Point Updates**: Update a single element
- **Range Queries**: Query sum over a range

### Key Insights:

1. **Naive Approach Fails**: O(1) update but O(n) query → TLE for many queries
2. **Segment Tree**: O(log n) for both update and query
3. **Binary Indexed Tree (Fenwick Tree)**: Alternative with O(log n) for both operations
4. **Array-Based Tree**: Use 0-indexed or 1-indexed array representation

### Algorithm:

1. **Build Segment Tree**: Recursively build tree storing range sums
2. **Update**: Update leaf node and propagate changes to parent nodes
3. **Query**: Recursively query overlapping ranges and combine results

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

## Key Insights

1. **0-Indexed vs 1-Indexed**: This solution uses 0-indexed (left child = `2*node+1`). 1-indexed uses `2*node` and `2*node+1`.
2. **Array Size**: Allocate `4 * n` to handle worst-case tree structure
3. **Long Long**: Use `long long` to prevent integer overflow for large sums
4. **Recursive vs Iterative**: Recursive is cleaner; iterative can avoid stack overflow
5. **Range Query Logic**: Three cases: no overlap, complete overlap, partial overlap

## Edge Cases

1. **Single element**: `nums = [5]` → tree stores single value
2. **Negative numbers**: `nums = [-1, -2, -3]` → sum works correctly
3. **Large array**: Up to 30,000 elements → segment tree handles efficiently
4. **Many queries**: Up to 30,000 queries → O(log n) per query is essential
5. **Update same index multiple times**: Each update is independent

## Common Mistakes

1. **Wrong array size**: Using `2 * n` instead of `4 * n` → index out of bounds
2. **Index calculation errors**: Wrong child indices (off-by-one)
3. **Not updating parent**: Forgetting to recalculate parent after update
4. **Query boundary errors**: Incorrect overlap checking logic
5. **Integer overflow**: Not using `long long` for large sums

## Alternative Approaches

### **Approach 2: Binary Indexed Tree (Fenwick Tree)**

Fenwick Tree is a more space-efficient alternative to Segment Tree. It uses O(n) space instead of O(4n) and has simpler code.

```cpp
class NumArray {
public:
    NumArray(vector<int>& nums) {
        n = nums.size();
        tree.assign(n + 1, 0);
        arr = nums;
        for(int i = 0; i < n; i++) {
            add(i + 1, nums[i]);
        }
    }
    
    void update(int index, int val) {
        int diff = val - arr[index];
        arr[index] = val;
        add(index + 1, diff);
    }
    
    int sumRange(int left, int right) {
        return prefixSum(right + 1) - prefixSum(left);
    }

private:
    vector<int> tree;
    vector<int> arr;
    int n;

    int lowbit(int x) {
        return x & (-x);
    }

    void add(int index, int val) {
        while(index <= n) {
            tree[index] += val;
            index += lowbit(index);
        }
    }

    // Prefix sum [1 .. index]
    int prefixSum(int index) {
        int sum = 0;
        while(index > 0) {
            sum += tree[index];
            index -= lowbit(index);
        }
        return sum;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
```

### **Algorithm Explanation:**

#### **Fenwick Tree Structure:**

1. **1-Indexed Array**: Fenwick Tree uses 1-indexed array internally (index 0 is unused)
2. **Lowest Set Bit (`lowbit`)**: `x & (-x)` extracts the lowest set bit
   - Example: `lowbit(6) = 6 & -6 = 2` (binary: `110 & 010 = 010`)
   - Used to traverse the tree structure
3. **Update Path**: `index += lowbit(index)` moves to next node that includes current index
4. **Query Path**: `index -= lowbit(index)` moves to parent node

#### **Key Methods:**

1. **lowbit(x)**: 
   - Helper function to extract the lowest set bit
   - Used for tree traversal in both `add` and `prefixSum`

2. **add(index, val)**: 
   - Add `val` to position `index` (1-indexed) and all ancestors
   - Traverse upward: `index += lowbit(index)`
   - Updates all nodes that include index `index` in their range
   - Stops when `index > n`

3. **prefixSum(index)**:
   - Get prefix sum from index 1 to `index` (both 1-indexed)
   - Traverse downward: `index -= lowbit(index)`
   - Sums all nodes on path from `index` to root
   - Stops when `index <= 0`

4. **sumRange(left, right)**:
   - Range sum = `prefixSum(right + 1) - prefixSum(left)`
   - Converts 0-indexed range `[left, right]` to 1-indexed prefix sums
   - Uses inclusion-exclusion principle: sum from 1 to (right+1) minus sum from 1 to left

### **How It Works:**

For array `[1, 3, 5]`:

```
Tree Structure (1-indexed):
tree[1] = 1
tree[2] = 1 + 3 = 4
tree[3] = 5
tree[4] = 1 + 3 + 5 = 9 (not used for n=3)

Query prefixSum(3):
  index = 3, sum += tree[3] = 5
  index = 2 (3 - lowbit(3) = 3 - 1 = 2), sum += tree[2] = 4, total = 9
  index = 0 (2 - lowbit(2) = 2 - 2 = 0), stop
  Result: 9 ✓
```

### **Example Walkthrough:**

**Input:** `nums = [1, 3, 5]`

```
Step 1: Build Fenwick Tree
  Constructor: arr = [1, 3, 5], n = 3
  add(1, 1): tree[1] = 1
  add(2, 3): tree[1] = 1, tree[2] = 4
  add(3, 5): tree[3] = 5
  
Step 2: Query sumRange(0, 2)
  prefixSum(3) = tree[3] + tree[2] = 5 + 4 = 9
  prefixSum(0) = 0
  Result: 9 - 0 = 9 ✓
  
Step 3: Update index 1 to 2
  diff = 2 - 3 = -1
  arr[1] = 2
  add(2, -1):
    tree[2] = 4 - 1 = 3
    tree[4] = ... (if n >= 4, but n=3, so stop)
    
Step 4: Query sumRange(0, 2)
  prefixSum(3) = tree[3] + tree[2] = 5 + 3 = 8
  prefixSum(0) = 0
  Result: 8 - 0 = 8 ✓
```

### **Complexity Analysis:**

- **Time Complexity:**
  - **Build**: O(n log n) - Each `add` takes O(log n)
  - **Update**: O(log n) - Traverse tree height
  - **Query**: O(log n) - Traverse tree height
  - **Overall**: O(n log n) build + O(k log n) for k operations

- **Space Complexity:** O(n)
  - BIT array: `n + 1` (1-indexed)
  - Original array: `n`
  - Overall: O(n)

### **Comparison:**

| Aspect | Segment Tree | Fenwick Tree |
|--------|-------------|--------------|
| **Space** | O(4n) | O(n) |
| **Build Time** | O(n) | O(n log n) |
| **Update** | O(log n) | O(log n) |
| **Query** | O(log n) | O(log n) |
| **Range Update** | O(log n) with lazy | Not directly supported |
| **Min/Max Query** | Supported | Not directly supported |
| **Code Complexity** | More verbose | Simpler |
| **Flexibility** | High | Limited to prefix/range sum |

### **When to Use Fenwick Tree:**

- ✅ **Space Constraint**: When O(n) space is preferred
- ✅ **Simple Code**: When simpler implementation is desired
- ✅ **Prefix/Range Sum**: When only sum queries are needed
- ❌ **Range Updates**: Not suitable for range updates
- ❌ **Min/Max Queries**: Cannot query min/max efficiently

### **Approach 3: Naive (TLE for Large Inputs)**

```cpp
class NumArray {
private:
    vector<int> nums;
public:
    NumArray(vector<int>& nums) : nums(nums) {}
    
    void update(int index, int val) {
        nums[index] = val;
    }
    
    int sumRange(int left, int right) {
        int sum = 0;
        for (int i = left; i <= right; i++) {
            sum += nums[i];
        }
        return sum;
    }
};
```

**Time Complexity:** O(1) update, O(n) query → **TLE** for many queries  
**Space Complexity:** O(n)

## Related Problems

- [LC 303: Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) - Prefix sum (no updates)
- [LC 308: Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) - 2D segment tree
- [LC 850: Rectangle Area II](https://robinali34.github.io/blog_leetcode/posts/2025-12-16-hard-850-rectangle-area-ii/) - Segment tree with coordinate compression
- [LC 3477: Number of Unplaced Fruits](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-3477-number-of-unplaced-fruits/) - Segment tree for leftmost query
- [LC 699: Falling Squares](https://leetcode.com/problems/falling-squares/) - Segment tree for range max updates

---

*This problem demonstrates the **Segment Tree** pattern for range sum queries with point updates. The key insight is using a binary tree structure to achieve O(log n) time for both operations, making it efficient for frequent queries and updates.*

