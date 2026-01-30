---
layout: post
title: "315. Count of Smaller Numbers After Self"
date: 2026-01-17 00:00:00 -0700
categories: [leetcode, hard, array, binary-search, divide-and-conquer, binary-indexed-tree, segment-tree, merge-sort]
permalink: /2026/01/17/hard-315-count-of-smaller-numbers-after-self/
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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **"After self" definition**: What does "smaller numbers after self" mean? (Assumption: For each element at index i, count how many elements to the right (indices > i) have smaller values)

2. **Duplicate values**: How should we handle duplicate values? (Assumption: Count only strictly smaller values - if nums[j] == nums[i] and j > i, don't count it)

3. **Output format**: Should we return counts for each position? (Assumption: Yes - return array where result[i] = count of smaller numbers after nums[i])

4. **Array mutability**: Can the input array be modified? (Assumption: No - we need to preserve original array for counting)

5. **Time complexity**: What's the expected time complexity? (Assumption: O(n log n) is optimal - need efficient data structure like Fenwick Tree or BST)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

For each element nums[i], scan all elements after it (nums[i+1] to nums[n-1]) and count how many are smaller. This straightforward approach has O(n²) time complexity, which is too slow for arrays up to 10^5 elements.

**Step 2: Semi-Optimized Approach (10 minutes)**

Process from right to left, maintaining a sorted data structure (like a balanced BST or sorted list) of elements seen so far. For each element, insert it into the sorted structure and count how many elements are smaller. Using a balanced BST gives O(n log n) time, but implementing a balanced BST is complex. Alternatively, use a Fenwick Tree or Segment Tree for efficient range queries.

**Step 3: Optimized Solution (12 minutes)**

Use merge sort with counting: during the merge process, when merging two sorted halves, count inversions. When an element from the right half is smaller than an element from the left half, all remaining elements in the left half are larger, so we can count them. Alternatively, use Fenwick Tree (Binary Indexed Tree): process from right to left, for each element, query how many smaller elements have been inserted, then insert the current element. This achieves O(n log n) time with O(n) space, which is optimal. The key insight is that we need to count elements that appear after the current element and are smaller, which can be done efficiently using merge sort inversion counting or Fenwick Tree range queries.

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
class FrenwickTree{
public:
    FrenwickTree(int n): sums_(n + 1, 0){}

    void update(int i, int delta) {
        while(i < sums_.size()) {
            sums_[i] += delta;
            i += lowbit(i);
        }
    }

    int query(int i) {
        int sum = 0;
        while(i > 0) {
            sum += sums_[i];
            i -= lowbit(i);
        }
        return sum;
    }

private:
    vector<int> sums_;

    int lowbit(int x) {
        return x & (-x);
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        // Get rank order
        vector<int> sorted(nums);
        sort(sorted.begin(), sorted.end());
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
        unordered_map<int, int> ranks;
        int rank = 1;
        for(const int num: sorted) {
            ranks[num] = rank++;
        }
        vector<int> rtn;
        // Update pre-fix sum while iterate, add ranks by 1 when encouter
        FrenwickTree tree(ranks.size());
        for(int i = nums.size() - 1; i >= 0; i--) {
            rtn.push_back(tree.query(ranks[nums[i]] - 1));
            tree.update(ranks[nums[i]], 1);
        }
        reverse(rtn.begin(), rtn.end());
        return rtn;
    }
};
```

### **Algorithm Explanation:**

#### **FrenwickTree Class:**

1. **Constructor**: Initialize Fenwick Tree with size `n` (1-indexed array `sums_`)
2. **lowbit(x)**: Extract lowest set bit using `x & (-x)`
3. **update(i, delta)**: Add `delta` to position `i` (1-indexed) and all ancestors
   - Traverse upward: `i += lowbit(i)`
   - Stops when `i >= sums_.size()`
4. **query(i)**: Get prefix sum from 1 to `i` (1-indexed)
   - Traverse downward: `i -= lowbit(i)`
   - Stops when `i <= 0`

#### **Solution Class:**

1. **Coordinate Compression**:
   - Create sorted, unique array of all values
   - Build `unordered_map` mapping each value to its rank [1, k]
   - Handles negative numbers and large ranges efficiently
   - Example: `[5, 2, 6, 1]` → sorted `[1, 2, 5, 6]` → ranks: `{1:1, 2:2, 5:3, 6:4}`

2. **Right-to-Left Processing**:
   - Process from `nums.size()-1` down to `0`
   - For each element:
     - Get rank: `ranks[nums[i]]`
     - Query count of elements < current: `tree.query(ranks[nums[i]] - 1)`
     - Push result to `rtn` vector
     - Update tree: mark current element as seen with `tree.update(ranks[nums[i]], 1)`
   - Reverse result array to get correct order

### **How It Works:**

- **Coordinate Compression**: `[5, 2, 6, 1]` → sorted `[1, 2, 5, 6]` → ranks `{1:1, 2:2, 5:3, 6:4}`
- **Right-to-Left**: Ensures we only count elements to the right
- **Query Before Update**: Query counts elements already processed (to the right)
- **Update**: Marks current element for future queries
- **Reverse Result**: Results are collected in reverse order, then reversed at the end

### **Example Walkthrough:**

**Input:** `nums = [5, 2, 6, 1]`

```
Step 1: Coordinate Compression
  sorted = [1, 2, 5, 6]
  ranks = {1:1, 2:2, 5:3, 6:4}

Step 2: Process from right to left
  i=3: nums[3] = 1, rank = 1
    query(0) = 0 → rtn.push_back(0)
    update(1, 1) → sums_[1] = 1
    rtn = [0]
    
  i=2: nums[2] = 6, rank = 4
    query(3) = sums_[3] + sums_[2] = 0 + 1 = 1 → rtn.push_back(1)
    update(4, 1) → sums_[4] = 1
    rtn = [0, 1]
    
  i=1: nums[1] = 2, rank = 2
    query(1) = sums_[1] = 1 → rtn.push_back(1)
    update(2, 1) → sums_[2] = 2
    rtn = [0, 1, 1]
    
  i=0: nums[0] = 5, rank = 3
    query(2) = sums_[2] = 2 → rtn.push_back(2)
    update(3, 1) → sums_[3] = 1
    rtn = [0, 1, 1, 2]

Step 3: Reverse result
  reverse(rtn) → [2, 1, 1, 0] ✓
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
   - Use `unordered_map` for O(1) rank lookup after sorting
   - Maps distinct values to consecutive ranks [1, k]
2. **Right-to-Left Processing**: Ensures we only count elements to the right
3. **Fenwick Tree Efficiency**: O(log n) per operation, better than naive O(n)
4. **Query Before Update**: Query counts already-seen elements, then mark current
5. **Result Collection**: Use `push_back` and `reverse` for cleaner code when processing backwards
6. **Rank Mapping**: `unordered_map` provides O(1) lookup vs O(log n) binary search

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

Count inversions during merge sort by tracking how many elements from the right subarray are smaller than each element in the left subarray.

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
        int rightCount = 0; // Count of elements from right subarray already merged
        
        while (i <= mid && j <= r) {
            if (arr[i].first > arr[j].first) {
                // Right element is smaller, will be placed before left elements
                rightCount++;
                temp.push_back(arr[j++]);
            } else {
                // Left element is smaller/equal, add count of right elements already merged
                res[arr[i].second] += rightCount;
                temp.push_back(arr[i++]);
            }
        }
        
        // Remaining left elements: all right elements were smaller
        while (i <= mid) {
            res[arr[i].second] += rightCount;
            temp.push_back(arr[i++]);
        }
        
        // Remaining right elements: no left elements to count
        while (j <= r) {
            temp.push_back(arr[j++]);
        }
        
        // Copy back to original array
        for (int k = 0; k < temp.size(); k++) {
            arr[l + k] = temp[k];
        }
    }
};
```

**Algorithm Explanation:**
- **Divide**: Split array into halves recursively
- **Conquer**: Merge sorted halves while counting inversions
- **Key Insight**: When merging, if a right element is smaller than a left element, it contributes to the count for all remaining left elements

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

### **Approach 3: Segment Tree with Coordinate Compression**

Similar to Fenwick Tree but using explicit segment tree structure.

```cpp
class SegmentTree {
private:
    int n;
    vector<int> tree;
    
