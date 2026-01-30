---
layout: post
title: "[Hard] 1206. Design Skiplist"
date: 2025-12-03 00:00:00 -0800
categories: leetcode algorithm hard cpp data-structures skiplist linked-list problem-solving
---

# [Hard] 1206. Design Skiplist

Design a **Skiplist** without using any built-in libraries.

A **skiplist** is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.

For example, we have a Skiplist containing `[30,40,50,60,70,90]` and we want to add `80` and `45` into it. The Skiplist works this way:

```
Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons
```

You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of the top layers, add, erase and search can be faster than O(n). It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n).

To be specific, your design should include these functions:

- `bool search(int target)`: Return whether the `target` exists in the Skiplist or not.
- `void add(int num)`: Insert a value into the SkipList.
- `bool erase(int num)`: Remove a value from the Skiplist. If `num` does not exist in the Skiplist, do nothing and return false. If there exists multiple `num` values, removing any one of them is fine.

See more about Skiplist: https://en.wikipedia.org/wiki/Skip_list

Notice that duplicates may exist in the Skiplist, your code needs to handle this situation.

## Examples

**Example 1:**
```
Input
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
Output
[null, null, null, null, false, null, true, false, true, false]

Explanation
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // return False.
skiplist.add(4);
skiplist.search(1);   // return True.
skiplist.erase(0);    // return False, 0 is not in skiplist.
skiplist.erase(1);    // return True.
skiplist.search(1);   // return False, 1 has already been erased.
```

## Constraints

- `0 <= num, target <= 20000`
- At most `50000` calls will be made to `search`, `add`, and `erase`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Skiplist definition**: What is a skiplist? (Assumption: A probabilistic data structure with multiple levels, allowing O(log n) search, insert, and delete operations)

2. **Duplicate handling**: Can the skiplist contain duplicate values? (Assumption: Yes - per examples, duplicates may exist, need to handle them)

3. **Operations**: What operations should we support? (Assumption: search(target) - find if target exists, add(num) - insert num, erase(num) - remove one occurrence of num)

4. **Return values**: What should operations return? (Assumption: search returns bool, add returns void, erase returns bool indicating if num was found and removed)

5. **Time complexity**: What time complexity is expected? (Assumption: O(log n) average case for all operations - probabilistic structure)

## Interview Deduction Process (30 minutes)

### Step 1: Brute-Force Approach (8 minutes)
**Initial Thought**: "I need to implement skiplist. Let me use sorted array or linked list."

**Naive Solution**: Use sorted array for search/insert/erase. Binary search for O(log n) search, but insert/erase are O(n).

**Complexity**: O(log n) search, O(n) insert/erase, O(n) space

**Issues**:
- O(n) insert/erase is inefficient
- Doesn't meet O(log n) requirement for all operations
- Array shifting is expensive
- Can be optimized

### Step 2: Semi-Optimized Approach (10 minutes)
**Insight**: "Skiplist uses multiple levels of linked lists with probabilistic promotion."

**Improved Solution**: Implement skiplist with multiple levels. Each node has probability 0.5 to be promoted to next level. Search/insert/erase traverse levels from top to bottom.

**Complexity**: O(log n) average case for all operations, O(n) space

**Improvements**:
- Probabilistic structure enables O(log n) operations
- Multiple levels enable fast search
- Handles all operations efficiently
- More complex than simple structures

### Step 3: Optimized Solution (12 minutes)
**Final Optimization**: "Skiplist implementation with proper level management is optimal."

**Best Solution**: Skiplist with multiple levels. Use coin flip (probability 0.5) to determine node levels. Search/insert/erase traverse from top level down, maintaining proper links.

**Complexity**: O(log n) average case, O(n) space

**Key Realizations**:
1. Probabilistic structure is key to efficiency
2. Multiple levels enable logarithmic operations
3. O(log n) average case is optimal for skiplist
4. Proper level management is crucial

## Solution: Skiplist Implementation

**Time Complexity:** O(log n) average for all operations  
**Space Complexity:** O(n)

A skiplist is a probabilistic data structure that maintains multiple levels of sorted linked lists. Higher levels act as "express lanes" for faster traversal.

