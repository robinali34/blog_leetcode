---
layout: post
title: "[Medium] 48. Rotate Image"
date: 2025-09-24 21:00:00 -0000
categories: leetcode algorithm matrix data-structures 2d-array transformation medium cpp rotate-image in-place problem-solving
---
This is a matrix manipulation problem that requires rotating a 2D matrix 90 degrees clockwise in-place. The key insight is understanding the relationship between matrix positions during rotation and implementing it efficiently.

Given an n x n 2D matrix representing an image, rotate the image by 90 degrees clockwise in-place.

## Examples
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

## Constraints
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

## Thinking Process

There are two main approaches to solve this problem:

1. **Direct Rotation**: Rotate elements in groups of 4 using coordinate mapping
2. **Transpose + Reflect**: Transpose the matrix then reflect each row



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Grid traversal</text>

  <rect x="50" y="40" width="28" height="28" fill="#D4D8E0" stroke="#8B8680"/><rect x="78" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="106" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="50" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="78" y="68" width="28" height="28" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="106" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="110" y="115" text-anchor="middle" font-size="11" fill="#6B6560">BFS/DFS flood from each cell</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Row/column traversal | O(nm) | O(1) | Simulation, spiral |
| BFS/DFS on grid | O(nm) | O(nm) | Islands, shortest path |
| Matrix as graph | O(nm) | O(nm) | 4/8-directional neighbors |
| **Transpose / rotate** *(this problem)* | O(nm) | O(1) | In-place rotation tricks |

## Solution

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

### Solution Explanation

**Approach:** Transpose / rotate (this problem)

**Key idea:** There are two main approaches to solve this problem:

**How the code works:**
1. **Direct Rotation**: Rotate elements in groups of 4 using coordinate mapping
2. **Transpose + Reflect**: Transpose the matrix then reflect each row

**Walkthrough** — input `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, expected output `[[7,4,1],[8,5,2],[9,6,3]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
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

## Matrix Size Considerations

- **Even n**: Process all n²/4 groups
- **Odd n**: Process (n²-1)/4 groups (center element stays unchanged)

## Common Mistakes

- **Coordinate Errors**: Incorrect mapping formulas
- **Boundary Issues**: Not handling odd matrix sizes correctly
- **Over-rotation**: Processing the same elements multiple times
- **Index Confusion**: Mixing up row and column indices

---

## References

- [LC 48: Rotate Image on LeetCode](https://www.leetcode.com/problems/rotate-image/)
- [LeetCode Discuss — LC 48: Rotate Image](https://www.leetcode.com/problems/rotate-image/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/rotate-image/editorial/) *(may require premium)*

## Key Takeaways

1. **In-Place Rotation**: Must modify the original matrix without extra space
2. **Group of 4**: Each element participates in a cycle of 4 positions
3. **Boundary Handling**: Careful with odd/even matrix sizes
4. **Mathematical Approach**: Transpose + reflect is more intuitive
