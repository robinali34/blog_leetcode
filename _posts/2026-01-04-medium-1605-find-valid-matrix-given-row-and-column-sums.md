---
layout: post
title: "[Medium] 1605. Find Valid Matrix Given Row and Column Sums"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, medium, array, matrix, greedy]
permalink: /2026/01/04/medium-1605-find-valid-matrix-given-row-and-column-sums/
---
You are given two arrays `rowSum` and `colSum` of non-negative integers where `rowSum[i]` is the sum of the elements in the `i`-th row and `colSum[j]` is the sum of the elements in the `j`-th column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any non-negative integer matrix of size `rowSum.length x colSum.length` that satisfies the `rowSum` and `colSum` requirements.

Return *a 2D array representing **any** matrix that fulfills the requirements. It's guaranteed that **at least one** matrix that fulfills the requirements exists*.

## Examples

**Example 1:**
```
Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation:
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The matrix is valid.
```

**Example 2:**
```
Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[5,0,0],
         [3,4,0],
         [0,2,8]]
```

**Example 3:**
```
Input: rowSum = [14,9], colSum = [6,9,8]
Output: [[6,8,0],
         [0,1,8]]
```

## Constraints

- `1 <= rowSum.length, colSum.length <= 500`
- `0 <= rowSum[i], colSum[j] <= 10^8`
- `sum(rowSum) == sum(colSum)`

## Thinking Process

You are given two arrays `rowSum` and `colSum` of non-negative integers where `rowSum[i]` is the sum of the elements in the `i`-th row and `colSum[j]` is the sum of the elements in the `j`-th column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any non-negative integer matrix of size `rowSum.length x colSum.length` that satisfies the `rowSum` and `colSum` requirements.

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

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
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

## Solution

### **Solution: Greedy with Two Pointers**

```cpp
class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        const int N = rowSum.size(), M = colSum.size();
        vector<vector<int>> matrix(N, vector<int>(M, 0));
        int i = 0, j = 0;
        while(i < N && j < M) {
            int v = min(rowSum[i], colSum[j]);
            matrix[i][j] = v;
            rowSum[i] -= v;
            colSum[j] -= v;
            if(rowSum[i] == 0) {
                i++;
            }
            if(colSum[j] == 0) {
                j++;
            }
        }
        return matrix;
    }
};
```

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** You are given two arrays `rowSum` and `colSum` of non-negative integers where `rowSum[i]` is the sum of the elements in the `i`-th row and `colSum[j]` is the sum of the elements in the `j`-th column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

**How the code works:**
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `rowSum = [3,8], colSum = [4,7]`, expected output `[[3,0],`:

0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The matrix is valid.

**Time:** O(N × M) where N is number of rows, M is number of columns · **Space:** O(N × M)

### **Algorithm Explanation:**

1. **Initialize (Lines 4-6)**:
   - `N`: Number of rows (`rowSum.size()`)
   - `M`: Number of columns (`colSum.size()`)
   - `matrix`: Initialize with zeros
   - `i`, `j`: Pointers for current row and column (start at 0)

2. **Greedy Fill (Lines 7-16)**:
   - **While both pointers are valid** (`i < N && j < M`):
     - **Calculate value**: `v = min(rowSum[i], colSum[j])`
       - Place the minimum to satisfy both constraints
     - **Place value**: `matrix[i][j] = v`
     - **Update sums**: Subtract `v` from both `rowSum[i]` and `colSum[j]`
     - **Advance pointers**:
       - If `rowSum[i] == 0`: Move to next row (`i++`)
       - If `colSum[j] == 0`: Move to next column (`j++`)

3. **Return (Line 17)**:
   - Return the constructed matrix

### **Why This Works:**

**Key Insight**: At each step, we place the maximum value that satisfies both the row and column constraints.

**Strategy**:
1. **Place Minimum**: `min(rowSum[i], colSum[j])` ensures:
   - We don't exceed either constraint
   - We make maximum progress (satisfy at least one constraint completely)
2. **Update Sums**: Subtracting the placed value maintains the remaining sums
3. **Advance Pointers**: When a sum becomes 0, that row/column is satisfied, so we move on
4. **Termination**: The loop ends when all rows or all columns are satisfied
   - Since `sum(rowSum) == sum(colSum)`, when we finish, both are satisfied

**Example Walkthrough:**

**Example 1: `rowSum = [3,8]`, `colSum = [4,7]`**

**Initial state:**
```
rowSum = [3, 8]
colSum = [4, 7]
matrix = [[0, 0],
          [0, 0]]
i = 0, j = 0
```

**Execution:**
```
Step 1: i=0, j=0
  v = min(3, 4) = 3
  matrix[0][0] = 3
  rowSum[0] = 3 - 3 = 0 → i++
  colSum[0] = 4 - 3 = 1
  State: i=1, j=0, rowSum=[0,8], colSum=[1,7]

Step 2: i=1, j=0
  v = min(8, 1) = 1
  matrix[1][0] = 1
  rowSum[1] = 8 - 1 = 7
  colSum[0] = 1 - 1 = 0 → j++
  State: i=1, j=1, rowSum=[0,7], colSum=[0,7]

Step 3: i=1, j=1
  v = min(7, 7) = 7
  matrix[1][1] = 7
  rowSum[1] = 7 - 7 = 0 → i++
  colSum[1] = 7 - 7 = 0 → j++
  State: i=2, j=2 (both out of bounds)

Loop ends: i=2 >= N=2

Final matrix:
[[3, 0],
 [1, 7]]
```

