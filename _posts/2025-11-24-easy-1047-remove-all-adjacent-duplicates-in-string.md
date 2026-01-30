---
layout: post
title: "[Easy] 1047. Remove All Adjacent Duplicates In String"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm easy cpp string stack two-pointers problem-solving
permalink: /posts/2025-11-24-easy-1047-remove-all-adjacent-duplicates-in-string/
tags: [leetcode, easy, string, stack, two-pointers, in-place]
---

# [Easy] 1047. Remove All Adjacent Duplicates In String

You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.

We repeatedly make **duplicate removals** on `s` until we no longer can.

Return *the final string after all such duplicate removals have been made*. It can be proven that the answer is **unique**.

## Examples

**Example 1:**
```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is "aaca" of which only "aa" is possible, so the final string is "ca".
```

**Example 2:**
```
Input: s = "azxxzy"
Output: "ay"
Explanation: 
First, we remove "xx" to get "azzy". Then we remove "zz" to get "ay".
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Duplicate removal**: What does "adjacent duplicates" mean? (Assumption: Two identical characters next to each other - "aa" is adjacent duplicates)

2. **Removal process**: How should we remove duplicates? (Assumption: Remove pairs of adjacent duplicates repeatedly until no more exist)

3. **Cascading removal**: Can removal cause new duplicates? (Assumption: Yes - removing "aa" from "baa" leaves "b", removing "aa" from "aab" leaves "b")

4. **Return format**: What should we return? (Assumption: Final string after all duplicate removals)

5. **Empty string**: What if string becomes empty? (Assumption: Return empty string "")

## Solution Approaches

### Approach 1: Stack-Based Solution

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Use a stack (or string as stack) to track characters. When encountering a character that matches the top of the stack, pop it. Otherwise, push the character.

### Approach 2: In-Place Two Pointers

**Time Complexity:** O(n)  
**Space Complexity:** O(1) excluding output space

Use two pointers to simulate a stack in-place. `left` acts as the stack pointer, `right` iterates through the string.

## Solution 1: Stack-Based (String as Stack)

```cpp
class Solution {
public:
    string removeDuplicates(string s) {
        string stk;
        for(char ch: s) {
            if(!stk.empty() && stk.back() == ch) {
                stk.pop_back();
            } else {
                stk.push_back(ch);
            }
        }
        return stk;
    }
};
```

## Solution 2: In-Place Two Pointers

```cpp
class Solution {
public:
    string removeDuplicates(string s) {
        int left = -1;
        for(int right = 0; right < s.size(); right++) {
            if(left >= 0 && s[right] == s[left]) {
                left--;
                continue;
            }
            s[++left] = s[right];
        }
        return s.substr(0, left + 1);
    }
};
```

## How the Algorithms Work

### Stack-Based Approach

**Key Insight:** This problem is similar to matching parentheses. When we see a duplicate, we remove both characters (like popping from stack).

**Step-by-Step Example: `s = "abbaca"`**

```
Step | Char | Stack Before | Action | Stack After
-----|------|--------------|--------|-------------
0    | -    | ""           | Init   | ""
1    | 'a'  | ""           | Push   | "a"
2    | 'b'  | "a"          | Push   | "ab"
3    | 'b'  | "ab"         | Pop    | "a"  (b == b)
4    | 'a'  | "a"          | Pop    | ""   (a == a)
5    | 'c'  | ""           | Push   | "c"
6    | 'a'  | "c"          | Push   | "ca"

Result: "ca"
```

**Visual Representation:**
```
"abbaca"
  ↓
"a" → push 'a'
"ab" → push 'b'
"a" → pop 'b' (duplicate)
"" → pop 'a' (duplicate)
"c" → push 'c'
"ca" → push 'a'
```

### In-Place Two Pointers Approach

**Key Insight:** Use `left` as a stack pointer. When we find a duplicate, decrement `left` (simulating pop). Otherwise, increment `left` and assign (simulating push).

**Step-by-Step Example: `s = "abbaca"`**

```
Step | right | s[right] | left | s[0..left] | Action
-----|-------|----------|------|-------------|--------
0    | 0     | 'a'      | -1   | ""          | left=0, s[0]='a'
1    | 1     | 'b'      | 0    | "a"         | left=1, s[1]='b'
2    | 2     | 'b'      | 1    | "ab"        | left=0 (pop: b==b)
3    | 3     | 'a'      | 0    | "a"         | left=-1 (pop: a==a)
4    | 4     | 'c'      | -1   | ""          | left=0, s[0]='c'
5    | 5     | 'a'      | 0    | "c"         | left=1, s[1]='a'

