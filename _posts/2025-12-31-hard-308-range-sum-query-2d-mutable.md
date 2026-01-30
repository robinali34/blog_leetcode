---
layout: post
title: "308. Range Sum Query 2D - Mutable"
date: 2025-12-31 21:30:00 -0700
categories: [leetcode, hard, design, data-structures, prefix-sum, matrix]
permalink: /2025/12/31/hard-308-range-sum-query-2d-mutable/
---

# 308. Range Sum Query 2D - Mutable

## Problem Statement

Given a 2D matrix `matrix`, handle multiple queries of the following types:

1. **Update** the value of a cell in `matrix`.
2. **Calculate the sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(vector<vector<int>>& matrix)` Initializes the object with the integer matrix `matrix`.
- `void update(int row, int col, int val)` Updates the value of `matrix[row][col]` to be `val`.
- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the **sum** of the elements of `matrix` inside the rectangle defined by **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

## Examples

**Example 1:**
```
Input
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
Output
[null, 8, null, 10]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the left red rectangle)
numMatrix.update(3, 2, 2);       // matrix changes from [[1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]] to [[1, 2, 0, 1, 5], [4, 1, 2, 1, 7], [1, 0, 3, 0, 5]]
numMatrix.sumRegion(2, 1, 4, 3); // return 10 (i.e sum of the right red rectangle)
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `-10^5 <= matrix[i][j] <= 10^5`
- `0 <= row < m`
- `0 <= col < n`
- `-10^5 <= val <= 10^5`
- `0 <= row1 <= row2 < m`
- `0 <= col1 <= col2 < n`
- At most `10^4` calls will be made to `update` and `sumRegion`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Range format**: How are ranges represented? (Assumption: [row1, col1, row2, col2] - rectangle from (row1, col1) to (row2, col2) inclusive)

2. **Update operation**: What does update do? (Assumption: Updates matrix[row][col] to new value val)

3. **Sum calculation**: How is sum calculated? (Assumption: Sum of all elements in the rectangle range)

4. **Return value**: What should sumRegion return? (Assumption: Integer - sum of elements in specified rectangle)

5. **Time complexity**: What time complexity is expected? (Assumption: O(log m * log n) for both operations using 2D Fenwick Tree or Segment Tree)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

Store the matrix as-is. For `update`, simply modify `matrix[row][col] = val` in O(1) time. For `sumRegion`, iterate through all cells in the rectangle and sum them up, which takes O(rows × cols) time. This approach is simple but inefficient for queries, especially with many query operations.

**Step 2: Semi-Optimized Approach (10 minutes)**

Use 2D prefix sums: precompute a 2D prefix sum array where `prefix[i][j]` represents the sum of the rectangle from (0,0) to (i,j). This allows O(1) range queries using inclusion-exclusion. However, each update requires recomputing all prefix sums from the updated cell to the end, which takes O(rows × cols) time. This is better for query-heavy scenarios but still slow for updates.

**Step 3: Optimized Solution (12 minutes)**

Use row prefix sums: maintain a prefix sum array for each row separately. For `update`, only recompute the prefix sums for the affected row from the updated column onwards, taking O(cols) time. For `sumRegion`, sum up the row ranges using prefix sum differences, taking O(rows) time. This balances update and query costs. Alternatively, use a 2D Fenwick Tree or Segment Tree for O(log m × log n) for both operations, but the row prefix sum approach is simpler to implement and provides good performance for typical use cases.

## Solution Approach

This problem requires efficiently handling both **updates** and **range sum queries** on a 2D matrix. We can use **row prefix sums** to optimize range queries while allowing efficient updates.

### Key Insights:

1. **Row Prefix Sums**: For each row, maintain prefix sum array
2. **Range Query**: Use prefix sums to compute row sums in O(1)
3. **Update**: When a cell is updated, recompute prefix sums for that row from that column onwards
4. **Efficient**: O(cols) update, O(rows) query

### Algorithm:

1. **Initialize**: Build row prefix sum arrays for all rows
2. **Update**: Update matrix value, recompute prefix sums for affected row
3. **Query**: Sum up row ranges using prefix sums

## Solution

### **Solution: Row Prefix Sums**

