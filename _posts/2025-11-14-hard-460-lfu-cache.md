---
layout: post
title: "[Hard] 460. LFU Cache"
date: 2025-11-14 00:00:00 -0800
categories: leetcode algorithm hard cpp design data-structures hash-map linked-list problem-solving
---

# [Hard] 460. LFU Cache

Design and implement a data structure for a **Least Frequently Used (LFU)** cache.

Implement the `LFUCache` class:

- `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
- `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
- `void put(int key, int value)` Update or insert the value. If the `key` already exists, update the value. If the key does not exist, insert the key-value pair. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** key would be invalidated.

To determine the least frequently used key, a **use counter** is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to `1` (due to the `put` operation). The use counter for a key in the cache is incremented either a `get` or `put` operation is called on it.

The functions `get` and `put` must each run in **O(1)** average time complexity.

## Examples

**Example 1:**
```
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the key-value pairs in the order they were inserted.

LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
```

## Constraints

- `1 <= capacity <= 10^4`
- `0 <= key <= 10^5`
- `0 <= value <= 10^9`
- At most `2 * 10^5` calls will be made to `get` and `put`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **LFU definition**: What does "Least Frequently Used" mean? (Assumption: The item that has been accessed the fewest times - need to track access frequency)

2. **Cache operations**: What operations should the cache support? (Assumption: get(key) - retrieve value, put(key, value) - insert/update, both operations update frequency)

3. **Eviction policy**: When should we evict items? (Assumption: When cache is full and we need to add a new item, evict the least frequently used item, tie-break by least recently used)

4. **Capacity**: What is the cache capacity? (Assumption: Fixed capacity specified in constructor - cannot exceed this limit)

5. **Return values**: What should get() return if key doesn't exist? (Assumption: Return -1 - key not found in cache)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

Use a hash map to store key-value pairs and a separate hash map to track access frequencies. For eviction, scan all entries to find the one with minimum frequency, and if there are ties, find the least recently used among them. This requires O(n) time for eviction, which doesn't meet the O(1) requirement. The challenge is efficiently finding the minimum frequency and handling ties.

**Step 2: Semi-Optimized Approach (10 minutes)**

Maintain a min-heap (priority queue) keyed by frequency, with a secondary timestamp for tie-breaking. However, updating frequencies requires removing and re-inserting elements in the heap, which is O(log n). Additionally, finding and removing arbitrary elements from a heap is inefficient. Alternatively, maintain separate lists for each frequency level (like LFU buckets), but updating frequencies still requires moving nodes between lists, which can be complex.

**Step 3: Optimized Solution (12 minutes)**

Use a hash map storing key → (value, frequency, iterator) and maintain a map of frequency → doubly linked list of keys. Each frequency level has its own list maintaining LRU order. When accessing a key, remove it from its current frequency list and add it to the (frequency+1) list. For eviction, find the minimum frequency (tracked separately), remove the LRU node from that frequency's list. This achieves O(1) operations: hash map lookup O(1), list removal O(1), list insertion O(1). The key insight is combining frequency-based organization with LRU ordering within each frequency level.

## Solution: Hash Map + Frequency Lists (C++20 Optimized)

**Time Complexity:** O(1) for both `get` and `put`  
**Space Complexity:** O(capacity)

We use two hash maps:
1. `frequencies`: Maps frequency → list of (key, value) pairs (ordered by recency)
2. `cache`: Maps key → (frequency, iterator) pair

When there's a tie in frequency, we use the least recently used key (front of the list).

### Solution: Optimized C++20 Version

