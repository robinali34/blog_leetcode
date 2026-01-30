---
layout: post
title: "661. Image Smoother"
date: 2025-12-30 18:30:00 -0700
categories: [leetcode, easy, matrix, array, simulation]
permalink: /2025/12/30/easy-661-image-smoother/
---

# 661. Image Smoother

## Problem Statement

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the red smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., we only count the present cells).

Given an `m x n` integer matrix `img` representing the grayscale of an image, return *the image after applying the smoother on each cell of it*.

## Examples

**Example 1:**
```
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.833) = 0
For the point (1,1): floor(8/9) = floor(0.888) = 0
```

**Example 2:**
```
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+100+200+50+200+100)/6) = floor(141.666) = 141
For the point (1,1): floor((50+200+100+200+50+200+100+200+100)/9) = floor(138.888) = 138
```

## Constraints

- `m == img.length`
- `n == img[i].length`
- `1 <= m, n <= 200`
- `0 <= img[i][j] <= 255`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Smoothing definition**: How is smoothing calculated? (Assumption: Average of all 8 surrounding cells plus the cell itself - 3x3 neighborhood)

2. **Boundary handling**: How should we handle cells at the boundary? (Assumption: Only average cells that exist - fewer neighbors for boundary cells)

3. **Rounding**: How should we round the average? (Assumption: Floor division - truncate to integer, rounding down)

