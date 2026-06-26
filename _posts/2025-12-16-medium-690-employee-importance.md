---
layout: post
title: "[Medium] 690. Employee Importance"
date: 2025-12-16 00:00:00 -0800
categories: leetcode algorithm medium cpp dfs bfs hash-table problem-solving
---
{% raw %}

You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees `employees` where:
- `employees[i].id` is the ID of the `ith` employee.
- `employees[i].importance` is the importance value of the `ith` employee.
- `employees[i].subordinates` is a list of the IDs of the direct subordinates of the `ith` employee.

Given an integer `id` that represents an employee's ID, return the **total importance value** of this employee and all their direct and indirect subordinates.

## Examples

**Example 1:**
```
Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
```

**Example 2:**
```
Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3
Explanation: Employee 5 has an importance value of -3 and has no subordinates.
Thus, the total importance value of employee 5 is -3.
```

## Constraints

- `1 <= employees.length <= 2000`
- `1 <= employees[i].id <= 2000`
- All `employees[i].id` are **unique**.
- `-100 <= employees[i].importance <= 100`
- One employee has at most one direct leader and may have several subordinates.
- The IDs in `employees[i].subordinates` are valid IDs.

## Thinking Process

1. **Hash map for lookup**: Essential for O(1) employee access

- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.



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
| **Recursive DFS** *(this problem)* | $O(n)$ | $O(h)$ stack | Natural for trees and graphs |
| Iterative DFS (stack) | $O(n)$ | $O(n)$ | Avoid recursion depth limits |
| DFS with memoization | $O(n)$ | $O(n)$ | Overlapping subproblems on graphs |
| Backtracking DFS | $O(2^n)$ typical | $O(n)$ | Enumerate choices with pruning |

## Solution

**Time Complexity:** O(n) - Visit each employee once  
**Space Complexity:** O(n) - Hash map + recursion stack

```cpp
/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
private:
    unordered_map<int, Employee*> emap;
    
    int dfs(int id) {
        Employee* employee = emap[id];
        int rtn = employee->importance;
        for(int subid: employee->subordinates) {
            rtn += dfs(subid);
        }
        return rtn;
    }
    
public:
    int getImportance(vector<Employee*> employees, int id) {
        emap.clear();
        for(auto& e: employees) {
            emap[e->id] = e;
        }
        return dfs(id);
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **Hash map for lookup**: Essential for O(1) employee access

**How the code works:**
1. **Hash map for lookup**: Essential for O(1) employee access
- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.

**Walkthrough** — input `employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1`, expected output `11`:

Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.

| Operation | Time | Space |
|-----------|------|-------|
| Build hash map | O(n) | O(n) |
| DFS/BFS traversal | O(n) | O(n) |
| **Overall** | **O(n)** | **O(n)** |

### How Solution 1 Works

1. **Build hash map**: Map employee ID to Employee pointer for O(1) lookup
2. **DFS traversal**: 
   - Start from the given employee
   - Add their importance value
   - Recursively add importance of all subordinates
3. **Return total**: Sum of employee's importance + all subordinates' importance
## Example Walkthrough

**Input:** `employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1`

```
Employee Structure:
    1 (importance: 5)
   / \
  2   3
(3)  (3)

DFS Traversal:
1. Start at employee 1: importance = 5
2. Visit subordinate 2: importance = 3
3. Visit subordinate 3: importance = 3
4. Total = 5 + 3 + 3 = 11
```

### Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Build hash map | O(n) | O(n) |
| DFS/BFS traversal | O(n) | O(n) |
| **Overall** | **O(n)** | **O(n)** |

## Common Mistakes

1. **Single employee**: No subordinates, return their importance
2. **Negative importance**: Handle negative values correctly
3. **Deep hierarchy**: Recursion handles deep trees
4. **Wide hierarchy**: Many direct subordinates

1. **Linear search**: Not using hash map for O(1) lookup
2. **Missing subordinates**: Not traversing all levels
3. **Wrong starting point**: Starting from wrong employee ID

## Related Problems

- [339. Nested List Weight Sum](https://www.leetcode.com/problems/nested-list-weight-sum/) - Similar recursive structure
- [364. Nested List Weight Sum II](https://www.leetcode.com/problems/nested-list-weight-sum-ii/) - Weighted traversal
- [559. Maximum Depth of N-ary Tree](https://www.leetcode.com/problems/maximum-depth-of-n-ary-tree/) - N-ary tree traversal

## Pattern Recognition

This problem demonstrates the **"Tree/Graph Traversal with Hash Map"** pattern:

```
1. Build hash map for O(1) node lookup
2. Use DFS or BFS to traverse
3. Accumulate values during traversal
```

{% endraw %}

## References

- [LC 690: Employee Importance on LeetCode](https://www.leetcode.com/problems/employee-importance/)
- [LeetCode Discuss — LC 690: Employee Importance](https://www.leetcode.com/problems/employee-importance/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/employee-importance/editorial/) *(may require premium)*

## Key Takeaways

1. **Hash map for lookup**: Essential for O(1) employee access
2. **Tree traversal**: Employee hierarchy is a tree structure
3. **DFS vs BFS**: Both work equally well for this problem