```cpp
using namespace std;

class LFUCache {
private:
    // frequency -> list of (key, value) pairs (most recent at back)
    unordered_map<int, list<pair<int, int>>> frequencies_;
    
    // key -> (frequency, iterator to node in frequencies list)
    unordered_map<int, pair<int, list<pair<int, int>>::iterator>> cache_;
    
    int capacity_;
    int min_frequency_;

    // Insert key-value pair with given frequency
    void insert(int key, int frequency, int value) {
        frequencies_[frequency].emplace_back(key, value);
        cache_[key] = {frequency, --frequencies_[frequency].end()};
    }

    // Remove key from its current frequency list
    void removeFromFrequency(int frequency, list<pair<int, int>>::iterator it) {
        frequencies_[frequency].erase(it);
        if (frequencies_[frequency].empty()) {
            frequencies_.erase(frequency);
            if (min_frequency_ == frequency) {
                min_frequency_++;
            }
        }
    }

public:
    explicit LFUCache(int capacity) 
        : capacity_(capacity)
        , min_frequency_(0)
    {
        cache_.reserve(capacity_);
        frequencies_.reserve(capacity_);
    }

    int get(int key) {
        auto it = cache_.find(key);
        if (it == cache_.end()) {
            return -1;
        }

        // Get current frequency and iterator
        auto& [freq, iter] = it->second;
        auto [key_val, value] = *iter;

        // Remove from current frequency list
        removeFromFrequency(freq, iter);

        // Insert with incremented frequency
        insert(key, freq + 1, value);

        return value;
    }

    void put(int key, int value) {
        if (capacity_ <= 0) {
            return;
        }

        auto it = cache_.find(key);
        
        if (it != cache_.end()) {
            // Update existing key
            it->second.second->second = value;  // Update value in place
            get(key);  // Increment frequency by calling get
            return;
        }

        // Check capacity
        if (cache_.size() >= capacity_) {
            // Evict least frequently used (and least recently used if tie)
            // min_frequency_ list's front is the LRU item
            auto [lfu_key, _] = frequencies_[min_frequency_].front();
            cache_.erase(lfu_key);
            frequencies_[min_frequency_].pop_front();
            
            if (frequencies_[min_frequency_].empty()) {
                frequencies_.erase(min_frequency_);
            }
        }

        // Insert new key with frequency 1
        min_frequency_ = 1;
        insert(key, 1, value);
    }
};
```

### Alternative: More Explicit Version

```cpp
using namespace std;

class LFUCache {
private:
    struct Node {
        int key;
        int value;
        int frequency;
    };

    // frequency -> list of nodes (most recent at back)
    unordered_map<int, list<Node>> freq_lists_;
    
    // key -> iterator in frequency list
    unordered_map<int, list<Node>::iterator> cache_;
    
    int capacity_;
    int min_freq_;

    void promote(int key) {
        auto& node = *cache_[key];
        int old_freq = node.frequency;
        int new_freq = old_freq + 1;

        // Remove from old frequency list
        freq_lists_[old_freq].erase(cache_[key]);
        if (freq_lists_[old_freq].empty()) {
            freq_lists_.erase(old_freq);
            if (min_freq_ == old_freq) {
                min_freq_++;
            }
        }

        // Add to new frequency list
        freq_lists_[new_freq].emplace_back(node);
        cache_[key] = --freq_lists_[new_freq].end();
        cache_[key]->frequency = new_freq;
    }

public:
    explicit LFUCache(int capacity) 
        : capacity_(capacity)
        , min_freq_(0)
    {
        cache_.reserve(capacity_);
        freq_lists_.reserve(capacity_);
    }

    int get(int key) {
        auto it = cache_.find(key);
        if (it == cache_.end()) {
            return -1;
        }

        promote(key);
        return cache_[key]->value;
    }

    void put(int key, int value) {
        if (capacity_ <= 0) return;

        auto it = cache_.find(key);
        
        if (it != cache_.end()) {
            // Update existing
            it->second->value = value;
            promote(key);
            return;
        }

        // Evict if needed
        if (cache_.size() >= capacity_) {
            auto& lfu_list = freq_lists_[min_freq_];
            int lfu_key = lfu_list.front().key;
            cache_.erase(lfu_key);
            lfu_list.pop_front();
            
            if (lfu_list.empty()) {
                freq_lists_.erase(min_freq_);
            }
        }

        // Insert new
        min_freq_ = 1;
        freq_lists_[1].emplace_back(Node{key, value, 1});
        cache_[key] = --freq_lists_[1].end();
    }
};
```

