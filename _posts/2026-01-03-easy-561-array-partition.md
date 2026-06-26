---
layout: post
title: "[Easy] 561. Array Partition"
date: 2026-01-03 07:00:00 -0700
categories: [leetcode, easy, array, greedy, sorting]
permalink: /2026/01/03/easy-561-array-partition/
---
Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `min(ai, bi)` for all `i` is **maximized**. Return *the maximized sum*.

## Examples

**Example 1:**
```
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1,4) + min(2,3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1,3) + min(2,4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1,2) + min(3,4) = 1 + 3 = 4
So the maximum possible sum is 4.
```

**Example 2:**
```
Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
```

## Constraints

- `1 <= n <= 10^4`
- `nums.length == 2 * n`
- `-10^4 <= nums[i] <= 10^4`

## Thinking Process

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `min(ai, bi)` for all `i` is **maximized**. Return *the maximized sum*.

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

## Solution

### **Solution: Greedy with Sorting**

```cpp
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int sum = 0;
        for(int i = 0; i < (int)nums.size(); i += 2) {
            sum += nums[i];
        }
        return sum;
    }
};
```

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `min(ai, bi)` for all `i` is **maximized**. Return *the maximized sum*.

**How the code works:**
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `nums = [1,4,3,2]`, expected output `4`:

All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1,4) + min(2,3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1,3) + min(2,4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1,2) + min(3,4) = 1 + 3 = 4
So the maximum possible sum is 4.

**Time:** O(n log n) where n is the length of the array · **Space:** O(1)

### **Algorithm Explanation:**

1. **Sort Array (Line 4)**:
   - Sort `nums` in ascending order
   - This ensures smaller numbers come first

2. **Sum Minimums (Lines 5-8)**:
   - **Initialize**: `sum = 0`
   - **For each pair**: Iterate with step 2 (`i += 2`)
     - After sorting, pairs are `(nums[i], nums[i+1])`
     - The minimum in each pair is `nums[i]` (smaller element)
     - Add `nums[i]` to sum

3. **Return (Line 9)**:
   - Return the accumulated sum

### **Example Walkthrough:**

**Example 1: `nums = [1,4,3,2]`**

**After sorting:**
```
Original: [1, 4, 3, 2]
Sorted:   [1, 2, 3, 4]
```

**Pairing and summing:**
```
Pair 1: (1, 2) → min = 1
Pair 2: (3, 4) → min = 3
Sum: 1 + 3 = 4
```

**Execution:**
```
Initial: sum = 0

i=0: nums[0]=1
  sum = 0 + 1 = 1

i=2: nums[2]=3
  sum = 1 + 3 = 4

Result: 4
```

**Example 2: `nums = [6,2,6,5,1,2]`**

**After sorting:**
```
Original: [6, 2, 6, 5, 1, 2]
Sorted:   [1, 2, 2, 5, 6, 6]
```

**Pairing and summing:**
```
Pair 1: (1, 2) → min = 1
Pair 2: (2, 5) → min = 2
Pair 3: (6, 6) → min = 6
Sum: 1 + 2 + 6 = 9
```

**Execution:**
```
Initial: sum = 0

i=0: nums[0]=1
  sum = 0 + 1 = 1

i=2: nums[2]=2
  sum = 1 + 2 = 3

i=4: nums[4]=6
  sum = 3 + 6 = 9

Result: 9
```
## Algorithm Breakdown

### **Why Greedy Works**

The greedy strategy is optimal because:
1. **Minimize Loss**: By pairing smallest with second smallest, we minimize the "waste" from the larger number
2. **Maximize Minimums**: This strategy maximizes the sum of minimums
3. **No Better Pairing**: Any other pairing would result in a smaller sum

**Mathematical Proof:**
- If we pair `(a, b)` where `a < b`, we get `a` in the sum
- If we pair `(a, c)` where `c > b`, we still get `a`, but `b` might be paired with a smaller number, reducing the sum
- Therefore, pairing consecutive elements after sorting is optimal

### **Key Insight: Pair Consecutive Elements**

After sorting, the optimal pairing is:
- `(nums[0], nums[1])`
- `(nums[2], nums[3])`
- `(nums[4], nums[5])`
- ...

This ensures:
- Each pair has the smallest possible difference
- The sum of minimums is maximized

### **Why Not Pair Differently?**

**Counter-example:**
```
nums = [1, 2, 3, 4]

Pairing 1 (optimal): (1,2), (3,4)
  Sum: min(1,2) + min(3,4) = 1 + 3 = 4

Pairing 2: (1,3), (2,4)
  Sum: min(1,3) + min(2,4) = 1 + 2 = 3

Pairing 3: (1,4), (2,3)
  Sum: min(1,4) + min(2,3) = 1 + 2 = 3
```

Pairing consecutive elements gives the maximum sum.

## Time & Space Complexity

- **Time Complexity**: O(n log n) where n is the length of the array
  - Dominated by sorting: O(n log n)
  - Iteration: O(n) - single pass with step 2
  - **Total**: O(n log n)
- **Space Complexity**: O(1)
  - Only using a few variables
  - Sorting is in-place (or O(n) if not in-place, but typically O(1) extra space)

## Key Points

1. **Sort First**: Essential for greedy strategy
2. **Greedy Pairing**: Pair consecutive elements after sorting
3. **Sum Minimums**: Add the first element of each pair
4. **Optimal**: Greedy approach finds maximum sum
5. **Simple**: Straightforward implementation after sorting

## Common Mistakes

1. **All same values**: `[1,1,1,1]` → return 2 (1+1)
2. **Negative numbers**: `[-1,-2,-3,-4]` → return -6 (-1 + -3)
3. **Mixed signs**: `[-1,2,-3,4]` → return -1 (-3 + 2)
4. **Two elements**: `[1,2]` → return 1
5. **Large range**: `[1,100,2,99]` → return 3 (1+2)

1. **Not sorting**: Trying to pair without sorting
2. **Wrong pairing**: Not pairing consecutive elements
3. **Wrong sum**: Summing both elements instead of minimum
4. **Index error**: Off-by-one errors in loop
5. **Negative numbers**: Forgetting to handle negative numbers correctly

## Related Problems

- [455. Assign Cookies](https://www.leetcode.com/problems/assign-cookies/) - Greedy matching
- [561. Array Partition](https://www.leetcode.com/problems/array-partition/) - Current problem
- [628. Maximum Product of Three Numbers](https://www.leetcode.com/problems/maximum-product-of-three-numbers/) - Greedy with sorting
- [462. Minimum Moves to Equal Array Elements II](https://www.leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) - Median-based greedy

## Tags

`Array`, `Greedy`, `Sorting`, `Easy`

## Key Takeaways

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

## References

- [LC 561: Array Partition on LeetCode](https://www.leetcode.com/problems/array-partition/)
- [LeetCode Discuss — LC 561: Array Partition](https://www.leetcode.com/problems/array-partition/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/array-partition/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
