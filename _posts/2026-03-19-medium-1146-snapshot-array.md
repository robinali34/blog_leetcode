---
layout: post
title: "[Medium] 1146. Snapshot Array"
date: 2026-03-19
categories: [leetcode, medium, design, binary-search]
tags: [leetcode, medium, design, binary-search, map]
permalink: /2026/03/19/medium-1146-snapshot-array/
---
Implement a `SnapshotArray` that supports:
- `SnapshotArray(int length)` -- initializes an array of the given length (all zeros)
- `void set(index, val)` -- sets the element at `index` to `val`
- `int snap()` -- takes a snapshot, returns the `snap_id` (starting from 0)
- `int get(index, snap_id)` -- returns the value at `index` at the time of the given snapshot

## Examples

**Example 1:**

```
Input:
  SnapshotArray(3), set(0,5), snap(), set(0,6), get(0,0)
Output:
  null, null, 0, null, 5
Explanation:
  set(0,5) → arr = [5,0,0]
  snap()   → snap_id 0 captures [5,0,0]
  set(0,6) → arr = [6,0,0]
  get(0,0) → value at index 0 in snap 0 = 5
```

## Constraints

- `1 <= length <= 5 * 10^4`
- `0 <= index < length`
- `0 <= val <= 10^9`
- `0 <= snap_id <` (number of times `snap()` was called)
- At most `5 * 10^4` calls to `set`, `snap`, and `get`

## Thinking Process

### Naive: Copy Entire Array -- O(n) per snap

The simplest approach: maintain a working array and copy it on every `snap()`.

- `set`: O(1)
- `snap`: O(n) -- copies the full array
- `get`: O(1)

This works but is **too slow and memory-heavy** when there are many snapshots and a large array, especially if only a few elements change between snaps.

### Bottleneck

Copying the entire array on every snapshot, even when most values haven't changed.

### Optimization: Store Only Changes

Instead of copying the full array, for each index store a **sorted log** of `(snap_id, value)` pairs -- only recording when a value actually changes.

On `get(index, snap_id)`: binary search for the latest entry at or before `snap_id`.

A `map<int,int>` per index gives this naturally with `upper_bound`.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 130" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary search: shrink [lo … hi]</text>

  <rect x="40" y="40" width="48" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="64" y="58" text-anchor="middle" font-size="12" fill="#3A3530">lo</text>
  <rect x="108" y="40" width="48" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="132" y="58" text-anchor="middle" font-size="12" fill="#3A3530">mid</text>
  <rect x="196" y="40" width="48" height="32" rx="4" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="220" y="58" text-anchor="middle" font-size="12" fill="#3A3530">hi</text>
  <rect x="60" y="90" width="160" height="28" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="140" y="108" text-anchor="middle" font-size="11" fill="#6B6560">discard half each step → O(log n)</text>
  <path d="M132 72v12M220 72v12" stroke="#9A9792" stroke-width="1.5" marker-end="url(#a)"/>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Standard binary search | O(log n) | O(1) | Sorted array, `left <= right` |
| Lower / upper bound | O(log n) | O(1) | First/last position, insert index |
| **Binary search on rotated array** *(this problem)* | O(log n) | O(1) | Identify sorted half, discard other |
| Binary search on answer | O(n log M) | O(1) | Monotonic predicate over search space |

## Solution

{% raw %}
```cpp
class SnapshotArray {
public:
    SnapshotArray(int length) {
        arr.resize(length);
    }

    void set(int index, int val) {
        arr[index] = val;
    }

    int snap() {
        int id = snaps.size();
        snaps.push_back(arr);
        return id;
    }

    int get(int index, int snap_id) {
        return snaps[snap_id][index];
    }

private:
    vector<vector<int>> snaps;
    vector<int> arr;
};
```

### Solution Explanation

**Approach:** Binary search on rotated array (this problem)

**Key idea:** ### Naive: Copy Entire Array -- O(n) per snap

**How the code works:**
- `set`: O(1)
- `snap`: O(n) -- copies the full array
- `get`: O(1)

**Walkthrough** — input `SnapshotArray(3), set(0,5), snap(), set(0,6), get(0,0)`, expected output `null, null, 0, null, 5`:

set(0,5) → arr = [5,0,0]
  snap()   → snap_id 0 captures [5,0,0]
  set(0,6) → arr = [6,0,0]
  get(0,0) → value at index 0 in snap 0 = 5
## Comparison

| Approach | `set` | `snap` | `get` | Space |
|---|---|---|---|---|
| Copy Array | O(1) | O(n) | O(1) | O(n · text{snaps}) |
| Map + Binary Search | O(log S) | O(1) | O(log S) | O(text{total sets}) |

The map approach wins when snapshots are frequent but changes are sparse.

## Common Mistakes

- Forgetting to initialize `data[i][0] = 0` (without it, `get` on an index that was never set returns garbage)
- Using `lower_bound` instead of `upper_bound` (off-by-one on the snap boundary)
- Storing snapshots in the wrong direction (value at snap time, not snap at value time)

## Key Takeaways

- **"Versioned data with sparse updates"** = store change log per element + binary search
- `upper_bound` then decrement is the standard pattern for "latest version at or before X"
- The optimization from O(n) snap to O(1) snap comes from only recording diffs, not full copies

## Related Problems

- [981. Time Based Key-Value Store](https://www.leetcode.com/problems/time-based-key-value-store/) -- same binary search on timestamps
- [362. Design Hit Counter](https://www.leetcode.com/problems/design-hit-counter/) -- time-based design
- [155. Min Stack](https://www.leetcode.com/problems/min-stack/) -- data structure design with history

## References

- [LC 1146: Snapshot Array on LeetCode](https://www.leetcode.com/problems/snapshot-array/)
- [LeetCode Discuss — LC 1146: Snapshot Array](https://www.leetcode.com/problems/snapshot-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/snapshot-array/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
