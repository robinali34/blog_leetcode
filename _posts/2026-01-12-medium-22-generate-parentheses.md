---
layout: post
title: "22. Generate Parentheses"
date: 2026-01-12 00:00:00 -0700
categories: [leetcode, medium, string, backtracking, recursion]
permalink: /2026/01/12/medium-22-generate-parentheses/
tags: [leetcode, medium, string, backtracking, recursion, dfs]
---

# 22. Generate Parentheses

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Valid parentheses**: What makes a parentheses string valid? (Assumption: Every opening '(' has a matching closing ')', and they're properly nested)

2. **Output format**: Should we return all valid combinations or just count them? (Assumption: Return all distinct valid combinations - list of strings)

3. **Order requirement**: Does the order of results matter? (Assumption: No - can return in any order, but typically lexicographic order)

4. **Parentheses type**: Are we only dealing with one type of parentheses? (Assumption: Yes - only '(' and ')', not other types like '[]' or '{}')

5. **String length**: What is the length of each valid string? (Assumption: 2n - exactly n opening and n closing parentheses)

## Solution Approach

This is a classic **backtracking** problem. The key insight is to build valid parentheses strings by making choices at each step: add `'('` or `')'`, while ensuring the string remains valid.

### Key Insights:

1. **Two Choices**: At each step, we can add `'('` or `')'`
2. **Constraints**:
   - Can add `'('` if `open < n` (haven't used all opening parentheses)
   - Can add `')'` if `close < open` (have unmatched opening parentheses)
3. **Base Case**: When `path.size() == 2 * n`, we have a complete valid string
4. **Backtracking**: Try both choices, then undo (backtrack) to try other possibilities

### Algorithm:

1. **Initialize**: Start with empty path, `open = 0`, `close = 0`
2. **Base Case**: If path length equals `2 * n`, add to result and return
3. **Add Opening**: If `open < n`, add `'('`, recurse, then backtrack
4. **Add Closing**: If `close < open`, add `')'`, recurse, then backtrack
5. **Return**: All valid combinations

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

## Key Insights

1. **Backtracking Pattern**: Try choice → recurse → undo (backtrack)
2. **Two Constraints**: 
   - `open < n`: Can add opening parenthesis
   - `close < open`: Can add closing parenthesis (ensures validity)
3. **Base Case**: Complete when path length equals `2 * n`
4. **Catalan Numbers**: Number of valid combinations follows Catalan sequence

## Edge Cases

1. **n = 1**: Return `["()"]`
2. **n = 2**: Return `["(())", "()()"]`
3. **n = 3**: Return 5 combinations
4. **Large n**: Exponential growth (but n ≤ 8, so manageable)

## Common Mistakes

1. **Wrong constraint**: Using `close < n` instead of `close < open`
2. **Missing backtrack**: Forgetting to undo choices (remove character)
3. **Wrong base case**: Not checking if path is complete
4. **String reference**: Passing string by reference without copying (modifies original)
5. **Order of conditions**: Should check opening before closing for correct ordering

## Alternative Approaches

### **Approach 2: Iterative with Queue**

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        queue<pair<string, pair<int, int>>> q;
        q.push({"", {0, 0}});
        vector<string> result;
        
        while(!q.empty()) {
            auto [path, counts] = q.front();
            auto [open, close] = counts;
            q.pop();
            
            if(path.size() == 2 * n) {
                result.push_back(path);
                continue;
            }
            
            if(open < n) {
                q.push({path + "(", {open + 1, close}});
            }
            if(close < open) {
                q.push({path + ")", {open, close + 1}});
            }
        }
        
        return result;
    }
};
```

**Time Complexity:** O(4^n / √n)  
**Space Complexity:** O(4^n / √n) for queue

### **Approach 3: Dynamic Programming (Catalan Numbers)**

Build combinations by combining smaller valid parentheses strings.

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if(n == 0) return {""};
        vector<string> result;
        for(int i = 0; i < n; i++) {
            for(string left: generateParenthesis(i)) {
                for(string right: generateParenthesis(n - 1 - i)) {
                    result.push_back("(" + left + ")" + right);
                }
            }
        }
        return result;
    }
};
```

**Time Complexity:** O(4^n / √n)  
**Space Complexity:** O(4^n / √n)

## Related Problems

- [LC 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Check if parentheses are valid
- [LC 32: Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) - Find longest valid substring
- [LC 301: Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) - Remove minimum to make valid
- [LC 921: Minimum Add to Make Valid Parentheses](https://leetcode.com/problems/minimum-add-to-make-valid-parentheses/) - Minimum additions needed

---

*This problem demonstrates the classic backtracking pattern. The key is maintaining valid constraints (`open < n` and `close < open`) while exploring all possibilities through recursion and backtracking.*

