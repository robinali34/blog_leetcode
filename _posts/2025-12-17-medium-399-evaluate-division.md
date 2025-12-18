---
layout: post
title: "[Medium] 399. Evaluate Division"
date: 2025-12-17 00:00:00 -0800
categories: leetcode algorithm medium cpp union-find graph dfs problem-solving
---

{% raw %}
# [Medium] 399. Evaluate Division

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

## Solution 1: Union-Find with Weighted Edges (Recommended)

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

## Solution 2: Graph DFS

**Time Complexity:** O(E + Q × V) where V = number of variables  
**Space Complexity:** O(E + V) - For graph and visited set

Build a graph and use DFS to find paths between variables.

```cpp
class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, vector<pair<string, double>>> graph;
        
        // Build graph
        for(int i = 0; i < equations.size(); i++) {
            string a = equations[i][0];
            string b = equations[i][1];
            double val = values[i];
            
            graph[a].push_back({b, val});
            graph[b].push_back({a, 1.0 / val});
        }
        
        vector<double> result;
        for(auto& query : queries) {
            string start = query[0];
            string end = query[1];
            
            if(graph.find(start) == graph.end() || graph.find(end) == graph.end()) {
                result.push_back(-1.0);
                continue;
            }
            
            unordered_set<string> visited;
            double ans = dfs(start, end, graph, visited, 1.0);
            result.push_back(ans);
        }
        
        return result;
    }
    
private:
    double dfs(string curr, string target, unordered_map<string, vector<pair<string, double>>>& graph, 
               unordered_set<string>& visited, double product) {
        if(curr == target) {
            return product;
        }
        
        visited.insert(curr);
        
        for(auto& [neighbor, weight] : graph[curr]) {
            if(visited.find(neighbor) == visited.end()) {
                double result = dfs(neighbor, target, graph, visited, product * weight);
                if(result != -1.0) {
                    return result;
                }
            }
        }
        
        visited.erase(curr);
        return -1.0;
    }
};
```

### How Solution 2 Works

1. **Build Bidirectional Graph**:
   - For `a / b = value`, add edges: `a → b` with weight `value`, `b → a` with weight `1/value`

2. **DFS Search**:
   - Start from dividend, search for divisor
   - Multiply weights along path
   - Return product when target found

3. **Backtracking**:
   - Use visited set to avoid cycles
   - Remove from visited when backtracking

## Comparison of Approaches

| Aspect | Union-Find | Graph DFS |
|--------|-----------|-----------|
| **Time Complexity** | O((E+Q)×α(n)) | O(E + Q×V) |
| **Space Complexity** | O(n) | O(E + V) |
| **Query Time** | O(α(n)) | O(V) |
| **Code Complexity** | Moderate | Simple |
| **Best For** | Many queries | Few queries |

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

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Union-Find | O((E+Q)×α(n)) | O(n) | Optimal for many queries |
| Graph DFS | O(E + Q×V) | O(E+V) | Simple, good for few queries |

## Edge Cases

1. **Variable not in equations**: Return `-1.0`
2. **Same variable query**: `a / a = 1.0`
3. **Disconnected components**: Variables in different components return `-1.0`
4. **Single equation**: Handle minimal input
5. **Transitive relationships**: `a/b=2, b/c=3` → `a/c=6`

## Common Mistakes

1. **Path compression**: Not updating weights during path compression
2. **Union weight calculation**: Wrong formula for connecting roots
3. **Division by zero**: Should not occur per problem constraints
4. **Missing variables**: Not checking if variables exist before querying

## Key Insights

1. **Weighted Union-Find**: Maintains ratios relative to root
2. **Path compression**: Updates weights along path for efficiency
3. **Union by weight**: Connects roots with correct ratio
4. **Query formula**: `dividend_weight / divisor_weight` when same root

## Optimization Tips

1. **Path compression**: Essential for O(α(n)) amortized time
2. **Lazy initialization**: Only create entries when needed
3. **Early termination**: Check if variables exist before processing

## Related Problems

- [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) - Similar Union-Find structure
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) - Union-Find for connectivity
- [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) - Union-Find for cycle detection

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

{% endraw %}

