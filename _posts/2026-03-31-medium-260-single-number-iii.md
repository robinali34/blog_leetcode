---
layout: post
title: "LeetCode 260. Single Number III"
date: 2026-03-31
categories: [leetcode, medium, bit-manipulation]
tags: [leetcode, medium, bit-manipulation, xor]
permalink: /2026/03/31/medium-260-single-number-iii/
---

Given an integer array `nums` where **exactly two** elements appear once and all other elements appear exactly twice, find the two elements that appear only once. Return them in any order. Your algorithm should run in linear time and constant space.

## Examples

**Example 1:**

```
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
```

**Example 2:**

```
Input: nums = [-1,0]
Output: [-1,0]
```

**Example 3:**

```
Input: nums = [0,1]
Output: [1,0]
```

## Constraints

- `2 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Exactly two elements appear once; all others appear twice

## Thinking Process

### Step 1: XOR Everything

XOR all elements. Paired elements cancel out (`a ^ a = 0`), leaving `x = a ^ b` where `a` and `b` are the two unique numbers.

But `x` is the XOR of both -- how do we separate `a` and `b`?

### Step 2: Find a Distinguishing Bit

Since `a != b`, at least one bit differs between them. In `x = a ^ b`, every `1` bit is a position where `a` and `b` differ.

We only need **one** such bit. The trick `x & (-x)` isolates the **lowest set bit**:

```
x    = 0110  (a ^ b)
-x   = 1010  (two's complement)
x&-x = 0010  ← lowest 1-bit
```

### Step 3: Split into Two Groups

Use this distinguishing bit `diff` to partition all numbers into two groups:
- Group 1: numbers with that bit **set**
- Group 2: numbers with that bit **clear**

Since `a` and `b` differ at this bit, they land in **different groups**. Paired elements always land in the **same group** (they're identical). XOR within each group gives the unique element.

### Walk-through

```
nums = [1, 2, 1, 3, 2, 5]

Step 1: x = 1^2^1^3^2^5 = 3^5 = 6 (binary: 110)

Step 2: diff = 6 & (-6) = 6 & ...1010 = 010 (bit 1)

Step 3: Partition by bit 1:
  bit 1 set:   2, 3, 2  → XOR = 3  (a)
  bit 1 clear: 1, 1, 5  → XOR = 5  (b)

Answer: [3, 5] ✓
```

## Solution: XOR + Bit Partitioning -- $O(n)$ time, $O(1)$ space

{% raw %}
```cpp
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int x = 0;
        for (int num : nums) x ^= num;
        unsigned int diff = x & (-x);
        int a = 0, b = 0;
        for (int num : nums) {
            if (num & diff) a ^= num;
            else b ^= num;
        }
        return {a, b};
    }
};
```
{% endraw %}

**Time**: $O(n)$ -- two passes
**Space**: $O(1)$

## Why `x & (-x)` Works

In two's complement, `-x = ~x + 1`. This flips all bits and adds 1, which propagates through the trailing zeros and flips the lowest `1` bit's position. The AND with the original isolates exactly that bit:

```
x    = 1010 1100
~x   = 0101 0011
~x+1 = 0101 0100  (-x)
x&-x = 0000 0100  ← lowest set bit
```

## Single Number Family

| Problem | Constraint | Technique |
|---|---|---|
| 136 Single Number | One unique, rest appear twice | XOR all |
| **260 Single Number III** | **Two unique, rest appear twice** | **XOR + bit partition** |
| 137 Single Number II | One unique, rest appear three times | Bit counting mod 3 |

## Common Mistakes

- Trying to use a hash map (works but violates the $O(1)$ space requirement)
- Using any bit of `x` other than a set bit to partition (a `0` bit means `a` and `b` agree there -- useless for splitting)
- Integer overflow: `x & (-x)` can overflow if `x = INT_MIN`; using `unsigned` or `x & (unsigned)(-x)` is safer

## Key Takeaways

- **"Two unique elements among pairs"** = XOR all → find distinguishing bit → partition → XOR each group
- `x & (-x)` to isolate the lowest set bit is a fundamental bit trick
- This extends the Single Number pattern: one pass to combine, one pass to separate

## Related Problems

- [136. Single Number](https://leetcode.com/problems/single-number/) -- one unique element (simpler)
- [137. Single Number II](https://leetcode.com/problems/single-number-ii/) -- triples instead of pairs
- [389. Find the Difference](https://leetcode.com/problems/find-the-difference/) -- XOR to find extra element
- [268. Missing Number](https://leetcode.com/problems/missing-number/) -- XOR with indices

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
