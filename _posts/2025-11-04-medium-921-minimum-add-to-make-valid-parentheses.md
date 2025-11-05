---
layout: post
title: "[Medium] 921. Minimum Add to Make Parentheses Valid"
date: 2025-11-04 22:20:28 -0800
categories: leetcode algorithm medium cpp string stack greedy problem-solving
permalink: /posts/2025-11-04-medium-921-minimum-add-to-make-valid-parentheses/
tags: [leetcode, medium, string, stack, parentheses, greedy, counting]
---

# [Medium] 921. Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

- For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(()))"` or a closing parenthesis to be `"())))"`.

Return *the minimum number of moves required to make `s` valid*.

## Examples

**Example 1:**
```
Input: s = "())"
Output: 1
Explanation: Insert '(' at the beginning: "()())"
```

**Example 2:**
```
Input: s = "((("
Output: 3
Explanation: Insert ')' at the end: "((()))"
```

**Example 3:**
```
Input: s = "()))(("
Output: 4
Explanation: Need to add 2 '(' at the beginning and 2 ')' at the end
```

## Constraints

- `1 <= s.length <= 1000`
- `s[i]` is either `'('` or `')'`.

## Solution: Greedy Counter Approach

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Use a counter to track unmatched opening parentheses. When we see a closing parenthesis, decrement if possible, otherwise we need to add an opening parenthesis. At the end, add closing parentheses for any remaining unmatched opening parentheses.

```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        int open = 0, minAdd = 0;
        
        for(char c: s) {
            if(c == '(') {
                open++;
            } else {
                open > 0 ? open--: minAdd++;
            }
        }
        
        return minAdd + open;
    }
};
```

## How the Algorithm Works

### Key Insight: Balance Tracking

- **`open`**: Counts unmatched opening parentheses
- **`minAdd`**: Counts closing parentheses we need to add
- **Greedy approach**: Match closing parentheses immediately when possible

### Step-by-Step Example: `s = "()))(("`

| Step | Char | `open` | `minAdd` | Action | Reason |
|------|------|--------|----------|--------|--------|
| Initial | - | 0 | 0 | - | - |
| 1 | `(` | 1 | 0 | Increment `open` | New opening |
| 2 | `)` | 0 | 0 | Decrement `open` | Matched with existing `(` |
| 3 | `)` | 0 | 1 | Increment `minAdd` | No `(` to match, need to add one |
| 4 | `)` | 0 | 2 | Increment `minAdd` | No `(` to match, need to add one |
| 5 | `(` | 1 | 2 | Increment `open` | New opening |
| 6 | `(` | 2 | 2 | Increment `open` | New opening |

**Final:** `minAdd = 2` (need to add 2 `(`), `open = 2` (need to add 2 `)`)  
**Total:** `2 + 2 = 4`

### Visual Representation

```
s = "()))(("
     ( ) ) ) ( (
     0 1 2 3 4 5
     
Step 1: '(' → open = 1
  Need: 1 '(' unmatched
  
Step 2: ')' → open = 0
  Matched! Now balanced
  
Step 3: ')' → minAdd = 1
  No '(' to match → need to add 1 '('
  
Step 4: ')' → minAdd = 2
  No '(' to match → need to add 1 '('
  
Step 5: '(' → open = 1
  Need: 1 '(' unmatched
  
Step 6: '(' → open = 2
  Need: 2 '(' unmatched → need to add 2 ')'

Final: minAdd = 2 (add '('), open = 2 (add ')')
Total: 4 additions
```

## Key Insights

1. **Counter-Based**: Use a counter instead of stack for single bracket type
2. **Greedy Matching**: Match closing parentheses immediately when possible
3. **Two Types of Deficits**:
   - **Unmatched closing**: Tracked by `minAdd` (need to add opening)
   - **Unmatched opening**: Tracked by `open` (need to add closing)
4. **Final Answer**: Sum of both deficits

## Algorithm Breakdown

### 1. Initialize Counters
```cpp
int open = 0, minAdd = 0;
```
- **`open`**: Tracks unmatched opening parentheses
- **`minAdd`**: Tracks closing parentheses we need to add

### 2. Process Opening Parentheses
```cpp
if(c == '(') {
    open++;
}
```
- Increment `open` counter
- This represents an opening that needs to be closed later

