---
layout: post
title: "[Easy] 349. Intersection of Two Arrays"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, array, hash-table]
permalink: /2026/01/19/easy-349-intersection-of-two-arrays/
tags: [leetcode, easy, array, hash-table, two-pointers, sorting]
---
Given two integer arrays `nums1` and `nums2`, return an array of their **intersection**. Each element in the result must be **unique** and you may return the result in **any order**.

## Examples

**Example 1:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Explanation: The intersection contains only the element 2.
```

**Example 2:**
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4] or [4,9]
Explanation: The intersection contains elements 9 and 4. Order does not matter.
```

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Thinking Process

1. **Hash Set for Uniqueness**: Automatically handles duplicates

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
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Solution

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> seen(nums1.begin(), nums1.end());
        vector<int> rtn;
        for(int num: nums2) {
            if(seen.contains(num)) {
                rtn.emplace_back(num);
                seen.erase(num);
            }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** 1. **Hash Set for Uniqueness**: Automatically handles duplicates

**How the code works:**
1. **Hash Set for Uniqueness**: Automatically handles duplicates
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `nums1 = [1,2,2,1], nums2 = [2,2]`, expected output `[2]`:

The intersection contains only the element 2.
## Common Mistakes

1. **No intersection**: `nums1 = [1,2,3]`, `nums2 = [4,5,6]` → `[]`
2. **Complete overlap**: `nums1 = [1,2,3]`, `nums2 = [1,2,3]` → `[1,2,3]`
3. **One array empty**: `nums1 = []`, `nums2 = [1,2]` → `[]`
4. **Duplicates in both**: `nums1 = [1,1,2,2]`, `nums2 = [2,2]` → `[2]`
5. **Single element**: `nums1 = [1]`, `nums2 = [1]` → `[1]`

1. **Not removing from set**: Results in duplicate elements in output
2. **Using vector instead of set**: Doesn't handle duplicates in `nums1`
3. **Wrong comparison**: Comparing entire arrays instead of elements
4. **Forgetting empty check**: Not handling empty arrays
5. **Order dependency**: Trying to maintain order when not needed

## Related Problems

- [LC 350: Intersection of Two Arrays II](https://www.leetcode.com/problems/intersection-of-two-arrays-ii/) - Allow duplicates in result
- [LC 349: Intersection of Two Arrays](https://www.leetcode.com/problems/intersection-of-two-arrays/) - Unique elements only (this problem)
- [LC 1002: Find Common Characters](https://www.leetcode.com/problems/find-common-characters/) - Find common characters in strings
- [LC 1213: Intersection of Three Sorted Arrays](https://www.leetcode.com/problems/intersection-of-three-sorted-arrays/) - Three arrays intersection
- [LC 2248: Intersection of Multiple Arrays](https://www.leetcode.com/problems/intersection-of-multiple-arrays/) - Multiple arrays intersection

## Key Takeaways

1. **Hash Set for Uniqueness**: Automatically handles duplicates
2. **Erase After Add**: Prevents duplicate results efficiently
3. **Order Independence**: Can return result in any order
4. **Space-Time Trade-off**: Hash set uses more space but provides O(1) lookup

## References

- [LC 349: Intersection of Two Arrays on LeetCode](https://www.leetcode.com/problems/intersection-of-two-arrays/)
- [LeetCode Discuss — LC 349: Intersection of Two Arrays](https://www.leetcode.com/problems/intersection-of-two-arrays/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/intersection-of-two-arrays/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
