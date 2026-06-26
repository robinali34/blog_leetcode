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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute force** *(this problem)* | Often O(n^2) or O(2^n) | O(n) | Baseline; clarifies the optimization target |
| Sort + scan | O(n log n) | O(1) | Pairs, intervals, greedy ordering |
| Hash map / set | O(n) | O(n) | Frequency, membership, two-sum style |
| Single-pass linear | O(n) | O(1) | Two pointers, sliding window, Kadane |

## Solution
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

### Solution Explanation

**Approach:** Brute force (this problem)

**Key idea:** This is a classic **producer-consumer synchronization** problem. Two threads must take strict turns:

**How the code works:**
1. **Mutual exclusion** -- only one thread prints at a time
2. **Ordering** -- foo always goes before bar in each round
- `foo_turn = true` means it's foo's turn
- Each thread waits until the flag matches its turn, prints, flips the flag, and notifies the other
1. Checks `predicate()` -- if true, proceeds immediately
2. If false, releases the lock and sleeps

**Walkthrough** — input `n = 1`, expected output `"foobar"`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
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

## References

- [LC 1115: Print FooBar Alternately on LeetCode](https://www.leetcode.com/problems/print-foobar-alternately/)
- [LeetCode Discuss — LC 1115: Print FooBar Alternately](https://www.leetcode.com/problems/print-foobar-alternately/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/print-foobar-alternately/editorial/) *(may require premium)*

## Key Takeaways

- **"Alternate between two threads"** = mutex + condition variable + boolean flag
- The `cv.wait(lock, predicate)` pattern is the idiomatic C++ way to handle conditional synchronization
- This is the simplest form of the producer-consumer pattern with exactly two participants

## Related Problems

- [1114. Print in Order](https://www.leetcode.com/problems/print-in-order/) -- 3 threads, sequential ordering
- [1116. Print Zero Even Odd](https://www.leetcode.com/problems/print-zero-even-odd/) -- 3 threads, alternating pattern
- [1117. Building H2O](https://www.leetcode.com/problems/building-h2o/) -- barrier synchronization
- [1188. Design Bounded Blocking Queue](https://www.leetcode.com/problems/design-bounded-blocking-queue/) -- producer-consumer with capacity
