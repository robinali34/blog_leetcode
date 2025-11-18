---
layout: post
title: "[Medium] 1424. Diagonal Traverse II"
date: 2025-11-17 00:00:00 -0800
categories: leetcode algorithm medium cpp array matrix hash-map bfs problem-solving
---

# [Medium] 1424. Diagonal Traverse II

Given a 2D integer array `nums`, return *all elements of `nums` in diagonal order*.

## Examples

**Example 1:**
```
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
```

**Example 2:**
```
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

**Example 3:**
```
Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]
```

**Example 4:**
```
Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i].length <= 10^5`
- `1 <= sum(nums[i].length) <= 10^5`
- `1 <= nums[i][j] <= 10^9`

## Solution: Hash Map Grouping and BFS Approaches

**Time Complexity:** O(n) where n is total number of elements  
**Space Complexity:** O(n)

We can solve this problem using two approaches:
1. **Hash Map Grouping**: Group elements by their diagonal index (row + col), then iterate through diagonals in order.
2. **BFS Traversal**: Use a queue to traverse diagonally, processing elements level by level.

### Solution 1: Hash Map Grouping (C++23 Optimized)

**Key Insight:** Elements on the same diagonal have the same sum of row and column indices (`row + col`). We can group all elements by this diagonal index, then iterate through diagonals in ascending order.

```cpp
class Solution {
public:
    [[nodiscard]] vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        unordered_map<int, vector<int>> groups;
        
        // Traverse from bottom to top to maintain diagonal order
        for (int row = static_cast<int>(nums.size()) - 1; row >= 0; --row) {
            for (int col = 0; col < static_cast<int>(nums[row].size()); ++col) {
                const int diagonal = row + col;
                groups[diagonal].push_back(nums[row][col]);
            }
        }
        
        vector<int> rtn;
        rtn.reserve(nums.size() * nums[0].size()); // Reserve space for efficiency
        
        // Process diagonals in order (0, 1, 2, ...)
        int curr = 0;
        while (groups.contains(curr)) {
            for (const int num : groups[curr]) {
                rtn.push_back(num);
            }
            ++curr;
        }
        
        return rtn;
    }
};
```

**C++23 Optimizations:**
- `[[nodiscard]]` attribute to prevent ignoring return value
- `static_cast<int>()` for explicit type conversions
- `const` qualifier for diagonal index
- `groups.contains(curr)` instead of `groups.find(curr) != groups.end()` (C++20)
- `reserve()` to pre-allocate memory
- Range-based for loop with `const int num`

**How it works:**
1. **Group by Diagonal**: For each element at `(row, col)`, calculate `diagonal = row + col` and add it to the corresponding group.
2. **Bottom-to-Top Traversal**: We traverse rows from bottom to top so that when we process diagonals in order, elements appear in the correct sequence.
3. **Sequential Processing**: Process diagonals starting from 0, adding all elements in each diagonal group to the result.

### Solution 2: BFS Traversal (C++23 Optimized)

**Key Insight:** We can use BFS starting from `(0, 0)` and traverse diagonally. For each cell, we explore:
- The cell below (if in first column): `(row + 1, 0)`
- The cell to the right: `(row, col + 1)`

```cpp
#include <queue>
#include <utility>

class Solution {
public:
    [[nodiscard]] vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        queue<pair<int, int>> queue;
        queue.push({0, 0});
        vector<int> rtn;
        rtn.reserve(nums.size() * nums[0].size());
        
        while (!queue.empty()) {
            const auto [row, col] = queue.front();
            queue.pop();
            
            rtn.push_back(nums[row][col]);
            
            // If in first column, add cell below
            if (col == 0 && row + 1 < static_cast<int>(nums.size())) {
                queue.push({row + 1, col});
            }
            
            // Add cell to the right
            if (col + 1 < static_cast<int>(nums[row].size())) {
                queue.push({row, col + 1});
            }
        }
        
