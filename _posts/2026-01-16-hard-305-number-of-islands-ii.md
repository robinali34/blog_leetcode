---
layout: post
title: "305. Number of Islands II"
date: 2026-01-16 00:00:00 -0700
categories: [leetcode, hard, array, union-find, graph]
permalink: /2026/01/16/hard-305-number-of-islands-ii/
tags: [leetcode, hard, array, union-find, disjoint-set, incremental, dynamic]
---

# 305. Number of Islands II

## Problem Statement

You are given an empty 2D binary grid `grid` of size `m x n`. The grid represents a map where `0`'s represent **water** and `1`'s represent **land**. Initially, all the cells of `grid` are water cells (i.e., all the cells are `0`'s).

We may perform an **add land** operation which turns the water at position into a land. You are given an array `positions` where `positions[i] = [ri, ci]` is the position `(ri, ci)` at which we should operate the `i`th operation.

Return *an array of integers* `answer` *where* `answer[i]` *is the number of islands after turning the cell* `(ri, ci)` *into a land*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Examples

**Example 1:**
```
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
```

**Example 2:**
```
Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
```

## Constraints

- `1 <= m, n, positions.length <= 10^4`
- `1 <= m * n <= 10^4`
- `positions[i].length == 2`
- `0 <= ri < m`
- `0 <= ci < n`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Island definition**: What is an island? (Assumption: Group of connected land cells (1s) - horizontally or vertically adjacent)

2. **Dynamic operations**: What operations are performed? (Assumption: Add land at positions[i] = [ri, ci] - turn water (0) to land (1))

3. **Return format**: What should we return? (Assumption: Array of integers - island count after each addLand operation)

4. **Connection rules**: How are cells connected? (Assumption: Horizontal or vertical adjacency - not diagonal)

5. **Initial state**: What is the initial state? (Assumption: Grid filled with water (0) - no islands initially)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

After each `addLand` operation, run BFS/DFS from all land cells to count connected components (islands). This approach has O(m × n × k) time complexity where k is the number of operations, which is too slow for large grids and many operations.

**Step 2: Semi-Optimized Approach (10 minutes)**

Use Union-Find (Disjoint Set Union) with incremental updates: when adding a land cell, check its four neighbors. If a neighbor is land, union the current cell with that neighbor's component. Track the number of components and update it as unions occur. This reduces time to O(k × α(m×n)) per operation where α is the inverse Ackermann function, which is nearly constant.

**Step 3: Optimized Solution (12 minutes)**

Use Union-Find with path compression and union by rank: maintain a DSU data structure. When adding land at position (r, c), increment island count. Check four neighbors: if a neighbor is land and belongs to a different component, union them and decrement island count. Use path compression and union by rank for optimal performance. This achieves O(k × α(m×n)) ≈ O(k) amortized time, which is optimal. The key insight is that Union-Find efficiently handles dynamic connectivity queries, and we can maintain the island count incrementally as we add land cells.

## Solution Approach

This is an **incremental/dynamic** problem where we add land cells one by one and need to track the number of islands after each addition. Unlike [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/), we can't rebuild the entire grid each time (too slow).

### Key Insights:

1. **Union-Find (DSU)**: Perfect for incremental connectivity problems
2. **Dynamic Island Counting**: Track count as we add lands and merge islands
3. **Coordinate Mapping**: Map 2D coordinates `(r, c)` to 1D index: `id = r * n + c`
4. **Neighbor Checking**: When adding land, check 4 neighbors and union if they're also land
5. **Duplicate Handling**: Skip if position is already land

### Algorithm:

1. **Initialize Union-Find**: Create DSU for `m * n` cells (all initially water)
2. **For Each Position**:
   - Convert `(r, c)` to 1D index
   - If already land, skip (duplicate)
   - Add land: mark cell as land in DSU
   - Check 4 neighbors: if neighbor is land, union current cell with neighbor
   - Record current island count
3. **Return Results**: Array of island counts after each operation

## Solution

### **Solution: Union-Find (Disjoint Set Union) with Path Compression and Union by Rank**

```cpp
class UnionFind{
public:
    UnionFind(int size) {
        parent.resize(size, -1);
        rank.resize(size, 0);
        cnt = 0;
    }

    void addLand(int x) {
        if(parent[x] >= 0) return;
        parent[x] = x;
        cnt++;
    }

    bool isLand(int x) {
        if(parent[x] >= 0) {
            return true;
        }
        return false;
    }
    
    int numberOfIslands() {
        return cnt;
    }

    int find(int x) {
        if(parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void union_set(int x, int y) {
        int xset = find(x), yset = find(y);
        if(xset == yset) {
            return;
        } else if (rank[xset] < rank[yset]) {
            parent[xset] = yset;
        } else if(rank[xset] > rank[yset]) {
            parent[yset] = xset;
        } else {
            parent[yset] = xset;
            rank[xset]++;
        }
        cnt--;
    }

private:
    vector<int> parent, rank;
    int cnt;
};

class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        {% raw %}vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};{% endraw %}
        UnionFind dsu(m*n);
        vector<int> rtn;
        for(auto& position: positions) {
            int landPosition = position[0] * n + position[1];
            dsu.addLand(landPosition);
            for(auto& [dx, dy]: dirs) {
                int neighborX = position[0] + dx;
                int neighborY = position[1] + dy;
                int neighborPosition = neighborX * n + neighborY;
                if(neighborX >= 0 && neighborX < m && neighborY >= 0 && neighborY < n && dsu.isLand(neighborPosition)) {
                    dsu.union_set(landPosition, neighborPosition);
                }
            }
            rtn.emplace_back(dsu.numberOfIslands());
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

#### **UnionFind Class:**

1. **Constructor (Lines 3-7)**:
   - Initialize `parent` array with `-1` (water/uninitialized)
   - Initialize `rank` array with `0`
   - Initialize `cnt` (island count) to `0`

2. **addLand(int x) (Lines 9-13)**:
   - If cell is already land (`parent[x] >= 0`), return (duplicate)
   - Mark cell as land: `parent[x] = x` (self-parent)
   - Increment island count: `cnt++`

3. **isLand(int x) (Lines 15-20)**:
   - Check if cell is land: `parent[x] >= 0`
   - Return `true` if land, `false` otherwise

4. **numberOfIslands() (Lines 22-24)**:
   - Return current island count

5. **find(int x) (Lines 26-31)**:
   - Path compression: if `parent[x] != x`, recursively find root and update parent
   - Return root of the set

6. **union_set(int x, int y) (Lines 33-46)**:
   - Find roots of both sets
   - If same root, already connected (return)
   - Union by rank: attach smaller tree to larger tree
   - If ranks equal, attach one to other and increment rank
   - Decrement island count (merging two islands into one)

#### **Solution Class:**

1. **Main Function (Lines 48-66)**:
   - Initialize directions: up, down, right, left
   - Create UnionFind for `m * n` cells
   - For each position:
     - Convert `(r, c)` to 1D: `landPosition = r * n + c`
     - Add land at position
     - Check 4 neighbors:
       - If neighbor is within bounds and is land, union with current cell
     - Record current island count

### **How It Works:**

- **Initial State**: All cells are water (`parent[i] = -1`)
- **Adding Land**: When adding land at position `(r, c)`:
  1. Mark cell as land: `parent[id] = id`, increment count
  2. Check neighbors: if neighbor is land, union them (decrements count)
  3. Result: count reflects number of connected components (islands)
- **Union Operation**: Merges two islands, reducing count by 1
- **Duplicate Handling**: If position already land, skip (count unchanged)

### **Example Walkthrough:**

**Input:** `m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]`

```
Step 1: Add (0, 0)
  landPosition = 0 * 3 + 0 = 0
  addLand(0): parent[0] = 0, cnt = 1
  Neighbors: (none are land yet)
  Result: [1]

