---
layout: post
title: "1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit"
date: 2026-02-12 00:00:00 -0700
categories: [leetcode, medium, sliding-window, monotonic-queue]
tags: [leetcode, medium, sliding-window, monotonic-queue]
permalink: /2026/02/12/medium-1438-longest-continuous-subarray-with-absolute-diff/
---

## Problem

Given an integer array `nums` and an integer `limit`, return the size of the longest continuous subarray such that the absolute difference between the maximum and minimum element in the subarray is less than or equal to `limit`.

## Examples

**Example 1**

```
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: The longest subarray is [2,4] or [4,7].
```

**Example 2**

```
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The longest subarray is [2,4,7,2].
```

**Example 3**

```
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
Explanation: The longest subarray of equal values is length 3 (three 2's).
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

## Approach

We need the longest window [l..r] where max(nums[l..r]) - min(nums[l..r]) <= limit.

Two common sliding-window techniques:

1. Multiset (or balanced BST) to maintain current window's min and max. Expand right pointer; when condition violated, shrink left pointer and erase from multiset. Time: O(n log n), Space: O(n).

2. Monotonic deques (optimal): maintain two deques:
   - `decrease` keeps current window's values in decreasing order (front = max)
   - `increase` keeps values in increasing order (front = min)
   Push new value by popping from back while invariant violated. When shrinking left, pop from front if it equals outgoing value. This yields O(n) time and O(n) space.

## Solutions

### Multiset (balanced BST) — O(n log n)

{% raw %}
```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        multiset<int> ms;
        int left = 0, rtn = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            ms.insert(nums[right]);
            while (*ms.rbegin() - *ms.begin() > limit) {
                ms.erase(ms.find(nums[left]));
                left++;
            }
            rtn = max(rtn, right - left + 1);
        }
        return rtn;
    }
};
```
{% endraw %}

### Monotonic Deques — O(n)

{% raw %}
```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> increase, decrease; // store values (or indices)
        int left = 0, rtn = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            int val = nums[right];
            // maintain increasing deque for min
            while (!increase.empty() && increase.back() > val) increase.pop_back();
            increase.push_back(val);
            // maintain decreasing deque for max
            while (!decrease.empty() && decrease.back() < val) decrease.pop_back();
            decrease.push_back(val);

            // shrink window while invalid
            while (decrease.front() - increase.front() > limit) {
                if (nums[left] == decrease.front()) decrease.pop_front();
                if (nums[left] == increase.front()) increase.pop_front();
                left++;
            }
            rtn = max(rtn, right - left + 1);
        }
        return rtn;
    }
};
```
{% endraw %}

## Complexity

- Time: O(n) with monotonic deques, O(n log n) with multiset.
- Space: O(n).

## Template Reference

- [Monotonic Queue / Sliding Window](/posts/2025-10-29-leetcode-templates-data-structures/#monotonic-queue)

