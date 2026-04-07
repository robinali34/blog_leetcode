---
layout: post
title: "LeetCode 2433. Find The Original Array of Prefix Xor"
date: 2026-04-05
categories: [leetcode, medium, bit-manipulation, prefix]
tags: [leetcode, medium, bit-manipulation, xor, prefix]
permalink: /2026/04/05/medium-2433-find-the-original-array-of-prefix-xor/
---

You are given an integer array `pref` of size `n`. Find and return the array `arr` of size `n` that satisfies:

$$\text{pref}[i] = \text{arr}[0] \oplus \text{arr}[1] \oplus \ldots \oplus \text{arr}[i]$$

It is guaranteed that a unique `arr` exists.

## Examples

**Example 1:**

```
Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation:
  pref[0] = 5             → arr[0] = 5
  pref[1] = 5 ^ 7 = 2    → arr[1] = 7
  pref[2] = 5 ^ 7 ^ 2 = 0 → arr[2] = 2
  ...
```

**Example 2:**

```
Input: pref = [13]
Output: [13]
```

## Constraints

- `1 <= n <= 10^5`
- `0 <= pref[i] <= 10^6`

## Thinking Process

### XOR Prefix Sum Property

Given:

$$\text{pref}[i] = \text{arr}[0] \oplus \text{arr}[1] \oplus \ldots \oplus \text{arr}[i]$$

$$\text{pref}[i-1] = \text{arr}[0] \oplus \text{arr}[1] \oplus \ldots \oplus \text{arr}[i-1]$$

XOR both sides:

$$\text{pref}[i] \oplus \text{pref}[i-1] = \text{arr}[i]$$

This is the XOR analog of prefix sum difference: just as `arr[i] = prefixSum[i] - prefixSum[i-1]` for addition, we have `arr[i] = pref[i] ^ pref[i-1]` for XOR.

Base case: `arr[0] = pref[0]`.

## Solution 1: New Array -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int n = pref.size();
        vector<int> arr;
        arr.push_back(pref[0]);
        for (int i = 1; i < n; ++i) {
            arr.push_back(pref[i] ^ pref[i - 1]);
        }
        return arr;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ for output

## Solution 2: In-Place (Reverse Pass) -- $O(1)$ auxiliary

Process right-to-left so each `pref[i-1]` is still the original value when we compute `pref[i] ^ pref[i-1]`.

{% raw %}
```cpp
class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int n = pref.size();
        for (int i = n - 1; i > 0; --i) {
            pref[i] = pref[i] ^ pref[i - 1];
        }
        return pref;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(1)$ auxiliary

### Why Reverse Order?

If we process left-to-right in-place, modifying `pref[1]` corrupts the value needed for `pref[2]`. Going right-to-left, each `pref[i]` only depends on `pref[i-1]`, which hasn't been modified yet.

## Common Mistakes

- Processing left-to-right in-place (corrupts values needed for later computations)
- Forgetting the base case `arr[0] = pref[0]`

## Key Takeaways

- **XOR prefix ↔ original array** mirrors **addition prefix sum ↔ difference array**, with XOR replacing both addition and subtraction (since `a ^ a = 0`)
- In-place reverse pass avoids the dependency issue cleanly
- XOR is its own inverse: `a ^ b ^ b = a` -- this self-inverse property underpins all XOR prefix problems

## Related Problems

- [260. Single Number III](https://leetcode.com/problems/single-number-iii/) -- XOR partitioning
- [136. Single Number](https://leetcode.com/problems/single-number/) -- XOR cancellation
- [389. Find the Difference](https://leetcode.com/problems/find-the-difference/) -- XOR to find extra element
- [303. Range Sum Query](https://leetcode.com/problems/range-sum-query-immutable/) -- addition prefix sum analog

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
