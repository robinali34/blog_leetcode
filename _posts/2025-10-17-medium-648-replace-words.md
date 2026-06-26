---
layout: post
title: "[Medium] 648. Replace Words"
date: 2025-10-17 16:17:34 -0700
categories: leetcode algorithm medium cpp trie hash-set string-processing problem-solving
---
In English, we have a concept called **root**, which can be followed by some other word to form another longer word. Let's call this word **successor**. For example, when the root `"an"` is followed by the successor word `"other"`, we can form a new word `"another"`.

Given a `dictionary` consisting of roots and a `sentence` consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be formed by more than one root, replace it with the root that has the **shortest length**.

Return the `sentence` after the replacement.

## Examples

**Example 1:**
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Explanation: 
- "cattle" can be replaced by "cat" (shortest root)
- "rattled" can be replaced by "rat" (shortest root)
- "battery" can be replaced by "bat" (shortest root)
```

**Example 2:**
```
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
Explanation: 
- "aadsfasf" can be replaced by "a" (shortest root)
- "absbs" can be replaced by "a" (shortest root)
- "bbab" can be replaced by "b" (shortest root)
- "cadsfafs" can be replaced by "c" (shortest root)
```

## Constraints

- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 100`
- `1 <= sentence.length <= 10^6`
- `sentence` consists of only lower-case letters and spaces.
- The number of words in `sentence` is in the range `[1, 1000]`
- The length of each word in `sentence` is in the range `[1, 1000]`
- Each word in `sentence` consists of only lower-case letters.

## Thinking Process

1. **Simple implementation:** Easy to understand and implement
1. **Efficient traversal:** Character-by-character matching

- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute force** *(this problem)* | Often $O(n^2)$ or $O(2^n)$ | $O(n)$ | Baseline; clarifies the optimization target |
| Sort + scan | $O(n \log n)$ | $O(1)$ | Pairs, intervals, greedy ordering |
| Hash map / set | $O(n)$ | $O(n)$ | Frequency, membership, two-sum style |
| Single-pass linear | $O(n)$ | $O(1)$ | Two pointers, sliding window, Kadane |

## Solution

**Time Complexity:** O(n * m) where n is number of words, m is average word length  
**Space Complexity:** O(d) where d is dictionary size

Use a hash set to store dictionary roots and check prefixes for each word.

```cpp
class Solution {
private:
    string shortestRoot(unordered_set<string> dicSet, string word) {
        for(int i = 1; i <= word.size(); i++) {
            string root = word.substr(0, i);
            if(dicSet.contains(root)) {
                return root;
            }
        }
        return word;
    }
    
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        istringstream sStream(sentence);
        unordered_set<string> dicSet(dictionary.begin(), dictionary.end());
        string word;
        string newSentence;
        
        while(getline(sStream, word, ' ')) {
            newSentence.append(shortestRoot(dicSet, word));
            newSentence.append(" ");
        }
        
        if(!newSentence.empty()) newSentence.pop_back();
        return newSentence;
    }
};
```

### Solution Explanation

**Approach:** Brute force (this problem)

**Key idea:** 1. **Simple implementation:** Easy to understand and implement

**How the code works:**
1. **Simple implementation:** Easy to understand and implement
1. **Efficient traversal:** Character-by-character matching
- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.

**Walkthrough** — input `dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"`, expected output `"the cat was rat by the bat"`:

- "cattle" can be replaced by "cat" (shortest root)
- "rattled" can be replaced by "rat" (shortest root)
- "battery" can be replaced by "bat" (shortest root)

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Hash Set | O(n * m) | O(d) |
| Trie | O(n * m) | O(d * k) |

Where:
- n = number of words in sentence
- m = average word length
- d = dictionary size
- k = average root length
## How the Algorithms Work

### Solution 1: Hash Set Approach

**Key Insight:** For each word, check all possible prefixes to find the shortest root.

**Steps:**
1. **Store dictionary** in hash set for O(1) lookup
2. **For each word**, check prefixes of increasing length
3. **Return shortest root** found, or original word if none found
4. **Build new sentence** with replaced words

### Solution 2: Trie Approach

**Key Insight:** Use trie to efficiently traverse and find shortest root prefix.

**Steps:**
1. **Build trie** from dictionary roots
2. **For each word**, traverse trie character by character
3. **Return shortest root** when reaching end node, or original word
4. **Build new sentence** with replaced words

## Step-by-Step Examples

### Solution 1 Example: `dictionary = ["cat","bat","rat"]`, `sentence = "the cattle was rattled"`

| Word | Check Prefixes | Found Root | Result |
|------|----------------|------------|--------|
| "the" | "t", "th", "the" | None | "the" |
| "cattle" | "c", "ca", "cat" | "cat" | "cat" |
| "was" | "w", "wa", "was" | None | "was" |
| "rattled" | "r", "ra", "rat" | "rat" | "rat" |

**Final result:** `"the cat was rat"`

### Solution 2 Example: `dictionary = ["cat","bat","rat"]`, `sentence = "the cattle was rattled"`