Result: s.substr(0, 2) = "ca"
```

**Visual Representation:**
```
Initial: left = -1, right = 0
s = ['a', 'b', 'b', 'a', 'c', 'a']
      ↑
    right=0, left=-1 → left=0, s[0]='a'

s = ['a', 'b', 'b', 'a', 'c', 'a']
           ↑
    right=1, left=0 → left=1, s[1]='b'

s = ['a', 'b', 'b', 'a', 'c', 'a']
                ↑
    right=2, left=1, s[2]=='b'==s[1] → left=0 (pop)

s = ['a', 'b', 'b', 'a', 'c', 'a']
                     ↑
    right=3, left=0, s[3]=='a'==s[0] → left=-1 (pop)

s = ['a', 'b', 'b', 'a', 'c', 'a']
                          ↑
    right=4, left=-1 → left=0, s[0]='c'

s = ['a', 'b', 'b', 'a', 'c', 'a']
                               ↑
    right=5, left=0 → left=1, s[1]='a'

Final: s.substr(0, 2) = "ca"
```

## Key Insights

1. **Stack Pattern**: This is essentially a stack problem - matching adjacent pairs
2. **In-Place Optimization**: Can simulate stack using two pointers to save space
3. **Greedy Approach**: Remove duplicates as soon as we find them
4. **No Need for Multiple Passes**: Single pass is sufficient with proper data structure

## Algorithm Breakdown

### Stack-Based Solution

```cpp
string stk;
for(char ch: s) {
    if(!stk.empty() && stk.back() == ch) {
        stk.pop_back();  // Remove duplicate
    } else {
        stk.push_back(ch);  // Add character
    }
}
return stk;
```

**How it works:**
1. Iterate through each character
2. If stack is not empty and top matches current character → pop (remove duplicate)
3. Otherwise → push current character
4. Return final stack contents

### In-Place Two Pointers Solution

```cpp
int left = -1;  // Stack pointer (points to last valid character)
for(int right = 0; right < s.size(); right++) {
    if(left >= 0 && s[right] == s[left]) {
        left--;  // Pop: move stack pointer back
        continue;
    }
    s[++left] = s[right];  // Push: increment and assign
}
return s.substr(0, left + 1);
```

**How it works:**
1. `left` acts as stack pointer (points to last valid character)
2. `right` iterates through input string
3. If `left >= 0` and `s[right] == s[left]` → decrement `left` (pop)
4. Otherwise → increment `left` and assign `s[right]` (push)
5. Return substring from 0 to `left+1`

## Edge Cases

1. **Empty string**: Returns empty string
2. **All duplicates**: `"aaaa"` → `""`
3. **No duplicates**: `"abc"` → `"abc"`
4. **Nested duplicates**: `"abccba"` → `""`
5. **Single character**: `"a"` → `"a"`

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Stack (String)** | O(n) | O(n) | Simple, readable | Extra space |
| **In-Place Two Pointers** | O(n) | O(1) | Space efficient | Slightly more complex |

## Implementation Details

### Stack-Based: Why String Works

```cpp
string stk;  // Acts as stack
stk.back()    // Top of stack
stk.pop_back() // Pop from stack
stk.push_back() // Push to stack
```

**Why use string instead of stack<char>?**
- Easier to return result (no need to reverse)
- Same time complexity
- More memory efficient for this use case

### In-Place: Two Pointer Logic

```cpp
int left = -1;  // Points to last valid character (-1 means empty)
```

**Why `left = -1` initially?**
- Represents empty stack
- `left >= 0` check ensures stack is not empty before comparing
- `s[++left]` increments first, then assigns (pushes to stack)

**Why `continue` after decrementing?**
- Skip assigning current character (we've already "popped" it)
- Move to next character immediately

## Alternative Approaches

### Approach 3: Using STL Stack

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    string removeDuplicates(string s) {
        stack<char> stk;
        for(char ch: s) {
            if(!stk.empty() && stk.top() == ch) {
                stk.pop();
            } else {
                stk.push(ch);
            }
        }
        
        string result;
        while(!stk.empty()) {
            result = stk.top() + result;
            stk.pop();
        }
        return result;
    }
};
```

