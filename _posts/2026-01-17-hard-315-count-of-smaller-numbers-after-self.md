---
layout: post
title: "[Hard] 315. Count of Smaller Numbers After Self"
date: 2026-01-17 00:00:00 -0700
categories: [leetcode, hard, array, binary-search, divide-and-conquer, binary-indexed-tree, segment-tree, merge-sort]
permalink: /2026/01/17/hard-315-count-of-smaller-numbers-after-self/
tags: [leetcode, hard, array, fenwick-tree, binary-indexed-tree, coordinate-compression, inversion-count]
---
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

## Thinking Process

1. **Coordinate Compression**: Essential for handling negative numbers and large ranges
- Use `unordered_map` for O(1) rank lookup after sorting
- Maps distinct values to consecutive ranks [1, k]

- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 130" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary search: shrink [lo … hi]</text>

  <rect x="40" y="40" width="48" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="64" y="58" text-anchor="middle" font-size="12" fill="#3A3530">lo</text>
  <rect x="108" y="40" width="48" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="132" y="58" text-anchor="middle" font-size="12" fill="#3A3530">mid</text>
  <rect x="196" y="40" width="48" height="32" rx="4" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="220" y="58" text-anchor="middle" font-size="12" fill="#3A3530">hi</text>
  <rect x="60" y="90" width="160" height="28" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="140" y="108" text-anchor="middle" font-size="11" fill="#6B6560">discard half each step → O(log n)</text>
  <path d="M132 72v12M220 72v12" stroke="#9A9792" stroke-width="1.5" marker-end="url(#a)"/>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Prefix sum | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| **Hash map counting** *(this problem)* | O(n) | O(n) | Frequency, two-sum variants |

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

### Solution Explanation

**Approach:** Hash map counting (this problem)

**Key idea:** 1. **Coordinate Compression**: Essential for handling negative numbers and large ranges

**How the code works:**
1. **Coordinate Compression**: Essential for handling negative numbers and large ranges
- Use `unordered_map` for O(1) rank lookup after sorting
- Maps distinct values to consecutive ranks [1, k]
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

**Walkthrough** — input `nums = [5,2,6,1]`, expected output `[2,1,1,0]`:

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller elements.

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
## Common Mistakes

1. **Single element**: `nums = [5]` → return `[0]`
2. **All same**: `nums = [1, 1, 1]` → return `[0, 0, 0]`
3. **Negative numbers**: `nums = [-1, -2]` → coordinate compression handles it
4. **Descending order**: `nums = [5, 4, 3, 2, 1]` → all counts are 0
5. **Ascending order**: `nums = [1, 2, 3, 4, 5]` → counts increase

1. **Left-to-right processing**: Would count elements to the left instead
2. **Forgetting coordinate compression**: BIT requires positive indices
3. **Wrong query index**: Using `query(x)` instead of `query(x-1)` for strictly smaller
4. **Update before query**: Should query first, then update
5. **Not handling duplicates**: Coordinate compression must preserve uniqueness

## Related Problems

- [LC 327: Count of Range Sum](https://www.leetcode.com/problems/count-of-range-sum/) - Similar inversion counting
- [LC 493: Reverse Pairs](https://www.leetcode.com/problems/reverse-pairs/) - Count inversions with condition
- [LC 1649: Create Sorted Array through Instructions](https://www.leetcode.com/problems/create-sorted-array-through-instructions/) - Fenwick Tree for cost calculation
- [LC 307: Range Sum Query - Mutable](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-307-range-sum-query-mutable/) - Fenwick Tree basics

## Key Takeaways

1. **Coordinate Compression**: Essential for handling negative numbers and large ranges
   - Use `unordered_map` for O(1) rank lookup after sorting
   - Maps distinct values to consecutive ranks [1, k]
2. **Right-to-Left Processing**: Ensures we only count elements to the right
3. **Fenwick Tree Efficiency**: O(log n) per operation, better than naive O(n)
4. **Query Before Update**: Query counts already-seen elements, then mark current
5. **Result Collection**: Use `push_back` and `reverse` for cleaner code when processing backwards
6. **Rank Mapping**: `unordered_map` provides O(1) lookup vs O(log n) binary search

## References

- [LC 315: Count of Smaller Numbers After Self on LeetCode](https://www.leetcode.com/problems/count-of-smaller-numbers-after-self/)
- [LeetCode Discuss — LC 315: Count of Smaller Numbers After Self](https://www.leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/count-of-smaller-numbers-after-self/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
