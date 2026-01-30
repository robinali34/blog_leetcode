---
layout: post
title: "860. Lemonade Change"
date: 2026-01-03 01:00:00 -0700
categories: [leetcode, easy, array, greedy, simulation]
permalink: /2026/01/03/easy-860-lemonade-change/
---

# 860. Lemonade Change

## Problem Statement

At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by `bills`). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you don't have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the `i`-th customer pays, return `true` if you can provide every customer with the correct change, or `false` otherwise.

## Examples

**Example 1:**
```
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we collect a $20 bill and give back a $10 and a $5.
Since all customers got correct change, we output true.
```

**Example 2:**
```
Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers, we collect a $10 bill and give back a $5 bill.
For the last customer, we collect a $20 bill but cannot give back change because we only have two $5 bills.
Since not every customer received correct change, the answer is false.
```

## Constraints

- `1 <= bills.length <= 10^5`
- `bills[i]` is either `5`, `10`, or `20`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Change availability**: Do we start with any change? (Assumption: Start with no change - need to make change from collected bills)

2. **Change priority**: When giving change, which bills should we use first? (Assumption: Use larger bills first when possible - greedy approach, but $5 bills are most valuable for change)

3. **Exact change**: Can we give exact change? (Assumption: Yes - must give exact change, cannot give more or less)

4. **Bill denominations**: What bills are available? (Assumption: Only $5, $10, $20 bills - per constraints)

5. **Customer order**: Are customers processed in the given order? (Assumption: Yes - process customers sequentially in the given order)

## Solution Approach

This is a **greedy algorithm** problem where we need to give change optimally. The key insight is to **prioritize using larger bills** when giving change for $20, to preserve $5 bills for future $10 bills.

### Key Insights:

