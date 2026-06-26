---
layout: post
title: "[Medium] 208. Implement Trie (Prefix Tree)"
date: 2026-01-18 00:00:00 -0700
categories: [leetcode, medium, string, design, trie]
permalink: /2026/01/18/medium-208-implement-trie/
tags: [leetcode, medium, string, design, trie, prefix-tree, data-structure]
---
A [trie](https://en.wikipedia.org/wiki/Trie) (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

## Examples

**Example 1:**
```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10^4` calls **in total** will be made to `insert`, `search`, and `startsWith`.

## Thinking Process

1. **Self-Referential Design**: Each `Trie` object is itself a node, making the structure simpler

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Design pattern</text>

  <rect x="40" y="45" width="70" height="36" rx="4" fill="#D4D8E0" stroke="#8B8680"/><text x="75" y="67" text-anchor="middle" font-size="10">API</text>
  <rect x="150" y="45" width="90" height="36" rx="4" fill="#E0D8E4" stroke="#A098A8"/><text x="195" y="67" text-anchor="middle" font-size="10">hash + list</text>
  <path d="M110 63h36" stroke="#8B8680" stroke-width="2" marker-end="url(#arr2)"/>
  <defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>
  <text x="140" y="105" text-anchor="middle" font-size="11" fill="#6B6560">compose data structures for operations</text>

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

```cpp
class Trie {
public:
    Trie() : children(26), isWord(false) {
        
    }
    
    void insert(string word) {
        Trie* node = this;
        for(char ch: word) {
            ch -= 'a';
            if(!node->children[ch]) {
                node->children[ch] = new Trie();
            }
            node = node->children[ch];
        }
        node->isWord = true;
    }
    
    bool search(string word) {
        Trie* node = this->searchPrefix(word);
        return node != nullptr && node->isWord;
    }
    
    bool startsWith(string prefix) {
        return this->searchPrefix(prefix) != nullptr;
    }

private:
    vector<Trie*> children;
    bool isWord;

    Trie* searchPrefix(string prefix) {
        Trie* node = this;
        for(char ch: prefix) {
            ch -= 'a';
            if(!node->children[ch]) {
                return nullptr;
            }
            node = node->children[ch];
        }
        return node;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** 1. **Self-Referential Design**: Each `Trie` object is itself a node, making the structure simpler

**How the code works:**
1. **Self-Referential Design**: Each `Trie` object is itself a node, making the structure simpler
- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.
## Common Mistakes

1. **Empty string**: Should be handled (mark root as end if needed)
2. **Single character**: Works normally
3. **Duplicate insert**: Same word inserted twice (safe, just re-marks end)
4. **Prefix of existing word**: `insert("apple")`, then `insert("app")` works
5. **Word extends prefix**: `insert("app")`, then `insert("apple")` works
6. **Non-existent search**: Returns `false` correctly
7. **Non-existent prefix**: `startsWith` returns `false` correctly

1. **Forgetting `isWord` check**: `search` returns true for prefixes if not checking `isWord`
2. **Not checking `isWord` in search**: `search("app")` returns true when only "apple" exists
3. **Character indexing error**: Forgetting `ch -= 'a'` before accessing `children[ch]`
4. **Index out of bounds**: Not validating character is lowercase (0-25 range)
5. **Null pointer access**: Not checking `if(!node->children[ch])` before accessing
6. **Incorrect traversal**: Not updating `node = node->children[ch]` in loop
7. **Case sensitivity**: Assuming only lowercase (problem constraint)
8. **Using `this` incorrectly**: Forgetting that root is `this` itself, not a separate pointer

## When to Use Trie

1. **Autocomplete**: Fast prefix matching
2. **Spell Checker**: Dictionary lookup
3. **IP Routing**: Longest prefix matching
4. **Search Engines**: Prefix-based search
5. **Phone Directory**: Name/contact lookup
6. **Word Games**: Valid word checking

## Related Problems

- [LC 211: Design Add and Search Words Data Structure](https://www.leetcode.com/problems/design-add-and-search-words-data-structure/) - Trie with wildcard search
- [LC 212: Word Search II](https://www.leetcode.com/problems/word-search-ii/) - Trie + DFS on board
- [LC 642: Design Search Autocomplete System](https://www.leetcode.com/problems/design-search-autocomplete-system/) - Trie with frequency tracking
- [LC 648: Replace Words](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-648-replace-words/) - Trie for prefix replacement
- [LC 677: Map Sum Pairs](https://www.leetcode.com/problems/map-sum-pairs/) - Trie with value storage
- [LC 720: Longest Word in Dictionary](https://www.leetcode.com/problems/longest-word-in-dictionary/) - Trie traversal

---

*This problem is a fundamental **data structure implementation** that demonstrates the Trie (Prefix Tree) structure. It's essential for understanding prefix-based string operations and is widely used in autocomplete systems and search engines.*

## Key Takeaways

1. **Self-Referential Design**: Each `Trie` object is itself a node, making the structure simpler
2. **Trie Structure**: Tree where each path represents a prefix/word
3. **End Marker (`isWord`)**: Critical to distinguish between prefix and complete word
4. **Shared Prefixes**: Multiple words sharing prefixes share nodes (space efficient)
5. **Array vs Map**: `vector<Trie*>` (26 elements) is faster and uses less memory than `unordered_map`
6. **Character Indexing**: `ch -= 'a'` converts character to 0-25 index efficiently
7. **Helper Method**: `searchPrefix` reduces code duplication between `search` and `startsWith`
8. **Root as `this`**: The Trie object itself serves as the root, eliminating need for separate root pointer

## References

- [LC 208: Implement Trie (Prefix Tree) on LeetCode](https://www.leetcode.com/problems/implement-trie/)
- [LeetCode Discuss — LC 208: Implement Trie (Prefix Tree)](https://www.leetcode.com/problems/implement-trie/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/implement-trie/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
