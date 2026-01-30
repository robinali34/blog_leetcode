---
layout: post
title: "[Medium] 240. Search a 2D Matrix II"
date: 2025-10-07 22:01:10 -0700
categories: leetcode algorithm medium cpp binary-search matrix 2d-array divide-conquer search optimization problem-solving
---

# [Medium] 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

## Examples

**Example 1:**
```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

Matrix visualization:
```
[ 1,  4,  7, 11, 15]
[ 2,  5,  8, 12, 19]  ← target = 5 found here
[ 3,  6,  9, 16, 22]
[10, 13, 14, 17, 24]
[18, 21, 23, 26, 30]
```

**Example 2:**
```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

Matrix visualization:
```
[ 1,  4,  7, 11, 15]
[ 2,  5,  8, 12, 19]
[ 3,  6,  9, 16, 22]
[10, 13, 14, 17, 24]
[18, 21, 23, 26, 30]
```
Target = 20 not found in matrix

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order.
- `-10^9 <= target <= 10^9`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Matrix properties**: What are the matrix properties? (Assumption: Each row sorted left-to-right, each column sorted top-to-bottom - not fully sorted)

2. **Search target**: What are we searching for? (Assumption: Find if target value exists in the matrix)

3. **Return value**: What should we return? (Assumption: Boolean - true if target found, false otherwise)

4. **Time complexity**: What time complexity is expected? (Assumption: O(m + n) - linear time using matrix properties)

5. **Duplicate values**: Can matrix contain duplicates? (Assumption: Yes - per constraints, no restriction on duplicates)

## Solution 1: Binary Search per Row

**Time Complexity:** O(m log n)  
**Space Complexity:** O(1)

Search each row using binary search.

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        const int rows = matrix.size(), cols = matrix[0].size();
        
        for(int i = 0; i < rows; i++) {
            int left = 0, right = cols - 1;
            while(left <= right) {
                int mid = left + (right - left) / 2;
                if(matrix[i][mid] == target) {
                    return true;
                } else if (matrix[i][mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return false;
    }
};
```

### How it Works:

1. **Iterate through each row**
2. **Binary search** within each row for the target
3. **Return true** if found in any row, **false** otherwise

## Solution 2: Divide and Conquer

**Time Complexity:** O(n log n) average case  
**Space Complexity:** O(log n) for recursion stack

Use divide and conquer by eliminating regions based on the middle column.

```cpp
class Solution {
private:
    bool searchMatrix(vector<vector<int>>& matrix, int target, int top, int left, int bottom, int right) {
        if(top > bottom || left > right) return false;
        if(target < matrix[top][left] || target > matrix[bottom][right]) return false;
        
        int midCol = left + (right - left) / 2;
        int row = top;
        
        // Find the last row where matrix[row][midCol] <= target
        while(row <= bottom && matrix[row][midCol] <= target) {
            if(matrix[row][midCol] == target) return true;
            row++;
        }
        
        // Search in top-right and bottom-left quadrants
        return searchMatrix(matrix, target, top, midCol + 1, row - 1, right) ||
               searchMatrix(matrix, target, row, left, bottom, midCol - 1);
    }
    
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        return searchMatrix(matrix, target, 0, 0, matrix.size() - 1, matrix[0].size() - 1);
    }
};
```

### How it Works:

1. **Choose middle column** and find the boundary where elements ≤ target
2. **Eliminate regions**: Search only in top-right and bottom-left quadrants
3. **Recursively search** the remaining regions

## Solution 3: Optimal Search from Top-Right (Recommended)

**Time Complexity:** O(m + n)  
**Space Complexity:** O(1)

Start from top-right corner and eliminate row or column at each step.

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        const int rows = matrix.size(), cols = matrix[0].size();
        int row = 0, col = cols - 1;
        
        while(row < rows && col >= 0) {
            if(matrix[row][col] == target) {
                return true;
            } else if(matrix[row][col] > target) {
                col--;  // Eliminate current column
            } else {
                row++;  // Eliminate current row
            }
        }
        return false;
    }
};
```

### How it Works:

1. **Start from top-right corner** (matrix[0][cols-1])
2. **Compare with target**:
   - If equal: found target
   - If greater: eliminate current column (move left)
   - If smaller: eliminate current row (move down)
3. **Continue until** target found or out of bounds

## Algorithm Comparison

| Solution | Time Complexity | Space Complexity | Approach |
|----------|----------------|------------------|----------|
| Binary Search per Row | O(m log n) | O(1) | Search each row |
| Divide and Conquer | O(n log n) avg | O(log n) | Recursive elimination |
| Top-Right Search | O(m + n) | O(1) | Optimal elimination |

## Visual Example

For target = 5 in the matrix:
```
[ 1,  4,  7, 11, 15]
[ 2,  5,  8, 12, 19]  ← Found here!
[ 3,  6,  9, 16, 22]
[10, 13, 14, 17, 24]
[18, 21, 23, 26, 30]
```

**Top-Right Search Path:**
1. Start at 15 (top-right)
2. 15 > 5 → move left to 11
3. 11 > 5 → move left to 7  
4. 7 > 5 → move left to 4
5. 4 < 5 → move down to 5
6. 5 == 5 → **Found!**

**Search Path Visualization:**
```
[ 1,  4,  7, 11, 15] ← Start here
[ 2,  5,  8, 12, 19] ← End here (found!)
[ 3,  6,  9, 16, 22]
[10, 13, 14, 17, 24]
[18, 21, 23, 26, 30]
```
Path: 15 → 11 → 7 → 4 → 5 ✓

## Key Insights

1. **Matrix properties** allow elimination strategies
2. **Top-right approach** is optimal with O(m + n) time
3. **Binary search per row** is simple but not optimal
4. **Divide and conquer** provides good average performance
5. **Elimination strategy** leverages sorted properties

## Why Top-Right Works

- **If current element > target**: All elements in current column are ≥ current element, so eliminate column
- **If current element < target**: All elements in current row are ≤ current element, so eliminate row
- **Each step eliminates** either a row or column, guaranteeing O(m + n) steps

## Related Problems

- [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) - Strictly sorted matrix
- [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) - Finding kth element
- [1428. Leftmost Column with at Least a One](https://leetcode.com/problems/leftmost-column-with-at-least-a-one/) - Binary matrix search
