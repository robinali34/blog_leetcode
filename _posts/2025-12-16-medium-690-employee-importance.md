---
layout: post
title: "[Medium] 690. Employee Importance"
date: 2025-12-16 00:00:00 -0800
categories: leetcode algorithm medium cpp dfs bfs hash-table problem-solving
---

{% raw %}
# [Medium] 690. Employee Importance

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Employee structure**: How are employees represented? (Assumption: [id, importance, subordinates] - id, importance value, list of subordinate IDs)

2. **Total importance**: How is total importance calculated? (Assumption: Employee's importance + sum of all direct and indirect subordinates' importance)

3. **Return value**: What should we return? (Assumption: Integer - total importance of employee and all subordinates)

4. **Employee existence**: Is the given employee ID guaranteed to exist? (Assumption: Yes - per problem statement)

5. **Subordinate hierarchy**: Can subordinates have their own subordinates? (Assumption: Yes - need to recursively calculate all levels)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Build a tree structure from the employee list. Then traverse the tree starting from the given employee ID, visiting all nodes in the subtree. Sum up the importance values of all visited employees. This approach works but requires building the tree structure first, which adds complexity. The traversal itself is straightforward but needs proper tree construction.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a hash map to quickly look up employees by ID. Use BFS with a queue: start with the given employee, add it to queue. Process queue: for each employee, add its importance to total, then add all subordinates to queue. Continue until queue is empty. This avoids building an explicit tree structure and processes employees level by level.

**Step 3: Optimized Solution (8 minutes)**

Use DFS with a hash map for employee lookup. Create a hash map from employee ID to employee object for O(1) lookup. Use recursive DFS: for the given employee, return its importance plus the sum of recursively calculated importance of all subordinates. This achieves O(n) time where n is the total number of employees (we visit each once) and O(h) space for recursion stack where h is the height. The recursive solution is elegant and naturally handles the tree structure without explicit tree building.

## Solution 1: DFS with Hash Map (Recommended)

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

### How Solution 1 Works

1. **Build hash map**: Map employee ID to Employee pointer for O(1) lookup
2. **DFS traversal**: 
   - Start from the given employee
   - Add their importance value
   - Recursively add importance of all subordinates
3. **Return total**: Sum of employee's importance + all subordinates' importance

## Solution 2: BFS with Queue

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, Employee*> emap;
        for(auto& e: employees) {
            emap[e->id] = e;
        }
        
        int total = 0;
        queue<int> q;
        q.push(id);
        
        while(!q.empty()) {
            int currId = q.front();
            q.pop();
            
            Employee* emp = emap[currId];
            total += emp->importance;
            
            for(int subId : emp->subordinates) {
                q.push(subId);
            }
        }
        
        return total;
    }
};
```

### How Solution 2 Works

1. **Build hash map**: Same as DFS approach
2. **BFS traversal**:
   - Start with target employee in queue
   - Process each employee: add importance and enqueue subordinates
3. **Return total**: Accumulated importance from all visited employees

## Comparison of Approaches

| Aspect | DFS | BFS |
|--------|-----|-----|
| **Time Complexity** | O(n) | O(n) |
| **Space Complexity** | O(n) | O(n) |
| **Code Simplicity** | Simple | Simple |
| **Stack Usage** | Recursion stack | Queue |

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

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Build hash map | O(n) | O(n) |
| DFS/BFS traversal | O(n) | O(n) |
| **Overall** | **O(n)** | **O(n)** |

## Edge Cases

1. **Single employee**: No subordinates, return their importance
2. **Negative importance**: Handle negative values correctly
3. **Deep hierarchy**: Recursion handles deep trees
4. **Wide hierarchy**: Many direct subordinates

## Common Mistakes

1. **Linear search**: Not using hash map for O(1) lookup
2. **Missing subordinates**: Not traversing all levels
3. **Wrong starting point**: Starting from wrong employee ID

## Key Insights

1. **Hash map for lookup**: Essential for O(1) employee access
2. **Tree traversal**: Employee hierarchy is a tree structure
3. **DFS vs BFS**: Both work equally well for this problem

## Related Problems

- [339. Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/) - Similar recursive structure
- [364. Nested List Weight Sum II](https://leetcode.com/problems/nested-list-weight-sum-ii/) - Weighted traversal
- [559. Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) - N-ary tree traversal

## Pattern Recognition

This problem demonstrates the **"Tree/Graph Traversal with Hash Map"** pattern:

```
1. Build hash map for O(1) node lookup
2. Use DFS or BFS to traverse
3. Accumulate values during traversal
```

{% endraw %}

