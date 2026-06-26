---
layout: post
title: "Algorithm Templates: Data Structure Design"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates design
permalink: /posts/2025-11-24-leetcode-templates-data-structure-design/
tags: [leetcode, templates, design, data-structures]
---
Data structure design problems are among the most popular interview questions at top tech companies. This page provides complete, tested C++ implementations for LRU/LFU cache, Trie, time-based key-value store, and other classic design patterns. The key insight for most of these problems is combining two or more simple structures to achieve the required time complexity.

> **Design problems test your ability to compose data structures.** The trick is almost always combining a hash map with another structure (linked list, heap, array) to get O(1) for multiple operations.

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="360" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">LRU Cache — hash map + doubly linked list</text>
  <rect x="30" y="40" width="200" height="120" rx="8" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="130" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Hash Map</text>
  <text x="50" y="80" font-size="10" fill="#5A5752">key=1 → node₁</text>
  <text x="50" y="98" font-size="10" fill="#5A5752">key=2 → node₂</text>
  <text x="50" y="116" font-size="10" fill="#5A5752">key=3 → node₃</text>
  <text x="130" y="145" font-size="9" fill="#9A9792" text-anchor="middle">O(1) lookup by key</text>
  <text x="400" y="35" font-size="10" fill="#9A9792">head (oldest)</text>
  <rect x="280" y="45" width="70" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="315" y="64" font-size="12" fill="#9A9792" text-anchor="middle">1</text>
  <line x1="350" y1="61" x2="380" y2="61" stroke="#B8B5B0" marker-end="url(#lru-arr)"/>
  <rect x="380" y="45" width="70" height="32" rx="4" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/><text x="415" y="64" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">2</text>
  <line x1="450" y1="61" x2="480" y2="61" stroke="#B8B5B0"/>
  <rect x="480" y="45" width="70" height="32" rx="4" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="515" y="64" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">3</text>
  <text x="560" y="35" font-size="10" fill="#C08070" font-weight="600">tail (recent)</text>
  <defs><marker id="lru-arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#B8B5B0"/></marker></defs>
  <text x="400" y="100" font-size="10" fill="#5A5752" text-anchor="middle">Doubly linked list — O(1) insert/remove at any position</text>
  <text x="400" y="130" font-size="10" fill="#5A5752" text-anchor="middle">get(3): map lookup → splice node to tail (mark recent)</text>
  <text x="400" y="152" font-size="10" fill="#5A5752" text-anchor="middle">put(4): if full → evict head (oldest), insert at tail</text>
  <text x="400" y="180" font-size="10" fill="#3A6B3A" font-weight="600" text-anchor="middle">Both get and put are O(1)</text>
</svg>

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)

## Contents

- [Stack-based Design](#stack-based-design)
- [LRU Cache](#lru-cache)
- [LFU Cache](#lfu-cache)
- [Trie](#trie)
- [Time-based Key-Value Store](#time-based-key-value-store)
- [Design Patterns](#design-patterns)

## Stack-based Design

**When to use:** "get min/max in O(1)", "design a stack with extra operations", or when you need to track additional state alongside the primary data.

### Min Stack
Maintain a primary stack for data and an auxiliary stack to track the minimum value at each state.

```cpp
class MinStack {
    stack<int> stk, minStk;
public:
    void push(int val) {
        stk.push(val);
        if (minStk.empty()) minStk.push(val);
        else minStk.push(min(minStk.top(), val));
    }
    void pop() { stk.pop(); minStk.pop(); }
    int top() { return stk.top(); }
    int getMin() { return minStk.top(); }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 155 | Min Stack | [Link](https://leetcode.com/problems/min-stack/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/11/medium-155-min-stack/) |

## LRU Cache

**When to use:** "least recently used", "design a cache with O(1) get and put", or any eviction policy based on access recency.

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

**When to use:** "least frequently used", "evict the element used fewest times", or cache designs where frequency matters more than recency.

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

**When to use:** "prefix search", "autocomplete", "word dictionary with wildcards", or any problem requiring efficient prefix lookups over a set of strings.

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

**When to use:** "get value at timestamp", "versioned storage", or when you need to retrieve the most recent value at or before a given time.

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
| 362 | Design Hit Counter | [Link](https://leetcode.com/problems/design-hit-counter/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/18/medium-362-design-hit-counter/) |
| 1146 | Snapshot Array | [Link](https://leetcode.com/problems/snapshot-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/19/medium-1146-snapshot-array/) |

## Design Patterns

**When to use:** "random with weight", "design tic-tac-toe", "iterator", or other custom data structure problems that combine multiple techniques.

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
| 348 | Design Tic-Tac-Toe | [Link](https://leetcode.com/problems/design-tic-tac-toe/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/04/medium-348-design-tic-tac-toe/) |
| 1275 | Find Winner on a Tic Tac Toe Game | [Link](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/04/easy-1275-find-winner-on-a-tic-tac-toe-game/) |
| 398 | Random Pick Index | [Link](https://leetcode.com/problems/random-pick-index/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-398-random-pick-index/) |
| 2043 | Simple Bank System | [Link](https://leetcode.com/problems/simple-bank-system/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-2043-simple-bank-system/) |
| 281 | Zigzag Iterator | [Link](https://leetcode.com/problems/zigzag-iterator/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-10-medium-281-zigzag-iterator/) |
| 1206 | Design Skiplist | [Link](https://leetcode.com/problems/design-skiplist/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-03-hard-1206-design-skiplist/) |
| 341 | Flatten Nested List Iterator | [Link](https://leetcode.com/problems/flatten-nested-list-iterator/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/24/medium-341-flatten-nested-list-iterator/) |
| 1115 | Print FooBar Alternately | [Link](https://leetcode.com/problems/print-foobar-alternately/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/28/medium-1115-print-foobar-alternately/) |
| 1188 | Design Bounded Blocking Queue | [Link](https://leetcode.com/problems/design-bounded-blocking-queue/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/29/medium-1188-design-bounded-blocking-queue/) |

## Summary

| Pattern | Signal Phrases | Structures Used |
|---|---|---|
| Min Stack | "min in O(1)" | Two stacks |
| LRU Cache | "least recently used" | Hash map + doubly linked list |
| LFU Cache | "least frequently used" | Hash map + frequency buckets |
| Trie | "prefix search", "autocomplete" | Tree of character nodes |
| Time-based KV | "get value at timestamp" | Hash map + binary search |

## More templates

- **Data structures (Trie, segment tree):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
