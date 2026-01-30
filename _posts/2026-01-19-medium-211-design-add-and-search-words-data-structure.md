---
layout: post
title: "211. Design Add and Search Words Data Structure"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, medium, string, design, trie]
permalink: /2026/01/19/medium-211-design-add-and-search-words-data-structure/
tags: [leetcode, medium, string, design, trie, wildcard-search, dfs]
---

# 211. Design Add and Search Words Data Structure

## Problem Statement

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

## Examples

**Example 1:**
```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

## Constraints

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- There will be at most `10^4` calls to `addWord` and `search`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Word dictionary**: What operations should it support? (Assumption: addWord(word) - add word, search(word) - search with wildcard support)

2. **Wildcard matching**: What does '.' represent? (Assumption: '.' matches any single lowercase letter - can be any character)

3. **Return value**: What should search() return? (Assumption: Boolean - true if word exists (with wildcard matching), false otherwise)

4. **Word format**: What format are words? (Assumption: Lowercase English letters - per constraints)

5. **Multiple matches**: Can '.' match different letters in same search? (Assumption: Yes - each '.' independently matches any letter)

## Solution Approach

This problem extends [LC 208: Implement Trie](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-208-implement-trie/) with **wildcard search** support. The key challenge is handling the `'.'` character which can match any letter.

### Key Insights:

1. **Trie Structure**: Use Trie to store words efficiently
2. **Wildcard Matching**: When encountering `'.'`, explore all possible child paths
3. **DFS Search**: Use recursive DFS to handle wildcard exploration
4. **Memory Management**: Proper destructor to prevent memory leaks

### Algorithm:

1. **addWord**: Same as standard Trie - traverse and create nodes, mark end
2. **search**: 
   - Use DFS with index tracking
   - If character is `'.'`, try all children
   - If character is specific, follow that path
   - Return true if any path leads to a word

## Solution

```cpp
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isWord = false;
};

class WordDictionary {
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    ~WordDictionary() {
        deleteTrie(root);
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for(char ch : word) {
            if(!node->children.contains(ch)) {
                node->children[ch] = new TrieNode();
            }
            node = node->children[ch];
        }
        node->isWord = true;
    }
    
    bool search(string word) {
        return searchInNode(word, 0, root);
    }

private:
    TrieNode* root;

    bool searchInNode(string& word, int idx, TrieNode* node) {
        if(!node) return false;
        if(idx == word.size()) return node->isWord;
        char curr = word[idx];
        if(curr == '.') {
            for(auto& [_, child]: node->children) {
                if(searchInNode(word, idx + 1, child)) {
                    return true;
                }
            }
            return false;
        }
        if(!node->children.contains(curr)) return false;
        return searchInNode(word, idx + 1, node->children[curr]);
    }

