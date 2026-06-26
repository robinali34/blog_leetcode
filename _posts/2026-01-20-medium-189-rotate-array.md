---
layout: post
title: "[Medium] 189. Rotate Array"
date: 2026-01-20 00:00:00 -0700
categories: [leetcode, medium, array]
permalink: /2026/01/20/medium-189-rotate-array/
tags: [leetcode, medium, array, rotation, two-pointers]
---
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^9`

## Thinking Process

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

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

This solution rotates the array by 1 step, `k` times.

```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        int temp, previous;
        for (int i = 0; i < k; i++) {
            previous = nums[nums.size() - 1];
            for (int j = 0; j < nums.size(); j++) {
                temp = nums[j];
                nums[j] = previous;
                previous = temp;
            }
        }
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**How the code works:**
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `nums = [1,2,3,4,5,6,7], k = 3`, expected output `[5,6,7,1,2,3,4]`:

rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

- **Time Complexity:** O(n × k) — For each of the `k` steps, we traverse `n` elements.
- **Space Complexity:** O(1) — Only a few extra variables.

This approach is simple but can be too slow when `k` and `n` are large.
## Edge Cases

1. `k = 0` → Array remains unchanged.
2. `k` multiple of `n` → Array remains unchanged after normalization with `k %= n`.
3. Single element array → Always unchanged.
4. Large `k` (e.g., `k > n`) → Handled by `k %= n`.

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [LC 61. Rotate List](https://www.leetcode.com/problems/rotate-list/)
- [LC 189. Rotate Array](https://www.leetcode.com/problems/rotate-array/) — This problem
- [LC 396. Rotate Function](https://www.leetcode.com/problems/rotate-function/)

## Key Takeaways

- **Pattern:** Opposite ends (this problem)
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.

## References

- [LC 189: Rotate Array on LeetCode](https://www.leetcode.com/problems/rotate-array/)
- [LeetCode Discuss — LC 189: Rotate Array](https://www.leetcode.com/problems/rotate-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/rotate-array/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
