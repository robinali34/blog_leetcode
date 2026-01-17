---
layout: post
title: "315. Count of Smaller Numbers After Self"
date: 2026-01-15 00:00:00 -0700
categories: [leetcode, hard, array, binary-search, divide-and-conquer, binary-indexed-tree, segment-tree, merge-sort]
permalink: /2026/01/15/hard-315-count-of-smaller-numbers-after-self/
tags: [leetcode, hard, array, fenwick-tree, binary-indexed-tree, coordinate-compression, inversion-count]
---

# 315. Count of Smaller Numbers After Self

## Problem Statement

You are given an integer array `nums` and you have to return a new array `counts`. The array `counts` has the property where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

## Examples

**Example 1:**
```
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller elements.
```

**Example 2:**
```
Input: nums = [-1]
Output: [0]
```

**Example 3:**
```
Input: nums = [-1,-1]
Output: [0,0]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Solution Approach

This problem requires counting inversions (smaller elements to the right). We need an efficient data structure to track counts as we process elements from right to left.

### Key Insights:

1. **Right-to-Left Processing**: Process from right to left so we can query counts of already-seen elements
2. **Coordinate Compression**: Map values to indices [1, k] for Fenwick Tree (handles negative numbers)
3. **Fenwick Tree**: Efficiently track and query counts of smaller elements
4. **Query Before Update**: Query count of elements < current, then update tree

### Algorithm:

1. **Coordinate Compression**: Map distinct values to [1, k]
2. **Process Right to Left**: For each element from right to left
3. **Query**: Count how many elements < current have been seen
4. **Update**: Mark current element as seen in Fenwick Tree

## Solution

### **Solution: Fenwick Tree (Binary Indexed Tree) with Coordinate Compression**

```cpp
class Fenwick {
private:
    int n;
    vector<int> bit;
    int lowbit(int x) { return x & -x; }
public:
    Fenwick(int _n): n(_n), bit(n + 1, 0) {}
    
    // Add delta at position x (1-indexed)
    void update(int x, int delta) {
        for (; x <= n; x += lowbit(x)) {
            bit[x] += delta;
        }
    }
    
    // Sum from 1..x (1-indexed)
    int query(int x) {
        int s = 0;
        for (; x > 0; x -= lowbit(x)) {
            s += bit[x];
        }
        return s;
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int sz = nums.size();
        vector<int> res(sz, 0);
        
        // Coordinate compression: map distinct values to [1, k]
        vector<int> sorted(nums.begin(), nums.end());
        sort(sorted.begin(), sorted.end());
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());

        Fenwick fw(sorted.size());
        
        // Process from right to left
        for (int i = sz - 1; i >= 0; --i) {
            // Find compressed index for nums[i]
            int x = lower_bound(sorted.begin(), sorted.end(), nums[i]) - sorted.begin() + 1;
            // Query how many numbers < nums[i] have been seen
            res[i] = fw.query(x - 1);
            // Mark nums[i] as seen
            fw.update(x, 1);
        }
        return res;
    }
};
```

### **Algorithm Explanation:**

#### **Fenwick Class:**

1. **Constructor**: Initialize BIT with size `n` (1-indexed array)
2. **lowbit()**: Extract lowest set bit using `x & -x`
3. **update(x, delta)**: Add `delta` to position `x` and all ancestors
4. **query(x)**: Get prefix sum from 1 to `x`

#### **Solution Class:**

1. **Coordinate Compression (Lines 20-23)**:
   - Create sorted, unique array of all values
   - Maps original values to compressed indices [1, k]
   - Handles negative numbers and large ranges

2. **Right-to-Left Processing (Lines 27-33)**:
   - Process from `sz-1` down to `0`
   - For each element:
     - Find compressed index `x` using binary search
     - Query count of elements < current: `fw.query(x - 1)`
     - Update tree: mark current element as seen

### **How It Works:**

- **Coordinate Compression**: `[5, 2, 6, 1]` → `[1, 2, 5, 6]` → indices `[1, 2, 3, 4]`
- **Right-to-Left**: Ensures we only count elements to the right
- **Query Before Update**: Query counts elements already processed (to the right)
- **Update**: Marks current element for future queries

### **Example Walkthrough:**

**Input:** `nums = [5, 2, 6, 1]`

```
Step 1: Coordinate Compression
  sorted = [1, 2, 5, 6]
  Mapping: 1→1, 2→2, 5→3, 6→4

