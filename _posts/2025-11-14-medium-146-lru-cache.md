---
layout: post
title: "[Medium] 146. LRU Cache"
date: 2025-11-15 00:00:00 -0800
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

We use a combination of hash map and doubly linked list to achieve O(1) operations. The hash map stores key-to-node mappings, and the doubly linked list maintains the order of recently used items.

### Solution 1: Using list (Recommended - C++20 Optimized)

```cpp
using namespace std;

class LRUCache {
private:
    int capacity_;
    unordered_map<int, list<pair<int, int>>::iterator> cache_;
    list<pair<int, int>> lru_list_;

    // Helper to move node to front (most recently used)
    void moveToFront(list<pair<int, int>>::iterator it) {
        if (it != lru_list_.begin()) {
            lru_list_.splice(lru_list_.begin(), lru_list_, it);
        }
    }

public:
    explicit LRUCache(int capacity) 
        : capacity_(capacity) 
    {
        cache_.reserve(capacity_);  // Pre-allocate hash map
    }

    int get(int key) {
        auto it = cache_.find(key);
        if (it == cache_.end()) {
            return -1;
        }

        // Move to front (most recently used)
        moveToFront(it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = cache_.find(key);
        
        if (it != cache_.end()) {
            // Update existing key
            it->second->second = value;
            moveToFront(it->second);
        } else {
            // Add new key
            if (cache_.size() >= capacity_) {
                // Evict least recently used (back of list)
                auto [lru_key, _] = lru_list_.back();
                cache_.erase(lru_key);
                lru_list_.pop_back();
            }
            
            // Insert at front
            lru_list_.emplace_front(key, value);
            cache_[key] = lru_list_.begin();
        }
    }
};
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

### Solution 2: Custom Doubly Linked List (C++20 Optimized)

```cpp
using namespace std;

class LRUCache {
private:
    struct Node {
        int key;
        int value;
        Node* next;
        Node* prev;
        
        Node(int k, int v) 
            : key(k), value(v), next(nullptr), prev(nullptr) {}
    };

    int capacity_;
    unordered_map<int, Node*> cache_;
    
    // Dummy head and tail for easier list manipulation
    unique_ptr<Node> head_;
    unique_ptr<Node> tail_;

    // Add node right before tail (most recently used)
    void addNode(Node* node) {
        Node* prev_end = tail_->prev;
        prev_end->next = node;
        node->prev = prev_end;
        node->next = tail_.get();
        tail_->prev = node;
    }

    // Remove node from list
    void removeNode(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    // Move node to end (most recently used)
    void moveToEnd(Node* node) {
        removeNode(node);
        addNode(node);
    }

public:
    explicit LRUCache(int capacity) 
        : capacity_(capacity)
        , head_(make_unique<Node>(-1, -1))
        , tail_(make_unique<Node>(-1, -1))
    {
        head_->next = tail_.get();
        tail_->prev = head_.get();
        cache_.reserve(capacity_);
    }

    ~LRUCache() {
        // Clean up nodes
        Node* current = head_->next;
        while (current != tail_.get()) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }

    // Delete copy constructor and assignment
    LRUCache(const LRUCache&) = delete;
    LRUCache& operator=(const LRUCache&) = delete;

    int get(int key) {
        auto it = cache_.find(key);
        if (it == cache_.end()) {
            return -1;
        }

        Node* node = it->second;
        moveToEnd(node);
        return node->value;
    }

    void put(int key, int value) {
        auto it = cache_.find(key);
        
        if (it != cache_.end()) {
            // Update existing
            Node* node = it->second;
            node->value = value;
            moveToEnd(node);
        } else {
            // Add new
            if (cache_.size() >= capacity_) {
                // Evict least recently used (head->next)
                Node* lru = head_->next;
                removeNode(lru);
                cache_.erase(lru->key);
                delete lru;
            }
            
            Node* newNode = new Node(key, value);
            addNode(newNode);
            cache_[key] = newNode;
        }
    }
};
```

### Solution 3: Most Optimized with Move Semantics

```cpp
#include <unordered_map>
#include <list>
#include <utility>

class LRUCache {
private:
    int capacity_;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cache_;
    std::list<std::pair<int, int>> lru_list_;

public:
    explicit LRUCache(int capacity) 
        : capacity_(capacity) 
    {
        cache_.reserve(capacity_);
    }

    [[nodiscard]] int get(int key) {
        const auto it = cache_.find(key);
        if (it == cache_.end()) {
            return -1;
        }

        // Move to front using splice (O(1))
        lru_list_.splice(lru_list_.begin(), lru_list_, it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = cache_.find(key);
        
        if (it != cache_.end()) {
            // Update and move to front
            it->second->second = value;
            lru_list_.splice(lru_list_.begin(), lru_list_, it->second);
        } else {
            // Check capacity
            if (cache_.size() >= capacity_) {
                // Evict LRU (back of list)
                cache_.erase(lru_list_.back().first);
                lru_list_.pop_back();
            }
            
            // Insert at front
            lru_list_.emplace_front(key, value);
            cache_[key] = lru_list_.begin();
        }
    }
};
```
## Key Optimizations (C++20)

1. **`list::splice()`**: O(1) operation to move nodes without copying
2. **`unordered_map::reserve()`**: Pre-allocates hash map to avoid rehashing
3. **`explicit` constructor**: Prevents implicit conversions
4. **Structured bindings**: Cleaner code with `auto [key, value]`
5. **`emplace_front()`**: Constructs in-place, avoiding copies
6. **Move semantics**: Efficient transfer of ownership

### Data Structure Design

```
Hash Map:          Doubly Linked List:
key -> iterator    [head] <-> [1,1] <-> [2,2] <-> [tail]
                   (LRU)                (MRU)
```

### Operation Flow

**Get Operation:**
1. Look up key in hash map → O(1)
2. If found, move node to front (most recently used) → O(1)
3. Return value

**Put Operation:**
1. Look up key in hash map → O(1)
2. If exists: update value and move to front → O(1)
3. If new:
   - Check capacity
   - If full: remove back node (LRU) → O(1)
   - Insert at front → O(1)

### Example Walkthrough

```
capacity = 2

put(1, 1):  cache = {1: [1,1]}
            list: [head] <-> [1,1] <-> [tail]

put(2, 2):  cache = {1: [1,1], 2: [2,2]}
            list: [head] <-> [1,1] <-> [2,2] <-> [tail]

get(1):     Move [1,1] to front
            list: [head] <-> [2,2] <-> [1,1] <-> [tail]
            return 1

put(3, 3):  Evict [2,2] (LRU), add [3,3] at front
            cache = {1: [1,1], 3: [3,3]}
            list: [head] <-> [3,3] <-> [1,1] <-> [tail]
```

## Why std::list is Preferred

1. **`splice()` is O(1)**: Moves nodes without copying
2. **Automatic memory management**: No manual node deletion
3. **Less error-prone**: No pointer management
4. **Better cache locality**: Standard library optimizations
5. **Cleaner code**: Less boilerplate

## Common Mistakes

1. **Capacity = 1**: Only one item can exist
2. **Get non-existent key**: Returns -1
3. **Update existing key**: Moves to front, doesn't increase size
4. **Multiple puts**: Evicts oldest when capacity exceeded

1. **Not moving to front on get**: Must update access order
2. **Wrong eviction order**: Remove from back (LRU), not front
3. **Memory leaks**: Forgetting to delete nodes in custom implementation
4. **Not updating iterator**: After list modification, iterators may be invalid
5. **Copying instead of moving**: Use `splice()` or move semantics

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
