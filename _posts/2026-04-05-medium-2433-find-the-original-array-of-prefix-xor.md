---
layout: post
title: "[Medium] 2433. Find The Original Array of Prefix Xor"
date: 2026-04-05
categories: [leetcode, medium, bit-manipulation, prefix]
tags: [leetcode, medium, bit-manipulation, xor, prefix]
permalink: /2026/04/05/medium-2433-find-the-original-array-of-prefix-xor/
---
You are given an integer array `pref` of size `n`. Find and return the array `arr` of size `n` that satisfies:

$text{pref}[i] = text{arr}[0] oplus text{arr}[1] oplus ldots oplus text{arr}[i]

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

text{pref}[i] = text{arr}[0] oplus text{arr}[1] oplus ldots oplus text{arr}[i]

text{pref}[i-1] = text{arr}[0] oplus text{arr}[1] oplus ldots oplus text{arr}[i-1]

XOR both sides:

text{pref}[i] oplus text{pref}[i-1] = text{arr}[i]

This is the XOR analog of prefix sum difference: just as `arr[i] = prefixSum[i] - prefixSum[i-1]` for addition, we have `arr[i] = pref[i] ^ pref[i-1]` for XOR.

Base case: `arr[0] = pref[0]`.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 90" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Bit manipulation</text>

  <text x="40" y="50" font-family="monospace" font-size="14" fill="#3A3530">1 0 1 1 0 1 0</text>
  <text x="40" y="75" font-size="11" fill="#6B6560">XOR pairs · masks · shifts</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **XOR tricks** *(this problem)* | O(n) | O(1) | Single number, swap without temp |
| Bit masks | O(2^n) | O(n) | Subset enumeration |
| Brian Kernighan | O(\log n) | O(1) | Count set bits |
| Shift operations | O(n) | O(1)$ | Power of two, divide by 2 |

## Solution

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

### Solution Explanation

**Approach:** XOR tricks (this problem)

**Key idea:** ### XOR Prefix Sum Property

**Walkthrough** — input `pref = [5,2,0,3,1]`, expected output `[5,7,2,3,2]`:

pref[0] = 5             → arr[0] = 5
  pref[1] = 5 ^ 7 = 2    → arr[1] = 7
  pref[2] = 5 ^ 7 ^ 2 = 0 → arr[2] = 2
  ...
## Common Mistakes

- Processing left-to-right in-place (corrupts values needed for later computations)
- Forgetting the base case `arr[0] = pref[0]`

## Key Takeaways

- **XOR prefix ↔ original array** mirrors **addition prefix sum ↔ difference array**, with XOR replacing both addition and subtraction (since `a ^ a = 0`)
- In-place reverse pass avoids the dependency issue cleanly
- XOR is its own inverse: `a ^ b ^ b = a` -- this self-inverse property underpins all XOR prefix problems

## Related Problems

- [260. Single Number III](https://www.leetcode.com/problems/single-number-iii/) -- XOR partitioning
- [136. Single Number](https://www.leetcode.com/problems/single-number/) -- XOR cancellation
- [389. Find the Difference](https://www.leetcode.com/problems/find-the-difference/) -- XOR to find extra element
- [303. Range Sum Query](https://www.leetcode.com/problems/range-sum-query-immutable/) -- addition prefix sum analog

## References

- [LC 2433: Find The Original Array of Prefix Xor on LeetCode](https://www.leetcode.com/problems/find-the-original-array-of-prefix-xor/)
- [LeetCode Discuss — LC 2433: Find The Original Array of Prefix Xor](https://www.leetcode.com/problems/find-the-original-array-of-prefix-xor/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-the-original-array-of-prefix-xor/editorial/) *(may require premium)*

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
