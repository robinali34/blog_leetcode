---
layout: post
title: "[Medium] 77. Combinations"
date: 2025-09-29 00:00:00 -0000
categories: leetcode algorithm backtracking data-structures recursion medium cpp combinations dfs problem-solving
---
This is a classic backtracking problem that requires generating all possible combinations of k numbers chosen from the range [1, n]. The key insight is using DFS with backtracking to explore all possible paths while avoiding duplicates.

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

## Examples
**Example 1:**
```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

**Example 2:**
```
Input: n = 1, k = 1
Output: [[1]]
```

**Example 3:**
```
Input: n = 3, k = 3
Output: [[1,2,3]]
```

## Constraints
- 1 <= n <= 20
- 1 <= k <= n

## Thinking Process

The solution uses backtracking (DFS) with the following strategy:

1. **Base Case**: When the current path has k elements, add it to the result
2. **Early Termination**: If not enough numbers remain to form a valid combination, return early
3. **Recursive Case**: For each number from `first_num` to n, add it to the path and recurse
4. **Backtrack**: Remove the last element before trying the next number
5. **Avoid Duplicates**: Start from `i + 1` in the next recursive call to ensure ascending order



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 165" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Tree DFS (bottom-up)</text>

  <line x1="140" y1="42" x2="80" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="140" y1="42" x2="200" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="80" y1="88" x2="50" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="200" y1="88" x2="230" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <circle cx="140" cy="42" r="18" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="140" y="46" text-anchor="middle" font-size="12" fill="#3D3535">3</text>
  <circle cx="80" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="80" y="92" text-anchor="middle" font-size="11" fill="#3D3535">9</text>
  <circle cx="200" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="200" y="92" text-anchor="middle" font-size="11" fill="#3D3535">20</text>
  <circle cx="50" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="50" y="132" text-anchor="middle" font-size="10" fill="#3D3535">15</text>
  <circle cx="230" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="230" y="132" text-anchor="middle" font-size="10" fill="#3D3535">7</text>
  <text x="140" y="155" text-anchor="middle" font-size="11" fill="#6B6560">post-order: combine left + right + 1</text>

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
**Time Complexity:** O(C(n,k) × k) - We generate C(n,k) combinations, each taking O(k) time  
**Space Complexity:** O(k) - For the recursion stack and current path

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> rtn;
        vector<int> path;
        dfs(n, k, rtn, path, 1);
        return rtn;
    }

private:
    void dfs(const int n, const int k, vector<vector<int>> & rtn, vector<int>& path, int first_num) {
        if(path.size() == k) {
            rtn.push_back(path);
            return;
        }
        if (path.size() + (n - first_num + 1) < k) {
            return;
        }
        for (int i = first_num; i <= n; i++) {
            path.push_back(i);
            dfs(n, k, rtn, path, i + 1);
            path.pop_back();
        }
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** The solution uses backtracking (DFS) with the following strategy:

**How the code works:**
1. **Base Case**: When the current path has k elements, add it to the result
2. **Early Termination**: If not enough numbers remain to form a valid combination, return early
3. **Recursive Case**: For each number from `first_num` to n, add it to the path and recurse
4. **Backtrack**: Remove the last element before trying the next number
5. **Avoid Duplicates**: Start from `i + 1` in the next recursive call to ensure ascending order

**Walkthrough** — input `n = 4, k = 2`, expected output `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Step-by-Step Example

Let's trace through the solution with n = 4, k = 2:

**Initial Call:** `dfs(4, 2, rtn, [], 1)`

**Iteration 1:** i = 1
- Add 1 to path: `[1]`
- Recursive call: `dfs(4, 2, rtn, [1], 2)`
  - i = 2: Add 2 → `[1,2]` → Base case hit → Add to result
  - i = 3: Add 3 → `[1,3]` → Base case hit → Add to result  
  - i = 4: Add 4 → `[1,4]` → Base case hit → Add to result
- Remove 1 from path: `[]`

**Iteration 2:** i = 2
- Add 2 to path: `[2]`
- Recursive call: `dfs(4, 2, rtn, [2], 3)`
  - i = 3: Add 3 → `[2,3]` → Base case hit → Add to result
  - i = 4: Add 4 → `[2,4]` → Base case hit → Add to result
- Remove 2 from path: `[]`

**Iteration 3:** i = 3
- Add 3 to path: `[3]`
- Recursive call: `dfs(4, 2, rtn, [3], 4)`
  - i = 4: Add 4 → `[3,4]` → Base case hit → Add to result
- Remove 3 from path: `[]`

**Iteration 4:** i = 4
- Add 4 to path: `[4]`
- Recursive call: `dfs(4, 2, rtn, [4], 5)` → No iterations (i > n)
- Remove 4 from path: `[]`

**Result:** `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`

## Backtracking Template

This problem follows the classic backtracking template:

```cpp
void backtrack(parameters) {
    if (base_case) {
        // Process result
        return;
    }
    
    for (choice in choices) {
        // Make choice
        make_choice(choice);
        
        // Recurse
        backtrack(updated_parameters);
        
        // Undo choice (backtrack)
        undo_choice(choice);
    }
}
```

## Optimization Techniques

### Early Termination
```cpp
void dfs(int n, int k, vector<vector<int>>& result, vector<int>& path, int start) {
    // Early termination: not enough numbers left
    if (path.size() + (n - start + 1) < k) {
        return;
    }
    
    if (path.size() == k) {
        result.push_back(path);
        return;
    }
    
    for (int i = start; i <= n; i++) {
        path.push_back(i);
        dfs(n, k, result, path, i + 1);
        path.pop_back();
    }
}
```

## Common Mistakes

1. **Not Backtracking**: Forgetting to remove elements after recursion
2. **Duplicate Combinations**: Not using `first_num` parameter correctly
3. **Index Confusion**: Mixing 0-indexed and 1-indexed ranges
4. **Base Case Errors**: Incorrect termination condition

## Related Problems

- **39. Combination Sum** - Combinations that sum to target
- **40. Combination Sum II** - With duplicates and constraints
- **216. Combination Sum III** - Using digits 1-9 only
- **46. Permutations** - All permutations instead of combinations
- **78. Subsets** - All possible subsets

## Visual Representation

For n = 4, k = 2, the recursion tree looks like:

```
dfs(4,2,[],1)
├── i=1: [1] → dfs(4,2,[1],2)
│   ├── i=2: [1,2] ✓
│   ├── i=3: [1,3] ✓
│   └── i=4: [1,4] ✓
├── i=2: [2] → dfs(4,2,[2],3)
│   ├── i=3: [2,3] ✓
│   └── i=4: [2,4] ✓
├── i=3: [3] → dfs(4,2,[3],4)
│   └── i=4: [3,4] ✓
└── i=4: [4] → dfs(4,2,[4],5) (no iterations)
```

---

## References

- [LC 77: Combinations on LeetCode](https://www.leetcode.com/problems/combinations/)
- [LeetCode Discuss — LC 77: Combinations](https://www.leetcode.com/problems/combinations/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/combinations/editorial/) *(may require premium)*

## Key Takeaways

1. **Backtracking Pattern**: Add → Recurse → Remove
2. **Avoiding Duplicates**: Use `first_num` parameter to ensure ascending order
3. **Early Termination**: Prune branches where `path.size() + (n - first_num + 1) < k`
4. **Pruning**: Stop when `i > n` or when remaining numbers can't form a valid combination
5. **Base Case**: When path size equals k, we have a valid combination
