---
layout: post
title: "[Medium] 22. Generate Parentheses"
date: 2026-01-12 00:00:00 -0700
categories: [leetcode, medium, string, backtracking, recursion]
permalink: /2026/01/12/medium-22-generate-parentheses/
tags: [leetcode, medium, string, backtracking, recursion, dfs]
---
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples

**Example 1:**
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**
```
Input: n = 1
Output: ["()"]
```

## Constraints

- `1 <= n <= 8`

## Thinking Process

1. **Backtracking Pattern**: Try choice → recurse → undo (backtrack)
- `open < n`: Can add opening parenthesis
- `close < open`: Can add closing parenthesis (ensures validity)

- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.

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

### **Solution: Backtracking**

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> rtn;
        backtrack(n, 0, 0, "", rtn);
        return rtn;
    }
    
private:
    void backtrack(int n, int open, int close, string path, vector<string>& rtn) {
        if(path.size() == 2 * n) {
            rtn.push_back(path);
            return;
        }
        if(open < n) {
            path.push_back('(');
            backtrack(n, open + 1, close, path, rtn);
            path.pop_back();
        }
        if(close < open) {
            path.push_back(')');
            backtrack(n, open, close + 1, path, rtn);
            path.pop_back();
        }
    }
};
```

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **Backtracking Pattern**: Try choice → recurse → undo (backtrack)

**How the code works:**
1. **Backtracking Pattern**: Try choice → recurse → undo (backtrack)
- `open < n`: Can add opening parenthesis
- `close < open`: Can add closing parenthesis (ensures validity)
- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.

**Walkthrough** — input `n = 3`, expected output `["((()))","(()())","(())()","()(())","()()()"]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

### **Algorithm Explanation:**

1. **Main Function (Lines 3-7)**:
   - Initialize result vector
   - Call `backtrack` with initial state: `open = 0`, `close = 0`, empty path
   - Return all generated combinations

2. **Backtrack Function (Lines 10-26)**:
   - **Base Case (Lines 11-14)**: If path length is `2 * n`, we have a complete valid string
     - Add to result and return
   - **Add Opening Parenthesis (Lines 15-19)**:
     - **Condition**: `open < n` (haven't used all opening parentheses)
     - **Action**: Add `'('`, increment `open`, recurse
     - **Backtrack**: Remove `'('` to try other possibilities
   - **Add Closing Parenthesis (Lines 20-24)**:
     - **Condition**: `close < open` (have unmatched opening parentheses)
     - **Action**: Add `')'`, increment `close`, recurse
     - **Backtrack**: Remove `')'` to try other possibilities

### **Why This Works:**

- **Valid Constraint**: `close < open` ensures we never have more closing than opening parentheses
- **Complete Constraint**: `open < n` ensures we use exactly `n` opening parentheses
- **Backtracking**: Trying both choices and undoing allows us to explore all valid combinations
- **Base Case**: When path length is `2 * n`, we have used all parentheses and the string is valid

### **Example Walkthrough:**

**For `n = 2`:**

```
Initial: open=0, close=0, path=""

Level 0:
  open=0 < 2 → Add '(', path="("
    Level 1 (open=1, close=0, path="("):
      open=1 < 2 → Add '(', path="(("
        Level 2 (open=2, close=0, path="(("):
          open=2 == 2, skip
          close=0 < 2 → Add ')', path="(()"
            Level 3 (open=2, close=1, path="(()"):
              open=2 == 2, skip
              close=1 < 2 → Add ')', path="(())"
                Level 4 (open=2, close=2, path="(())"):
                  path.size() == 4 → Add to result: ["(())"]
                  Return
              Backtrack: path="(()"
          Backtrack: path="(("
      Backtrack: path="("
      close=0 < 1 → Add ')', path="()"
        Level 2 (open=1, close=1, path="()"):
          open=1 < 2 → Add '(', path="()("
            Level 3 (open=2, close=1, path="()("):
              open=2 == 2, skip
              close=1 < 2 → Add ')', path="()()"
                Level 4 (open=2, close=2, path="()()"):
                  path.size() == 4 → Add to result: ["(())", "()()"]
                  Return
              Backtrack: path="()("
          Backtrack: path="()"
      Backtrack: path="("
  Backtrack: path=""

Result: ["(())", "()()"]
```

**Tree Visualization for `n = 2`:**

```
                    ""
                   /
                  (
                 / \
               ((   ()
              /      \
           (()      ()(
            |         |
          (())      ()()
```

### **Complexity Analysis:**

- **Time Complexity:** O(4^n / √n)
  - This is the Catalan number C(n) = (2n)! / ((n+1)! × n!)
  - Each valid combination takes O(n) to build
  - Total: O(n × C(n)) = O(4^n / √n)
- **Space Complexity:** O(n)
  - Recursion stack depth: at most `2 * n` (length of path)
  - Path string: O(n) space
  - Result: O(4^n / √n) strings, each of length `2 * n`

### **Why Catalan Numbers?**

The number of valid parentheses combinations for `n` pairs is the `n`-th Catalan number:
- C(1) = 1: `"()"`
- C(2) = 2: `"(())"`, `"()()"`
- C(3) = 5: `"((()))"`, `"(()())"`, `"(())()"`, `"()(())"`, `"()()()"`

This is because:
- We need to place `n` opening and `n` closing parentheses
- At any point, number of opening ≥ number of closing
- This matches the definition of Catalan numbers
## Common Mistakes

1. **n = 1**: Return `["()"]`
2. **n = 2**: Return `["(())", "()()"]`
3. **n = 3**: Return 5 combinations
4. **Large n**: Exponential growth (but n ≤ 8, so manageable)

1. **Wrong constraint**: Using `close < n` instead of `close < open`
2. **Missing backtrack**: Forgetting to undo choices (remove character)
3. **Wrong base case**: Not checking if path is complete
4. **String reference**: Passing string by reference without copying (modifies original)
5. **Order of conditions**: Should check opening before closing for correct ordering

## Related Problems

- [LC 20: Valid Parentheses](https://www.leetcode.com/problems/valid-parentheses/) - Check if parentheses are valid
- [LC 32: Longest Valid Parentheses](https://www.leetcode.com/problems/longest-valid-parentheses/) - Find longest valid substring
- [LC 301: Remove Invalid Parentheses](https://www.leetcode.com/problems/remove-invalid-parentheses/) - Remove minimum to make valid
- [LC 921: Minimum Add to Make Valid Parentheses](https://www.leetcode.com/problems/minimum-add-to-make-valid-parentheses/) - Minimum additions needed

## Key Takeaways

1. **Backtracking Pattern**: Try choice → recurse → undo (backtrack)
2. **Two Constraints**: 
   - `open < n`: Can add opening parenthesis
   - `close < open`: Can add closing parenthesis (ensures validity)
3. **Base Case**: Complete when path length equals `2 * n`
4. **Catalan Numbers**: Number of valid combinations follows Catalan sequence

## References

- [LC 22: Generate Parentheses on LeetCode](https://www.leetcode.com/problems/generate-parentheses/)
- [LeetCode Discuss — LC 22: Generate Parentheses](https://www.leetcode.com/problems/generate-parentheses/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/generate-parentheses/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
