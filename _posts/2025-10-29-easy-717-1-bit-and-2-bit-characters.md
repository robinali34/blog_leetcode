---
layout: post
title: "LC 717: 1-bit and 2-bit Characters"
date: 2025-10-29 00:00:00 -0700
categories: leetcode easy array parsing
permalink: /posts/2025-10-29-easy-717-1-bit-and-2-bit-characters/
tags: [leetcode, easy, array, parsing]
---

# LC 717: 1-bit and 2-bit Characters

Given a binary array `bits` that ends with `0`, determine whether the last character must be a 1‑bit character.

- A 1‑bit character is represented by `0`
- A 2‑bit character is represented by `10` or `11`

We need to parse from left to right using the encoding rules and check if the last parsed character is the single `0` at the end.

## Key Idea

Walk the array from left to right. If we see `1`, we must consume two bits (`10` or `11`). If we see `0`, we consume one bit. We stop before the last index and see if we land exactly on the last index at the end.

- While `i < n - 1`: advance `i += (bits[i] == 1 ? 2 : 1)`
- If we stop with `i == n - 1`, the last character is 1‑bit (`0`) → return true
- If we stop with `i == n`, the last character was a 2‑bit that consumed the final `0` → return false

## C++ Solution

```cpp
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int n = (int)bits.size();
        int i = 0;
        // Parse until we reach or pass the last index
        while (i < n - 1) {
            i += (bits[i] == 1 ? 2 : 1);
        }
        return i == n - 1;
    }
};
```

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Character encoding**: What are 1-bit and 2-bit characters? (Assumption: 1-bit character is '0', 2-bit character is '10' or '11' - encoding rules)

2. **Last character**: What are we checking? (Assumption: Whether the last character is a 1-bit character - ends with '0')

3. **Return value**: What should we return? (Assumption: Boolean - true if last character is 1-bit, false if 2-bit)

4. **Parsing rules**: How do we parse the bits? (Assumption: Parse left to right - if bit is 1, it's start of 2-bit character, if 0, it's 1-bit character)

5. **Valid encoding**: Is the encoding guaranteed valid? (Assumption: Yes - bits form valid sequence of 1-bit and 2-bit characters)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Parse the entire array from left to right, tracking which characters we've consumed. When we reach the end, check if the last consumed character was 1-bit or 2-bit. This requires maintaining state about parsing progress, which can be complex.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use a pointer that moves through the array. If current bit is 1, consume 2 bits (2-bit character). If current bit is 0, consume 1 bit (1-bit character). Track the position and check if we end exactly at the last element (1-bit) or go past it (2-bit). This works but requires careful pointer management.

**Step 3: Optimized Solution (5 minutes)**

Use a simple observation: parse from left to right. If we encounter 1, it must be a 2-bit character, so skip 2 positions. If we encounter 0, it's a 1-bit character, so skip 1 position. If we end exactly at the last index (bits.length - 1), the last character is 1-bit. If we would go past the end, the last character is 2-bit. Alternatively, check if the second-to-last bit is 1: if bits[n-2] == 1, then bits[n-2] and bits[n-1] form a 2-bit character, so last is 2-bit. Otherwise, last is 1-bit. This achieves O(n) time with O(1) space, which is optimal.

## Complexity

- Time: O(n) — single pass
- Space: O(1)

## Examples

- `bits = [1,0,0]` → parse `10` (i=2), last index is 2, which is `0` → true
- `bits = [1,1,1,0]` → parse `11` (i=2), then `10` (i=4==n) → false
