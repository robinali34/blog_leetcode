---
layout: post
title: "LeetCode Templates: Backtracking"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates backtracking
permalink: /posts/2025-11-24-leetcode-templates-backtracking/
tags: [leetcode, templates, backtracking, dfs]
---

{% raw %}
## Contents

- [Permutations](#permutations-all-arrangements)
- [Combinations](#combinations-choose-k-from-n)
- [Subsets](#subsets-all-subsets)
- [Combination Sum](#combination-sum-unboundedreuse-elements)
- [Grid Backtracking](#grid-backtracking-word-search-path-finding)
- [Constraint Satisfaction](#constraint-satisfaction-n-queens-sudoku)
- [Palindrome Partitioning](#palindrome-partitioning)
- [General Backtracking Template](#general-backtracking-template)

## Introduction

Backtracking is a systematic way to explore all possible solutions by building candidates incrementally and abandoning ("backtracking") partial candidates that cannot lead to valid solutions. It's essentially a depth-first search with pruning.

**Key Characteristics:**
- Builds solutions incrementally
- Abandons partial solutions that cannot be completed (pruning)
- Uses recursion to explore the solution space
- Restores state after recursive calls (backtracking step)

## Permutations (All Arrangements)

Generate all permutations of distinct elements.

### Permutations without duplicates

```cpp
// Permutations without duplicates
void backtrack(vector<int>& nums, vector<int>& cur, vector<bool>& used, vector<vector<int>>& res){
    if (cur.size() == nums.size()){
        res.push_back(cur);
        return;
    }
    for (int i = 0; i < (int)nums.size(); ++i){
        if (used[i]) continue;
        used[i] = true;
        cur.push_back(nums[i]);
        backtrack(nums, cur, used, res);
        cur.pop_back();
        used[i] = false;
    }
}
```

### Permutations with duplicates

Avoid duplicates by sorting first, then skipping duplicates at the same level when the previous duplicate hasn't been used.

```cpp
// Permutations with duplicates (avoid duplicates by sorting + skip used duplicates)
void backtrack(vector<int>& nums, vector<int>& cur, vector<bool>& used, vector<vector<int>>& res){
    if (cur.size() == nums.size()){
        res.push_back(cur);
        return;
    }
    for (int i = 0; i < (int)nums.size(); ++i){
        // Skip if already used, or if duplicate and previous duplicate not used
        if (used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1])) continue;
        used[i] = true;
        cur.push_back(nums[i]);
        backtrack(nums, cur, used, res);
        cur.pop_back();
        used[i] = false;
    }
}

// Call with sorted array
vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    vector<int> cur;
    vector<bool> used(nums.size(), false);
    backtrack(nums, cur, used, res);
    return res;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 46 | Permutations | [Link](https://leetcode.com/problems/permutations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-46-permutations/) |
| 47 | Permutations II | [Link](https://leetcode.com/problems/permutations-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-47-permutations-ii/) |

## Combinations (Choose k from n)

Generate all combinations of k elements from n elements. Order doesn't matter, so we use `start` index to avoid duplicates.

```cpp
// Combinations C(n, k)
void backtrack(int start, int n, int k, vector<int>& cur, vector<vector<int>>& res){
    if (cur.size() == k){
        res.push_back(cur);
        return;
    }
    // Only consider elements from start onwards to avoid duplicates
    for (int i = start; i <= n; ++i){
        cur.push_back(i);
        backtrack(i+1, n, k, cur, res);  // Next start is i+1
        cur.pop_back();
    }
}
```

**Key insight:** Use `start` parameter to ensure we only consider elements after the current position, preventing duplicate combinations.

| ID | Title | Link | Solution |
|---|---|---|---|
| 77 | Combinations | [Link](https://leetcode.com/problems/combinations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-77-combinations/) |

## Subsets (All Subsets)

Generate all subsets (power set) of an array. This includes the empty set and the set itself.

### Subsets without duplicates

```cpp
// Subsets without duplicates
void backtrack(int start, vector<int>& nums, vector<int>& cur, vector<vector<int>>& res){
    res.push_back(cur);  // Add current subset (including empty set)
    for (int i = start; i < (int)nums.size(); ++i){
        cur.push_back(nums[i]);
        backtrack(i+1, nums, cur, res);
        cur.pop_back();
    }
}
```

### Subsets with duplicates

Sort first, then skip duplicates at the same level.

```cpp
// Subsets with duplicates (sort first, skip duplicates at same level)
void backtrack(int start, vector<int>& nums, vector<int>& cur, vector<vector<int>>& res){
    res.push_back(cur);
    for (int i = start; i < (int)nums.size(); ++i){
        // Skip duplicates at the same level
        if (i > start && nums[i] == nums[i-1]) continue;
        cur.push_back(nums[i]);
        backtrack(i+1, nums, cur, res);
        cur.pop_back();
    }
}

// Call with sorted array
vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    vector<int> cur;
    backtrack(0, nums, cur, res);
    return res;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 78 | Subsets | [Link](https://leetcode.com/problems/subsets/) | - |
| 90 | Subsets II | [Link](https://leetcode.com/problems/subsets-ii/) | - |

## Combination Sum (Unbounded/Reuse Elements)

Find all combinations that sum to target. Elements can be reused or used once depending on the problem.

### Combination Sum (can reuse same element)

```cpp
// Combination Sum (can reuse same element)
void backtrack(int start, vector<int>& candidates, int target, vector<int>& cur, vector<vector<int>>& res){
    if (target == 0){
        res.push_back(cur);
        return;
    }
    if (target < 0) return;  // Pruning: target exceeded
    
    for (int i = start; i < (int)candidates.size(); ++i){
        cur.push_back(candidates[i]);
        // Can reuse: start=i (not i+1)
        backtrack(i, candidates, target - candidates[i], cur, res);
        cur.pop_back();
    }
}
```

### Combination Sum II (each element used once, duplicates exist)

```cpp
// Combination Sum II (each element used once, duplicates exist)
void backtrack(int start, vector<int>& candidates, int target, vector<int>& cur, vector<vector<int>>& res){
    if (target == 0){
        res.push_back(cur);
        return;
    }
    if (target < 0) return;
    
    for (int i = start; i < (int)candidates.size(); ++i){
        // Skip duplicates at the same level
        if (i > start && candidates[i] == candidates[i-1]) continue;
        cur.push_back(candidates[i]);
        // No reuse: start=i+1
        backtrack(i+1, candidates, target - candidates[i], cur, res);
        cur.pop_back();
    }
}

// Call with sorted array
vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> res;
    vector<int> cur;
    backtrack(0, candidates, target, cur, res);
    return res;
}
```

### Combination Sum III (choose k numbers from 1-9 that sum to n)

```cpp
// Combination Sum III: choose k numbers from 1-9 that sum to n
void backtrack(int start, int k, int n, vector<int>& cur, vector<vector<int>>& res){
    if (cur.size() == k && n == 0){
        res.push_back(cur);
        return;
    }
    if (cur.size() >= k || n < 0) return;
    
    for (int i = start; i <= 9; ++i){
        cur.push_back(i);
        backtrack(i+1, k, n-i, cur, res);
        cur.pop_back();
    }
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 39 | Combination Sum | [Link](https://leetcode.com/problems/combination-sum/) | - |
| 40 | Combination Sum II | [Link](https://leetcode.com/problems/combination-sum-ii/) | - |
| 216 | Combination Sum III | [Link](https://leetcode.com/problems/combination-sum-iii/) | - |

## Grid Backtracking (Word Search, Path Finding)

Backtrack on 2D grid with constraints. Mark cells as visited during exploration, then restore them.

### Word Search

```cpp
// Word Search: find if word exists in grid
bool dfs(vector<vector<char>>& board, int i, int j, string& word, int idx){
    if (idx == (int)word.size()) return true;
    if (i < 0 || i >= (int)board.size() || j < 0 || j >= (int)board[0].size()) return false;
    if (board[i][j] != word[idx]) return false;
    
    char temp = board[i][j];
    board[i][j] = '#';  // Mark as visited
    
    int dirs[4][2] = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
    for (auto& d : dirs){
        if (dfs(board, i+d[0], j+d[1], word, idx+1)) return true;
    }
    
    board[i][j] = temp;  // Backtrack: restore original value
    return false;
}

bool exist(vector<vector<char>>& board, string word) {
    for (int i = 0; i < (int)board.size(); ++i){
        for (int j = 0; j < (int)board[0].size(); ++j){
            if (dfs(board, i, j, word, 0)) return true;
        }
    }
    return false;
}
```

**Key points:**
- Mark cell as visited before recursion
- Restore cell value after recursion (backtracking)
- Check bounds and constraints before recursing

| ID | Title | Link | Solution |
|---|---|---|---|
| 79 | Word Search | [Link](https://leetcode.com/problems/word-search/) | - |
| 212 | Word Search II | [Link](https://leetcode.com/problems/word-search-ii/) | - |
| 489 | Robot Room Cleaner | [Link](https://leetcode.com/problems/robot-room-cleaner/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-hard-489-robot-room-cleaner/) |

## Constraint Satisfaction (N-Queens, Sudoku)

Backtracking with complex constraints. Validate each move before placing.

### N-Queens

```cpp
// N-Queens: place n queens on n×n board
void backtrack(int row, int n, vector<string>& board, vector<vector<string>>& res){
    if (row == n){
        res.push_back(board);
        return;
    }
    for (int col = 0; col < n; ++col){
        if (isValid(board, row, col, n)){
            board[row][col] = 'Q';
            backtrack(row+1, n, board, res);
            board[row][col] = '.';  // Backtrack
        }
    }
}

bool isValid(vector<string>& board, int row, int col, int n){
    // Check column above
    for (int i = 0; i < row; ++i) 
        if (board[i][col] == 'Q') return false;
    
    // Check diagonal \ (top-left to bottom-right)
    for (int i = row-1, j = col-1; i >= 0 && j >= 0; --i, --j)
        if (board[i][j] == 'Q') return false;
    
    // Check diagonal / (top-right to bottom-left)
    for (int i = row-1, j = col+1; i >= 0 && j < n; --i, ++j)
        if (board[i][j] == 'Q') return false;
    
    return true;
}
```

### Sudoku Solver

```cpp
// Sudoku Solver
bool solveSudoku(vector<vector<char>>& board){
    for (int i = 0; i < 9; ++i){
        for (int j = 0; j < 9; ++j){
            if (board[i][j] == '.'){
                for (char c = '1'; c <= '9'; ++c){
                    if (isValid(board, i, j, c)){
                        board[i][j] = c;
                        if (solveSudoku(board)) return true;
                        board[i][j] = '.';  // Backtrack
                    }
                }
                return false;  // No valid number found
            }
        }
    }
    return true;  // All cells filled
}

bool isValid(vector<vector<char>>& board, int row, int col, char c){
    for (int i = 0; i < 9; ++i){
        // Check row
        if (board[row][i] == c) return false;
        // Check column
        if (board[i][col] == c) return false;
        // Check 3x3 box
        if (board[3*(row/3) + i/3][3*(col/3) + i%3] == c) return false;
    }
    return true;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 51 | N-Queens | [Link](https://leetcode.com/problems/n-queens/) | - |
| 52 | N-Queens II | [Link](https://leetcode.com/problems/n-queens-ii/) | - |
| 37 | Sudoku Solver | [Link](https://leetcode.com/problems/sudoku-solver/) | - |

## Palindrome Partitioning

Partition string into palindromic substrings. Check if substring is palindrome before partitioning.

```cpp
// Palindrome Partitioning
void backtrack(int start, string& s, vector<string>& cur, vector<vector<string>>& res){
    if (start == (int)s.size()){
        res.push_back(cur);
        return;
    }
    for (int end = start; end < (int)s.size(); ++end){
        if (isPalindrome(s, start, end)){
            cur.push_back(s.substr(start, end-start+1));
            backtrack(end+1, s, cur, res);
            cur.pop_back();  // Backtrack
        }
    }
}

bool isPalindrome(string& s, int l, int r){
    while (l < r) {
        if (s[l++] != s[r--]) return false;
    }
    return true;
}
```

**Optimization:** Precompute palindrome table to avoid repeated checks.

```cpp
// Optimized: Precompute palindrome table
vector<vector<bool>> precomputePalindromes(string& s){
    int n = s.size();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    for (int i = n-1; i >= 0; --i){
        for (int j = i; j < n; ++j){
            if (i == j) dp[i][j] = true;
            else if (j == i+1) dp[i][j] = (s[i] == s[j]);
            else dp[i][j] = (s[i] == s[j] && dp[i+1][j-1]);
        }
    }
    return dp;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 131 | Palindrome Partitioning | [Link](https://leetcode.com/problems/palindrome-partitioning/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/30/medium-131-palindrome-partitioning/) |
| 132 | Palindrome Partitioning II | [Link](https://leetcode.com/problems/palindrome-partitioning-ii/) | - |

## General Backtracking Template

```cpp
void backtrack(state, constraints, current_solution, results){
    // Base case: solution is complete
    if (isComplete(current_solution)){
        results.add(current_solution);
        return;
    }
    
    // Generate candidates
    for (each candidate in candidates){
        // Pruning: skip invalid candidates early
        if (isValid(candidate, constraints)){
            // Make move: add candidate to solution
            makeMove(candidate, current_solution);
            
            // Recurse: explore further
            backtrack(updated_state, constraints, current_solution, results);
            
            // Backtrack: remove candidate to try next option
            undoMove(candidate, current_solution);
        }
    }
}
```

**Key Points:**
- **Base Case**: When solution is complete, add to results
- **Pruning**: Skip invalid candidates early to reduce search space
- **Make Move**: Add candidate to current solution and update state
- **Recurse**: Explore further with updated state
- **Backtrack**: Remove candidate and restore state to try next option

**Common Optimizations:**
1. **Early pruning**: Check constraints before recursing
2. **Memoization**: Cache results for repeated subproblems (if applicable)
3. **Sorting**: Sort input to handle duplicates efficiently
4. **Precomputation**: Precompute expensive checks (e.g., palindrome table)

**Time Complexity:** Typically exponential O(2^n) or O(n!) depending on problem
**Space Complexity:** O(depth) for recursion stack + O(solution_size) for current solution
{% endraw %}

