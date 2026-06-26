---
layout: post
title: "[Medium] 360. Sort Transformed Array"
date: 2025-12-31 17:30:00 -0700
categories: [leetcode, medium, array, two-pointers, math, parabola]
permalink: /2025/12/31/medium-360-sort-transformed-array/
---
Given a **sorted** integer array `nums` and three integers `a`, `b`, and `c`, apply a quadratic function `f(x) = ax² + bx + c` to each element `nums[i]` in the array, and return the array in a **sorted order**.

## Examples

**Example 1:**
```
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Explanation: The function is f(x) = x² + 3x + 5
f(-4) = 16 - 12 + 5 = 9
f(-2) = 4 - 6 + 5 = 3
f(2) = 4 + 6 + 5 = 15
f(4) = 16 + 12 + 5 = 33
Sorted: [3,9,15,33]
```

**Example 2:**
```
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
Explanation: The function is f(x) = -x² + 3x + 5
f(-4) = -16 - 12 + 5 = -23
f(-2) = -4 - 6 + 5 = -5
f(2) = -4 + 6 + 5 = 7
f(4) = -16 + 12 + 5 = 1
Sorted: [-23,-5,1,7]
```

## Constraints

- `1 <= nums.length <= 200`
- `-100 <= nums[i], a, b, c <= 100`
- `nums` is sorted in **ascending order**.

## Thinking Process

Given a **sorted** integer array `nums` and three integers `a`, `b`, and `c`, apply a quadratic function `f(x) = ax² + bx + c` to each element `nums[i]` in the array, and return the array in a **sorted order**.

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

### **Solution: Two-Pointer with Parabola Property**

```cpp
class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        if(nums.empty()) return {};
        const int N = nums.size();
        vector<int> rtn(N, 0);
        auto fn = [&](const auto& x) {
            return a * x * x + b * x + c;
        };

        int i = 0, j = N - 1;
        int index = a >= 0 ? N - 1: 0;
        while(i <=j) {
            if(a >= 0) {
                rtn[index--] = fn(nums[i]) >= fn(nums[j]) ? fn(nums[i++]) : fn(nums[j--]);
            } else {
                rtn[index++] = fn(nums[i]) <= fn(nums[j]) ? fn(nums[i++]) : fn(nums[j--]);
            }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** Given a **sorted** integer array `nums` and three integers `a`, `b`, and `c`, apply a quadratic function `f(x) = ax² + bx + c` to each element `nums[i]` in the array, and return the array in a **sorted order**.

**How the code works:**
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `nums = [-4,-2,2,4], a = 1, b = 3, c = 5`, expected output `[3,9,15,33]`:

The function is f(x) = x² + 3x + 5
f(-4) = 16 - 12 + 5 = 9
f(-2) = 4 - 6 + 5 = 3
f(2) = 4 + 6 + 5 = 15
f(4) = 16 + 12 + 5 = 33
Sorted: [3,9,15,33]

### **Algorithm Explanation:**

1. **Edge Case (Line 4)**: Return empty array if input is empty

2. **Lambda Function (Lines 7-9)**:
   - Defines transformation: `f(x) = ax² + bx + c`
   - Captures `a`, `b`, `c` by reference

3. **Initialize Pointers (Lines 11-12)**:
   - `i = 0`: Left pointer (start of array)
   - `j = N - 1`: Right pointer (end of array)
   - `index`: Starting position in result array
     - `a >= 0`: Start from end (N-1) - fill largest first
     - `a < 0`: Start from start (0) - fill smallest first

4. **Two-Pointer Merge (Lines 13-19)**:
   - **Case 1: `a >= 0` (Upward Parabola)** (Lines 14-15):
     - Maximum values are at ends
     - Compare `fn(nums[i])` and `fn(nums[j])`
     - Take larger value, fill from end, move pointer
   - **Case 2: `a < 0` (Downward Parabola)** (Lines 16-17):
     - Minimum values are at ends
     - Compare `fn(nums[i])` and `fn(nums[j])`
     - Take smaller value, fill from start, move pointer

### **Example Walkthrough:**

**Example 1: `nums = [-4,-2,2,4], a = 1, b = 3, c = 5`**

```
Function: f(x) = x² + 3x + 5

Transformations:
f(-4) = 16 - 12 + 5 = 9
f(-2) = 4 - 6 + 5 = 3
f(2) = 4 + 6 + 5 = 15
f(4) = 16 + 12 + 5 = 33

Since a = 1 > 0 (upward parabola):
- Fill from end (index = N-1 = 3)

Step 1: i=0, j=3, index=3
  fn(-4) = 9, fn(4) = 33
  9 >= 33? No → take fn(4) = 33
  rtn[3] = 33, j=2, index=2

Step 2: i=0, j=2, index=2
  fn(-4) = 9, fn(2) = 15
  9 >= 15? No → take fn(2) = 15
  rtn[2] = 15, j=1, index=1

Step 3: i=0, j=1, index=1
  fn(-4) = 9, fn(-2) = 3
  9 >= 3? Yes → take fn(-4) = 9
  rtn[1] = 9, i=1, index=0

Step 4: i=1, j=1, index=0
  fn(-2) = 3, fn(-2) = 3
  3 >= 3? Yes → take fn(-2) = 3
  rtn[0] = 3, i=2, index=-1

Result: [3, 9, 15, 33] ✓
```

**Example 2: `nums = [-4,-2,2,4], a = -1, b = 3, c = 5`**

```
Function: f(x) = -x² + 3x + 5

Transformations:
f(-4) = -16 - 12 + 5 = -23
f(-2) = -4 - 6 + 5 = -5
f(2) = -4 + 6 + 5 = 7
f(4) = -16 + 12 + 5 = 1

