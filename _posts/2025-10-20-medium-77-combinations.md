---
layout: post
title: "77. Combinations"
date: 2025-10-20 14:00:00 -0700
categories: [leetcode, medium, backtracking, recursion, combinations]
permalink: /2025/10/20/medium-77-combinations/
---

# 77. Combinations

## Problem Statement

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

You may return the answer in **any order**.

## Examples

**Example 1:**
```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
```

**Example 2:**
```
Input: n = 1, k = 1
Output: [[1]]
```

## Constraints

- `1 <= n <= 20`
- `1 <= k <= n`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Combination definition**: What is a combination? (Assumption: Selection of k elements from n elements, order doesn't matter - {1,2} same as {2,1})

2. **Element range**: What are the available elements? (Assumption: Numbers from 1 to n inclusive - [1, 2, ..., n])

3. **Output format**: Should we return all combinations or just count? (Assumption: Return all distinct combinations - list of lists)

4. **Order requirement**: Does the order of combinations matter? (Assumption: No - can return in any order, but typically lexicographic)

5. **Empty combination**: Should we include empty combination? (Assumption: No - k >= 1 per constraints, so no empty combinations)

## Solution Approach

This problem asks for all possible combinations of `k` numbers from `[1, n]`. Since combinations are unordered (unlike permutations), we need to ensure we don't generate duplicate combinations.

### Key Insights:

1. **Order doesn't matter**: `[1,2]` and `[2,1]` are the same combination
2. **Avoid duplicates**: Start from `first_num` and only consider numbers after it
3. **Backtracking**: Use DFS to explore all possible combinations
4. **Pruning**: Stop when we have `k` elements in the current path

### Algorithm:

1. **DFS with backtracking**: Start from number 1 and explore all possible combinations
2. **Avoid duplicates**: For each position, only consider numbers greater than the previous number
3. **Base case**: When path size equals `k`, add to result
4. **Recursive case**: Try each number from `first_num` to `n`

## Solution

### **Solution: Backtracking with DFS**

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> rtn;
        vector<int> path;
        dfs(n, k, path, 1, rtn);
        return rtn;
    }
private:
    void dfs(const int n, const int k, vector<int>& path, int first_num, vector<vector<int>>& rtn) {
        if (path.size() == k) {
            rtn.push_back(path);
            return;
        }
        for(int i = first_num; i <= n; i++) {
            path.push_back(i);
            dfs(n, k, path, i + 1, rtn);
            path.pop_back();
        }
    }
};
```

### **Algorithm Explanation:**

1. **Initialize**: Start with empty `path` and `first_num = 1`
2. **Base case**: If `path.size() == k`, we have a valid combination
3. **Recursive case**: 
   - Try each number from `first_num` to `n`
   - Add current number to path
   - Recursively explore with `first_num = i + 1` (avoid duplicates)
   - Backtrack by removing the number from path

### **Example Walkthrough:**

**For `n = 4, k = 2`:**

```
dfs(4, 2, [], 1, result)
├── i=1: path=[1]
│   └── dfs(4, 2, [1], 2, result)
│       ├── i=2: path=[1,2] → result=[[1,2]]
│       ├── i=3: path=[1,3] → result=[[1,2],[1,3]]
│       └── i=4: path=[1,4] → result=[[1,2],[1,3],[1,4]]
├── i=2: path=[2]
│   └── dfs(4, 2, [2], 3, result)
│       ├── i=3: path=[2,3] → result=[[1,2],[1,3],[1,4],[2,3]]
│       └── i=4: path=[2,4] → result=[[1,2],[1,3],[1,4],[2,3],[2,4]]
└── i=3: path=[3]
    └── dfs(4, 2, [3], 4, result)
        └── i=4: path=[3,4] → result=[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

## Complexity Analysis

### **Time Complexity:** O(C(n,k) × k)
- **Number of combinations**: C(n,k) = n! / (k! × (n-k)!)
- **Each combination**: Takes O(k) time to build
- **Total**: O(C(n,k) × k)

### **Space Complexity:** O(k)
- **Recursion depth**: O(k) - maximum depth of recursion
- **Path storage**: O(k) - stores current combination
- **Result storage**: O(C(n,k) × k) - not counted in auxiliary space

## Key Points

1. **Backtracking**: Use DFS with backtracking to explore all combinations
2. **Avoid duplicates**: Start from `first_num` and only consider larger numbers
3. **Efficient pruning**: Stop when path size equals k
4. **Order preservation**: Combinations are generated in lexicographical order

## Related Problems

- [46. Permutations](https://leetcode.com/problems/permutations/)
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/)
- [78. Subsets](https://leetcode.com/problems/subsets/)
- [90. Subsets II](https://leetcode.com/problems/subsets-ii/)

## Tags

`Backtracking`, `Recursion`, `Combinations`, `DFS`, `Medium`
