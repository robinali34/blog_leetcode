---
layout: post
title: "208. Implement Trie (Prefix Tree)"
date: 2026-01-18 00:00:00 -0700
categories: [leetcode, medium, string, design, trie]
permalink: /2026/01/18/medium-208-implement-trie/
tags: [leetcode, medium, string, design, trie, prefix-tree, data-structure]
---

# 208. Implement Trie (Prefix Tree)

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Character set**: What characters can appear in words? (Assumption: Only lowercase English letters 'a'-'z' - 26 characters)

2. **Empty string**: How should we handle empty strings for `search` and `startsWith`? (Assumption: Based on constraints, length is at least 1, but we should clarify if empty string is considered a valid word)

3. **Duplicate insertion**: What happens if we insert the same word multiple times? (Assumption: The word should still be searchable - we can mark it as a word each time or just once)

4. **Prefix vs exact match**: For `startsWith`, should it return true for the exact word itself? (Assumption: Yes - a word is considered to start with itself)

5. **Memory constraints**: Are there any space complexity requirements? (Assumption: O(ALPHABET_SIZE * N * M) where N is number of words and M is average length)

## Solution Approach

A **Trie (Prefix Tree)** is a tree-like data structure where each node represents a character. The path from root to any node represents a prefix, and nodes can be marked to indicate the end of a word.

### Key Components:

1. **TrieNode**: Each node has:
   - 26 children pointers (one for each lowercase letter)
   - A boolean flag `isEnd` to mark end of word

2. **Operations**:
   - **Insert**: Traverse/create path for each character, mark end node
   - **Search**: Traverse path, check if exists and is marked as end
   - **StartsWith**: Traverse path, check if path exists (regardless of end flag)

3. **Memory Management**: Proper destructor to clean up allocated nodes

### Algorithm:

1. **Insert**: For each character, create node if missing, traverse, mark end
2. **Search**: Traverse path, return true only if path exists AND end is marked
3. **StartsWith**: Traverse path, return true if path exists (end flag not required)

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

### Algorithm Explanation:

#### **Trie Class Structure:**

This implementation uses a **self-referential design** where each `Trie` object represents a node in the trie. The root is the `Trie` object itself (`this`).

1. **Data Members**:
   - `vector<Trie*> children`: Array of 26 pointers (one for each lowercase letter)
   - `bool isWord`: Flag marking if this node represents the end of a word

2. **Constructor**: 
   - Initializes `children` vector with 26 `nullptr` elements
   - Sets `isWord` to `false`

3. **insert(word)**:
   - Start from `this` (root node)
   - For each character in word:
     - Convert to index: `ch -= 'a'`
     - Create new `Trie` node if child doesn't exist
     - Move to child node
   - Mark final node's `isWord` as `true`

4. **search(word)**:
   - Use `searchPrefix` helper to find the node
   - Return `true` only if node exists AND `isWord` is `true`

5. **startsWith(prefix)**:
   - Use `searchPrefix` helper to find the node
   - Return `true` if node exists (regardless of `isWord` flag)

6. **searchPrefix(prefix)** (Private Helper):
   - Start from `this` (root)
   - Traverse following each character in prefix
   - Return `nullptr` if path doesn't exist
   - Return the final node if path exists

### Example Walkthrough:

**Operations:** `insert("apple")`, `search("app")`, `startsWith("app")`, `insert("app")`, `search("app")`

```
Step 1: insert("apple")
  this (root) -> children['a'] -> children['p'] -> children['p'] -> children['l'] -> children['e']
  Final node: isWord = true
  
Step 2: search("app")
  searchPrefix("app"): Traverse this -> 'a' -> 'p' -> 'p'
  Node exists but isWord = false
  Return: false ✓

Step 3: startsWith("app")
  searchPrefix("app"): Traverse this -> 'a' -> 'p' -> 'p'
  Node exists (regardless of isWord flag)
  Return: true ✓

Step 4: insert("app")
  Traverse existing path: this -> 'a' -> 'p' -> 'p'
  Set isWord = true on the 'p' node
  
Step 5: search("app")
  searchPrefix("app"): Traverse this -> 'a' -> 'p' -> 'p'
  Node exists AND isWord = true
  Return: true ✓
```

### Complexity Analysis:

- **Time Complexity:**
  - `insert(word)`: O(m) where m = word length
  - `search(word)`: O(m) where m = word length
  - `startsWith(prefix)`: O(p) where p = prefix length
  - All operations are linear in the length of the input string