```cpp
const int MAX_LEVEL = 32;
const double P_FACTOR = 0.25;

struct SkiplistNode {
    int val_;
    vector<SkiplistNode*> forward_;
    
    SkiplistNode(int val, int maxLevel = MAX_LEVEL) : val_(val), forward_(maxLevel, nullptr) {}
};

class Skiplist {
private:
    SkiplistNode* head_;
    int level_;

    int randomLevel() {
        int level = 1;
        while((rand() / (double)RAND_MAX) < P_FACTOR && level < MAX_LEVEL) {
            level++;
        }
        return level;
    }

public:
    Skiplist(): head_(new SkiplistNode(-1)), level_(0) {
    }
    
    bool search(int target) {
        SkiplistNode* curr = this->head_;
        for(int i = level_ - 1; i >= 0; i--) {
            while(curr->forward_[i] && curr->forward_[i]->val_ < target) {
                curr = curr->forward_[i];
            }
        }
        curr = curr->forward_[0];
        if(curr && curr->val_ == target) {
            return true;
        }
        return false;
    }
    
    void add(int num) {
        vector<SkiplistNode*> update(MAX_LEVEL, head_);
        SkiplistNode* curr = this->head_;
        
        for(int i = level_ - 1; i >= 0; i--) {
            while(curr->forward_[i] && curr->forward_[i]->val_ < num) {
                curr = curr->forward_[i];
            }
            update[i] = curr;
        }
        
        int lv = randomLevel();
        level_ = max(level_, lv);
        SkiplistNode* newNode = new SkiplistNode(num, lv);
        
        for(int i = 0; i < lv; i++) {
            newNode->forward_[i] = update[i]->forward_[i];
            update[i]->forward_[i] = newNode;
        }
    }
    
    bool erase(int num) {
        vector<SkiplistNode*> update(MAX_LEVEL, nullptr);
        SkiplistNode* curr = this->head_;
        
        for(int i = level_ - 1; i >= 0; i--) {
            while(curr->forward_[i] && curr->forward_[i]->val_ < num) {
                curr = curr->forward_[i];
            }
            update[i] = curr;
        }
        
        curr = curr->forward_[0];
        if(!curr || curr->val_ != num) {
            return false;
        }
        
        for(int i = 0; i < level_; i++) {
            if(update[i]->forward_[i] != curr) {
                break;
            }
            update[i]->forward_[i] = curr->forward_[i];
        }
        
        delete curr;
        
        while(level_ > 1 && head_->forward_[level_ - 1] == nullptr) {
            level_--;
        }
        
        return true;
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */
```

## How the Algorithm Works

### Skiplist Structure

A skiplist consists of multiple levels of sorted linked lists:
- **Level 0**: Contains all elements in sorted order
- **Level 1+**: Contains a subset of elements, acting as "express lanes"
- **Head node**: Dummy node with value -1, points to first node at each level

### Key Components

1. **`SkiplistNode`**: Each node contains:
   - `val_`: The value stored
   - `forward_`: Array of pointers to next nodes at each level

2. **`randomLevel()`**: Determines the height of a new node:
   - Starts at level 1
   - With probability `P_FACTOR` (0.25), increases level
   - Maximum level is `MAX_LEVEL` (32)
   - Expected level is approximately 1.33

3. **`level_`**: Current maximum level in the skiplist

### Search Operation

```cpp
bool search(int target) {
    // Start from head at highest level
    // Traverse down levels, moving right while value < target
    // At level 0, check if next node equals target
}
```

**Algorithm:**
1. Start from `head_` at level `level_ - 1`
2. For each level from top to bottom:
   - Move right while next node's value < target
3. At level 0, check if next node equals target

**Time Complexity:** O(log n) average

### Add Operation

```cpp
void add(int num) {
    // Find insertion points at each level
    // Generate random level for new node
    // Insert node and update pointers
}
```

**Algorithm:**
1. **Find update points**: For each level, find the rightmost node with value < num
2. **Generate level**: Use `randomLevel()` to determine new node's height
3. **Update level**: Set `level_ = max(level_, newLevel)`
4. **Insert node**: Create new node and update pointers at each level

**Time Complexity:** O(log n) average

