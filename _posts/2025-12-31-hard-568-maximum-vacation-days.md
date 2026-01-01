---
layout: post
title: "568. Maximum Vacation Days"
date: 2025-12-31 20:30:00 -0700
categories: [leetcode, hard, dynamic-programming, graph, optimization]
permalink: /2025/12/31/hard-568-maximum-vacation-days/
---

# 568. Maximum Vacation Days

## Problem Statement

LeetCode wants to give one of its best employees the option to travel among `n` cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

**Rules and restrictions:**

1. You can only travel among `n` cities, represented by indexes from `0` to `n - 1`. Initially, you are in city `0` on **Monday**.
2. The cities are connected by flights. The flights are represented as an `n x n` matrix (not necessarily symmetrical), called `flights`, representing the airline status from the city `i` to the city `j`. If there is no flight from the city `i` to the city `j`, `flights[i][j] = 0`; Otherwise, `flights[i][j] = 1`. Also, `flights[i][i] = 0` for all `i`.
3. You totally have `k` weeks (each week has **7 days**) to travel. You can only take flights at most once per day and can only take flights on each **Monday** morning. Since flight time is so short, we don't consider the impact of flight time.
4. For each city, you can only have restricted vacation days in different weeks, given an `n x k` matrix called `days` representing this relationship. For the value of `days[i][j]`, it represents the maximum number of vacation days you could take in the city `i` in the week `j`.

You're given the `flights` matrix and `days` matrix, and you need to output the maximum number of vacation days you could take during `k` weeks.

## Examples

**Example 1:**
```
Input: flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]
Output: 12
Explanation:
One of the best strategies is:
1st week: fly from city 0 to city 1 on Monday, and play 6 days and work 1 day.
2nd week: fly from city 1 to city 2 on Monday, and play 3 days and work 4 days.
3rd week: stay at city 2, and play 3 days and work 4 days.
Ans = 6 + 3 + 3 = 12.
```

**Example 2:**
```
Input: flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]
Output: 3
Explanation:
Since there are no flights that enable you to move to another city, you have to stay at city 0 for the whole 3 weeks.
For each week, you only have one day off, so the maximum number of vacation days is 3.
```

## Constraints

- `n == flights.length`
- `n == flights[i].length`
- `n == days.length`
- `k == days[i].length`
- `1 <= n, k <= 100`
- `flights[i][j]` is `0` or `1`.
- `0 <= days[i][j] <= 7`

## Solution Approach

This problem requires maximizing vacation days over `k` weeks by choosing which city to be in each week, subject to flight constraints. We can solve this using **dynamic programming** with a bottom-up approach.

### Key Insights:

1. **DP State**: `dp[city]` = maximum vacation days achievable ending at `city` for current week
2. **Bottom-Up**: Process weeks from end to beginning (or beginning to end)
3. **State Transition**: For each city, consider staying or flying from other cities
4. **Optimization**: Choose maximum vacation days among all options

### Algorithm:

1. **Initialize**: Start with last week, compute maximum for each city
2. **Backward DP**: For each week, compute optimal choice for each city
3. **State Update**: Consider staying in same city or flying from other cities
4. **Result**: Return maximum vacation days starting from city 0

## Solution

### **Solution: Dynamic Programming (Bottom-Up)**

```cpp
class Solution {
public:
    int maxVacationDays(vector<vector<int>>& flights, vector<vector<int>>& days) {
        if(days.size() == 0 || flights.size() == 0) return 0;
        const int N = flights.size(), M = days[0].size(); 
        vector<int> dp(N);
        for(int week = M - 1; week >= 0; week--) {
            vector<int> temp(N);
            for(int cur_city = 0; cur_city < N; cur_city++) {
                temp[cur_city] = days[cur_city][week] + dp[cur_city];
                for(int dest_city = 0; dest_city < N; dest_city++) {
                    if(flights[cur_city][dest_city] == 1) {
                        temp[cur_city] = max(days[dest_city][week] + dp[dest_city], temp[cur_city]);
                    }
                }
            }
            dp = move(temp);
        }
        return dp[0];
    }
};
```

