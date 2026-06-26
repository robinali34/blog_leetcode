---
layout: post
title: "[Medium] 399. Evaluate Division"
date: 2025-12-17 00:00:00 -0800
categories: leetcode algorithm medium cpp disjoint-set graph dfs problem-solving
---
You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the `jth` query where you must find the answer for `Cj / Dj = ?`.

Return *the answers to all queries*. If a single answer cannot be determined, return `-1.0`.

**Note:** The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

## Examples

**Example 1:**
```
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
Return: [6.0, 0.5, -1.0, 1.0, -1.0]
```

**Example 2:**
```
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
```

**Example 3:**
```
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
```

## Constraints

- `1 <= equations.length <= 20`
- `equations[i].length == 2`
- `1 <= Ai.length, Bi.length <= 5`
- `values.length == equations.length`
- `0.0 < values[i] <= 20.0`
- `1 <= queries.length <= 20`
- `queries[i].length == 2`
- `1 <= Cj.length, Dj.length <= 5`
- `Ai, Bi, Cj, Dj` consist of lower case English letters and digits.

## Thinking Process

1. **Weighted Union-Find**: Maintains ratios relative to root

- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | O(n) | O(h) stack | Natural for trees and graphs |
| Iterative DFS (stack) | O(n) | O(n) | Avoid recursion depth limits |
| DFS with memoization | O(n) | O(n) | Overlapping subproblems on graphs |
| Backtracking DFS | O(2^n) typical | O(n) | Enumerate choices with pruning |

## Solution

**Time Complexity:** O((E + Q) × α(n)) where E = equations, Q = queries, n = variables  
**Space Complexity:** O(n) - For the union-find structure

This solution uses Union-Find with path compression and union by weight to maintain ratios between variables.

```cpp
class Solution {
private:
    unordered_map<string, pair<string, double>> weights;

    pair<string, double> find(const string& node) {
        if(!weights.contains(node)) {
            weights[node] = {node, 1.0};
        }
        auto entry = weights[node];
        if(entry.first != node) {
            auto parentEntry = find(entry.first);
            weights[node] = {
                parentEntry.first,
                entry.second * parentEntry.second
            };
        }
        return weights[node];
    }

    void unite(const string& dividend, const string& divisor, double value) {
        auto dividendEntry = find(dividend);
        auto divisorEntry = find(divisor);

        string dividendRoot = dividendEntry.first;
        string divisorRoot = divisorEntry.first;

        if(dividendRoot != divisorRoot) {
            weights[dividendRoot] = {
                divisorRoot,
                divisorEntry.second * value / dividendEntry.second
            };
        }
    }

public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        for(int i = 0; i < equations.size(); i++) {
            string dividend = equations[i][0];
            string divisor = equations[i][1];
            double value = values[i];
            unite(dividend, divisor, value);
        }

        vector<double> rtn;
        for (auto& query: queries) {
            string dividend = query[0];
            string divisor = query[1];
            if(!weights.contains(dividend) || !weights.contains(divisor)) {
                rtn.push_back(-1.0);
                continue;
            }

            auto dividendEntry = find(dividend);
            auto divisorEntry = find(divisor);
            if(dividendEntry.first != divisorEntry.first) {
                rtn.push_back(-1.0);
            } else {
                rtn.push_back(dividendEntry.second / divisorEntry.second);
            }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **Weighted Union-Find**: Maintains ratios relative to root

**How the code works:**
1. **Weighted Union-Find**: Maintains ratios relative to root
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]`, expected output `[6.00000,0.50000,-1.00000,1.00000,-1.00000]`:

Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
Return: [6.0, 0.5, -1.0, 1.0, -1.0]

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Union-Find | O((E+Q)×α(n)) | O(n) | Optimal for many queries |
| Graph DFS | O(E + Q×V) | O(E+V) | Simple, good for few queries |

### How Solution 1 Works

1. **Union-Find Structure**:
   - `weights[node] = {parent, weight}` where `weight = node / parent`
   - Example: If `a / b = 2.0`, then `weights[a] = {b, 2.0}`

