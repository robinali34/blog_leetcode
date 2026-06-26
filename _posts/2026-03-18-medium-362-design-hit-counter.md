---
layout: post
title: "[Medium] 362. Design Hit Counter"
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



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Sliding window</text>

  <rect x="20" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="36" y="63" text-anchor="middle" font-size="11">a</text>
  <rect x="52" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="68" y="63" text-anchor="middle" font-size="11">b</text>
  <rect x="84" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="63" text-anchor="middle" font-size="11">c</text>
  <rect x="116" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="132" y="63" text-anchor="middle" font-size="11">d</text>
  <rect x="148" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="164" y="63" text-anchor="middle" font-size="11">e</text>
  <rect x="52" y="38" width="64" height="42" rx="4" fill="none" stroke="#C4956A" stroke-width="2" stroke-dasharray="4"/>
  <text x="84" y="32" text-anchor="middle" font-size="10" fill="#C4956A" font-weight="600">window</text>
  <text x="110" y="105" text-anchor="middle" font-size="11" fill="#6B6560">expand right, shrink left when invalid</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Fixed-size window** *(this problem)* | O(n) | O(1) | Window size known upfront |
| Variable-size window | O(n) | O(1) | Expand/shrink until valid |
| Window + hash map | O(n) | O(k) | Track character/count frequencies |
| Deque window max | O(n) | O(k) | Monotonic deque for max/min in window |

## Solution

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

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** We need a **sliding window** of hits within the last 300 seconds. The key question is: how do we efficiently expire old hits?

**Walkthrough** — input `hit(1), hit(2), hit(3), getHits(4), hit(300), getHits(300), getHits(301)`, expected output `null, null, null, 3, null, 4, 3`:

getHits(4):   hits at 1,2,3 → 3
  getHits(300): hits at 1,2,3,300 → 4
  getHits(301): hit at 1 is outside [2,301] → hits at 2,3,300 → 3
## Comparison

| Approach | `hit` | `getHits` | Best For |
|---|---|---|---|
| Deque | O(1) | amortized O(1) | Timestamps in order (this problem) |
| Sorted Vector | O(n) worst / O(1) practical | O(log n + k) | Random access needed |
| Multiset | O(log n) | O(k log n) | Timestamps out of order |

## Common Mistakes

- Using `< timestamp - 300` instead of `<= timestamp - 300` (the window is exactly 300 seconds: `[timestamp - 299, timestamp]`)
- Not handling duplicate timestamps (multiple hits at the same time)
- Over-engineering with a hash map when a simple queue suffices

## Key Takeaways

- **Sliding time window + ordered arrivals** = deque is the natural data structure
- Each element is enqueued and dequeued at most once, giving amortized O(1) per operation
- The deque solution is the expected interview answer for this problem -- clean, simple, and optimal

## Related Problems

- [933. Number of Recent Calls](https://www.leetcode.com/problems/number-of-recent-calls/) -- nearly identical (queue + time window)
- [346. Moving Average from Data Stream](https://www.leetcode.com/problems/moving-average-from-data-stream/) -- sliding window with queue
- [155. Min Stack](https://www.leetcode.com/problems/min-stack/) -- data structure design

## References

- [LC 362: Design Hit Counter on LeetCode](https://www.leetcode.com/problems/design-hit-counter/)
- [LeetCode Discuss — LC 362: Design Hit Counter](https://www.leetcode.com/problems/design-hit-counter/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/design-hit-counter/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
