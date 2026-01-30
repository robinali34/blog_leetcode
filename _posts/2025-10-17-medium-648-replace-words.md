---
layout: post
title: "[Medium] 648. Replace Words"
date: 2025-10-17 16:17:34 -0700
categories: leetcode algorithm medium cpp trie hash-set string-processing problem-solving
---

# [Medium] 648. Replace Words

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Root replacement**: When should we replace a word? (Assumption: If word starts with a root from dictionary, replace with shortest matching root)

2. **Shortest root**: What if multiple roots match? (Assumption: Use shortest root - lexicographically smallest if same length)

3. **Word boundaries**: How are words separated? (Assumption: Words separated by spaces - standard sentence format)

4. **Case sensitivity**: Are comparisons case-sensitive? (Assumption: Based on constraints, only lowercase letters, so case doesn't matter)

5. **Return format**: What should we return? (Assumption: Modified sentence with words replaced by roots where applicable)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to replace words with roots. Let me check each word against all dictionary roots."

**Naive Solution**: For each word in sentence, check all dictionary roots to find shortest prefix match.

**Complexity**: O(m × n × k) time where m = words, n = dictionary size, k = average word length, O(m × k) space

**Issues**:
- O(m × n × k) time - inefficient
- Repeats prefix checking
- Doesn't leverage prefix structure
- Can be optimized

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use hash set for dictionary and check prefixes efficiently."

**Improved Solution**: Store dictionary in hash set. For each word, check all prefixes from shortest to longest, replace with first matching root.

**Complexity**: O(m × k²) time, O(n × k) space

**Improvements**:
- Hash set enables O(1) lookup
- O(m × k²) is better than O(m × n × k)
- Still checks all prefixes
- Can optimize further

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "I can use Trie to efficiently find shortest matching prefix."

**Best Solution**: Build Trie from dictionary. For each word, traverse Trie to find shortest matching root. Trie enables efficient prefix matching without checking all prefixes.

**Complexity**: O(n × k + m × k) time, O(n × k) space

**Key Realizations**:
1. Trie is perfect for prefix matching
2. O(n × k + m × k) time is optimal
3. Trie space is O(n × k) for dictionary
4. Much more efficient than hash set approach

## Solution 1: Hash Set with Prefix Matching

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

## Solution 2: Trie Data Structure

**Time Complexity:** O(n * m) where n is number of words, m is average word length  
**Space Complexity:** O(d * k) where d is dictionary size, k is average root length

Use a trie to efficiently find the shortest root prefix for each word.

```cpp
class TrieNode{
public:
    bool isEnd;
    vector<TrieNode*> children;
    TrieNode(): children(26, nullptr) {isEnd = false;}
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {root = new TrieNode();}

    void insert(string word) {
        TrieNode * current = root;
        for(char c: word) {
            if(current->children[c - 'a'] == nullptr) {
                current->children[c - 'a'] = new TrieNode();
            }
            current = current->children[c - 'a'];
        }
        current->isEnd = true;
    }

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
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        istringstream sStream(sentence);
        Trie dicTrie;
        
        for(string& word: dictionary) {
            dicTrie.insert(word);
        }
        
        string word, newSentence;
        while(getline(sStream, word, ' ')) {
            newSentence.append(dicTrie.shortestRoot(word) + " ");
        }
        
        if(!newSentence.empty()) newSentence.pop_back();
        return newSentence;
    }
};
```

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

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Hash Set | O(n * m) | O(d) |
| Trie | O(n * m) | O(d * k) |

Where:
- n = number of words in sentence
- m = average word length
- d = dictionary size
- k = average root length

## Edge Cases

1. **Single word:** `dictionary = ["a"]`, `sentence = "a"` → `"a"`
2. **No matches:** `dictionary = ["cat"]`, `sentence = "dog"` → `"dog"`
3. **Empty dictionary:** `dictionary = []`, `sentence = "hello"` → `"hello"`
4. **Single character roots:** `dictionary = ["a","b"]`, `sentence = "abc"` → `"a"`

## Key Insights

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

## Common Mistakes

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

## Alternative Approaches

### Approach 1: Brute Force
```cpp
class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        istringstream sStream(sentence);
        string word, result;
        
        while(getline(sStream, word, ' ')) {
            string shortest = word;
            for(string& root : dictionary) {
                if(word.substr(0, root.size()) == root && root.size() < shortest.size()) {
                    shortest = root;
                }
            }
            result += shortest + " ";
        }
        
        if(!result.empty()) result.pop_back();
        return result;
    }
};
```

**Time Complexity:** O(n * d * m)  
**Space Complexity:** O(1)

### Approach 2: Sorted Dictionary
```cpp
class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        sort(dictionary.begin(), dictionary.end());
        istringstream sStream(sentence);
        string word, result;
        
        while(getline(sStream, word, ' ')) {
            string shortest = word;
            for(string& root : dictionary) {
                if(word.substr(0, root.size()) == root) {
                    shortest = root;
                    break;
                }
            }
            result += shortest + " ";
        }
        
        if(!result.empty()) result.pop_back();
        return result;
    }
};
```

**Time Complexity:** O(d log d + n * d * m)  
**Space Complexity:** O(1)

## Related Problems

- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/)
- [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)

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
