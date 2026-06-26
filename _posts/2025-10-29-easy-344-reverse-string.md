---
layout: post
title: "[Easy] 344. Reverse String"
date: 2025-10-29 00:00:00 -0700
categories: leetcode easy two-pointers string
permalink: /posts/2025-10-29-easy-344-reverse-string/
tags: [leetcode, easy, two-pointers, string]
---
Reverse the array of characters `s` in-place using O(1) extra memory.

> **Pattern:** Two Pointers · **Template:** [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)

## Examples

**Example 1:**

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:**

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Thinking Process

In-place reversal is a classic **two-pointer** pattern: swap the characters at the ends, then move inward until the pointers meet.

- `left` starts at 0, `right` at `n - 1`
- While `left < right`, swap `s[left]` and `s[right]`, then increment `left` and decrement `right`
- No extra array needed — each swap fixes two positions

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Solution — O(n) time, O(1) space

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0, right = (int)s.size() - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            ++left;
            --right;
        }
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** In-place reversal is a classic **two-pointer** pattern: swap the characters at the ends, then move inward until the pointers meet.

**How the code works:**
- `left` starts at 0, `right` at `n - 1`
- While `left < right`, swap `s[left]` and `s[right]`, then increment `left` and decrement `right`
- No extra array needed — each swap fixes two positions

**Walkthrough** — input `s = ["h","e","l","l","o"]`, expected output `["o","l","l","e","h"]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

**Time:** O(n) · **Space:** O(1)
## Common Mistakes

- Using `left <= right` and swapping the middle element twice (use `left < right`)
- Allocating a second array — violates the in-place constraint
- Forgetting that `s` is modified in place (return type is `void`)

## Key Takeaways

- **Opposite-end two pointers** is the standard template for in-place reversal (arrays, strings, linked lists)
- Same idea extends to [LC 345. Reverse Vowels of a String](https://www.leetcode.com/problems/reverse-vowels-of-a-string/) and partial reversals like [LC 541. Reverse String II](https://www.leetcode.com/problems/reverse-string-ii/)

## Related Problems

- [345. Reverse Vowels of a String](https://www.leetcode.com/problems/reverse-vowels-of-a-string/)
- [541. Reverse String II](https://www.leetcode.com/problems/reverse-string-ii/)
- [206. Reverse Linked List](https://www.leetcode.com/problems/reverse-linked-list/)

## References

- [LC 344: Reverse String on LeetCode](https://www.leetcode.com/problems/reverse-string/)
- [LeetCode Discuss — LC 344: Reverse String](https://www.leetcode.com/problems/reverse-string/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/reverse-string/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
