---
layout: post
title: "LeetCode 2365. Task Scheduler II"
date: 2026-04-10
categories: [leetcode, medium, hash-map, simulation]
tags: [leetcode, medium, hash-map, simulation, greedy]
permalink: /2026/04/10/medium-2365-task-scheduler-ii/
---

You are given a list of `tasks` to complete in order. Each day you can complete one task. After completing a task of type `t`, you must wait at least `space` days before doing another task of the **same type**. You may insert idle days as needed. Return the **minimum number of days** to finish all tasks.

## Examples

**Example 1:**

```
Input: tasks = [1,2,1,2,3,1], space = 3
Output: 9
Explanation:
  Day 1: task 1
  Day 2: task 2
  Day 3: idle (task 1 needs 3-day gap)
  Day 4: idle
  Day 5: task 1
  Day 6: task 2
  Day 7: task 3
  Day 8: idle
  Day 9: task 1
```

**Example 2:**

```
Input: tasks = [5,8,8,5], space = 2
Output: 6
Explanation:
  Day 1: task 5
  Day 2: task 8
  Day 3: idle (task 8 needs 2-day gap)
  Day 4: idle
  Day 5: task 8
  Day 6: task 5
```

## Constraints

- `1 <= tasks.length <= 10^5`
- `1 <= tasks[i] <= 10^9`
- `1 <= space <= tasks.length`

## Thinking Process

We must process tasks **in order** (no reordering). For each task, either:

1. **Enough time has passed** since the last same-type task -- do it on the next day (`day + 1`)
2. **Not enough time** -- we must wait, jumping to `lastSeen[t] + space + 1`

A hash map tracking the **last day** each task type was performed gives us $O(1)$ lookup per task.

### Walk-through

```
tasks = [1, 2, 1, 2, 3, 1], space = 3

task 1: first time → day=1, lastSeen[1]=1
task 2: first time → day=2, lastSeen[2]=2
task 1: day-lastSeen[1] = 2-1 = 1 ≤ 3 → day=1+3+1=5, lastSeen[1]=5
task 2: day-lastSeen[2] = 5-2 = 3 ≤ 3 → day=2+3+1=6, lastSeen[2]=6
task 3: first time → day=7, lastSeen[3]=7
task 1: day-lastSeen[1] = 7-5 = 2 ≤ 3 → day=5+3+1=9, lastSeen[1]=9

Answer: 9 ✓
```

## Solution: Hash Map + Simulation -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    long long taskSchedulerII(vector<int>& tasks, int space) {
        unordered_map<int, long long> lastSeen;
        long long day = 0;

        for (int t : tasks) {
            if (lastSeen.find(t) == lastSeen.end()) {
                day += 1;
            } else {
                if (day - lastSeen[t] <= space) {
                    day = lastSeen[t] + space + 1;
                } else {
                    day += 1;
                }
            }
            lastSeen[t] = day;
        }
        return day;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$ -- hash map for last-seen days

## Key Details

**Why `lastSeen[t] + space + 1`?** If the last occurrence was on day $d$, the earliest we can do the same task again is day $d + \text{space} + 1$ (the gap of `space` days between them).

**Why `long long`?** With $10^5$ tasks and each potentially adding `space` ($\leq 10^5$) idle days, the total days can reach $\sim 10^{10}$.

**Why not just `day++` always?** When we need to wait, we jump forward in time. This is a simulation that skips idle days rather than counting them one by one, keeping the algorithm $O(n)$.

## Common Mistakes

- Using `int` for `day` (overflows when many idle days accumulate)
- Checking `day - lastSeen[t] < space` instead of `<= space` (off-by-one: need **at least** `space` days between, meaning `space + 1` total)
- Trying to reorder tasks (the problem requires tasks to be completed in the given order)

## Key Takeaways

- **"Execute in order with cooldown per type"** = greedy simulation with last-seen tracking
- Jump forward instead of incrementing through idle days -- keeps it $O(n)$ regardless of `space` size
- Unlike LC 621 Task Scheduler (which allows reordering), this problem fixes the order, making it a simpler simulation

## Related Problems

- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) -- allows reordering, greedy + math
- [1115. Print FooBar Alternately](https://leetcode.com/problems/print-foobar-alternately/) -- ordered scheduling with constraints
- [362. Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) -- time-based tracking

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