Step 2: Add (0, 1)
  landPosition = 0 * 3 + 1 = 1
  addLand(1): parent[1] = 1, cnt = 2
  Neighbors: (0, 0) = 0 is land
  union_set(1, 0): merge islands, cnt = 1
  Result: [1, 1]

Step 3: Add (1, 2)
  landPosition = 1 * 3 + 2 = 5
  addLand(5): parent[5] = 5, cnt = 2
  Neighbors: (none are land)
  Result: [1, 1, 2]

Step 4: Add (2, 1)
  landPosition = 2 * 3 + 1 = 7
  addLand(7): parent[7] = 7, cnt = 3
  Neighbors: (none are land)
  Result: [1, 1, 2, 3]
```

### **Complexity Analysis:**

- **Time Complexity:** O(k × α(mn))
  - `k` = number of positions
  - `α` = inverse Ackermann function (very small, effectively constant)
  - For each position: O(1) amortized for find/union operations
  - Overall: O(k × α(mn)) ≈ O(k)

- **Space Complexity:** O(mn)
  - `parent` array: O(mn)
  - `rank` array: O(mn)
  - Result array: O(k)
  - Overall: O(mn)

## Key Insights

1. **Union-Find for Incremental Problems**: Perfect for dynamic connectivity
2. **Coordinate Mapping**: 2D to 1D: `id = r * n + c`
3. **Dynamic Counting**: Track count as islands merge
4. **Path Compression**: Keeps find operations O(α(n))
5. **Union by Rank**: Keeps tree balanced for efficiency
6. **Duplicate Handling**: Skip already-land positions

## Edge Cases

1. **Empty positions**: `positions = []` → return `[]`
2. **Single cell**: `m = 1, n = 1` → return `[1]`
3. **Duplicate positions**: Same position added twice → count unchanged
4. **All positions form one island**: All adjacent → final count = 1
5. **No adjacent positions**: All isolated → count = number of positions

## Common Mistakes

1. **Not handling duplicates**: Adding same position twice should not change count
2. **Wrong coordinate mapping**: Using `r * m + c` instead of `r * n + c`
3. **Not checking bounds**: Forgetting to validate neighbor coordinates
4. **Incorrect union logic**: Not decrementing count when merging islands
5. **Initializing parent incorrectly**: Should use `-1` for water, not `0`

## Alternative Approaches

### **Approach 2: Brute-Force DFS/BFS (Not Recommended)**

Rebuild island count from scratch after each addition. This approach is too slow for large inputs.

```cpp
class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        vector<vector<int>> grid(m, vector<int>(n, 0));
        vector<int> result;
        for (auto& pos : positions) {
            int r = pos[0], c = pos[1];
            if (grid[r][c] == 1) {
                // duplicate: count stays same
                result.push_back(countIslands(grid));
            } else {
                grid[r][c] = 1;
                result.push_back(countIslands(grid));
            }
        }
        return result;
    }
