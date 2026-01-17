---
layout: post
title: "3477. Number of Unplaced Fruits"
date: 2026-01-15 00:00:00 -0700
categories: [leetcode, medium, array, greedy, segment-tree]
permalink: /2026/01/15/medium-3477-number-of-unplaced-fruits/
tags: [leetcode, medium, array, greedy, segment-tree, data-structure]
---

# 3477. Number of Unplaced Fruits

## Problem Statement

You are given two integer arrays `fruits` and `baskets`.

- `fruits[i]` represents the quantity of the `i`-th type of fruit.
- `baskets[j]` represents the capacity of the `j`-th basket.

You process fruits from left to right. For each fruit type, you must place it in the **leftmost** available basket whose capacity is **greater than or equal to** the fruit's quantity.

- Each basket can hold **at most one** type of fruit.
- If no such basket exists for a fruit type, it remains **unplaced**.

Return *the number of fruit types that are **not placed** after trying to place all fruits*.

## Examples

**Example 1:**
```
Input: fruits = [4, 2, 5], baskets = [3, 5, 4]
Output: 1
Explanation:
- Fruit 4: Place in leftmost basket with capacity >= 4 → baskets[1] = 5 (placed)
- Fruit 2: Place in leftmost basket with capacity >= 2 → baskets[0] = 3 (placed)
- Fruit 5: Requires capacity >= 5, but remaining basket baskets[2] = 4 < 5 → unplaced
Result: 1 unplaced fruit
```

**Example 2:**
```
Input: fruits = [3, 2, 1], baskets = [1, 2, 3]
Output: 0
Explanation:
- Fruit 3: Place in baskets[2] = 3 (placed)
- Fruit 2: Place in baskets[1] = 2 (placed)
- Fruit 1: Place in baskets[0] = 1 (placed)
Result: 0 unplaced fruits
```

## Constraints

- `1 <= fruits.length <= 10^5`
- `1 <= baskets.length <= 10^5`
- `1 <= fruits[i] <= 10^9`
- `1 <= baskets[j] <= 10^9`

## Solution Approach

This is a **greedy matching** problem where we need to find the leftmost available basket for each fruit. The challenge is to do this efficiently for large inputs.

### Key Insights:

1. **Greedy Strategy**: Always use the leftmost available basket that can hold the fruit
2. **Leftmost Requirement**: Must maintain original index order (not just any basket)
3. **Capacity Constraint**: Basket capacity must be >= fruit quantity
4. **One-to-One Matching**: Each basket can only hold one fruit
5. **Efficient Query**: Need to find leftmost index with capacity >= value quickly

### Algorithm:

1. **Segment Tree**: Build segment tree storing maximum capacity in each range
2. **Query**: Find leftmost index with capacity >= fruit quantity
3. **Update**: Mark basket as used (set capacity to 0) after placing fruit
4. **Count Unplaced**: Track fruits that can't find a suitable basket

## Solution

### **Solution: Segment Tree for Leftmost Query**

```cpp
struct SegmentTree {
    int n;
    vector<int> tree;

    SegmentTree(vector<int>& baskets) {
        n = baskets.size();
        tree.resize(4*n);
        build(1, 0, n-1, baskets);
    }

    void build(int node, int l, int r, vector<int>& baskets) {
        if (l == r) {
            tree[node] = baskets[l];
        } else {
            int mid = (l + r) / 2;
            build(node*2, l, mid, baskets);
            build(node*2+1, mid+1, r, baskets);
            tree[node] = max(tree[node*2], tree[node*2+1]);
        }
    }

    // Find leftmost index >= l with value >= val
    int query(int node, int l, int r, int val) {
        if (tree[node] < val) return -1; // no basket in this range can hold fruit
        if (l == r) return l; // found
        int mid = (l + r) / 2;
        int left = query(node*2, l, mid, val);
        if (left != -1) return left;
        return query(node*2+1, mid+1, r, val);
    }

    void update(int node, int l, int r, int idx) {
        if (l == r) {
            tree[node] = 0; // mark basket used
        } else {
            int mid = (l + r) / 2;
            if (idx <= mid) update(node*2, l, mid, idx);
            else update(node*2+1, mid+1, r, idx);
            tree[node] = max(tree[node*2], tree[node*2+1]);
        }
    }
};

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = baskets.size();
        SegmentTree st(baskets);
        int unplaced = 0;

        for (int f : fruits) {
            int idx = st.query(1, 0, n-1, f);
            if (idx == -1) {
                unplaced++;
            } else {
                st.update(1, 0, n-1, idx); // mark basket used
            }
        }

        return unplaced;
    }
};
```

### **Algorithm Explanation:**

#### **SegmentTree Class:**

1. **Constructor (Lines 5-9)**:
   - Initialize segment tree with size `4 * n`
   - Build tree from baskets array

2. **build() (Lines 11-20)**:
   - Recursively build segment tree
   - Each node stores maximum capacity in its range
   - Leaf nodes store individual basket capacities

3. **query() (Lines 22-30)**:
   - Find leftmost index with capacity >= `val`
   - **Early Termination**: If `tree[node] < val`, no basket in range can hold fruit → return -1
   - **Left-First Search**: Check left child first to maintain leftmost property
   - **Base Case**: If leaf node and capacity >= val, return index

4. **update() (Lines 32-42)**:
   - Mark basket as used by setting capacity to 0
   - Update parent nodes to reflect new maximum

#### **Solution Class:**

