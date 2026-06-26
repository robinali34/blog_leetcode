---
layout: post
title: "[Medium] 1029. Two City Scheduling"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, medium, array, greedy, sorting]
permalink: /2026/01/04/medium-1029-two-city-scheduling/
---
A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCosti, bCosti]`, the cost of flying the `i`-th person to city `a` is `aCosti`, and the cost of flying the `i`-th person to city `b` is `bCosti`.

Return *the minimum cost to fly every person to a city such that exactly `n` people arrive in each city*.

## Examples

**Example 1:**
```
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
```

**Example 2:**
```
Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
```

**Example 3:**
```
Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
```

## Constraints

- `2 * n == costs.length`
- `2 <= costs.length <= 100`
- `costs.length` is even
- `1 <= aCosti, bCosti <= 1000`

## Thinking Process

A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCosti, bCosti]`, the cost of flying the `i`-th person to city `a` is `aCosti`, and the cost of flying the `i`-th person to city `b` is `bCosti`.

Return *the minimum cost to fly every person to a city such that exactly `n` people arrive in each city*.

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
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

## Solution

### **Solution: Greedy with Sorting by Difference**

```cpp
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        sort(costs.begin(), costs.end(), [](auto& u, auto&v) {
            return (u[0] - u[1] < v[0] - v[1]);
        });
        int total = 0;
        const int N = costs.size() / 2;
        for(int i = 0; i < N; i++) {
            total += costs[i][0] + costs[i + N][1];
        }
        return total;
    }
};
```

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCosti, bCosti]`, the cost of flying the `i`-th person to city `a` is `aCosti`, and the cost of flying the `i`-th person to city `b` is `bCosti`.

**How the code works:**
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `costs = [[10,20],[30,200],[400,50],[30,20]]`, expected output `110`:

The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

**Time:** O(n log n) where n is the number of people · **Space:** O(1)

### **Algorithm Explanation:**

1. **Sort by Cost Difference (Lines 4-6)**:
   - Sort `costs` by `cost[0] - cost[1]` in ascending order
   - Custom comparator: `u[0] - u[1] < v[0] - v[1]`
   - **Why**: People with smaller differences (cheaper to send to A) come first
   - **Why**: People with larger differences (cheaper to send to B) come last

2. **Initialize (Lines 7-8)**:
   - `total`: Total cost (starts at 0)
   - `N`: Half the number of people (`costs.size() / 2`)

3. **Assign and Sum (Lines 9-12)**:
   - **For first `N` people** (`i = 0` to `N-1`):
     - Add `costs[i][0]` (send to city A)
   - **For last `N` people** (`i = N` to `2N-1`):
     - Add `costs[i + N][1]` (send to city B)
   - **Note**: `costs[i + N]` accesses the `(i+N)`-th element, which is in the second half

4. **Return (Line 13)**:
   - Return the total cost

### **Why This Works:**

**Key Insight**: The difference `cost[0] - cost[1]` tells us the "savings" from sending a person to city A instead of city B.

**Strategy**:
1. **Sort by difference**: People with negative differences (cheaper to A) come first
2. **Send first N to A**: These people save money by going to A
3. **Send last N to B**: These people save money by going to B (or lose less)
4. **Optimal**: This maximizes total savings

**Mathematical Proof**:
- If we send person `i` to city A: cost = `costs[i][0]`
- If we send person `i` to city B: cost = `costs[i][1]`
- Savings from sending to A: `costs[i][1] - costs[i][0] = -(costs[i][0] - costs[i][1])`
- To maximize savings, send people with largest `(costs[i][1] - costs[i][0])` to A
- Equivalently, send people with smallest `(costs[i][0] - costs[i][1])` to A

**Example Walkthrough:**

**Example 1: `costs = [[10,20],[30,200],[400,50],[30,20]]`**

**Calculate differences:**
```
Person 0: [10, 20] → difference = 10 - 20 = -10 (cheaper to A)
Person 1: [30, 200] → difference = 30 - 200 = -170 (cheaper to A)
Person 2: [400, 50] → difference = 400 - 50 = 350 (cheaper to B)
Person 3: [30, 20] → difference = 30 - 20 = 10 (cheaper to B)
```

**After sorting by difference (ascending):**
```
Sorted: [[30, 200], [10, 20], [30, 20], [400, 50]]
        (diff=-170)  (diff=-10)  (diff=10)  (diff=350)
```

**Execution:**
```
N = 4 / 2 = 2

First N (i=0,1): Send to city A
  i=0: costs[0][0] = 30
  i=1: costs[1][0] = 10

Last N (i=0,1): Send to city B
  i=0: costs[0+2][1] = costs[2][1] = 20
  i=1: costs[1+2][1] = costs[3][1] = 50

Total = 30 + 10 + 20 + 50 = 110
```

**Verification:**
```
Person 0: [30, 200] → Send to A: 30 ✓
Person 1: [10, 20] → Send to A: 10 ✓
Person 2: [30, 20] → Send to B: 20 ✓
Person 3: [400, 50] → Send to B: 50 ✓
Total: 30 + 10 + 20 + 50 = 110
```

**Example 2: `costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]`**

**Calculate differences:**
```
Person 0: [259, 770] → diff = 259 - 770 = -511
Person 1: [448, 54] → diff = 448 - 54 = 394
Person 2: [926, 667] → diff = 926 - 667 = 259
Person 3: [184, 139] → diff = 184 - 139 = 45
Person 4: [840, 118] → diff = 840 - 118 = 722
Person 5: [577, 469] → diff = 577 - 469 = 108
```

**After sorting by difference (ascending):**
```
Sorted: [[259, 770], [184, 139], [577, 469], [926, 667], [448, 54], [840, 118]]
        (diff=-511)  (diff=45)   (diff=108)  (diff=259)  (diff=394)  (diff=722)
