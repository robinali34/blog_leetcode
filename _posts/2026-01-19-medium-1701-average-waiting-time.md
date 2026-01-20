---
layout: post
title: "1701. Average Waiting Time"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, medium, array, simulation]
permalink: /2026/01/19/medium-1701-average-waiting-time/
tags: [leetcode, medium, array, simulation, greedy]
---

# 1701. Average Waiting Time

## Problem Statement

There is a restaurant with a single chef. You are given an array `customers`, where `customers[i] = [arrival_i, time_i]`:

- `arrival_i` is the arrival time of the `i`th customer. The arrival times are sorted in **non-decreasing** order.
- `time_i` is the time needed to prepare the order of the `i`th customer.

When a customer arrives, he gives his order to the chef, and the chef starts preparing it once he is idle. The customer waits until his order is prepared. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers **in the order they were given in the input**.

Return *the **average waiting time** of all customers*. Solutions within `10^-5` from the actual answer are considered accepted.

## Examples

**Example 1:**
```
Input: customers = [[1,2],[2,5],[4,3]]
Output: 5.00000
Explanation:
1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
So the average waiting time = (2 + 6 + 7) / 3 = 5.00000.
```

**Example 2:**
```
Input: customers = [[5,2],[5,4],[10,3],[20,2]]
Output: 3.25000
Explanation:
1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 22, so the waiting time of the fourth customer is 22 - 20 = 2.
So the average waiting time = (2 + 6 + 4 + 2) / 4 = 3.25000.
```

## Constraints

- `1 <= customers.length <= 10^5`
- `1 <= arrival_i, time_i <= 10^4`
- `arrival_i <= arrival_{i+1}` (arrival times are sorted in non-decreasing order)

## Solution Approach

This problem simulates a single-server queue system where customers arrive and wait for service. The key is to track when the chef becomes available and calculate waiting time for each customer.

### Key Insights:

1. **Chef Availability**: Chef can start next order only when idle
2. **Waiting Time**: `waiting_time = finish_time - arrival_time`
3. **Finish Time**: `finish_time = max(chef_free_time, arrival_time) + order_time`
4. **Sequential Processing**: Orders are processed in the given order

## Solution 1: Explicit Simulation (If-Else)

```cpp
class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        long long t = 0, totalTime = 0;
        for(auto& c: customers) {
            int arrival = c[0], order = c[1];
            if(t > arrival) {
                totalTime += t - arrival;
            } else {
                t = arrival;
            }
            totalTime += order;
            t += order;
        }
        return (double) totalTime / customers.size();
    }
};
```

### Algorithm Explanation:

1. **Initialize Variables**:
   - `t`: Current time when chef becomes free (finish time of previous order)
   - `totalTime`: Cumulative waiting time for all customers

2. **Process Each Customer**:
   - Extract `arrival` and `order` time
   - **If chef is busy** (`t > arrival`):
     - Customer waits: `totalTime += t - arrival`
   - **If chef is idle** (`t <= arrival`):
     - Chef starts immediately: `t = arrival`
   - Add order preparation time: `totalTime += order`
   - Update chef free time: `t += order`

3. **Return Average**: `totalTime / customers.size()`

### Example Walkthrough:

**Input:** `customers = [[1,2],[2,5],[4,3]]`

