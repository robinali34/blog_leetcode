---
layout: post
title: "[Medium] 417. Pacific Atlantic Water Flow"
date: 2025-10-19 11:43:11 -0700
categories: leetcode algorithm medium cpp dfs bfs graph problem-solving
---

# [Medium] 417. Pacific Atlantic Water Flow

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and the **Atlantic Ocean**. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a **2D list of grid coordinates** `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to **both the Pacific and Atlantic oceans**.

## Examples

**Example 1:**
```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following are the cells where water can flow to both Pacific and Atlantic oceans:
- [0,4]: Water flows from [0,4] to Pacific Ocean
- [1,3]: Water flows from [1,3] to Pacific Ocean
- [1,4]: Water flows from [1,4] to Pacific Ocean
- [2,2]: Water flows from [2,2] to Pacific Ocean
- [3,0]: Water flows from [3,0] to Pacific Ocean
- [3,1]: Water flows from [3,1] to Pacific Ocean
- [4,0]: Water flows from [4,0] to Pacific Ocean
```

**Example 2:**
```
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
Explanation: All cells can flow to both Pacific and Atlantic oceans.
```

## Constraints

- `m == heights.length`
- `n == heights[i].length`
- `1 <= m, n <= 200`
- `0 <= heights[i][j] <= 10^5`

## Solution: DFS from Ocean Boundaries

**Time Complexity:** O(m × n) where m and n are dimensions of the grid  
**Space Complexity:** O(m × n) for visited arrays and recursion stack

Use DFS from Pacific and Atlantic ocean boundaries to find all cells that can reach each ocean, then find the intersection.

```cpp
class Solution {
private:
    int m, n;
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int row, int col) {
        visited[row][col] = true;
        for(auto& dir: dirs) {
            int newRow = row + dir[0], newCol = col + dir[1];
            if(newRow < 0 || newRow >= m || newCol < 0 || newCol >= n) continue;
            if(visited[newRow][newCol] || heights[row][col] > heights[newRow][newCol]) continue;

            dfs(heights, visited, newRow, newCol);
        }
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size(), n = heights[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // DFS from Pacific Ocean boundaries (left and top edges)
        for(int i = 0; i < m; i++) dfs(heights, pacific, i, 0);
        for(int j = 0; j < n; j++) dfs(heights, pacific, 0, j);
        
        // DFS from Atlantic Ocean boundaries (right and bottom edges)
        for(int i = m - 1; i >= 0; i--) dfs(heights, atlantic, i, n - 1);
        for(int j = n - 1; j >= 0; j--) dfs(heights, atlantic, m - 1, j);

        // Find cells that can reach both oceans
        vector<vector<int>> rtn;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(pacific[i][j] && atlantic[i][j]) {
                    rtn.push_back({i, j});
                }
            }
        }
        return rtn;
    }
};
```

## How the Algorithm Works

**Key Insight:** Instead of checking if each cell can reach both oceans, start from ocean boundaries and find all reachable cells.

**Steps:**
1. **Create visited arrays** for Pacific and Atlantic oceans
2. **DFS from Pacific boundaries:**
   - Left edge: `(i, 0)` for all rows
   - Top edge: `(0, j)` for all columns
3. **DFS from Atlantic boundaries:**
   - Right edge: `(i, n-1)` for all rows
   - Bottom edge: `(m-1, j)` for all columns
4. **Find intersection:** Cells that can reach both oceans
5. **Return result** as list of coordinates

## Step-by-Step Example

### Example: `heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`

**Step 1: DFS from Pacific Ocean boundaries**

**Pacific boundaries (left and top edges):**
- Left edge: `(0,0), (1,0), (2,0), (3,0), (4,0)`
- Top edge: `(0,0), (0,1), (0,2), (0,3), (0,4)`

**DFS from Pacific boundaries:**
```
Pacific reachable cells:
[0,0] → [0,1] → [0,2] → [0,3] → [0,4]
[1,0] → [1,1] → [1,2] → [1,3] → [1,4]
[2,0] → [2,1] → [2,2] → [2,3] → [2,4]
[3,0] → [3,1] → [3,2] → [3,3] → [3,4]
[4,0] → [4,1] → [4,2] → [4,3] → [4,4]
```

**Step 2: DFS from Atlantic Ocean boundaries**

**Atlantic boundaries (right and bottom edges):**
- Right edge: `(0,4), (1,4), (2,4), (3,4), (4,4)`
- Bottom edge: `(4,0), (4,1), (4,2), (4,3), (4,4)`

**DFS from Atlantic boundaries:**
```
Atlantic reachable cells:
[0,4] → [0,3] → [0,2] → [0,1] → [0,0]
[1,4] → [1,3] → [1,2] → [1,1] → [1,0]
[2,4] → [2,3] → [2,2] → [2,1] → [2,0]
[3,4] → [3,3] → [3,2] → [3,1] → [3,0]
[4,4] → [4,3] → [4,2] → [4,1] → [4,0]
```

**Step 3: Find intersection**

**Cells that can reach both oceans:**
- `[0,4]`: Can reach Pacific and Atlantic
- `[1,3]`: Can reach Pacific and Atlantic
- `[1,4]`: Can reach Pacific and Atlantic
- `[2,2]`: Can reach Pacific and Atlantic
- `[3,0]`: Can reach Pacific and Atlantic
- `[3,1]`: Can reach Pacific and Atlantic
- `[4,0]`: Can reach Pacific and Atlantic

**Final result:** `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`

## Algorithm Breakdown

### DFS Function:
```cpp
void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int row, int col) {
    visited[row][col] = true;
    for(auto& dir: dirs) {
        int newRow = row + dir[0], newCol = col + dir[1];
        if(newRow < 0 || newRow >= m || newCol < 0 || newCol >= n) continue;
        if(visited[newRow][newCol] || heights[row][col] > heights[newRow][newCol]) continue;

        dfs(heights, visited, newRow, newCol);
    }
}
```

**Process:**
1. **Mark current cell** as visited
2. **Check all 4 directions** (up, down, left, right)
3. **Skip invalid cells** (out of bounds, already visited)
4. **Skip higher cells** (water can't flow uphill)
5. **Recursively visit** reachable cells

### Boundary DFS:
```cpp
// Pacific boundaries
for(int i = 0; i < m; i++) dfs(heights, pacific, i, 0);
for(int j = 0; j < n; j++) dfs(heights, pacific, 0, j);

