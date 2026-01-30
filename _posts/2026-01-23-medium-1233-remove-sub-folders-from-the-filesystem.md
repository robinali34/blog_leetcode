---
layout: post
title: "1233. Remove Sub-Folders from the Filesystem"
date: 2026-01-23 00:00:00 -0700
categories: [leetcode, medium, array, string, trie, sorting]
permalink: /2026/01/23/medium-1233-remove-sub-folders-from-the-filesystem/
tags: [leetcode, medium, array, string, trie, sorting, prefix-matching]
---

# 1233. Remove Sub-Folders from the Filesystem

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Subfolder definition**: What exactly defines a subfolder? (Assumption: Folder A is a subfolder of folder B if A's path starts with B's path followed by '/', e.g., "/a/b" is subfolder of "/a")

2. **Path format**: Are all paths absolute (starting with '/')? (Assumption: Yes - all paths start with '/' and don't have trailing '/')

3. **Case sensitivity**: Are folder names case-sensitive? (Assumption: Yes - only lowercase letters are allowed per constraints)

4. **Empty folders**: Can there be empty folder paths? (Assumption: No - minimum length is 2, so at least "/a" format)

5. **Duplicate folders**: Can the same folder path appear multiple times? (Assumption: Based on constraints, folder names are unique, so no duplicates)

## Solution Approach

This problem requires identifying and removing folder paths that are subfolders of other folders. A folder is a subfolder if its path is a prefix of another folder's path.

### Key Insights:

1. **Prefix Matching**: A folder is a subfolder if its path is a prefix of another folder
2. **Trie Approach**: Build a trie of all folders, then check if any prefix is marked as end
3. **Sorting Approach**: Sort folders lexicographically, then check if current folder is a prefix of previous
4. **Path Parsing**: Split paths by `'/'` to process folder names individually

## Solution 1: Trie-Based Approach

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

### Algorithm Explanation:

#### **TrieNode Structure:**

1. **`isEnd`**: Marks if this node represents the end of a folder path
2. **`children`**: Map from folder name to child TrieNode

#### **Build Trie (First Pass):**

1. **Parse Each Path**: Split path by `'/'` using `istringstream` and `getline`
2. **Skip Empty**: Ignore empty strings (from leading `/`)
3. **Create Nodes**: For each folder name, create node if missing
4. **Mark End**: Mark final node as `isEnd = true`

#### **Check Subfolders (Second Pass):**

1. **Traverse Path**: For each folder path, traverse trie following folder names
2. **Check Prefix**: If we encounter a node with `isEnd = true` and there are more folders remaining (`iss.rdbuf()->in_avail() != 0`), it's a subfolder
3. **Add to Result**: Only add folders that are not subfolders

#### **Memory Management:**

- **Destructor**: Recursively deletes all nodes to prevent memory leaks
- **`deleteTrie`**: Helper function for recursive deletion

### Example Walkthrough:

**Input:** `folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]`

```
Step 1: Build Trie
  "/a": root -> "a" (isEnd=true)
  "/a/b": root -> "a" -> "b" (isEnd=true)
  "/c/d": root -> "c" -> "d" (isEnd=true)
  "/c/d/e": root -> "c" -> "d" -> "e" (isEnd=true)
  "/c/f": root -> "c" -> "f" (isEnd=true)

Step 2: Check Each Path
  "/a": Traverse "a", isEnd=true, no more folders → NOT subfolder ✓
  "/a/b": Traverse "a", isEnd=true, more folders exist → IS subfolder ✗
  "/c/d": Traverse "c" -> "d", isEnd=true, no more → NOT subfolder ✓
  "/c/d/e": Traverse "c" -> "d", isEnd=true, more exist → IS subfolder ✗
  "/c/f": Traverse "c" -> "f", isEnd=true, no more → NOT subfolder ✓

Result: ["/a","/c/d","/c/f"] ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n × m)
  - Building trie: O(n × m) where n = number of folders, m = average path length
  - Checking subfolders: O(n × m)
  - Overall: O(n × m)

- **Space Complexity:** O(n × m)
  - Trie structure: O(n × m) in worst case
  - Result array: O(n)
  - Overall: O(n × m)

## Solution 2: Sorting-Based Approach

```cpp
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        sort(folder.begin(), folder.end());
        vector<string> rtn;
        for(const string& f: folder) {
            if(rtn.empty() || f.compare(0, rtn.back().size(), rtn.back()) != 0 ||
                f[rtn.back().size()] != '/'){
                    rtn.push_back(f);
                }
        }
        return rtn;
    }
};
```

### Algorithm Explanation:

1. **Sort Folders**: Sort all folders lexicographically
   - After sorting, parent folders come before their subfolders
   - Example: `["/a", "/a/b", "/c/d"]` stays in order

2. **Check Prefix**: For each folder:
   - If result is empty, add it
   - Otherwise, check if current folder is a prefix of the last added folder
   - **Key Check**: `f.compare(0, rtn.back().size(), rtn.back()) != 0`
     - Compares first `rtn.back().size()` characters of `f` with `rtn.back()`
     - Returns non-zero if they differ
   - **Additional Check**: `f[rtn.back().size()] != '/'`
     - Ensures the next character after prefix is `/` (not just a prefix match)
     - Prevents false positives like `/a/bc` matching `/a/b`

3. **Add to Result**: Only add if not a subfolder

### Example Walkthrough:

**Input:** `folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]`

```
Step 1: Sort
  ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]

