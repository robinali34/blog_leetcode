---
layout: post
title: "[Medium] Round Trip Ticket Cost Minimization"
date: 2025-11-24 00:00:00 -0800
categories: algorithm medium cpp array optimization problem-solving
permalink: /posts/2025-11-24-medium-round-trip-ticket-cost/
tags: [algorithm, medium, array, optimization, greedy, two-pointers]
---

# [Medium] Round Trip Ticket Cost Minimization

Given two lists representing round trip ticket prices, select the cheapest outbound and return tickets where the return follows the outbound. Implement a function to find the minimum total cost of the trip.

## Problem Statement

You are given two lists of ticket prices:
- `outbound`: List of outbound ticket prices
- `return_trip`: List of return ticket prices

Both lists have the same length `n`, and you must select:
- One outbound ticket at index `i`
- One return ticket at index `j` (can be any index, no ordering constraint)

**Note:** Based on the example, it appears there's no strict ordering constraint between outbound and return ticket indices. The "return follows outbound" likely refers to the logical sequence of the trip rather than array indices.

Find the minimum total cost of such a round trip.

## Requirements

- Write a function `int minimizeRoundTripCost(vector<int>& outbound, vector<int>& returnTrip)`
- Both lists are of length `n`, and the values range from 1 to 1000
- Ensure the selected outbound precedes the return in the trip (index-wise)
- Return the minimum total trip cost

## Examples

**Example 1:**
{% raw %}
```cpp
Input: 
  outbound = {9, 1, 5}
  returnTrip = {4, 5, 3}

Output: 5
Explanation: 
  - Select outbound[1] = 1 (index 1)
  - Select return_trip[0] = 4 (index 0)
  - Total: 1 + 4 = 5
  
  All possible pairings:
  - outbound[0] = 9 with return_trip[0] = 4 → 13
  - outbound[0] = 9 with return_trip[1] = 5 → 14
  - outbound[0] = 9 with return_trip[2] = 3 → 12
  - outbound[1] = 1 with return_trip[0] = 4 → 5 ✓ (minimum)
  - outbound[1] = 1 with return_trip[1] = 5 → 6
  - outbound[1] = 1 with return_trip[2] = 3 → 4
  - outbound[2] = 5 with return_trip[0] = 4 → 9
  - outbound[2] = 5 with return_trip[1] = 5 → 10
  - outbound[2] = 5 with return_trip[2] = 3 → 8
  
  Minimum: min(13, 14, 12, 5, 6, 4, 9, 10, 8) = 4
  
  Wait, the minimum is actually 4 (outbound[1] = 1 + return_trip[2] = 3), but the example says 5.
  This suggests the example might be showing one valid solution (1 + 4 = 5) rather than the optimal.
  Or there might be additional constraints not stated.
  
  For the solution, we'll find the true minimum cost.
```
{% endraw %}

**Example 2:**
{% raw %}
```cpp
Input:
  outbound = {3, 2, 1}
  returnTrip = {1, 2, 3}

Output: 3
Explanation:
  - outbound[0] = 3: can pair with return_trip[1] = 2 → 5, return_trip[2] = 3 → 6
  - outbound[1] = 2: can pair with return_trip[2] = 3 → 5
  - Minimum: min(5, 6, 5) = 5... wait, let me recalculate
  
Actually with j > i:
  - outbound[0] = 3: return_trip[1] = 2 → 5, return_trip[2] = 3 → 6
  - outbound[1] = 2: return_trip[2] = 3 → 5
  - Minimum: 5

But if j >= i:
  - outbound[0] = 3: return_trip[0] = 1 → 4, return_trip[1] = 2 → 5, return_trip[2] = 3 → 6
  - outbound[1] = 2: return_trip[1] = 2 → 4, return_trip[2] = 3 → 5
  - outbound[2] = 2: return_trip[2] = 3 → 4
  - Minimum: 4
```
{% endraw %}

## Constraints

- `1 <= n <= 10^5`
- `1 <= outbound[i], return_trip[i] <= 1000`
- Both lists have the same length `n`

## Solution: Find Minimum Return Price

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Since we can pair any outbound ticket with any return ticket, we simply need to find:
1. The minimum return ticket price overall
2. For each outbound ticket, calculate the sum with the minimum return price
3. Return the minimum of all such sums

Alternatively, we can find the minimum outbound price and minimum return price separately, but we need to be careful - the optimal solution might pair a specific outbound with a specific return that isn't the global minimum.

### Solution 1: Brute Force - Check All Pairs (O(n²))

