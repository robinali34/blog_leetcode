---
layout: post
title: "Algorithm Templates: Array & Matrix"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates array matrix
permalink: /posts/2025-11-24-leetcode-templates-array-matrix/
tags: [leetcode, templates, array, matrix]
---
Welcome to the Array & Matrix template collection! These are ready-to-use C++ snippets for the most common array patterns: two pointers, sliding window, prefix sum, binary search, and matrix operations. Each template is minimal enough to memorize yet complete enough to paste into a solution and adapt. See also [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/) and [Search](/posts/2026-01-20-leetcode-templates-search/).

> **Arrays are the most common data structure in interviews.** Most problems start with an array or can be reduced to one. Learning these patterns well — two pointers, sliding window, prefix sum, and binary search — covers roughly 40% of all LeetCode problems.

## Contents

- [Two Pointers](#two-pointers)
- [Sliding Window](#sliding-window)
- [Prefix Sum](#prefix-sum)
- [Binary Search](#binary-search)
- [Matrix Operations](#matrix-operations)
- [Array Manipulation](#array-manipulation)

## Two Pointers

**When to use:** The problem says "sorted array", asks for a "pair with target sum", mentions "container with most water", or requires comparing elements from both ends.

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

**When to use:** The problem asks for a "subarray of size k", "longest/shortest subarray with property X", or any contiguous subarray optimization.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 170" style="max-width:520px;width:100%">
  <style>
    text { font-family: ui-monospace, monospace; fill: #5A5752; }
    .label { font-size: 13px; }
    .idx { font-size: 11px; }
    .arrow-label { font-size: 11px; font-style: italic; }
  </style>
  <!-- array boxes -->
  <g transform="translate(30,50)">
    <rect x="0"   y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="25"  y="26" text-anchor="middle" class="label">3</text>
    <text x="25"  y="55" text-anchor="middle" class="idx">0</text>
    <rect x="60"  y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="85"  y="26" text-anchor="middle" class="label">1</text>
    <text x="85"  y="55" text-anchor="middle" class="idx">1</text>
    <rect x="120" y="0" width="50" height="40" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="145" y="26" text-anchor="middle" class="label">7</text>
    <text x="145" y="55" text-anchor="middle" class="idx">2</text>
    <rect x="180" y="0" width="50" height="40" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="205" y="26" text-anchor="middle" class="label">2</text>
    <text x="205" y="55" text-anchor="middle" class="idx">3</text>
    <rect x="240" y="0" width="50" height="40" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="265" y="26" text-anchor="middle" class="label">5</text>
    <text x="265" y="55" text-anchor="middle" class="idx">4</text>
    <rect x="300" y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="325" y="26" text-anchor="middle" class="label">9</text>
    <text x="325" y="55" text-anchor="middle" class="idx">5</text>
    <rect x="360" y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="385" y="26" text-anchor="middle" class="label">4</text>
    <text x="385" y="55" text-anchor="middle" class="idx">6</text>
    <rect x="420" y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="445" y="26" text-anchor="middle" class="label">8</text>
    <text x="445" y="55" text-anchor="middle" class="idx">7</text>
  </g>
  <!-- window bracket -->
  <rect x="148" y="42" width="194" height="52" rx="6" fill="none" stroke="#D4D8E0" stroke-width="2.5" stroke-dasharray="6,3"/>
  <!-- left pointer -->
  <line x1="175" y1="38" x2="175" y2="18" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#arrowUp)"/>
  <text x="175" y="12" text-anchor="middle" class="arrow-label" fill="#5A5752">left</text>
  <!-- right pointer -->
  <line x1="325" y1="38" x2="325" y2="18" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#arrowUp)"/>
  <text x="325" y="12" text-anchor="middle" class="arrow-label" fill="#5A5752">right</text>
  <!-- shrink-left arrow -->
  <line x1="165" y1="130" x2="210" y2="130" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#arrowRight)"/>
  <text x="188" y="148" text-anchor="middle" class="arrow-label">shrink left</text>
  <!-- expand-right arrow -->
  <line x1="380" y1="130" x2="335" y2="130" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#arrowLeft)"/>
  <text x="358" y="148" text-anchor="middle" class="arrow-label">expand right</text>
  <!-- window label -->
  <text x="245" y="130" text-anchor="middle" class="label" fill="#5A5752">window [left, right]</text>
  <defs>
    <marker id="arrowUp" markerWidth="8" markerHeight="6" refX="4" refY="6" orient="auto"><path d="M0,6 L4,0 L8,6" fill="none" stroke="#B8B5B0" stroke-width="1.2"/></marker>
    <marker id="arrowRight" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="none" stroke="#B8B5B0" stroke-width="1.2"/></marker>
    <marker id="arrowLeft" markerWidth="8" markerHeight="6" refX="0" refY="3" orient="auto"><path d="M8,0 L0,3 L8,6" fill="none" stroke="#B8B5B0" stroke-width="1.2"/></marker>
  </defs>
</svg>

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

**When to use:** The problem involves "range sum queries", "subarray sum equals k", or asks you to compute cumulative totals over a range efficiently.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 280" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <rect width="700" height="280" rx="12" fill="#FAF8F5"/>
  <text x="350" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#3A3530">Prefix Sum — Range Query</text>
  <text x="148" y="72" text-anchor="end" font-size="11" fill="#7A7772">Original</text>
  <g font-size="13" text-anchor="middle">
    <rect x="205" y="58" width="54" height="34" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="232" y="80" fill="#5A5752">1</text><text x="232" y="104" font-size="9" fill="#9A9792">0</text>
    <rect x="263" y="58" width="54" height="34" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="290" y="80" fill="#5A5752">2</text><text x="290" y="104" font-size="9" fill="#9A9792">1</text>
    <rect x="321" y="58" width="54" height="34" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
    <text x="348" y="80" fill="#3A3530" font-weight="bold">3</text><text x="348" y="104" font-size="9" fill="#5A5752">2</text>
    <rect x="379" y="58" width="54" height="34" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
    <text x="406" y="80" fill="#3A3530" font-weight="bold">4</text><text x="406" y="104" font-size="9" fill="#5A5752">3</text>
    <rect x="437" y="58" width="54" height="34" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
    <text x="464" y="80" fill="#3A3530" font-weight="bold">5</text><text x="464" y="104" font-size="9" fill="#5A5752">4</text>
  </g>
  <line x1="321" y1="52" x2="491" y2="52" stroke="#8B8680" stroke-width="1.5"/>
  <line x1="321" y1="52" x2="321" y2="56" stroke="#8B8680" stroke-width="1.5"/>
  <line x1="491" y1="52" x2="491" y2="56" stroke="#8B8680" stroke-width="1.5"/>
  <text x="406" y="46" text-anchor="middle" font-size="10" fill="#8B8680">range [2..4]</text>
  <text x="148" y="166" text-anchor="end" font-size="11" fill="#7A7772">Prefix</text>
  <g font-size="13" text-anchor="middle">
    <rect x="176" y="152" width="54" height="34" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="203" y="174" fill="#5A5752">0</text><text x="203" y="198" font-size="9" fill="#9A9792">0</text>
    <rect x="234" y="152" width="54" height="34" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="261" y="174" fill="#5A5752">1</text><text x="261" y="198" font-size="9" fill="#9A9792">1</text>
    <rect x="292" y="152" width="54" height="34" rx="5" fill="#E8E3D8" stroke="#8B8680" stroke-width="1.5"/>
    <text x="319" y="174" fill="#3A3530" font-weight="bold">3</text><text x="319" y="198" font-size="9" fill="#5A5752">2</text>
    <rect x="350" y="152" width="54" height="34" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="377" y="174" fill="#5A5752">6</text><text x="377" y="198" font-size="9" fill="#9A9792">3</text>
    <rect x="408" y="152" width="54" height="34" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
    <text x="435" y="174" fill="#5A5752">10</text><text x="435" y="198" font-size="9" fill="#9A9792">4</text>
    <rect x="466" y="152" width="54" height="34" rx="5" fill="#E8E3D8" stroke="#8B8680" stroke-width="1.5"/>
    <text x="493" y="174" fill="#3A3530" font-weight="bold">15</text><text x="493" y="198" font-size="9" fill="#5A5752">5</text>
  </g>
  <line x1="493" y1="188" x2="493" y2="218" stroke="#8B8680" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="319" y1="188" x2="319" y2="218" stroke="#8B8680" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="350" y="238" text-anchor="middle" font-size="12" fill="#5A5752">sum(a[2..4]) = prefix[5] − prefix[2] = 15 − 3 = <tspan font-weight="bold" fill="#3A3530">12</tspan></text>
  <text x="350" y="260" text-anchor="middle" font-size="11" fill="#7A7772" font-style="italic">Range sum in O(1) after O(n) preprocessing</text>
</svg>
</div>

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

**When to use:** The input is sorted, the problem says "find position", "search", or you need to minimize/maximize a value where the answer is monotonic.

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

**When to use:** The problem says "rotate image", "spiral order", "transpose matrix", or involves traversing a 2D grid in a specific pattern.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 330" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="sp6Arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#8B8680"/></marker>
  </defs>
  <rect width="620" height="330" rx="12" fill="#FAF8F5"/>
  <text x="310" y="26" text-anchor="middle" font-size="15" font-weight="bold" fill="#3A3530">Spiral Matrix — Traversal Order</text>
  <g font-size="14" text-anchor="middle">
    <rect x="200" y="48" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="225" y="79" fill="#3A3530" font-weight="bold">1</text>
    <rect x="254" y="48" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="279" y="79" fill="#3A3530">2</text>
    <rect x="308" y="48" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="333" y="79" fill="#3A3530">3</text>
    <rect x="362" y="48" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="387" y="79" fill="#3A3530">4</text>
    <rect x="200" y="102" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="225" y="133" fill="#3A3530">12</text>
    <rect x="254" y="102" width="50" height="50" rx="4" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="279" y="133" fill="#3A3530">13</text>
    <rect x="308" y="102" width="50" height="50" rx="4" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="333" y="133" fill="#3A3530">14</text>
    <rect x="362" y="102" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="387" y="133" fill="#3A3530">5</text>
    <rect x="200" y="156" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="225" y="187" fill="#3A3530">11</text>
    <rect x="254" y="156" width="50" height="50" rx="4" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="279" y="187" fill="#3A3530">16</text>
    <rect x="308" y="156" width="50" height="50" rx="4" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="333" y="187" fill="#3A3530">15</text>
    <rect x="362" y="156" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="387" y="187" fill="#3A3530">6</text>
    <rect x="200" y="210" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="225" y="241" fill="#3A3530">10</text>
    <rect x="254" y="210" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="279" y="241" fill="#3A3530">9</text>
    <rect x="308" y="210" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="333" y="241" fill="#3A3530">8</text>
    <rect x="362" y="210" width="50" height="50" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.2"/>
    <text x="387" y="241" fill="#3A3530">7</text>
  </g>
  <line x1="218" y1="40" x2="398" y2="40" stroke="#8B8680" stroke-width="2" marker-end="url(#sp6Arr)"/>
  <text x="308" y="36" text-anchor="middle" font-size="10" fill="#7A7772">→ right</text>
  <line x1="420" y1="58" x2="420" y2="252" stroke="#8B8680" stroke-width="2" marker-end="url(#sp6Arr)"/>
  <text x="444" y="155" font-size="10" fill="#7A7772">↓ down</text>
  <line x1="398" y1="268" x2="218" y2="268" stroke="#8B8680" stroke-width="2" marker-end="url(#sp6Arr)"/>
  <text x="308" y="282" text-anchor="middle" font-size="10" fill="#7A7772">← left</text>
  <line x1="192" y1="252" x2="192" y2="112" stroke="#8B8680" stroke-width="2" marker-end="url(#sp6Arr)"/>
  <text x="178" y="175" text-anchor="end" font-size="10" fill="#7A7772">↑ up</text>
  <g transform="translate(68, 302)">
    <rect x="0" y="0" width="14" height="14" rx="2" fill="#D4D8E0" stroke="#8B8680" stroke-width="1"/>
    <text x="20" y="11" font-size="10" fill="#5A5752">outer ring (1–12)</text>
    <rect x="150" y="0" width="14" height="14" rx="2" fill="#E8D5D0" stroke="#8B8680" stroke-width="1"/>
    <text x="170" y="11" font-size="10" fill="#5A5752">inner ring (13–16)</text>
    <text x="300" y="11" font-size="10" fill="#7A7772">right → down → left → up → repeat inward</text>
  </g>
</svg>
</div>

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
| 73 | Set Matrix Zeroes | [Link](https://leetcode.com/problems/set-matrix-zeroes/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/02/medium-73-set-matrix-zeroes/) |

## Array Manipulation

**When to use:** The problem involves "merge intervals", "jump game", "overlapping ranges", or requires rearranging array elements in-place.

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

## Summary

| Pattern | Signal Phrases | Key Idea |
|---|---|---|
| Two Pointers | "sorted array", "pair sum", "container" | Start/end pointers moving inward |
| Sliding Window | "substring", "subarray of size k" | Expand right, shrink left |
| Prefix Sum | "range sum", "subarray sum equals k" | Precompute cumulative sums |
| Binary Search | "sorted", "find position" | Halve search space |
| Matrix | "rotate", "spiral", "transpose" | Index mapping |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Arrays & Strings, Search:** [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Data structures, Graph:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
