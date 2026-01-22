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


