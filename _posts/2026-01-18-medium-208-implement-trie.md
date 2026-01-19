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
class TrieNode {
public:
    TrieNode() {
        for(int i = 0; i < 26; i++) {
            links[i] = nullptr;
        }
        isEnd = false;
    }

    bool containsKey(char ch) const {
        return links[ch - 'a'] != nullptr;
    }

    TrieNode* get(char ch) const {
        return links[ch - 'a'];
    }

    TrieNode* getAt(int i) const {
        return links[i];
    }

    void put (char ch, TrieNode* node) {
        links[ch - 'a'] = node;
    }

    void setEnd(){
        isEnd = true;
    }

    bool isEndofWord() const {
        return isEnd;
    }

private:
    TrieNode* links[26];
    bool isEnd;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    ~Trie(){
        deleteSubtree(root);
    }
    
    void insert(string word) {
        TrieNode* node = root;
        for(int i = 0; i < (int)word.length(); i++) {
            char curr = word[i];
            if(!node->containsKey(curr)) {
                node->put(curr, new TrieNode());
            }
            node = node->get(curr);
        }
        node->setEnd();
    }
    
    bool search(string word) {
        TrieNode* node = searchPrefix(word);
        return node != nullptr && node->isEndofWord();
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = searchPrefix(prefix);
        return node != nullptr;
    }

private:
    TrieNode* root;

    TrieNode* searchPrefix(const string& word) {
        TrieNode* node = root;
        for(int i = 0; i < (int)word.length(); i++) {
            char curr = word[i];
            if(node->containsKey(curr)){
                node = node->get(curr);
            } else {
                return nullptr;
            }
        }
        return node;
    }

    void deleteSubtree(TrieNode* node) {
        if(!node) return;
        for(int i = 0; i < 26; i++) {
            deleteSubtree(node->getAt(i));
        }
        delete node;
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

#### **TrieNode Class:**

1. **Constructor**: Initializes 26 child pointers to `nullptr` and `isEnd` to `false`
2. **containsKey(char ch)**: Checks if child node exists for character
3. **get(char ch)**: Returns child node for character
4. **getAt(int i)**: Returns child node at index (for cleanup)
5. **put(char ch, TrieNode* node)**: Sets child node for character
6. **setEnd()**: Marks node as end of word
7. **isEndofWord()**: Returns whether node marks end of word

#### **Trie Class:**

1. **Constructor**: Creates root node
2. **Destructor**: Recursively deletes all nodes to prevent memory leaks
3. **insert(word)**:
   - Start from root
   - For each character, create node if missing
   - Traverse to next node
   - Mark final node as end of word

4. **search(word)**:
   - Use `searchPrefix` to find node
   - Return `true` only if node exists AND is marked as end

5. **startsWith(prefix)**:
   - Use `searchPrefix` to find node
   - Return `true` if node exists (end flag not required)

6. **searchPrefix(word)** (Helper):
   - Traverse from root following characters
   - Return node if path exists, `nullptr` otherwise

7. **deleteSubtree(node)** (Helper):
   - Recursively delete all children
   - Delete current node

### Example Walkthrough:

**Operations:** `insert("apple")`, `search("app")`, `startsWith("app")`, `insert("app")`, `search("app")`

```
Step 1: insert("apple")
  root -> 'a' -> 'p' -> 'p' -> 'l' -> 'e' (marked as end)
  
Step 2: search("app")
  Traverse: root -> 'a' -> 'p' -> 'p'
  Node exists but NOT marked as end
  Return: false ✓

Step 3: startsWith("app")
  Traverse: root -> 'a' -> 'p' -> 'p'
  Node exists (regardless of end flag)
  Return: true ✓

Step 4: insert("app")
  root -> 'a' -> 'p' -> 'p' (marked as end)
  
Step 5: search("app")
  Traverse: root -> 'a' -> 'p' -> 'p'
  Node exists AND marked as end
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

1. **Trie Structure**: Tree where each path represents a prefix/word
2. **End Marker**: Critical to distinguish between prefix and complete word
3. **Shared Prefixes**: Multiple words sharing prefixes share nodes (space efficient)
4. **Array vs Map**: Array (26 elements) is faster and uses less memory than map
5. **Memory Management**: Destructor prevents memory leaks in C++
6. **Helper Methods**: Encapsulate node operations for cleaner code
7. **searchPrefix**: Reusable helper reduces code duplication

## Edge Cases

1. **Empty string**: Should be handled (mark root as end if needed)
2. **Single character**: Works normally
3. **Duplicate insert**: Same word inserted twice (safe, just re-marks end)
4. **Prefix of existing word**: `insert("apple")`, then `insert("app")` works
5. **Word extends prefix**: `insert("app")`, then `insert("apple")` works
6. **Non-existent search**: Returns `false` correctly
7. **Non-existent prefix**: `startsWith` returns `false` correctly

## Common Mistakes

1. **Forgetting end marker**: `search` returns true for prefixes
2. **Not checking end in search**: `search("app")` returns true when only "apple" exists
3. **Memory leaks**: Not implementing destructor
4. **Index out of bounds**: Not validating character is lowercase
5. **Null pointer**: Not checking if node exists before accessing
6. **Incorrect traversal**: Not moving to next node in loop
7. **Case sensitivity**: Assuming only lowercase (problem constraint)

## Alternative Approaches

### Using `unordered_map` for Children

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEnd;
    TrieNode() : isEnd(false) {}
};
```

**Pros**: Supports any character set, more flexible  
**Cons**: More memory overhead, slightly slower lookups

### Simplified Version (No Helper Methods)

```cpp
class Trie {
    struct TrieNode {
        TrieNode* children[26] = {};
        bool isEnd = false;
    };
    TrieNode* root = new TrieNode();
    
public:
    void insert(string word) {
        TrieNode* node = root;
        for(char c : word) {
            int idx = c - 'a';
            if(!node->children[idx])
                node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->isEnd = true;
    }
    // ... similar for search and startsWith
};
```

**Pros**: More concise  
**Cons**: Less encapsulation, harder to extend

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

