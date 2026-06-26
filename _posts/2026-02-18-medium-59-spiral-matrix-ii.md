---
layout: post
title: "[Medium] 59. Spiral Matrix II"
date: 2026-02-18
categories: [leetcode, medium, matrix, simulation]
tags: [leetcode, medium, matrix, simulation, spiral]
permalink: /2026/02/18/medium-59-spiral-matrix-ii/
---
Given a positive integer `n`, generate an `n × n` matrix filled with elements from `1` to `n²` in spiral order (clockwise).

## Examples

**Example 1:**

```
Input: n = 3
Output:
1  2  3
8  9  4
7  6  5
```

**Example 2:**

```
Input: n = 1
Output: [[1]]
```

## Constraints

- `1 <= n <= 20`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Row/column traversal | $O(nm)$ | $O(1)$ | Simulation, spiral |
| BFS/DFS on grid | $O(nm)$ | $O(nm)$ | Islands, shortest path |
| **Matrix as graph** *(this problem)* | $O(nm)$ | $O(nm)$ | 4/8-directional neighbors |
| Transpose / rotate | $O(nm)$ | $O(1)$ | In-place rotation tricks |

## Thinking Process

### Core Observations

- The matrix is square
- We fill numbers `1 → n²` in a clockwise spiral
- This is a **simulation** problem -- no DP or graph tricks, just precise boundary control

### Layer-by-Layer (Boundary Shrinking)

Think of the matrix as concentric layers (rings). There are `⌈n/2⌉` layers. For each layer, fill four sides in order:

1. **Left → Right** (top row of this layer)
2. **Top → Bottom** (right column)
3. **Right → Left** (bottom row)
4. **Bottom → Top** (left column)

After each complete ring, shrink inward to the next layer.

### Walk-Through (n = 4)

```
Layer 0:  1  2  3  4    Layer 1:  .  .  .  .
         12  .  .  5              .  6  7  .
         11  .  .  6              . 10  .  .
         10  9  8  7              .  9  .  .

Layer 0 fills the outer ring (1–12)
Layer 1 fills the inner ring (13–16)
```

### Why Layer Index Works

For layer `k`:
- Top-left corner is at `(k, k)`
- Bottom-right corner is at `(n-k-1, n-k-1)`
- Each of the four sides has carefully adjusted start/end to avoid double-counting corners



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Grid traversal</text>

  <rect x="50" y="40" width="28" height="28" fill="#D4D8E0" stroke="#8B8680"/><rect x="78" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="106" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="40" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="50" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="78" y="68" width="28" height="28" fill="#E0D8E4" stroke="#A098A8"/>
  <rect x="106" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/><rect x="134" y="68" width="28" height="28" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="110" y="115" text-anchor="middle" font-size="11" fill="#6B6560">BFS/DFS flood from each cell</text>

</svg>

## Approach: Layer-by-Layer -- $O(n^2)$

Iterate over layers from `0` to `(n+1)/2 - 1`. For each layer, fill the four sides with incrementing counter.

{% raw %}
```cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> rtn(n, vector<int>(n));
        int cnt = 1;

        for (int layer = 0; layer < (n + 1) / 2; layer++) {
            for (int ptr = layer; ptr < n - layer; ptr++)
                rtn[layer][ptr] = cnt++;

            for (int ptr = layer + 1; ptr < n - layer; ptr++)
                rtn[ptr][n - layer - 1] = cnt++;

            for (int ptr = n - layer - 2; ptr >= layer; ptr--)
                rtn[n - layer - 1][ptr] = cnt++;

            for (int ptr = n - layer - 2; ptr > layer; ptr--)
                rtn[ptr][layer] = cnt++;
        }

        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Matrix as graph (this problem)

**Key idea:** ### Core Observations

**How the code works:**
- The matrix is square
- We fill numbers `1 → n²` in a clockwise spiral
- This is a **simulation** problem -- no DP or graph tricks, just precise boundary control
1. **Left → Right** (top row of this layer)
2. **Top → Bottom** (right column)
3. **Right → Left** (bottom row)

**Walkthrough** — input `n = 3`, expected output `1  2  3`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Alternative: Direction Array Simulation

Instead of explicit layer logic, use direction vectors and rotate when hitting a boundary or an already-filled cell. Often shorter code.

{% raw %}
```cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> mat(n, vector<int>(n, 0));
        int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
        int d = 0, r = 0, c = 0;

        for (int num = 1; num <= n * n; num++) {
            mat[r][c] = num;
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr < 0 || nr >= n || nc < 0 || nc >= n || mat[nr][nc] != 0) {
                d = (d + 1) % 4;
                nr = r + dirs[d][0];
                nc = c + dirs[d][1];
            }
            r = nr;
            c = nc;
        }

        return mat;
    }
};
```
{% endraw %}

**Time**: $O(n^2)$
**Space**: $O(n^2)$

## Common Mistakes

- **Double-filling the center**: when `n` is odd, the center cell belongs to only one side
- **Off-by-one on boundaries**: each side must carefully exclude the corners already filled by the previous side
- **Wrong loop bounds on the return sides**: the "right → left" and "bottom → top" loops start at `n - layer - 2`, not `n - layer - 1`

## Key Takeaways

- This is a pure **implementation accuracy** problem -- recognize it as spiral simulation immediately
- **Layer-by-layer** is safer and more explicit about boundaries
- **Direction array** is shorter but requires checking "already filled" cells
- Both approaches are $O(n^2)$ and optimal since every cell must be visited

## Related Problems

- [54. Spiral Matrix](https://www.leetcode.com/problems/spiral-matrix/) -- read a matrix in spiral order (the reverse operation)
- [885. Spiral Matrix III](https://www.leetcode.com/problems/spiral-matrix-iii/) -- spiral walk on a grid from a starting point
- [2326. Spiral Matrix IV](https://www.leetcode.com/problems/spiral-matrix-iv/) -- fill spiral from a linked list

## References

- [LC 59: Spiral Matrix II on LeetCode](https://www.leetcode.com/problems/spiral-matrix-ii/)
- [LeetCode Discuss — LC 59: Spiral Matrix II](https://www.leetcode.com/problems/spiral-matrix-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/spiral-matrix-ii/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
