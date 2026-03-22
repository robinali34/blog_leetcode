---
layout: post
title: "LeetCode 362. Design Hit Counter"
date: 2026-03-18
categories: [leetcode, medium, design, queue]
tags: [leetcode, medium, design, queue, deque, sliding-window]
permalink: /2026/03/18/medium-362-design-hit-counter/
---

Design a hit counter that counts the number of hits received in the past 5 minutes (300 seconds).

Implement `HitCounter`:
- `HitCounter()` -- initializes the counter
- `void hit(int timestamp)` -- records a hit at the given timestamp
- `int getHits(int timestamp)` -- returns the number of hits in the past 300 seconds (i.e., `[timestamp - 299, timestamp]`)

Timestamps are in **increasing order** (though ties are allowed).

## Examples

**Example 1:**

```
Input:
  hit(1), hit(2), hit(3), getHits(4), hit(300), getHits(300), getHits(301)

Output:
  null, null, null, 3, null, 4, 3

Explanation:
  getHits(4):   hits at 1,2,3 → 3
  getHits(300): hits at 1,2,3,300 → 4
  getHits(301): hit at 1 is outside [2,301] → hits at 2,3,300 → 3
```

## Constraints

- `1 <= timestamp <= 2 * 10^9`
- All calls to `hit` and `getHits` are made with strictly increasing `timestamp` (with ties allowed for `hit`)
- At most `300` calls to `hit` and `getHits`

## Thinking Process

We need a **sliding window** of hits within the last 300 seconds. The key question is: how do we efficiently expire old hits?

Since timestamps arrive in non-decreasing order, older hits are always at the front -- a natural fit for a **queue/deque**.

## Solution 1: Deque (Optimal) -- $O(1)$ amortized

Use a deque to store timestamps. On `getHits`, pop from the front while the oldest hit is outside the window.

{% raw %}
```cpp
class HitCounter {
public:
    HitCounter() {}

    void hit(int timestamp) {
        hits.push_back(timestamp);
    }

    int getHits(int timestamp) {
        while (!hits.empty() && hits.front() <= timestamp - 300) {
            hits.pop_front();
        }
        return hits.size();
    }

private:
    deque<int> hits;
};
```
{% endraw %}

| Operation | Time | Space |
|---|---|---|
| `hit` | $O(1)$ | $O(n)$ total |
| `getHits` | $O(k)$ amortized $O(1)$ | -- |

Each element is pushed once and popped once, so across all operations the total work for eviction is $O(n)$.

## Solution 2: Sorted Vector + Binary Search

Maintain a sorted vector. On `getHits`, use `lower_bound` to find the window boundary and erase expired entries.

{% raw %}
```cpp
class HitCounter {
public:
    HitCounter() {}

    void hit(int timestamp) {
        auto it = lower_bound(cache.begin(), cache.end(), timestamp);
        cache.insert(it, timestamp);
    }

    int getHits(int timestamp) {
        auto it_old = lower_bound(cache.begin(), cache.end(), timestamp - 300 + 1);
        cache.erase(cache.begin(), it_old);
        return cache.size();
    }

private:
    vector<int> cache;
};
```
{% endraw %}

| Operation | Time | Space |
|---|---|---|
| `hit` | $O(n)$ (vector insert shifts elements) | $O(n)$ |
| `getHits` | $O(\log n + k)$ (binary search + erase) | -- |

Since timestamps arrive in order, `lower_bound` always finds the end, making `hit` effectively $O(1)$ in practice. However the vector insert is still $O(n)$ worst case due to shifting.

## Solution 3: Multiset + Binary Search

A balanced BST gives $O(\log n)$ insert and $O(\log n)$ per element erased.

{% raw %}
```cpp
class HitCounter {
public:
    HitCounter() {}

    void hit(int timestamp) {
        hits.insert(timestamp);
    }

    int getHits(int timestamp) {
        auto it = hits.lower_bound(timestamp - 300 + 1);
        hits.erase(hits.begin(), it);
        return hits.size();
    }

private:
    multiset<int> hits;
};
```
{% endraw %}

| Operation | Time | Space |
|---|---|---|
| `hit` | $O(\log n)$ | $O(n)$ |
| `getHits` | $O(k \log n)$ | -- |

## Comparison

| Approach | `hit` | `getHits` | Best For |
|---|---|---|---|
| Deque | $O(1)$ | amortized $O(1)$ | Timestamps in order (this problem) |
| Sorted Vector | $O(n)$ worst / $O(1)$ practical | $O(\log n + k)$ | Random access needed |
| Multiset | $O(\log n)$ | $O(k \log n)$ | Timestamps out of order |

## Common Mistakes

- Using `< timestamp - 300` instead of `<= timestamp - 300` (the window is exactly 300 seconds: `[timestamp - 299, timestamp]`)
- Not handling duplicate timestamps (multiple hits at the same time)
- Over-engineering with a hash map when a simple queue suffices

## Key Takeaways

- **Sliding time window + ordered arrivals** = deque is the natural data structure
- Each element is enqueued and dequeued at most once, giving amortized $O(1)$ per operation
- The deque solution is the expected interview answer for this problem -- clean, simple, and optimal

## Related Problems

- [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) -- nearly identical (queue + time window)
- [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) -- sliding window with queue
- [155. Min Stack](https://leetcode.com/problems/min-stack/) -- data structure design

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
