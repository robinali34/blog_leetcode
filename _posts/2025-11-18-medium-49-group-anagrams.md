---
layout: post
title: "[Medium] 49. Group Anagrams"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp string hash-table problem-solving
permalink: /posts/2025-11-18-medium-49-group-anagrams/
tags: [leetcode, medium, string, hash-table, anagram, counting]
---
Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Thinking Process

1. **Character Frequency as Key**: Use character count array to create a unique key for each anagram group

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.



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
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Solution

**Time Complexity:** O(N * K) where N is the number of strings and K is the maximum length of a string  
**Space Complexity:** O(N * K) for storing all strings in the hash map

The key insight is to use a character frequency count as the hash map key. Strings with the same character frequencies are anagrams of each other.

### Solution: Character Count Key

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        if(strs.size() == 0) return vector<vector<string>>();
        
        unordered_map<string, vector<string>> hm;
        int count[26];
        
        for(string& s: strs) {
            fill(begin(count), end(count), 0);
            
            for(char c: s) count[c-'a']++;
            
            string key = "";
            for(int i = 0; i < 26; i++) {
                key += "#";
                key += to_string(count[i]);
            }
            
            if(!hm.contains(key)) hm[key] = vector<string>();
            hm[key].push_back(s);
        }
        
        vector<vector<string>> rtn;
        for(auto itr = hm.begin(); itr != hm.end(); itr++) {
            rtn.push_back(itr->second);
        }
        
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** 1. **Character Frequency as Key**: Use character count array to create a unique key for each anagram group

**How the code works:**
1. **Character Frequency as Key**: Use character count array to create a unique key for each anagram group
- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

**Walkthrough** — input `strs = ["eat","tea","tan","ate","nat","bat"]`, expected output `[["bat"],["nat","tan"],["ate","eat","tea"]]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Character Count Key** | O(N * K) | O(N * K) | Fast, no sorting | String concatenation overhead |
| **Sorted String Key** | O(N * K log K) | O(N * K) | Simple, readable | Slower due to sorting |
| **Prime Number Hash** | O(N * K) | O(N * K) | Very fast key generation | Overflow risk, complex |
## Algorithm Breakdown

```cpp
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // Handle empty input
    if(strs.size() == 0) return vector<vector<string>>();
    
    // Map: character count key -> list of anagrams
    unordered_map<string, vector<string>> hm;
    int count[26];  // Count array for 26 lowercase letters
    
    for(string& s: strs) {
        // Reset count array
        fill(begin(count), end(count), 0);
        
        // Count characters in current string
        for(char c: s) count[c-'a']++;
        
        // Build key from character counts
        string key = "";
        for(int i = 0; i < 26; i++) {
            key += "#";           // Delimiter
            key += to_string(count[i]);  // Count for each letter
        }
        
        // Add string to appropriate group
        if(!hm.contains(key)) hm[key] = vector<string>();
        hm[key].push_back(s);
    }
    
    // Convert map values to result vector
    vector<vector<string>> rtn;
    for(auto itr = hm.begin(); itr != hm.end(); itr++) {
        rtn.push_back(itr->second);
    }
    
    return rtn;
}
```

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Character Count Key** | O(N * K) | O(N * K) | Fast, no sorting | String concatenation overhead |
| **Sorted String Key** | O(N * K log K) | O(N * K) | Simple, readable | Slower due to sorting |
| **Prime Number Hash** | O(N * K) | O(N * K) | Very fast key generation | Overflow risk, complex |

### Why Character Count Key is Preferred

1. **Optimal Time Complexity**: O(N * K) without sorting overhead
2. **Predictable Performance**: No dependency on string length for key generation
3. **Memory Efficient**: Fixed-size count array (26 integers)
4. **Robust**: Works for any string length without overflow concerns

## Implementation Details

### Character Count Array

```cpp
int count[26];  // For 26 lowercase letters a-z
fill(begin(count), end(count), 0);  // Reset to zero

// Count characters
for(char c: s) count[c-'a']++;  // 'a' maps to index 0, 'z' to 25
```

### Key Construction

```cpp
string key = "";
for(int i = 0; i < 26; i++) {
    key += "#";              // Delimiter prevents ambiguity
    key += to_string(count[i]);  // Count for letter at position i
}
```

**Why use "#" delimiter?**
- Without delimiter: "12" could mean count[0]=1, count[1]=2 OR count[0]=12
- With delimiter: "#1#2" unambiguously means count[0]=1, count[1]=2

### C++20 contains() Method

```cpp
if(!hm.contains(key)) hm[key] = vector<string>();
```

Alternative (C++11/14):
```cpp
if(hm.find(key) == hm.end()) hm[key] = vector<string>();
```

## Common Mistakes

1. **Empty input**: `strs = []` → return `[]`
2. **Single empty string**: `strs = [""]` → return `[[""]]`
3. **Single character**: `strs = ["a"]` → return `[["a"]]`
4. **All anagrams**: `strs = ["eat","tea","ate"]` → return `[["eat","tea","ate"]]`
5. **No anagrams**: `strs = ["abc","def","ghi"]` → return `[["abc"],["def"],["ghi"]]`

1. **Forgetting to reset count array**: Must reset for each string
2. **Wrong delimiter**: Using numbers without delimiter causes key collisions
3. **Case sensitivity**: Assuming uppercase letters (this problem uses lowercase only)
4. **Empty string handling**: Not handling empty input or empty strings correctly
5. **Inefficient key generation**: Using sorting when counting is faster

## Optimization Tips

1. **Pre-allocate result vector**: Can reserve space if you know approximate number of groups
2. **Use emplace_back**: More efficient than push_back for strings
3. **Avoid string concatenation**: Character count approach minimizes this overhead
4. **Early return**: Handle empty input immediately

## Related Problems

- [242. Valid Anagram](https://www.leetcode.com/problems/valid-anagram/) - Check if two strings are anagrams
- [438. Find All Anagrams in a String](https://www.leetcode.com/problems/find-all-anagrams-in-a-string/) - Find anagram substrings
- [2273. Find Resultant Array After Removing Anagrams](https://www.leetcode.com/problems/find-resultant-array-after-removing-anagrams/) - Remove anagrams from array
- [49. Group Anagrams](https://www.leetcode.com/problems/group-anagrams/) - This problem

## Real-World Applications

1. **Word Games**: Grouping words by anagram patterns (Scrabble, Boggle)
2. **Text Analysis**: Finding similar words or patterns in text
3. **Cryptography**: Anagram-based ciphers and puzzles
4. **Search Engines**: Grouping similar search terms
5. **Data Deduplication**: Identifying similar strings

## Key Takeaways

1. **Character Frequency as Key**: Use character count array to create a unique key for each anagram group
2. **Hash Map Grouping**: Strings with identical character frequencies map to the same key
3. **Delimiter Usage**: Using "#" delimiter ensures keys are unique (e.g., "1#2" vs "12#")
4. **Efficient Counting**: Count array of size 26 (for lowercase letters) is space-efficient

## References

- [LC 49: Group Anagrams on LeetCode](https://www.leetcode.com/problems/group-anagrams/)
- [LeetCode Discuss — LC 49: Group Anagrams](https://www.leetcode.com/problems/group-anagrams/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/group-anagrams/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