// Atlantic boundaries
for(int i = m - 1; i >= 0; i--) dfs(heights, atlantic, i, n - 1);
for(int j = n - 1; j >= 0; j--) dfs(heights, atlantic, m - 1, j);
```

**Process:**
1. **Pacific boundaries:** Left edge and top edge
2. **Atlantic boundaries:** Right edge and bottom edge
3. **DFS from each boundary** to find reachable cells
4. **Mark visited cells** in respective arrays

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Pacific DFS | O(m × n) | O(m × n) |
| Atlantic DFS | O(m × n) | O(m × n) |
| Intersection | O(m × n) | O(1) |
| **Total** | **O(m × n)** | **O(m × n)** |

Where m and n are the dimensions of the grid.

## Edge Cases

1. **Single cell:** `heights = [[5]]` → `[[0,0]]`
2. **All same height:** `heights = [[1,1],[1,1]]` → `[[0,0],[0,1],[1,0],[1,1]]`
3. **Increasing heights:** `heights = [[1,2],[3,4]]` → `[[0,0],[0,1],[1,0],[1,1]]`
4. **Decreasing heights:** `heights = [[4,3],[2,1]]` → `[[0,0],[0,1],[1,0],[1,1]]`

## Key Insights

### Reverse Thinking:
1. **Instead of checking** if each cell can reach oceans
2. **Start from ocean boundaries** and find reachable cells
3. **Much more efficient** than checking each cell individually
4. **O(m × n) complexity** instead of O(m² × n²)

### DFS Properties:
1. **Visited tracking:** Prevents infinite loops
2. **Boundary checking:** Ensures valid coordinates
3. **Height constraint:** Water flows downhill or level
4. **Recursive exploration:** Finds all reachable cells

## Detailed Example Walkthrough

### Example: `heights = [[2,1],[1,2]]`

**Step 1: Pacific boundaries**
- Left edge: `(0,0), (1,0)`
- Top edge: `(0,0), (0,1)`

**Pacific DFS:**
```
[0,0] → [0,1] → [1,1]
[1,0] → [1,1]
```

**Step 2: Atlantic boundaries**
- Right edge: `(0,1), (1,1)`
- Bottom edge: `(1,0), (1,1)`

**Atlantic DFS:**
```
[0,1] → [0,0] → [1,0]
[1,1] → [1,0]
```

**Step 3: Intersection**
**All cells can reach both oceans:**
- `[0,0]`: Pacific ✓, Atlantic ✓
- `[0,1]`: Pacific ✓, Atlantic ✓
- `[1,0]`: Pacific ✓, Atlantic ✓
- `[1,1]`: Pacific ✓, Atlantic ✓

**Final result:** `[[0,0],[0,1],[1,0],[1,1]]`

## Alternative Approaches

### Approach 1: BFS from Boundaries
```cpp
class Solution {
private:
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    void bfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, queue<pair<int,int>>& q) {
        while(!q.empty()) {
            auto [row, col] = q.front();
            q.pop();
            
            for(auto& dir: dirs) {
                int newRow = row + dir[0], newCol = col + dir[1];
                if(newRow < 0 || newRow >= heights.size() || newCol < 0 || newCol >= heights[0].size()) continue;
                if(visited[newRow][newCol] || heights[row][col] > heights[newRow][newCol]) continue;
                
                visited[newRow][newCol] = true;
                q.push({newRow, newCol});
            }
        }
    }
    
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        queue<pair<int,int>> pacificQ, atlanticQ;
        
        // Add Pacific boundaries
        for(int i = 0; i < m; i++) {
            pacificQ.push({i, 0});
            pacific[i][0] = true;
        }
        for(int j = 0; j < n; j++) {
            pacificQ.push({0, j});
            pacific[0][j] = true;
        }
        
        // Add Atlantic boundaries
        for(int i = 0; i < m; i++) {
            atlanticQ.push({i, n-1});
            atlantic[i][n-1] = true;
        }
        for(int j = 0; j < n; j++) {
            atlanticQ.push({m-1, j});
            atlantic[m-1][j] = true;
        }
        
        bfs(heights, pacific, pacificQ);
        bfs(heights, atlantic, atlanticQ);
        
        vector<vector<int>> result;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }
        return result;
    }
};
```

**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n)

### Approach 2: Union-Find
```cpp
class Solution {
private:
    vector<int> parent;
    vector<int> rank;
    
