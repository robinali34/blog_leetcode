---
layout: post
title: "3110. Score of a String"
date: 2026-01-18 00:00:00 -0700
categories: [leetcode, easy, string, array]
permalink: /2026/01/18/easy-3110-score-of-a-string/
tags: [leetcode, easy, string, array, simulation, ascii]
---

# 3110. Score of a String

## Problem Statement

You are given a string `s`. The **score** of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the **score** of `s`.

## Examples

**Example 1:**
```
Input: s = "hello"
Output: 13

Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'l' = 108, 'o' = 111.
So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
```

**Example 2:**
```
Input: s = "zaz"
Output: 50

Explanation:
The ASCII values of the characters in s are: 'z' = 122, 'a' = 97, 'z' = 122.
So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
```

## Constraints

- `2 <= s.length <= 100`
- `s` consists only of lowercase English letters.

## Solution Approach

This is a straightforward **simulation** problem. We need to:
1. Iterate through all adjacent pairs of characters
2. Calculate the absolute difference between their ASCII values
3. Sum all the differences

### Key Insights:

1. **Adjacent Pairs**: Only consider consecutive characters `(s[i], s[i+1])`
2. **Absolute Difference**: Use `abs()` to get positive values
3. **ASCII Values**: Characters are automatically converted to integers in C++
4. **Single Pass**: Process the string in one iteration

### Algorithm:

1. Initialize `sum = 0`
2. Loop from `i = 0` to `i = s.length() - 2`
3. For each pair `(s[i], s[i+1])`:
   - Calculate `abs(s[i] - s[i+1])`
   - Add to `sum`
4. Return `sum`

## Solution

```cpp
class Solution {
public:
    int scoreOfString(string s) {
        int sum = 0;
        for(int i = 0; i < (int)s.length() - 1; i++) {
            sum += abs(s[i] - s[i + 1]);
        }
        return sum;
    }
};
```

### Algorithm Explanation:

1. **Initialization**: `sum = 0` to accumulate the score
2. **Iteration**: Loop from `0` to `s.length() - 2` to access all adjacent pairs
   - Note: Cast `s.length()` to `int` to avoid unsigned integer issues
3. **Calculation**: For each adjacent pair:
   - `s[i] - s[i+1]` computes the difference in ASCII values
   - `abs()` ensures we get the absolute (positive) difference
   - Add to `sum`
4. **Return**: Return the total sum

### Example Walkthrough:

**Input:** `s = "hello"`

```
i=0: |'h' - 'e'| = |104 - 101| = 3, sum = 3
i=1: |'e' - 'l'| = |101 - 108| = 7, sum = 10
i=2: |'l' - 'l'| = |108 - 108| = 0, sum = 10
i=3: |'l' - 'o'| = |108 - 111| = 3, sum = 13
Return: 13 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Single pass through the string
  - n = length of string
  - Each iteration does constant work
  - Overall: O(n)

- **Space Complexity:** O(1)
  - Only using a few variables (`sum`, `i`)
  - No additional data structures
  - Overall: O(1) extra space

## Key Insights

1. **Simple Simulation**: No complex algorithm needed, just iterate and sum
2. **ASCII Conversion**: Characters automatically convert to integers in C++
3. **Boundary Handling**: Loop from `0` to `length-2` to access all adjacent pairs
4. **Type Safety**: Cast `s.length()` to `int` to avoid unsigned comparison issues
5. **Absolute Value**: Always use `abs()` to ensure positive differences

## Edge Cases

1. **Minimum length (n=2)**: `s = "ab"` → `|97 - 98| = 1`
2. **Same characters**: `s = "aa"` → `|97 - 97| = 0`
3. **Maximum difference**: `s = "az"` → `|97 - 122| = 25`
4. **Repeated characters**: `s = "aaa"` → `0 + 0 = 0`
5. **Alternating**: `s = "abab"` → `1 + 1 + 1 = 3`

## Common Mistakes

1. **Off-by-one error**: Looping to `s.length()` instead of `s.length() - 1`
2. **Unsigned comparison**: Not casting `s.length()` to `int` can cause issues
3. **Forgetting absolute value**: Using `s[i] - s[i+1]` without `abs()`
4. **Empty string**: Not handling (though constraints guarantee `n >= 2`)
5. **Integer overflow**: Not an issue here since ASCII values are small (97-122)

## Alternative Approaches

### Using `std::accumulate` (C++)

```cpp
class Solution {
public:
    int scoreOfString(string s) {
        int sum = 0;
        for(int i = 0; i < (int)s.length() - 1; i++) {
            sum += abs(s[i] - s[i + 1]);
        }
        return sum;
    }
};
```

The provided solution is already optimal. Alternative approaches would be similar in complexity.

## Related Problems

- [LC 3111: Minimum Rectangles to Cover Points](https://leetcode.com/problems/minimum-rectangles-to-cover-points/) - Similar string/array processing
- [LC 3112: Minimum Time to Visit Disappearing Nodes](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/) - Graph traversal
- [LC 13: Roman to Integer](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-13-roman-to-integer/) - Character value processing
- [LC 171: Excel Sheet Column Number](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-171-excel-sheet-column-number/) - Character to number conversion

---

*This problem is a simple **simulation** exercise that demonstrates basic string iteration and ASCII value manipulation. The key is to iterate through adjacent pairs and sum their absolute differences.*

