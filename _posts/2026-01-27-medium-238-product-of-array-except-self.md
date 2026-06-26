---
layout: post
title: "[Medium] 238. Product of Array Except Self"
date: 2026-01-27 00:00:00 -0700
categories: [leetcode, medium, array, prefix-sum, two-pointers]
permalink: /2026/01/27/medium-238-product-of-array-except-self/
tags: [leetcode, medium, array, prefix-sum, two-pointers]
---
Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operator.

## Thinking Process

1. **Two Arrays Approach**: Use separate arrays for left and right products for clarity

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

## Examples

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a **32-bit** integer.

## Space-Optimized Solution

We can optimize space by using the output array itself to store left products, then building right products on the fly:

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> answer(len, 1);
        
        // Build left products in answer array
        for (int i = 1; i < len; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }
        
        // Build right products on the fly and multiply
        int right = 1;
        for (int i = len - 1; i >= 0; i--) {
            answer[i] *= right;
            right *= nums[i];
        }
        
        return answer;
    }
};
```

**Space Complexity:** O(1) extra space (excluding output array)

## Common Mistakes

1. **Two elements**: `nums = [2, 3]` → `answer = [3, 2]`
2. **Contains zero**: `nums = [-1,1,0,-3,3]` → `answer = [0,0,9,0,0]`
3. **All same**: `nums = [2,2,2]` → `answer = [4,4,4]`
4. **Negative numbers**: `nums = [-1,2,-3,4]` → `answer = [24,-12,8,-6]`
5. **Single zero**: `nums = [1,0,3,4]` → `answer = [0,12,0,0]`

1. **Using division**: `answer[i] = totalProduct / nums[i]` fails with zeros
2. **Wrong initialization**: Forgetting to set `L[0] = 1` and `R[len-1] = 1`
3. **Index off-by-one**: Confusing left/right boundaries
4. **Integer overflow**: Not considering product might exceed 32-bit (but constraints guarantee it won't)
5. **Space optimization**: Not realizing we can use output array for left products

## Comparison with Alternative Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Left/Right Arrays** | O(n) | O(n) | Clear and intuitive |
| **Space-Optimized** | O(n) | O(1) | Uses output array |
| **Division (Invalid)** | O(n) | O(1) | Fails with zeros |

## Related Problems

- [LC 42: Trapping Rain Water](https://www.leetcode.com/problems/trapping-rain-water/) - Similar left/right pass pattern
- [LC 135: Candy](https://www.leetcode.com/problems/candy/) - Left and right passes
- [LC 2256: Minimum Average Difference](https://www.leetcode.com/problems/minimum-average-difference/) - Prefix and suffix sums
- [LC 724: Find Pivot Index](https://www.leetcode.com/problems/find-pivot-index/) - Left and right sums

## Key Takeaways

1. **Two Arrays Approach**: Use separate arrays for left and right products for clarity

2. **Space Optimization**: Can use output array to store left products, then build right products on the fly

3. **No Division**: Avoids division operator, which would fail with zeros

4. **Handles Zeros**: Works correctly even when array contains zeros

5. **Prefix/Suffix Products**: Similar to prefix sum, but with multiplication

## References

- [LC 238: Product of Array Except Self on LeetCode](https://www.leetcode.com/problems/product-of-array-except-self/)
- [LeetCode Discuss — LC 238: Product of Array Except Self](https://www.leetcode.com/problems/product-of-array-except-self/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/product-of-array-except-self/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
