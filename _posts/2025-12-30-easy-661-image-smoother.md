---
layout: post
title: "[Easy] 661. Image Smoother"
date: 2025-12-30 18:30:00 -0700
categories: [leetcode, easy, matrix, array, simulation]
permalink: /2025/12/30/easy-661-image-smoother/
---
An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the red smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., we only count the present cells).

Given an `m x n` integer matrix `img` representing the grayscale of an image, return *the image after applying the smoother on each cell of it*.

## Thinking Process

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the red smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., we only count the present cells).

Given an `m x n` integer matrix `img` representing the grayscale of an image, return *the image after applying the smoother on each cell of it*.

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

### Complexity
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [661. Image Smoother](https://www.leetcode.com/problems/image-smoother/) - Current problem
- [289. Game of Life](https://www.leetcode.com/problems/game-of-life/) - Similar neighbor checking
- [733. Flood Fill](https://www.leetcode.com/problems/flood-fill/) - Matrix traversal
- [200. Number of Islands](https://www.leetcode.com/problems/number-of-islands/) - Neighbor exploration

## Tags

`Matrix`, `Array`, `Simulation`, `Easy`

## Key Takeaways

- Treat the grid as a graph with 4- or 8-directional neighbors.
- Row-major vs column-major traversal affects cache and logic.
- Boundary checks on every neighbor expansion.

## References

- [LC 661: Image Smoother on LeetCode](https://www.leetcode.com/problems/image-smoother/)
- [LeetCode Discuss — LC 661: Image Smoother](https://www.leetcode.com/problems/image-smoother/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/image-smoother/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
