---
layout: post
title: "[Medium] 316. Remove Duplicate Letters"
date: 2025-10-17 22:23:33 -0700
categories: leetcode algorithm medium cpp stack monotonic-stack greedy problem-solving
---
Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the **smallest in lexicographical order** among all possible results.

## Examples

**Example 1:**
```
Input: s = "bcabc"
Output: "abc"
Explanation: 
- Remove duplicate 'b' and 'c'
- Result "abc" is lexicographically smallest
```

**Example 2:**
```
Input: s = "cbacdcbc"
Output: "acdb"
Explanation: 
- Remove duplicate 'c' and 'b'
- Result "acdb" is lexicographically smallest
```

**Example 3:**
```
Input: s = "bbcaac"
Output: "bac"
Explanation: 
- Remove duplicate 'b' and 'c'
- Result "bac" is lexicographically smallest
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters only.

## Thinking Process

1. **Lexicographically smallest:** Always prefer smaller characters
1. **Maintains order:** Characters in lexicographical order

- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in O(n).

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Stack</text>

  <rect x="100" y="30" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="46" text-anchor="middle" font-size="10">top</text>
  <rect x="100" y="54" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="100" y="78" width="80" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="200" y="70" font-size="11" fill="#6B6560">push / pop</text>
  <path d="M90 42v60" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="115" text-anchor="middle" font-size="11" fill="#6B6560">LIFO — monotonic stack scans array</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Monotonic stack** *(this problem)* | O(n) | O(n) | Next greater/smaller element |
| Parentheses matching | O(n) | O(n) | Push open, pop on close |
| Expression evaluation | O(n) | O(n) | Operand + operator stacks |
| Stack simulation | O(n) | O(n) | Process in LIFO order |

## Solution

**Time Complexity:** O(n) where n is the length of string  
**Space Complexity:** O(1) since we use at most 26 characters

Use a monotonic stack to maintain lexicographically smallest result while ensuring each character appears exactly once.

```cpp
class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<int> count(26, 0);
        vector<bool> visited(26, false);
        stack<char> st;
        
        // Count frequency of each character
        for(char c : s) {
            count[c - 'a']++;
        }
        
        for(char c : s) {
            count[c - 'a']--;
            
            // Skip if already in result
            if(visited[c - 'a']) continue;
            
            // Remove characters that are:
            // 1. Greater than current character
            // 2. Will appear again later
            while(!st.empty() && st.top() > c && count[st.top() - 'a'] > 0) {
                visited[st.top() - 'a'] = false;
                st.pop();
            }
            
            st.push(c);
            visited[c - 'a'] = true;
        }
        
        string result;
        while(!st.empty()) {
            result = st.top() + result;
            st.pop();
        }
        
        return result;
    }
};
```

### Solution Explanation
**Key Insight:** Use a monotonic stack to maintain lexicographically smallest result while ensuring each character appears exactly once.

**Steps:**
1. **Count frequency** of each character in the string
2. **Use visited array** to track characters already in result
3. **For each character:**
   - Skip if already processed
   - Remove characters from stack that are:
     - Greater than current character (lexicographically)
     - Will appear again later (count > 0)
4. **Add current character** to stack and mark as visited
5. **Build result** from stack

## Step-by-Step Example

### Example: `s = "cbacdcbc"`

**Initial state:**
- `count = [2,2,2,1]` (a=2, b=2, c=2, d=1)
- `visited = [false,false,false,false]`
- `stack = []`

**Processing each character:**

| Char | Count After | Visited | Stack Operation | Stack State |
|------|-------------|---------|-----------------|-------------|
| 'c' | [2,2,1,1] | [f,f,t,f] | Push 'c' | ['c'] |
| 'b' | [2,1,1,1] | [f,t,t,f] | Push 'b' | ['c','b'] |
| 'a' | [1,1,1,1] | [t,t,t,f] | Pop 'b','c', Push 'a' | ['a'] |
| 'c' | [1,1,0,1] | [t,t,t,f] | Skip (already visited) | ['a'] |
| 'd' | [1,1,0,0] | [t,t,t,t] | Push 'd' | ['a','d'] |
| 'c' | [1,1,0,0] | [t,t,t,t] | Skip (already visited) | ['a','d'] |
| 'b' | [1,0,0,0] | [t,t,t,t] | Skip (already visited) | ['a','d'] |
| 'c' | [0,0,0,0] | [t,t,t,t] | Skip (already visited) | ['a','d'] |

**Final result:** `"acdb"`

## Algorithm Breakdown

### Core Logic:
```cpp
for(char c : s) {
    count[c - 'a']--;
    
    // Skip if already in result
    if(visited[c - 'a']) continue;
    
    // Remove characters that are:
    // 1. Greater than current character
    // 2. Will appear again later
    while(!st.empty() && st.top() > c && count[st.top() - 'a'] > 0) {
        visited[st.top() - 'a'] = false;
        st.pop();
    }
    
    st.push(c);
    visited[c - 'a'] = true;
}
```

**Process:**
1. **Decrement count** for current character
2. **Skip if already processed** (visited)
3. **Remove larger characters** that will appear again
4. **Add current character** to stack
5. **Mark as visited**

### Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Count frequency | O(n) | O(1) |
| Process characters | O(n) | O(1) |
| Stack operations | O(n) | O(1) |
| Build result | O(n) | O(1) |
| **Total** | **O(n)** | **O(1)** |

Where n is the length of the string.

## Detailed Example Walkthrough

### Example: `s = "bcabc"`

**Initial state:**
- `count = [1,2,2]` (a=1, b=2, c=2)
- `visited = [false,false,false]`
- `stack = []`

**Processing each character:**

| Char | Count After | Visited | Stack Operation | Stack State | Explanation |
|------|-------------|---------|-----------------|-------------|-------------|
| 'b' | [1,1,2] | [f,t,f] | Push 'b' | ['b'] | First 'b', add to stack |
| 'c' | [1,1,1] | [f,t,t] | Push 'c' | ['b','c'] | First 'c', add to stack |
| 'a' | [0,1,1] | [t,t,t] | Pop 'c','b', Push 'a' | ['a'] | 'a' < 'c','b', and 'c','b' will appear again |
| 'b' | [0,0,1] | [t,t,t] | Skip (already visited) | ['a'] | 'b' already in result |
| 'c' | [0,0,0] | [t,t,t] | Skip (already visited) | ['a'] | 'c' already in result |

**Final result:** `"abc"`

## Common Mistakes

1. **Single character:** `s = "a"` → `"a"`
2. **All same characters:** `s = "aaaa"` → `"a"`
3. **Already sorted:** `s = "abc"` → `"abc"`
4. **Reverse sorted:** `s = "cba"` → `"abc"`

1. **Wrong removal condition:** Not checking if character will appear again
2. **Missing visited check:** Processing same character multiple times
3. **Incorrect stack order:** Not maintaining lexicographical order
4. **Count management:** Not properly decrementing counts

## Related Problems

- [402. Remove K Digits](https://www.leetcode.com/problems/remove-k-digits/)
- [321. Create Maximum Number](https://www.leetcode.com/problems/create-maximum-number/)
- [1081. Smallest Subsequence of Distinct Characters](https://www.leetcode.com/problems/smallest-subsequence-of-distinct-characters/)
- [316. Remove Duplicate Letters](https://www.leetcode.com/problems/remove-duplicate-letters/)

## Why This Solution Works

### Greedy Strategy:
1. **Lexicographically smallest:** Always prefer smaller characters
2. **One occurrence:** Each character appears exactly once
3. **Future availability:** Consider if character will appear again
4. **Optimal choice:** Make locally optimal choice at each step

### Monotonic Stack:
1. **Maintains order:** Characters in lexicographical order
2. **Efficient removal:** Can remove multiple characters at once
3. **Future consideration:** Checks if characters will appear again
4. **Optimal result:** Ensures smallest lexicographical order

### Key Algorithm Properties:
1. **Correctness:** Always produces valid result
2. **Optimality:** Produces lexicographically smallest result
3. **Efficiency:** O(n) time complexity
4. **Simplicity:** Easy to understand and implement

## References

- [LC 316: Remove Duplicate Letters on LeetCode](https://www.leetcode.com/problems/remove-duplicate-letters/)
- [LeetCode Discuss — LC 316: Remove Duplicate Letters](https://www.leetcode.com/problems/remove-duplicate-letters/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/remove-duplicate-letters/editorial/) *(may require premium)*

## Key Takeaways

### Greedy Strategy:
1. **Lexicographically smallest:** Always prefer smaller characters
2. **One occurrence:** Each character appears exactly once
3. **Future availability:** Consider if character will appear again
4. **Stack property:** Maintains order and allows efficient removal

### Monotonic Stack:
1. **Maintains order:** Characters in lexicographical order
2. **Efficient removal:** Can remove multiple characters at once
3. **Future consideration:** Checks if characters will appear again
4. **Optimal result:** Ensures smallest lexicographical order
