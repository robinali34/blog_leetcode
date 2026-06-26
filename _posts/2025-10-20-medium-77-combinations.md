---
layout: post
title: "[Medium] 77. Combinations"
date: 2025-10-20 14:00:00 -0700
categories: [leetcode, medium, backtracking, recursion, combinations]
permalink: /2025/10/20/medium-77-combinations/
---
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

## Thinking Process

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

You may return the answer in **any order**.

- Build solution incrementally; undo (backtrack) when constraints fail.
- Prune branches early to avoid exploring invalid partial states.
- Sort input to skip duplicate combinations efficiently.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Backtracking tree</text>

  <circle cx="140" cy="30" r="12" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="34" text-anchor="middle" font-size="9">start</text>
  <line x1="140" y1="42" x2="90" y2="65" stroke="#9A9792"/><line x1="140" y1="42" x2="190" y2="65" stroke="#9A9792"/>
  <circle cx="90" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/><circle cx="190" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/>
  <line x1="90" y1="82" x2="60" y2="100" stroke="#9A9792" stroke-dasharray="3"/><line x1="190" y1="82" x2="220" y2="100" stroke="#9A9792" stroke-dasharray="3"/>
  <text x="140" y="118" text-anchor="middle" font-size="11" fill="#6B6560">choose → explore → undo (prune)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Choose / explore / unchoose** *(this problem)* | $O(2^n)$ | $O(n)$ | Subsets, combinations |
| Constraint pruning | Reduced search | $O(n)$ | Early exit on invalid partial |
| Sort + skip duplicates | $O(2^n)$ | $O(n)$ | Combination sum II style |
| Path recording | $O(n!)$ worst | $O(n)$ | Permutations |

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

### Solution Explanation

**Approach:** Choose / explore / unchoose (this problem)

**Key idea:** Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

**How the code works:**
- Build solution incrementally; undo (backtrack) when constraints fail.
- Prune branches early to avoid exploring invalid partial states.
- Sort input to skip duplicate combinations efficiently.

**Walkthrough** — input `n = 4, k = 2`, expected output `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`:

There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [46. Permutations](https://www.leetcode.com/problems/permutations/)
- [47. Permutations II](https://www.leetcode.com/problems/permutations-ii/)
- [78. Subsets](https://www.leetcode.com/problems/subsets/)
- [90. Subsets II](https://www.leetcode.com/problems/subsets-ii/)

## Tags

`Backtracking`, `Recursion`, `Combinations`, `DFS`, `Medium`

## Key Takeaways

- Build solution incrementally; undo (backtrack) when constraints fail.
- Prune branches early to avoid exploring invalid partial states.
- Sort input to skip duplicate combinations efficiently.

## References

- [LC 77: Combinations on LeetCode](https://www.leetcode.com/problems/combinations/)
- [LeetCode Discuss — LC 77: Combinations](https://www.leetcode.com/problems/combinations/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/combinations/editorial/) *(may require premium)*

## Template Reference

- [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/)
