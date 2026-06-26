---
layout: post
title: "[Medium] 54. Spiral Matrix"
categories: leetcode algorithm matrix data-structures simulation traversal medium cpp spiral-matrix problem-solving
---
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

## Thinking Process

There are two main approaches to solve this problem:

1. **Boundary Tracking**: Use four boundaries (top, bottom, left, right) and traverse in spiral order
2. **Direction Simulation**: Use direction vectors and mark visited cells to simulate spiral movement

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
| **Matrix as graph** *(this problem)* | O(nm) | O(nm) | 4/8-directional neighbors |
| Transpose / rotate | O(nm) | O(1) | In-place rotation tricks |

## Solution

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

### Solution Explanation

**Approach:** Matrix as graph (this problem)

**Key idea:** There are two main approaches to solve this problem:

**How the code works:**
1. **Boundary Tracking**: Use four boundaries (top, bottom, left, right) and traverse in spiral order
2. **Direction Simulation**: Use direction vectors and mark visited cells to simulate spiral movement

**Walkthrough** — input `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, expected output `[1,2,3,6,9,8,7,4,5]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

1. **Off-by-one errors** in boundary conditions
2. **Not handling single row/column** cases properly
3. **Incorrect boundary updates** after each spiral
4. **Missing edge cases** for 1x1 matrices

## Related Problems

- [59. Spiral Matrix II](https://www.leetcode.com/problems/spiral-matrix-ii/)
- [885. Spiral Matrix III](https://www.leetcode.com/problems/spiral-matrix-iii/)
- [2326. Spiral Matrix IV](https://www.leetcode.com/problems/spiral-matrix-iv/)

## References

- [LC 54: Spiral Matrix on LeetCode](https://www.leetcode.com/problems/spiral-matrix/)
- [LeetCode Discuss — LC 54: Spiral Matrix](https://www.leetcode.com/problems/spiral-matrix/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/spiral-matrix/editorial/) *(may require premium)*

## Key Takeaways

1. **Boundary Management**: Track four boundaries and move them inward after each complete spiral
2. **Edge Cases**: Handle single row/column matrices with conditional checks
3. **Direction Changes**: Use direction vectors to simulate spiral movement
4. **Visited Marking**: Mark cells as visited to avoid revisiting them
