---
layout: post
title: "[Medium] 240. Search a 2D Matrix II"
date: 2025-10-07 22:01:10 -0700
categories: leetcode algorithm medium cpp binary-search matrix 2d-array divide-conquer search optimization problem-solving
---
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

## Thinking Process

1. **Matrix properties** allow elimination strategies

- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.



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
| **Standard binary search** *(this problem)* | $O(\log n)$ | $O(1)$ | Sorted array, `left <= right` |
| Lower / upper bound | $O(\log n)$ | $O(1)$ | First/last position, insert index |
| Binary search on rotated array | $O(\log n)$ | $O(1)$ | Identify sorted half, discard other |
| Binary search on answer | $O(n \log M)$ | $O(1)$ | Monotonic predicate over search space |

## Solution

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

### Solution Explanation

**Approach:** Standard binary search (this problem)

**Key idea:** 1. **Matrix properties** allow elimination strategies

**How the code works:**
1. **Matrix properties** allow elimination strategies
- The search space must shrink monotonically each step.
- Decide which half still satisfies the predicate, discard the other.
- Use `mid = left + (right - left) / 2` to avoid overflow.

**Walkthrough** — input `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5`, expected output `true`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
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

## Why Top-Right Works

- **If current element > target**: All elements in current column are ≥ current element, so eliminate column
- **If current element < target**: All elements in current row are ≤ current element, so eliminate row
- **Each step eliminates** either a row or column, guaranteeing O(m + n) steps

## Related Problems

- [74. Search a 2D Matrix](https://www.leetcode.com/problems/search-a-2d-matrix/) - Strictly sorted matrix
- [378. Kth Smallest Element in a Sorted Matrix](https://www.leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) - Finding kth element
- [1428. Leftmost Column with at Least a One](https://www.leetcode.com/problems/leftmost-column-with-at-least-a-one/) - Binary matrix search

## References

- [LC 240: Search a 2D Matrix II on LeetCode](https://www.leetcode.com/problems/search-a-2d-matrix-ii/)
- [LeetCode Discuss — LC 240: Search a 2D Matrix II](https://www.leetcode.com/problems/search-a-2d-matrix-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/search-a-2d-matrix-ii/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Matrix properties** allow elimination strategies
2. **Top-right approach** is optimal with O(m + n) time
3. **Binary search per row** is simple but not optimal
4. **Divide and conquer** provides good average performance
5. **Elimination strategy** leverages sorted properties