    int find(int x) {
        if(parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int px = find(x), py = find(y);
        if(px == py) return;
        
        if(rank[px] < rank[py]) {
            parent[px] = py;
        } else if(rank[px] > rank[py]) {
            parent[py] = px;
        } else {
            parent[py] = px;
            rank[px]++;
        }
    }
    
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        int total = m * n;
        parent.resize(total);
        rank.resize(total, 0);
        iota(parent.begin(), parent.end(), 0);
        
        // Connect cells that can flow to each other
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                int curr = i * n + j;
                if(i > 0 && heights[i][j] >= heights[i-1][j]) {
                    unite(curr, (i-1) * n + j);
                }
                if(j > 0 && heights[i][j] >= heights[i][j-1]) {
                    unite(curr, i * n + (j-1));
                }
            }
        }
        
        // Find cells that can reach both oceans
        vector<vector<int>> result;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                int curr = i * n + j;
                bool canReachPacific = false, canReachAtlantic = false;
                
                // Check if can reach Pacific
                for(int k = 0; k < m; k++) {
                    if(find(curr) == find(k * n + 0)) {
                        canReachPacific = true;
                        break;
                    }
                }
                for(int k = 0; k < n; k++) {
                    if(find(curr) == find(0 * n + k)) {
                        canReachPacific = true;
                        break;
                    }
                }
                
                // Check if can reach Atlantic
                for(int k = 0; k < m; k++) {
                    if(find(curr) == find(k * n + (n-1))) {
                        canReachAtlantic = true;
                        break;
                    }
                }
                for(int k = 0; k < n; k++) {
                    if(find(curr) == find((m-1) * n + k)) {
                        canReachAtlantic = true;
                        break;
                    }
                }
                
                if(canReachPacific && canReachAtlantic) {
                    result.push_back({i, j});
                }
            }
        }
        
        return result;
    }
};
```

**Time Complexity:** O(m × n × α(m × n))  
**Space Complexity:** O(m × n)

## Common Mistakes

1. **Wrong direction:** Starting from each cell instead of ocean boundaries
2. **Missing boundary cells:** Not including all boundary cells in DFS
3. **Incorrect height check:** Not handling equal heights correctly
4. **Out of bounds:** Not checking array bounds properly

## Related Problems

- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
- [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [1020. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/)

## Why This Solution Works

### Reverse Thinking:
1. **Instead of checking** if each cell can reach oceans
2. **Start from ocean boundaries** and find reachable cells
3. **Much more efficient** than checking each cell individually
4. **O(m × n) complexity** instead of O(m² × n²)

### DFS Properties:
1. **Visited tracking:** Prevents infinite loops
2. **Boundary checking:** Ensures valid coordinates
3. **Height constraint:** Water flows downhill or level
4. **Recursive exploration:** Finds all reachable cells

### Key Algorithm Properties:
1. **Correctness:** Always produces valid result
2. **Optimality:** Produces correct ocean reachability
3. **Efficiency:** O(m × n) time complexity
4. **Simplicity:** Easy to understand and implement