- **Space Complexity:**
  - **Worst Case**: O(ALPHABET_SIZE × N × M)
    - ALPHABET_SIZE = 26 (lowercase letters)
    - N = number of words
    - M = average word length
  - **Best Case** (shared prefixes): O(ALPHABET_SIZE × M × N)
    - Prefixes are shared, reducing space
  - In practice, space depends on how many unique prefixes exist

## Key Insights

1. **Self-Referential Design**: Each `Trie` object is itself a node, making the structure simpler
2. **Trie Structure**: Tree where each path represents a prefix/word
3. **End Marker (`isWord`)**: Critical to distinguish between prefix and complete word
4. **Shared Prefixes**: Multiple words sharing prefixes share nodes (space efficient)
5. **Array vs Map**: `vector<Trie*>` (26 elements) is faster and uses less memory than `unordered_map`
6. **Character Indexing**: `ch -= 'a'` converts character to 0-25 index efficiently
7. **Helper Method**: `searchPrefix` reduces code duplication between `search` and `startsWith`
8. **Root as `this`**: The Trie object itself serves as the root, eliminating need for separate root pointer

## Edge Cases

1. **Empty string**: Should be handled (mark root as end if needed)
2. **Single character**: Works normally
3. **Duplicate insert**: Same word inserted twice (safe, just re-marks end)
4. **Prefix of existing word**: `insert("apple")`, then `insert("app")` works
5. **Word extends prefix**: `insert("app")`, then `insert("apple")` works
6. **Non-existent search**: Returns `false` correctly
7. **Non-existent prefix**: `startsWith` returns `false` correctly

## Common Mistakes

1. **Forgetting `isWord` check**: `search` returns true for prefixes if not checking `isWord`
2. **Not checking `isWord` in search**: `search("app")` returns true when only "apple" exists
3. **Character indexing error**: Forgetting `ch -= 'a'` before accessing `children[ch]`
4. **Index out of bounds**: Not validating character is lowercase (0-25 range)
5. **Null pointer access**: Not checking `if(!node->children[ch])` before accessing
6. **Incorrect traversal**: Not updating `node = node->children[ch]` in loop
7. **Case sensitivity**: Assuming only lowercase (problem constraint)
8. **Using `this` incorrectly**: Forgetting that root is `this` itself, not a separate pointer

## Alternative Approaches

### Using Separate TrieNode Class (with Memory Management)

```cpp
class TrieNode {
public:
    TrieNode* links[26];
    bool isEnd;
    TrieNode() {
        for(int i = 0; i < 26; i++) links[i] = nullptr;
        isEnd = false;
    }
};

class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }
    ~Trie() { deleteSubtree(root); }
    // ... insert, search, startsWith with helper methods
    void deleteSubtree(TrieNode* node) {
        if(!node) return;
        for(int i = 0; i < 26; i++) deleteSubtree(node->links[i]);
        delete node;
    }
};
```

**Pros**: Better encapsulation, explicit memory management with destructor  
**Cons**: More code, requires separate node class

### Using `unordered_map` for Children

```cpp
class Trie {
    unordered_map<char, Trie*> children;
    bool isWord;
    // ... rest of implementation
};
```

**Pros**: Supports any character set, more flexible  
**Cons**: More memory overhead, slightly slower lookups than array

### Note on Memory Management

The current implementation doesn't include a destructor. For production code, consider adding:

```cpp
~Trie() {
    for(Trie* child : children) {
        if(child) delete child;
    }
}
```

However, for LeetCode problems, this is often omitted for simplicity.

## When to Use Trie

1. **Autocomplete**: Fast prefix matching
2. **Spell Checker**: Dictionary lookup
3. **IP Routing**: Longest prefix matching
4. **Search Engines**: Prefix-based search
5. **Phone Directory**: Name/contact lookup
6. **Word Games**: Valid word checking

## Related Problems

- [LC 211: Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) - Trie with wildcard search
- [LC 212: Word Search II](https://leetcode.com/problems/word-search-ii/) - Trie + DFS on board
- [LC 642: Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) - Trie with frequency tracking
- [LC 648: Replace Words](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-648-replace-words/) - Trie for prefix replacement
- [LC 677: Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) - Trie with value storage
- [LC 720: Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) - Trie traversal

---

*This problem is a fundamental **data structure implementation** that demonstrates the Trie (Prefix Tree) structure. It's essential for understanding prefix-based string operations and is widely used in autocomplete systems and search engines.*