### 3. Process Closing Parentheses
```cpp
else {
    open > 0 ? open--: minAdd++;
}
```
- **If `open > 0`**: Match with existing opening → decrement `open`
- **If `open == 0`**: No opening to match → increment `minAdd` (need to add an opening)

### 4. Calculate Final Answer
```cpp
return minAdd + open;
```
- **`minAdd`**: Number of opening parentheses to add (for unmatched closing)
- **`open`**: Number of closing parentheses to add (for unmatched opening)
- **Sum**: Total minimum additions needed

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Single pass through string |
| **Space** | O(1) - Only using two integer variables |

## Alternative Approaches

### Approach 1: Stack-Based (More Verbose)

```cpp
int minAddToMakeValid(string s) {
    stack<char> st;
    int minAdd = 0;
    
    for(char c: s) {
        if(c == '(') {
            st.push(c);
        } else {
            if(st.empty()) {
                minAdd++;  // Need to add '('
            } else {
                st.pop();  // Match found
            }
        }
    }
    
    return minAdd + st.size();  // Add ')' for remaining '('
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Stack can hold up to n elements

### Approach 2: Two-Pass (Left to Right, Right to Left)

```cpp
int minAddToMakeValid(string s) {
    int left = 0, right = 0;
    
    // Left to right: count unmatched ')'
    for(char c: s) {
        if(c == '(') {
            left++;
        } else {
            if(left > 0) left--;
            else right++;
        }
    }
    
    return left + right;
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Note:** This is essentially the same as the counter approach, just with different variable names.

### Approach 3: Dynamic Programming (Overkill)

```cpp
// Not recommended for this problem
// DP would be O(n²) time and space
```

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Counter (Greedy)** | O(n) | O(1) | Optimal, simple | Only works for single bracket type |
| **Stack** | O(n) | O(n) | Extensible to multiple types | More memory, slower |
| **Two-Pass** | O(n) | O(1) | Clear separation | Same as counter approach |

## Edge Cases

1. **Empty string**: `""` → `0` (already valid)
2. **All opening**: `"((("` → `3` (need 3 closing)
3. **All closing**: `")))"` → `3` (need 3 opening)
4. **Already valid**: `"()()"` → `0`
5. **Nested valid**: `"((()))"` → `0`
6. **Mixed**: `"()))(("` → `4` (2 opening + 2 closing)

## Common Mistakes

1. **Only tracking one type**: Forgetting to add `open` at the end
2. **Wrong condition**: Using `open >= 0` instead of `open > 0`
3. **Not greedy**: Trying to optimize placement instead of just counting
4. **Off-by-one errors**: In length calculations

## Detailed Example Walkthrough

### Example 1: `s = "())"`

```
Step 0: Initialize
  open = 0
  minAdd = 0

Step 1: c = '('
  Opening → open = 1
  State: open=1, minAdd=0

Step 2: c = ')'
  Closing → open > 0? Yes → open = 0
  State: open=0, minAdd=0

Step 3: c = ')'
  Closing → open > 0? No → minAdd = 1
  State: open=0, minAdd=1

Final: minAdd + open = 1 + 0 = 1 ✓
```

### Example 2: `s = "((("`

```
Step 0: Initialize
  open = 0
  minAdd = 0

Step 1: c = '('
  Opening → open = 1
  State: open=1, minAdd=0

Step 2: c = '('
  Opening → open = 2
  State: open=2, minAdd=0

Step 3: c = '('
  Opening → open = 3
  State: open=3, minAdd=0

Final: minAdd + open = 0 + 3 = 3 ✓
```

### Example 3: `s = "()))(("`

```
Step 0: Initialize
  open = 0
  minAdd = 0

Step 1: c = '('
  Opening → open = 1
  State: open=1, minAdd=0

Step 2: c = ')'
  Closing → open > 0? Yes → open = 0
  State: open=0, minAdd=0

Step 3: c = ')'
  Closing → open > 0? No → minAdd = 1
  State: open=0, minAdd=1

Step 4: c = ')'
  Closing → open > 0? No → minAdd = 2
  State: open=0, minAdd=2

Step 5: c = '('
  Opening → open = 1
  State: open=1, minAdd=2

Step 6: c = '('
  Opening → open = 2
  State: open=2, minAdd=2

Final: minAdd + open = 2 + 2 = 4 ✓
```

## Why This Greedy Approach Works

### Optimal Substructure

The problem has optimal substructure:
- Making a prefix valid doesn't affect the optimal solution for the suffix
- We can greedily match parentheses as we go

### Mathematical Proof

**Claim:** The greedy approach (match immediately when possible) gives the minimum additions.

**Proof:**
1. If we have `(` and see `)`, matching immediately is optimal
   - Delaying would require adding a `)` later, which is at least as costly
2. If we see `)` with no `(` to match, we must add a `(`
   - Adding it now is as good as adding it later
3. Remaining unmatched `(` must be closed
   - No way to avoid adding `)` for each remaining `(`

Therefore, the greedy approach is optimal.

## Visualization of Different Cases

### Case 1: Unmatched Closing
```
s = ")))"
     ↑
   Need to add '(' here (or before)

Additions: 3 '('
```

### Case 2: Unmatched Opening
```
s = "((("
        ↑
      Need to add ')' here (or after)

Additions: 3 ')'
```

### Case 3: Mixed
```
s = "()))(("
     ( ) ) ) ( (
     0 1 2 3 4 5
     
Unmatched closing: positions 2, 3 → need 2 '('
Unmatched opening: positions 4, 5 → need 2 ')'

Additions: 2 '(' + 2 ')' = 4
```

## Optimization Tips

### Early Exit (Not Applicable)
We need to process the entire string to count all unmatched parentheses.

### Memory Optimization
Already optimal - O(1) space. The counter approach is the most memory-efficient.

### Branch Optimization
The ternary operator `open > 0 ? open-- : minAdd++` is efficient and clear.

## Related Problems

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Check if valid
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) - Find longest valid substring
- [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) - Remove minimum to make valid
- [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) - Remove minimum characters
- [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) - Similar to this problem