```cpp
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int minimizeRoundTripCost(vector<int>& outbound, vector<int>& returnTrip) {
    int n = outbound.size();
    int minCost = INT_MAX;
    
    // Try all possible pairs
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int cost = outbound[i] + returnTrip[j];
            minCost = min(minCost, cost);
        }
    }
    
    return minCost;
}
```

### Solution 2: Optimized - Find Minimums Separately (O(n))

```cpp
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int minimizeRoundTripCost(vector<int>& outbound, vector<int>& returnTrip) {
    int n = outbound.size();
    
    // Find minimum return price
    int minReturn = *min_element(returnTrip.begin(), returnTrip.end());
    
    // For each outbound, pair with minimum return
    int minCost = INT_MAX;
    for (int i = 0; i < n; ++i) {
        int cost = outbound[i] + minReturn;
        minCost = min(minCost, cost);
    }
    
    return minCost;
}
```

**Why this works:**
- Since we can pair any outbound with any return, the optimal strategy is:
  - Find the minimum return price overall
  - Pair each outbound with this minimum return price
  - Choose the outbound that gives the minimum sum

**Time Complexity:** O(n) - one pass to find min return, one pass through outbound  
**Space Complexity:** O(1)

## How the Algorithm Works

### Key Insight: Precompute Minimum Return Prices

**Problem:** For each outbound ticket at index `i`, we need the minimum return ticket price from indices `i+1` to `n-1`.

**Solution:** Precompute `minReturn[i]` = minimum return price from index `i` to the end.

**Why this works:**
- For outbound[i], we can pair with returnTrip[j] where `j > i`
- The minimum return price available is `minReturn[i+1]`
- Total cost = `outbound[i] + minReturn[i+1]`
- Find minimum over all valid `i`

### Step-by-Step Example: `outbound = {9, 1, 5}, returnTrip = {4, 5, 3}`

```
Step 1: Find minimum return price
  minReturn = min(returnTrip) = min(4, 5, 3) = 3

Step 2: Calculate cost for each outbound paired with minimum return
  i = 0: outbound[0] + minReturn = 9 + 3 = 12
  i = 1: outbound[1] + minReturn = 1 + 3 = 4
  i = 2: outbound[2] + minReturn = 5 + 3 = 8
  
  Minimum: min(12, 4, 8) = 4

Note: The example output is 5 (outbound[1] = 1 + returnTrip[0] = 4), 
but the optimal solution is 4 (outbound[1] = 1 + returnTrip[2] = 3).
The example might be showing a valid but not optimal solution.
```

**Visual Representation:**
{% raw %}
```
outbound:  {9,  1,  5}
            │   │   │
            │   └───┼───> Can pair with return[2] = 3 → cost = 4
            └───────┼───> Can pair with return[1] = 5 or return[2] = 3
                    │    Best: return[2] = 3 → cost = 12
                    └───> No return after index 2

returnTrip: {4,  5,  3}
              │   │   │
              └───┴───┘
              minReturn = {3, 3, 3}
```
{% endraw %}

## Key Insights

1. **Precompute minimums**: Build array of minimum return prices from right to left
2. **Pair optimally**: For each outbound, pair with minimum available return
3. **Boundary handling**: Last outbound ticket cannot pair with any return
4. **Greedy approach**: Always choose minimum return price for each outbound

## Algorithm Breakdown

### Step 1: Precompute Minimum Return Prices

```cpp
vector<int> minReturn(n);
minReturn[n - 1] = returnTrip[n - 1];

for (int i = n - 2; i >= 0; --i) {
    minReturn[i] = min(returnTrip[i], minReturn[i + 1]);
}
```

**Why:**
- Start from the end: `minReturn[n-1] = returnTrip[n-1]`
- For each index `i`, `minReturn[i]` is the minimum return price from `i` to the end
- Build from right to left to reuse previous computations

### Step 2: Find Minimum Cost

```cpp
int minCost = INT_MAX;
for (int i = 0; i < n - 1; ++i) {
    int cost = outbound[i] + minReturn[i + 1];
    minCost = min(minCost, cost);
}
```

**Why:**
- For outbound[i], minimum return price available is `minReturn[i]` (includes returnTrip[i] and all after)
- Calculate cost for each valid pairing
- Track minimum cost seen so far

## Alternative Solutions

### Solution 2: O(1) Space Optimization

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Instead of storing the entire `minReturn` array, we can iterate backwards and track the minimum return price seen so far.