```cpp
class NumMatrix {
private:
    vector<vector<int>> matrix, rowSumArr;
    int rowCnt, colCnt;

public:
    NumMatrix(vector<vector<int>>& matrix) {
        this->matrix = matrix;
        if(matrix.empty() || matrix[0].empty()) {
            rowCnt = 0;
            colCnt = 0;
            return;
        }
        rowCnt = matrix.size();
        colCnt = matrix[0].size();
        rowSumArr.assign(rowCnt, vector<int>(colCnt, 0));
        for(int i = 0; i < rowCnt; i++) {
            rowSumArr[i][0] = matrix[i][0];
            for(int j = 1; j < colCnt; j++) {
                rowSumArr[i][j] = rowSumArr[i][j - 1] + matrix[i][j];
            }
        }
    }
    
    void update(int row, int col, int val) {
        matrix[row][col] = val;
        int fromCol = col;
        if(col == 0) {
            rowSumArr[row][col] = matrix[row][col];
            fromCol = col + 1;
        }
        for(int j = fromCol; j < colCnt; j++) {
            rowSumArr[row][j] = rowSumArr[row][j - 1] + matrix[row][j];
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for(int i = row1; i <= row2; i++) {
            if(col1 == 0) {
                sum += rowSumArr[i][col2];
            } else {
                sum += rowSumArr[i][col2] - rowSumArr[i][col1 - 1];
            }
        }
        return sum;
    }
};
```

### **Algorithm Explanation:**

1. **Constructor (Lines 10-25)**:
   - **Store matrix**: Keep original matrix
   - **Edge case**: Handle empty matrix
   - **Initialize dimensions**: `rowCnt`, `colCnt`
   - **Build prefix sums**: For each row, compute prefix sum array
     - `rowSumArr[i][j]` = sum of row `i` from column 0 to `j`

2. **Update (Lines 27-38)**:
   - **Update matrix**: Set `matrix[row][col] = val`
   - **Recompute prefix sums**: Update prefix sums for affected row
   - **Handle column 0**: Special case - prefix sum is just the value
   - **Update from column**: Recompute prefix sums from updated column to end

3. **Sum Region (Lines 40-49)**:
   - **Iterate rows**: For each row in range `[row1, row2]`
   - **Compute row sum**: 
     - If `col1 == 0`: Use `rowSumArr[i][col2]`
     - Otherwise: Use `rowSumArr[i][col2] - rowSumArr[i][col1 - 1]`
   - **Sum up**: Add all row sums

### **Example Walkthrough:**

**Initialization:**
```
matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]

Build rowSumArr:
Row 0: [3, 3, 4, 8, 10]
Row 1: [5, 11, 14, 16, 17]
Row 2: [1, 3, 3, 4, 9]
Row 3: [4, 5, 5, 6, 13]
Row 4: [1, 1, 4, 4, 9]
```

**Query: `sumRegion(2, 1, 4, 3)`**
```
Row 2: rowSumArr[2][3] - rowSumArr[2][0] = 4 - 1 = 3
  (values: 2 + 0 + 1 = 3)

Row 3: rowSumArr[3][3] - rowSumArr[3][0] = 6 - 4 = 2
  (values: 1 + 0 + 1 = 2)

Row 4: rowSumArr[4][3] - rowSumArr[4][0] = 4 - 1 = 3
  (values: 0 + 3 + 0 = 3)

Sum = 3 + 2 + 3 = 8
```

**Update: `update(3, 2, 2)`**
```
matrix[3][2] = 2 (was 0)

Recompute rowSumArr[3] from column 2:
rowSumArr[3][2] = rowSumArr[3][1] + matrix[3][2] = 5 + 2 = 7
rowSumArr[3][3] = rowSumArr[3][2] + matrix[3][3] = 7 + 1 = 8
rowSumArr[3][4] = rowSumArr[3][3] + matrix[3][4] = 8 + 7 = 15

New rowSumArr[3] = [4, 5, 7, 8, 15]
```

**Query again: `sumRegion(2, 1, 4, 3)`**
```
Row 2: 4 - 1 = 3
Row 3: 8 - 4 = 4  (changed from 2 to 4)
Row 4: 4 - 1 = 3

Sum = 3 + 4 + 3 = 10
```

