---
layout: post
title: "[Medium] 33. Search in Rotated Sorted Array"
date: 2025-09-23 10:00:00 -0000
categories: [leetcode, medium, binary-search, array]
tags: [leetcode, medium, binary-search, array, search]
permalink: /posts/2025-09-23-medium-33-search-in-rotated-sorted-array/
---
There is an integer array `nums` sorted in ascending order (with distinct values), rotated at an unknown pivot. Given `nums` and `target`, return the index of `target` or `-1` if it is not in `nums`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Examples

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:**

```
Input: nums = [1], target = 0
Output: -1
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**
- `nums` is rotated at some pivot
- `-10^4 <= target <= 10^4`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Standard binary search | $O(\log n)$ | $O(1)$ | Only if array is not rotated |
| **Modified BS (sorted half)** | $O(\log n)$ | $O(1)$ | **This problem** — discard half each step |
| Find pivot + BS | $O(\log n)$ | $O(1)$ | Locate rotation index, then two BS calls |
| Linear scan | $O(n)$ | $O(1)$ | Violates the $O(\log n)$ requirement |

## Thinking Process

Even after rotation, **at least one half** of the array (left or right of `mid`) remains sorted.

1. Compute `mid`. If `nums[mid] == target`, return `mid`.
2. If the **left half** `[left … mid]` is sorted (`nums[left] <= nums[mid]`):
   - Target lies in that sorted half iff `nums[left] <= target < nums[mid]` → shrink right; else shrink left.
3. Otherwise the **right half** is sorted:
   - Target lies there iff `nums[mid] < target <= nums[right]` → shrink left; else shrink right.

This is the same binary-search loop — only the “which half to discard?” rule changes.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Rotated sorted array</text>

  <text x="20" y="35" font-size="11" fill="#6B6560">sorted half</text>
  <rect x="20" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="38" y="60" text-anchor="middle" font-size="11">4</text>
  <rect x="46" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="64" y="60" text-anchor="middle" font-size="11">5</text>
  <rect x="82" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="60" text-anchor="middle" font-size="11">6</text>
  <rect x="118" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="136" y="60" text-anchor="middle" font-size="11">7</text>
  <text x="160" y="35" font-size="11" fill="#A08888">pivot</text>
  <rect x="154" y="42" width="36" height="28" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/><text x="172" y="60" text-anchor="middle" font-size="11">0</text>
  <rect x="190" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="208" y="60" text-anchor="middle" font-size="11">1</text>
  <rect x="226" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="244" y="60" text-anchor="middle" font-size="11">2</text>
  <text x="140" y="95" text-anchor="middle" font-size="11" fill="#5A5752">One half is always sorted → BS on that half</text>

</svg>

## Solution — $O(\log n)$ time, $O(1)$ space

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = (int)nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;

            if (nums[mid] >= nums[left]) {
                // Left half is sorted
                if (target >= nums[left] && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            } else {
                // Right half is sorted
                if (target > nums[mid] && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }
        return -1;
    }
};
```

### Solution Explanation

**Why one half is always sorted:** In a rotated sorted array, walking from `left` to `mid` either stays inside the original ascending segment or crosses the pivot. If `nums[mid] >= nums[left]`, no pivot lies between `left` and `mid`, so that segment is sorted. Otherwise the pivot is in the left part, so the right segment `[mid … right]` must be sorted.

**Discard logic:** On a sorted segment, binary search tells you whether `target` can exist there (compare `target` to segment bounds). If yes, search that half; if no, search the other half.

**Walkthrough** — `nums = [4,5,6,7,0,1,2]`, `target = 0`:

| Step | left | right | mid | nums[mid] | Sorted half | Action |
|------|------|-------|-----|-----------|-------------|--------|
| 1 | 0 | 6 | 3 | 7 | left [4,5,6,7] | 0 not in [4,7) → `left = 4` |
| 2 | 4 | 6 | 5 | 1 | left [0,1] | 0 in [0,1) → `right = 4` |
| 3 | 4 | 4 | 4 | 0 | — | found at index 4 |

**Time:** $O(\log n)$ — halve search space each iteration · **Space:** $O(1)$

## Common Mistakes

- Using `nums[mid] > nums[left]` instead of `>=` — fails when `left == mid` (single-element half)
- Checking `target` against `nums[right]` when the left half is sorted (compare against the sorted half only)
- Forgetting distinct values — with duplicates use [LC 81](https://www.leetcode.com/problems/search-in-rotated-sorted-array-ii/)

## Key Takeaways

- Rotated sorted array = **modified binary search**, not a new algorithm
- Ask: “Which side is sorted?” then apply normal BS range checks on that side
- Same template covers [LC 81](https://www.leetcode.com/problems/search-in-rotated-sorted-array-ii/) (with duplicates) and [LC 153](https://www.leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Related Problems

- [81. Search in Rotated Sorted Array II](https://www.leetcode.com/problems/search-in-rotated-sorted-array-ii/) — duplicates allowed
- [153. Find Minimum in Rotated Sorted Array](https://www.leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](https://www.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
- [34. Find First and Last Position](https://www.leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## References

- [LC 33: Search in Rotated Sorted Array on LeetCode](https://www.leetcode.com/problems/search-in-rotated-sorted-array/)
- [LeetCode Discuss — LC 33](https://www.leetcode.com/problems/search-in-rotated-sorted-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/search-in-rotated-sorted-array/editorial/) *(may require premium)*

## Template Reference

- [Search / Binary Search](/blog_leetcode/posts/2026-01-20-leetcode-templates-search/)
