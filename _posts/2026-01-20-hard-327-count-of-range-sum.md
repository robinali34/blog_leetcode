---
layout: post
title: "327. Count of Range Sum"
date: 2026-01-20 00:00:00 -0700
categories: [leetcode, hard, array, divide-and-conquer]
permalink: /2026/01/20/hard-327-count-of-range-sum/
tags: [leetcode, hard, array, divide-and-conquer, merge-sort, segment-tree, prefix-sum]
---

# 327. Count of Range Sum

## Problem Statement

Given an integer array `nums` and two integers `lower` and `upper`, return *the number of range sums that lie in `[lower, upper]` inclusive*.

Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and `j` inclusive, where `i <= j`.

## Examples

**Example 1:**
```
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
```

**Example 2:**
```
Input: nums = [0], lower = 0, upper = 0
Output: 1
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `-10^5 <= lower <= upper <= 10^5`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Range inclusivity**: Is the range `[lower, upper]` inclusive on both ends? (Assumption: Yes - subarray sum should satisfy `lower <= sum <= upper`)

2. **Subarray definition**: Does a subarray need to be contiguous? (Assumption: Yes - subarray is contiguous by definition)

3. **Empty subarray**: Can an empty subarray be considered? (Assumption: Need to clarify - typically empty subarray has sum 0, but should confirm if it counts)

4. **Integer overflow**: Can prefix sums overflow? (Assumption: Yes - need to use `long long` for prefix sums to handle large numbers)

5. **Negative numbers**: Can the array contain negative numbers? (Assumption: Yes - this makes prefix sums non-monotonic, requiring advanced techniques like merge sort or segment tree)

## Interview Deduction Process (30 minutes)

### Step 1: Brute-Force Approach (8 minutes)
**Initial Thought**: "I need to count range sums. Let me check all possible subarrays."

**Naive Solution**: Check all possible subarrays, compute sum, count those in range [lower, upper].

**Complexity**: O(n²) time, O(1) space

**Issues**:
- O(n²) time - inefficient
- Repeats sum computation for overlapping subarrays
- Doesn't leverage prefix sum
- Can be optimized

### Step 2: Semi-Optimized Approach (10 minutes)
**Insight**: "I can use prefix sum to compute subarray sums efficiently, but need to count pairs."

**Improved Solution**: Build prefix sum array. For each j, count i < j where prefix[j] - prefix[i] is in [lower, upper]. This requires counting prefix[i] in range [prefix[j]-upper, prefix[j]-lower].

**Complexity**: O(n²) time with prefix sum, O(n) space

**Improvements**:
- Prefix sum enables O(1) subarray sum queries
- Still O(n²) for checking all pairs
- Better structure than brute-force
- Can optimize further

### Step 3: Optimized Solution (12 minutes)
**Final Optimization**: "I can use merge sort or segment tree to count pairs efficiently."

**Best Solution**: Use merge sort on prefix sums. During merge, count pairs where prefix[i] is in range [prefix[j]-upper, prefix[j]-lower]. Alternative: Segment Tree with coordinate compression.

**Complexity**: O(n log n) time, O(n) space

**Key Realizations**:
1. Prefix sum transformation is key insight
2. Merge sort enables efficient pair counting
3. O(n log n) time is optimal
4. Segment Tree is alternative approach

## Solution Approach

This problem requires counting the number of subarray sums that fall within a given range. The key insight is to use **prefix sums** and then count pairs of prefix sums that satisfy the condition.

### Key Insights:

1. **Prefix Sum**: `S(i, j) = prefix[j+1] - prefix[i]`
2. **Range Condition**: `lower <= prefix[j+1] - prefix[i] <= upper`
3. **Rearranged**: `prefix[j+1] - upper <= prefix[i] <= prefix[j+1] - lower`
4. **Problem Transformation**: Count pairs `(i, j)` where `i < j` and `prefix[i]` is in range `[prefix[j] - upper, prefix[j] - lower]`

## Solution 1: Divide and Conquer (Merge Sort)

```cpp
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);

        // prefix sum with 0 included
        for (int i = 0; i < n; i++)
            prefix[i + 1] = prefix[i] + nums[i];

        vector<long long> temp(n + 1);
        return divide(prefix, 0, n, lower, upper, temp);
    }

