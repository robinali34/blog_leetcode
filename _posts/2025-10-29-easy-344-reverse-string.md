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
