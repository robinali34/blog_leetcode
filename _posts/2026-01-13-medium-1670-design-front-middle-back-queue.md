---
layout: post
title: "[Medium] 1670. Design Front Middle Back Queue"
date: 2026-01-13 00:00:00 -0700
categories: [leetcode, medium, design, deque, data-structure]
permalink: /2026/01/13/medium-1670-design-front-middle-back-queue/
tags: [leetcode, medium, design, deque, data-structure, two-deques]
---
Design a queue that supports `push` and `pop` operations in the **front**, **middle**, and **back**.

Implement the `FrontMiddleBackQueue` class:

- `FrontMiddleBackQueue()` Initializes the queue.
- `void pushFront(int val)` Adds `val` to the **front** of the queue.
- `void pushMiddle(int val)` Adds `val` to the **middle** of the queue.
- `void pushBack(int val)` Adds `val` to the **back** of the queue.
- `int popFront()` Removes the **front** element of the queue and returns it. If the queue is empty, return `-1`.
- `int popMiddle()` Removes the **middle** element of the queue and returns it. If the queue is empty, return `-1`.
- `int popBack()` Removes the **back** element of the queue and returns it. If the queue is empty, return `-1`.

**Notice** that when there are **two** middle position choices, the operation is performed on the **frontmost** middle position choice. For example:

- Pushing `6` into the middle of `[1, 2, 3, 4, 5]` results in `[1, 2, 6, 3, 4, 5]`.
- Popping the middle from `[1, 2, 3, 4, 5, 6]` returns `3` and results in `[1, 2, 4, 5, 6]`.

## Examples

**Example 1:**
```
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
```

## Constraints

- `1 <= val <= 10^9`
- At most `1000` calls will be made to `pushFront`, `pushMiddle`, `pushBack`, `popFront`, `popMiddle`, and `popBack`.

## Thinking Process

1. **Two Deques Pattern**: Split queue into two halves for efficient middle access

- Identify required operations and their frequency (get/put/insert).
- Combine data structures: hash map + list, heap + map, trie + DFS.
- Amortized O(1) often needs lazy cleanup or doubly-linked lists.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Design pattern</text>

  <rect x="40" y="45" width="70" height="36" rx="4" fill="#D4D8E0" stroke="#8B8680"/><text x="75" y="67" text-anchor="middle" font-size="10">API</text>
  <rect x="150" y="45" width="90" height="36" rx="4" fill="#E0D8E4" stroke="#A098A8"/><text x="195" y="67" text-anchor="middle" font-size="10">hash + list</text>
  <path d="M110 63h36" stroke="#8B8680" stroke-width="2" marker-end="url(#arr2)"/>
  <defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>
  <text x="140" y="105" text-anchor="middle" font-size="11" fill="#6B6560">compose data structures for operations</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Hash map + list** *(this problem)* | O(1) avg | O(n) | LRU cache pattern |
| Heap + hash map | O(log n) | O(n) | LFU, time-based store |
| Trie (prefix tree) | O(m) | O(nm) | Word search, autocomplete |
| Deque / circular buffer | O(1) | O(n) | Queue with fixed capacity |

## Solution

### **Solution: Two Deques with Rebalancing**

```cpp
class FrontMiddleBackQueue {
public:
    FrontMiddleBackQueue() {
        
    }
    
    void pushFront(int val) {
        front_cache.push_front(val);
        rebalance();
    }
    
    void pushMiddle(int val) {        
        front_cache.push_back(val);
        rebalance();
    }
    
    void pushBack(int val) {
        back_cache.push_back(val);
        rebalance();
    }
    
    int popFront() {
        if(front_cache.empty() && back_cache.empty())  return -1;
        int rtn;
        if(front_cache.empty()) {
            rtn = back_cache.front();
            back_cache.pop_front();
        } else {
            rtn = front_cache.front();
            front_cache.pop_front();
            rebalance();
        }
        return rtn;
    }
    
    int popMiddle() {
        if(front_cache.empty() && back_cache.empty())  return -1;
        int rtn;
        if(front_cache.size() == back_cache.size()) {
            rtn = front_cache.back();
            front_cache.pop_back();
        } else {
            rtn = back_cache.front();
            back_cache.pop_front();
        }
        return rtn;
    }
    
    int popBack() {
        if(front_cache.empty() && back_cache.empty())  return -1;
        int rtn = back_cache.back();
        back_cache.pop_back();
        rebalance();
        return rtn;
    }
private:
    deque<int> front_cache, back_cache;

    void rebalance() {
        while(front_cache.size() > back_cache.size()) {
            back_cache.push_front(front_cache.back());
            front_cache.pop_back();
        }
        while(back_cache.size() > front_cache.size() + 1) {
            front_cache.push_back(back_cache.front());
            back_cache.pop_front();
        }
    }
};
```

### Solution Explanation

**Approach:** Hash map + list (this problem)

**Key idea:** 1. **Two Deques Pattern**: Split queue into two halves for efficient middle access

**How the code works:**
1. **Two Deques Pattern**: Split queue into two halves for efficient middle access
- Identify required operations and their frequency (get/put/insert).
- Combine data structures: hash map + list, heap + map, trie + DFS.
- Amortized O(1) often needs lazy cleanup or doubly-linked lists.

**Walkthrough** — input `["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]`, expected output `[null, null, null, null, null, 1, 3, 4, 2, -1]`:

FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)

### **Algorithm Explanation:**

1. **pushFront (Lines 7-10)**:
   - Add `val` to front of `front_cache`
   - Rebalance to maintain invariant

2. **pushMiddle (Lines 12-15)**:
   - Add `val` to back of `front_cache` (becomes new middle)
   - Rebalance to maintain invariant