## Pattern Recognition

This problem demonstrates the **Greedy Counter Pattern**:
- Use counter instead of stack for single bracket type
- Track unmatched opening and closing separately
- Greedily match whenever possible
- Sum remaining unmatched counts

**Key Insight:**
- For single bracket type: counter is simpler and more efficient than stack
- Track two types of deficits separately
- Greedy matching is optimal

**Applications:**
- Parentheses balancing
- Bracket counting
- Expression validation
- Simple matching problems

## Extension: Multiple Bracket Types

If we had multiple bracket types like `()[]{}`, we'd need a stack:

```cpp
int minAddToMakeValid(string s) {
    stack<char> st;
    int minAdd = 0;
    
    for(char c: s) {
        if(c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if(st.empty()) {
                minAdd++;  // Need to add opening
            } else {
                char top = st.top();
                if((c == ')' && top == '(') ||
                   (c == ']' && top == '[') ||
                   (c == '}' && top == '{')) {
                    st.pop();
                } else {
                    minAdd++;  // Mismatch, need to add opening
                }
            }
        }
    }
    
    return minAdd + st.size();  // Add closing for remaining
}
```

But for single bracket type `()`, the counter approach is optimal.

## Code Quality Notes

1. **Readability**: Clear variable names (`open`, `minAdd`)
2. **Efficiency**: Optimal O(n) time, O(1) space
3. **Correctness**: Handles all edge cases properly
4. **Simplicity**: Much simpler than stack-based approach for single type

## Comparison with Similar Problems

| Problem | Approach | Complexity |
|---------|---------|-----------|
| **LC 20** (Check valid) | Stack | O(n) time, O(n) space |
| **LC 921** (Min add) | Counter | O(n) time, O(1) space |
| **LC 1249** (Min remove) | Stack | O(n) time, O(n) space |
| **LC 1541** (Min insertions) | Counter | O(n) time, O(1) space |

**Key Difference:**
- **Single bracket type** (`()`) → Counter is optimal
- **Multiple bracket types** (`()[]{}`) → Stack is needed

---

*This problem demonstrates how a simple counter-based approach can be more efficient than a stack when dealing with a single bracket type. The greedy strategy of matching immediately ensures optimality.*

