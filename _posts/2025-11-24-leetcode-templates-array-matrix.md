---
layout: post
title: "Algorithm Templates: Array & Matrix"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates array matrix
permalink: /posts/2025-11-24-leetcode-templates-array-matrix/
tags: [leetcode, templates, array, matrix]
---

{% raw %}
Minimal, copy-paste C++ for two pointers, sliding window, prefix sum, binary search, and matrix operations. See also [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/) and [Search](/posts/2026-01-20-leetcode-templates-search/).

## Contents

- [Two Pointers](#two-pointers)
- [Sliding Window](#sliding-window)
- [Prefix Sum](#prefix-sum)
- [Binary Search](#binary-search)
- [Matrix Operations](#matrix-operations)
- [Array Manipulation](#array-manipulation)

## Two Pointers

### Two Sum on Sorted Array

```cpp
bool twoSumSorted(const vector<int>& a, int target){
    int l = 0, r = (int)a.size() - 1;
    while (l < r){
        long long sum = (long long)a[l] + a[r];
        if (sum == target) return true;
        if (sum < target) ++l; else --r;
    }
    return false;
}
```

### Three Sum / Four Sum

```cpp
// 3Sum
vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    int n = nums.size();
    
    for (int i = 0; i < n - 2; ++i) {
        if (i > 0 && nums[i] == nums[i-1]) continue;
        
        int left = i + 1, right = n - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum == 0) {
                result.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left+1]) left++;
                while (left < right && nums[right] == nums[right-1]) right--;
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 15 | 3Sum | [Link](https://leetcode.com/problems/3sum/) | - |
| 18 | 4Sum | [Link](https://leetcode.com/problems/4sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/11/04/medium-18-4sum/) |
| 11 | Container With Most Water | [Link](https://leetcode.com/problems/container-with-most-water/) | - |
| 75 | Sort Colors | [Link](https://leetcode.com/problems/sort-colors/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-02-medium-75-sort-colors/) |
| 360 | Sort Transformed Array | [Link](https://leetcode.com/problems/sort-transformed-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/medium-360-sort-transformed-array/) |
| 344 | Reverse String | [Link](https://leetcode.com/problems/reverse-string/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-29-easy-344-reverse-string/) |
| 844 | Backspace String Compare | [Link](https://leetcode.com/problems/backspace-string-compare/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/easy-844-backspace-string-compare/) |
| 1868 | Product of Two Run-Length Encoded Arrays | [Link](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-1868-product-of-two-run-length-encoded-arrays/) |

## Sliding Window

### Fixed Size Window

```cpp
// Maximum sum of subarray of size k
int maxSumSubarray(vector<int>& nums, int k) {
    int sum = 0;
    for (int i = 0; i < k; ++i) {
        sum += nums[i];
    }
    int maxSum = sum;
    
    for (int i = k; i < nums.size(); ++i) {
        sum = sum - nums[i-k] + nums[i];
        maxSum = max(maxSum, sum);
    }
    
    return maxSum;
}
```

### Variable Size Window

```cpp
// Longest subarray with sum <= k
int longestSubarray(vector<int>& nums, int k) {
    int left = 0, sum = 0, maxLen = 0;
    
    for (int right = 0; right < nums.size(); ++right) {
        sum += nums[right];
        
        while (sum > k) {
            sum -= nums[left++];
        }
        
        maxLen = max(maxLen, right - left + 1);
    }
    
    return maxLen;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 3 | Longest Substring Without Repeating Characters | [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) |
| 209 | Minimum Size Subarray Sum | [Link](https://leetcode.com/problems/minimum-size-subarray-sum/) | - |
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 480 | Sliding Window Median | [Link](https://leetcode.com/problems/sliding-window-median/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-480-sliding-window-median/) |
| 2799 | Count Complete Subarrays in an Array | [Link](https://leetcode.com/problems/count-complete-subarrays-in-an-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-2799-count-complete-subarrays-in-an-array/) |
| 346 | Moving Average from Data Stream | [Link](https://leetcode.com/problems/moving-average-from-data-stream/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-14-easy-346-moving-average-from-data-stream/) |
| 713 | Subarray Product Less Than K | [Link](https://leetcode.com/problems/subarray-product-less-than-k/) | - |

## Prefix Sum

### Basic Prefix Sum

```cpp
vector<int> prefixSum(const vector<int>& a){
    vector<int> ps(a.size()+1);
    for (int i = 0; i < (int)a.size(); ++i) {
        ps[i+1] = ps[i] + a[i];
    }
    return ps;
}

// Range sum query
int rangeSum(vector<int>& prefix, int l, int r) {
    return prefix[r+1] - prefix[l];
}
```

### Difference Array

```cpp
// Range addition
vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
    vector<int> diff(length + 1, 0);
    
    for (auto& update : updates) {
        diff[update[0]] += update[2];
        diff[update[1] + 1] -= update[2];
    }
    
    vector<int> result(length);
    result[0] = diff[0];
    for (int i = 1; i < length; ++i) {
        result[i] = result[i-1] + diff[i];
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 303 | Range Sum Query - Immutable | [Link](https://leetcode.com/problems/range-sum-query-immutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/01/easy-303-range-sum-query-immutable/) |
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/16/medium-307-range-sum-query-mutable/) |
| 560 | Subarray Sum Equals K | [Link](https://leetcode.com/problems/subarray-sum-equals-k/) | - |
| 525 | Contiguous Array | [Link](https://leetcode.com/problems/contiguous-array/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-medium-525-contiguous-array/) |
| 1124 | Longest Well-Performing Interval | [Link](https://leetcode.com/problems/longest-well-performing-interval/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/16/medium-1124-longest-well-performing-interval/) |
| 327 | Count of Range Sum | [Link](https://leetcode.com/problems/count-of-range-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/20/hard-327-count-of-range-sum/) |
| 370 | Range Addition | [Link](https://leetcode.com/problems/range-addition/) | - |
| 1094 | Car Pooling | [Link](https://leetcode.com/problems/car-pooling/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-22-medium-1094-car-pooling/) |

## Binary Search

### Search in Sorted Array

```cpp
int binarySearch(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    
    return -1;
}
```

### Search in Rotated Sorted Array

```cpp
int searchRotated(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        
        if (nums[left] <= nums[mid]) {
            // Left half is sorted
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            // Right half is sorted
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    
    return -1;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 33 | Search in Rotated Sorted Array | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/23/medium-33-search-in-rotated-sorted-array/) |
| 34 | Find First and Last Position | [Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | - |
| 240 | Search a 2D Matrix II | [Link](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/07/medium-240-search-a-2d-matrix-ii/) |

## Matrix Operations

### Rotate Matrix

```cpp
// Rotate 90 degrees clockwise
void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();
    
    // Transpose
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    
    // Reverse each row
    for (int i = 0; i < n; ++i) {
        reverse(matrix[i].begin(), matrix[i].end());
    }
}
```

### Spiral Matrix

```cpp
vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.empty()) return result;
    
    int m = matrix.size(), n = matrix[0].size();
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    
    while (top <= bottom && left <= right) {
        // Right
        for (int j = left; j <= right; ++j) {
            result.push_back(matrix[top][j]);
        }
        top++;
        
        // Down
        for (int i = top; i <= bottom; ++i) {
            result.push_back(matrix[i][right]);
        }
        right--;
        
        // Left
        if (top <= bottom) {
            for (int j = right; j >= left; --j) {
                result.push_back(matrix[bottom][j]);
            }
            bottom--;
        }
        
        // Up
        if (left <= right) {
            for (int i = bottom; i >= top; --i) {
                result.push_back(matrix[i][left]);
            }
            left++;
        }
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 48 | Rotate Image | [Link](https://leetcode.com/problems/rotate-image/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/medium-48-rotate-image/) |
| 54 | Spiral Matrix | [Link](https://leetcode.com/problems/spiral-matrix/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/25/medium-54-spiral-matrix/) |
| 59 | Spiral Matrix II | [Link](https://leetcode.com/problems/spiral-matrix-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/18/medium-59-spiral-matrix-ii/) |
| 498 | Diagonal Traverse | [Link](https://leetcode.com/problems/diagonal-traverse/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/20/medium-498-diagonal-traverse/) |
| 189 | Rotate Array | [Link](https://leetcode.com/problems/rotate-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/20/medium-189-rotate-array/) |
| 419 | Battleships in a Board | [Link](https://leetcode.com/problems/battleships-in-a-board/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-419-battleships-in-a-board/) |
| 661 | Image Smoother | [Link](https://leetcode.com/problems/image-smoother/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/easy-661-image-smoother/) |

## Array Manipulation

### Merge Intervals

```cpp
vector<vector<int>> merge(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> merged;
    
    for (auto& interval : intervals) {
        if (merged.empty() || merged.back()[1] < interval[0]) {
            merged.push_back(interval);
        } else {
            merged.back()[1] = max(merged.back()[1], interval[1]);
        }
    }
    
    return merged;
}
```

### Jump Game

```cpp
// Jump Game II - Minimum jumps
int jump(vector<int>& nums) {
    int n = nums.size();
    int jumps = 0, curEnd = 0, curFar = 0;
    
    for (int i = 0; i < n - 1; ++i) {
        curFar = max(curFar, i + nums[i]);
        
        if (i == curEnd) {
            jumps++;
            curEnd = curFar;
        }
    }
    
    return jumps;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 56 | Merge Intervals | [Link](https://leetcode.com/problems/merge-intervals/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-56-merge-intervals/) |
| 45 | Jump Game II | [Link](https://leetcode.com/problems/jump-game-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-45-jump-game-ii/) |
| 969 | Pancake Sorting | [Link](https://leetcode.com/problems/pancake-sorting/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-969-pancake-sorting/) |

## More templates

- **Arrays & Strings, Search:** [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Data structures, Graph:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