private:
    int countIslands(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        int count = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    dfs(grid, visited, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int r, int c) {
        int m = grid.size(), n = grid[0].size();
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0 || visited[r][c]) {
            return;
        }
        visited[r][c] = true;
        dfs(grid, visited, r + 1, c);
        dfs(grid, visited, r - 1, c);
        dfs(grid, visited, r, c + 1);
        dfs(grid, visited, r, c - 1);
    }
};
```

**Time Complexity:** O(k × m × n) - Too slow for large inputs  
**Space Complexity:** O(m × n)

**Why Union-Find is Better:**
- Union-Find: O(k × α(mn)) ≈ O(k) - Very efficient
- Brute-Force: O(k × m × n) - Rebuilds entire grid each time

## Related Problems

- [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) - Static island counting with DFS/BFS
- [LC 323: Number of Connected Components in an Undirected Graph](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-323-number-of-connected-components-in-an-undirected-graph/) - Union-Find for connectivity
- [LC 547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/) - Union-Find for connected components
- [LC 721: Accounts Merge](https://robinali34.github.io/blog_leetcode/2026/01/11/medium-721-accounts-merge/) - Union-Find for grouping
- [LC 990: Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) - Union-Find for equality constraints

---

*This problem demonstrates the **Union-Find (DSU)** pattern for incremental connectivity problems. The key insight is to track island count dynamically as lands are added and merged, rather than rebuilding the entire grid each time.*

