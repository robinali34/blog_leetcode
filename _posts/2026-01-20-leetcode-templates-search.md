---
layout: post
title: "LeetCode Templates: Search"
date: 2026-01-20 00:00:00 -0700
categories: leetcode templates search binary-search
permalink: /posts/2026-01-20-leetcode-templates-search/
tags: [leetcode, templates, search, binary-search, divide-and-conquer]
---

{% raw %}
## Contents

- [Quick Links](#quick-links)
- [Basic Binary Search](#basic-binary-search)
- [Binary Search on Rotated Array](#binary-search-on-rotated-array)
- [Binary Search on Answer Space](#binary-search-on-answer-space)
- [Search in 2D Matrix](#search-in-2d-matrix)
- [Advanced Search Patterns](#advanced-search-patterns)
  - [Merge Sort on Prefix Sums](#merge-sort-on-prefix-sums)
  - [Divide and Conquer Search](#divide-and-conquer-search)
  - [Ternary Search](#ternary-search)
  - [Parallel Binary Search](#parallel-binary-search)
  - [Exponential Search](#exponential-search)
  - [Tree-Based Search (Segment Tree, BIT)](#tree-based-search-segment-tree-bit)

## Quick Links

- **[All Templates](/leetcode-templates/)** - Browse all LeetCode solution templates
- **[LeetCode Questions List](/leetcode-questions-list/)** - Complete list of solved problems

## Basic Binary Search

### Standard Binary Search Template

```cpp
// Find target in sorted array
int binarySearch(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1; // Not found
}
```

### Lower Bound (First Position)

```cpp
// Find first position where target can be inserted
int lowerBound(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}
```

### Upper Bound (Last Position)

```cpp
// Find last position where target can be inserted
int upperBound(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return left;
}
```

### Find Range of Target

```cpp
vector<int> searchRange(vector<int>& nums, int target) {
    int first = lowerBound(nums, target);
    
    if (first == nums.size() || nums[first] != target) {
        return {-1, -1};
    }
    
    int last = upperBound(nums, target) - 1;
    return {first, last};
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 704 | Binary Search | [Link](https://leetcode.com/problems/binary-search/) | - |
| 34 | Find First and Last Position | [Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | - |
| 35 | Search Insert Position | [Link](https://leetcode.com/problems/search-insert-position/) | - |
| 528 | Random Pick with Weight | [Link](https://leetcode.com/problems/random-pick-with-weight/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-528-random-pick-with-weight/) |
| 300 | Longest Increasing Subsequence | [Link](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-300-longest-increasing-subsequence/) |
| 673 | Number of Longest Increasing Subsequence | [Link](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/09/medium-673-number-of-longest-increasing-subsequence/) |

## Binary Search on Rotated Array

### Search in Rotated Sorted Array

```cpp
int search(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (nums[mid] == target) {
            return mid;
        }
        
        // Left half is sorted
        if (nums[mid] >= nums[left]) {
            if (target >= nums[left] && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        // Right half is sorted
        else {
            if (target > nums[mid] && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    
    return -1;
}
```

### Find Minimum in Rotated Sorted Array

```cpp
int findMin(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        // Right half is unsorted (contains pivot)
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        }
        // Left half is unsorted or mid is minimum
        else {
            right = mid;
        }
    }
    
    return nums[left];
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 33 | Search in Rotated Sorted Array | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/23/medium-33-search-in-rotated-sorted-array/) |
| 81 | Search in Rotated Sorted Array II | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | - |
| 153 | Find Minimum in Rotated Sorted Array | [Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | - |
| 154 | Find Minimum in Rotated Sorted Array II | [Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | - |

## Binary Search on Answer Space

### Binary Search on Answer Template

```cpp
// Find the answer in a search space
int binarySearchOnAnswer(int left, int right) {
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (isValid(mid)) {
            right = mid;  // Try smaller values
        } else {
            left = mid + 1;  // Try larger values
        }
    }
    
    return left;
}

// Or for maximum valid value
int binarySearchOnAnswerMax(int left, int right) {
    while (left < right) {
        int mid = left + (right - left + 1) / 2;
        
        if (isValid(mid)) {
            left = mid;  // Try larger values
        } else {
            right = mid - 1;  // Try smaller values
        }
    }
    
    return left;
}
```

### Example: Koko Eating Bananas

```cpp
int minEatingSpeed(vector<int>& piles, int h) {
    int left = 1, right = *max_element(piles.begin(), piles.end());
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        int hours = 0;
        
        for (int pile : piles) {
            hours += (pile + mid - 1) / mid;  // Ceiling division
        }
        
        if (hours <= h) {
            right = mid;  // Can eat slower
        } else {
            left = mid + 1;  // Need to eat faster
        }
    }
    
    return left;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 875 | Koko Eating Bananas | [Link](https://leetcode.com/problems/koko-eating-bananas/) | - |
| 1011 | Capacity To Ship Packages | [Link](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | - |
| 410 | Split Array Largest Sum | [Link](https://leetcode.com/problems/split-array-largest-sum/) | - |

## Search in 2D Matrix

### Search in Sorted 2D Matrix

```cpp
// Matrix sorted row-wise and column-wise
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size(), n = matrix[0].size();
    int row = 0, col = n - 1;
    
    while (row < m && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] > target) {
            col--;  // Move left
        } else {
            row++;  // Move down
        }
    }
    
    return false;
}
```

### Binary Search in 2D Matrix (Fully Sorted)

```cpp
// Matrix sorted in row-major order
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size(), n = matrix[0].size();
    int left = 0, right = m * n - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int row = mid / n, col = mid % n;
        
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return false;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 74 | Search a 2D Matrix | [Link](https://leetcode.com/problems/search-a-2d-matrix/) | - |
| 240 | Search a 2D Matrix II | [Link](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/07/medium-240-search-a-2d-matrix-ii/) |
| 270 | Closest Binary Search Tree Value | [Link](https://leetcode.com/problems/closest-binary-search-tree-value/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/easy-270-closest-binary-search-tree-value/) |

## Advanced Search Patterns

### Merge Sort on Prefix Sums

This advanced pattern combines prefix sums with merge sort to solve range query problems efficiently.

#### Template: Count Range Sum

```cpp
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        
        // Build prefix sum array
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        
        vector<long long> temp(n + 1);
        return divide(prefix, 0, n, lower, upper, temp);
    }

private:
    int divide(vector<long long>& prefix, int left, int right,
               int lower, int upper, vector<long long>& temp) {
        if (left >= right) return 0;
        
        int mid = (left + right) / 2;
        int count = 0;
        
        // Count in left and right halves
        count += divide(prefix, left, mid, lower, upper, temp);
        count += divide(prefix, mid + 1, right, lower, upper, temp);
        
        // Count cross pairs
        count += countCross(prefix, left, mid, right, lower, upper);
        
        // Merge sorted halves
        merge(prefix, left, mid, right, temp);
        
        return count;
    }
    
    int countCross(vector<long long>& prefix, int left, int mid, int right,
                   int lower, int upper) {
        int count = 0;
        int wl = left, wr = left;
        
        // For each prefix[j] in right half, count valid prefix[i] in left half
        // Condition: lower <= prefix[j] - prefix[i] <= upper
        // Rearranged: prefix[j] - upper <= prefix[i] <= prefix[j] - lower
        for (int i = mid + 1; i <= right; i++) {
            long long low = prefix[i] - upper;
            long long high = prefix[i] - lower;
            
            // Two pointers to find valid range
            while (wl <= mid && prefix[wl] < low) wl++;
            while (wr <= mid && prefix[wr] <= high) wr++;
            
            count += wr - wl;
        }
        
        return count;
    }
    
    void merge(vector<long long>& prefix, int left, int mid, int right,
               vector<long long>& temp) {
        int i = left, j = mid + 1, k = left;
        
        while (i <= mid && j <= right) {
            temp[k++] = (prefix[i] <= prefix[j]) ? prefix[i++] : prefix[j++];
        }
        
        while (i <= mid) temp[k++] = prefix[i++];
        while (j <= right) temp[k++] = prefix[j++];
        
        for (int i = left; i <= right; i++) {
            prefix[i] = temp[i];
        }
    }
};
```

#### Key Insights:

1. **Prefix Sum Transformation**: Convert subarray sum problem to prefix sum difference
   - `S(i, j) = prefix[j+1] - prefix[i]`
   - Range condition: `lower <= prefix[j+1] - prefix[i] <= upper`

2. **Divide and Conquer**: 
   - Divide prefix array into left and right halves
   - Recursively count valid pairs in each half
   - Count cross pairs (one from left, one from right)
   - Merge sorted halves

3. **Two Pointers in Merge**: 
   - For each `prefix[j]` in right half, find valid `prefix[i]` in left half
   - Use sliding window with two pointers `wl` and `wr`
   - `wl`: first index where `prefix[wl] >= prefix[j] - upper`
   - `wr`: first index where `prefix[wr] > prefix[j] - lower`
   - Count: `wr - wl`

4. **Time Complexity**: O(n log n)
   - Divide: O(log n) levels
   - Each level: O(n) for counting and merging

| ID | Title | Link | Solution |
|---|---|---|---|
| 327 | Count of Range Sum | [Link](https://leetcode.com/problems/count-of-range-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/20/hard-327-count-of-range-sum/) |
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/17/hard-315-count-of-smaller-numbers-after-self/) |

### Divide and Conquer Search

#### Template: Merge Sort with Counting

```cpp
// General template for divide and conquer with counting
int divideAndConquer(vector<int>& arr, int left, int right) {
    if (left >= right) return 0;
    
    int mid = left + (right - left) / 2;
    int count = 0;
    
    // Count in left and right halves
    count += divideAndConquer(arr, left, mid);
    count += divideAndConquer(arr, mid + 1, right);
    
    // Count cross pairs
    count += countCross(arr, left, mid, right);
    
    // Merge
    merge(arr, left, mid, right);
    
    return count;
}

int countCross(vector<int>& arr, int left, int mid, int right) {
    // Count pairs (i, j) where i in [left, mid] and j in [mid+1, right]
    // that satisfy some condition
    int count = 0;
    // Implementation depends on problem
    return count;
}

void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> temp(right - left + 1);
    int i = left, j = mid + 1, k = 0;
    
    while (i <= mid && j <= right) {
        temp[k++] = (arr[i] <= arr[j]) ? arr[i++] : arr[j++];
    }
    
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    
    for (int i = 0; i < temp.size(); i++) {
        arr[left + i] = temp[i];
    }
}
```

#### Applications:

- **Inversion Count**: Count pairs where `arr[i] > arr[j]` and `i < j`
- **Reverse Pairs**: Count pairs where `arr[i] > 2 * arr[j]` and `i < j`
- **Range Sum Queries**: Count subarray sums in a range using prefix sums
- **Closest Pair**: Find closest pair of points in 2D space

| ID | Title | Link | Solution |
|---|---|---|---|
| 493 | Reverse Pairs | [Link](https://leetcode.com/problems/reverse-pairs/) | - |
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | - |

### Ternary Search

Used to find the maximum or minimum of a **unimodal** function (a function that first increases then decreases, or vice versa).

#### Template: Find Maximum

```cpp
double ternarySearch(double left, double right) {
    double eps = 1e-9; // Precision
    while (right - left > eps) {
        double m1 = left + (right - left) / 3;
        double m2 = right - (right - left) / 3;
        
        if (f(m1) < f(m2)) {
            left = m1;
        } else {
            right = m2;
        }
    }
    return f(left);
}
```

#### Integer Version

```cpp
int ternarySearchInt(int left, int right) {
    while (right - left > 3) {
        int m1 = left + (right - left) / 3;
        int m2 = right - (right - left) / 3;
        
        if (f(m1) < f(m2)) {
            left = m1;
        } else {
            right = m2;
        }
    }
    
    // Check remaining elements linearly
    int res = f(left);
    for (int i = left + 1; i <= right; i++) {
        res = max(res, f(i));
    }
    return res;
}
```

### Parallel Binary Search

Used when we have multiple queries ($Q$) that can be answered by binary search on a monotonic sequence of $N$ operations. Instead of $O(Q \cdot N \log N)$, it answers all queries in $O((N + Q) \log N)$.

#### Template

```cpp
struct Query {
    int id, l, r;
};

void solve(int L, int R, vector<Query>& queries) {
    if (queries.empty()) return;
    if (L == R) {
        for (auto& q : queries) ans[q.id] = L;
        return;
    }
    
    int mid = L + (R - L) / 2;
    
    // 1. Apply operations from L to mid
    // 2. Check each query in 'queries'
    // 3. Split queries into two groups: leftHalf and rightHalf
    // 4. Undo operations from L to mid
    
    solve(L, mid, leftHalf);
    solve(mid + 1, R, rightHalf);
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1515 | Best Position for a Service Centre | [Link](https://leetcode.com/problems/best-position-for-a-service-centre/) | - |
| 1095 | Find in Mountain Array | [Link](https://leetcode.com/problems/find-in-mountain-array/) | - |
| 715 | Range Module | [Link](https://leetcode.com/problems/range-module/) | - |
| 1157 | Online Majority Element In Subarray | [Link](https://leetcode.com/problems/online-majority-element-in-subarray/) | - |

### Exponential Search

Used when searching in an infinite array or when the target is expected to be near the beginning of the array. It first finds a range where the target exists by doubling the index, then performs binary search.

#### Template

```cpp
int exponentialSearch(vector<int>& arr, int target) {
    if (arr.empty()) return -1;
    if (arr[0] == target) return 0;
    
    int i = 1;
    int n = arr.size();
    while (i < n && arr[i] <= target) {
        i *= 2;
    }
    
    // Binary search within [i/2, min(i, n-1)]
    return binarySearchRange(arr, i / 2, min(i, n - 1), target);
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 702 | Search in a Sorted Array of Unknown Size | [Link](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) | - |

### Tree-Based Search (Segment Tree, BIT)

For advanced search problems involving range updates or dynamic prefix sums, tree-based data structures like **Segment Trees** and **Fenwick Trees** are essential.

- **[Binary Search on Segment Tree (Tree Walking)](/posts/2025-10-29-leetcode-templates-trees/#binary-search-on-segment-tree-tree-walking)** - Descending the tree in $O(\log N)$.
- **[Segment Tree with Lazy Propagation](/posts/2025-10-29-leetcode-templates-trees/#segment-tree-with-lazy-propagation-range-update)** - Range updates and range queries.
- **[Fenwick Tree (Binary Indexed Tree)](/posts/2025-10-29-leetcode-templates-trees/#fenwick-tree-binary-indexed-tree)** - Efficient prefix sums and point updates.

| ID | Title | Link | Solution |
|---|---|---|---|
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | - |
| 218 | The Skyline Problem | [Link](https://leetcode.com/problems/the-skyline-problem/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/05/hard-218-skyline-problem/) |
| 699 | Falling Squares | [Link](https://leetcode.com/problems/falling-squares/) | - |

## Common Patterns Summary

1. **Standard Binary Search**: `left <= right`, check `nums[mid] == target`
2. **Lower/Upper Bound**: `left < right`, adjust based on condition
3. **Rotated Array**: Check which half is sorted, then decide direction
4. **Answer Space**: Binary search on possible answers, check validity
5. **2D Matrix**: Start from corner, move based on comparison
6. **Merge Sort on Prefix**: Divide and conquer with prefix sums for range queries

## Related Templates

- **[Array & Matrix](/posts/2025-11-24-leetcode-templates-array-matrix/)** - Binary search in arrays
- **[Divide and Conquer](/posts/2025-10-29-leetcode-templates-advanced/)** - Advanced divide and conquer patterns
- **[Dynamic Programming](/posts/2025-10-29-leetcode-templates-dp/)** - DP with binary search

{% endraw %}