3. **pushBack (Lines 17-20)**:
   - Add `val` to back of `back_cache`
   - Rebalance to maintain invariant

4. **popFront (Lines 22-33)**:
   - If both empty, return `-1`
   - If `front_cache` empty, pop from `back_cache`
   - Otherwise, pop from `front_cache` and rebalance

5. **popMiddle (Lines 35-45)**:
   - If both empty, return `-1`
   - If sizes equal: pop from `front_cache.back()`
   - Otherwise: pop from `back_cache.front()`
   - No rebalance needed (sizes become balanced after removal)

6. **popBack (Lines 47-53)**:
   - If both empty, return `-1`
   - Pop from `back_cache.back()`
   - Rebalance to maintain invariant

7. **rebalance (Lines 57-65)**:
   - **First loop**: If `front_cache.size() > back_cache.size()`, move last element from `front_cache` to front of `back_cache`
   - **Second loop**: If `back_cache.size() > front_cache.size() + 1`, move first element from `back_cache` to back of `front_cache`
   - Maintains: `front_cache.size() <= back_cache.size() <= front_cache.size() + 1`

### **Why This Works:**

- **Two Deques**: Split queue into two halves for efficient middle access
- **Balance Invariant**: Ensures middle element is always accessible in O(1)
- **Rebalancing**: Maintains invariant after each modification
- **Middle Definition**: When sizes equal, middle is `front_cache.back()`; when `back_cache` is larger, middle is `back_cache.front()`

### **Example Walkthrough:**

**Operations:** `pushFront(1)`, `pushBack(2)`, `pushMiddle(3)`, `pushMiddle(4)`, `popFront()`, `popMiddle()`, `popMiddle()`, `popBack()`

```
Initial: front_cache = [], back_cache = []

pushFront(1):
  front_cache = [1], back_cache = []
  Rebalance: sizes equal (1, 0) → move 1 to back_cache
  front_cache = [], back_cache = [1]

pushBack(2):
  front_cache = [], back_cache = [1, 2]
  Rebalance: back_cache too large (0, 2) → move 1 to front_cache
  front_cache = [1], back_cache = [2]

pushMiddle(3):
  front_cache = [1, 3], back_cache = [2]
  Rebalance: sizes equal (2, 1) → OK
  front_cache = [1, 3], back_cache = [2]

pushMiddle(4):
  front_cache = [1, 3, 4], back_cache = [2]
  Rebalance: front_cache too large (3, 1) → move 4 to back_cache
  front_cache = [1, 3], back_cache = [4, 2]

State: front_cache = [1, 3], back_cache = [4, 2]
Queue: [1, 3, 4, 2]

popFront():
  front_cache not empty → pop 1
  front_cache = [3], back_cache = [4, 2]
  Rebalance: back_cache too large (1, 2) → move 4 to front_cache
  front_cache = [3, 4], back_cache = [2]
  Return: 1

popMiddle():
  Sizes: front_cache.size()=2, back_cache.size()=1
  Sizes equal → pop from front_cache.back() = 4
  front_cache = [3], back_cache = [2]
  Return: 4

popMiddle():
  Sizes: front_cache.size()=1, back_cache.size()=1
  Sizes equal → pop from front_cache.back() = 3
  front_cache = [], back_cache = [2]
  Return: 3

popBack():
  Pop from back_cache.back() = 2
  front_cache = [], back_cache = []
  Rebalance: OK
  Return: 2
```

### **Complexity Analysis:**

- **Time Complexity:** O(1) amortized per operation
  - Deque operations (push/pop front/back) are O(1)
  - Rebalancing is O(1) amortized (each element moved at most once)
- **Space Complexity:** O(n) where n is number of elements in queue
  - Two deques store all elements
## Common Mistakes

1. **Empty queue**: All pop operations return `-1`
2. **Single element**: After one push, one pop returns that element
3. **Two elements**: Middle is the first element (frontmost middle)
4. **Many operations**: Rebalancing maintains efficiency
5. **Alternating operations**: Balance maintained correctly

1. **Wrong middle calculation**: Not handling the case when sizes are equal vs unequal
2. **Missing rebalance**: Forgetting to rebalance after push/pop operations
3. **Wrong rebalance logic**: Incorrectly moving elements between deques
4. **Empty check**: Not checking if both deques are empty before popping
5. **Pop from wrong deque**: Popping from `front_cache` when it's empty in `popFront()`

## Related Problems

- [LC 641: Design Circular Deque](https://www.leetcode.com/problems/design-circular-deque/) - Design a circular deque
- [LC 622: Design Circular Queue](https://www.leetcode.com/problems/design-circular-queue/) - Design a circular queue
- [LC 232: Implement Queue using Stacks](https://www.leetcode.com/problems/implement-queue-using-stacks/) - Queue with stacks
- [LC 225: Implement Stack using Queues](https://www.leetcode.com/problems/implement-stack-using-queues/) - Stack with queues

## Key Takeaways

1. **Two Deques Pattern**: Split queue into two halves for efficient middle access
2. **Balance Invariant**: `front_cache.size() <= back_cache.size() <= front_cache.size() + 1`
3. **Middle Element**: Always accessible in O(1) due to invariant
4. **Rebalancing**: Maintains invariant after each modification
5. **Push Middle**: Add to end of `front_cache` (becomes new middle)

## References

- [LC 1670: Design Front Middle Back Queue on LeetCode](https://www.leetcode.com/problems/design-front-middle-back-queue/)
- [LeetCode Discuss — LC 1670: Design Front Middle Back Queue](https://www.leetcode.com/problems/design-front-middle-back-queue/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/design-front-middle-back-queue/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