    void update(int node, int l, int r, int idx) {
        if (l == r) {
            tree[node]++;
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) {
            update(2 * node + 1, l, mid, idx);
        } else {
            update(2 * node + 2, mid + 1, r, idx);
        }
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }
    
    int query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        return query(2 * node + 1, l, mid, ql, qr) + 
               query(2 * node + 2, mid + 1, r, ql, qr);
    }
    
public:
    SegmentTree(int size) : n(size), tree(4 * size, 0) {}
    
    void update(int idx) {
        update(0, 0, n - 1, idx);
    }
    
    int query(int l, int r) {
        return query(0, 0, n - 1, l, r);
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);
        
        // Coordinate compression
        vector<int> sorted(nums.begin(), nums.end());
        sort(sorted.begin(), sorted.end());
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
        
        SegmentTree st(sorted.size());
        
        // Process from right to left
        for (int i = n - 1; i >= 0; i--) {
            int rank = lower_bound(sorted.begin(), sorted.end(), nums[i]) - sorted.begin();
            // Query count of elements < nums[i]
            if (rank > 0) {
                res[i] = st.query(0, rank - 1);
            }
            // Mark nums[i] as seen
            st.update(rank);
        }
        
        return res;
    }
};
```

**Time Complexity:** O(n log n)  
**Space Complexity:** O(4n) = O(n)

### **Approach 4: Binary Search Tree (BST)**

Use an augmented BST that tracks the count of smaller elements.

```cpp
struct Node{
    int val, count, left_count;
    Node *left, *right;
    Node(int val): val(val), count(1), left_count(0), left{nullptr}, right{nullptr} {}
    ~Node() {delete left; delete right;};
    int less_or_equal() const{return count + left_count;};
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        if(nums.empty()) return {};
        reverse(nums.begin(), nums.end());
        unique_ptr<Node> root{new Node(nums[0])};
        vector<int> rtn{0};
        for(int i = 1; i < nums.size(); i++) {
            rtn.emplace_back(insert(root.get(), nums[i]));
        }
        reverse(rtn.begin(), rtn.end());
        return rtn;
    }

