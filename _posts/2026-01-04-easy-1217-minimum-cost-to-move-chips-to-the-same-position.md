---
layout: post
title: "1217. Minimum Cost to Move Chips to The Same Position"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, easy, array, math, greedy]
permalink: /2026/01/04/easy-1217-minimum-cost-to-move-chips-to-the-same-position/
---

# 1217. Minimum Cost to Move Chips to The Same Position

## Problem Statement

We have `n` chips, where the position of the `i`-th chip is `position[i]`.

We need to move all the chips to **the same position**. In one step, we can change the position of the `i`-th chip from `position[i]` to:

- `position[i] + 2` or `position[i] - 2` with cost = **0**.
- `position[i] + 1` or `position[i] - 1` with cost = **1**.

Return *the minimum cost* needed to move all the chips to the same position.

## Examples

**Example 1:**
```
Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
```

**Example 2:**
```
Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position 3 to position 2. Each move has cost = 1. The total cost = 2.
```

**Example 3:**
```
Input: position = [1,1000000000]
Output: 1
Explanation: Move chip at position 1000000000 to position 1 with cost = 1.
```

## Constraints

- `1 <= position.length <= 100`
- `1 <= position[i] <= 10^9`

## Solution Approach

This is a **greedy algorithm** problem with a key mathematical insight. The crucial observation is that moving chips by 2 positions costs 0, while moving by 1 position costs 1.

### Key Insights:

1. **Parity Matters**: Chips at even positions can be moved to any even position for free (cost 0)
2. **Parity Matters**: Chips at odd positions can be moved to any odd position for free (cost 0)
3. **Cross-Parity Cost**: Moving from even to odd (or vice versa) costs 1 per chip
4. **Optimal Strategy**: 
   - Move all chips to either all even positions or all odd positions (cost 0)
   - Then move all chips from one parity to the other (cost 1 per chip)
   - Choose the parity with fewer chips to minimize cost

### Algorithm:

1. **Count Chips by Parity**: Count chips at even positions and odd positions
2. **Choose Minimum**: Return the minimum of the two counts
   - This represents moving all chips from the minority parity to the majority parity

## Solution

### **Solution: Greedy with Parity Counting**

```cpp
class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int even = 0, odd = 0;
        for(int pos : position) {
            if(pos % 2 == 0) {
                odd++;
            } else {
                even++;
            }
        }
        return min(odd, even);
    }
};
```

### **Algorithm Explanation:**

1. **Initialize Counters (Line 4)**:
   - `even`: Count of chips at odd positions (note: variable name is swapped)
   - `odd`: Count of chips at even positions (note: variable name is swapped)
   - **Note**: The variable names are swapped in the code, but the logic is correct

2. **Count Chips by Parity (Lines 5-10)**:
   - **For each chip position**:
     - **If position is even** (`pos % 2 == 0`):
       - Increment `odd` (counts even positions)
     - **If position is odd** (`pos % 2 != 0`):
       - Increment `even` (counts odd positions)

3. **Return Minimum (Line 11)**:
   - Return `min(odd, even)`
   - This is `min(count of even positions, count of odd positions)`
   - Represents the cost to move all chips from the minority parity to the majority parity

### **Why This Works:**

**Key Insight**: Moving by 2 positions costs 0, moving by 1 position costs 1.

**Strategy**:
1. **Step 1**: Move all chips to the same parity (even or odd) - **cost 0**
   - Chips at even positions → move to any even position (cost 0)
   - Chips at odd positions → move to any odd position (cost 0)
2. **Step 2**: Move all chips from one parity to the other - **cost 1 per chip**
   - If we have fewer chips at even positions, move them to odd positions
   - If we have fewer chips at odd positions, move them to even positions
   - Cost = number of chips in the minority parity

**Example Walkthrough:**

**Example 1: `position = [1,2,3]`**

**Count by parity:**
```
Position 1 (odd): 1 chip
Position 2 (even): 1 chip
Position 3 (odd): 1 chip

Even positions: 1 chip (at position 2)
Odd positions: 2 chips (at positions 1, 3)
```

**Execution:**
```
Step 1: Move all chips to same parity (cost 0)
  - Chip at position 1 (odd) → move to position 3 (odd): cost 0
  - Chip at position 2 (even) → move to position 2 (even): cost 0
  - Chip at position 3 (odd) → already at odd position: cost 0
  Result: 2 chips at odd positions, 1 chip at even position

Step 2: Move minority parity to majority (cost 1)
  - Move chip at even position (position 2) to odd position (position 1 or 3): cost 1
  Result: All chips at odd positions

Total cost: 0 + 1 = 1
```

**Code execution:**
```
Initial: even = 0, odd = 0

pos = 1: pos % 2 = 1 (odd) → even++ → even = 1
pos = 2: pos % 2 = 0 (even) → odd++ → odd = 1
pos = 3: pos % 2 = 1 (odd) → even++ → even = 2

even = 2 (counts odd positions)
odd = 1 (counts even positions)

min(odd, even) = min(1, 2) = 1
```

**Example 2: `position = [2,2,2,3,3]`**

**Count by parity:**
```
Position 2 (even): 3 chips
Position 3 (odd): 2 chips

Even positions: 3 chips
Odd positions: 2 chips
```

**Execution:**
```
Step 1: Move all chips to same parity (cost 0)
  - All chips at even positions → already at even: cost 0
  - All chips at odd positions → already at odd: cost 0

Step 2: Move minority parity to majority (cost 2)
  - Move 2 chips from odd positions to even positions: cost 2 (1 per chip)
  Result: All chips at even positions

Total cost: 0 + 2 = 2
```

