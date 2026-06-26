---
layout: post
title: "[Medium] 622. Design Circular Queue"
date: 2026-01-24 00:00:00 -0700
categories: [leetcode, medium, array, linked-list, design, queue]
permalink: /2026/01/24/medium-622-design-circular-queue/
tags: [leetcode, medium, array, linked-list, design, queue, circular-queue, data-structure]
---
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the `MyCircularQueue` class:

- `MyCircularQueue(int k)` Initializes the object with the size of the queue to be `k`.
- `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful.
- `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful.
- `int Front()` Gets the front item from the queue. If the queue is empty, return `-1`.
- `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`.
- `boolean isEmpty()` Checks whether the circular queue is empty or not.
- `boolean isFull()` Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language.

## Examples

**Example 1:**

```
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False (queue is full)
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
```

## Constraints

- `1 <= k <= 1000`
- `0 <= value <= 1000`
- At most `3000` calls will be made to `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.

## Thinking Process

1. **Circular Array Approach**:
- Uses modulo arithmetic for wrapping: `(index + 1) % cap`
- Tracks `size` to distinguish empty vs full
- More memory efficient (fixed array)

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

```cpp
class MyCircularQueue {
public:
    MyCircularQueue(int k) : q(k), head(0), tail(0), size(0), cap(k) {
        
    }
    
    bool enQueue(int value) {
        if(isFull()) return false;
        q[tail] = value;
        tail = (tail + 1) % cap;
        size++;
        return true;
    }
    
    bool deQueue() {
        if(isEmpty()) return false;
        head = (head + 1) % cap;
        size--;
        return true;
    }
    
    int Front() {
        return isEmpty() ? -1 : q[head];
    }
    
    int Rear() {
        return isEmpty()? -1 : q[(tail - 1 + cap) % cap];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == cap;
    }

private:
    vector<int> q;
    int head, tail, size, cap;
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** 1. **Circular Array Approach**:

**How the code works:**
1. **Circular Array Approach**:
- Uses modulo arithmetic for wrapping: `(index + 1) % cap`
- Tracks `size` to distinguish empty vs full
- More memory efficient (fixed array)
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
## Common Mistakes

1. **Empty queue**: All operations return `-1` or `false` except `isEmpty()` → `true`
2. **Full queue**: `enQueue()` returns `false`
3. **Single element**: After `deQueue()`, queue becomes empty
4. **Capacity 1**: Only one element can be stored
5. **Wrap around**: Array approach wraps `tail` from `cap-1` to `0`

1. **Not tracking size**: Using only `head` and `tail` can't distinguish empty from full
2. **Wrong modulo calculation**: `(tail - 1 + cap) % cap` for rear (not `tail - 1`)
3. **Memory leaks**: Not deleting nodes in linked list `deQueue()`
4. **Null pointer**: Not checking `tail == nullptr` after `deQueue()` when empty
5. **Index out of bounds**: Not using modulo for array indices

## Related Problems

- [LC 641: Design Circular Deque](https://www.leetcode.com/problems/design-circular-deque/) - Circular queue with both ends
- [LC 232: Implement Queue using Stacks](https://www.leetcode.com/problems/implement-queue-using-stacks/) - Queue implementation
- [LC 225: Implement Stack using Queues](https://www.leetcode.com/problems/implement-stack-using-queues/) - Stack implementation
- [LC 146: LRU Cache](https://robinali34.github.io/blog_leetcode/posts/2025-12-02-medium-146-lru-cache/) - Another design problem

## Key Takeaways

1. **Circular Array Approach**:
   - Uses modulo arithmetic for wrapping: `(index + 1) % cap`
   - Tracks `size` to distinguish empty vs full
   - More memory efficient (fixed array)

2. **Linked List Approach**:
   - Dynamic node allocation
   - Simpler logic (no modulo needed)
   - Requires memory management (delete nodes)

3. **Empty vs Full Distinction**:
   - Array: Use `size` counter (not just head/tail positions)
   - Linked List: Use `cnt` counter

4. **Rear Element**:
   - Array: `q[(tail - 1 + cap) % cap]` (previous position, wrapped)
   - Linked List: `tail->val` (direct access)

## References

- [LC 622: Design Circular Queue on LeetCode](https://www.leetcode.com/problems/design-circular-queue/)
- [LeetCode Discuss — LC 622: Design Circular Queue](https://www.leetcode.com/problems/design-circular-queue/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/design-circular-queue/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
