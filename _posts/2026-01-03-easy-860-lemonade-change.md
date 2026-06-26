---
layout: post
title: "[Easy] 860. Lemonade Change"
date: 2026-01-03 01:00:00 -0700
categories: [leetcode, easy, array, greedy, simulation]
permalink: /2026/01/03/easy-860-lemonade-change/
---
At a lemonade stand, each lemonade costs `5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by `bills`). Each customer will only buy one lemonade and pay with either a `5`, `10`, or `20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `5`.

Note that you don't have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the `i`-th customer pays, return `true` if you can provide every customer with the correct change, or `false` otherwise.

## Examples

**Example 1:**
```
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three 5 bills in order.
From the fourth customer, we collect a 10 bill and give back a 5.
From the fifth customer, we collect a 20 bill and give back a 10 and a 5.
Since all customers got correct change, we output true.
```

**Example 2:**
```
Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two 5 bills.
For the next two customers, we collect a 10 bill and give back a 5 bill.
For the last customer, we collect a 20 bill but cannot give back change because we only have two 5 bills.
Since not every customer received correct change, the answer is false.
```

## Constraints

- `1 <= bills.length <= 10^5`
- `bills[i]` is either `5`, `10`, or `20`.

## Thinking Process

At a lemonade stand, each lemonade costs `5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by `bills`). Each customer will only buy one lemonade and pay with either a `5`, `10`, or `20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `5`.

Note that you don't have any change in hand at first.

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
| Sort + greedy | O(n \log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n \log n) | O(n) | Merge streams, room allocation |
| **Exchange argument** *(this problem)* | O(n) | O(1) | Prove greedy choice is safe |

## Solution

### **Solution: Greedy Change Giving**

```cpp
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0;
        for(auto& bill: bills) {
            if(bill == 5) {
                five++;
            } else if(bill == 10) {
                if(five == 0) return false;
                five--;
                ten++;
            } else {
                if(five > 0 && ten > 0) {
                    five--;
                    ten--;
                } else if(five >= 3) {
                    five -= 3;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
};
```

### Solution Explanation

**Approach:** Exchange argument (this problem)

**Key idea:** At a lemonade stand, each lemonade costs `5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by `bills`). Each customer will only buy one lemonade and pay with either a `5`, `10`, or `20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `5`.

**How the code works:**
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `bills = [5,5,5,10,20]`, expected output `true`:

From the first 3 customers, we collect three 5 bills in order.
From the fourth customer, we collect a 10 bill and give back a 5.
From the fifth customer, we collect a 20 bill and give back a 10 and a 5.
Since all customers got correct change, we output true.

**Time:** O(n) where n is the number of customers · **Space:** O(1)

### **Algorithm Explanation:**

1. **Initialize (Line 4)**:
   - `five`: Count of 5 bills
   - `ten`: Count of 10 bills
   - Don't need to track 20 bills (we never give them as change)

2. **Process Each Bill (Lines 5-20)**:
   - **5 Bill (Lines 6-8)**:
     - No change needed
     - Increment `five` counter
   
   - **10 Bill (Lines 9-12)**:
     - Need to give 5 change
     - Check if we have a 5 bill
     - If not, return `false` (cannot give change)
     - If yes, decrement `five` and increment `ten`
   
   - **20 Bill (Lines 13-19)**:
     - Need to give 15 change
     - **Greedy choice**: Prefer 10 + 5 (if available)
       - This preserves 5 bills for future 10 bills
     - **Fallback**: Use 3×5 (if no 10 available)
     - If neither option available, return `false`

### **Example Walkthrough:**

**Example 1: `bills = [5,5,5,10,20]`**

```
Initial: five=0, ten=0

Customer 1: 5
  five=1, ten=0
  Change: 0 ✓

Customer 2: 5
  five=2, ten=0
  Change: 0 ✓

Customer 3: 5
  five=3, ten=0
  Change: 0 ✓

Customer 4: 10
  Need: 5 change
  five=2, ten=1
  Change: 5 ✓

Customer 5: 20
  Need: 15 change
  Prefer: 10 + 5 (five=2>0, ten=1>0)
  five=1, ten=0
  Change: 15 ✓

Result: true
```

