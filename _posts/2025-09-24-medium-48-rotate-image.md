---
layout: post
title: "[Medium] 48. Rotate Image"
date: 2025-09-24 21:00:00 -0000
categories: leetcode algorithm matrix data-structures 2d-array transformation medium cpp rotate-image in-place problem-solving
---

# [Medium] 48. Rotate Image

This is a matrix manipulation problem that requires rotating a 2D matrix 90 degrees clockwise in-place. The key insight is understanding the relationship between matrix positions during rotation and implementing it efficiently.

## Problem Description

Given an n x n 2D matrix representing an image, rotate the image by 90 degrees clockwise in-place.

### Examples

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2:**
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

### Constraints
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Rotation direction**: Which direction should we rotate? (Assumption: Clockwise 90 degrees - typical matrix rotation)

2. **Matrix type**: Is the matrix square? (Assumption: Yes - per constraints, n x n matrix)

3. **In-place modification**: Should we modify the matrix in-place? (Assumption: Yes - modify matrix in-place, O(1) extra space)

4. **Rotation angle**: What is the rotation angle? (Assumption: 90 degrees clockwise - standard matrix rotation)

5. **Element movement**: How do elements move? (Assumption: Element at (i, j) moves to (j, n-1-i) after 90° clockwise rotation)

## Approach

There are two main approaches to solve this problem:

1. **Direct Rotation**: Rotate elements in groups of 4 using coordinate mapping
2. **Transpose + Reflect**: Transpose the matrix then reflect each row

## Solution 1: Direct Rotation

**Time Complexity:** O(n²) - Visit each element once  
**Space Complexity:** O(1) - Only using constant extra space

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for(int i = 0; i < (n+1)/2; i++) {
            for (int j = 0; j< n/2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][i];
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = temp;
            }
        }
    }
};
```

## Solution 2: Transpose + Reflect

**Time Complexity:** O(n²) - Visit each element twice  
**Space Complexity:** O(1) - Only using constant extra space

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        transpose(matrix);
        reflect(matrix);
    }

private:
    void transpose(vector<vector<int>>& matrix) {
        const int n = matrix.size();
        for (int i = 0; i < n; i++){
            for (int j = i + 1; j < n; j++) {
                swap(matrix[j][i], matrix[i][j]);
            }
        }
    }

    void reflect(vector<vector<int>>& matrix) {
        for (auto& row : matrix) {
            reverse(row.begin(), row.end());
        }
    }
};
```

## Step-by-Step Example

Let's trace through Solution 2 with matrix = `[[1,2,3],[4,5,6],[7,8,9]]`:

**Step 1: Transpose**
```
Original:  [1,2,3]    Transposed:  [1,4,7]
           [4,5,6]                 [2,5,8]
           [7,8,9]                 [3,6,9]
```

**Step 2: Reflect (reverse each row)**
```
Transposed: [1,4,7]    Reflected:   [7,4,1]
            [2,5,8]                [8,5,2]
            [3,6,9]                [9,6,3]
```

**Result:** `[[7,4,1],[8,5,2],[9,6,3]]`

## Coordinate Mapping (Solution 1)

For a 90° clockwise rotation, the coordinate transformation is:
- `(i, j) → (j, n-1-i)`

The four positions that rotate together:
1. `(i, j)` → `(j, n-1-i)`
2. `(j, n-1-i)` → `(n-1-i, n-1-j)`
3. `(n-1-i, n-1-j)` → `(n-1-j, i)`
4. `(n-1-j, i)` → `(i, j)`

## Key Insights

1. **In-Place Rotation**: Must modify the original matrix without extra space
2. **Group of 4**: Each element participates in a cycle of 4 positions
3. **Boundary Handling**: Careful with odd/even matrix sizes
4. **Mathematical Approach**: Transpose + reflect is more intuitive

## Solution Comparison

| Approach | Pros | Cons |
|----------|------|------|
| **Direct Rotation** | Single pass, efficient | Complex coordinate mapping |
| **Transpose + Reflect** | Intuitive, easier to understand | Two passes through matrix |

## Matrix Size Considerations

- **Even n**: Process all n²/4 groups
- **Odd n**: Process (n²-1)/4 groups (center element stays unchanged)

## Common Mistakes

- **Coordinate Errors**: Incorrect mapping formulas
- **Boundary Issues**: Not handling odd matrix sizes correctly
- **Over-rotation**: Processing the same elements multiple times
- **Index Confusion**: Mixing up row and column indices

---
