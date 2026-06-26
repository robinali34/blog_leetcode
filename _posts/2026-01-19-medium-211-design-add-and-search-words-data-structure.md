---
layout: post
title: "[Medium] 211. Design Add and Search Words Data Structure"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, medium, string, design, trie]
permalink: /2026/01/19/medium-211-design-add-and-search-words-data-structure/
tags: [leetcode, medium, string, design, trie, wildcard-search, dfs]
---
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

## Thinking Process

1. **Trie Foundation**: Builds on standard Trie structure

- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 165" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Tree DFS (bottom-up)</text>

  <line x1="140" y1="42" x2="80" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="140" y1="42" x2="200" y2="88" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="80" y1="88" x2="50" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <line x1="200" y1="88" x2="230" y2="128" stroke="#8E9AAF" stroke-width="2"/>
  <circle cx="140" cy="42" r="18" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="140" y="46" text-anchor="middle" font-size="12" fill="#3D3535">3</text>
  <circle cx="80" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="80" y="92" text-anchor="middle" font-size="11" fill="#3D3535">9</text>
  <circle cx="200" cy="88" r="16" fill="#C9B1BD" stroke="#8E9AAF" stroke-width="2"/>
  <text x="200" y="92" text-anchor="middle" font-size="11" fill="#3D3535">20</text>
  <circle cx="50" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="50" y="132" text-anchor="middle" font-size="10" fill="#3D3535">15</text>
  <circle cx="230" cy="128" r="14" fill="#A8B5A2" stroke="#8E9AAF" stroke-width="1.5"/>
  <text x="230" y="132" text-anchor="middle" font-size="10" fill="#3D3535">7</text>
  <text x="140" y="155" text-anchor="middle" font-size="11" fill="#6B6560">post-order: combine left + right + 1</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Recursive DFS** *(this problem)* | $O(n)$ | $O(h)$ stack | Natural for trees and graphs |
| Iterative DFS (stack) | $O(n)$ | $O(n)$ | Avoid recursion depth limits |
| DFS with memoization | $O(n)$ | $O(n)$ | Overlapping subproblems on graphs |
| Backtracking DFS | $O(2^n)$ typical | $O(n)$ | Enumerate choices with pruning |

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

### Solution Explanation

**Approach:** Recursive DFS (this problem)

**Key idea:** 1. **Trie Foundation**: Builds on standard Trie structure

**How the code works:**
1. **Trie Foundation**: Builds on standard Trie structure
- DFS explores one branch fully before backtracking.
- Mark visited nodes to avoid cycles on graphs.
- Return aggregated results from children to the parent.
## Common Mistakes

1. **Single wildcard**: `search(".")` when no single-letter words exist
2. **All wildcards**: `search("...")` explores all 3-letter words
3. **Wildcard at start**: `search(".ad")` matches "bad", "dad", "mad"
4. **Wildcard at end**: `search("ba.")` matches "bad", "bat", etc.
5. **No match**: `search("xyz")` returns false correctly
6. **Empty word**: Not applicable (constraints guarantee length ≥ 1)
7. **Multiple wildcards**: `search("b..")` handles multiple wildcards

1. **Not handling null nodes**: Forgetting to check if node exists before accessing
2. **Incorrect base case**: Not checking `idx == word.size()` before checking `isWord`
3. **Wildcard logic**: Not trying all children when encountering `'.'`
4. **Memory leaks**: Forgetting to implement destructor
5. **Early exit**: Not returning immediately when match found in wildcard search
6. **Index management**: Off-by-one errors in recursive calls

## When to Use This Structure

1. **Word Search with Wildcards**: Pattern matching in dictionaries
2. **Autocomplete with Partial Input**: When users type incomplete words
3. **Spell Checker**: Finding similar words with wildcards
4. **Text Search**: Searching documents with pattern matching
5. **Game Development**: Word games like Scrabble, Boggle
6. **Search Engines**: Prefix-based search with pattern support

## Related Problems

- [LC 208: Implement Trie (Prefix Tree)](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-208-implement-trie/) - Basic Trie without wildcards
- [LC 212: Word Search II](https://www.leetcode.com/problems/word-search-ii/) - Trie + DFS on board
- [LC 642: Design Search Autocomplete System](https://www.leetcode.com/problems/design-search-autocomplete-system/) - Trie with frequency tracking
- [LC 648: Replace Words](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-648-replace-words/) - Trie for prefix replacement
- [LC 677: Map Sum Pairs](https://www.leetcode.com/problems/map-sum-pairs/) - Trie with value storage
- [LC 720: Longest Word in Dictionary](https://www.leetcode.com/problems/longest-word-in-dictionary/) - Trie traversal

---

*This problem extends the **Trie data structure** with **wildcard search** capabilities. The key is using DFS to explore all possible paths when encountering wildcard characters, making it useful for pattern matching and flexible word search applications.*

## Key Takeaways

1. **Trie Foundation**: Builds on standard Trie structure
2. **Wildcard Handling**: DFS explores all paths when encountering `'.'`
3. **Early Termination**: Returns true immediately when match found
4. **Memory Safety**: Destructor prevents memory leaks
5. **Map vs Array**: Using `unordered_map` is more flexible but slightly slower than array
6. **Recursive Search**: Clean recursive approach for wildcard matching

## References

- [LC 211: Design Add and Search Words Data Structure on LeetCode](https://www.leetcode.com/problems/design-add-and-search-words-data-structure/)
- [LeetCode Discuss — LC 211: Design Add and Search Words Data Structure](https://www.leetcode.com/problems/design-add-and-search-words-data-structure/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/design-add-and-search-words-data-structure/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
