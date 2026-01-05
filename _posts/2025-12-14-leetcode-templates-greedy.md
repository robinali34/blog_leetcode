---
layout: post
title: "LeetCode Templates: Greedy"
date: 2025-12-14 00:00:00 -0800
categories: leetcode templates greedy
permalink: /posts/2025-12-14-leetcode-templates-greedy/
tags: [leetcode, templates, greedy, algorithms]
---

{% raw %}
## Contents

- [Greedy Algorithm Overview](#greedy-algorithm-overview)
- [Interval Scheduling](#interval-scheduling)
- [Activity Selection](#activity-selection)
- [Fractional Knapsack](#fractional-knapsack)
- [Greedy on Arrays](#greedy-on-arrays)
- [Greedy on Strings](#greedy-on-strings)
- [Greedy with Sorting](#greedy-with-sorting)

## Greedy Algorithm Overview

Greedy algorithms make locally optimal choices at each step, hoping to find a global optimum. They work well when:
- The problem has optimal substructure
- The greedy choice property holds (locally optimal choice leads to global optimum)
- No need to reconsider previous choices

### Key Principles

1. **Greedy Choice Property**: A global optimum can be reached by making locally optimal choices
2. **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
3. **No Backtracking**: Once a choice is made, it's never reconsidered

## Interval Scheduling

Greedy approach: Sort by end time, always pick the interval that ends earliest.

```cpp
// Non-overlapping Intervals
int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    if(intervals.empty()) return 0;
    
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];  // Sort by end time
    });
    
    int count = 1;
    int end = intervals[0][1];
    
    for(int i = 1; i < intervals.size(); i++) {
        if(intervals[i][0] >= end) {
            count++;
            end = intervals[i][1];
        }
    }
    
    return intervals.size() - count;
}
```

## Activity Selection

Similar to interval scheduling, select maximum number of non-overlapping activities.

```cpp
// Maximum number of non-overlapping intervals
int maxNonOverlappingIntervals(vector<vector<int>>& intervals) {
    if(intervals.empty()) return 0;
    
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    int count = 1;
    int end = intervals[0][1];
    
    for(int i = 1; i < intervals.size(); i++) {
        if(intervals[i][0] >= end) {
            count++;
            end = intervals[i][1];
        }
    }
    
    return count;
}
```

## Fractional Knapsack

Greedy approach: Sort items by value/weight ratio, take items with highest ratio first.

```cpp
// Fractional Knapsack (not a LeetCode problem, but classic greedy)
struct Item {
    int value, weight;
    double ratio;
};

double fractionalKnapsack(int W, vector<Item>& items) {
    sort(items.begin(), items.end(), [](const Item& a, const Item& b) {
        return a.ratio > b.ratio;
    });
    
    double totalValue = 0.0;
    int remainingWeight = W;
    
    for(auto& item : items) {
        if(remainingWeight >= item.weight) {
            totalValue += item.value;
            remainingWeight -= item.weight;
        } else {
            totalValue += item.value * ((double)remainingWeight / item.weight);
            break;
        }
    }
    
    return totalValue;
}
```

## Greedy on Arrays

Greedy choices on array elements, often with two pointers or sliding window.

```cpp
// Maximum Subarray (Kadane's Algorithm)
int maxSubArray(vector<int>& nums) {
    int maxSum = nums[0];
    int currentSum = nums[0];
    
    for(int i = 1; i < nums.size(); i++) {
        currentSum = max(nums[i], currentSum + nums[i]);
        maxSum = max(maxSum, currentSum);
    }
    
    return maxSum;
}

// Best Time to Buy and Sell Stock II
int maxProfit(vector<int>& prices) {
    int profit = 0;
    for(int i = 1; i < prices.size(); i++) {
        if(prices[i] > prices[i-1]) {
            profit += prices[i] - prices[i-1];
        }
    }
    return profit;
}

// Candy - Greedy with sequence tracking
int candy(vector<int>& ratings) {
    const int N = ratings.size();
    int rtn = 1;
    int inc = 1, dec = 0, pre = 1;
    for(int i = 1; i < N; i++) {
        if(ratings[i] >= ratings[i - 1]) {
            dec = 0;
            pre = ratings[i] == ratings[i - 1] ? 1: pre + 1;
            rtn += pre;
            inc = pre;
        } else {
            dec++;
            if(dec == inc) {
                dec++;
            }
            rtn += dec;
            pre = 1;
        }
    }
    return rtn;
}

// Wiggle Subsequence - Greedy with difference tracking
int wiggleMaxLength(vector<int>& nums) {
    const int N = nums.size();
    if(N < 2) return N;
    int prevDiff = nums[1] - nums[0];
    int rtn = prevDiff != 0? 2 : 1;
    for(int i = 2; i < N; i++) {
        int diff = nums[i] - nums[i - 1];
        if((diff > 0 && prevDiff <= 0) ||
            diff < 0 && prevDiff >= 0) {
                rtn++;
                prevDiff = diff;
            }
    }
    return rtn;
}
```

## Greedy on Strings

Greedy choices when processing strings, often with character frequency or ordering.

```cpp
// Is Subsequence
bool isSubsequence(string s, string t) {
    int i = 0, j = 0;
    while(i < s.length() && j < t.length()) {
        if(s[i] == t[j]) {
            i++;
        }
        j++;
    }
    return i == s.length();
}

// Minimum Swaps to Make Strings Equal - Mismatch pairing
int minimumSwap(string s1, string s2) {
    int xy = 0, yx = 0;
    for(int i = 0; i < (int) s1.length(); i++) {
        if(s1[i] == 'x' && s2[i] == 'y') {
            xy++;
        } else if(s1[i] == 'y' && s2[i] == 'x') {
            yx++;
        }
    }
    if((xy + yx) % 2 == 1) {
        return -1;  // Impossible if odd total mismatches
    }
    return xy / 2 + yx / 2 + xy % 2 + yx % 2;
}

// Construct K Palindrome Strings - Frequency-based greedy
bool canConstruct(string s, int k) {
    int right = s.length();
    int occ[26] = {0};
    for(char ch: s) {
        occ[ch - 'a']++;
    }
    int left = 0;
    for(int i = 0; i < 26; i++) {
        if(occ[i] % 2 == 1) {
            left++;
        }
    }
    left = max(left, 1);
    return left <= k && k <= right;
}
```

## Greedy with Sorting

Many greedy problems require sorting first to make optimal choices.

```cpp
// Assign Cookies
int findContentChildren(vector<int>& g, vector<int>& s) {
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    
    int i = 0, j = 0;
    int count = 0;
    
    while(i < g.size() && j < s.size()) {
        if(s[j] >= g[i]) {
            count++;
            i++;
        }
        j++;
    }
    
    return count;
}

// Array Partition - Maximize sum of minimums
int arrayPairSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int sum = 0;
    for(int i = 0; i < (int)nums.size(); i += 2) {
        sum += nums[i];
    }
    return sum;
}

// Maximum Units on a Truck - Fractional knapsack style
int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
    sort(boxTypes.begin(), boxTypes.end(), [](auto& u, auto& v){
        return u[1] > v[1];  // Sort by units per box (descending)
    });
    int remainSize = truckSize;
    int maximumUnits = 0;
    for(auto& boxType: boxTypes) {
        if(remainSize == 0) break;
        int cnt = min(remainSize, boxType[0]);
        maximumUnits += cnt * boxType[1];
        remainSize -= cnt;
    }
    return maximumUnits;
}

// Minimum Cost to Move Chips - Parity-based greedy
int minCostToMoveChips(vector<int>& position) {
    int even = 0, odd = 0;
    for(int pos : position) {
        if(pos % 2 == 0) {
            odd++;  // Count even positions
        } else {
            even++;  // Count odd positions
        }
    }
    return min(odd, even);  // Move minority parity to majority
}

// Two City Scheduling - Sort by cost difference
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

// Find Valid Matrix Given Row and Column Sums - Greedy two pointers
vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
    const int N = rowSum.size(), M = colSum.size();
    vector<vector<int>> matrix(N, vector<int>(M, 0));
    int i = 0, j = 0;
    while(i < N && j < M) {
        int v = min(rowSum[i], colSum[j]);
        matrix[i][j] = v;
        rowSum[i] -= v;
        colSum[j] -= v;
        if(rowSum[i] == 0) i++;
        if(colSum[j] == 0) j++;
    }
    return matrix;
}

// Queue Reconstruction by Height
vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
    sort(people.begin(), people.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] == b[0] ? a[1] < b[1] : a[0] > b[0];
    });
    
    vector<vector<int>> result;
    for(auto& person : people) {
        result.insert(result.begin() + person[1], person);
    }
    
    return result;
}
```

## Easy Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 455 | Assign Cookies | [Link](https://leetcode.com/problems/assign-cookies/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/easy-455-assign-cookies/) |
| 860 | Lemonade Change | [Link](https://leetcode.com/problems/lemonade-change/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/easy-860-lemonade-change/) |
| 392 | Is Subsequence | [Link](https://leetcode.com/problems/is-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/easy-392-is-subsequence/) |
| 406 | Queue Reconstruction by Height | [Link](https://leetcode.com/problems/queue-reconstruction-by-height/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-406-queue-reconstruction-by-height/) |
| 53 | Maximum Subarray | [Link](https://leetcode.com/problems/maximum-subarray/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-53-maximum-subarray/) |
| 435 | Non-overlapping Intervals | [Link](https://leetcode.com/problems/non-overlapping-intervals/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/medium-435-non-overlapping-intervals/) |
| 452 | Minimum Number of Arrows to Burst Balloons | [Link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/medium-452-minimum-number-of-arrows-to-burst-balloons/) |
| 561 | Array Partition | [Link](https://leetcode.com/problems/array-partition/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/easy-561-array-partition/) |
| 1029 | Two City Scheduling | [Link](https://leetcode.com/problems/two-city-scheduling/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-1029-two-city-scheduling/) |
| 122 | Best Time to Buy and Sell Stock II | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/medium-122-best-time-to-buy-and-sell-stock-ii/) |
| 1710 | Maximum Units on a Truck | [Link](https://leetcode.com/problems/maximum-units-on-a-truck/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/easy-1710-maximum-units-on-a-truck/) |
| 1217 | Minimum Cost to Move Chips to The Same Position | [Link](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/easy-1217-minimum-cost-to-move-chips-to-the-same-position/) |

## Medium Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 763 | Partition Labels | [Link](https://leetcode.com/problems/partition-labels/) | - |
| 621 | Task Scheduler | [Link](https://leetcode.com/problems/task-scheduler/) | - |
| 435 | Non-overlapping Intervals | [Link](https://leetcode.com/problems/non-overlapping-intervals/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/medium-435-non-overlapping-intervals/) |
| 55 | Jump Game | [Link](https://leetcode.com/problems/jump-game/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/03/medium-55-jump-game/) |
| 1094 | Car Pooling | [Link](https://leetcode.com/problems/car-pooling/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-22-medium-1094-car-pooling/) |
| 45 | Jump Game II | [Link](https://leetcode.com/problems/jump-game-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-45-jump-game-ii/) |
| 134 | Gas Station | [Link](https://leetcode.com/problems/gas-station/) | - |
| 1024 | Video Stitching | [Link](https://leetcode.com/problems/video-stitching/) | - |
| 1247 | Minimum Swaps to Make Strings Equal | [Link](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-1247-minimum-swaps-to-make-strings-equal/) |
| 1400 | Construct K Palindrome Strings | [Link](https://leetcode.com/problems/construct-k-palindrome-strings/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-1400-construct-k-palindrome-strings/) |
| 1605 | Find Valid Matrix Given Row and Column Sums | [Link](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-1605-find-valid-matrix-given-row-and-column-sums/) |
| 376 | Wiggle Subsequence | [Link](https://leetcode.com/problems/wiggle-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-376-wiggle-subsequence/) |

## Hard Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 135 | Candy | [Link](https://leetcode.com/problems/candy/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/04/hard-135-candy/) |
| 871 | Minimum Number of Refueling Stops | [Link](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | - |
| 818 | Race Car | [Link](https://leetcode.com/problems/race-car/) | - |
| 410 | Split Array Largest Sum | [Link](https://leetcode.com/problems/split-array-largest-sum/) | - |
| 420 | Strong Password Checker | [Link](https://leetcode.com/problems/strong-password-checker/) | - |
| 68 | Text Justification | [Link](https://leetcode.com/problems/text-justification/) | - |
| 76 | Minimum Window Substring | [Link](https://leetcode.com/problems/minimum-window-substring/) | - |
| 1799 | Maximize Score After N Operations | [Link](https://leetcode.com/problems/maximize-score-after-n-operations/) | - |

## Common Greedy Patterns

### 1. Interval Problems
- Sort by end time
- Always pick the interval that ends earliest
- Examples: Non-overlapping Intervals, Minimum Arrows to Burst Balloons

### 2. Two Pointers
- Use two pointers to make greedy choices
- Examples: Is Subsequence, Assign Cookies

### 3. Sorting + Greedy
- Sort first, then apply greedy strategy
- Examples: Queue Reconstruction by Height, Two City Scheduling

### 4. Local Optimization
- Make best local choice at each step
- Examples: Best Time to Buy and Sell Stock II, Maximum Subarray

### 5. Jump Problems
- Greedy choice: jump as far as possible
- Examples: Jump Game, Jump Game II

### 6. Scheduling Problems
- Sort and schedule optimally
- Examples: Task Scheduler, Car Pooling

## Key Insights

1. **When to use Greedy**: 
   - Problem has optimal substructure
   - Greedy choice property holds
   - No need to reconsider previous choices

2. **Common Mistakes**:
   - Not sorting when needed
   - Wrong sorting criteria
   - Not considering edge cases
   - Assuming greedy always works (need to prove correctness)

3. **Proving Greedy Correctness**:
   - Show greedy choice property
   - Show optimal substructure
   - Use exchange argument or contradiction

## Related Topics

- Dynamic Programming (when greedy doesn't work)
- Sorting Algorithms
- Interval Problems
- Two Pointers
- Sliding Window

## References

- [Mastering Greedy Algorithms with LeetCode](https://leetcode.com/discuss/post/5330283/mastering-greedy-algorithms-with-leetcod-d0dq/) - Comprehensive guide to greedy algorithms with LeetCode problems

{% endraw %}

