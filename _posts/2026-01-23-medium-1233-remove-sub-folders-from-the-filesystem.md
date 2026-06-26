---
layout: post
title: "[Medium] 1233. Remove Sub-Folders from the Filesystem"
date: 2026-01-23 00:00:00 -0700
categories: [leetcode, medium, array, string, trie, sorting]
permalink: /2026/01/23/medium-1233-remove-sub-folders-from-the-filesystem/
tags: [leetcode, medium, array, string, trie, sorting, prefix-matching]
---
Given a list of folders `folder`, return *the folders after removing all **sub-folders** in those folders*. You may return the answer in **any order**.

If a `folder[i]` is located within another `folder[j]`, it is called a **sub-folder** of it.

The format of a path is one or more concatenated strings of the form: `'/'` followed by one or more lowercase English letters.

For example, `"/leetcode"` and `"/leetcode/problems"` are valid paths while an empty string and `"/"` are not.

## Examples

**Example 1:**

```
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
```

**Example 2:**

```
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
```

**Example 3:**

```
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
Explanation: None of the folders are subfolders of another folder.
```

## Constraints

- `1 <= folder.length <= 4 * 10^4`
- `2 <= folder[i].length <= 100`
- `folder[i]` contains only lowercase letters and `'/'`
- `folder[i]` always starts with `'/'`
- Each folder name is **unique**

## Thinking Process

1. **Prefix Matching**: A folder is a subfolder if its path is a prefix of another folder
- Efficient for checking if any prefix exists
- More memory intensive but clearer logic
- Simpler code, more efficient

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.



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
| **Two pointers on string** *(this problem)* | $O(n)$ | $O(1)$ | Palindrome, parsing |
| Hash map / frequency | $O(n)$ | $O(k)$ | Anagram, character counts |
| KMP / rolling hash | $O(n)$ | $O(n)$ | Pattern matching |
| Stack parsing | $O(n)$ | $O(n)$ | Decode string, parentheses |

## Solution

```cpp
struct TrieNode{
    bool isEnd;
    unordered_map<string, TrieNode*> children;
    TrieNode(): isEnd(false){}
};

class Solution {
public:
    Solution(): root(new TrieNode()) {}

    ~Solution() {deleteTrie(root);}

    vector<string> removeSubfolders(vector<string>& folder) {
        for(auto& path: folder) {
            TrieNode* curr = root;
            istringstream iss(path);
            string folderName;

            while(getline(iss, folderName, '/')) {
                if(folderName.empty()) continue;
                if(!curr->children.contains(folderName)) {
                    curr->children[folderName] = new TrieNode();
                }
                curr = curr->children[folderName];
            }
            curr->isEnd = true;
        }
        vector<string> rtn;
        for(auto& path: folder) {
            TrieNode* curr = root;
            istringstream iss(path);
            string folderName;
            bool isSubFolder = false;

            while(getline(iss, folderName, '/')) {
                if(folderName.empty()) continue;
                auto it = curr->children.find(folderName);
                if(it == curr->children.end()) break;
                TrieNode* nextNode = it->second;
                if(nextNode->isEnd && iss.rdbuf()->in_avail() != 0) {
                    isSubFolder = true;
                    break;
                }
                curr = nextNode;
            }
            if(!isSubFolder) rtn.push_back(path);
        }
        return rtn;
    }

private:
    TrieNode* root;

    void deleteTrie(TrieNode* node) {
        if(!node) return;
        for(auto& [_, child]: node->children) {
            deleteTrie(child);
        }
        delete node;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** 1. **Prefix Matching**: A folder is a subfolder if its path is a prefix of another folder

**How the code works:**
1. **Prefix Matching**: A folder is a subfolder if its path is a prefix of another folder
- Efficient for checking if any prefix exists
- More memory intensive but clearer logic
- Simpler code, more efficient
- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.

**Walkthrough** — input `folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]`, expected output `["/a","/c/d","/c/f"]`:

Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
## Common Mistakes

1. **Single folder**: `["/a"]` → `["/a"]`
2. **No subfolders**: `["/a/b", "/c/d"]` → `["/a/b", "/c/d"]`
3. **All subfolders**: `["/a", "/a/b", "/a/b/c"]` → `["/a"]`
4. **Similar prefixes**: `["/a/b", "/a/bc"]` → Both kept (not subfolders)
5. **Deep nesting**: `["/a", "/a/b", "/a/b/c", "/a/b/c/d"]` → `["/a"]`

1. **False prefix match**: `/a/bc` matching `/a/b` without checking next character
2. **Wrong comparison**: Using `startsWith` without verifying `/` boundary
3. **Memory leaks**: Not deleting trie nodes in C++
4. **Empty string handling**: Not skipping empty strings from leading `/`
5. **Sorting order**: Not understanding lexicographic ordering

## Related Problems

- [LC 208: Implement Trie (Prefix Tree)](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-208-implement-trie/) - Trie basics
- [LC 648: Replace Words](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-648-replace-words/) - Trie for prefix replacement
- [LC 720: Longest Word in Dictionary](https://www.leetcode.com/problems/longest-word-in-dictionary/) - Trie traversal
- [LC 14: Longest Common Prefix](https://www.leetcode.com/problems/longest-common-prefix/) - Prefix matching

## Key Takeaways

1. **Prefix Matching**: A folder is a subfolder if its path is a prefix of another folder
2. **Trie Approach**: 
   - Efficient for checking if any prefix exists
   - More memory intensive but clearer logic
3. **Sorting Approach**: 
   - Simpler code, more efficient
   - Leverages lexicographic ordering property
4. **Path Parsing**: Use `istringstream` and `getline` to split by `/`
5. **Edge Case**: Check that prefix match is followed by `/` to avoid false positives

## References

- [LC 1233: Remove Sub-Folders from the Filesystem on LeetCode](https://www.leetcode.com/problems/remove-sub-folders-from-the-filesystem/)
- [LeetCode Discuss — LC 1233: Remove Sub-Folders from the Filesystem](https://www.leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/remove-sub-folders-from-the-filesystem/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
