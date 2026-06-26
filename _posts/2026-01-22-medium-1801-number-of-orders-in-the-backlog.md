---
layout: post
title: "[Medium] 1801. Number of Orders in the Backlog"
date: 2026-01-22 00:00:00 -0700
categories: [leetcode, medium, array, heap, priority-queue, simulation]
permalink: /2026/01/22/medium-1801-number-of-orders-in-the-backlog/
tags: [leetcode, medium, array, heap, priority-queue, simulation, greedy]
---
You are given a 2D integer array `orders`, where `orders[i] = [price_i, amount_i, orderType_i]` denotes that `amount_i` orders have been placed of type `orderType_i` at price `price_i`. The `orderType_i` is:

- `0` if it is a batch of **buy orders**, or
- `1` if it is a batch of **sell orders**.

Note that `orders[i]` represents a batch of `amount_i` independent orders with the same price and type. All orders represented by `orders[i]` will be placed before all orders represented by `orders[i+1]` for all valid `i`.

There is a **backlog** that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:

- If the order is a **buy order**, you look at the **sell order** with the **smallest price** in the backlog. If that sell order's price is **smaller than or equal to** the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.
- Vice versa, if the order is a **sell order**, you look at the **buy order** with the **largest price** in the backlog. If that buy order's price is **larger than or equal to** the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.

Return *the total **amount** of orders in the backlog after placing all the orders from the input*. Since the number can be large, return it **modulo** `10^9 + 7`.

## Examples

**Example 1:**

```
Input: orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
Output: 6
Explanation: Here is what happens with the orders:
- 5 orders of type buy with price 10 are placed. There are no sell orders in the backlog, so the 5 orders are added to the backlog.
- 2 orders of type sell with price 15 are placed. There are no buy orders in the backlog with price >= 15, so the 2 orders are added to the backlog.
- 1 order of type sell with price 25 is placed. There are no buy orders in the backlog with price >= 25, so it is added to the backlog.
- 4 orders of type buy with price 30 are placed. The first sell order with price 15 is matched and removed, and 4 is reduced by 1 to 3. The second sell order with price 15 is matched and removed, and 3 is reduced by 2 to 1. The third sell order with price 25 is matched and removed, and 1 is reduced by 1 to 0. The 4 buy orders with price 30 are now added to the backlog.
Finally, the backlog has 5 + 1 = 6 orders. So we return 6.
```

**Example 2:**

```
Input: orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
Output: 999999984
Explanation: Here is what happens with the orders:
- 10^9 orders of type sell with price 7 are placed. There are no buy orders, so the 10^9 orders are added to the backlog.
- 3 orders of type buy with price 15 are placed. They are matched with the 3 sell orders with the smallest price, which is 7, and these 3 sell orders are removed from the backlog.
- 999999995 orders of type buy with price 5 are placed. The sell order with price 7 should be matched, but since the buy order price is 5 < 7, it is not matched. Instead, 999999995 orders are added to the backlog.
- 1 order of type sell with price 5 is placed. This sell order is matched with a buy order of price 5, so 1 buy order is removed, and 999999994 orders remain in the backlog.
Finally, the backlog has (10^9 - 3) + 999999994 = 1999999991 orders. So we return 1999999991 mod 10^9 + 7 = 999999984.
```

## Constraints

- `1 <= orders.length <= 10^5`
- `orders[i].length == 3`
- `1 <= price_i, amount_i <= 10^9`
- `orderType_i` is either `0` or `1`.

## Thinking Process

1. **Heap Selection**:
- Max heap for buy orders (want highest price)
- Min heap for sell orders (want lowest price)
- Always match with best available price

- Heap gives fast access to min/max without full sorting.
- Size-k heap handles Top-K in O(n log k).
- Lazy deletion when elements leave the heap before removal.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 120" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary heap</text>

  <circle cx="140" cy="35" r="16" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="39" text-anchor="middle" font-size="11">1</text>
  <circle cx="90" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="90" y="79" text-anchor="middle" font-size="10">3</text>
  <circle cx="190" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="190" y="79" text-anchor="middle" font-size="10">2</text>
  <line x1="140" y1="51" x2="90" y2="61" stroke="#9A9792"/><line x1="140" y1="51" x2="190" y2="61" stroke="#9A9792"/>
  <text x="140" y="110" text-anchor="middle" font-size="11" fill="#6B6560">parent ≤ children (min-heap)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Min/max heap** *(this problem)* | O(n log k) | O(k) | Top-K, streaming median |
| Two heaps | O(n log n) | O(n) | Median from data stream |
| Heap + lazy deletion | O(n log n) | O(n) | Delayed removal |
| Priority-driven search | O(n log n) | O(n) | Dijkstra, best-first expansion |

## Solution

