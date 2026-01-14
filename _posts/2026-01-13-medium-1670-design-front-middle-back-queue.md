---
layout: post
title: "1670. Design Front Middle Back Queue"
date: 2026-01-13 00:00:00 -0700
categories: [leetcode, medium, design, deque, data-structure]
permalink: /2026/01/13/medium-1670-design-front-middle-back-queue/
tags: [leetcode, medium, design, deque, data-structure, two-deques]
---

# 1670. Design Front Middle Back Queue

## Problem Statement

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

## Solution Approach

This problem requires implementing a queue with operations at front, middle, and back. The key challenge is efficiently accessing and modifying the middle element.

### Key Insights:

1. **Two Deques**: Use two deques (`front_cache` and `back_cache`) to split the queue
2. **Balance Invariant**: Maintain `front_cache.size() <= back_cache.size() <= front_cache.size() + 1`
3. **Middle Element**: 
   - If sizes equal: middle is `front_cache.back()`
   - If `back_cache` is larger: middle is `back_cache.front()`
4. **Rebalancing**: After each operation, rebalance to maintain the invariant
5. **Push Middle**: Add to end of `front_cache` (becomes new middle)

### Algorithm:

1. **Push Operations**:
   - `pushFront`: Add to front of `front_cache`, rebalance
   - `pushMiddle`: Add to back of `front_cache`, rebalance
   - `pushBack`: Add to back of `back_cache`, rebalance
2. **Pop Operations**:
   - `popFront`: Remove from `front_cache` (or `back_cache` if `front_cache` empty), rebalance
   - `popMiddle`: Remove from appropriate deque based on sizes, no rebalance needed
   - `popBack`: Remove from `back_cache`, rebalance
3. **Rebalance**: Ensure `front_cache.size() <= back_cache.size() <= front_cache.size() + 1`

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

## Key Insights

1. **Two Deques Pattern**: Split queue into two halves for efficient middle access
2. **Balance Invariant**: `front_cache.size() <= back_cache.size() <= front_cache.size() + 1`
3. **Middle Element**: Always accessible in O(1) due to invariant
4. **Rebalancing**: Maintains invariant after each modification
5. **Push Middle**: Add to end of `front_cache` (becomes new middle)

## Edge Cases

1. **Empty queue**: All pop operations return `-1`
2. **Single element**: After one push, one pop returns that element
3. **Two elements**: Middle is the first element (frontmost middle)
4. **Many operations**: Rebalancing maintains efficiency
5. **Alternating operations**: Balance maintained correctly

## Common Mistakes

1. **Wrong middle calculation**: Not handling the case when sizes are equal vs unequal
2. **Missing rebalance**: Forgetting to rebalance after push/pop operations
3. **Wrong rebalance logic**: Incorrectly moving elements between deques
4. **Empty check**: Not checking if both deques are empty before popping
5. **Pop from wrong deque**: Popping from `front_cache` when it's empty in `popFront()`

## Alternative Approaches

### **Approach 2: Single Deque with Index Calculation**

```cpp
class FrontMiddleBackQueue {
private:
    deque<int> dq;
public:
    FrontMiddleBackQueue() {}
    
    void pushFront(int val) {
        dq.push_front(val);
    }
    
    void pushMiddle(int val) {
        int mid = dq.size() / 2;
        dq.insert(dq.begin() + mid, val);
    }
    
    void pushBack(int val) {
        dq.push_back(val);
    }
    
    int popFront() {
        if(dq.empty()) return -1;
        int val = dq.front();
        dq.pop_front();
        return val;
    }
    
    int popMiddle() {
        if(dq.empty()) return -1;
        int mid = (dq.size() - 1) / 2;
        int val = dq[mid];
        dq.erase(dq.begin() + mid);
        return val;
    }
    
    int popBack() {
        if(dq.empty()) return -1;
        int val = dq.back();
        dq.pop_back();
        return val;
    }
};
```

**Time Complexity:** O(n) for `pushMiddle` and `popMiddle` (insertion/deletion in middle)  
**Space Complexity:** O(n)

**Comparison:**
- **Two Deques**: O(1) amortized for all operations
- **Single Deque**: O(n) for middle operations, O(1) for front/back

## Related Problems

- [LC 641: Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) - Design a circular deque
- [LC 622: Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) - Design a circular queue
- [LC 232: Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) - Queue with stacks
- [LC 225: Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) - Stack with queues

---

*This problem demonstrates the **Two Deques Pattern** for efficiently accessing middle elements in a queue. The key is maintaining a balance invariant between the two deques.*

