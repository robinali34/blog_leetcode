---
layout: post
title: "[Medium] 324. Wiggle Sort II"
date: 2025-11-04 22:30:02 -0800
categories: leetcode algorithm medium cpp arrays nth-element three-way-partition index-mapping problem-solving
permalink: /posts/2025-11-04-medium-324-wiggle-sort-ii/
tags: [leetcode, medium, array, wiggle, nth_element, partition]
---
Rearrange `nums` such that `nums[0] < nums[1] > nums[2] < nums[3] ...` (wiggle order).

## Examples

**Example:**
```
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: 1 < 6 > 1 < 5 > 1 < 4
```

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`

## Thinking Process

- `nth_element` finds the median in average O(n) time
- 3-way partition handles duplicates correctly
- Virtual indexing avoids overwriting placements by distributing indices across the array cyclically



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Prefix sum | $O(n)$ | $O(n)$ | Range queries, subarray sum |
| **Sort + scan** *(this problem)* | $O(n \log n)$ | $O(1)$ | Intervals, meeting rooms |
| Kadane's algorithm | $O(n)$ | $O(1)$ | Maximum subarray |
| Hash map counting | $O(n)$ | $O(n)$ | Frequency, two-sum variants |

## Solution

**Time Complexity:** O(n) average (due to `nth_element`)  
**Space Complexity:** O(1) extra

Steps:
- Find the median in-place using `nth_element` (average O(n))
- Use a 3-way partition (Dutch National Flag) around the median
- Apply a virtual index mapping `vi(i) = (1 + 2*i) % (n | 1)` so that larger numbers go to odd indices and smaller ones to even indices, achieving wiggle order

```cpp
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        const int n = nums.size();
        auto midIt = nums.begin() + n / 2;
        nth_element(nums.begin(), midIt, nums.end());
        int median = *midIt;

        auto vi = [n](int i) {return (1 + 2 * i) % (n | 1);};
        int left = 0, right = n - 1, i = 0;
        while(i <= right) {
            if(nums[vi(i)] > median) {
                swap(nums[vi(left)], nums[vi(i)]);
                left++;
                i++;
            } else if(nums[vi(i)] < median) {
                swap(nums[vi(i)], nums[vi(right)]);
                right--;
            } else {
                i++;
            }
        }
    }
};
```

### Solution Explanation

**Approach:** Sort + scan (this problem)

**Key idea:** `nth_element` finds the median in average O(n) time

**How the code works:**
- `nth_element` finds the median in average O(n) time
- 3-way partition handles duplicates correctly
- Virtual indexing avoids overwriting placements by distributing indices across the array cyclically
## Why Virtual Indexing Works

- The mapping `vi(i) = (1 + 2*i) % (n | 1)` interleaves indices so that large elements are placed at positions 1, 3, 5, ... and small elements at 0, 2, 4, ...
- Partitioning by median ensures elements greater than median occupy odd positions, and elements less than median occupy even positions, satisfying wiggle constraints.

## Edge Cases

- All elements equal → already wiggle (no swaps needed)
- Many duplicates → 3-way partition around median is essential
- Small arrays (n <= 2) → already satisfy or trivially adjustable

## Related Problems

- [280. Wiggle Sort] — simpler version without strict inequality
- [75. Sort Colors] — Dutch National Flag
- [215. Kth Largest Element in an Array] — `nth_element`

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

- `nth_element` finds the median in average O(n) time
- 3-way partition handles duplicates correctly
- Virtual indexing avoids overwriting placements by distributing indices across the array cyclically

## References

- [LC 324: Wiggle Sort II on LeetCode](https://www.leetcode.com/problems/wiggle-sort-ii/)
- [LeetCode Discuss — LC 324: Wiggle Sort II](https://www.leetcode.com/problems/wiggle-sort-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/wiggle-sort-ii/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