        return rtn;
    }
};
```

**C++23 Optimizations:**
- `[[nodiscard]]` attribute
- Structured bindings `const auto [row, col]` for pair unpacking
- `static_cast<int>()` for explicit conversions
- `reserve()` for memory pre-allocation
- `const` qualifiers where appropriate

**How it works:**
1. **Start at Origin**: Begin BFS from `(0, 0)`.
2. **Process Current Cell**: Add the current cell's value to the result.
3. **Explore Neighbors**:
   - If in the first column (`col == 0`), add the cell below: `(row + 1, 0)`
   - Always add the cell to the right: `(row, col + 1)`
4. **Continue BFS**: Process all cells in the queue until empty.

## Step-by-Step Example

**Input:** `nums = [[1,2,3],[4,5,6],[7,8,9]]`

### Solution 1: Hash Map Approach

| Step | Row | Col | Diagonal | Groups |
|------|-----|-----|----------|--------|
| 1 | 2 | 0 | 2 | `{2: [7]}` |
| 2 | 2 | 1 | 3 | `{2: [7], 3: [8]}` |
| 3 | 2 | 2 | 4 | `{2: [7], 3: [8], 4: [9]}` |
| 4 | 1 | 0 | 1 | `{1: [4], 2: [7], 3: [8], 4: [9]}` |
| 5 | 1 | 1 | 2 | `{1: [4], 2: [7,5], 3: [8], 4: [9]}` |
| 6 | 1 | 2 | 3 | `{1: [4], 2: [7,5], 3: [8,6], 4: [9]}` |
| 7 | 0 | 0 | 0 | `{0: [1], 1: [4], 2: [7,5], 3: [8,6], 4: [9]}` |
| 8 | 0 | 1 | 1 | `{0: [1], 1: [4,2], 2: [7,5], 3: [8,6], 4: [9]}` |
| 9 | 0 | 2 | 2 | `{0: [1], 1: [4,2], 2: [7,5,3], 3: [8,6], 4: [9]}` |

**Processing diagonals:**
- Diagonal 0: `[1]` → `[1]`
- Diagonal 1: `[4,2]` → `[1,4,2]`
- Diagonal 2: `[7,5,3]` → `[1,4,2,7,5,3]`
- Diagonal 3: `[8,6]` → `[1,4,2,7,5,3,8,6]`
- Diagonal 4: `[9]` → `[1,4,2,7,5,3,8,6,9]`

**Output:** `[1,4,2,7,5,3,8,6,9]`

### Solution 2: BFS Approach

| Step | Queue | Process | Result | Next Moves |
|------|-------|---------|--------|------------|
| 0 | `[(0,0)]` | - | `[]` | - |
| 1 | `[(0,0)]` | `(0,0)` → 1 | `[1]` | `(1,0), (0,1)` |
| 2 | `[(1,0), (0,1)]` | `(1,0)` → 4 | `[1,4]` | `(2,0), (1,1)` |
| 3 | `[(0,1), (2,0), (1,1)]` | `(0,1)` → 2 | `[1,4,2]` | `(0,2)` |
| 4 | `[(2,0), (1,1), (0,2)]` | `(2,0)` → 7 | `[1,4,2,7]` | `(2,1)` |
| 5 | `[(1,1), (0,2), (2,1)]` | `(1,1)` → 5 | `[1,4,2,7,5]` | `(1,2)` |
| 6 | `[(0,2), (2,1), (1,2)]` | `(0,2)` → 3 | `[1,4,2,7,5,3]` | - |
| 7 | `[(2,1), (1,2)]` | `(2,1)` → 8 | `[1,4,2,7,5,3,8]` | `(2,2)` |
| 8 | `[(1,2), (2,2)]` | `(1,2)` → 6 | `[1,4,2,7,5,3,8,6]` | - |
| 9 | `[(2,2)]` | `(2,2)` → 9 | `[1,4,2,7,5,3,8,6,9]` | - |

**Output:** `[1,4,2,7,5,3,8,6,9]`

## Visual Representation

```
Matrix:
    0  1  2
0 [ 1  2  3 ]
1 [ 4  5  6 ]
2 [ 7  8  9 ]

Diagonals (row + col):
    0  1  2
0 [ 0  1  2 ]
1 [ 1  2  3 ]
2 [ 2  3  4 ]

Diagonal Traversal:
Diagonal 0: [1]
Diagonal 1: [4, 2]
Diagonal 2: [7, 5, 3]
Diagonal 3: [8, 6]
Diagonal 4: [9]

Result: [1, 4, 2, 7, 5, 3, 8, 6, 9]
```

## Key Insights

1. **Diagonal Property**: Elements on the same diagonal share the same `row + col` sum.
2. **Traversal Order**: Bottom-to-top traversal ensures correct ordering when processing diagonals sequentially.
3. **BFS Alternative**: BFS naturally explores diagonals when we prioritize right moves over down moves.
4. **Jagged Arrays**: Both solutions handle jagged arrays (rows of different lengths) correctly.

## Complexity Analysis

### Solution 1: Hash Map
- **Time:** O(n) - Each element is visited once
- **Space:** O(n) - Hash map stores all elements

### Solution 2: BFS
- **Time:** O(n) - Each element is processed once
- **Space:** O(n) - Queue can contain up to O(n) elements in worst case

## When to Use Each Approach

- **Hash Map Approach**: More intuitive, easier to understand the diagonal grouping concept.
- **BFS Approach**: More natural for graph-like traversal, but requires careful neighbor selection logic.

Both approaches are efficient and handle jagged arrays well. Choose based on your preference and coding style.

