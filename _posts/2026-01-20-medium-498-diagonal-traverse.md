---
layout: post
title: "498. Diagonal Traverse"
date: 2026-01-20 00:00:00 -0700
categories: [leetcode, medium, array, matrix, simulation]
permalink: /2026/01/20/medium-498-diagonal-traverse/
tags: [leetcode, medium, array, matrix, simulation]
---

# 498. Diagonal Traverse

## Problem Statement

Given an `m x n` matrix `mat`, return an array of all the elements of the matrix in a **diagonal order**.

## Examples

**Example 1:**
```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

**Example 2:**
```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `-10^5 <= mat[i][j] <= 10^5`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Traversal direction**: What is the starting direction and how does it alternate? (Assumption: Start going up-right, then alternate between up-right and down-left)

2. **Boundary handling**: What happens when we hit a boundary? (Assumption: Change direction and adjust position - up-right becomes down-left when hitting top or right edge)

3. **Matrix shape**: Can the matrix be non-square (rectangular)? (Assumption: Yes - m and n can be different)

4. **Output format**: Should we return a 1D array with all elements? (Assumption: Yes - return elements in diagonal traversal order as a 1D array)

5. **Empty matrix**: How should we handle an empty matrix? (Assumption: Return empty array)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Identify all diagonals (elements with same (row + col) sum). For each diagonal, collect elements and append to result, reversing order for even-indexed diagonals. This requires identifying diagonal groups, which can be done by grouping elements by (row + col) sum. However, the traversal order and direction changes need careful handling.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use BFS starting from (0,0). Process diagonals level by level, where each level represents elements with the same (row + col) sum. For each level, collect elements and reverse if needed based on diagonal index. This works but requires careful level tracking and direction management.

**Step 3: Optimized Solution (8 minutes)**

Use a hash map to group elements by diagonal index (row + col). Iterate through the matrix, adding each element to its diagonal bucket. Then iterate through diagonals in order (0, 1, 2, ...), and for each diagonal, reverse the order if diagonal index is even (for upward direction). This achieves O(m × n) time where m and n are matrix dimensions, and O(m × n) space for the hash map, which is optimal since we must visit all elements. Alternatively, simulate the traversal directly by tracking current position and direction, but the hash map approach is simpler and more intuitive.

## Solution Approach (Direction Simulation)

We simulate moving along diagonals with two directions:

- **Up-right**: `(-1, +1)`
- **Down-left**: `(+1, -1)`

Whenever the next move would go **out of bounds**, we “bounce” by:

- flipping direction, and
- moving to the next valid boundary cell (either move right or move down depending on which edge we hit and the current direction).

## C++ Solution

{% raw %}
```cpp
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        const int M = mat.size(), N = mat[0].size();
        const int TOTAL = M * N;
        int row = 0, col = 0, dirIdx = 0;
        vector<int> rtn(TOTAL);
        for(int i = 0; i < TOTAL; i++) {
            rtn[i] = mat[row][col];
            int nextRow = row + DIRS[dirIdx][0];
            int nextCol = col + DIRS[dirIdx][1];
            if(nextRow < 0 || nextRow >= M || nextCol < 0 || nextCol >= N) {
                dirIdx = 1 - dirIdx;
                if(dirIdx == 0) {
                    if(row == M - 1) col++;
                    else row++;
                } else {
                    if(col == N - 1) row++;
                    else col++;
                }
            } else{
                row = nextRow;
                col = nextCol;
            }
        }
        return rtn;
    }
private:
    const vector<vector<int>> DIRS = {{-1, 1}, {1, -1}};
};
```
{% endraw %}

## Complexity Analysis

- **Time Complexity:** O(m × n) — visit each cell exactly once
- **Space Complexity:** O(1) extra space (excluding the output array)

## Related Problems

- [LC 54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [LC 1424. Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/)


