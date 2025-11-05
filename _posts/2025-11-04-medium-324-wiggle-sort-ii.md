---
layout: post
title: "[Medium] 324. Wiggle Sort II"
date: 2025-11-04 22:30:02 -0800
categories: leetcode algorithm medium cpp arrays nth-element three-way-partition index-mapping problem-solving
permalink: /posts/2025-11-04-medium-324-wiggle-sort-ii/
tags: [leetcode, medium, array, wiggle, nth_element, partition]
---

# [Medium] 324. Wiggle Sort II

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

## Solution: Median + 3-way Partition with Virtual Indexing

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

## Why Virtual Indexing Works

- The mapping `vi(i) = (1 + 2*i) % (n | 1)` interleaves indices so that large elements are placed at positions 1, 3, 5, ... and small elements at 0, 2, 4, ...
- Partitioning by median ensures elements greater than median occupy odd positions, and elements less than median occupy even positions, satisfying wiggle constraints.

## Key Insights

- `nth_element` finds the median in average O(n) time
- 3-way partition handles duplicates correctly
- Virtual indexing avoids overwriting placements by distributing indices across the array cyclically

## Edge Cases

- All elements equal → already wiggle (no swaps needed)
- Many duplicates → 3-way partition around median is essential
- Small arrays (n <= 2) → already satisfy or trivially adjustable

## Related Problems

- [280. Wiggle Sort] — simpler version without strict inequality
- [75. Sort Colors] — Dutch National Flag
- [215. Kth Largest Element in an Array] — `nth_element`