**Pros:**
- Explicit stack usage
- Clear intent

**Cons:**
- Need to reverse result
- More verbose

### Approach 4: Recursive Solution

**Time Complexity:** O(n²) worst case  
**Space Complexity:** O(n) for recursion stack

```cpp
class Solution {
public:
    string removeDuplicates(string s) {
        for(int i = 0; i < (int)s.size() - 1; i++) {
            if(s[i] == s[i+1]) {
                return removeDuplicates(s.substr(0, i) + s.substr(i+2));
            }
        }
        return s;
    }
};
```

**Pros:**
- Intuitive recursive thinking

**Cons:**
- Inefficient (creates new strings)
- Stack overflow risk for large inputs

## Common Mistakes

1. **Not handling empty stack**: Forgetting to check `!stk.empty()` before accessing top
2. **Wrong comparison**: Comparing with wrong character
3. **In-place index errors**: Off-by-one errors with `left` pointer
4. **Multiple passes**: Trying to do multiple passes instead of single pass
5. **Not using continue**: In in-place solution, forgetting `continue` after decrementing

## Optimization Tips

1. **Use string as stack**: More efficient than `stack<char>` for this problem
2. **In-place when possible**: Two-pointer approach saves space
3. **Early termination**: Can optimize if we know string length (not applicable here)

## Related Problems

- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Similar stack pattern
- [1544. Make The String Great](https://leetcode.com/problems/make-the-string-great/) - Similar duplicate removal
- [1209. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) - Extension with k duplicates
- [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) - This problem

## Real-World Applications

1. **Text Processing**: Removing duplicate characters in text editors
2. **Data Cleaning**: Removing adjacent duplicates in data streams
3. **Compression**: Basic run-length encoding preprocessing
4. **Parsing**: Removing redundant tokens in parsers

## Pattern Recognition

This problem demonstrates the **"Stack for Matching Pairs"** pattern:

```
1. Use stack to track elements
2. When encountering matching pair → pop
3. Otherwise → push
4. Return remaining stack contents
```

Similar problems:
- Valid Parentheses
- Make The String Great
- Remove K Digits
- Decode String

## Why Stack Works

1. **LIFO Property**: Last character added is first to be matched
2. **Adjacent Matching**: Duplicates are always adjacent, matching stack's top
3. **Cascading Removals**: Removing one pair may create new adjacent pairs
4. **Single Pass**: Stack handles cascading removals in one pass

## In-Place Optimization Explanation

**Why it works:**
- `left` pointer simulates stack top
- `s[0..left]` represents current stack contents
- When duplicate found, decrement `left` (pop)
- When new character, increment `left` and assign (push)
- Final result is `s[0..left]`

**Space savings:**
- Stack approach: O(n) extra space
- In-place: O(1) extra space (reusing input string)

## Step-by-Step Trace: `s = "azxxzy"`

### Stack Approach:
```
'a' → push → stack: "a"
'z' → push → stack: "az"
'x' → push → stack: "azx"
'x' → pop  → stack: "az"  (x == x)
'z' → pop  → stack: "a"   (z == z)
'y' → push → stack: "ay"
Result: "ay"
```

### In-Place Approach:
```
right=0: 'a' → left=0, s[0]='a'
right=1: 'z' → left=1, s[1]='z'
right=2: 'x' → left=2, s[2]='x'
right=3: 'x' → left=1 (pop, x==x)
right=4: 'z' → left=0 (pop, z==z)
right=5: 'y' → left=1, s[1]='y'
Result: s.substr(0, 2) = "ay"
```

## Comparison: Stack vs In-Place

| Aspect | Stack | In-Place |
|--------|-------|----------|
| **Readability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Space** | O(n) | O(1) |
| **Time** | O(n) | O(n) |
| **Code Length** | Shorter | Slightly longer |
| **Best For** | Clarity | Space constraints |

---

*This problem is an excellent example of using a stack to solve matching problems, with an elegant in-place optimization using two pointers.*