**Verification:**
```
Row 0: 3 + 0 = 3 ✓
Row 1: 1 + 7 = 8 ✓
Col 0: 3 + 1 = 4 ✓
Col 1: 0 + 7 = 7 ✓
```

**Example 2: `rowSum = [5,7,10]`, `colSum = [8,6,8]`**

**Execution:**
```
Step 1: i=0, j=0
  v = min(5, 8) = 5
  matrix[0][0] = 5
  rowSum[0] = 0 → i++
  colSum[0] = 3
  State: i=1, j=0

Step 2: i=1, j=0
  v = min(7, 3) = 3
  matrix[1][0] = 3
  rowSum[1] = 4
  colSum[0] = 0 → j++
  State: i=1, j=1

Step 3: i=1, j=1
  v = min(4, 6) = 4
  matrix[1][1] = 4
  rowSum[1] = 0 → i++
  colSum[1] = 2
  State: i=2, j=1

Step 4: i=2, j=1
  v = min(10, 2) = 2
  matrix[2][1] = 2
  rowSum[2] = 8
  colSum[1] = 0 → j++
  State: i=2, j=2

Step 5: i=2, j=2
  v = min(8, 8) = 8
  matrix[2][2] = 8
  rowSum[2] = 0 → i++
  colSum[2] = 0 → j++
  State: i=3, j=3 (both out of bounds)

Final matrix:
[[5, 0, 0],
 [3, 4, 0],
 [0, 2, 8]]
```

## Algorithm Breakdown

### **Why Greedy Works**

**Greedy Choice Property**: At each step, placing `min(rowSum[i], colSum[j])` is optimal because:
1. **Satisfies Constraints**: Doesn't exceed either row or column sum
2. **Maximizes Progress**: Satisfies at least one constraint completely
3. **No Regret**: Any value we place here reduces both constraints, so we want to place as much as possible

**Optimal Substructure**: After placing a value, the remaining problem (satisfying remaining sums) is independent and can be solved optimally.

### **Why Two Pointers Work**

**Pointer Advancement**:
- When `rowSum[i] == 0`: Row `i` is satisfied, move to next row
- When `colSum[j] == 0`: Column `j` is satisfied, move to next column
- Both can advance in the same iteration if both become 0

**Termination**: The loop ends when `i >= N` or `j >= M`. Since `sum(rowSum) == sum(colSum)`, when we finish processing all cells, both row and column sums are satisfied.

### **Mathematical Guarantee**

**Invariant**: At any point, `sum(rowSum) == sum(colSum)` (remaining sums are equal).

**Proof**:
- Initially: `sum(rowSum) == sum(colSum)` (given)
- At each step: We subtract the same value `v` from both `rowSum[i]` and `colSum[j]`
- Therefore: The sums remain equal throughout

**Corollary**: When all rows are satisfied (`i >= N`), all columns are also satisfied, and vice versa.

## Time & Space Complexity

- **Time Complexity**: O(N × M) where N is number of rows, M is number of columns
  - In worst case, we visit each cell once
  - Each iteration does O(1) work
  - **Total**: O(N × M)
- **Space Complexity**: O(N × M)
  - Space for the output matrix
  - O(1) extra space for variables

## Key Points

1. **Greedy Choice**: Always place `min(rowSum[i], colSum[j])` at each cell
2. **Two Pointers**: Use pointers to track current row and column
3. **Advance When Zero**: Move to next row/column when sum becomes 0
4. **Optimal**: This greedy strategy always finds a valid matrix
5. **Simple**: Straightforward implementation

## Common Mistakes

1. **Single cell**: `rowSum = [5]`, `colSum = [5]` → `[[5]]`
2. **Single row**: `rowSum = [10]`, `colSum = [3,7]` → `[[3,7]]`
3. **Single column**: `rowSum = [3,7]`, `colSum = [10]` → `[[3],[7]]`
4. **All zeros**: `rowSum = [0,0]`, `colSum = [0,0]` → `[[0,0],[0,0]]`
5. **Large values**: Works with values up to 10^8

1. **Wrong minimum**: Not using `min(rowSum[i], colSum[j])`
2. **Not updating sums**: Forgetting to subtract placed value
3. **Wrong pointer logic**: Not advancing pointers correctly
4. **Index errors**: Incorrect matrix indexing
5. **Not handling zeros**: Not advancing when sum becomes 0

## Related Problems

- [406. Queue Reconstruction by Height](https://www.leetcode.com/problems/queue-reconstruction-by-height/) - Greedy with constraints
- [435. Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/) - Greedy interval selection
- [1029. Two City Scheduling](https://www.leetcode.com/problems/two-city-scheduling/) - Greedy with sorting
- [1710. Maximum Units on a Truck](https://www.leetcode.com/problems/maximum-units-on-a-truck/) - Greedy selection

## Follow-Up: Why Minimum is Optimal

**Question**: Why does placing `min(rowSum[i], colSum[j])` give an optimal solution?

**Answer**:
- **Maximizes Progress**: By placing the maximum possible value (minimum of constraints), we satisfy at least one constraint completely
- **No Waste**: We don't place more than needed, leaving room for other cells
- **Greedy Choice**: This locally optimal choice leads to a globally optimal solution
- **Mathematical Proof**: Any other value would either:
  - Exceed a constraint (invalid)
  - Leave more work for later (suboptimal)
  - Be equivalent (same result)

## Tags

`Array`, `Matrix`, `Greedy`, `Medium`

## Key Takeaways

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

## References

- [LC 1605: Find Valid Matrix Given Row and Column Sums on LeetCode](https://www.leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/)
- [LeetCode Discuss — LC 1605: Find Valid Matrix Given Row and Column Sums](https://www.leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
