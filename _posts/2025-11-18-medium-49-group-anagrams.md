---
layout: post
title: "[Medium] 49. Group Anagrams"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp string hash-table problem-solving
permalink: /posts/2025-11-18-medium-49-group-anagrams/
tags: [leetcode, medium, string, hash-table, anagram, counting]
---

# [Medium] 49. Group Anagrams

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Anagram definition**: What is an anagram? (Assumption: Words with same characters in different order - same character frequencies)

2. **Grouping rule**: How should we group anagrams? (Assumption: Group strings that are anagrams of each other together)

3. **Return format**: What should we return? (Assumption: List of groups - each group contains anagrams)

4. **Order requirement**: Does order of groups matter? (Assumption: No - can return in any order)

5. **Single character**: Do single characters count as anagrams? (Assumption: Yes - "a" is anagram of "a")

## Solution: Character Count Key Approach

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

## How the Algorithm Works

### Step-by-Step Example: `strs = ["eat","tea","tan","ate","nat","bat"]`

```
Step 1: Process "eat"
  Count: [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
  Key: "#1#0#0#0#1#0#0#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#0"
  hm[key] = ["eat"]

Step 2: Process "tea"
  Count: [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
  Key: "#1#0#0#0#1#0#0#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#0" (same as "eat")
  hm[key] = ["eat", "tea"]

Step 3: Process "tan"
  Count: [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]
  Key: "#1#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#1#0#0#0#0#0#0"
  hm[key] = ["tan"]

Step 4: Process "ate"
  Count: [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
  Key: "#1#0#0#0#1#0#0#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#0" (same as "eat")
  hm[key] = ["eat", "tea", "ate"]

Step 5: Process "nat"
  Count: [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]
  Key: "#1#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#1#0#0#0#0#0#0" (same as "tan")
  hm[key] = ["tan", "nat"]

Step 6: Process "bat"
  Count: [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
  Key: "#1#1#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#0#1#0#0#0#0#0#0"
  hm[key] = ["bat"]

Result:
  [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

### Visual Representation

```
Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
         ↓       ↓       ↓       ↓       ↓       ↓
Keys:   key1   key1   key2   key1   key2   key3
         ↓       ↓       ↓       ↓       ↓       ↓
Groups: ["eat","tea","ate"]  ["tan","nat"]  ["bat"]
```

## Key Insights

1. **Character Frequency as Key**: Use character count array to create a unique key for each anagram group
2. **Hash Map Grouping**: Strings with identical character frequencies map to the same key
3. **Delimiter Usage**: Using "#" delimiter ensures keys are unique (e.g., "1#2" vs "12#")
4. **Efficient Counting**: Count array of size 26 (for lowercase letters) is space-efficient

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

## Edge Cases

1. **Empty input**: `strs = []` → return `[]`
2. **Single empty string**: `strs = [""]` → return `[[""]]`
3. **Single character**: `strs = ["a"]` → return `[["a"]]`
4. **All anagrams**: `strs = ["eat","tea","ate"]` → return `[["eat","tea","ate"]]`
5. **No anagrams**: `strs = ["abc","def","ghi"]` → return `[["abc"],["def"],["ghi"]]`

## Alternative Approaches

### Approach 2: Sorted String Key

**Time Complexity:** O(N * K log K) where K is the average string length  
**Space Complexity:** O(N * K)

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hm;
        
        for(string& s: strs) {
            string key = s;
            sort(key.begin(), key.end());
            hm[key].push_back(s);
        }
        
        vector<vector<string>> rtn;
        for(auto& [key, group] : hm) {
            rtn.push_back(group);
        }
        
        return rtn;
    }
};
```

**Pros:**
- Simpler implementation
- Easier to understand

**Cons:**
- Slower due to sorting: O(K log K) per string
- Less efficient for long strings

### Approach 3: Prime Number Hash (Advanced)

**Time Complexity:** O(N * K)  
**Space Complexity:** O(N * K)

Uses prime numbers to create hash keys, avoiding string concatenation overhead.

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Prime numbers for each letter
        int primes[26] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};
        
        unordered_map<long long, vector<string>> hm;
        
        for(string& s: strs) {
            long long key = 1;
            for(char c: s) {
                key *= primes[c - 'a'];
            }
            hm[key].push_back(s);
        }
        
        vector<vector<string>> rtn;
        for(auto& [key, group] : hm) {
            rtn.push_back(group);
        }
        
        return rtn;
    }
};
```

**Pros:**
- Fast key generation (multiplication)
- No string concatenation overhead

**Cons:**
- Risk of integer overflow for very long strings
- More complex to implement

## Complexity Analysis

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

- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) - Check if two strings are anagrams
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) - Find anagram substrings
- [2273. Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) - Remove anagrams from array
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) - This problem

## Real-World Applications

1. **Word Games**: Grouping words by anagram patterns (Scrabble, Boggle)
2. **Text Analysis**: Finding similar words or patterns in text
3. **Cryptography**: Anagram-based ciphers and puzzles
4. **Search Engines**: Grouping similar search terms
5. **Data Deduplication**: Identifying similar strings

---

*This problem demonstrates the power of using character frequency as a hash key, showing how counting can be more efficient than sorting for certain string problems.*

