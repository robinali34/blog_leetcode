---
layout: post
title: "616. Add Bold Tag in String"
date: 2025-12-30 17:30:00 -0700
categories: [leetcode, medium, string, array, greedy]
permalink: /2025/12/30/medium-616-add-bold-tag-in-string/
---

# 616. Add Bold Tag in String

## Problem Statement

You are given a string `s` and an array of strings `words`. You should add a closed pair of bold tag `<b>` and `</b>` to wrap the substrings in `s` that exist in `words`. If two such substrings overlap, you should wrap them together by only one pair of closed bold tag. If two consecutive substrings are wrapped, you should combine them.

Return `s` *after adding the bold tags*.

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

## Solution Approach

This problem requires identifying all substrings in `s` that match any word in `words`, and wrapping them with bold tags. The key challenge is handling **overlapping** and **consecutive** substrings by merging them into a single bold tag.

### Key Insights:

1. **Mark Bold Characters**: Use a boolean array to mark which characters should be bold
2. **Check All Matches**: For each position, check if any word matches starting there
3. **Merge Overlaps**: Overlapping matches automatically merge when we mark all characters
4. **Insert Tags**: Insert `<b>` at start of bold sequences and `</b>` at end

### Algorithm:

1. **Create mask array**: Boolean array to mark bold characters
2. **Find matches**: For each position, check all words for matches
3. **Mark characters**: Mark all characters in matched substrings
4. **Build result**: Traverse string and insert tags at boundaries

## Solution

### **Solution: Boolean Mask with String Matching**

```cpp
class Solution {
public:
    string addBoldTag(string s, vector<string>& words) {
        const int n = s.size();
        if(n == 0) return "";
        vector<bool> mask(n, false);
        for(int i = 0; i < n; i++) {
            for(string& word: words) {
                int word_len = word.size();
                if(i + word_len <= n && s.substr(i, word_len) == word) {
                    for(int j = i; j < i + word_len; j++)
                        mask[j] = true;
                }
            }
        }
        string res = "";
        for(int i = 0; i < n; i++) {
            if(mask[i] == true && (i == 0 || mask[i - 1] == false)) {
                res += "<b>";
            }
            res.push_back(s[i]);
            if(mask[i] == true && (i == n - 1 || mask[i+1] == false)) {
                res += "</b>";
            }
        }
        return res;
    }
};
```

### **Algorithm Explanation:**

1. **Edge Case (Line 5)**:
   - Return empty string if input is empty

2. **Initialize Mask (Line 6)**:
   - Create boolean array `mask` of size `n`
   - `mask[i] = true` means character at position `i` should be bold

3. **Find and Mark Matches (Lines 7-14)**:
   - For each position `i` in string `s`:
     - Check each word in `words`
     - If word matches substring starting at `i`:
       - Mark all characters from `i` to `i + word_len - 1` as bold
   - This automatically handles overlapping matches

4. **Build Result String (Lines 15-24)**:
   - Traverse string character by character
   - **Insert `<b>` tag**: When entering a bold sequence
     - Current character is bold AND
     - Either at start OR previous character is not bold
   - **Add character**: Always add current character
   - **Insert `</b>` tag**: When exiting a bold sequence
     - Current character is bold AND
     - Either at end OR next character is not bold

### **Example Walkthrough:**

**For `s = "abcxyz123", words = ["abc","123"]`:**

```
Step 1: Initialize mask
mask = [false, false, false, false, false, false, false, false, false]

Step 2: Find matches and mark
i=0: Check "abc" → matches! Mark positions 0,1,2
i=1: Check "abc" → no match
i=2: Check "abc" → no match
i=6: Check "123" → matches! Mark positions 6,7,8

mask = [true, true, true, false, false, false, true, true, true]
        a    b    c    x    y    z    1    2    3

Step 3: Build result string
i=0: mask[0]=true, i==0 → Insert "<b>", add 'a'
     Result: "<b>a"
i=1: mask[1]=true, mask[0]=true → No tag, add 'b'
     Result: "<b>ab"
i=2: mask[2]=true, mask[1]=true → No tag, add 'c'
     Result: "<b>abc"
i=3: mask[3]=false, mask[2]=true → Insert "</b>", add 'x'
     Result: "<b>abc</b>x"
i=4: mask[4]=false → No tag, add 'y'
     Result: "<b>abc</b>xy"
i=5: mask[5]=false → No tag, add 'z'
     Result: "<b>abc</b>xyz"
i=6: mask[6]=true, mask[5]=false → Insert "<b>", add '1'
     Result: "<b>abc</b>xyz<b>1"
i=7: mask[7]=true, mask[6]=true → No tag, add '2'
     Result: "<b>abc</b>xyz<b>12"
i=8: mask[8]=true, mask[7]=true, i==n-1 → Add '3', Insert "</b>"
     Result: "<b>abc</b>xyz<b>123</b>"
```

**For `s = "aaabbcc", words = ["aaa","aab","bc"]`:**

```
Step 1: Find matches
i=0: "aaa" matches → mark 0,1,2
i=0: "aab" matches → mark 0,1,2 (already marked)
i=1: "aab" matches → mark 1,2,3
i=4: "bc" matches → mark 4,5

mask = [true, true, true, true, true, true, false]
        a    a    a    b    b    c    c

Step 2: Build result
i=0: Start bold → "<b>a"
i=1: Continue → "<b>aa"
i=2: Continue → "<b>aaa"
i=3: Continue → "<b>aaab"
i=4: Continue → "<b>aaabb"
i=5: Continue → "<b>aaabbc"
i=6: End bold → "<b>aaabbc</b>c"
```

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

## Complexity Analysis

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

## Alternative Approaches

### **Approach 1: Boolean Mask (Current Solution)**
- **Time**: O(n × m × k)
- **Space**: O(n)
- **Best for**: Simple and straightforward

### **Approach 2: Interval Merging**
- **Time**: O(n × m × k) for finding, O(n log n) for merging
- **Space**: O(n)
- **Use case**: When many overlaps expected

### **Approach 3: Trie + Interval Merging**
- **Time**: O(n × k + n log n)
- **Space**: O(n + total word length)
- **Best for**: Large word dictionaries

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

## Related Problems

- [616. Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/) - Current problem
- [758. Bold Words in String](https://leetcode.com/problems/bold-words-in-string/) - Similar problem
- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) - String matching

## Tags

`String`, `Array`, `Greedy`, `Medium`

