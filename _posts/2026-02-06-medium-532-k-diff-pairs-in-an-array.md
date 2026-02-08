---
layout: post
title: "532. K-diff Pairs in an Array"
date: 2026-02-06 00:00:00 -0700
categories: [leetcode, medium, array, hash-table]
permalink: /2026/02/06/medium-532-k-diff-pairs-in-an-array/
tags: [leetcode, medium, array, hash-table]
---

# 532. K-diff Pairs in an Array

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the number of **unique** k-diff pairs in the array.

A **k-diff pair** is an integer pair `(nums[i], nums[j])` where:

- `0 <= i, j < nums.length`
- `i != j`
- `|nums[i] - nums[j]| == k`

Pairs `(i, j)` and `(j, i)` count as the same pair.

## Examples

**Example 1:**

```
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: The two 2-diff pairs are (1, 3) and (3, 5). (Two 1s yield one unique pair (1,3).)
```

**Example 2:**

```
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: The four 1-diff pairs are (1,2), (2,3), (3,4), (4,5).
```

**Example 3:**

```
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: The only 0-diff pair is (1, 1).
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^7 <= nums[i] <= 10^7`
- `0 <= k <= 10^7`

## Solution Approach

- **k == 0:** We need pairs of the same value. Count how many distinct numbers appear more than once; each such number contributes one unique pair.
- **k > 0:** We need pairs with difference exactly k. For each distinct value `num`, check whether `num + k` exists (checking only `num + k` avoids double-counting (a, a+k) and (a+k, a)). Use a frequency map or a set of values.

## Solution 1: Single Hash Map (Frequencies)

One pass to build frequency map; then handle k==0 (count values with freq > 1) and k>0 (count values where num+k exists).

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;
        for (auto& i : nums) {
            freqs[i] += 1;
        }

        int rtn = 0;
        if (k == 0) {
            for (auto& [_, freq] : freqs) {
                if (freq > 1) rtn++;
            }
        } else {
            for (auto& [num, _] : freqs) {
                if (freqs.contains(num + k)) {
                    rtn++;
                }
            }
        }
        return rtn;
    }
};
```

- **k == 0:** Each value that appears at least twice gives exactly one unique pair (that value with itself).
- **k > 0:** For each distinct `num`, we only check `num + k` so each pair is counted once.
- **Time:** O(n). **Space:** O(n).

## Solution 2: Map for k==0, Set for k>0

Same logic; k==0 uses a map to count frequencies, k>0 uses a set and checks `num + k`.

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int rtn = 0;
        if (k == 0) {
            unordered_map<int, int> hm;
            for (int num : nums) {
                hm[num]++;
            }
            for (auto it = hm.begin(); it != hm.end(); ++it) {
                if (it->second > 1) rtn++;
            }
        } else {
            unordered_set<int> hs;
            for (int num : nums) {
                hs.insert(num);
            }
            for (auto it = hs.begin(); it != hs.end(); ++it) {
                if (hs.contains(*it + k)) {
                    rtn++;
                }
            }
        }
        return rtn;
    }
};
```

- **Time:** O(n). **Space:** O(n).

## Key Insights

1. **Unique pairs:** Count by distinct values (or by one representative of each pair), not by indices.
2. **k == 0:** Count distinct numbers that appear more than once.
3. **k > 0:** Only check `num + k` (or only `num - k`) to count each pair once.
4. **Avoid k < 0:** Problem states `k >= 0`; no need to handle negative k.

## Related Problems

- [1. Two Sum](https://leetcode.com/problems/two-sum/) — Find pairs with a target sum
- [454. 4Sum II](https://leetcode.com/problems/4sum-ii/) — Count pairs from four arrays
