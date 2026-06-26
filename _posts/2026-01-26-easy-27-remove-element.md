---
layout: post
title: "[Easy] 27. Remove Element"
date: 2026-01-26 00:00:00 -0700
categories: [leetcode, easy, array, two-pointers]
permalink: /2026/01/26/easy-27-remove-element/
tags: [leetcode, easy, array, two-pointers, in-place]
---
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return *the number of elements in* `nums` *which are not equal to* `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The elements beyond the first `k` elements are not important as well as the size of `nums`.
- Return `k`.

## Examples

**Example 1:**

```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**

```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 3, 0, and 4.
Note that the five elements can be returned in any order, and it does not matter what you leave beyond the returned k.
```

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Thinking Process

1. **Two Pointers Pattern**: Classic pattern for in-place array modification

- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.



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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Opposite ends** *(this problem)* | $O(n)$ | $O(1)$ | Sorted array pair search, reversal |
| Slow / fast pointers | $O(n)$ | $O(1)$ | Linked list middle, cycle detection |
| Same-direction chase | $O(n)$ | $O(1)$ | Remove duplicates in-place |
| Sliding window (variable) | $O(n)$ | $O(1)$ | Subarray with constraint |

## Solution

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int last = 0;
        for(int curr = 0; curr < (int)nums.size(); curr++) {
            if(nums[curr] != val) {
                nums[last] = nums[curr];
                last += 1;
            }
        }
        return last;
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** 1. **Two Pointers Pattern**: Classic pattern for in-place array modification

**How the code works:**
1. **Two Pointers Pattern**: Classic pattern for in-place array modification
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `nums = [3,2,2,3], val = 3`, expected output `2, nums = [2,2,_,_]`:

Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
## Common Mistakes

1. **Empty array**: `nums = []` → return `0`
2. **All elements removed**: `nums = [3,3,3]`, `val = 3` → return `0`
3. **No elements removed**: `nums = [1,2,3]`, `val = 4` → return `3`
4. **Single element removed**: `nums = [1]`, `val = 1` → return `0`
5. **Single element kept**: `nums = [1]`, `val = 2` → return `1`

1. **Wrong pointer logic**: Incrementing `last` even when element equals `val`
2. **Index out of bounds**: Not checking bounds when accessing `nums[curr]`
3. **Wrong return value**: Returning `nums.size()` instead of `last`
4. **Not modifying array**: Only counting without actually removing elements
5. **Type casting**: Forgetting `(int)` cast for `nums.size()` comparison

## Related Problems

- [LC 26: Remove Duplicates from Sorted Array](https://www.leetcode.com/problems/remove-duplicates-from-sorted-array/) - Similar two pointers pattern
- [LC 283: Move Zeroes](https://www.leetcode.com/problems/move-zeroes/) - Move zeros to end
- [LC 80: Remove Duplicates from Sorted Array II](https://www.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) - Allow at most 2 duplicates
- [LC 203: Remove Linked List Elements](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-easy-203-remove-linked-list-elements/) - Similar problem on linked list

## Key Takeaways

1. **Two Pointers Pattern**: Classic pattern for in-place array modification
2. **Write Pointer (`last`)**: Tracks where to write next valid element
3. **Read Pointer (`curr`)**: Scans through all elements
4. **In-Place**: No extra space needed, modifies array directly
5. **Order Preservation**: Maintains relative order of non-removed elements

## References

- [LC 27: Remove Element on LeetCode](https://www.leetcode.com/problems/remove-element/)
- [LeetCode Discuss — LC 27: Remove Element](https://www.leetcode.com/problems/remove-element/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/remove-element/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