1. **Main Function (Lines 45-58)**:
   - Build segment tree from baskets
   - For each fruit:
     - Query for leftmost basket with capacity >= fruit quantity
     - If found, update basket (mark as used)
     - If not found, increment unplaced count
   - Return number of unplaced fruits

### **How It Works:**

- **Segment Tree Structure**: Each node stores maximum capacity in its range
- **Leftmost Query**: By checking left child first, we ensure leftmost index is found
- **Efficient Updates**: After placing fruit, basket capacity becomes 0 (unavailable)
- **Greedy Matching**: Always uses leftmost available basket that fits

### **Example Walkthrough:**

**Input:** `fruits = [4, 2, 5], baskets = [3, 5, 4]`

```
Initial Segment Tree:
        [5] (max of [3,5,4])
       /   \
    [5]     [4]
   /   \   /   \
  [3] [5] [4] [0]
   0   1   2   3

Step 1: Process fruit = 4
  query(1, 0, 2, 4):
    - Check left [0,1]: max = 5 >= 4 → explore left
    - Check left [0,0]: max = 3 < 4 → skip
    - Check right [1,1]: max = 5 >= 4 → found at index 1
  Place fruit 4 in basket[1]
  Update: basket[1] = 0
  Tree: [4] (max of [3,0,4])
  
Step 2: Process fruit = 2
  query(1, 0, 2, 2):
    - Check left [0,1]: max = 3 >= 2 → explore left
    - Check left [0,0]: max = 3 >= 2 → found at index 0
  Place fruit 2 in basket[0]
  Update: basket[0] = 0
  Tree: [4] (max of [0,0,4])
  
Step 3: Process fruit = 5
  query(1, 0, 2, 5):
    - Check left [0,1]: max = 0 < 5 → skip
    - Check right [2,2]: max = 4 < 5 → no solution
  No basket found → unplaced++
  
Result: 1 unplaced fruit
```

### **Complexity Analysis:**

- **Time Complexity:** O(n log m)
  - Building segment tree: O(m)
  - For each fruit: O(log m) for query + O(log m) for update
  - Overall: O(m + n log m) ≈ O(n log m) where n = fruits.length, m = baskets.length

- **Space Complexity:** O(m)
  - Segment tree: O(4m) = O(m)
  - Other variables: O(1)
  - Overall: O(m)

## Key Insights

1. **Segment Tree for Range Max**: Efficiently find leftmost index with capacity >= value
2. **Left-First Traversal**: Check left child first to maintain leftmost property
3. **Greedy Matching**: Always use leftmost available basket
4. **Update Strategy**: Mark basket as used by setting capacity to 0
5. **Early Termination**: If max capacity in range < required, skip entire range

## Edge Cases

1. **All fruits placed**: `fruits = [1, 2], baskets = [2, 3]` → return `0`
2. **No fruits placed**: `fruits = [5, 6], baskets = [1, 2]` → return `2`
3. **Exact match**: `fruits = [3], baskets = [3]` → return `0`
4. **Single basket**: `fruits = [1, 2], baskets = [2]` → return `1`
5. **Large capacities**: Handle up to 10^9 values

## Common Mistakes

1. **Not maintaining leftmost order**: Using any basket instead of leftmost
2. **Wrong query logic**: Not checking left child first
3. **Incorrect update**: Not properly updating parent nodes after marking basket used
4. **Off-by-one errors**: Incorrect index calculations in segment tree
5. **Not handling duplicates**: Same basket capacity appearing multiple times

## Alternative Approaches

### **Approach 2: Greedy with Boolean Array (Brute Force)**

Simple approach for small inputs:

```cpp
class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = baskets.size();
        vector<bool> used(n, false);
        int unplaced = 0;
        
        for (int f : fruits) {
            bool placed = false;
            for (int j = 0; j < n; j++) {
                if (!used[j] && baskets[j] >= f) {
                    used[j] = true;
                    placed = true;
                    break;
                }
            }
            if (!placed) unplaced++;
        }
        
        return unplaced;
    }
};
```

**Time Complexity:** O(n × m) - Too slow for large inputs  
**Space Complexity:** O(m)

**When to Use:**
- Small inputs (n, m ≤ 1000)
- Simple implementation preferred
- Not suitable for constraints up to 10^5

### **Approach 3: Multiset/Balanced BST (Alternative)**

Use ordered set to maintain unused baskets, but maintaining leftmost property is tricky.

**Comparison:**

| Approach | Time | Space | Complexity | Notes |
|----------|------|-------|------------|-------|
| **Brute Force** | O(n × m) | O(m) | Low | Simple, only for small inputs |
| **Segment Tree** | O(n log m) | O(m) | Medium | Efficient, handles large inputs |
| **Multiset** | O(n log m) | O(m) | Medium | Harder to maintain leftmost property |

## Related Problems

- [LC 307: Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) - Segment tree for range queries
- [LC 850: Rectangle Area II](https://robinali34.github.io/blog_leetcode/posts/2025-12-16-hard-850-rectangle-area-ii/) - Segment tree with coordinate compression
- [LC 699: Falling Squares](https://leetcode.com/problems/falling-squares/) - Segment tree for range max updates
- [LC 715: Range Module](https://leetcode.com/problems/range-module/) - Segment tree for interval operations

---

*This problem demonstrates the **Segment Tree** pattern for efficient range queries with leftmost property. The key insight is using segment tree to find the leftmost index satisfying a capacity constraint, then updating it to mark as used.*