## Key Optimizations (C++20)

1. **`unordered_map::reserve()`**: Pre-allocates hash maps to avoid rehashing
2. **`explicit` constructor**: Prevents implicit conversions
3. **Structured bindings**: Cleaner code with `auto [key, value]`
4. **`emplace_back()`**: Constructs in-place, avoiding copies
6. **Efficient list operations**: O(1) insertion and removal
7. **Min frequency tracking**: O(1) access to least frequently used items

## How the Algorithm Works

### Data Structure Design

```
frequencies:          cache:
1 -> [2,2] -> [3,3]   1 -> (2, iter1)
2 -> [1,1]            2 -> (1, iter2)
                      3 -> (1, iter3)

min_frequency = 1
```

### Operation Flow

**Get Operation:**
1. Look up key in `cache` → O(1)
2. If found:
   - Get current frequency and iterator
   - Remove from current frequency list
   - Insert into frequency+1 list
   - Update `min_frequency` if needed
3. Return value

**Put Operation:**
1. If key exists: update value and promote (call get)
2. If new:
   - Check capacity
   - If full: evict from `min_frequency` list (front = LRU)
   - Insert with frequency 1
   - Set `min_frequency = 1`

### Example Walkthrough

```
capacity = 2

put(1, 1):  freq=1: [1,1]
            cache: {1: (1, iter1)}
            min_freq = 1

put(2, 2):  freq=1: [1,1] -> [2,2]
            cache: {1: (1, iter1), 2: (1, iter2)}
            min_freq = 1

get(1):     Remove 1 from freq=1, add to freq=2
            freq=1: [2,2]
            freq=2: [1,1]
            cache: {1: (2, iter1_new), 2: (1, iter2)}
            min_freq = 1
            return 1

put(3, 3):  Evict 2 (min_freq=1, front of list)
            freq=1: [3,3]
            freq=2: [1,1]
            cache: {1: (2, iter1), 3: (1, iter3)}
            min_freq = 1
```

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| `get(key)` | O(1) | O(1) |
| `put(key, value)` | O(1) | O(1) |
| **Overall** | **O(1)** | **O(capacity)** |

## Why This Design Works

1. **Frequency Lists**: Each frequency has its own list, maintaining LRU order
2. **Min Frequency Tracking**: Always know which frequency to evict from
3. **Iterator Storage**: O(1) access to nodes for removal
4. **Tie Breaking**: Front of list = least recently used (LRU)

## Edge Cases

1. **Capacity = 0 or 1**: Handle empty cache
2. **Get non-existent key**: Returns -1
3. **Update existing key**: Promotes frequency, doesn't increase size
4. **Tie in frequency**: Evict least recently used (front of list)
5. **All keys have same frequency**: Use LRU order

## Common Mistakes

1. **Not updating min_frequency**: Must track minimum frequency correctly
2. **Wrong eviction order**: Evict from front of min_frequency list (LRU)
3. **Not handling empty frequency lists**: Remove empty lists and update min_frequency
4. **Iterator invalidation**: Be careful when modifying lists
5. **Forgetting to promote on put update**: Must increment frequency when updating existing key

## Comparison: LRU vs LFU

| Aspect | LRU Cache | LFU Cache |
|--------|-----------|-----------|
| **Eviction Policy** | Least Recently Used | Least Frequently Used |
| **Tie Breaking** | N/A (single order) | Least Recently Used |
| **Complexity** | O(1) | O(1) |
| **Use Case** | Temporal locality | Frequency-based access |

## Related Problems

- [146. LRU Cache](https://leetcode.com/problems/lru-cache/) - Least Recently Used
- [432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/)
- [588. Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/)

