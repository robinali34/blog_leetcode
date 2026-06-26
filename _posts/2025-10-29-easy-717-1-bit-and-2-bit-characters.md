---
layout: post
title: "[Easy] 717. 1-bit and 2-bit Characters"
date: 2025-10-29 00:00:00 -0700
categories: leetcode easy array parsing
permalink: /posts/2025-10-29-easy-717-1-bit-and-2-bit-characters/
tags: [leetcode, easy, array, parsing]
---
Given a binary array `bits` that ends with `0`, determine whether the last character must be a 1-bit character.

- A 1-bit character is `0`
- A 2-bit character is `10` or `11`

Parse from left to right and check whether the final `0` stands alone as a 1-bit character.

## Examples

**Example 1:**

```
Input: bits = [1,0,0]
Output: true
Explanation: Parse "10" then the final "0" is a lone 1-bit character.
```

**Example 2:**

```
Input: bits = [1,1,1,0]
Output: false
Explanation: Parse "11" then "10" — the final 0 is part of a 2-bit character.
```

## Constraints

- `1 <= bits.length <= 1000`
- `bits[i]` is `0` or `1`
- `bits[bits.length - 1]` is `0`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Prefix sum** *(this problem)* | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| Hash map counting | O(n) | O(n) | Frequency, two-sum variants |

## Thinking Process

Simulate parsing without building characters:

- From index `i`, if `bits[i] == 1`, the next two bits form one character → advance by 2
- If `bits[i] == 0`, advance by 1
- Stop before the last index (`i < n - 1`) so we can tell whether the final bit is consumed as part of a pair

If we land exactly on `n - 1`, the last `0` was never paired → **true**. If we reach `n`, the last `0` was consumed as the second bit of `10` → **false**.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Solution — O(n) time, O(1) space

```cpp
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int n = (int)bits.size();
        int i = 0;
        while (i < n - 1) {
            i += (bits[i] == 1 ? 2 : 1);
        }
        return i == n - 1;
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** Simulate parsing without building characters:

**How the code works:**
- From index `i`, if `bits[i] == 1`, the next two bits form one character → advance by 2
- If `bits[i] == 0`, advance by 1
- Stop before the last index (`i < n - 1`) so we can tell whether the final bit is consumed as part of a pair

**Walkthrough** — input `bits = [1,0,0]`, expected output `true`:

Parse "10" then the final "0" is a lone 1-bit character.

**Time:** O(n) · **Space:** O(1)
## Common Mistakes

- Looping while `i < n` instead of `i < n - 1` — can overshoot and misread the last character
- Treating `1` as a standalone 1-bit character (only `0` is 1-bit)
- Not using the guarantee that the array ends in `0`

## Key Takeaways

- **Greedy linear scan** with a variable step size (`+1` or `+2`) handles encoding rules without explicit decoding
- The loop bound `i < n - 1` is the key insight — same pattern appears in string decoding problems

## Related Problems

- [394. Decode String](https://www.leetcode.com/problems/decode-string/)
- [809. Expressive Words](https://www.leetcode.com/problems/expressive-words/)

## References

- [LC 717: 1-bit and 2-bit Characters on LeetCode](https://www.leetcode.com/problems/1-bit-and-2-bit-characters/)
- [LeetCode Discuss — LC 717: 1-bit and 2-bit Characters](https://www.leetcode.com/problems/1-bit-and-2-bit-characters/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/1-bit-and-2-bit-characters/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