Step 2: Process from right to left
  i=3: nums[3] = 1, x = 1
    query(0) = 0 → res[3] = 0
    update(1, 1) → BIT[1] = 1
    
  i=2: nums[2] = 6, x = 4
    query(3) = BIT[3] + BIT[2] = 0 + 1 = 1 → res[2] = 1
    update(4, 1) → BIT[4] = 1
    
  i=1: nums[1] = 2, x = 2
    query(1) = BIT[1] = 1 → res[1] = 1
    update(2, 1) → BIT[2] = 2
    
  i=0: nums[0] = 5, x = 3
    query(2) = BIT[2] = 2 → res[0] = 2
    update(3, 1) → BIT[3] = 1

Result: [2, 1, 1, 0] ✓
```

### **Complexity Analysis:**

- **Time Complexity:** O(n log n)
  - Coordinate compression: O(n log n) for sorting
  - Binary search for each element: O(n log n)
  - Fenwick Tree operations: O(n log n) for n updates + n queries
  - Overall: O(n log n)

- **Space Complexity:** O(n)
  - Result array: O(n)
  - Sorted array: O(n)
  - Fenwick Tree: O(n)
  - Overall: O(n)

## Key Insights

1. **Coordinate Compression**: Essential for handling negative numbers and large ranges
2. **Right-to-Left Processing**: Ensures we only count elements to the right
3. **Fenwick Tree Efficiency**: O(log n) per operation, better than naive O(n)
4. **Query Before Update**: Query counts already-seen elements, then mark current
5. **Binary Search**: Use `lower_bound` for coordinate compression lookup

## Edge Cases

1. **Single element**: `nums = [5]` → return `[0]`
2. **All same**: `nums = [1, 1, 1]` → return `[0, 0, 0]`
3. **Negative numbers**: `nums = [-1, -2]` → coordinate compression handles it
4. **Descending order**: `nums = [5, 4, 3, 2, 1]` → all counts are 0
5. **Ascending order**: `nums = [1, 2, 3, 4, 5]` → counts increase

## Common Mistakes

1. **Left-to-right processing**: Would count elements to the left instead
2. **Forgetting coordinate compression**: BIT requires positive indices
3. **Wrong query index**: Using `query(x)` instead of `query(x-1)` for strictly smaller
4. **Update before query**: Should query first, then update
5. **Not handling duplicates**: Coordinate compression must preserve uniqueness

## Alternative Approaches

### **Approach 2: Merge Sort (Divide and Conquer)**

Count inversions during merge sort:

```cpp
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);
        vector<pair<int, int>> indexed;
        for (int i = 0; i < n; i++) {
            indexed.push_back({nums[i], i});
        }
        mergeSort(indexed, 0, n - 1, res);
        return res;
    }
    
private:
    void mergeSort(vector<pair<int, int>>& arr, int l, int r, vector<int>& res) {
        if (l >= r) return;
        int mid = l + (r - l) / 2;
        mergeSort(arr, l, mid, res);
        mergeSort(arr, mid + 1, r, res);
        merge(arr, l, mid, r, res);
    }
    
    void merge(vector<pair<int, int>>& arr, int l, int mid, int r, vector<int>& res) {
        vector<pair<int, int>> temp;
        int i = l, j = mid + 1;
        int rightCount = 0;
        
        while (i <= mid && j <= r) {
            if (arr[i].first > arr[j].first) {
                rightCount++;
                temp.push_back(arr[j++]);
            } else {
                res[arr[i].second] += rightCount;
                temp.push_back(arr[i++]);
            }
        }
        
        while (i <= mid) {
            res[arr[i].second] += rightCount;
            temp.push_back(arr[i++]);
        }
        
        while (j <= r) {
            temp.push_back(arr[j++]);
        }
        
        for (int k = 0; k < temp.size(); k++) {
            arr[l + k] = temp[k];
        }
    }
};
```

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

### **Approach 3: Segment Tree**

Similar to Fenwick Tree but with explicit segment tree structure.

**Comparison:**

| Approach | Time | Space | Code Complexity |
|----------|------|-------|-----------------|
| **Fenwick Tree** | O(n log n) | O(n) | Simple |
| **Merge Sort** | O(n log n) | O(n) | Moderate |
| **Segment Tree** | O(n log n) | O(4n) | More verbose |
| **Naive** | O(n²) | O(1) | Simple but TLE |

## Related Problems

- [LC 327: Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) - Similar inversion counting
- [LC 493: Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) - Count inversions with condition
- [LC 1649: Create Sorted Array through Instructions](https://leetcode.com/problems/create-sorted-array-through-instructions/) - Fenwick Tree for cost calculation
- [LC 307: Range Sum Query - Mutable](https://robinali34.github.io/blog_leetcode/2026/01/15/medium-307-range-sum-query-mutable/) - Fenwick Tree basics

---

*This problem demonstrates the **Fenwick Tree (Binary Indexed Tree)** pattern for efficient inversion counting. The key insight is using coordinate compression to map values to indices and processing from right to left to count smaller elements efficiently.*