### **Algorithm Explanation:**

1. **Edge Case (Line 4)**: Return 0 if inputs are empty

2. **Initialization (Lines 5-6)**:
   - `N`: Number of cities
   - `M`: Number of weeks
   - `dp[i]`: Maximum vacation days from week `week+1` to end, ending at city `i`

3. **Bottom-Up DP (Lines 7-17)**:
   - **Process weeks backwards**: From last week to first week
   - **For each city** (Lines 9-16):
     - **Stay option**: `temp[cur_city] = days[cur_city][week] + dp[cur_city]`
       - Stay in current city, add current week's days, plus future optimal
     - **Fly option**: Check all cities with flights from current city
       - If flight exists: `max(days[dest_city][week] + dp[dest_city], temp[cur_city])`
       - Fly to destination, add destination's days, plus future optimal
   - **Update DP**: `dp = move(temp)` for next iteration

4. **Result (Line 18)**: Return `dp[0]` - maximum starting from city 0

### **Example Walkthrough:**

**For `flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]`:**

```
N = 3 cities, M = 3 weeks

Step 1: Week 2 (last week)
dp = [0, 0, 0] (no future weeks)

For city 0:
  Stay: days[0][2] + dp[0] = 1 + 0 = 1
  Fly to 1: days[1][2] + dp[1] = 3 + 0 = 3
  Fly to 2: days[2][2] + dp[2] = 3 + 0 = 3
  temp[0] = max(1, 3, 3) = 3

For city 1:
  Stay: days[1][2] + dp[1] = 3 + 0 = 3
  Fly to 0: days[0][2] + dp[0] = 1 + 0 = 1
  Fly to 2: days[2][2] + dp[2] = 3 + 0 = 3
  temp[1] = max(3, 1, 3) = 3

For city 2:
  Stay: days[2][2] + dp[2] = 3 + 0 = 3
  Fly to 0: days[0][2] + dp[0] = 1 + 0 = 1
  Fly to 1: days[1][2] + dp[1] = 3 + 0 = 3
  temp[2] = max(3, 1, 3) = 3

dp = [3, 3, 3]

Step 2: Week 1
For city 0:
  Stay: days[0][1] + dp[0] = 3 + 3 = 6
  Fly to 1: days[1][1] + dp[1] = 0 + 3 = 3
  Fly to 2: days[2][1] + dp[2] = 3 + 3 = 6
  temp[0] = max(6, 3, 6) = 6

For city 1:
  Stay: days[1][1] + dp[1] = 0 + 3 = 3
  Fly to 0: days[0][1] + dp[0] = 3 + 3 = 6
  Fly to 2: days[2][1] + dp[2] = 3 + 3 = 6
  temp[1] = max(3, 6, 6) = 6

For city 2:
  Stay: days[2][1] + dp[2] = 3 + 3 = 6
  Fly to 0: days[0][1] + dp[0] = 3 + 3 = 6
  Fly to 1: days[1][1] + dp[1] = 0 + 3 = 3
  temp[2] = max(6, 6, 3) = 6

dp = [6, 6, 6]

Step 3: Week 0 (first week)
For city 0 (starting city):
  Stay: days[0][0] + dp[0] = 1 + 6 = 7
  Fly to 1: days[1][0] + dp[1] = 6 + 6 = 12
  Fly to 2: days[2][0] + dp[2] = 3 + 6 = 9
  temp[0] = max(7, 12, 9) = 12

dp = [12, ...]

Result: dp[0] = 12

Optimal path:
Week 0: City 0 → City 1 (fly), days = 6
Week 1: City 1 → City 2 (fly), days = 3
Week 2: City 2 (stay), days = 3
Total: 6 + 3 + 3 = 12
```