```cpp
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int minimizeRoundTripCost(vector<int>& outbound, vector<int>& returnTrip) {
    int n = outbound.size();
    if (n < 2) {
        return INT_MAX;
    }
    
    int minCost = INT_MAX;
    int minReturnPrice = returnTrip[n - 1];  // Minimum return price from current position onwards
    
    // Iterate backwards through outbound tickets
    for (int i = n - 1; i >= 0; --i) {
        // Update minimum return price available (includes returnTrip[i] and all after)
        if (i < n - 1) {
            minReturnPrice = min(minReturnPrice, returnTrip[i + 1]);
        }
        minReturnPrice = min(minReturnPrice, returnTrip[i]);
        
        // Calculate cost for current outbound ticket
        int cost = outbound[i] + minReturnPrice;
        minCost = min(minCost, cost);
    }
    
    return minCost;
}
```

**Pros:**
- O(1) extra space
- Same time complexity
- More memory efficient

**Cons:**
- Slightly less intuitive
- Iterates backwards

### Solution 3: Brute Force (For Comparison)

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

```cpp
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

int minimizeRoundTripCost(vector<int>& outbound, vector<int>& returnTrip) {
    int n = outbound.size();
    int minCost = INT_MAX;
    
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int cost = outbound[i] + returnTrip[j];
            minCost = min(minCost, cost);
        }
    }
    
    return minCost;
}
```

**Pros:**
- Simple and straightforward
- Easy to understand

**Cons:**
- O(n²) time complexity
- Inefficient for large inputs

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Precompute Array** | O(n) | O(n) | Clear logic, easy to understand | Extra space |
| **O(1) Space** | O(n) | O(1) | Memory efficient | Backwards iteration |
| **Brute Force** | O(n²) | O(1) | Simple | Too slow |

## Edge Cases

1. **Single ticket**: `n = 1` → No valid pairing, return infinity or handle appropriately
2. **Two tickets**: `n = 2` → Only one possible pairing
3. **All same prices**: Algorithm still works correctly
4. **Decreasing return prices**: Optimal to choose later return tickets
5. **Increasing return prices**: Optimal to choose earlier return tickets

## Implementation Details

### Why Iterate Backwards?

**For O(1) space solution:**
- We need minimum return price from `i+1` to `n-1`
- By iterating backwards, we can maintain `min_return_price` as we go
- At each step, we've seen all return prices from current position to the end

### Why Precompute Array?

**For O(n) space solution:**
- More intuitive: build array of minimums first
- Then use it to calculate costs
- Easier to understand and debug

### Handling Edge Cases

```cpp
if (n < 2) {
    return INT_MAX;  // or throw exception, or return -1
}
```

**Why:** Need at least 2 tickets (one outbound, one return) for a valid round trip.

## Common Mistakes

1. **Wrong index constraint**: Using `j >= i` instead of `j > i` (or vice versa)
2. **Missing boundary check**: Not handling case when `n < 2`
3. **Wrong minimum calculation**: Not correctly computing minimum return prices
4. **Index out of bounds**: Accessing `min_return[i+1]` when `i = n-1`
5. **Not iterating backwards**: Trying to compute minimums from left to right

## Optimization Tips

1. **Use O(1) space solution**: If memory is a concern
2. **Early termination**: Not applicable here (need to check all pairs)
3. **Precompute once**: Build min_return array once, use multiple times if needed

## Related Problems

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Similar pattern of finding min/max with ordering constraint
- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) - Multiple transactions
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) - At most two transactions
- Array problems with ordering constraints

## Real-World Applications

1. **Travel Planning**: Finding cheapest round trip flights
2. **Resource Scheduling**: Optimizing resource allocation with time constraints
3. **Cost Optimization**: Minimizing costs with ordering requirements
4. **Pairing Problems**: Finding optimal pairs with constraints

## Pattern Recognition

This problem demonstrates the **"Precompute Minimums/Maximums"** pattern:

```
1. Identify that we need min/max of a subarray
2. Precompute min/max array from one direction
3. Use precomputed values to solve the problem efficiently
```

Similar problems:
- Stock buying/selling problems
- Array range queries
- Optimization with constraints

## Step-by-Step Trace: `outbound = {3, 2, 1}, returnTrip = {1, 2, 3}`

