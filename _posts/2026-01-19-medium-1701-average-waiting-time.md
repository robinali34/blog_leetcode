---
layout: post
title: "[Medium] 1701. Average Waiting Time"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, medium, array, simulation]
permalink: /2026/01/19/medium-1701-average-waiting-time/
tags: [leetcode, medium, array, simulation, greedy]
---
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

## Thinking Process

1. **Single Server Queue**: Classic queueing theory problem

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | $O(n \log n)$ | $O(1)$ | Interval scheduling, assignment |
| Local greedy choice | $O(n)$ | $O(1)$ | Jump game, gas station |
| Greedy + heap | $O(n \log n)$ | $O(n)$ | Merge streams, room allocation |
| Exchange argument | $O(n)$ | $O(1)$ | Prove greedy choice is safe |

## Solution

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

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** 1. **Single Server Queue**: Classic queueing theory problem

**How the code works:**
1. **Single Server Queue**: Classic queueing theory problem
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `customers = [[1,2],[2,5],[4,3]]`, expected output `5.00000`:

1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
So the average waiting time = (2 + 6 + 7) / 3 = 5.00000.
## Comparison of Solutions

| Solution | Code Length | Readability | Logic Clarity |
|----------|-------------|-------------|---------------|
| **Solution 1** | Longer | More explicit | Clear if-else logic |
| **Solution 2** | Shorter | More concise | Elegant `max()` usage |

## Common Mistakes

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

1. **Wrong waiting time calculation**: Using `start_time - arrival` instead of `finish_time - arrival`
2. **Not handling chef idle case**: Assuming chef is always busy
3. **Integer overflow**: Not using `long long` for large sums
4. **Wrong order processing**: Processing orders out of sequence
5. **Precision issues**: Not using `double` for division

## Related Problems

- [LC 1834: Single-Threaded CPU](https://www.leetcode.com/problems/single-threaded-cpu/) - Similar queue processing with priority
- [LC 1882: Process Tasks Using Servers](https://www.leetcode.com/problems/process-tasks-using-servers/) - Multiple servers, task scheduling
- [LC 621: Task Scheduler](https://www.leetcode.com/problems/task-scheduler/) - Task scheduling with cooldown
- [LC 253: Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/) - Resource allocation, similar simulation

## Key Takeaways

1. **Single Server Queue**: Classic queueing theory problem
2. **Sequential Processing**: Orders processed in arrival order
3. **Waiting Time Formula**: `finish_time - arrival_time`
4. **Chef Availability**: `start_time = max(chef_free_time, arrival_time)`
5. **Finish Time**: `finish_time = start_time + order_time`

## References

- [LC 1701: Average Waiting Time on LeetCode](https://www.leetcode.com/problems/average-waiting-time/)
- [LeetCode Discuss — LC 1701: Average Waiting Time](https://www.leetcode.com/problems/average-waiting-time/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/average-waiting-time/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
