---
layout: post
title: "[Medium] 54. Spiral Matrix"
categories: leetcode algorithm matrix data-structures simulation traversal medium cpp spiral-matrix problem-solving
---

# [Medium] 54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

## Examples

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Spiral direction**: What is the spiral order? (Assumption: Right → Down → Left → Up, repeating - clockwise spiral)

2. **Matrix shape**: Can the matrix be non-square (rectangular)? (Assumption: Yes - m and n can be different)

3. **Output format**: Should we return elements in spiral order? (Assumption: Yes - return 1D array with elements in spiral traversal order)

4. **Empty matrix**: How should we handle an empty matrix? (Assumption: Return empty array)

5. **Visited tracking**: Can we modify the matrix or need separate tracking? (Assumption: Can use visited array or modify matrix values to mark visited)

## Approach

There are two main approaches to solve this problem:

1. **Boundary Tracking**: Use four boundaries (top, bottom, left, right) and traverse in spiral order
2. **Direction Simulation**: Use direction vectors and mark visited cells to simulate spiral movement

## Solution 1: Boundary Tracking Approach

```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> rtn;
        const int rows = matrix.size(), cols = matrix[0].size();
        int up = 0, left = 0, right = cols - 1, down = rows - 1;
        
        while(rtn.size() < rows * cols) {
            // Traverse right along top row
            for(int col = left; col <= right; col++) {
                rtn.push_back(matrix[up][col]);
            }
            
            // Traverse down along right column
            for(int row = up + 1; row <= down; row++) {
                rtn.push_back(matrix[row][right]);
            }
            
            // Traverse left along bottom row (if not same as top)
            if(up != down) {
                for (int col = right - 1; col >= left; col--) {
                    rtn.push_back(matrix[down][col]);
                }
            }
            
            // Traverse up along left column (if not same as right)
            if(left != right) {
                for(int row = down - 1; row > up; row--) {
                    rtn.push_back(matrix[row][left]);
                }
            }
            
            // Move boundaries inward
            left++;
            right--;
            up++;
            down--;
        }
        return rtn;
    }
};
```

**Time Complexity:** O(m × n) - Visit each cell exactly once
**Space Complexity:** O(1) - Only using variables for boundaries

## Solution 2: Direction Simulation Approach

{% raw %}
```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(matrix.size() == 0 || matrix[0].size() == 0) return {};

        const int ROWS = matrix.size(), COLS = matrix[0].size();
        vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
        const int TOTAL = ROWS * COLS;
        vector<int> order(TOTAL);

        int row = 0, col = 0;
        int dirIdx = 0;
        for(int i = 0; i < TOTAL; i++) {
            order[i] = matrix[row][col];
            visited[row][col] = true;
            int nextRow = row + DIRS[dirIdx][0], nextCol = col + DIRS[dirIdx][1];
            if(nextRow < 0 || nextRow >= ROWS || nextCol < 0 || nextCol >= COLS || visited[nextRow][nextCol]) {
                dirIdx = (dirIdx + 1) % 4;
            }
            row += DIRS[dirIdx][0];
            col += DIRS[dirIdx][1];
        }
        return order;
    }

private:
    const vector<vector<int>> DIRS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
};
```
{% endraw %}

**Time Complexity:** O(m × n) - Visit each cell exactly once
**Space Complexity:** O(m × n) - Visited matrix plus output array

## Step-by-Step Example (Solution 1)

For matrix = [[1,2,3],[4,5,6],[7,8,9]]:

1. **Initial boundaries:** up=0, down=2, left=0, right=2
2. **Right traversal:** [1,2,3] → rtn = [1,2,3]
3. **Down traversal:** [6,9] → rtn = [1,2,3,6,9]
4. **Left traversal:** [8,7] → rtn = [1,2,3,6,9,8,7]
5. **Up traversal:** [4] → rtn = [1,2,3,6,9,8,7,4]
6. **Update boundaries:** up=1, down=1, left=1, right=1
7. **Right traversal:** [5] → rtn = [1,2,3,6,9,8,7,4,5]

Final result: [1,2,3,6,9,8,7,4,5]

## Key Insights

1. **Boundary Management**: Track four boundaries and move them inward after each complete spiral
2. **Edge Cases**: Handle single row/column matrices with conditional checks
3. **Direction Changes**: Use direction vectors to simulate spiral movement
4. **Visited Marking**: Mark cells as visited to avoid revisiting them

## Solution Comparison

- **Boundary Tracking**: More intuitive, doesn't modify input matrix, cleaner logic
- **Direction Simulation**: More general approach, can be extended to other spiral problems

## Common Mistakes

1. **Off-by-one errors** in boundary conditions
2. **Not handling single row/column** cases properly
3. **Incorrect boundary updates** after each spiral
4. **Missing edge cases** for 1x1 matrices

## Related Problems

- [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)
- [885. Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/)
- [2326. Spiral Matrix IV](https://leetcode.com/problems/spiral-matrix-iv/)
