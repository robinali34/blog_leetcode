---
layout: post
title: "2185. Counting Words With a Given Prefix"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, string, array]
permalink: /2026/01/19/easy-2185-counting-words-with-a-given-prefix/
tags: [leetcode, easy, string, array, prefix, simulation]
---

# 2185. Counting Words With a Given Prefix

## Problem Statement

You are given an array of strings `words` and a string `pref`.

Return the **number** of strings in `words` that contain `pref` as a **prefix**.

A **prefix** of a string `s` is any leading contiguous substring of `s`.

## Examples

**Example 1:**
```
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
```

**Example 2:**
```
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
```

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length, pref.length <= 100`
- `words[i]` and `pref` consist of lowercase English letters.

## Solution Approach

This is a straightforward **simulation** problem. We need to:
1. Iterate through each word in the array
2. Check if the word starts with the given prefix
3. Count how many words match

### Key Insights:

1. **Prefix Check**: A word has a prefix if its first `pref.length()` characters match `pref`
2. **Length Validation**: A word must be at least as long as the prefix
3. **Simple Comparison**: Use substring comparison or character-by-character check

### Algorithm:

1. Initialize counter to 0
2. For each word:
   - Check if word length >= prefix length
   - Compare first `pref.length()` characters with `pref`
   - If match, increment counter
3. Return counter

## Solution

```cpp
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int cnt = 0;
        const int prel = pref.length();
        for(auto& word: words) {
            if(word.substr(0, prel) == pref) {
                cnt++;
            }
        }
        return cnt;
    }
};
```

### Algorithm Explanation:

1. **Initialize Counter**: `cnt = 0` to track matching words
2. **Store Prefix Length**: `prel = pref.length()` for efficiency
3. **Iterate Through Words**:
   - For each word, extract substring from index 0 to `prel`
   - Compare with `pref`
   - If equal, increment counter
4. **Return Result**: Total count of words with the prefix

### Example Walkthrough:

**Input:** `words = ["pay","attention","practice","attend"]`, `pref = "at"`

```
Word: "pay"
  word.substr(0, 2) = "pa" ≠ "at" → skip

Word: "attention"
  word.substr(0, 2) = "at" == "at" → cnt = 1 ✓

Word: "practice"
  word.substr(0, 2) = "pr" ≠ "at" → skip

Word: "attend"
  word.substr(0, 2) = "at" == "at" → cnt = 2 ✓

Return: 2
```

### Complexity Analysis:

- **Time Complexity:** O(n × m)
  - `n` = number of words
  - `m` = length of prefix
  - For each word, we create a substring of length `m` and compare (O(m) operation)
  - Total: O(n × m)

- **Space Complexity:** O(1)
  - Only using a counter variable
  - Note: `substr()` creates a temporary string, but this is typically optimized by the compiler

## Key Insights

1. **Simple Prefix Matching**: Use substring comparison for clarity
2. **Length Safety**: `substr(0, prel)` automatically handles cases where word is shorter than prefix (returns shorter substring)
3. **Efficient**: Linear time complexity, suitable for given constraints
4. **Readable**: Clear and straightforward implementation

## Edge Cases

1. **Word shorter than prefix**: `substr(0, prel)` returns a shorter string, comparison fails correctly
2. **Empty prefix**: If `pref = ""`, all words match (but constraints guarantee `pref.length >= 1`)
3. **Prefix equals word**: Word still counts (e.g., `pref = "at"`, `word = "at"` → match)
4. **No matches**: Returns 0 correctly
5. **All words match**: Returns `words.length`
6. **Single character prefix**: Works correctly with `pref = "a"`

## Common Mistakes

1. **Out-of-bounds access**: Not checking word length before accessing characters
2. **Off-by-one errors**: Incorrect substring indices
3. **Case sensitivity**: Problem states lowercase only, but worth noting
4. **Forgetting to increment counter**: Missing the increment statement
5. **Using wrong comparison**: Comparing entire word instead of prefix

## Alternative Approaches

### Character-by-Character Comparison

```cpp
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int cnt = 0;
        int prel = pref.length();
        for(auto& word: words) {
            if(word.length() < prel) continue;
            bool match = true;
            for(int i = 0; i < prel; i++) {
                if(word[i] != pref[i]) {
                    match = false;
                    break;
                }
            }
            if(match) cnt++;
        }
        return cnt;
    }
};
```

**Pros**: More explicit, avoids substring creation  
**Cons**: Slightly more verbose

### Using `find()` Method

```cpp
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int cnt = 0;
        for(auto& word: words) {
            if(word.find(pref) == 0) {
                cnt++;
            }
        }
        return cnt;
    }
};
```

**Pros**: Very concise  
**Cons**: `find()` searches entire string, less efficient for prefix-only check

### Using `starts_with()` (C++20)

```cpp
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int cnt = 0;
        for(auto& word: words) {
            if(word.starts_with(pref)) {
                cnt++;
            }
        }
        return cnt;
    }
};
```

**Pros**: Most semantic, clearly expresses intent  
**Cons**: Requires C++20

## When to Use This Pattern

1. **Prefix Matching**: Checking if strings start with specific patterns
2. **Filtering**: Selecting items from a collection based on prefix
3. **Autocomplete**: Finding words that start with user input
4. **String Processing**: Text analysis and pattern matching
5. **Data Validation**: Checking format or structure of strings

## Related Problems

- [LC 208: Implement Trie (Prefix Tree)](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-208-implement-trie/) - More efficient for multiple prefix queries
- [LC 211: Design Add and Search Words Data Structure](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-211-design-add-and-search-words-data-structure/) - Trie with wildcard support
- [LC 648: Replace Words](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-648-replace-words/) - Prefix matching with replacement
- [LC 14: Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) - Finding common prefix
- [LC 720: Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) - Prefix-based word selection

---

*This problem demonstrates **simple prefix matching** using substring comparison. For multiple queries, consider using a **Trie data structure** for better efficiency.*