4. **In-place modification**: Should we modify the original image or create a new one? (Assumption: Create a new image - don't modify original during calculation)

5. **Neighbor count**: How many neighbors does a corner cell have? (Assumption: 3 neighbors (plus itself = 4 total); edge cells have 5 neighbors (plus itself = 6 total)

## Interview Deduction Process (10 minutes)

### Step 1: Brute-Force Approach (2 minutes)
**Initial Thought**: "I need to smooth each pixel. Let me check all neighbors for each cell."

**Naive Solution**: For each cell, check all 8 neighbors plus itself, sum values, divide by count. Handle boundaries by checking if indices are valid.

**Complexity**: O(m × n × 9) = O(m × n) time, O(m × n) space

**Issues**:
- Lots of boundary checking
- Repetitive neighbor access
- Can be optimized but logic is correct

### Step 2: Semi-Optimized Approach (3 minutes)
**Insight**: "I can use nested loops with offsets to check neighbors more systematically."

**Improved Solution**: For each cell, use nested loops with offsets [-1, 0, 1] for both row and column. Count valid neighbors and sum their values.

**Complexity**: O(m × n × 9) = O(m × n) time, O(m × n) space

**Improvements**:
- More systematic neighbor checking
- Cleaner code structure
- Still O(m × n) which is optimal

### Step 3: Optimized Solution (5 minutes)
**Final Optimization**: "The approach is already optimal. Can optimize by precomputing neighbor offsets or using helper function."

**Best Solution**: Use offset-based neighbor checking. Precompute valid neighbor offsets or use helper function for clarity. O(m × n) is optimal since we must process each cell.

**Key Realizations**:
1. O(m × n) time is optimal - must process each cell
2. O(m × n) space is optimal - need result matrix
3. Offset-based neighbor checking is clean
4. Boundary checking is necessary and handled naturally

## Solution Approach

This problem requires applying a 3×3 smoothing filter to each cell in the image. For each cell, we calculate the average of itself and its 8 neighbors (if they exist), then round down the result.

### Key Insights:

1. **3×3 Neighborhood**: For each cell `(i, j)`, check all cells in range `[i-1, i+1] × [j-1, j+1]`
2. **Boundary Handling**: Only count neighbors that exist (within matrix bounds)
3. **Average Calculation**: Sum all valid neighbors, divide by count, round down
4. **New Matrix**: Create new matrix to store results (don't modify original)

### Algorithm:

1. **Iterate through each cell**: Process every cell in the matrix
2. **Check 3×3 neighborhood**: For each cell, check all 9 positions (including itself)
3. **Count valid neighbors**: Only include neighbors within bounds
4. **Calculate average**: Sum valid neighbors, divide by count
5. **Store result**: Put result in new matrix

## Solution

### **Solution: Direct Neighbor Checking**

```cpp
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        const int m = img.size(), n = img[0].size();
        vector<vector<int>> rtn(m, vector<int>(n));
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                int num = 0, sum = 0;
                for(int x = i - 1; x <= i + 1; x++) {
                    for(int y = j - 1; y <= j + 1; y++) {
                        if(x >= 0 && x < m && y >= 0 && y < n) {
                            num++;
                            sum += img[x][y];
                        }
                    }
                }
                rtn[i][j] = sum / num;
            }
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize Result Matrix (Lines 4-5)**:
   - Get dimensions: `m` rows, `n` columns
   - Create result matrix `rtn` of same size

2. **Iterate Through Each Cell (Lines 6-7)**:
   - Outer loops: iterate through every cell `(i, j)`

3. **Check 3×3 Neighborhood (Lines 8-15)**:
   - Inner loops: check all 9 positions in 3×3 grid centered at `(i, j)`
   - Range: `[i-1, i+1] × [j-1, j+1]`
   - **Boundary check**: Only include valid neighbors within bounds
   - Count valid neighbors: `num++`
   - Sum values: `sum += img[x][y]`

4. **Calculate Average (Line 16)**:
   - Divide sum by count: `sum / num`
   - Integer division automatically rounds down

5. **Return Result (Line 19)**:
   - Return smoothed image matrix

### **Example Walkthrough:**

**For `img = [[1,1,1],[1,0,1],[1,1,1]]`:**

```
Step 1: Process cell (0,0) - top-left corner
Neighbors to check: (-1,-1) to (1,1)
Valid neighbors: (0,0), (0,1), (1,0), (1,1)
Values: 1, 1, 1, 0
Sum = 3, Count = 4
Result: 3/4 = 0

Step 2: Process cell (0,1) - top edge
Neighbors to check: (-1,0) to (1,2)
Valid neighbors: (0,0), (0,1), (0,2), (1,0), (1,1), (1,2)
Values: 1, 1, 1, 1, 0, 1
Sum = 5, Count = 6
Result: 5/6 = 0

Step 3: Process cell (1,1) - center
Neighbors to check: (0,0) to (2,2)
Valid neighbors: All 9 positions
Values: 1,1,1, 1,0,1, 1,1,1
Sum = 8, Count = 9
Result: 8/9 = 0

Final result: [[0,0,0],[0,0,0],[0,0,0]]
```

**Visual Representation:**

```
Original:          Neighbors for (1,1):    Smoothed:
[1, 1, 1]          [1, 1, 1]              [0, 0, 0]
[1, 0, 1]    →     [1, 0, 1]         →    [0, 0, 0]
[1, 1, 1]          [1, 1, 1]              [0, 0, 0]
                    ↑ center
```

## Algorithm Breakdown

### **Key Insight: Boundary Handling**

The algorithm handles boundaries correctly by checking bounds before accessing:
```cpp
if(x >= 0 && x < m && y >= 0 && y < n) {
    num++;
    sum += img[x][y];
}
```

This ensures:
- **Corner cells**: Only count 4 neighbors (including itself)
- **Edge cells**: Only count 6 neighbors (including itself)
- **Center cells**: Count all 9 neighbors (including itself)

### **Neighborhood Pattern**

For each cell `(i, j)`, the 3×3 neighborhood includes:
```
(i-1, j-1)  (i-1, j)   (i-1, j+1)
(i, j-1)    (i, j)     (i, j+1)
(i+1, j-1)  (i+1, j)   (i+1, j+1)
```

### **Average Calculation**

Integer division automatically rounds down:
- `3 / 4 = 0` (not 0.75)
- `5 / 6 = 0` (not 0.833)
- `8 / 9 = 0` (not 0.888)

## Complexity Analysis

### **Time Complexity:** O(m × n)
- **Outer loops**: O(m × n) - iterate through each cell
- **Inner loops**: O(9) = O(1) - check 9 neighbors (constant)
- **Total**: O(m × n) where m = rows, n = columns

### **Space Complexity:** O(m × n)
- **Result matrix**: O(m × n) - store smoothed image
- **Variables**: O(1) - constant space for counters
- **Total**: O(m × n)

## Key Points

1. **3×3 Filter**: Standard image smoothing filter
2. **Boundary Handling**: Only count existing neighbors
3. **Integer Division**: Automatically rounds down
4. **New Matrix**: Don't modify original (use new matrix)
5. **Simple Logic**: Straightforward nested loop approach

## Alternative Approaches

### **Approach 1: Direct Neighbor Checking (Current Solution)**
- **Time**: O(m × n)
- **Space**: O(m × n)
- **Best for**: Simple and clear implementation

### **Approach 2: Direction Array**
- **Time**: O(m × n)
- **Space**: O(m × n)
- **Use direction offsets**: `int dirs[9][2] = {% raw %}{{-1,-1}, {-1,0}, ...}{% endraw %}`

### **Approach 3: In-Place with Temporary Storage**
- **Time**: O(m × n)
- **Space**: O(1) extra space (but need to handle carefully)
- **Modify original**: Store results in original matrix (requires careful handling)

## Detailed Example Walkthrough

### **Example: `img = [[100,200,100],[200,50,200],[100,200,100]]`**

```
Step 1: Process cell (0,0) - corner
Neighbors: (0,0), (0,1), (1,0), (1,1)
Values: 100, 200, 200, 50
Sum = 550, Count = 4
Result: 550/4 = 137

Step 2: Process cell (0,1) - top edge
Neighbors: (0,0), (0,1), (0,2), (1,0), (1,1), (1,2)
Values: 100, 200, 100, 200, 50, 200
Sum = 850, Count = 6
Result: 850/6 = 141

Step 3: Process cell (1,1) - center
Neighbors: All 9 positions
Values: 100,200,100, 200,50,200, 100,200,100
Sum = 1250, Count = 9
Result: 1250/9 = 138

Final result: [[137,141,137],[141,138,141],[137,141,137]]
```

## Edge Cases

1. **Single cell**: `[[5]]` → `[[5]]` (only itself)
2. **Single row**: `[[1,2,3]]` → average of 3 neighbors per cell
3. **Single column**: `[[1],[2],[3]]` → average of 3 neighbors per cell
4. **All same values**: `[[5,5,5],[5,5,5],[5,5,5]]` → unchanged
5. **Large values**: Works with values up to 255

## Related Problems

- [661. Image Smoother](https://leetcode.com/problems/image-smoother/) - Current problem
- [289. Game of Life](https://leetcode.com/problems/game-of-life/) - Similar neighbor checking
- [733. Flood Fill](https://leetcode.com/problems/flood-fill/) - Matrix traversal
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) - Neighbor exploration

## Tags

`Matrix`, `Array`, `Simulation`, `Easy`