1. **Track Bills**: Keep count of $5 and $10 bills (don't need to track $20)
2. **Greedy Strategy**: When giving change for $20, prefer $10+$5 over 3×$5
3. **Preserve $5 Bills**: $5 bills are most valuable (needed for $10 change)
4. **Simulation**: Process each customer in order and check if change can be given

### Algorithm:

1. **Initialize**: Counters for $5 and $10 bills
2. **For each bill**:
   - **$5**: Keep it (no change needed)
   - **$10**: Give back $5 (need one $5 bill)
   - **$20**: Give back $15 (prefer $10+$5, else 3×$5)
3. **Return**: `true` if all customers get change, `false` otherwise

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

### **Algorithm Explanation:**

1. **Initialize (Line 4)**:
   - `five`: Count of $5 bills
   - `ten`: Count of $10 bills
   - Don't need to track $20 bills (we never give them as change)

2. **Process Each Bill (Lines 5-20)**:
   - **$5 Bill (Lines 6-8)**:
     - No change needed
     - Increment `five` counter
   
   - **$10 Bill (Lines 9-12)**:
     - Need to give $5 change
     - Check if we have a $5 bill
     - If not, return `false` (cannot give change)
     - If yes, decrement `five` and increment `ten`
   
   - **$20 Bill (Lines 13-19)**:
     - Need to give $15 change
     - **Greedy choice**: Prefer $10 + $5 (if available)
       - This preserves $5 bills for future $10 bills
     - **Fallback**: Use 3×$5 (if no $10 available)
     - If neither option available, return `false`

### **Example Walkthrough:**

**Example 1: `bills = [5,5,5,10,20]`**

```
Initial: five=0, ten=0

Customer 1: $5
  five=1, ten=0
  Change: $0 ✓

Customer 2: $5
  five=2, ten=0
  Change: $0 ✓

Customer 3: $5
  five=3, ten=0
  Change: $0 ✓

Customer 4: $10
  Need: $5 change
  five=2, ten=1
  Change: $5 ✓

Customer 5: $20
  Need: $15 change
  Prefer: $10 + $5 (five=2>0, ten=1>0)
  five=1, ten=0
  Change: $15 ✓

Result: true
```

**Example 2: `bills = [5,5,10,10,20]`**

```
Initial: five=0, ten=0

Customer 1: $5
  five=1, ten=0
  Change: $0 ✓

Customer 2: $5
  five=2, ten=0
  Change: $0 ✓

Customer 3: $10
  Need: $5 change
  five=1, ten=1
  Change: $5 ✓

Customer 4: $10
  Need: $5 change
  five=0, ten=2
  Change: $5 ✓

Customer 5: $20
  Need: $15 change
  Prefer: $10 + $5 (five=0, cannot use)
  Fallback: 3×$5 (five=0, cannot use)
  Cannot give change ✗

Result: false
```

**Example 3: `bills = [5,5,10,20]`**

```
Initial: five=0, ten=0

Customer 1: $5
  five=1, ten=0 ✓

Customer 2: $5
  five=2, ten=0 ✓

Customer 3: $10
  Need: $5
  five=1, ten=1 ✓

Customer 4: $20
  Need: $15
  Prefer: $10 + $5 (five=1>0, ten=1>0)
  five=0, ten=0 ✓

Result: true
```

## Algorithm Breakdown

### **Why Greedy Works**

The greedy strategy of preferring $10+$5 over 3×$5 for $20 change is optimal because:

1. **Preserve $5 Bills**: $5 bills are needed for $10 change
2. **$10 Bills Less Useful**: $10 bills can only be used for $20 change
3. **Optimal Choice**: Using $10+$5 preserves more $5 bills for future $10 bills
4. **No Regret**: If we can give change, we should (no benefit in saving)

### **Change Giving Logic**

**For $10 bill:**
- Always need exactly 1×$5
- Simple check: `if(five == 0) return false`

**For $20 bill:**
- Need $15 change
- **Option 1**: $10 + $5 (preferred)
  - Uses 1×$10 and 1×$5
  - Preserves $5 bills
- **Option 2**: 3×$5 (fallback)
  - Uses 3×$5
  - Only if no $10 available

### **Why We Don't Track $20 Bills**

- We never give $20 bills as change (too large)
- We only receive $20 bills
- No need to track them

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the number of customers
  - Single pass through the bills array
  - Constant time operations for each bill
- **Space Complexity**: O(1)
  - Only using two integer counters
  - No additional data structures

## Key Points

1. **Greedy Strategy**: Prefer $10+$5 over 3×$5 for $20 change
2. **Bill Tracking**: Only need to track $5 and $10 bills
3. **Early Termination**: Return `false` immediately if change cannot be given
4. **Optimal**: Greedy approach is optimal for this problem
5. **Simple**: Straightforward simulation approach

## Alternative Approaches

### **Approach 1: Greedy (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Optimal solution, simple and efficient

### **Approach 2: Track All Bills**
- **Time**: O(n)
- **Space**: O(1)
- **Use when**: Need to track $20 bills (not necessary here)

### **Approach 3: Dynamic Programming**
- **Time**: O(n × amount)
- **Space**: O(amount)
- **Overkill**: Not needed, greedy is optimal

## Edge Cases

1. **All $5 bills**: `[5,5,5,5,5]` → return `true`
2. **All $10 bills**: `[10,10,10]` → return `false` (no $5 for first customer)
3. **All $20 bills**: `[20,20,20]` → return `false` (no change for first customer)
4. **Mixed, insufficient**: `[5,5,10,20]` → depends on order
5. **Single customer**: `[5]` → return `true`
6. **Single customer, $10**: `[10]` → return `false`

## Common Mistakes

1. **Wrong priority**: Using 3×$5 before $10+$5 for $20 change
2. **Not checking**: Forgetting to check if change can be given
3. **Wrong change amount**: Giving wrong change (e.g., $10 for $20)
4. **Not tracking**: Forgetting to update bill counters

## Related Problems

- [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/) - Greedy matching
- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) - Greedy trading
- [322. Coin Change](https://leetcode.com/problems/coin-change/) - DP coin change
- [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/) - Count ways to make change

## Tags

`Array`, `Greedy`, `Simulation`, `Easy`