## Algorithm Breakdown

### **Key Insight: Bottom-Up DP**

The algorithm processes weeks **backwards** (from end to beginning):
- **Base case**: Last week - no future weeks, only current week's days
- **Recursive case**: For each week, consider all options and choose maximum
- **State**: `dp[city]` = maximum vacation days from current week to end, ending at `city`

### **State Transition**

For each city in each week:
1. **Stay option**: Stay in current city
   - `days[cur_city][week] + dp[cur_city]`
2. **Fly option**: Fly to any city with available flight
   - `days[dest_city][week] + dp[dest_city]`
3. **Choose maximum**: `max(stay, all_fly_options)`

### **Why Backward Processing Works**

Processing backwards ensures:
- When computing week `i`, we already know optimal for weeks `i+1` to `M-1`
- `dp[city]` represents future optimal value
- Current week's decision uses future optimal values

## Complexity Analysis

### **Time Complexity:** O(M × N²)
- **Outer loop**: O(M) - iterate through each week
- **City loop**: O(N) - for each city
- **Flight check**: O(N) - check all possible destinations
- **Total**: O(M × N²) where M = weeks, N = cities

### **Space Complexity:** O(N)
- **DP array**: O(N) - stores maximum for each city
- **Temporary array**: O(N) - used for current week
- **Total**: O(N) - space-optimized (only current state needed)

## Key Points

1. **Bottom-Up DP**: Process weeks from end to beginning
2. **State Optimization**: Only store current week's state (O(N) space)
3. **Two Options**: Stay in same city or fly to another city
4. **Optimal Substructure**: Optimal solution uses optimal subproblems
5. **Starting City**: Result is `dp[0]` since we start in city 0

## Alternative Approaches

### **Approach 1: Bottom-Up DP (Current Solution)**
- **Time**: O(M × N²)
- **Space**: O(N)
- **Best for**: Space-efficient solution

### **Approach 2: Top-Down DP with Memoization**
- **Time**: O(M × N²)
- **Space**: O(M × N) for memoization
- **Recursive**: Start from week 0, recurse to end
- **More intuitive**: But uses more space

### **Approach 3: 2D DP Table**
- **Time**: O(M × N²)
- **Space**: O(M × N)
- **Store all states**: `dp[week][city]` for all weeks
- **Easier to understand**: But uses more space

## Detailed Example Walkthrough

### **Example: `flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]`**

```
N = 3 cities, M = 3 weeks
No flights available (all 0s)

Step 1: Week 2
For each city, can only stay:
  dp[0] = days[0][2] = 1
  dp[1] = days[1][2] = 7
  dp[2] = days[2][2] = 7

Step 2: Week 1
For city 0: Stay only → dp[0] = 1 + 1 = 2
For city 1: Stay only → dp[1] = 7 + 7 = 14
For city 2: Stay only → dp[2] = 7 + 7 = 14

Step 3: Week 0
For city 0 (starting): Stay only → dp[0] = 1 + 2 = 3

Result: 3
```

## Edge Cases

1. **No flights**: Can only stay in starting city
2. **Single city**: Only one city, no travel options
3. **Single week**: Only one week to maximize
4. **All zeros**: No vacation days available
5. **All maximum**: Maximum vacation days in all cities

## Optimization Notes

The solution uses **space optimization**:
- Instead of `dp[week][city]` (O(M × N) space)
- Uses `dp[city]` and `temp[city]` (O(N) space)
- Processes one week at a time, reusing space

## Related Problems

- [568. Maximum Vacation Days](https://leetcode.com/problems/maximum-vacation-days/) - Current problem
- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Similar DP with flights
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) - DP on grid
- [120. Triangle](https://leetcode.com/problems/triangle/) - DP optimization

## Tags

`Dynamic Programming`, `Graph`, `Optimization`, `Hard`

