---
layout: post
title: "[Medium] 990. Satisfiability of Equality Equations"
date: 2025-10-04 00:00:00 -0000
categories: leetcode algorithm data-structures disjoint-set graph dfs medium cpp connected-components graph-coloring problem-solving
---

# [Medium] 990. Satisfiability of Equality Equations

You are given an array of strings `equations` that represent relationships between variables. Each string `equations[i]` is of length `4` and takes one of two different forms: `"xi==yi"` or `"xi!=yi"`. Here, `xi` and `yi` are lowercase letters (not necessarily different) representing one-letter variable names.

Return `true` if it is possible to assign integers to variable names so as to satisfy all the given equations, or `false` otherwise.

## Examples

**Example 1:**
```
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but the second is not.
There is no way to assign the variables to satisfy both equations.
```

**Example 2:**
```
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
```

**Example 3:**
```
Input: equations = ["a==b","b==c","a==c"]
Output: true
Explanation: We can assign a = 1, b = 1, c = 1 to satisfy all equations.
```

**Example 4:**
```
Input: equations = ["a==b","b!=c","c==a"]
Output: false
Explanation: We cannot assign values to satisfy all equations.
```

## Constraints

- `1 <= equations.length <= 500`
- `equations[i].length == 4`
- `equations[i][0]` is a lowercase letter
- `equations[i][1]` is either `'='` or `'!'`
- `equations[i][2]` is `'='`
- `equations[i][3]` is a lowercase letter

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Equation format**: What is the equation format? (Assumption: "a==b" means a equals b, "a!=b" means a not equals b)

2. **Variable assignment**: What values can variables have? (Assumption: Any integer values - just need to satisfy all equations)

3. **Transitivity**: Are equality relations transitive? (Assumption: Yes - if a==b and b==c, then a==c)

4. **Contradiction**: What makes equations unsatisfiable? (Assumption: If we derive both a==b and a!=b from the equations)

5. **Return value**: What should we return? (Assumption: Boolean - true if all equations can be satisfied, false otherwise)

## Approach

This problem can be solved using two main approaches:

1. **Union-Find (Disjoint Set Union)**: Process equality equations first to build connected components, then check inequality equations
2. **Graph Coloring/DFS**: Build a graph from equality equations and use DFS to find connected components

The key insight is that variables connected by equality equations must have the same value, while variables connected by inequality equations must have different values.

## Solution 1: Union-Find (Disjoint Set Union)