**Example 2: `bills = [5,5,10,10,20]`**

```
Initial: five=0, ten=0

Customer 1: 5
  five=1, ten=0
  Change: 0 ✓

Customer 2: 5
  five=2, ten=0
  Change: 0 ✓

Customer 3: 10
  Need: 5 change
  five=1, ten=1
  Change: 5 ✓

Customer 4: 10
  Need: 5 change
  five=0, ten=2
  Change: 5 ✓

Customer 5: 20
  Need: 15 change
  Prefer: 10 + 5 (five=0, cannot use)
  Fallback: 3×5 (five=0, cannot use)
  Cannot give change ✗

Result: false
```

**Example 3: `bills = [5,5,10,20]`**

```
Initial: five=0, ten=0

Customer 1: 5
  five=1, ten=0 ✓

Customer 2: 5
  five=2, ten=0 ✓

Customer 3: 10
  Need: 5
  five=1, ten=1 ✓

Customer 4: 20
  Need: 15
  Prefer: 10 + 5 (five=1>0, ten=1>0)
  five=0, ten=0 ✓

Result: true
```

## Algorithm Breakdown

### **Why Greedy Works**

The greedy strategy of preferring 10+5 over 3×5 for 20 change is optimal because:

1. **Preserve 5 Bills**: 5 bills are needed for 10 change
2. **10 Bills Less Useful**: 10 bills can only be used for 20 change
3. **Optimal Choice**: Using 10+5 preserves more 5 bills for future 10 bills
4. **No Regret**: If we can give change, we should (no benefit in saving)

### **Change Giving Logic**

**For 10 bill:**
- Always need exactly 1×5
- Simple check: `if(five == 0) return false`

**For 20 bill:**
- Need 15 change
- **Option 1**: 10 + 5 (preferred)
  - Uses 1×10 and 1×5
  - Preserves 5 bills
- **Option 2**: 3×5 (fallback)
  - Uses 3×5
  - Only if no 10 available

### **Why We Don't Track 20 Bills**

- We never give 20 bills as change (too large)
- We only receive 20 bills
- No need to track them

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the number of customers
  - Single pass through the bills array
  - Constant time operations for each bill
- **Space Complexity**: O(1)
  - Only using two integer counters
  - No additional data structures

## Key Points

1. **Greedy Strategy**: Prefer 10+5 over 3×5 for 20 change
2. **Bill Tracking**: Only need to track 5 and 10 bills
3. **Early Termination**: Return `false` immediately if change cannot be given
4. **Optimal**: Greedy approach is optimal for this problem
5. **Simple**: Straightforward simulation approach

## Common Mistakes

1. **All 5 bills**: `[5,5,5,5,5]` → return `true`
2. **All 10 bills**: `[10,10,10]` → return `false` (no 5 for first customer)
3. **All 20 bills**: `[20,20,20]` → return `false` (no change for first customer)
4. **Mixed, insufficient**: `[5,5,10,20]` → depends on order
5. **Single customer**: `[5]` → return `true`
6. **Single customer, 10**: `[10]` → return `false`

1. **Wrong priority**: Using 3×5 before 10+5 for 20 change
2. **Not checking**: Forgetting to check if change can be given
3. **Wrong change amount**: Giving wrong change (e.g., 10 for 20)
4. **Not tracking**: Forgetting to update bill counters

## Related Problems

- [455. Assign Cookies](https://www.leetcode.com/problems/assign-cookies/) - Greedy matching
- [122. Best Time to Buy and Sell Stock II](https://www.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) - Greedy trading
- [322. Coin Change](https://www.leetcode.com/problems/coin-change/) - DP coin change
- [518. Coin Change 2](https://www.leetcode.com/problems/coin-change-2/) - Count ways to make change

## Tags

`Array`, `Greedy`, `Simulation`, `Easy`

## Key Takeaways

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

## References

- [LC 860: Lemonade Change on LeetCode](https://www.leetcode.com/problems/lemonade-change/)
- [LeetCode Discuss — LC 860: Lemonade Change](https://www.leetcode.com/problems/lemonade-change/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/lemonade-change/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