2. **Find with Path Compression**:
   - Finds root and compresses path
   - Updates weight along path: `node_weight = node_weight × parent_weight`
   - Returns `{root, node_weight}`

3. **Union Operation**:
   - Connects two components with a ratio
   - If `a / b = value`, connects roots with appropriate weight
   - Weight formula: `root_weight = (divisor_weight × value) / dividend_weight`

4. **Query Processing**:
   - If both variables exist and have same root, return `dividend_weight / divisor_weight`
   - Otherwise return `-1.0`

### Key Insight

The Union-Find structure maintains ratios relative to the root:
- `weights[node] = {root, node/root}`
- To find `a / b`: If both have same root, `(a/root) / (b/root) = a/b`
## Example Walkthrough

**Input:** `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"]]`

### Solution 1 (Union-Find):

```
Step 1: Process "a / b = 2.0"
  unite(a, b, 2.0):
    find(a) → {a, 1.0}
    find(b) → {b, 1.0}
    weights[a] = {b, 2.0}

Step 2: Process "b / c = 3.0"
  unite(b, c, 3.0):
    find(b) → {b, 1.0}
    find(c) → {c, 1.0}
    weights[b] = {c, 3.0}

Step 3: Query "a / c = ?"
  find(a) → find(b) → {c, 1.0}
    Path: a → b → c
    weights[a] = {b, 2.0}
    find(b) → {c, 3.0}
    weights[a] = {c, 2.0 × 3.0 = 6.0}
  
  find(c) → {c, 1.0}
  
  Result: 6.0 / 1.0 = 6.0
```

### Solution 2 (Graph DFS):

```
Graph:
  a → [(b, 2.0)]
  b → [(a, 0.5), (c, 3.0)]
  c → [(b, 0.333)]

Query "a / c":
  DFS(a, c):
    a → b (product = 2.0)
    b → c (product = 2.0 × 3.0 = 6.0)
    Found! Return 6.0
```

### Complexity
| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Union-Find | O((E+Q)×α(n)) | O(n) | Optimal for many queries |
| Graph DFS | O(E + Q×V) | O(E+V) | Simple, good for few queries |

## Common Mistakes

1. **Variable not in equations**: Return `-1.0`
2. **Same variable query**: `a / a = 1.0`
3. **Disconnected components**: Variables in different components return `-1.0`
4. **Single equation**: Handle minimal input
5. **Transitive relationships**: `a/b=2, b/c=3` → `a/c=6`

1. **Path compression**: Not updating weights during path compression
2. **Union weight calculation**: Wrong formula for connecting roots
3. **Division by zero**: Should not occur per problem constraints
4. **Missing variables**: Not checking if variables exist before querying

## Optimization Tips

1. **Path compression**: Essential for O(α(n)) amortized time
2. **Lazy initialization**: Only create entries when needed
3. **Early termination**: Check if variables exist before processing

## Related Problems

- [990. Satisfiability of Equality Equations](https://www.leetcode.com/problems/satisfiability-of-equality-equations/) - Similar Union-Find structure
- [547. Number of Provinces](https://www.leetcode.com/problems/number-of-provinces/) - Union-Find for connectivity
- [684. Redundant Connection](https://www.leetcode.com/problems/redundant-connection/) - Union-Find for cycle detection

## Pattern Recognition

This problem demonstrates the **"Weighted Union-Find"** pattern:

```
1. Maintain parent and weight in union-find structure
2. Path compression updates weights along path
3. Union operation connects with correct weight
4. Query uses weight ratio when same root
```

Similar problems:
- Satisfiability of Equality Equations
- Network Connectivity with Weights
- Ratio Queries
## References

- [LC 399: Evaluate Division on LeetCode](https://www.leetcode.com/problems/evaluate-division/)
- [LeetCode Discuss — LC 399: Evaluate Division](https://www.leetcode.com/problems/evaluate-division/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/evaluate-division/editorial/) *(may require premium)*

## Key Takeaways

1. **Weighted Union-Find**: Maintains ratios relative to root
2. **Path compression**: Updates weights along path for efficiency
3. **Union by weight**: Connects roots with correct ratio
4. **Query formula**: `dividend_weight / divisor_weight` when same root
