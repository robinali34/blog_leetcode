---
layout: post
title: "LC 344: Reverse String"
date: 2025-10-29 00:00:00 -0700
categories: leetcode easy two-pointers string
permalink: /posts/2025-10-29-easy-344-reverse-string/
tags: [leetcode, easy, two-pointers, string]
---

# LC 344: Reverse String

Reverse the array of characters in-place using O(1) extra memory.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **In-place requirement**: Can we use extra space? (Assumption: O(1) extra memory only - cannot use additional array)

2. **Modification**: Should we modify the input array? (Assumption: Yes - reverse in-place, modify the original array)

3. **Return value**: What should we return? (Assumption: Void - modify array in-place, no return value)

4. **Character set**: What characters can be in the array? (Assumption: Any characters - letters, digits, symbols)

5. **Empty array**: What if array is empty? (Assumption: No operation needed - empty array is already reversed)

## Approach

Two pointers at the ends swap characters and converge toward the center.
- Initialize `left=0`, `right=n-1`
- While `left < right`, swap `s[left]` with `s[right]`, then move inward

## C++ Solution

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0, right = (int)s.size() - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            ++left;
            --right;
        }
    }
};
```

## Complexity

- Time: O(n)
- Space: O(1)
