---
layout: post
title: "622. Design Circular Queue"
date: 2026-01-24 00:00:00 -0700
categories: [leetcode, medium, array, linked-list, design, queue]
permalink: /2026/01/24/medium-622-design-circular-queue/
tags: [leetcode, medium, array, linked-list, design, queue, circular-queue, data-structure]
---

# 622. Design Circular Queue

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Queue behavior**: What should happen when we try to enqueue into a full queue? (Assumption: Return `false`, don't add the element)

2. **Empty queue operations**: What should `Front()` and `Rear()` return when the queue is empty? (Assumption: Return `-1` as specified in the problem)

3. **Circular property**: When the queue is full and we dequeue, can we immediately enqueue at that position? (Assumption: Yes - that's the circular property, we reuse freed space)

4. **Size tracking**: Should we track the current size separately or calculate it from head/tail pointers? (Assumption: Either approach works, but tracking size separately simplifies implementation)

5. **Thread safety**: Do we need to handle concurrent operations? (Assumption: No - single-threaded operations are sufficient for this problem)

## Solution Approach

A circular queue is a queue where the last position is connected back to the first position. This allows efficient use of space by reusing freed positions.

### Key Insights:

1. **Circular Array**: Use modulo arithmetic to wrap around when reaching array bounds
2. **Two Approaches**: Array-based (fixed size) or Linked List-based (dynamic nodes)
3. **Tracking State**: Need to track head, tail, and current size/count
4. **Empty vs Full**: Distinguish between empty and full states

## Solution 1: Array-Based Circular Queue

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

### Algorithm Explanation:

#### **Data Members:**

1. **`q`**: Fixed-size array to store queue elements
2. **`head`**: Index of the front element
3. **`tail`**: Index where next element will be inserted
4. **`size`**: Current number of elements in queue
5. **`cap`**: Maximum capacity of the queue

#### **Key Operations:**

1. **`enQueue(value)`**:
   - Check if queue is full → return `false`
   - Insert value at `tail` position
   - Update tail: `tail = (tail + 1) % cap` (wrap around)
   - Increment size

2. **`deQueue()`**:
   - Check if queue is empty → return `false`
   - Update head: `head = (head + 1) % cap` (wrap around)
   - Decrement size

3. **`Front()`**:
   - Return element at `head` index if not empty

4. **`Rear()`**:
   - Return element at `(tail - 1 + cap) % cap` (previous position, wrapped)

5. **`isEmpty()`**: Check if `size == 0`
6. **`isFull()`**: Check if `size == cap`

### Example Walkthrough:

**Input:** `k = 3`, operations: `enQueue(1)`, `enQueue(2)`, `enQueue(3)`, `enQueue(4)`, `Rear()`, `deQueue()`, `enQueue(4)`, `Rear()`

```
Initial: q = [_, _, _], head = 0, tail = 0, size = 0

enQueue(1): q[0] = 1, tail = 1, size = 1
  q = [1, _, _], head = 0, tail = 1

enQueue(2): q[1] = 2, tail = 2, size = 2
  q = [1, 2, _], head = 0, tail = 2

enQueue(3): q[2] = 3, tail = 0 (wrapped), size = 3
  q = [1, 2, 3], head = 0, tail = 0

enQueue(4): isFull() → false (size == cap)
  Return: false

Rear(): q[(0 - 1 + 3) % 3] = q[2] = 3
  Return: 3

deQueue(): head = (0 + 1) % 3 = 1, size = 2
  q = [_, 2, 3], head = 1, tail = 0

enQueue(4): q[0] = 4, tail = 1, size = 3
  q = [4, 2, 3], head = 1, tail = 1

Rear(): q[(1 - 1 + 3) % 3] = q[0] = 4
  Return: 4 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(1) for all operations
  - Array access: O(1)
  - Modulo arithmetic: O(1)
  - All operations are constant time

- **Space Complexity:** O(k)
  - Array of size `k`: O(k)
  - Variables: O(1)
  - Overall: O(k)

## Solution 2: Linked List-Based Circular Queue

```cpp
class MyCircularQueue {
public:
    MyCircularQueue(int k) : head(nullptr), tail(nullptr), cnt(0), cap(k) {
        
    }
    
    bool enQueue(int value) {
        if(cnt == cap) return false;
        Node* nextNode = new Node(value);
        if(cnt == 0) {
            head = tail = nextNode;
        } else {
            tail->next = nextNode;
            tail = nextNode;
        }
        cnt++;
        return true;
    }
    
    bool deQueue() {
        if(cnt == 0) return false;
        Node* tmp = head;
        head = head->next;
        delete tmp;
        cnt--;
        if(cnt == 0) tail = nullptr;
        return true;
    }
    
    int Front() {
        return cnt == 0 ? -1 : head->val;
    }
    
    int Rear() {
        return cnt == 0 ? -1 : tail->val;
    }
    
    bool isEmpty() {
        return cnt == 0;
    }
    
    bool isFull() {
        return cnt == cap;        
    }

private:
    struct Node {
        int val;
        Node* next;
        Node(int v): val(v), next(nullptr){}
    };

    Node *head, *tail;
    int cnt, cap;
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

### Algorithm Explanation:

#### **Node Structure:**

1. **`val`**: Value stored in the node
2. **`next`**: Pointer to next node

#### **Data Members:**

1. **`head`**: Pointer to front node
2. **`tail`**: Pointer to rear node
3. **`cnt`**: Current count of elements
4. **`cap`**: Maximum capacity

#### **Key Operations:**

1. **`enQueue(value)`**:
   - Check if full (`cnt == cap`) → return `false`
   - Create new node with value
   - If empty (`cnt == 0`): set both `head` and `tail` to new node
   - Otherwise: append to `tail->next`, update `tail`
   - Increment `cnt`

2. **`deQueue()`**:
   - Check if empty (`cnt == 0`) → return `false`
   - Save `head`, move `head` to `head->next`
   - Delete old head node
   - Decrement `cnt`
   - If empty after deletion, set `tail = nullptr`

3. **`Front()`**: Return `head->val` if not empty
4. **`Rear()`**: Return `tail->val` if not empty
5. **`isEmpty()`**: Check if `cnt == 0`
6. **`isFull()`**: Check if `cnt == cap`

### Example Walkthrough:

**Input:** `k = 3`, operations: `enQueue(1)`, `enQueue(2)`, `enQueue(3)`, `enQueue(4)`, `Rear()`, `deQueue()`, `enQueue(4)`, `Rear()`

```
Initial: head = nullptr, tail = nullptr, cnt = 0

enQueue(1): Create node(1)
  head → [1] ← tail, cnt = 1

enQueue(2): Create node(2), append
  head → [1] → [2] ← tail, cnt = 2

enQueue(3): Create node(3), append
  head → [1] → [2] → [3] ← tail, cnt = 3

enQueue(4): cnt == cap → false
  Return: false

Rear(): tail->val = 3
  Return: 3

deQueue(): Remove head node
  head → [2] → [3] ← tail, cnt = 2

enQueue(4): Create node(4), append
  head → [2] → [3] → [4] ← tail, cnt = 3

Rear(): tail->val = 4
  Return: 4 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(1) for all operations
  - Node creation: O(1)
  - Pointer updates: O(1)
  - All operations are constant time

- **Space Complexity:** O(k)
  - Up to `k` nodes: O(k)
  - Variables: O(1)
  - Overall: O(k)

## Key Insights

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

## Edge Cases

1. **Empty queue**: All operations return `-1` or `false` except `isEmpty()` → `true`
2. **Full queue**: `enQueue()` returns `false`
3. **Single element**: After `deQueue()`, queue becomes empty
4. **Capacity 1**: Only one element can be stored
5. **Wrap around**: Array approach wraps `tail` from `cap-1` to `0`

## Common Mistakes

1. **Not tracking size**: Using only `head` and `tail` can't distinguish empty from full
2. **Wrong modulo calculation**: `(tail - 1 + cap) % cap` for rear (not `tail - 1`)
3. **Memory leaks**: Not deleting nodes in linked list `deQueue()`
4. **Null pointer**: Not checking `tail == nullptr` after `deQueue()` when empty
5. **Index out of bounds**: Not using modulo for array indices

## Comparison of Approaches

| Aspect | Array-Based | Linked List-Based |
|--------|-------------|-------------------|
| **Memory** | Fixed O(k) | Dynamic O(k) |
| **Speed** | Faster (no allocation) | Slower (allocation overhead) |
| **Code Complexity** | Moderate (modulo arithmetic) | Simpler (no modulo) |
| **Memory Management** | None needed | Requires delete |
| **Cache Performance** | Better (contiguous memory) | Worse (scattered nodes) |
| **Best For** | When size is known | When flexibility needed |

## Related Problems

- [LC 641: Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) - Circular queue with both ends
- [LC 232: Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) - Queue implementation
- [LC 225: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) - Stack implementation
- [LC 146: LRU Cache](https://robinali34.github.io/blog_leetcode/posts/2025-12-02-medium-146-lru-cache/) - Another design problem

---

*This problem demonstrates the **circular queue** data structure, which efficiently reuses space by connecting the end back to the beginning. The array-based approach is generally preferred for its simplicity and performance, while the linked list approach offers more flexibility.*
