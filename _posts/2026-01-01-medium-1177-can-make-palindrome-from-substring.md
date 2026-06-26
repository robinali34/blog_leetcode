---
layout: post
title: "[Medium] 1177. Can Make Palindrome from Substring"
date: 2026-01-01 01:00:00 -0700
categories: [leetcode, medium, string, bit-manipulation, prefix-sum, hash-table]
permalink: /2026/01/01/medium-1177-can-make-palindrome-from-substring/
---
You are given a string `s` and array `queries` where `queries[i] = [left, right, k]`. We may **rearrange** the substring `s[left...right]` and then choose **up to `k`** of its characters to replace with any lowercase English letter.

If the substring can be made a **palindrome** after the operations above, the result of the query is `true`. Otherwise, the result is `false`.

Return an array `answer`, where `answer[i]` is the result of the `i`-th query `queries[i]`.

Note that: Each letter is counted **individually** for replacement, so if, for example `s[left...right] = "aaa"`, and `k = 2`, we can only replace 2 of the letters. Also, note that the initial string `s` is never modified.

## Thinking Process

You are given a string `s` and array `queries` where `queries[i] = [left, right, k]`. We may **rearrange** the substring `s[left...right]` and then choose **up to `k`** of its characters to replace with any lowercase English letter.

If the substring can be made a **palindrome** after the operations above, the result of the query is `true`. Otherwise, the result is `false`.

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 90" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Bit manipulation</text>

  <text x="40" y="50" font-family="monospace" font-size="14" fill="#3A3530">1 0 1 1 0 1 0</text>
  <text x="40" y="75" font-size="11" fill="#6B6560">XOR pairs · masks · shifts</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | $O(n)$ | $O(1)$ | Palindrome, parsing |
| Hash map / frequency | $O(n)$ | $O(k)$ | Anagram, character counts |
| KMP / rolling hash | $O(n)$ | $O(n)$ | Pattern matching |
| Stack parsing | $O(n)$ | $O(n)$ | Decode string, parentheses |

## Examples

**Example 1:**
```
Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]

Explanation:
- queries[0]: substring = "d", could be changed to "d" which is palindrome. true
- queries[1]: substring = "bc", could not get palindrome by rearranging without replacement. false
- queries[2]: substring = "abcd", could not get palindrome by rearranging and replacing 1 character. false
- queries[3]: substring = "abcd", could get palindrome by rearranging to "abba" and replacing 2 characters. true
- queries[4]: substring = "abcda", could get palindrome by rearranging to "aacda" and replacing 1 character. true
```

**Example 2:**
```
Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
Output: [false,true]
```

## Constraints

- `1 <= s.length, queries.length <= 10^5`
- `0 <= left <= right < s.length`
- `0 <= k <= s.length`
- `s` consists of lowercase English letters.

## Algorithm Breakdown

### **Why XOR Works for Parity**

XOR has the property that:
- `x ^ x = 0` (even occurrences cancel out)
- `x ^ 0 = x` (odd occurrence remains)

So when we XOR all characters in a range:
- Characters with even frequency → bit becomes 0
- Characters with odd frequency → bit becomes 1

### **Prefix XOR Pattern**

Similar to prefix sums, prefix XOR allows O(1) range queries:
- `count[i]` = XOR of characters from 0 to i-1
- `count[right + 1] ^ count[left]` = XOR of characters in range [left, right]

### **Palindrome Check Formula**

For a substring to be a palindrome:
- **At most 1 character** can have odd frequency (the center)
- With `k` replacements, we can fix `2k` odd frequencies
- Plus 1 for the center: `odd_count <= 2k + 1`

**Why `2k`?**
- Each replacement changes 2 characters' frequencies
- Replacing 'a' with 'b' decreases 'a' frequency by 1 and increases 'b' frequency by 1
- Net effect: fixes 2 odd frequencies (if both were odd) or creates 2 even frequencies

### **Brian Kernighan's Algorithm**

Counting set bits efficiently:
```cpp
int bits = 0;
while(x > 0) {
    x &= x - 1;  // Clear rightmost set bit
    bits++;
}
```

Time: O(number of set bits) instead of O(32)

## Time & Space Complexity

- **Time Complexity**:
  - **Initialization**: O(n) - build prefix XOR array
  - **Each Query**: O(1) amortized - count bits (at most 26 set bits)
  - **Total**: O(n + q) where q is number of queries
- **Space Complexity**: O(n) - store prefix XOR array

## Key Points

1. **Bit Manipulation**: Use XOR to track character parity efficiently
2. **Prefix XOR**: Similar to prefix sums, enables O(1) range queries
3. **Palindrome Property**: At most 1 odd frequency allowed
4. **Replacement Formula**: `k` replacements can fix `2k` odd frequencies
5. **Efficient**: O(1) per query after O(n) preprocessing

## Edge Cases

1. **Single character**: Always palindrome, `bits = 1 <= 2k + 1`
2. **All even frequencies**: `bits = 0 <= 2k + 1` (always true)
3. **All odd frequencies**: Need `(n - 1) / 2` replacements
4. **k = 0**: Only works if substring is already palindrome
5. **Empty substring**: Not possible per constraints

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [266. Palindrome Permutation](https://www.leetcode.com/problems/palindrome-permutation/) - Check if string can be palindrome
- [409. Longest Palindrome](https://www.leetcode.com/problems/longest-palindrome/) - Build longest palindrome
- [680. Valid Palindrome II](https://www.leetcode.com/problems/valid-palindrome-ii/) - Can make palindrome with 1 deletion
- [125. Valid Palindrome](https://www.leetcode.com/problems/valid-palindrome/) - Check if palindrome

## Tags

`String`, `Bit Manipulation`, `Prefix Sum`, `Hash Table`, `Medium`

## Key Takeaways

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

## References

- [LC 1177: Can Make Palindrome from Substring on LeetCode](https://www.leetcode.com/problems/can-make-palindrome-from-substring/)
- [LeetCode Discuss — LC 1177: Can Make Palindrome from Substring](https://www.leetcode.com/problems/can-make-palindrome-from-substring/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/can-make-palindrome-from-substring/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
