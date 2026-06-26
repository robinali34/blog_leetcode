---
layout: post
title: "[Medium] 990. Satisfiability of Equality Equations"
date: 2025-10-04 00:00:00 -0000
categories: leetcode algorithm data-structures disjoint-set graph dfs medium cpp connected-components graph-coloring problem-solving
---
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

## Thinking Process

This problem can be solved using two main approaches:

1. **Union-Find (Disjoint Set Union)**: Process equality equations first to build connected components, then check inequality equations
2. **Graph Coloring/DFS**: Build a graph from equality equations and use DFS to find connected components

The key insight is that variables connected by equality equations must have the same value, while variables connected by inequality equations must have different values.



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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** This problem can be solved using two main approaches:

**How the code works:**
1. **Union-Find (Disjoint Set Union)**: Process equality equations first to build connected components, then check inequality equations
2. **Graph Coloring/DFS**: Build a graph from equality equations and use DFS to find connected components

**Walkthrough** — input `equations = ["a==b","b!=a"]`, expected output `false`:

If we assign say, a = 1 and b = 1, then the first equation is satisfied, but the second is not.
There is no way to assign the variables to satisfy both equations.
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

## Common Mistakes

1. **Self-inequality**: `["a!=a"]` → `false`
2. **Transitive equality**: `["a==b","b==c","a==c"]` → `true`
3. **Circular conflict**: `["a==b","b!=c","c==a"]` → `false`
4. **Single variable**: `["a==a"]` → `true`

1. **Processing order**: Must process equality before inequality
2. **Self-reference**: Forgetting to handle `"a!=a"` cases
3. **Component tracking**: Not properly tracking connected components
4. **Index mapping**: Incorrectly mapping characters to array indices

## Related Problems

- [399. Evaluate Division](https://www.leetcode.com/problems/evaluate-division/)
- [547. Number of Provinces](https://www.leetcode.com/problems/number-of-provinces/)
- [684. Redundant Connection](https://www.leetcode.com/problems/redundant-connection/)
- [685. Redundant Connection II](https://www.leetcode.com/problems/redundant-connection-ii/)
- [721. Accounts Merge](https://www.leetcode.com/problems/accounts-merge/)

## Conclusion

This problem demonstrates the power of Union-Find and graph algorithms for handling equality constraints. The key insight is recognizing that equality equations create equivalence classes (connected components), while inequality equations create conflicts between these classes.

Both Union-Find and graph coloring approaches are valid, with Union-Find being more efficient for dynamic connectivity and graph coloring being more intuitive for static analysis.

## References

- [LC 990: Satisfiability of Equality Equations on LeetCode](https://www.leetcode.com/problems/satisfiability-of-equality-equations/)
- [LeetCode Discuss — LC 990: Satisfiability of Equality Equations](https://www.leetcode.com/problems/satisfiability-of-equality-equations/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/satisfiability-of-equality-equations/editorial/) *(may require premium)*

## Key Takeaways

1. **Two-Phase Processing**: Process equality equations first, then check inequality equations
2. **Connected Components**: Variables connected by equality must have the same value
3. **Conflict Detection**: Inequality equations create conflicts if variables are in the same component
4. **Self-Reference**: Handle cases like `"a!=a"` which are always false
