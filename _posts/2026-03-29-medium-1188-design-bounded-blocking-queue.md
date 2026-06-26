---
layout: post
title: "[Medium] 1188. Design Bounded Blocking Queue"
date: 2026-03-29
categories: [leetcode, medium, concurrency, design]
tags: [leetcode, medium, concurrency, design, semaphore, producer-consumer]
permalink: /2026/03/29/medium-1188-design-bounded-blocking-queue/
---
Implement a thread-safe bounded blocking queue with the following methods:
- `BoundedBlockingQueue(int capacity)` -- initialize with max capacity
- `void enqueue(int element)` -- add element to the back; **blocks** if the queue is full until space is available
- `int dequeue()` -- remove and return the front element; **blocks** if the queue is empty until an element is available
- `int size()` -- return the current number of elements

Multiple threads will call `enqueue` and `dequeue` concurrently.

## Examples

**Example 1:**

```
Input: capacity = 2
  Thread 1: enqueue(1), dequeue(), dequeue()
  Thread 2: enqueue(0), enqueue(2), enqueue(3)

Output: [1,0,2]
Explanation: Cannot enqueue(3) until a dequeue makes space.
```

## Constraints

- `1 <= capacity <= 100`
- Multiple producer and consumer threads

## Thinking Process

This is the classic **bounded producer-consumer** problem. We need to coordinate:

1. **Producers** (`enqueue`) must block when the queue is full
2. **Consumers** (`dequeue`) must block when the queue is empty
3. **Mutual exclusion** on the shared queue

### Three Semaphores

| Semaphore | Initial Value | Purpose |
|---|---|---|
| `empty` | `capacity` | Tracks available slots (producers acquire, consumers release) |
| `full` | `0` | Tracks available items (consumers acquire, producers release) |
| `mutex` | `1` | Protects the shared queue (binary semaphore for mutual exclusion) |

### Protocol

```
enqueue(x):                    dequeue():
  empty.acquire()  ← block       full.acquire()  ← block
                     if full                        if empty
  mutex.acquire()                 mutex.acquire()
  q.push(x)                      x = q.front(); q.pop()
  mutex.release()                 mutex.release()
  full.release()   → wake        empty.release()  → wake
                     consumer                        producer
```

### Why Semaphore Order Matters

`empty.acquire()` must come **before** `mutex.acquire()`. If reversed, a producer could hold the mutex while blocking on `empty`, preventing any consumer from acquiring the mutex to dequeue -- **deadlock**.

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
```cpp
class BoundedBlockingQueue {
public:
    BoundedBlockingQueue(int capacity)
        : capacity(capacity), empty(capacity), full(0), mutex(1) {}

    void enqueue(int element) {
        empty.acquire();
        mutex.acquire();
        q.push(element);
        mutex.release();
        full.release();
    }

    int dequeue() {
        full.acquire();
        mutex.acquire();
        int rtn = q.front();
        q.pop();
        mutex.release();
        empty.release();
        return rtn;
    }

    int size() {
        mutex.acquire();
        int sz = q.size();
        mutex.release();
        return sz;
    }

private:
    queue<int> q;
    int capacity;
    counting_semaphore<> empty;
    counting_semaphore<> full;
    counting_semaphore<> mutex;
};
```

### Solution Explanation

**Approach:** Hash map + list (this problem)

**Key idea:** This is the classic **bounded producer-consumer** problem. We need to coordinate:

**How the code works:**
1. **Producers** (`enqueue`) must block when the queue is full
2. **Consumers** (`dequeue`) must block when the queue is empty
3. **Mutual exclusion** on the shared queue

**Walkthrough** — input `capacity = 2`, expected output `[1,0,2]`:

Cannot enqueue(3) until a dequeue makes space.
## Comparison

| Approach | Mechanism | C++ Version | Deadlock Risk |
|---|---|---|---|
| Three Semaphores | `counting_semaphore` × 3 | C++20 | Must acquire in correct order |
| Mutex + 2 CVs | `mutex` + `condition_variable` × 2 | C++11 | None (single lock) |

## Execution Trace

```
capacity = 2, empty=2, full=0, mutex=1

enqueue(1): empty(2→1), mutex(1→0), push 1, mutex(0→1), full(0→1)
            queue: [1]

enqueue(0): empty(1→0), mutex(1→0), push 0, mutex(0→1), full(1→2)
            queue: [1, 0]

enqueue(2): empty=0 → BLOCKS (queue full)

dequeue():  full(2→1), mutex(1→0), pop 1, mutex(0→1), empty(0→1)
            queue: [0]  → returns 1
            → unblocks enqueue(2)

enqueue(2): empty(1→0), push 2
            queue: [0, 2]
```

## Key Details

**`counting_semaphore<>` vs `binary_semaphore`**: `counting_semaphore` can count higher than 1, tracking multiple available slots/items. The mutex semaphore only ever goes 0↔1, but using `counting_semaphore<>` with initial value 1 is equivalent.

**Why not use `std::mutex`?** You could -- replacing the mutex semaphore with `std::mutex` and `lock_guard` works fine. Using all semaphores keeps the pattern uniform.

## Common Mistakes

- Acquiring mutex **before** the capacity semaphore (causes deadlock)
- Forgetting to protect `size()` with the mutex (data race on concurrent access)
- Using `binary_semaphore` for `empty`/`full` when capacity > 1

## Key Takeaways

- **Bounded producer-consumer** = three semaphores: `empty(capacity)`, `full(0)`, `mutex(1)`
- The acquire order (capacity semaphore → mutex) is critical to avoid deadlock
- This is one of the most fundamental concurrency patterns -- appears in OS courses, job interviews, and real systems (thread pools, message queues)

## Related Problems

- [1115. Print FooBar Alternately](https://www.leetcode.com/problems/print-foobar-alternately/) -- simpler two-thread alternation
- [1114. Print in Order](https://www.leetcode.com/problems/print-in-order/) -- sequential ordering
- [1116. Print Zero Even Odd](https://www.leetcode.com/problems/print-zero-even-odd/) -- multi-thread coordination
- [362. Design Hit Counter](https://www.leetcode.com/problems/design-hit-counter/) -- queue-based design

## References

- [LC 1188: Design Bounded Blocking Queue on LeetCode](https://www.leetcode.com/problems/design-bounded-blocking-queue/)
- [LeetCode Discuss — LC 1188: Design Bounded Blocking Queue](https://www.leetcode.com/problems/design-bounded-blocking-queue/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/design-bounded-blocking-queue/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
