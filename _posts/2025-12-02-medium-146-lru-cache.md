---
layout: post
title: "[Medium] 146. LRU Cache"
date: 2025-12-02 00:00:00 -0800
categories: leetcode algorithm medium cpp design data-structures hash-map linked-list problem-solving
---
Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in **O(1)** average time complexity.

## Examples

**Example 1:**
```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`.

## Thinking Process

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Linked list: pointer walk</text>

  <rect x="30" y="50" width="44" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="52" y="68" text-anchor="middle" font-size="12">1</text>
  <path d="M74 66h16" stroke="#8B8680" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="90" y="50" width="44" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="112" y="68" text-anchor="middle" font-size="12">2</text>
  <path d="M134 66h16" stroke="#8B8680" stroke-width="2"/>
  <rect x="150" y="50" width="44" height="32" rx="4" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="172" y="68" text-anchor="middle" font-size="12">3</text>
  <text x="130" y="105" text-anchor="middle" font-size="11" fill="#6B6560">slow → → fast (2x speed)</text>
  <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Iterative pointer walk** *(this problem)* | O(n) | O(1) | Traversal, insertion |
| Dummy head node | O(n) | O(1) | Simplify head-edge cases |
| Reversal (3-pointer) | O(n) | O(1) | Reverse sublist or full list |
| Slow/fast pointers | O(n) | O(1) | Middle, cycle, merge lists |

## Solution

**Time Complexity:** O(1) for both `get` and `put`  
**Space Complexity:** O(capacity)

We use a combination of hash map and doubly linked list to achieve O(1) operations. The hash map stores key-to-iterator mappings, and the doubly linked list maintains the order of recently used items.

### Solution: Using std::list with splice

```cpp
#include <list>
#include <unordered_map>

class LRUCache {
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
        if(hashMap_.size() >= capacity_) {
            int removeKey = keyList_.front();
            keyList_.pop_front();
            hashMap_.erase(removeKey);
        }
        keyList_.push_back(key);
        hashMap_[key] = {value, --keyList_.end()};
    }

private:
    int capacity_;
    list<int> keyList_;
    unordered_map<int, pair<int, list<int>::iterator>> hashMap_;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

**How the code works:**
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.

| Operation | Time | Space |
|-----------|------|-------|
| `get(key)` | O(1) | O(1) |
| `put(key, value)` | O(1) | O(1) |
| **Overall** | **O(1)** | **O(capacity)** |
## Thread-Safe LRU Cache

Thread-safe version using mutex for concurrent access.

```cpp
#include <list>
#include <unordered_map>
#include <mutex>
#include <shared_mutex>

class ThreadSafeLRUCache {
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
        auto it = hashMap_.find(key);
        if(it != hashMap_.end()) {
            // Key exists, update value and move to end
            hashMap_[key].first = value;
            keyList_.splice(keyList_.end(), keyList_, it->second.second);
            return;
        }
        if(hashMap_.size() >= capacity_) {
            int removeKey = keyList_.front();
            keyList_.pop_front();
            hashMap_.erase(removeKey);
        }
        keyList_.push_back(key);
        hashMap_[key] = {value, --keyList_.end()};
    }
    
    size_t size() const {
        shared_lock<shared_mutex> lock(mtx_);
        return hashMap_.size();
    }

private:
    int capacity_;
    list<int> keyList_;
    unordered_map<int, pair<int, list<int>::iterator>> hashMap_;
    mutable shared_mutex mtx_; // Use shared_mutex for read-write lock
};

// Example usage:
// ThreadSafeLRUCache cache(2);
// cache.put(1, 1);
// cache.put(2, 2);
// int val = cache.get(1); // returns 1
// cache.put(3, 3); // evicts key 2
```

### Thread-Safe Implementation Details

1. **`shared_mutex`**: Allows multiple concurrent reads when no writes are happening
2. **`unique_lock<shared_mutex>`**: Exclusive lock for both `get()` and `put()` since they modify the list
3. **`shared_lock<shared_mutex>`**: Shared lock for read-only operations like `size()`
4. **Note**: The thread-safe `put()` calls `get()` which requires careful lock management - both methods use exclusive locks

### Solution Explanation
### Data Structure Design

```
Hash Map:                    Doubly Linked List:
key -> (value, iterator)      [1] <-> [2] <-> [3]
                              (LRU)            (MRU)
```

### Operation Flow

**Get Operation:**
1. Look up key in hash map → O(1)
2. If found, move node to end (most recently used) using `splice()` → O(1)
3. Return value

**Put Operation:**
1. Check if key exists via `get()` → O(1)
2. If exists: update value (already moved to end by `get()`) → O(1)
3. If new:
   - Check capacity
   - If full: remove front node (LRU) → O(1)
   - Insert at end → O(1)

### Example Walkthrough

```
capacity = 2

put(1, 1):  cache = {1: (1, it1)}
            list: [1]

put(2, 2):  cache = {1: (1, it1), 2: (2, it2)}
            list: [1] <-> [2]

get(1):     Move 1 to end using splice
            list: [2] <-> [1]
            return 1

put(3, 3):  get(3) returns -1, capacity full
            Remove front (key 2), insert 3 at end
            cache = {1: (1, it1), 3: (3, it3)}
            list: [1] <-> [3]
```

### Complexity
| Operation | Time | Space |
|-----------|------|-------|
| `get(key)` | O(1) | O(1) |
| `put(key, value)` | O(1) | O(1) |
| **Overall** | **O(1)** | **O(capacity)** |

## Why This Approach Works

1. **Hash map**: Provides O(1) lookup by key
2. **Doubly linked list**: Maintains insertion order and allows O(1) removal/insertion
3. **Iterator storage**: Hash map stores iterators to list nodes for O(1) access
4. **`splice()` optimization**: Moves nodes without copying, maintaining O(1) complexity

## Common Mistakes

1. **Capacity = 1**: Only one item can exist
2. **Get non-existent key**: Returns -1
3. **Update existing key**: Moves to end, doesn't increase size
4. **Multiple puts**: Evicts oldest when capacity exceeded

1. **Not moving to end on get**: Must update access order
2. **Wrong eviction order**: Remove from front (LRU), not back
3. **Invalid iterator after modification**: Use `splice()` which preserves iterators
4. **Not handling existing key in put**: Must check and update, not just insert

## Key Takeaways

- **Pattern:** Iterative pointer walk (this problem)
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.

## References

- [LC 146: LRU Cache on LeetCode](https://www.leetcode.com/problems/lru-cache/)
- [LeetCode Discuss — LC 146: LRU Cache](https://www.leetcode.com/problems/lru-cache/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/lru-cache/editorial/) *(may require premium)*

## Related Problems

- [460. LFU Cache](https://www.leetcode.com/problems/lfu-cache/) - Least Frequently Used
- [432. All O`one Data Structure](https://www.leetcode.com/problems/all-oone-data-structure/)
- [588. Design In-Memory File System](https://www.leetcode.com/problems/design-in-memory-file-system/)