**Trie Structure:**
```
root
├── c → a → t (end)
├── b → a → t (end)
└── r → a → t (end)
```

| Word | Trie Traversal | Found Root | Result |
|------|----------------|------------|--------|
| "the" | t → h → e (not found) | None | "the" |
| "cattle" | c → a → t (end) | "cat" | "cat" |
| "was" | w (not found) | None | "was" |
| "rattled" | r → a → t (end) | "rat" | "rat" |

**Final result:** `"the cat was rat"`

## Algorithm Breakdown

### Solution 1: Hash Set

```cpp
string shortestRoot(unordered_set<string> dicSet, string word) {
    for(int i = 1; i <= word.size(); i++) {
        string root = word.substr(0, i);
        if(dicSet.contains(root)) {
            return root;
        }
    }
    return word;
}
```

**Process:**
1. **Check prefixes** of increasing length
2. **Return first match** (shortest root)
3. **Return original word** if no match found

### Solution 2: Trie

```cpp
string shortestRoot(string word) {
    TrieNode* current = root;
    for(int i = 0; i < word.size(); i++) {
        char ch = word[i];
        if(current->children[ch - 'a'] == nullptr) {
            return word;
        }
        current = current->children[ch - 'a'];
        if(current->isEnd) {
            return word.substr(0, i + 1);
        }
    }
    return word;
}
```

**Process:**
1. **Traverse trie** character by character
2. **Return prefix** when reaching end node
3. **Return original word** if path doesn't exist

### Complexity
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Hash Set | O(n * m) | O(d) |
| Trie | O(n * m) | O(d * k) |

Where:
- n = number of words in sentence
- m = average word length
- d = dictionary size
- k = average root length

## Common Mistakes

1. **Single word:** `dictionary = ["a"]`, `sentence = "a"` → `"a"`
2. **No matches:** `dictionary = ["cat"]`, `sentence = "dog"` → `"dog"`
3. **Empty dictionary:** `dictionary = []`, `sentence = "hello"` → `"hello"`
4. **Single character roots:** `dictionary = ["a","b"]`, `sentence = "abc"` → `"a"`

1. **Wrong prefix order:** Not checking shortest prefixes first
2. **Missing edge cases:** Not handling empty dictionary or sentence
3. **String building:** Inefficient string concatenation
4. **Trie implementation:** Not properly setting end markers

## Detailed Example Walkthrough

### Solution 1: `dictionary = ["a","aa","aaa"]`, `sentence = "a aa aaa"`

**Hash Set:** `{"a", "aa", "aaa"}`

| Word | Prefix Check | Found Root | Result |
|------|--------------|------------|--------|
| "a" | "a" | "a" | "a" |
| "aa" | "a" | "a" | "a" |
| "aaa" | "a" | "a" | "a" |

**Final result:** `"a a a"`

### Solution 2: `dictionary = ["a","aa","aaa"]`, `sentence = "a aa aaa"`

**Trie Structure:**
```
root
└── a (end)
    └── a (end)
        └── a (end)
```

| Word | Trie Traversal | Found Root | Result |
|------|----------------|------------|--------|
| "a" | a (end) | "a" | "a" |
| "aa" | a (end) | "a" | "a" |
| "aaa" | a (end) | "a" | "a" |

**Final result:** `"a a a"`

## Related Problems

- [208. Implement Trie (Prefix Tree)](https://www.leetcode.com/problems/implement-trie-prefix-tree/)
- [211. Design Add and Search Words Data Structure](https://www.leetcode.com/problems/design-add-and-search-words-data-structure/)
- [212. Word Search II](https://www.leetcode.com/problems/word-search-ii/)
- [720. Longest Word in Dictionary](https://www.leetcode.com/problems/longest-word-in-dictionary/)

## Why These Solutions Work

### Solution 1 (Hash Set):
1. **Correct prefix checking:** Checks all prefixes systematically
2. **Shortest first:** Returns first match (shortest root)
3. **Efficient lookup:** O(1) hash set lookup
4. **Simple logic:** Easy to understand and debug

### Solution 2 (Trie):
1. **Efficient traversal:** Character-by-character matching
2. **Early termination:** Stops at first end node
3. **Structured approach:** Organized prefix tree
4. **Scalable design:** Better for large dictionaries

## References

- [LC 648: Replace Words on LeetCode](https://www.leetcode.com/problems/replace-words/)
- [LeetCode Discuss — LC 648: Replace Words](https://www.leetcode.com/problems/replace-words/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/replace-words/editorial/) *(may require premium)*

## Key Takeaways

### Solution 1 (Hash Set):
1. **Simple implementation:** Easy to understand and implement
2. **Prefix checking:** Check all possible prefixes systematically
3. **Shortest first:** Return first match (shortest root)
4. **Space efficient:** Only stores dictionary roots

### Solution 2 (Trie):
1. **Efficient traversal:** Character-by-character matching
2. **Early termination:** Stop at first end node found
3. **Structured storage:** Organized prefix tree structure
4. **Scalable:** Better for large dictionaries
