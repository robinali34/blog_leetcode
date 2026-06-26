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

For an O(1) extra space solution:
1. Reverse the entire string
2. Reverse each individual word
3. Clean up extra spaces

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Solution
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

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** ### Key Challenges

**How the code works:**
1. **Leading/trailing spaces** -- must be stripped
2. **Multiple spaces between words** -- must be collapsed to one
3. **Reverse word order** -- not character order
1. Reverse the entire string
2. Reverse each individual word
3. Clean up extra spaces

**Walkthrough** — input `s = "the sky is blue"`, expected output `"blue is sky the"`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Comparison

| Approach | Time | Extra Space | Notes |
|---|---|---|---|
| Deque | O(n) | O(n) | Clean, easy to understand |
| Reverse Twice | O(n) | O(1) | In-place, interview follow-up |

## Common Mistakes

- Not handling multiple consecutive spaces (outputting extra spaces between words)
- Forgetting the last word (no trailing space to trigger word completion)
- In the in-place approach: not compacting spaces during the write pass

## Key Takeaways

- **"Reverse word order"** has two classic approaches: collect-in-reverse (deque/stack) or reverse-entire-then-reverse-each-word
- The in-place "reverse twice" technique is a common interview follow-up: "Can you do it in O(1) space?"
- Trimming and compacting spaces is the fiddly part -- the deque approach sidesteps it by only collecting non-empty words

## Related Problems

- [186. Reverse Words in a String II](https://www.leetcode.com/problems/reverse-words-in-a-string-ii/) -- in-place on char array
- [557. Reverse Words in a String III](https://www.leetcode.com/problems/reverse-words-in-a-string-iii/) -- reverse each word (not word order)
- [58. Length of Last Word](https://www.leetcode.com/problems/length-of-last-word/) -- word parsing with trailing spaces
- [1768. Merge Strings Alternately](https://www.leetcode.com/problems/merge-strings-alternately/) -- string traversal

## References

- [LC 151: Reverse Words in a String on LeetCode](https://www.leetcode.com/problems/reverse-words-in-a-string/)
- [LeetCode Discuss — LC 151: Reverse Words in a String](https://www.leetcode.com/problems/reverse-words-in-a-string/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/reverse-words-in-a-string/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
