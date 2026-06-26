---
layout: post
title: "[Hard] 460. LFU Cache"
date: 2025-11-14 00:00:00 -0800
categories: leetcode algorithm hard cpp design data-structures hash-map linked-list problem-solving
---
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

## Thinking Process

Design and implement a data structure for a **Least Frequently Used (LFU)** cache.

Implement the `LFUCache` class:

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

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** Design and implement a data structure for a **Least Frequently Used (LFU)** cache.

**How the code works:**
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.
## Why This Design Works

1. **Frequency Lists**: Each frequency has its own list, maintaining LRU order
2. **Min Frequency Tracking**: Always know which frequency to evict from
3. **Iterator Storage**: O(1) access to nodes for removal
4. **Tie Breaking**: Front of list = least recently used (LRU)

## Common Mistakes

1. **Capacity = 0 or 1**: Handle empty cache
2. **Get non-existent key**: Returns -1
3. **Update existing key**: Promotes frequency, doesn't increase size
4. **Tie in frequency**: Evict least recently used (front of list)
5. **All keys have same frequency**: Use LRU order

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

## Key Takeaways

- **Pattern:** Iterative pointer walk (this problem)
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.

## References

- [LC 460: LFU Cache on LeetCode](https://www.leetcode.com/problems/lfu-cache/)
- [LeetCode Discuss — LC 460: LFU Cache](https://www.leetcode.com/problems/lfu-cache/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/lfu-cache/editorial/) *(may require premium)*

## Related Problems

- [146. LRU Cache](https://www.leetcode.com/problems/lru-cache/) - Least Recently Used
- [432. All O`one Data Structure](https://www.leetcode.com/problems/all-oone-data-structure/)
- [588. Design In-Memory File System](https://www.leetcode.com/problems/design-in-memory-file-system/)
