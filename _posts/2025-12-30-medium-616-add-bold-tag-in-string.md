---
layout: post
title: "[Medium] 616. Add Bold Tag in String"
date: 2025-12-30 17:30:00 -0700
categories: [leetcode, medium, string, array, greedy]
permalink: /2025/12/30/medium-616-add-bold-tag-in-string/
---
You are given a string `s` and an array of strings `words`. You should add a closed pair of bold tag `<b>` and `</b>` to wrap the substrings in `s` that exist in `words`. If two such substrings overlap, you should wrap them together by only one pair of closed bold tag. If two consecutive substrings are wrapped, you should combine them.

Return `s` *after adding the bold tags*.

## Thinking Process

You are given a string `s` and an array of strings `words`. You should add a closed pair of bold tag `<b>` and `</b>` to wrap the substrings in `s` that exist in `words`. If two such substrings overlap, you should wrap them together by only one pair of closed bold tag. If two consecutive substrings are wrapped, you should combine them.

Return `s` *after adding the bold tags*.

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | $O(n \log n)$ | $O(1)$ | Interval scheduling, assignment |
| Local greedy choice | $O(n)$ | $O(1)$ | Jump game, gas station |
| Greedy + heap | $O(n \log n)$ | $O(n)$ | Merge streams, room allocation |
| Exchange argument | $O(n)$ | $O(1)$ | Prove greedy choice is safe |

## Examples

**Example 1:**
```
Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"
```

**Example 2:**
```
Input: s = "aaabbcc", words = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"
Explanation: The substrings "aaa" and "aab" overlap, so they are wrapped together. Then "bc" is also wrapped, so the result is "<b>aaabbc</b>c".
```

## Constraints

- `1 <= s.length <= 1000`
- `0 <= words.length <= 100`
- `1 <= words[i].length <= 1000`
- `s` and `words[i]` consist of English letters and digits.
- All the values of `words` are **unique**.

## Algorithm Breakdown

### **Key Insight: Overlapping Matches**

The algorithm handles overlapping matches automatically:
- When multiple words match at overlapping positions, all characters in the union are marked
- Example: `"aaa"` at position 0 and `"aab"` at position 1 both mark positions 1 and 2
- Result: Single continuous bold region from position 0 to 3

### **Tag Insertion Logic**

**Opening tag `<b>`:**
```cpp
if(mask[i] == true && (i == 0 || mask[i - 1] == false))
```
- Current character is bold
- AND we're at the start of a bold sequence (first char OR previous not bold)

**Closing tag `</b>`:**
```cpp
if(mask[i] == true && (i == n - 1 || mask[i+1] == false))
```
- Current character is bold
- AND we're at the end of a bold sequence (last char OR next not bold)

### **String Matching**

For each position, we check all words:
```cpp
if(i + word_len <= n && s.substr(i, word_len) == word)
```
- Bounds check: `i + word_len <= n`
- Substring comparison: `s.substr(i, word_len) == word`

### Complexity
### **Time Complexity:** O(n × m × k)
- **Outer loop**: O(n) - iterate through each position in string
- **Word loop**: O(m) - check each word in dictionary
- **Substring comparison**: O(k) - compare substring of average length k
- **Mask marking**: O(k) - mark characters (amortized)
- **Result building**: O(n) - traverse string once
- **Total**: O(n × m × k) where n = s.length(), m = words.length(), k = average word length

### **Space Complexity:** O(n)
- **Mask array**: O(n) - boolean array for each character
- **Result string**: O(n) - output string (with tags)
- **Total**: O(n)

## Key Points

1. **Boolean Mask**: Efficient way to mark which characters should be bold
2. **Automatic Merging**: Overlapping matches automatically merge into single regions
3. **Tag Boundaries**: Insert tags only at boundaries of bold sequences
4. **All Matches**: Check all words at each position to find all matches
5. **Simple Logic**: Straightforward approach that's easy to understand

## Optimization Opportunities

### **Optimization 1: Early Termination**
Skip positions that are too short for any word:
```cpp
int minLen = INT_MAX;
for(string& word: words) {
    minLen = min(minLen, (int)word.size());
}
// Skip positions where remaining string is too short
```

### **Optimization 2: Trie for Word Matching**
Use a trie to match words more efficiently:
- Build trie from words
- Match using trie traversal
- Reduces substring comparison overhead

### **Optimization 3: Interval Merging**
Instead of marking each character, use intervals:
- Find all match intervals
- Merge overlapping intervals
- Insert tags at interval boundaries

## Detailed Example Walkthrough

### **Example: `s = "aaabbcc", words = ["aaa","aab","bc"]`**

```
Step 1: Find all matches

Position 0:
  - Check "aaa": s.substr(0,3) = "aaa" ✓ → Mark [0,1,2]
  - Check "aab": s.substr(0,3) = "aaa" ✗
  - Check "bc": s.substr(0,2) = "aa" ✗

Position 1:
  - Check "aaa": s.substr(1,3) = "aab" ✗
  - Check "aab": s.substr(1,3) = "aab" ✓ → Mark [1,2,3]
  - Check "bc": s.substr(1,2) = "ab" ✗

Position 2:
  - Check "aaa": s.substr(2,3) = "abb" ✗
  - Check "aab": s.substr(2,3) = "abb" ✗
  - Check "bc": s.substr(2,2) = "bb" ✗

Position 3:
  - Check "aaa": s.substr(3,3) = "bbc" ✗
  - Check "aab": s.substr(3,3) = "bbc" ✗
  - Check "bc": s.substr(3,2) = "bb" ✗

Position 4:
  - Check "aaa": s.substr(4,3) = "bcc" ✗
  - Check "aab": s.substr(4,3) = "bcc" ✗
  - Check "bc": s.substr(4,2) = "bc" ✓ → Mark [4,5]

Position 5:
  - Check "aaa": s.substr(5,3) = "cc" ✗ (too short)
  - Check "aab": s.substr(5,3) = "cc" ✗ (too short)
  - Check "bc": s.substr(5,2) = "cc" ✗

Final mask: [true, true, true, true, true, true, false]
             a    a    a    b    b    c    c

Step 2: Build result with tags
Result: "<b>aaabbc</b>c"
```

## Edge Cases

1. **Empty string**: Return empty string
2. **No matches**: Return original string without tags
3. **All characters match**: Entire string wrapped in one tag
4. **Overlapping matches**: Merged into single region
5. **Consecutive matches**: Merged into single region

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [616. Add Bold Tag in String](https://www.leetcode.com/problems/add-bold-tag-in-string/) - Current problem
- [758. Bold Words in String](https://www.leetcode.com/problems/bold-words-in-string/) - Similar problem
- [28. Find the Index of the First Occurrence in a String](https://www.leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) - String matching

## Tags

`String`, `Array`, `Greedy`, `Medium`

## Key Takeaways

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

## References

- [LC 616: Add Bold Tag in String on LeetCode](https://www.leetcode.com/problems/add-bold-tag-in-string/)
- [LeetCode Discuss — LC 616: Add Bold Tag in String](https://www.leetcode.com/problems/add-bold-tag-in-string/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/add-bold-tag-in-string/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
