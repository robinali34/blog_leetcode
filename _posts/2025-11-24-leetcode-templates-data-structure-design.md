---
layout: post
title: "Algorithm Templates: Data Structure Design"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates design
permalink: /posts/2025-11-24-leetcode-templates-data-structure-design/
tags: [leetcode, templates, design, data-structures]
---

{% raw %}
Minimal, copy-paste C++ for LRU/LFU cache, Trie, time-based key-value store, and common design patterns.

## Contents

- [LRU Cache](#lru-cache)
- [LFU Cache](#lfu-cache)
- [Trie](#trie)
- [Time-based Key-Value Store](#time-based-key-value-store)
- [Design Patterns](#design-patterns)

## LRU Cache

Least Recently Used cache using hash map + doubly linked list.

```cpp
class LRUCache {
private:
    int capacity_;
    list<int> keyList_;
    unordered_map<int, pair<int, list<int>::iterator>> hashMap_;
    
    void insert(int key, int value) {
        keyList_.push_back(key);
        hashMap_[key] = make_pair(value, --keyList_.end());
    }

public:
    LRUCache(int capacity) : capacity_(capacity) {
    }
    
    int get(int key) {
        auto it = hashMap_.find(key);
        if(it != hashMap_.end()) {
            keyList_.splice(keyList_.end(), keyList_, it->second.second);
            return it->second.first;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(get(key) != -1) {
            hashMap_[key].first = value;
            return;
        }
        if(hashMap_.size() < capacity_) {
            insert(key, value);
        } else {
            int removeKey = keyList_.front();
            keyList_.pop_front();
            hashMap_.erase(removeKey);
            insert(key, value);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

### Thread-Safe LRU Cache

Thread-safe version using mutex for concurrent access.

```cpp
#include <mutex>
#include <shared_mutex>

class ThreadSafeLRUCache {
private:
    int capacity_;
    list<int> keyList_;
    unordered_map<int, pair<int, list<int>::iterator>> hashMap_;
    mutable shared_mutex mtx_; // Use shared_mutex for read-write lock
    
    void insert(int key, int value) {
        keyList_.push_back(key);
        hashMap_[key] = make_pair(value, --keyList_.end());
    }
    
    bool exists(int key) const {
        return hashMap_.find(key) != hashMap_.end();
    }

public:
    ThreadSafeLRUCache(int capacity) : capacity_(capacity) {
    }
    
    int get(int key) {
        unique_lock<shared_mutex> lock(mtx_); // Exclusive lock for read+modify
        auto it = hashMap_.find(key);
        if(it != hashMap_.end()) {
            keyList_.splice(keyList_.end(), keyList_, it->second.second);
            return it->second.first;
        }
        return -1;
    }
    
    void put(int key, int value) {
        unique_lock<shared_mutex> lock(mtx_); // Exclusive lock for write
        if(exists(key)) {
            hashMap_[key].first = value;
            keyList_.splice(keyList_.end(), keyList_, hashMap_[key].second);
            return;
        }
        if(hashMap_.size() < capacity_) {
            insert(key, value);
        } else {
            int removeKey = keyList_.front();
            keyList_.pop_front();
            hashMap_.erase(removeKey);
            insert(key, value);
        }
    }
    
    size_t size() const {
        shared_lock<shared_mutex> lock(mtx_);
        return hashMap_.size();
    }
};

// Example usage:
// ThreadSafeLRUCache cache(2);
// cache.put(1, 1);
// cache.put(2, 2);
// int val = cache.get(1); // returns 1
// cache.put(3, 3); // evicts key 2
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 146 | LRU Cache | [Link](https://leetcode.com/problems/lru-cache/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-14-medium-146-lru-cache/) |

## LFU Cache

Least Frequently Used cache.

```cpp
class LFUCache {
    int capacity, minFreq;
    unordered_map<int, pair<int, int>> keyValFreq; // key -> {value, frequency}
    unordered_map<int, list<int>> freqKeys; // frequency -> list of keys
    unordered_map<int, list<int>::iterator> keyIter; // key -> iterator in freqKeys list
    
    void updateFreq(int key) {
        int freq = keyValFreq[key].second;
        freqKeys[freq].erase(keyIter[key]);
        
        if (freqKeys[freq].empty() && freq == minFreq) {
            minFreq++;
        }
        
        freq++;
        keyValFreq[key].second = freq;
        freqKeys[freq].push_back(key);
        keyIter[key] = --freqKeys[freq].end();
    }
    
public:
    LFUCache(int capacity) : capacity(capacity), minFreq(0) {}
    
    int get(int key) {
        if (keyValFreq.find(key) == keyValFreq.end()) return -1;
        updateFreq(key);
        return keyValFreq[key].first;
    }
    
    void put(int key, int value) {
        if (capacity == 0) return;
        
        if (keyValFreq.find(key) != keyValFreq.end()) {
            keyValFreq[key].first = value;
            updateFreq(key);
        } else {
            if (keyValFreq.size() >= capacity) {
                int evictKey = freqKeys[minFreq].front();
                freqKeys[minFreq].pop_front();
                keyValFreq.erase(evictKey);
                keyIter.erase(evictKey);
            }
            
            keyValFreq[key] = {value, 1};
            freqKeys[1].push_back(key);
            keyIter[key] = --freqKeys[1].end();
            minFreq = 1;
        }
    }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 460 | LFU Cache | [Link](https://leetcode.com/problems/lfu-cache/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-14-hard-460-lfu-cache/) |

## Trie

Prefix tree for efficient string operations.

```cpp
class Trie {
    struct TrieNode {
        vector<TrieNode*> children;
        bool isEnd;
        TrieNode() : children(26, nullptr), isEnd(false) {}
    };
    
    TrieNode* root;
    
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->children[idx]) {
                node->children[idx] = new TrieNode();
            }
            node = node->children[idx];
        }
        node->isEnd = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->children[idx]) return false;
            node = node->children[idx];
        }
        return node->isEnd;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!node->children[idx]) return false;
            node = node->children[idx];
        }
        return true;
    }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 208 | Implement Trie (Prefix Tree) | [Link](https://leetcode.com/problems/implement-trie-prefix-tree/) | - |
| 211 | Design Add and Search Words Data Structure | [Link](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | - |

## Time-based Key-Value Store

```cpp
class TimeMap {
    unordered_map<string, vector<pair<int, string>>> store;
    
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        store[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        if (store.find(key) == store.end()) return "";
        
        auto& pairs = store[key];
        int left = 0, right = pairs.size() - 1;
        string result = "";
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (pairs[mid].first <= timestamp) {
                result = pairs[mid].second;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return result;
    }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 981 | Time Based Key-Value Store | [Link](https://leetcode.com/problems/time-based-key-value-store/) | - |

## Design Patterns

### Random Pick with Weight

```cpp
class Solution {
    vector<int> prefixSum;
public:
    Solution(vector<int>& w) {
        prefixSum.push_back(0);
        for (int weight : w) {
            prefixSum.push_back(prefixSum.back() + weight);
        }
    }
    
    int pickIndex() {
        int target = rand() % prefixSum.back();
        return upper_bound(prefixSum.begin(), prefixSum.end(), target) - prefixSum.begin() - 1;
    }
};
```

### Design Tic-Tac-Toe

```cpp
class TicTacToe {
    vector<int> rows, cols;
    int diagonal, antiDiagonal;
    int n;
    
public:
    TicTacToe(int n) : n(n), rows(n, 0), cols(n, 0), diagonal(0), antiDiagonal(0) {}
    
    int move(int row, int col, int player) {
        int add = (player == 1) ? 1 : -1;
        
        rows[row] += add;
        cols[col] += add;
        
        if (row == col) diagonal += add;
        if (row + col == n - 1) antiDiagonal += add;
        
        if (abs(rows[row]) == n || abs(cols[col]) == n || 
            abs(diagonal) == n || abs(antiDiagonal) == n) {
            return player;
        }
        
        return 0;
    }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 528 | Random Pick with Weight | [Link](https://leetcode.com/problems/random-pick-with-weight/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-528-random-pick-with-weight/) |
| 348 | Design Tic-Tac-Toe | [Link](https://leetcode.com/problems/design-tic-tac-toe/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-348-design-tic-tac-toe/) |
| 398 | Random Pick Index | [Link](https://leetcode.com/problems/random-pick-index/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-398-random-pick-index/) |
| 2043 | Simple Bank System | [Link](https://leetcode.com/problems/simple-bank-system/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-2043-simple-bank-system/) |
| 281 | Zigzag Iterator | [Link](https://leetcode.com/problems/zigzag-iterator/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-10-medium-281-zigzag-iterator/) |
| 1206 | Design Skiplist | [Link](https://leetcode.com/problems/design-skiplist/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-03-hard-1206-design-skiplist/) |

## More templates

- **Data structures (Trie, segment tree):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