private:
    int insert(Node* root, int val) {
        if(root->val == val) {
            root->count++;
            return root->left_count;
        } else if(val < root->val) {
            root->left_count++;
            if(!root->left) {
                root->left = new Node(val);
                return 0;
            }
            return insert(root->left, val);
        } else {
            if(!root->right) {
                root->right = new Node(val);
                return root->less_or_equal();
            }
            return root->less_or_equal() + insert(root->right, val);
        }
    }
};
```

**Algorithm Explanation:**
- **BST Structure**: Each node stores:
  - `val`: The value stored in the node
  - `count`: Number of duplicates of this value
  - `left_count`: Number of nodes in left subtree
  - `left`, `right`: Pointers to children
- **Helper Method `less_or_equal()`**: Returns `count + left_count` (elements ≤ current node)
- **Insert Logic**: 
  - If value equals node: increment `count`, return `left_count`
  - If value < node: increment `left_count`, go left (create node if needed)
  - If value > node: return `less_or_equal()` + count from right subtree (create node if needed)
- **Processing Strategy**: 
  - Reverse input array first
  - Process left-to-right (which corresponds to right-to-left in original)
  - Reverse result to get correct order
- **Memory Management**: Uses `unique_ptr` for automatic cleanup and destructor for recursive deletion

**Time Complexity:** 
- Average: O(n log n)
- Worst: O(n²) if tree becomes unbalanced

**Space Complexity:** O(n)

### **Approach 5: Binary Search with Sorted List**

Maintain a sorted list and use binary search to find insertion position.

```cpp
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);
        vector<int> sortedList;
        
        // Process from right to left
        for (int i = n - 1; i >= 0; i--) {
            // Find position where nums[i] should be inserted
            auto it = lower_bound(sortedList.begin(), sortedList.end(), nums[i]);
            // Count of elements smaller than nums[i]
            res[i] = it - sortedList.begin();
            // Insert nums[i] at correct position
            sortedList.insert(it, nums[i]);
        }
        
        return res;
    }
};
```

**Algorithm Explanation:**
- Maintain a sorted list of elements seen so far
- For each element, find its insertion position using binary search
- Count of smaller elements = insertion index
- Insert element to maintain sorted order

**Time Complexity:** O(n²) - `insert` operation is O(n)  
**Space Complexity:** O(n)

**When to Use:** Only for small inputs or when simplicity is preferred

### **Comparison of All Approaches**

| Approach | Time Complexity | Space Complexity | Code Complexity | Best For |
|----------|----------------|------------------|-----------------|----------|
| **Fenwick Tree** | O(n log n) | O(n) | Simple | General purpose, space-efficient |
| **Merge Sort** | O(n log n) | O(n) | Moderate | When you need stable sort |
| **Segment Tree** | O(n log n) | O(4n) | More verbose | When you need range queries later |
| **BST** | O(n log n) avg, O(n²) worst | O(n) | Moderate | When tree structure is preferred |
| **Binary Search + Insert** | O(n²) | O(n) | Simple | Small inputs only |
| **Naive** | O(n²) | O(1) | Very simple | Not recommended for large inputs |

## Related Problems

- [LC 327: Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) - Similar inversion counting
- [LC 493: Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) - Count inversions with condition
- [LC 1649: Create Sorted Array through Instructions](https://leetcode.com/problems/create-sorted-array-through-instructions/) - Fenwick Tree for cost calculation
- [LC 307: Range Sum Query - Mutable](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-307-range-sum-query-mutable/) - Fenwick Tree basics

---

*This problem demonstrates the **Fenwick Tree (Binary Indexed Tree)** pattern for efficient inversion counting. The key insight is using coordinate compression to map values to indices and processing from right to left to count smaller elements efficiently.*