Since a = -1 < 0 (downward parabola):
- Fill from start (index = 0)

Step 1: i=0, j=3, index=0
  fn(-4) = -23, fn(4) = 1
  -23 <= 1? Yes → take fn(-4) = -23
  rtn[0] = -23, i=1, index=1

Step 2: i=1, j=3, index=1
  fn(-2) = -5, fn(4) = 1
  -5 <= 1? Yes → take fn(-2) = -5
  rtn[1] = -5, i=2, index=2

Step 3: i=2, j=3, index=2
  fn(2) = 7, fn(4) = 1
  7 <= 1? No → take fn(4) = 1
  rtn[2] = 1, j=2, index=3

Step 4: i=2, j=2, index=3
  fn(2) = 7, fn(2) = 7
  7 <= 7? Yes → take fn(2) = 7
  rtn[3] = 7, i=3, index=4

Result: [-23, -5, 1, 7] ✓
```
## Algorithm Breakdown

### **Key Insight: Parabola Properties**

**For `a > 0` (Upward Parabola)**:
- Parabola opens upward
- Values at ends are **larger** than values in middle
- Fill result from **end** (largest to smallest)

**For `a < 0` (Downward Parabola)**:
- Parabola opens downward
- Values at ends are **smaller** than values in middle
- Fill result from **start** (smallest to largest)

**For `a = 0` (Linear Function)**:
- Function is linear: `f(x) = bx + c`
- If `b > 0`: increasing → preserve order
- If `b < 0`: decreasing → reverse order
- Algorithm handles this correctly (treated as `a >= 0` case)

### **Two-Pointer Merge Logic**

The algorithm works like merging two sorted arrays:
- Compare values at both ends
- Take the appropriate value based on parabola direction
- Move pointer that contributed the value
- Continue until all elements processed

### **Why This Works**

1. **Sorted Input**: Input array is sorted
2. **Parabola Symmetry**: Quadratic function has symmetric properties
3. **End Values**: Extreme values (max/min) are at ends for parabolas
4. **Merge Pattern**: Similar to merging sorted arrays, but filling from appropriate end

### Complexity
### **Time Complexity:** O(n)
- **Single pass**: Process each element exactly once
- **Transformations**: O(1) per element
- **Total**: O(n) where n = array length

### **Space Complexity:** O(n)
- **Result array**: O(n) to store transformed values
- **Variables**: O(1) extra space
- **Total**: O(n)

## Key Points

1. **Parabola Property**: Use parabola direction to determine fill order
2. **Two Pointers**: Efficiently merge from both ends
3. **O(n) Time**: Single pass through array
4. **No Sorting Needed**: Direct placement in correct position
5. **Handles All Cases**: Works for a > 0, a < 0, and a = 0

## Detailed Example Walkthrough

### **Example: `nums = [-1,0,1,2,3], a = 2, b = -1, c = 0`**

```
Function: f(x) = 2x² - x

Transformations:
f(-1) = 2 + 1 = 3
f(0) = 0 - 0 = 0
f(1) = 2 - 1 = 1
f(2) = 8 - 2 = 6
f(3) = 18 - 3 = 15

Since a = 2 > 0: fill from end

Step 1: i=0, j=4, index=4
  fn(-1)=3, fn(3)=15
  3 >= 15? No → rtn[4]=15, j=3, index=3

Step 2: i=0, j=3, index=3
  fn(-1)=3, fn(2)=6
  3 >= 6? No → rtn[3]=6, j=2, index=2

Step 3: i=0, j=2, index=2
  fn(-1)=3, fn(1)=1
  3 >= 1? Yes → rtn[2]=3, i=1, index=1

Step 4: i=1, j=2, index=1
  fn(0)=0, fn(1)=1
  0 >= 1? No → rtn[1]=1, j=1, index=0

Step 5: i=1, j=1, index=0
  fn(0)=0, fn(0)=0
  0 >= 0? Yes → rtn[0]=0, i=2

Result: [0, 1, 3, 6, 15] ✓
```

## Edge Cases

1. **a = 0 (Linear)**: Function is linear, algorithm still works
2. **Single element**: Returns transformed single value
3. **All same values**: All transform to same value
4. **Large coefficients**: Handles large a, b, c values
5. **Negative numbers**: Works with negative input values

## Mathematical Background

### **Quadratic Function: f(x) = ax² + bx + c**

**Vertex**: x = -b/(2a) (when a ≠ 0)

**Parabola Direction**:
- `a > 0`: Opens upward, vertex is minimum
- `a < 0`: Opens downward, vertex is maximum
- `a = 0`: Linear function (no vertex)

**On Sorted Array**:
- For upward parabola: values increase as we move away from vertex
- For downward parabola: values decrease as we move away from vertex
- Ends have extreme values (max for upward, min for downward)

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [360. Sort Transformed Array](https://www.leetcode.com/problems/sort-transformed-array/) - Current problem
- [977. Squares of a Sorted Array](https://www.leetcode.com/problems/squares-of-a-sorted-array/) - Similar two-pointer approach
- [88. Merge Sorted Array](https://www.leetcode.com/problems/merge-sorted-array/) - Merge two sorted arrays
- [977. Squares of a Sorted Array](https://www.leetcode.com/problems/squares-of-a-sorted-array/) - Transform and sort

## Tags

`Array`, `Two Pointers`, `Math`, `Parabola`, `Medium`

## Key Takeaways

- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

## References

- [LC 360: Sort Transformed Array on LeetCode](https://www.leetcode.com/problems/sort-transformed-array/)
- [LeetCode Discuss — LC 360: Sort Transformed Array](https://www.leetcode.com/problems/sort-transformed-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/sort-transformed-array/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