{% raw %}
```
Step 1: Precompute minReturn
  minReturn[2] = returnTrip[2] = 3
  minReturn[1] = min(returnTrip[1], minReturn[2]) = min(2, 3) = 2
  minReturn[0] = min(returnTrip[0], minReturn[1]) = min(1, 2) = 1
  
  minReturn = {1, 2, 3}

Step 2: Calculate costs
  i = 0: outbound[0] + minReturn[1] = 3 + 2 = 5
  i = 1: outbound[1] + minReturn[2] = 2 + 3 = 5
  
  Minimum: min(5, 5) = 5
```
{% endraw %}

## Why This Solution Works

**Optimal Substructure:**
- For each outbound ticket, the optimal return ticket is the minimum available
- We can compute this independently for each outbound ticket
- The overall minimum is the minimum of all optimal pairings

**Greedy Choice:**
- For each outbound ticket, always choose the minimum return ticket available
- This local optimal choice leads to global optimum

**Time Efficiency:**
- Precomputation: O(n) time
- Finding minimum: O(n) time
- Total: O(n) time, much better than O(n²) brute force

## Test Cases

Here are several test cases to verify the solution:

### Test Case 1
{% raw %}
```cpp
outbound = {9, 1, 5}
returnTrip = {4, 5, 3}
Expected Output: 4
Explanation:
  - Minimum return price: min(4, 5, 3) = 3
  - Costs: 9+3=12, 1+3=4, 5+3=8
  - Minimum: 4 (outbound[1]=1 + returnTrip[2]=3)
```
{% endraw %}

### Test Case 2
{% raw %}
```cpp
outbound = {5, 7, 10}
returnTrip = {20, 9, 1}
Expected Output: 6
Explanation:
  - Minimum return price: min(20, 9, 1) = 1
  - Costs: 5+1=6, 7+1=8, 10+1=11
  - Minimum: 6 (outbound[0]=5 + returnTrip[2]=1)
```
{% endraw %}

### Test Case 3
{% raw %}
```cpp
outbound = {1, 100, 200}
returnTrip = {1000, 400, 2}
Expected Output: 3
Explanation:
  - Minimum return price: min(1000, 400, 2) = 2
  - Costs: 1+2=3, 100+2=102, 200+2=202
  - Minimum: 3 (outbound[0]=1 + returnTrip[2]=2)
```
{% endraw %}

### Test Case 4
{% raw %}
```cpp
outbound = {8, 4, 2}
returnTrip = {5, 3, 6}
Expected Output: 5
Explanation:
  - Minimum return price: min(5, 3, 6) = 3
  - Costs: 8+3=11, 4+3=7, 2+3=5
  - Minimum: 5 (outbound[2]=2 + returnTrip[1]=3)
```
{% endraw %}

### Test Case 5
{% raw %}
```cpp
outbound = {1, 2, 3}
returnTrip = {10, 9, 8}
Expected Output: 9
Explanation:
  - Minimum return price: min(10, 9, 8) = 8
  - Costs: 1+8=9, 2+8=10, 3+8=11
  - Minimum: 9 (outbound[0]=1 + returnTrip[2]=8)
```
{% endraw %}

### Test Case Verification Code

{% raw %}
```cpp
#include <vector>
#include <iostream>
#include <cassert>
using namespace std;

void testMinimizeRoundTripCost() {
    vector<pair<pair<vector<int>, vector<int>>, int>> testCases = {
        {{{9, 1, 5}, {4, 5, 3}}, 4},
        {{{5, 7, 10}, {20, 9, 1}}, 6},
        {{{1, 100, 200}, {1000, 400, 2}}, 3},
        {{{8, 4, 2}, {5, 3, 6}}, 5},
        {{{1, 2, 3}, {10, 9, 8}}, 9},
    };
    
    for (auto& [input, expected] : testCases) {
        auto& [outbound, returnTrip] = input;
        int result = minimizeRoundTripCost(outbound, returnTrip);
        assert(result == expected && "Test case failed");
        cout << "✓ Passed: ";
        cout << "outbound = {";
        for (int i = 0; i < (int)outbound.size(); ++i) {
            cout << outbound[i];
            if (i < (int)outbound.size() - 1) cout << ", ";
        }
        cout << "}, returnTrip = {";
        for (int i = 0; i < (int)returnTrip.size(); ++i) {
            cout << returnTrip[i];
            if (i < (int)returnTrip.size() - 1) cout << ", ";
        }
        cout << "} -> " << result << endl;
    }
    
    cout << "All test cases passed!" << endl;
}

// Run tests
int main() {
    testMinimizeRoundTripCost();
    return 0;
}
```
{% endraw %}

---

*This problem demonstrates how precomputing minimums can optimize array problems with ordering constraints, reducing time complexity from O(n²) to O(n).*