```

**Execution:**
```
N = 6 / 2 = 3

First N (i=0,1,2): Send to city A
  i=0: costs[0][0] = 259
  i=1: costs[1][0] = 184
  i=2: costs[2][0] = 577

Last N (i=0,1,2): Send to city B
  i=0: costs[0+3][1] = costs[3][1] = 667
  i=1: costs[1+3][1] = costs[4][1] = 54
  i=2: costs[2+3][1] = costs[5][1] = 118

Total = 259 + 184 + 577 + 667 + 54 + 118 = 1859
```

## Algorithm Breakdown

### **Why Sorting by Difference Works**

**Key Insight**: The difference `cost[0] - cost[1]` represents the "penalty" for choosing city A over city B.

**Analysis**:
- **Negative difference** (`cost[0] - cost[1] < 0`): `cost[0] < cost[1]` → Cheaper to send to A
- **Positive difference** (`cost[0] - cost[1] > 0`): `cost[0] > cost[1]` → Cheaper to send to B
- **Zero difference** (`cost[0] - cost[1] = 0`): Same cost to both cities

**Sorting Strategy**:
- Sort by `cost[0] - cost[1]` in **ascending order**
- First half (smallest differences) → Send to city A (minimize penalty)
- Second half (largest differences) → Send to city B (minimize penalty)

### **Why This is Optimal**

**Greedy Choice Property**:
- For each person, we want to minimize their cost
- Sorting by difference ensures we make locally optimal choices
- The constraint (exactly N people to each city) is satisfied by the split

**Optimal Substructure**:
- After sorting, the problem reduces to: send first N to A, last N to B
- This is optimal because we're maximizing total savings

### **Alternative Interpretation**

**Cost Savings**:
- Savings from sending person `i` to A: `costs[i][1] - costs[i][0]`
- To maximize total savings, send people with largest savings to A
- Equivalently, send people with smallest `(costs[i][0] - costs[i][1])` to A

## Time & Space Complexity

- **Time Complexity**: O(n log n) where n is the number of people
  - **Sorting**: O(n log n) - dominates the time complexity
  - **Summing**: O(n) - single pass through sorted array
  - **Total**: O(n log n)
- **Space Complexity**: O(1)
  - Only using a few variables (`total`, `N`, `i`)
  - Sorting is typically in-place (O(1) extra space)

## Key Points

1. **Sort by Difference**: Sort by `cost[0] - cost[1]` to identify which city is cheaper
2. **Greedy Assignment**: Send first N to city A, last N to city B
3. **Optimal**: This greedy strategy minimizes total cost
4. **Simple**: Straightforward implementation after sorting
5. **Efficient**: O(n log n) time complexity

## Common Mistakes

1. **All same cost**: `[[1,1],[2,2],[3,3],[4,4]]` → Any assignment works
2. **All cheaper to A**: `[[1,100],[2,200],[3,300],[4,400]]` → Send first 2 to A, last 2 to A (but constraint: need 2 to B)
3. **All cheaper to B**: `[[100,1],[200,2],[300,3],[400,4]]` → Send first 2 to A, last 2 to B
4. **Mixed**: `[[10,20],[30,200],[400,50],[30,20]]` → Example 1

1. **Wrong sorting order**: Sorting in descending instead of ascending
2. **Wrong assignment**: Sending first N to B instead of A
3. **Index errors**: Incorrectly accessing `costs[i + N]`
4. **Not understanding difference**: Not realizing what the difference represents
5. **Forgetting constraint**: Not ensuring exactly N people to each city

## Related Problems

- [406. Queue Reconstruction by Height](https://www.leetcode.com/problems/queue-reconstruction-by-height/) - Greedy with sorting
- [435. Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/) - Greedy interval selection
- [455. Assign Cookies](https://www.leetcode.com/problems/assign-cookies/) - Greedy matching
- [1710. Maximum Units on a Truck](https://www.leetcode.com/problems/maximum-units-on-a-truck/) - Greedy with sorting

## Follow-Up: Why Sort by Difference?

**Question**: Why does sorting by `cost[0] - cost[1]` work?

**Answer**:
- The difference tells us the "penalty" for choosing city A over city B
- **Negative difference**: Choosing A saves money (penalty is negative)
- **Positive difference**: Choosing A costs more (penalty is positive)
- By sorting in ascending order, we put people who save the most by going to A first
- We send the first N to A (maximize savings) and last N to B (minimize losses)

**Mathematical Formulation**:
- Total cost if we send person `i` to A: `costs[i][0]`
- Total cost if we send person `i` to B: `costs[i][1]`
- Difference: `costs[i][0] - costs[i][1]`
- If difference < 0: A is cheaper
- If difference > 0: B is cheaper
- Sorting by difference groups people by which city is cheaper for them

## Tags

`Array`, `Greedy`, `Sorting`, `Medium`

## Key Takeaways

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

## References

- [LC 1029: Two City Scheduling on LeetCode](https://www.leetcode.com/problems/two-city-scheduling/)
- [LeetCode Discuss — LC 1029: Two City Scheduling](https://www.leetcode.com/problems/two-city-scheduling/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/two-city-scheduling/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
