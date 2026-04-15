---
layout: post
title: "[Medium] 151. Reverse Words in a String"
date: 2026-03-27
categories: [leetcode, medium, string, two-pointers]
tags: [leetcode, medium, string, two-pointers]
permalink: /2026/03/27/medium-151-reverse-words-in-a-string/
---

Given an input string `s`, reverse the order of the **words**. A word is a sequence of non-space characters. Words are separated by at least one space. Return a string with words in reverse order, joined by a single space (no leading/trailing spaces, no extra spaces between words).

## Examples

**Example 1:**

```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**

```
Input: s = "  hello world  "
Output: "world hello"
```

**Example 3:**

```
Input: s = "a good   example"
Output: "example good a"
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters, digits, and spaces `' '`
- There is at least one word in `s`

## Thinking Process

### Key Challenges

1. **Leading/trailing spaces** -- must be stripped
2. **Multiple spaces between words** -- must be collapsed to one
3. **Reverse word order** -- not character order

### Approach 1: Deque (Collect Words in Reverse)

Trim leading/trailing spaces, scan left to right building words, and push each completed word to the **front** of a deque. This naturally reverses the order.

### Approach 2: Reverse Entire String + Reverse Each Word (In-Place)

For an $O(1)$ extra space solution:
1. Reverse the entire string
2. Reverse each individual word
3. Clean up extra spaces

## Solution 1: Deque -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    string reverseWords(string s) {
        int left = 0, right = s.size() - 1;
        while (left <= right && s[left] == ' ') ++left;
        while (left <= right && s[right] == ' ') --right;

        deque<string> d;
        string word;
        while (left <= right) {
            if (s[left] == ' ' && !word.empty()) {
                d.push_front(word);
                word.clear();
            } else if (s[left] != ' ') {
                word += s[left];
            }
            ++left;
        }
        d.push_front(word);

        string rtn;
        while (!d.empty()) {
            rtn += d.front();
            d.pop_front();
            if (!d.empty()) rtn += " ";
        }
        return rtn;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ -- deque stores all words

## Solution 2: Reverse Twice (In-Place) -- $O(1)$ extra space

{% raw %}
```cpp
class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());

        int n = s.size();
        int write = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != ' ') {
                if (write != 0) s[write++] = ' ';
                int j = i;
                while (j < n && s[j] != ' ') s[write++] = s[j++];
                reverse(s.begin() + write - (j - i), s.begin() + write);
                i = j;
            }
        }
        s.resize(write);
        return s;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(1)$ auxiliary (modifies string in-place)

### How It Works

```
Original:   "  hello world  "
Reverse all: "  dlrow olleh  "
Copy + reverse each word:
  "world" → write at 0..4
  "hello" → write at 6..10
Resize:     "world hello"
```

1. **Reverse all** flips word order but scrambles each word
2. **Reverse each word** unscrambles individual words
3. **Compact** during the copy removes extra spaces

## Comparison

| Approach | Time | Extra Space | Notes |
|---|---|---|---|
| Deque | $O(n)$ | $O(n)$ | Clean, easy to understand |
| Reverse Twice | $O(n)$ | $O(1)$ | In-place, interview follow-up |

## Common Mistakes

- Not handling multiple consecutive spaces (outputting extra spaces between words)
- Forgetting the last word (no trailing space to trigger word completion)
- In the in-place approach: not compacting spaces during the write pass

## Key Takeaways

- **"Reverse word order"** has two classic approaches: collect-in-reverse (deque/stack) or reverse-entire-then-reverse-each-word
- The in-place "reverse twice" technique is a common interview follow-up: "Can you do it in $O(1)$ space?"
- Trimming and compacting spaces is the fiddly part -- the deque approach sidesteps it by only collecting non-empty words

## Related Problems

- [186. Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) -- in-place on char array
- [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) -- reverse each word (not word order)
- [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/) -- word parsing with trailing spaces
- [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) -- string traversal

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