    void deleteTrie(TrieNode* node) {
        if(!node) return;
        for(auto& [_, child]: node->children) {
            deleteTrie(child);
        }
        delete node;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
```

### Algorithm Explanation:

#### **TrieNode Structure:**

1. **children**: `unordered_map` storing child nodes (more flexible than array)
2. **isWord**: Boolean flag marking end of word

#### **WordDictionary Class:**

1. **Constructor**: Creates root node
2. **Destructor**: Recursively deletes all nodes to prevent memory leaks
3. **addWord(word)**:
   - Start from root
   - For each character, create node if missing
   - Traverse to next node
   - Mark final node as word

4. **search(word)**:
   - Calls helper `searchInNode` starting at index 0
   - Returns true if any matching word found

5. **searchInNode(word, idx, node)** (Helper):
   - **Base Cases**:
     - If node is null, return false
     - If reached end of word, return `node->isWord`
   
   - **Wildcard Handling** (`curr == '.'`):
     - Try all children paths
     - Return true if any path succeeds
     - Return false if all paths fail
   
   - **Specific Character**:
     - Check if child exists
     - Recursively search in that child

6. **deleteTrie(node)** (Helper):
   - Recursively delete all children
   - Delete current node

### Example Walkthrough:

**Operations:** `addWord("bad")`, `addWord("dad")`, `search(".ad")`

```
Step 1: addWord("bad")
  root -> 'b' -> 'a' -> 'd' (marked as word)

Step 2: addWord("dad")
  root -> 'd' -> 'a' -> 'd' (marked as word)

Step 3: search(".ad")
  searchInNode(".ad", 0, root):
    curr = '.', try all children:
      Try 'b': searchInNode(".ad", 1, node['b'])
        curr = 'a', follow 'a': searchInNode(".ad", 2, node['b']['a'])
          curr = 'd', follow 'd': searchInNode(".ad", 3, node['b']['a']['d'])
            idx == word.size(), return node->isWord = true ✓
      Return true (early exit)
  Return: true ✓
```

### Complexity Analysis:

- **Time Complexity:**
  - `addWord(word)`: O(m) where m = word length
  - `search(word)`: 
    - **Best Case**: O(m) when no wildcards
    - **Worst Case**: O(26^k × m) where k = number of `'.'` characters
    - In practice, much better due to early termination

- **Space Complexity:**
  - **Worst Case**: O(N × M) where N = number of words, M = average word length
  - **Best Case**: O(unique prefixes) - shared prefixes reduce space
  - Each node stores a map, so space depends on unique characters used

## Key Insights

1. **Trie Foundation**: Builds on standard Trie structure
2. **Wildcard Handling**: DFS explores all paths when encountering `'.'`
3. **Early Termination**: Returns true immediately when match found
4. **Memory Safety**: Destructor prevents memory leaks
5. **Map vs Array**: Using `unordered_map` is more flexible but slightly slower than array
6. **Recursive Search**: Clean recursive approach for wildcard matching

## Edge Cases

1. **Single wildcard**: `search(".")` when no single-letter words exist
2. **All wildcards**: `search("...")` explores all 3-letter words
3. **Wildcard at start**: `search(".ad")` matches "bad", "dad", "mad"
4. **Wildcard at end**: `search("ba.")` matches "bad", "bat", etc.
5. **No match**: `search("xyz")` returns false correctly
6. **Empty word**: Not applicable (constraints guarantee length ≥ 1)
7. **Multiple wildcards**: `search("b..")` handles multiple wildcards

## Common Mistakes

1. **Not handling null nodes**: Forgetting to check if node exists before accessing
2. **Incorrect base case**: Not checking `idx == word.size()` before checking `isWord`
3. **Wildcard logic**: Not trying all children when encountering `'.'`
4. **Memory leaks**: Forgetting to implement destructor
5. **Early exit**: Not returning immediately when match found in wildcard search
6. **Index management**: Off-by-one errors in recursive calls

## Alternative Approaches

### Using Array Instead of Map

```cpp
struct TrieNode {
    TrieNode* children[26] = {};
    bool isWord = false;
};
```

**Pros**: Faster lookups, less memory overhead  
**Cons**: Less flexible, assumes only lowercase letters

### Iterative Search (Non-Recursive)

```cpp
bool search(string word) {
    queue<pair<TrieNode*, int>> q;
    q.push({root, 0});
    
    while(!q.empty()) {
        auto [node, idx] = q.front();
        q.pop();
        
        if(idx == word.size()) {
            if(node->isWord) return true;
            continue;
        }
        
        char curr = word[idx];
        if(curr == '.') {
            for(auto& [_, child]: node->children) {
                q.push({child, idx + 1});
            }
        } else {
            if(node->children.contains(curr)) {
                q.push({node->children[curr], idx + 1});
            }
        }
    }
    return false;
}
```

**Pros**: Avoids recursion stack overflow for very long words  
**Cons**: More complex, uses more memory for queue

## When to Use This Structure

1. **Word Search with Wildcards**: Pattern matching in dictionaries
2. **Autocomplete with Partial Input**: When users type incomplete words
3. **Spell Checker**: Finding similar words with wildcards
4. **Text Search**: Searching documents with pattern matching
5. **Game Development**: Word games like Scrabble, Boggle
6. **Search Engines**: Prefix-based search with pattern support

## Comparison with LC 208

| Feature | LC 208 (Trie) | LC 211 (WordDictionary) |
|---------|---------------|-------------------------|
| **Wildcard Support** | No | Yes (`.`) |
| **Search Complexity** | O(m) | O(26^k × m) worst case |
| **Use Case** | Exact match, prefix | Pattern matching |
| **Implementation** | Simpler | More complex (DFS) |

## Related Problems

- [LC 208: Implement Trie (Prefix Tree)](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-208-implement-trie/) - Basic Trie without wildcards
- [LC 212: Word Search II](https://leetcode.com/problems/word-search-ii/) - Trie + DFS on board
- [LC 642: Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) - Trie with frequency tracking
- [LC 648: Replace Words](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-648-replace-words/) - Trie for prefix replacement
- [LC 677: Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) - Trie with value storage
- [LC 720: Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) - Trie traversal

---

*This problem extends the **Trie data structure** with **wildcard search** capabilities. The key is using DFS to explore all possible paths when encountering wildcard characters, making it useful for pattern matching and flexible word search applications.*