```cpp
class UnionFind{
private:
    vector<int>parent;
public:
    UnionFind() {
        parent.resize(26);
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int idx) {
        if(idx == parent[idx]) {
            return idx;
        }
        parent[idx] = find(parent[idx]);
        return parent[idx];
    }
    void unite(int idx1, int idx2){
        parent[find(idx1)] = find(idx2);
    }
};

class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        UnionFind uf;
        for(const string& str: equations) {
            if(str[1] == '=') {
                int idx1 = str[0] - 'a';
                int idx2 = str[3] - 'a';
                uf.unite(idx1, idx2);
            }
        }
        for(const string& str: equations) {
            if(str[1] == '!') {
                int idx1 = str[0] - 'a';
                int idx2 = str[3] - 'a';
                if(uf.find(idx1) == uf.find(idx2)) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

**Time Complexity:** O(n * α(26)) where α is the inverse Ackermann function (practically constant)
**Space Complexity:** O(26) = O(1) - constant space for 26 letters

### How Union-Find Works:

1. **Initialize**: Each letter is its own parent initially
2. **Process Equality**: For each `"a==b"`, unite `a` and `b` into the same component
3. **Check Inequality**: For each `"a!=b"`, verify that `a` and `b` are in different components

## Solution 2: Graph Coloring with DFS

```cpp
class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        constexpr int SIZE = 26;
        vector<vector<int>> graph(SIZE);
        vector<int> color(SIZE, -1);

        for(string& eqn : equations) {
            if(eqn[1] == '=') {
                int x = eqn[0] - 'a';
                int y = eqn[3] - 'a';
                graph[x].push_back(y);
                graph[y].push_back(x);
            }
        }
        function<void(int,int)> dfs = [&](int node, int c) {
            if(color[node] == -1) {
                color[node] = c;
                for(int nei: graph[node]) {
                    dfs(nei, c);
                }
            }
        };

        for(int i =0; i < SIZE; i++) {
            dfs(i, i);
        }

        for(string& eqn : equations) {
            if(eqn[1] == '!') {
                int x = eqn[0] - 'a';
                int y = eqn[3] - 'a';
                if(color[x] == color[y]) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

**Time Complexity:** O(n + 26) = O(n) - process equations + DFS on graph
**Space Complexity:** O(26) = O(1) - graph and color array

### How Graph Coloring Works:

1. **Build Graph**: Create adjacency list from equality equations
2. **Color Components**: Use DFS to assign the same color to connected components
3. **Check Conflicts**: Verify that inequality equations don't connect same-colored nodes

## Solution 3: DFS with Component Tracking

```cpp
class Solution {
private:
    static constexpr int SIZE = 26;
    void dfs(int node, int id, vector<vector<int>>& adjacency, vector<int>& component) {
        component[node] = id;
        for(int neighbor: adjacency[node]) {
            if(component[neighbor] == -1) {
                dfs(neighbor, id, adjacency, component);
            }
        }
    }

public:
    bool equationsPossible(vector<string>& equations) {
        vector<vector<int>> adjacency(SIZE);
        vector<int> component(SIZE, -1);
        for(const string& eq: equations) {
            if(eq[1] == '=') {
                int x = eq[0] - 'a';
                int y = eq[3] - 'a';
                adjacency[x].push_back(y);
                adjacency[y].push_back(x);
            }
        }

        int cur = 0;
        for(int i = 0; i < SIZE; i++) {
            if(component[i] == -1 && !adjacency[i].empty()) {
                dfs(i, cur++, adjacency, component);
            }
        }

        for(const string& eq: equations) {
            if(eq[1] == '!') {
                int x = eq[0] - 'a';
                int y = eq[3] - 'a';
                if(x == y || (component[x] != -1 && component[x] == component[y])) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

**Time Complexity:** O(n + 26) = O(n)
**Space Complexity:** O(26) = O(1)

### Key Differences in Solution 3:

1. **Component ID Tracking**: Assigns unique IDs to each connected component
2. **Empty Component Handling**: Only processes nodes that have edges
3. **Self-Reference Check**: Handles cases like `"a!=a"` explicitly

## Step-by-Step Example (Union-Find)

Let's trace through `["a==b","b!=c","c==a"]`:

### Initial State:
```
parent = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
         a b c d e f g h i j k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
```

### Process "a==b":
- `a` (index 0) and `b` (index 1) are united
- `parent[0] = 1`
- `parent = [1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]`

### Process "b!=c":
- Check if `find(1)` == `find(2)`
- `find(1)` = 1, `find(2)` = 2
- Since 1 ≠ 2, this inequality is satisfied

### Process "c==a":
- `c` (index 2) and `a` (index 0) are united
- `find(0)` = 1, `find(2)` = 2
- `parent[2] = 1`
- `parent = [1,1,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]`

### Final Check:
- Now `find(1)` = 1, `find(2)` = 1
- Since 1 == 1, the inequality "b!=c" is violated
- Return `false`

## Algorithm Analysis

### Union-Find Approach:
- **Pros**: 
  - Efficient for dynamic connectivity problems
  - Path compression optimizes future queries
  - Clean separation of equality and inequality processing
- **Cons**: 
  - Requires understanding of Union-Find data structure
  - Slightly more complex implementation

### Graph Coloring Approach:
- **Pros**: 
  - More intuitive for graph problems
  - Direct visualization of connected components
  - Easier to understand and implement
- **Cons**: 
  - Requires building adjacency list
  - DFS overhead for each component

## Key Insights

1. **Two-Phase Processing**: Process equality equations first, then check inequality equations
2. **Connected Components**: Variables connected by equality must have the same value
3. **Conflict Detection**: Inequality equations create conflicts if variables are in the same component
4. **Self-Reference**: Handle cases like `"a!=a"` which are always false

## Edge Cases

1. **Self-inequality**: `["a!=a"]` → `false`
2. **Transitive equality**: `["a==b","b==c","a==c"]` → `true`
3. **Circular conflict**: `["a==b","b!=c","c==a"]` → `false`
4. **Single variable**: `["a==a"]` → `true`

## Solution Comparison

| Approach | Time Complexity | Space Complexity | Implementation | Intuition |
|----------|----------------|-----------------|----------------|-----------|
| Union-Find | O(n * α(26)) | O(1) | Moderate | Moderate |
| Graph Coloring | O(n) | O(1) | Simple | High |
| Component DFS | O(n) | O(1) | Simple | High |

## Common Mistakes

1. **Processing order**: Must process equality before inequality
2. **Self-reference**: Forgetting to handle `"a!=a"` cases
3. **Component tracking**: Not properly tracking connected components
4. **Index mapping**: Incorrectly mapping characters to array indices

## Related Problems

- [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/)
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/)
- [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)

## Conclusion

This problem demonstrates the power of Union-Find and graph algorithms for handling equality constraints. The key insight is recognizing that equality equations create equivalence classes (connected components), while inequality equations create conflicts between these classes.

Both Union-Find and graph coloring approaches are valid, with Union-Find being more efficient for dynamic connectivity and graph coloring being more intuitive for static analysis.