## Algorithm Breakdown

### **Key Insight: Row Prefix Sums**

Instead of computing 2D prefix sums (which would require O(rows × cols) update), we use **row prefix sums**:
- Each row has its own prefix sum array
- Update only affects one row
- Query sums up row ranges

### **Prefix Sum Formula**

For row `i`, column range `[col1, col2]`:
```
sum = rowSumArr[i][col2] - rowSumArr[i][col1 - 1]
```

Special case when `col1 == 0`:
```
sum = rowSumArr[i][col2]
```

### **Update Efficiency**

When updating `matrix[row][col]`:
- Only need to recompute prefix sums for row `row`
- Only need to recompute from column `col` to end
- Time: O(cols - col) ≈ O(cols)

## Complexity Analysis

### **Time Complexity:**
- **Constructor**: O(rows × cols) - build all prefix sums
- **Update**: O(cols) - recompute prefix sums for one row
- **Query**: O(rows) - sum up row ranges
- **Total**: O(rows × cols) initialization, O(cols) update, O(rows) query

### **Space Complexity:** O(rows × cols)
- **Matrix**: O(rows × cols) - store original matrix
- **Row prefix sums**: O(rows × cols) - prefix sum arrays
- **Total**: O(rows × cols)

## Key Points

1. **Row Prefix Sums**: Maintain prefix sum for each row separately
2. **Efficient Update**: Only recompute affected row's prefix sums
3. **Range Query**: Use prefix sum difference for O(1) row sum
4. **Trade-off**: O(cols) update vs O(rows) query
5. **Simple Implementation**: Easier than 2D BIT/Fenwick Tree

## Alternative Approaches

### **Approach 1: Row Prefix Sums (Current Solution)**
- **Update**: O(cols)
- **Query**: O(rows)
- **Best for**: Balanced update/query frequency

### **Approach 2: 2D Binary Indexed Tree (Fenwick Tree)**
- **Update**: O(log rows × log cols)
- **Query**: O(log rows × log cols)
- **Best for**: Many queries, fewer updates
- **Complex**: More complex implementation

### **Approach 3: 2D Segment Tree**
- **Update**: O(log rows × log cols)
- **Query**: O(log rows × log cols)
- **Best for**: Many queries
- **Complex**: More complex implementation

### **Approach 4: Brute Force**
- **Update**: O(1)
- **Query**: O(rows × cols)
- **Simple**: But inefficient for queries

## Detailed Example Walkthrough

### **Example: `matrix = [[1,2],[3,4]]`**

```
Step 1: Initialization
matrix = [[1, 2],
          [3, 4]]

Build rowSumArr:
Row 0: [1, 3]  (1, 1+2)
Row 1: [3, 7]  (3, 3+4)

Step 2: Query sumRegion(0, 0, 1, 1)
Row 0: rowSumArr[0][1] = 3
Row 1: rowSumArr[1][1] = 7
Sum = 3 + 7 = 10

Step 3: Update update(0, 1, 5)
matrix[0][1] = 5
matrix = [[1, 5],
          [3, 4]]

Recompute rowSumArr[0]:
rowSumArr[0][1] = rowSumArr[0][0] + matrix[0][1] = 1 + 5 = 6
rowSumArr[0] = [1, 6]

Step 4: Query sumRegion(0, 0, 1, 1)
Row 0: rowSumArr[0][1] = 6
Row 1: rowSumArr[1][1] = 7
Sum = 6 + 7 = 13
```

## Edge Cases

1. **Empty matrix**: Handle empty or null matrix
2. **Single cell**: Matrix with one cell
3. **Single row/column**: Matrix with one row or column
4. **Update same cell**: Multiple updates to same cell
5. **Query single cell**: Range with one cell

## Optimization Notes

The solution balances:
- **Update cost**: O(cols) - reasonable for typical use
- **Query cost**: O(rows) - reasonable for typical use
- **Space**: O(rows × cols) - acceptable

For better performance with many queries, consider 2D BIT or Segment Tree.

## Related Problems

- [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) - Immutable version
- [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) - 1D mutable version
- [308. Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) - Current problem
- [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) - 1D immutable

## Tags

`Design`, `Data Structures`, `Prefix Sum`, `Matrix`, `Hard`