Step 2: Process
  "/a": rtn empty → add → rtn = ["/a"]
  "/a/b": compare("/a/b", 0, 2, "/a") = 0 (matches)
          "/a/b"[2] = '/' → IS subfolder ✗
  "/c/d": compare("/c/d", 0, 2, "/a") != 0 → NOT subfolder ✓
          rtn = ["/a", "/c/d"]
  "/c/d/e": compare("/c/d/e", 0, 4, "/c/d") = 0 (matches)
            "/c/d/e"[4] = '/' → IS subfolder ✗
  "/c/f": compare("/c/f", 0, 4, "/c/d") != 0 → NOT subfolder ✓
          rtn = ["/a", "/c/d", "/c/f"]

Result: ["/a","/c/d","/c/f"] ✓
```

### Why the Additional Check is Needed:

Consider: `folder = ["/a/b", "/a/bc"]`

- Without `f[rtn.back().size()] != '/'` check:
  - `/a/bc` would be incorrectly identified as subfolder of `/a/b`
- With the check:
  - `"/a/bc"[4] = 'c'` (not `/`) → NOT subfolder ✓

### Complexity Analysis:

- **Time Complexity:** O(n log n + n × m)
  - Sorting: O(n log n)
  - Processing: O(n × m) where m = average path length
  - Overall: O(n log n + n × m)

- **Space Complexity:** O(1) excluding output
  - Sorting: O(1) if in-place
  - Result array: O(n)
  - Overall: O(n) for output

## Key Insights

1. **Prefix Matching**: A folder is a subfolder if its path is a prefix of another folder
2. **Trie Approach**: 
   - Efficient for checking if any prefix exists
   - More memory intensive but clearer logic
3. **Sorting Approach**: 
   - Simpler code, more efficient
   - Leverages lexicographic ordering property
4. **Path Parsing**: Use `istringstream` and `getline` to split by `/`
5. **Edge Case**: Check that prefix match is followed by `/` to avoid false positives

## Edge Cases

1. **Single folder**: `["/a"]` → `["/a"]`
2. **No subfolders**: `["/a/b", "/c/d"]` → `["/a/b", "/c/d"]`
3. **All subfolders**: `["/a", "/a/b", "/a/b/c"]` → `["/a"]`
4. **Similar prefixes**: `["/a/b", "/a/bc"]` → Both kept (not subfolders)
5. **Deep nesting**: `["/a", "/a/b", "/a/b/c", "/a/b/c/d"]` → `["/a"]`

## Common Mistakes

1. **False prefix match**: `/a/bc` matching `/a/b` without checking next character
2. **Wrong comparison**: Using `startsWith` without verifying `/` boundary
3. **Memory leaks**: Not deleting trie nodes in C++
4. **Empty string handling**: Not skipping empty strings from leading `/`
5. **Sorting order**: Not understanding lexicographic ordering

## Comparison of Approaches

| Aspect | Trie Approach | Sorting Approach |
|--------|---------------|------------------|
| **Time** | O(n × m) | O(n log n + n × m) |
| **Space** | O(n × m) | O(n) |
| **Code Complexity** | More verbose | Simpler |
| **Memory Management** | Requires cleanup | No cleanup needed |
| **Clarity** | More explicit | More concise |
| **Best For** | When paths are long | When simplicity preferred |

## Related Problems

- [LC 208: Implement Trie (Prefix Tree)](https://robinali34.github.io/blog_leetcode/2026/01/18/medium-208-implement-trie/) - Trie basics
- [LC 648: Replace Words](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-648-replace-words/) - Trie for prefix replacement
- [LC 720: Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) - Trie traversal
- [LC 14: Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) - Prefix matching

---

*This problem demonstrates two approaches to prefix matching: **Trie** for explicit path structure representation and **Sorting** for leveraging lexicographic ordering. The sorting approach is generally preferred for its simplicity and efficiency.*
