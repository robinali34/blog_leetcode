---
layout: post
title: "LeetCode 134. Gas Station"
date: 2026-03-22
categories: [leetcode, medium, greedy, array]
tags: [leetcode, medium, greedy, array]
permalink: /2026/03/22/medium-134-gas-station/
---

There are `n` gas stations along a circular route. Station `i` has `gas[i]` units of gas. It costs `cost[i]` units to travel from station `i` to station `i+1`. Starting with an empty tank, return the starting station index if you can complete the circuit, or `-1` if impossible. The answer is guaranteed to be **unique** if it exists.

## Examples

**Example 1:**

```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation: Start at station 3 (gas=4).
  3→4: tank = 4-1 = 3
  4→0: tank = 3+5-2 = 6
  0→1: tank = 6+1-3 = 4
  1→2: tank = 4+2-4 = 2
  2→3: tank = 2+3-5 = 0  ✓
```

**Example 2:**

```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation: Total gas = 9 < total cost = 10, impossible.
```

## Constraints

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

## Thinking Process

### Key Observations

**Observation 1**: If `totalGain = sum(gas[i] - cost[i]) < 0`, no starting point works -- there simply isn't enough fuel for the full circuit.

**Observation 2**: If the total is non-negative, a solution exists. The question is *where* to start.

### Greedy Insight

Track `currGain` as the running tank from the current candidate start. If `currGain` drops below 0 at station `i`, then:
- No station in `[start, i]` can be the answer (they'd all run out at or before `i`)
- Reset the candidate to `i + 1` and reset `currGain = 0`

Why does skipping work? If `start` through `i` collectively can't sustain the trip to `i+1`, any later station in that range has even less accumulated fuel (since `start` contributes non-negative fuel to reach them).

### Walk-through

```
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
diff = [-2,-2,-2, 3, 3]    totalGain = 0 ≥ 0

i=0: currGain = -2 < 0 → reset, rtn=1, currGain=0
i=1: currGain = -2 < 0 → reset, rtn=2, currGain=0
i=2: currGain = -2 < 0 → reset, rtn=3, currGain=0
i=3: currGain = 3 ≥ 0   → keep going
i=4: currGain = 6 ≥ 0   → keep going

totalGain = 0 ≥ 0 → return rtn = 3 ✓
```

## Solution: Greedy -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int currGain = 0, totalGain = 0, rtn = 0;
        for (int i = 0; i < gas.size(); ++i) {
            totalGain += gas[i] - cost[i];
            currGain += gas[i] - cost[i];

            if (currGain < 0) {
                rtn = i + 1;
                currGain = 0;
            }
        }
        return totalGain >= 0 ? rtn : -1;
    }
};
```
{% endraw %}

**Time**: $O(n)$ -- single pass
**Space**: $O(1)$

## Why This Works

The algorithm maintains two invariants:

1. **`totalGain`** decides feasibility: if the total fuel balance is negative, no solution exists
2. **`currGain`** finds the start: whenever the running balance drops negative, every station in the current segment fails, so we start fresh from the next station

Since the answer is unique (given by the problem), the last candidate standing after the full scan must be correct -- all earlier candidates were eliminated, and `totalGain >= 0` guarantees this one works.

## Common Mistakes

- Trying to simulate from every station -- $O(n^2)$ brute force
- Forgetting the `totalGain` check (the greedy candidate might not work if there isn't enough total fuel)
- Off-by-one: resetting to `i + 1` not `i` (station `i` already failed)

## Key Takeaways

- **"Find a starting point on a circular route"** = greedy with running sum + total sum check
- The two-variable pattern (`totalGain` for feasibility, `currGain` for candidate selection) is elegant and reusable
- This is a variant of **Kadane's algorithm** thinking: when the running sum goes negative, reset

## Related Problems

- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) -- Kadane's algorithm (same reset-on-negative idea)
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) -- greedy scheduling
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) -- greedy with constraints

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
