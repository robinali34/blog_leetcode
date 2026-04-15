---
layout: post
title: "[Medium] 1115. Print FooBar Alternately"
date: 2026-03-28
categories: [leetcode, medium, concurrency]
tags: [leetcode, medium, concurrency, mutex, condition-variable, multithreading]
permalink: /2026/03/28/medium-1115-print-foobar-alternately/
---

Two different threads will call `foo` and `bar` respectively. Design a mechanism so that `"foobar"` is printed `n` times by alternating between the two threads: `foo` always prints first, then `bar`, then `foo` again, and so on.

## Examples

**Example 1:**

```
Input: n = 1
Output: "foobar"
```

**Example 2:**

```
Input: n = 2
Output: "foobarfoobar"
```

## Constraints

- `1 <= n <= 1000`

## Thinking Process

This is a classic **producer-consumer synchronization** problem. Two threads must take strict turns:

```
Thread A (foo): print "foo" only when it's foo's turn
Thread B (bar): print "bar" only when it's bar's turn
foo → bar → foo → bar → ...
```

### Synchronization Pattern

We need:
1. **Mutual exclusion** -- only one thread prints at a time
2. **Ordering** -- foo always goes before bar in each round

A **mutex + condition variable + boolean flag** achieves both:
- `foo_turn = true` means it's foo's turn
- Each thread waits until the flag matches its turn, prints, flips the flag, and notifies the other

### How `condition_variable::wait` Works

```cpp
cv.wait(lock, predicate);
```

This atomically:
1. Checks `predicate()` -- if true, proceeds immediately
2. If false, releases the lock and sleeps
3. On `notify_all`, re-acquires the lock and re-checks the predicate
4. Repeats until predicate is true

The predicate prevents **spurious wakeups** -- a thread only proceeds when the condition is actually met.

## Solution: Mutex + Condition Variable

{% raw %}
```cpp
class FooBar {
private:
    int n;
    mutex mtx;
    condition_variable cv;
    bool foo_turn = true;

public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [this]() { return foo_turn; });

            printFoo();

            foo_turn = false;
            cv.notify_all();
        }
    }

    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [this]() { return !foo_turn; });

            printBar();

            foo_turn = true;
            cv.notify_all();
        }
    }
};
```
{% endraw %}

**Time**: $O(n)$ per thread
**Space**: $O(1)$

## Solution 2: Binary Semaphores (C++20)

Two semaphores act as "tokens" passed back and forth. `foo_sem` starts at 1 (foo goes first), `bar_sem` starts at 0 (bar waits). Each thread acquires its own semaphore, prints, then releases the other's.

{% raw %}
```cpp
class FooBar {
private:
    int n;
    binary_semaphore foo_sem{1};
    binary_semaphore bar_sem{0};

public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        for (int i = 0; i < n; i++) {
            foo_sem.acquire();
            printFoo();
            bar_sem.release();
        }
    }

    void bar(function<void()> printBar) {
        for (int i = 0; i < n; i++) {
            bar_sem.acquire();
            printBar();
            foo_sem.release();
        }
    }
};
```
{% endraw %}

**Time**: $O(n)$ per thread
**Space**: $O(1)$

### Why This Works

```
foo_sem=1, bar_sem=0

foo: acquire foo_sem(1→0) → print "foo" → release bar_sem(0→1)
bar: acquire bar_sem(1→0) → print "bar" → release foo_sem(0→1)
foo: acquire foo_sem(1→0) → print "foo" → release bar_sem(0→1)
...
```

Each semaphore acts as a gate: `acquire` blocks until the count is > 0, `release` increments the count by 1. The two semaphores form a ping-pong -- each thread hands the turn to the other.

## Comparison

| Approach | Mechanism | Complexity | Notes |
|---|---|---|---|
| Mutex + CV | `mutex` + `condition_variable` + flag | More boilerplate | Works in C++11+ |
| Binary Semaphore | `binary_semaphore` pair | Minimal, elegant | Requires C++20 |

## Execution Trace

```
n = 2, foo_turn = true

foo thread:  wait(foo_turn=true) → passes → print "foo" → foo_turn=false → notify
bar thread:  wait(!foo_turn=true) → passes → print "bar" → foo_turn=true  → notify
foo thread:  wait(foo_turn=true) → passes → print "foo" → foo_turn=false → notify
bar thread:  wait(!foo_turn=true) → passes → print "bar" → foo_turn=true  → notify

Output: "foobarfoobar"
```

## Key Components

| Component | Role |
|---|---|
| `mutex` | Ensures only one thread accesses shared state at a time |
| `condition_variable` | Allows threads to sleep/wake efficiently (no busy-waiting) |
| `unique_lock` | RAII wrapper that locks on construction, unlocks on destruction |
| `foo_turn` | Boolean flag encoding whose turn it is |
| `notify_all` | Wakes the other thread to check its condition |

## Common Mistakes

- Using `notify_one` vs `notify_all` -- both work here (only 2 threads), but `notify_all` is safer in general
- Forgetting the predicate in `cv.wait` -- without it, spurious wakeups can cause out-of-order printing
- Using `lock_guard` instead of `unique_lock` -- `condition_variable::wait` requires `unique_lock` because it needs to temporarily release the lock

## Key Takeaways

- **"Alternate between two threads"** = mutex + condition variable + boolean flag
- The `cv.wait(lock, predicate)` pattern is the idiomatic C++ way to handle conditional synchronization
- This is the simplest form of the producer-consumer pattern with exactly two participants

## Related Problems

- [1114. Print in Order](https://leetcode.com/problems/print-in-order/) -- 3 threads, sequential ordering
- [1116. Print Zero Even Odd](https://leetcode.com/problems/print-zero-even-odd/) -- 3 threads, alternating pattern
- [1117. Building H2O](https://leetcode.com/problems/building-h2o/) -- barrier synchronization
- [1188. Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/) -- producer-consumer with capacity
