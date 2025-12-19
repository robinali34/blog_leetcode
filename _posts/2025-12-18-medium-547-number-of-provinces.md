---
layout: post
title: "[Medium] 547. Number of Provinces"
date: 2025-12-18 00:00:00 -0800
categories: leetcode algorithm medium cpp disjoint-set dfs graph problem-solving
---

{% raw %}
# [Medium] 547. Number of Provinces

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return *the total number of provinces*.

## Examples

**Example 1:**
```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Example 2:**
```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`.
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

## Solution 1: Union-Find (Disjoint Set Union) - Recommended

**Time Complexity:** O(n² × α(n)) where α is the inverse Ackermann function  
**Space Complexity:** O(n) - For parent array

This solution uses Union-Find to group connected cities into provinces.

```cpp
class Solution {
private:
    int find(vector<int>& parent, int index) {
        if(parent[index] != index) {
            parent[index] = find(parent, parent[index]);
        }
        return parent[index];
    }

    void unite(vector<int>& parent, int index1, int index2) {
        parent[find(parent, index1)] = find(parent, index2);
    }
    
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int cnt = isConnected.size();
        vector<int> parent(cnt);
        
        // Initialize: each city is its own parent
        for(int i = 0; i < cnt; i++) {
            parent[i] = i;
        }
        
        // Union connected cities
        for(int i = 0; i < cnt; i++) {
            for(int j = 0; j < cnt; j++) {
                if(isConnected[i][j] == 1) {
                    unite(parent, i, j);
                }
            }
        }
        
        // Count provinces (number of roots)
        int circles = 0;
        for(int i = 0; i < cnt; i++) {
            if(parent[i] == i) circles++;
        }
        return circles;
    }
};
```

### How Solution 1 Works

1. **Initialization**: Each city starts as its own parent (separate province)
2. **Union Operation**: For each connection `isConnected[i][j] == 1`, unite cities `i` and `j`
3. **Path Compression**: The `find` function compresses paths for efficiency
4. **Count Provinces**: Count the number of roots (cities where `parent[i] == i`)

### Key Insight

A province is a connected component. Union-Find groups all connected cities under the same root, so counting roots gives the number of provinces.

## Solution 2: DFS (Depth-First Search)

**Time Complexity:** O(n²) - Visit each city once  
**Space Complexity:** O(n) - For visited array and recursion stack

Use DFS to explore all cities in a province.

```cpp
class Solution {
private:
    void dfs(vector<vector<int>>& isConnected, vector<bool>& visited, int city) {
        visited[city] = true;
        for(int j = 0; j < isConnected.size(); j++) {
            if(isConnected[city][j] == 1 && !visited[j]) {
                dfs(isConnected, visited, j);
            }
        }
    }
    
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int provinces = 0;
        
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                dfs(isConnected, visited, i);
                provinces++;
            }
        }
        
        return provinces;
    }
};
```

### How Solution 2 Works

1. **Visit each city**: Iterate through all cities
2. **DFS exploration**: For each unvisited city, start DFS to mark all connected cities
3. **Count provinces**: Each DFS call represents one province

## Solution 3: BFS (Breadth-First Search)

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

Use BFS instead of DFS for iterative exploration.

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int provinces = 0;
        
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                queue<int> q;
                q.push(i);
                visited[i] = true;
                
                while(!q.empty()) {
                    int city = q.front();
                    q.pop();
                    
                    for(int j = 0; j < n; j++) {
                        if(isConnected[city][j] == 1 && !visited[j]) {
                            visited[j] = true;
                            q.push(j);
                        }
                    }
                }
                
                provinces++;
            }
        }
        
        return provinces;
    }
};
```

## Comparison of Approaches

| Aspect | Union-Find | DFS | BFS |
|--------|-----------|-----|-----|
| **Time Complexity** | O(n² × α(n)) | O(n²) | O(n²) |
| **Space Complexity** | O(n) | O(n) | O(n) |
| **Code Simplicity** | Moderate | Simple | Moderate |
| **Best For** | Dynamic connectivity | Static graph | Static graph |

## Example Walkthrough

**Input:** `isConnected = [[1,1,0],[1,1,0],[0,0,1]]`

### Solution 1 (Union-Find):
```
Initial: parent = [0, 1, 2]

Process connections:
i=0, j=0: isConnected[0][0] = 1 → unite(0, 0) → no change
i=0, j=1: isConnected[0][1] = 1 → unite(0, 1)
  find(0) = 0, find(1) = 1
  parent[0] = 1
  parent = [1, 1, 2]

i=1, j=0: isConnected[1][0] = 1 → unite(1, 0)
  find(1) = 1, find(0) = find(1) = 1
  Already connected, no change

i=1, j=1: isConnected[1][1] = 1 → unite(1, 1) → no change

i=2, j=2: isConnected[2][2] = 1 → unite(2, 2) → no change

Final: parent = [1, 1, 2]
Count roots: parent[1] == 1, parent[2] == 2
Result: 2 provinces
```

### Solution 2 (DFS):
```
visited = [false, false, false]

i=0: Not visited
  DFS(0):
    Mark 0 as visited
    Check j=0: isConnected[0][0]=1, visited[0]=true, skip
    Check j=1: isConnected[0][1]=1, visited[1]=false
      DFS(1):
        Mark 1 as visited
        Check j=0: visited[0]=true, skip
        Check j=1: visited[1]=true, skip
        Check j=2: isConnected[1][2]=0, skip
    Check j=2: isConnected[0][2]=0, skip
  provinces = 1

i=1: Already visited, skip
i=2: Not visited
  DFS(2):
    Mark 2 as visited
    Check j=0: isConnected[2][0]=0, skip
    Check j=1: isConnected[2][1]=0, skip
    Check j=2: visited[2]=true, skip
  provinces = 2

Result: 2 provinces
```

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Union-Find | O(n² × α(n)) | O(n) | Path compression makes α(n) ≈ constant |
| DFS | O(n²) | O(n) | Simple and intuitive |
| BFS | O(n²) | O(n) | Iterative, no recursion |

## Edge Cases

1. **Single city**: `[[1]]` → return 1
2. **All connected**: All cities in one province → return 1
3. **None connected**: Each city is separate → return n
4. **Self-loops**: `isConnected[i][i] == 1` (handled automatically)

## Common Mistakes

1. **Not using path compression**: Leads to O(n) find operations
2. **Wrong root counting**: Counting `parent[i] == i` before path compression
3. **Symmetric matrix**: Only need to check upper or lower triangle (but checking all is fine)
4. **Visited array**: In DFS/BFS, forgetting to mark visited

## Key Insights

1. **Connected Components**: Provinces are connected components in the graph
2. **Symmetric Matrix**: `isConnected[i][j] == isConnected[j][i]` (undirected graph)
3. **Self-loops**: `isConnected[i][i] == 1` (each city connects to itself)
4. **Union-Find Efficiency**: Path compression makes find operations nearly O(1)

## Optimization Tips

1. **Path Compression**: Essential for Union-Find efficiency
2. **Union by Rank**: Can add rank optimization for better performance
3. **Early Exit**: Can optimize by only checking upper triangle (but code is simpler checking all)

## Related Problems

- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) - Connected components in grid
- [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) - Find largest component
- [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) - Mark connected regions
- [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) - Union-Find for equality

## Pattern Recognition

This problem demonstrates the **"Connected Components"** pattern:

```
1. Use Union-Find or DFS/BFS to group connected nodes
2. Count the number of distinct groups
3. Each group represents one component
```

Similar problems:
- Number of Islands
- Max Area of Island
- Friend Circles (same problem)
- Accounts Merge

{% endraw %}