```cpp
class Solution {
public:
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        const int MOD = 1e9 +7;
        priority_queue<pair<int, int>> buy;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> sell;
        for(auto& o: orders) {
            int price = o[0], amount = o[1], type = o[2];
            if(type == 0) {
                while(amount > 0 && !sell.empty() && sell.top().first <= price) {
                    auto [sellPrice, sellAmount] = sell.top();
                    sell.pop();
                    int matched = min(amount, sellAmount);
                    amount -= matched;
                    sellAmount -= matched;
                    if (sellAmount > 0) {
                        sell.push({sellPrice, sellAmount});
                    }
                }
                if(amount > 0) {
                    buy.push({price, amount});
                }
            } else {
                while(amount > 0 && !buy.empty() && buy.top().first >= price) {
                    auto [buyPrice, buyAmount] = buy.top();
                    buy.pop();
                    int matched = min(amount, buyAmount);
                    amount -= matched;
                    buyAmount -= matched;
                    if(buyAmount > 0) {
                        buy.push({buyPrice, buyAmount});
                    }
                }
                if(amount > 0) {
                    sell.push({price, amount});
                }
            }
        } 
        long long rtn = 0;
        while(!buy.empty()) {
            rtn = (rtn + buy.top().second) % MOD;
            buy.pop();
        }
        while(!sell.empty()) {
            rtn = (rtn + sell.top().second) % MOD;
            sell.pop();
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Min/max heap (this problem)

**Key idea:** 1. **Heap Selection**:

**How the code works:**
1. **Heap Selection**:
- Max heap for buy orders (want highest price)
- Min heap for sell orders (want lowest price)
- Always match with best available price
- Heap gives fast access to min/max without full sorting.
- Size-k heap handles Top-K in O(n log k).

**Walkthrough** — input `orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]`, expected output `6`:

Here is what happens with the orders:
- 5 orders of type buy with price 10 are placed. There are no sell orders in the backlog, so the 5 orders are added to the backlog.
- 2 orders of type sell with price 15 are placed. There are no buy orders in the backlog with price >= 15, so the 2 orders are added to the backlog.
- 1 order of type sell with price 25 is placed. There are no buy orders in the backlog with price >= 25, so it is added to the backlog.
- 4 orders of type buy with price 30 are placed. The first sell order with price 15 is matched and removed, and 4 is reduced by 1 to 3. The second sell order with price 15 is matched and removed, and 3 is reduced by 2 to 1. The third sell order with price 25 is matched and removed, and 1 is reduced by 1 to 0. The 4 buy orders with price 30 are now added to the backlog.
Finally, the backlog has 5 + 1 = 6 orders. So we return 6.
## Common Mistakes

1. **No matches**: All orders added to backlog
   - `orders = [[10,5,0],[20,3,1]]` → buy: 5, sell: 3, total: 8

2. **Complete matching**: All orders matched
   - `orders = [[10,5,0],[10,5,1]]` → buy: 0, sell: 0, total: 0

3. **Partial matching**: Some orders partially matched
   - `orders = [[10,5,0],[8,3,1]]` → buy: 2, sell: 0, total: 2

4. **Large amounts**: Handle modulo correctly
   - Example 2 shows handling of 10^9 amounts

5. **Empty backlog**: No orders remain
   - All orders matched perfectly

1. **Wrong heap type**: Using min heap for buy orders or max heap for sell orders
2. **Incorrect matching condition**: 
   - Buy matches when `buyPrice >= sellPrice` (not `>`)
   - Sell matches when `sellPrice <= buyPrice` (not `<`)
3. **Not handling partial matches**: Forgetting to push back remaining amounts
4. **Modulo overflow**: Not applying modulo during accumulation
5. **Empty heap access**: Not checking if heap is empty before accessing top
6. **Integer overflow**: Not using `long long` for result accumulation

## Related Problems

- [LC 1701: Average Waiting Time](https://robinali34.github.io/blog_leetcode/2026/01/19/medium-1701-average-waiting-time/) - Order processing simulation
- [LC 1834: Single-Threaded CPU](https://www.leetcode.com/problems/single-threaded-cpu/) - Priority queue for task scheduling
- [LC 621: Task Scheduler](https://www.leetcode.com/problems/task-scheduler/) - Task scheduling with constraints
- [LC 253: Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/) - Resource allocation

## Key Takeaways

1. **Heap Selection**: 
   - Max heap for buy orders (want highest price)
   - Min heap for sell orders (want lowest price)
2. **Matching Strategy**: 
   - Always match with best available price
   - Partial matching is allowed
3. **Order Processing**: 
   - Process orders sequentially
   - Match greedily until no more matches possible
4. **Modulo Arithmetic**: 
   - Use modulo when summing to prevent overflow
   - Apply modulo at each addition step

## References

- [LC 1801: Number of Orders in the Backlog on LeetCode](https://www.leetcode.com/problems/number-of-orders-in-the-backlog/)
- [LeetCode Discuss — LC 1801: Number of Orders in the Backlog](https://www.leetcode.com/problems/number-of-orders-in-the-backlog/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/number-of-orders-in-the-backlog/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