**Code execution:**
```
Initial: even = 0, odd = 0

pos = 2: pos % 2 = 0 (even) → odd++ → odd = 1
pos = 2: pos % 2 = 0 (even) → odd++ → odd = 2
pos = 2: pos % 2 = 0 (even) → odd++ → odd = 3
pos = 3: pos % 2 = 1 (odd) → even++ → even = 1
pos = 3: pos % 2 = 1 (odd) → even++ → even = 2

even = 2 (counts odd positions)
odd = 3 (counts even positions)

min(odd, even) = min(3, 2) = 2
```

**Example 3: `position = [1,1000000000]`**

**Count by parity:**
```
Position 1 (odd): 1 chip
Position 1000000000 (even): 1 chip

Even positions: 1 chip
Odd positions: 1 chip
```

**Execution:**
```
Step 1: Move all chips to same parity (cost 0)
  - Chip at position 1 (odd) → already at odd: cost 0
  - Chip at position 1000000000 (even) → move to position 2 (even): cost 0
    (Move by 2 positions: 1000000000 - 2 = 999999998, then continue...)

Step 2: Move one chip from even to odd (cost 1)
  - Move chip at even position to odd position: cost 1

Total cost: 0 + 1 = 1
```

**Code execution:**
```
Initial: even = 0, odd = 0

pos = 1: pos % 2 = 1 (odd) → even++ → even = 1
pos = 1000000000: pos % 2 = 0 (even) → odd++ → odd = 1

even = 1 (counts odd positions)
odd = 1 (counts even positions)

min(odd, even) = min(1, 1) = 1
```

## Algorithm Breakdown

### **Why Parity Matters**

**Moving by 2 positions (cost 0):**
- Position `i` → Position `i+2` or `i-2`: **cost 0**
- This preserves parity (even stays even, odd stays odd)
- Can move any distance in steps of 2 for free

**Moving by 1 position (cost 1):**
- Position `i` → Position `i+1` or `i-1`: **cost 1**
- This changes parity (even becomes odd, odd becomes even)

### **Optimal Strategy**

1. **Group by Parity**: All chips at even positions can be moved to any even position for free
2. **Group by Parity**: All chips at odd positions can be moved to any odd position for free
3. **Choose Target Parity**: Choose the parity with more chips (majority)
4. **Move Minority**: Move all chips from minority parity to majority parity (cost 1 per chip)
5. **Total Cost**: Number of chips in minority parity

### **Mathematical Proof**

**Claim**: The minimum cost is `min(count_even, count_odd)`.

**Proof**:
- Moving chips within the same parity costs 0
- Moving chips from one parity to the other costs 1 per chip
- To have all chips at the same position, they must all be at the same parity
- We choose the parity with more chips (to minimize moves)
- Cost = number of chips we need to move = `min(count_even, count_odd)`

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the length of `position`
  - Single pass through the array to count chips by parity
- **Space Complexity**: O(1)
  - Only using two variables (`even`, `odd`)
  - No additional data structures

## Key Points

1. **Parity is Key**: The problem reduces to counting chips by parity
2. **Free Moves**: Moving by 2 positions costs 0 (preserves parity)
3. **Expensive Moves**: Moving by 1 position costs 1 (changes parity)
4. **Greedy Choice**: Always move chips from minority parity to majority parity
5. **Simple Solution**: Just count and return minimum

## Alternative Approaches

### **Approach 1: Parity Counting (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Optimal solution, most efficient

### **Approach 2: Try All Positions**
- **Time**: O(n × m) where m is the range of positions
- **Space**: O(1)
- **Not practical**: Too slow for large position values

### **Approach 3: Dynamic Programming**
- **Time**: O(n × m)
- **Space**: O(m)
- **Overkill**: Not needed, greedy is optimal

## Edge Cases

1. **All chips at same position**: `[1,1,1]` → return 0 (no moves needed)
2. **All chips at even positions**: `[2,4,6]` → return 0 (all same parity)
3. **All chips at odd positions**: `[1,3,5]` → return 0 (all same parity)
4. **Equal counts**: `[1,2]` → return 1 (move one chip)
5. **Large positions**: `[1,1000000000]` → return 1 (parity doesn't depend on magnitude)

## Common Mistakes

1. **Not understanding parity**: Trying to calculate actual distances
2. **Wrong counting**: Counting positions instead of chips
3. **Complex solution**: Trying to simulate moves instead of using parity
4. **Variable naming**: The code has swapped variable names (`even` counts odd, `odd` counts even), but logic is correct
5. **Overthinking**: The problem looks complex but has a simple parity-based solution

## Related Problems

- [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/) - Greedy matching
- [860. Lemonade Change](https://leetcode.com/problems/lemonade-change/) - Greedy change giving
- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) - Greedy profit maximization
- [55. Jump Game](https://leetcode.com/problems/jump-game/) - Greedy reachability

## Follow-Up: Why Parity Works

**Question**: Why does moving by 2 positions cost 0?

**Answer**: 
- Moving by 2 positions preserves parity
- Even + 2 = Even, Odd + 2 = Odd
- We can move any distance in steps of 2: `i → i+2 → i+4 → ... → i+2k` (all cost 0)
- Therefore, any chip at an even position can reach any even position for free
- Similarly, any chip at an odd position can reach any odd position for free

**Question**: Why does moving by 1 position cost 1?

**Answer**:
- Moving by 1 position changes parity
- Even + 1 = Odd, Odd + 1 = Even
- This is the only way to change parity, so it costs 1

## Tags

`Array`, `Math`, `Greedy`, `Easy`

