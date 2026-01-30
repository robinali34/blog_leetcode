---
layout: post
title: "360. Sort Transformed Array"
date: 2025-12-31 17:30:00 -0700
categories: [leetcode, medium, array, two-pointers, math, parabola]
permalink: /2025/12/31/medium-360-sort-transformed-array/
---

# 360. Sort Transformed Array

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Transformation function**: What is the transformation? (Assumption: f(x) = ax² + bx + c - quadratic function)

2. **Sorting requirement**: Should we sort the transformed array? (Assumption: Yes - return sorted array of transformed values)

3. **Return format**: What should we return? (Assumption: Array of transformed and sorted values)

4. **Input order**: Is input array sorted? (Assumption: Yes - nums is sorted in ascending order per constraints)

5. **Parabola direction**: How does parabola direction affect sorting? (Assumption: If a > 0, parabola opens upward (min at center), if a < 0, opens downward (max at center))

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Apply the transformation f(x) = ax² + bx + c to each element, then sort the resulting array. This straightforward approach has O(n log n) time complexity for sorting, which works but can be optimized further by leveraging the properties of the quadratic function.

**Step 2: Semi-Optimized Approach (7 minutes)**

Recognize that the transformation is a quadratic function. If a > 0, the function has a minimum (parabola opens upward), so values are smallest near the vertex and increase toward both ends. If a < 0, the function has a maximum (parabola opens downward), so values are largest near the vertex and decrease toward both ends. Use two pointers from both ends, comparing transformed values. However, handling the vertex and determining the merge order requires careful logic.

**Step 3: Optimized Solution (8 minutes)**

Use two pointers technique based on the sign of 'a'. If a >= 0 (parabola opens upward), transformed values are smallest at the ends and largest in the middle. Use two pointers starting from both ends, merge in descending order (largest first), then reverse. If a < 0 (parabola opens downward), transformed values are largest at the ends and smallest in the middle. Use two pointers merging in ascending order (smallest first). This achieves O(n) time with O(n) space, which is optimal since we must process all elements. The key insight is that the quadratic transformation preserves the relative ordering from the ends (for a >= 0) or reverses it (for a < 0), allowing linear-time merging.

## Solution Approach

This problem requires applying a quadratic function to each element and returning results in sorted order. The key insight is understanding how quadratic functions behave on sorted arrays.

### Key Insights:

1. **Parabola Properties**:
   - If `a > 0`: Parabola opens **upward** → maximum values at ends
   - If `a < 0`: Parabola opens **downward** → minimum values at ends
   - If `a = 0`: Linear function → preserves order

2. **Two-Pointer Technique**: 
   - Compare transformed values at both ends
   - Fill result from appropriate end based on `a`
   - Move pointers inward

3. **Merge Strategy**:
   - For `a >= 0`: Fill from end (largest first)
   - For `a < 0`: Fill from start (smallest first)

### Algorithm:

1. **Transform function**: `f(x) = ax² + bx + c`
2. **Two pointers**: Start from both ends of sorted array
3. **Compare and fill**: Based on `a`, fill result from appropriate end
4. **Move pointers**: Move pointer that contributed the value

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

## Complexity Analysis

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

## Alternative Approaches

### **Approach 1: Two-Pointer (Current Solution)**
- **Time**: O(n)
- **Space**: O(n)
- **Best for**: Optimal solution using parabola properties

### **Approach 2: Transform and Sort**
- **Time**: O(n log n)
- **Space**: O(n)
- **Simple**: Transform all, then sort
- **Inefficient**: Doesn't use parabola properties

### **Approach 3: Find Vertex and Merge**
- **Time**: O(n)
- **Space**: O(n)
- **Find vertex**: Calculate parabola vertex, split array
- **Merge**: Merge two sorted halves
- **More complex**: Similar performance to current solution

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

## Related Problems

- [360. Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array/) - Current problem
- [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) - Similar two-pointer approach
- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) - Merge two sorted arrays
- [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) - Transform and sort

## Tags

`Array`, `Two Pointers`, `Math`, `Parabola`, `Medium`