private:
    int divide(vector<long long>& prefix, int left, int right,
               int lower, int upper, vector<long long>& temp) {
        if (left >= right) return 0;

        int mid = (left + right) / 2;
        int count = 0;

        count += divide(prefix, left, mid, lower, upper, temp);
        count += divide(prefix, mid + 1, right, lower, upper, temp);

        count += countCross(prefix, left, mid, right, lower, upper);
        merge(prefix, left, mid, right, temp);

        return count;
    }

    int countCross(vector<long long>& prefix, int left, int mid, int right,
                   int lower, int upper) {
        int count = 0;
        int wl = left, wr = left;

        for (int i = mid + 1; i <= right; i++) {
            long long low = prefix[i] - upper;
            long long high = prefix[i] - lower;

            while (wl <= mid && prefix[wl] < low) wl++;
            while (wr <= mid && prefix[wr] <= high) wr++;

            count += wr - wl;
        }
        return count;
    }

    void merge(vector<long long>& prefix, int left, int mid, int right,
               vector<long long>& temp) {
        int i = left, j = mid + 1, k = left;

        while (i <= mid && j <= right)
            temp[k++] = (prefix[i] <= prefix[j]) ? prefix[i++] : prefix[j++];

        while (i <= mid) temp[k++] = prefix[i++];
        while (j <= right) temp[k++] = prefix[j++];

        for (int i = left; i <= right; i++)
            prefix[i] = temp[i];
    }
};
```

### Algorithm Explanation:

1. **Prefix Sum Array**: Build `prefix[i] = sum(nums[0..i-1])` with `prefix[0] = 0`

2. **Divide and Conquer**:
   - Divide prefix array into left and right halves
   - Recursively count valid pairs in left and right halves
   - Count cross pairs (one from left, one from right)
   - Merge the sorted halves

3. **Count Cross Pairs** (`countCross`):
   - For each `prefix[j]` in right half, find valid `prefix[i]` in left half
   - Condition: `prefix[j] - upper <= prefix[i] <= prefix[j] - lower`
   - Use two pointers `wl` and `wr` to maintain valid range
   - `wl`: first index where `prefix[wl] >= prefix[j] - upper`
   - `wr`: first index where `prefix[wr] > prefix[j] - lower`
   - Count: `wr - wl`

4. **Merge**: Standard merge sort merge operation

### Why This Works?

- **Sorted Property**: After merge, left and right halves are sorted
- **Two Pointers**: For each right element, find valid left elements using sliding window
- **Efficiency**: O(n log n) time complexity

### Complexity Analysis:

- **Time Complexity:** O(n log n)
  - Divide: O(log n) levels
  - Each level: O(n) for counting and merging
  - Total: O(n log n)

- **Space Complexity:** O(n)
  - Prefix array: O(n)
  - Temp array: O(n)
  - Recursion stack: O(log n)

## Solution 2: Segment Tree (Dynamic Node Creation)

```cpp
struct Node {
    long long start, end;
    int cnt;
    Node *left, *right;
    Node(long long start, long long end): start(start), end(end), cnt(0){
        left = right = nullptr;
    }
};

class Solution {
/*
Prefix sum pre
pre[j] - upper <= pre[i] <= pre[j] - lower
Fenwick Tree (Binary Indexed Tree)
Segment Tree with dynamic allocation - reduce allocations, no delete needed
*/
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        const int N = nums.size();
        vector<long long> presum(N + 1, 0);
        for(int i = 0; i < N; i++) {
            presum[i + 1] = presum[i] + nums[i];
        }
        long long mn = LLONG_MAX, mx = LLONG_MIN;
        for(auto x: presum) {
            mn = min({mn, x, x - upper});
            mx = max({mx, x, x - lower});
        }
        Node root(mn, mx);
        int rtn = 0;
        for(auto x: presum) {
            rtn += query(&root, x - upper, x - lower);
            add(&root, x);
        }
        return rtn;
    }