### Erase Operation

```cpp
bool erase(int num) {
    // Find update points at each level
    // Locate node to delete
    // Update pointers to bypass deleted node
    // Decrease level if necessary
}
```

**Algorithm:**
1. **Find update points**: For each level, find the rightmost node with value < num
2. **Locate target**: Check if next node at level 0 equals num
3. **Update pointers**: For each level where node exists, bypass it
4. **Decrease level**: If highest level becomes empty, decrease `level_`
5. **Delete node**: Free memory

**Time Complexity:** O(log n) average

## Example Walkthrough

**Adding elements: [1, 2, 3, 4]**

```
Initial: head -> null (all levels)

add(1):  head -> [1] (level 0, 1)
         Random level = 1

add(2):  head -> [1] -> [2] (level 0)
         head -> [1] -> [2] (level 1, if level 1)
         Random level determines height

add(3):  head -> [1] -> [2] -> [3] (level 0)
         Higher levels may skip some nodes

add(4):  head -> [1] -> [2] -> [3] -> [4] (level 0)
```

**Search operation:**

```
search(3):
Level 2: head -> ... (skip if 3 not at this level)
Level 1: head -> ... -> [2] -> ... (move right while < 3)
Level 0: head -> ... -> [2] -> [3] (found!)
```

## Complexity Analysis

| Operation | Time (Average) | Time (Worst) | Space |
|-----------|---------------|--------------|-------|
| `search(target)` | O(log n) | O(n) | O(1) |
| `add(num)` | O(log n) | O(n) | O(1) |
| `erase(num)` | O(log n) | O(n) | O(1) |
| **Overall** | **O(log n)** | **O(n)** | **O(n)** |

**Note:** Worst case occurs when all nodes are at level 0 (degenerates to linked list), but probability is extremely low.

## Key Design Choices

1. **`MAX_LEVEL = 32`**: Maximum height of any node
   - For 2^32 elements, expected height is ~32
   - Provides good balance between space and time

2. **`P_FACTOR = 0.25`**: Probability of increasing level
   - Lower values = fewer high-level nodes = less space
   - Standard value is 0.5, but 0.25 works well

3. **Head node with value -1**: Sentinel node simplifies edge cases
   - Always exists, never deleted
   - Points to first real node at each level

4. **Dynamic level management**: `level_` tracks current maximum
   - Increases when adding high-level nodes
   - Decreases when erasing removes highest level

## Edge Cases

1. **Empty skiplist**: `level_ = 0`, all `forward_` pointers are null
2. **Duplicate values**: Multiple nodes can have same value
3. **Erase non-existent**: Returns false, no changes
4. **Single element**: Works correctly with one node
5. **All same values**: Handles multiple nodes with same value

## Common Mistakes

1. **Not updating `level_`**: Must track current maximum level
2. **Wrong update array initialization**: Should initialize to `head_` for `add()`
3. **Not decreasing `level_`**: After erase, check if highest level is empty
4. **Memory leaks**: Must `delete` erased nodes
5. **Index out of bounds**: Check `update[i]->forward_[i]` before accessing

## Why Skiplist?

### Advantages:
- **Simple implementation**: Easier than balanced trees
- **Probabilistic balance**: No complex rebalancing needed
- **Cache friendly**: Better than trees for sequential access
- **Concurrent operations**: Easier to make thread-safe

### Disadvantages:
- **Space overhead**: Each node stores multiple pointers
- **Worst case O(n)**: Can degenerate (very unlikely)
- **Random number generation**: Requires good RNG

## Related Problems

- [432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) - Complex data structure design
- [146. LRU Cache](https://leetcode.com/problems/lru-cache/) - Cache design
- [460. LFU Cache](https://leetcode.com/problems/lfu-cache/) - Frequency-based cache
- [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) - Randomized data structure

## Pattern Recognition

This problem demonstrates the **"Probabilistic Data Structure"** pattern:

```
1. Use randomization to achieve balance
2. Multiple levels for faster traversal
3. Maintain sorted order at each level
4. Trade space for time complexity
```

Similar concepts:
- Bloom filters (probabilistic membership)
- Treap (randomized BST)
- Skip lists (this problem)

