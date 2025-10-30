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

## Complexity

- Time: O(n) — single pass
- Space: O(1)

## Examples

- `bits = [1,0,0]` → parse `10` (i=2), last index is 2, which is `0` → true
- `bits = [1,1,1,0]` → parse `11` (i=2), then `10` (i=4==n) → false