private:
    int query(Node* node, long long l, long long r) {
        if(!node) return 0;
        if(l > node->end || r < node->start) return 0;
        if(l <= node->start && node->end <= r) return node->cnt;
        return query(node->left, l, r) + query(node->right, l, r);
    }

    // node is not null
    // add pos [start, end]
    void add(Node* node, long long pos){
        node->cnt++;
        if(node->start == node->end) return;
        long long mid = (node->start + node->end) >> 1;
        if(pos <= mid) {
            if(!node->left) {
                node->left = new Node(node->start, mid);
            }
            add(node->left, pos);
        } else {
            if(!node->right) {
                node->right = new Node(mid+1, node->end);
            }
            add(node->right, pos);
        }
    }
};
```

### Algorithm Explanation:

1. **Prefix Sum Array**: Build prefix sums as in Solution 1

2. **Dynamic Segment Tree**:
   - Root covers range `[min_value, max_value]` of all possible prefix sums
   - Dynamically create nodes only when needed (lazy initialization)
   - Each node stores count of prefix sums in its range

3. **Query and Update**:
   - For each prefix sum `x`, query count of values in `[x - upper, x - lower]`
   - This counts how many previous prefix sums satisfy the condition
   - Then add current prefix sum to the tree

4. **Dynamic Node Creation**:
   - Only create child nodes when needed (when adding a value)
   - Reduces memory usage compared to full segment tree

### Why This Works?

- **Range Query**: Segment tree efficiently counts values in range
- **Online Processing**: Process prefix sums one by one
- **Memory Efficient**: Only create nodes for values that appear

### Complexity Analysis:

- **Time Complexity:** O(n log U)
  - n = number of elements
  - U = range size (max - min)
  - Each query/update: O(log U)

- **Space Complexity:** O(n log U)
  - Segment tree nodes: O(n log U) in worst case
  - Prefix array: O(n)

## Key Insights

1. **Prefix Sum Transformation**: Convert subarray sum problem to prefix sum difference problem
2. **Range Condition**: `lower <= prefix[j] - prefix[i] <= upper` becomes `prefix[j] - upper <= prefix[i] <= prefix[j] - lower`
3. **Two Approaches**:
   - **Divide & Conquer**: Sort prefix sums, count pairs using two pointers
   - **Segment Tree**: Maintain count of prefix sums, query range for each new prefix
4. **Dynamic Node Creation**: Reduces memory for sparse segment trees

## Edge Cases

1. **Single element**: `nums = [0]`, `lower = 0`, `upper = 0` → return `1`
2. **All negative**: `nums = [-2,-1]`, `lower = -3`, `upper = -1` → count valid ranges
3. **Large numbers**: Use `long long` to prevent overflow
4. **Empty ranges**: Handle cases where no valid ranges exist
5. **Overflow prevention**: Prefix sums can exceed `int` range

## Common Mistakes

1. **Integer overflow**: Not using `long long` for prefix sums
   ```cpp
   // WRONG:
   vector<int> prefix(n + 1, 0); // ❌ May overflow
   ```

2. **Off-by-one errors**: Incorrect prefix sum indexing
3. **Missing prefix[0]**: Forgetting to include empty prefix (sum = 0)
4. **Wrong range**: Confusing `prefix[j] - upper` and `prefix[j] - lower`
5. **Memory leaks**: Not managing segment tree nodes properly (though solution doesn't delete)

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Divide & Conquer** | O(n log n) | O(n) | Simple, stable | Requires sorting |
| **Segment Tree** | O(n log U) | O(n log U) | Online processing | More complex, memory overhead |

## Related Problems

- [LC 327: Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) - This problem
- [LC 315: Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) - Similar divide & conquer approach
- [LC 493: Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) - Count pairs with condition
- [LC 307: Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) - Segment tree for range sum
- [LC 303: Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) - Prefix sum basics

---

*This problem demonstrates **divide and conquer** and **segment tree** techniques for counting pairs satisfying a range condition. The key transformation is converting subarray sums to prefix sum differences, making it easier to count valid pairs efficiently.*