```
Customer 1: arrival=1, order=2
  t=0 <= arrival=1 → chef idle, start at 1
  totalTime += 0 (no wait) + 2 (order) = 2
  t = 1 + 2 = 3
  Waiting time: 3 - 1 = 2 ✓

Customer 2: arrival=2, order=5
  t=3 > arrival=2 → chef busy, wait until 3
  totalTime += (3 - 2) = 1 + 5 = 6
  t = 3 + 5 = 8
  Waiting time: 8 - 2 = 6 ✓

Customer 3: arrival=4, order=3
  t=8 > arrival=4 → chef busy, wait until 8
  totalTime += (8 - 4) = 4 + 3 = 7
  t = 8 + 3 = 11
  Waiting time: 11 - 4 = 7 ✓

Average: (2 + 6 + 7) / 3 = 5.0 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Single pass through customers array
  - Each customer processed in O(1) time

- **Space Complexity:** O(1)
  - Only using constant extra variables (`t`, `totalTime`)
  - No additional data structures

## Solution 2: Simplified with `max()` (More Concise)

```cpp
class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        long long t = 0, totalTime = 0;
        for(auto& c: customers) {
            int arrival = c[0], order = c[1];
            t = max(t, (long long)arrival) + order;
            totalTime += t - arrival;
        }
        return (double) totalTime / customers.size();
    }
};
```

### Algorithm Explanation:

1. **Initialize Variables**: Same as Solution 1

2. **Process Each Customer**:
   - **Update chef free time**: `t = max(t, arrival) + order`
     - `max(t, arrival)` ensures chef starts at the later of:
       - When chef becomes free (`t`)
       - When customer arrives (`arrival`)
   - **Calculate waiting time**: `totalTime += t - arrival`
     - `t` is now the finish time
     - Waiting time = finish time - arrival time

3. **Return Average**: `totalTime / customers.size()`

### Key Insight:

The `max(t, arrival)` elegantly handles both cases:
- **Chef idle**: `t <= arrival` → start at `arrival`
- **Chef busy**: `t > arrival` → start at `t`

### Example Walkthrough:

**Input:** `customers = [[1,2],[2,5],[4,3]]`

```
Customer 1: arrival=1, order=2
  t = max(0, 1) + 2 = 1 + 2 = 3
  totalTime += 3 - 1 = 2
  Waiting time: 2 ✓

Customer 2: arrival=2, order=5
  t = max(3, 2) + 5 = 3 + 5 = 8
  totalTime += 8 - 2 = 6
  Waiting time: 6 ✓

Customer 3: arrival=4, order=3
  t = max(8, 4) + 3 = 8 + 3 = 11
  totalTime += 11 - 4 = 7
  Waiting time: 7 ✓

Average: (2 + 6 + 7) / 3 = 5.0 ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Single pass through customers array
  - Each customer processed in O(1) time

- **Space Complexity:** O(1)
  - Only using constant extra variables
  - More concise than Solution 1

## Comparison of Solutions

| Solution | Code Length | Readability | Logic Clarity |
|----------|-------------|-------------|---------------|
| **Solution 1** | Longer | More explicit | Clear if-else logic |
| **Solution 2** | Shorter | More concise | Elegant `max()` usage |

## Key Insights

1. **Single Server Queue**: Classic queueing theory problem
2. **Sequential Processing**: Orders processed in arrival order
3. **Waiting Time Formula**: `finish_time - arrival_time`
4. **Chef Availability**: `start_time = max(chef_free_time, arrival_time)`
5. **Finish Time**: `finish_time = start_time + order_time`

## Edge Cases

1. **All customers arrive before chef finishes**: Chef always busy
   - `customers = [[1,10],[2,5],[3,3]]`
   - Each customer waits for previous to finish

2. **Chef always idle**: Customers arrive after chef finishes
   - `customers = [[1,2],[5,3],[10,1]]`
   - No waiting time, only order preparation time

3. **Single customer**: `customers = [[1,5]]`
   - Waiting time = order time = 5

4. **Simultaneous arrivals**: Multiple customers arrive at same time
   - `customers = [[5,2],[5,4],[5,3]]`
   - Processed sequentially, later ones wait longer

## Common Mistakes

1. **Wrong waiting time calculation**: Using `start_time - arrival` instead of `finish_time - arrival`
2. **Not handling chef idle case**: Assuming chef is always busy
3. **Integer overflow**: Not using `long long` for large sums
4. **Wrong order processing**: Processing orders out of sequence
5. **Precision issues**: Not using `double` for division

## Related Problems

- [LC 1834: Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) - Similar queue processing with priority
- [LC 1882: Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/) - Multiple servers, task scheduling
- [LC 621: Task Scheduler](https://leetcode.com/problems/task-scheduler/) - Task scheduling with cooldown
- [LC 253: Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) - Resource allocation, similar simulation

---

*This problem demonstrates **simulation of a single-server queue system**. The key insight is using `max(chef_free_time, arrival_time)` to determine when the chef can start the next order, elegantly handling both idle and busy states.*

