---
layout: post
title: "[Hard] 308. Range Sum Query 2D - Mutable"
date: 2025-12-31 21:30:00 -0700
categories: [leetcode, hard, design, data-structures, prefix-sum, matrix]
permalink: /2025/12/31/hard-308-range-sum-query-2d-mutable/
---
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

## Thinking Process

Given a 2D matrix `matrix`, handle multiple queries of the following types:

1. **Update** the value of a cell in `matrix`.

- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.
- Boundary checks on every neighbor expansion.

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
| **Row/column traversal** *(this problem)* | O(nm) | O(1) | Simulation, spiral |
| BFS/DFS on grid | O(nm) | O(nm) | Islands, shortest path |
| Matrix as graph | O(nm) | O(nm) | 4/8-directional neighbors |
| Transpose / rotate | O(nm) | O(1) | In-place rotation tricks |

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

### Solution Explanation

**Approach:** Row/column traversal (this problem)

**Key idea:** Given a 2D matrix `matrix`, handle multiple queries of the following types:

**How the code works:**
1. **Update** the value of a cell in `matrix`.
- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.
- Boundary checks on every neighbor expansion.

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

### Complexity
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [304. Range Sum Query 2D - Immutable](https://www.leetcode.com/problems/range-sum-query-2d-immutable/) - Immutable version
- [307. Range Sum Query - Mutable](https://www.leetcode.com/problems/range-sum-query-mutable/) - 1D mutable version
- [308. Range Sum Query 2D - Mutable](https://www.leetcode.com/problems/range-sum-query-2d-mutable/) - Current problem
- [303. Range Sum Query - Immutable](https://www.leetcode.com/problems/range-sum-query-immutable/) - 1D immutable

## Tags

`Design`, `Data Structures`, `Prefix Sum`, `Matrix`, `Hard`

## Key Takeaways

- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.
- Boundary checks on every neighbor expansion.

## References

- [LC 308: Range Sum Query 2D - Mutable on LeetCode](https://www.leetcode.com/problems/range-sum-query-2d-mutable/)
- [LeetCode Discuss — LC 308: Range Sum Query 2D - Mutable](https://www.leetcode.com/problems/range-sum-query-2d-mutable/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/range-sum-query-2d-mutable/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
