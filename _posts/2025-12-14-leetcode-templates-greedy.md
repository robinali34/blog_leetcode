---
layout: post
title: "Algorithm Templates: Greedy"
date: 2025-12-14 00:00:00 -0800
categories: leetcode templates greedy
permalink: /posts/2025-12-14-leetcode-templates-greedy/
tags: [leetcode, templates, greedy, algorithms]
---
Greedy algorithms are among the most elegant tools in competitive programming — when they work, they're simpler and faster than dynamic programming. This guide covers the core greedy patterns you'll encounter on LeetCode, with ready-to-use C++ templates for interval scheduling, activity selection, fractional knapsack, and greedy strategies on arrays and strings. Each section includes the key intuition so you know *why* the greedy choice is correct, not just *how* to code it.

> **New to Greedy?** Greedy algorithms make the locally best choice at each step. Unlike DP, you never reconsider previous choices. The challenge is proving that local optimality leads to global optimality — if you can, greedy is simpler and faster than DP.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 320" width="520" height="320" font-family="Segoe UI, Arial, sans-serif" font-size="14">
  <defs>
    <marker id="ah" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#7a6e6a"/>
    </marker>
  </defs>
  <rect width="520" height="320" rx="12" fill="#f4f0ec"/>
  <text x="260" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#5b4f4a">Greedy vs DP — Which one?</text>
  <rect x="140" y="50" width="240" height="48" rx="8" fill="#c5b4a7" stroke="#7a6e6a" stroke-width="1.5"/>
  <text x="260" y="70" text-anchor="middle" fill="#3b302b" font-size="13">Can I prove local choice</text>
  <text x="260" y="87" text-anchor="middle" fill="#3b302b" font-size="13">is globally optimal?</text>
  <line x1="200" y1="98" x2="130" y2="145" stroke="#7a6e6a" stroke-width="1.5" marker-end="url(#ah)"/>
  <text x="145" y="125" text-anchor="middle" fill="#6b8e6b" font-weight="bold" font-size="13">Yes</text>
  <line x1="320" y1="98" x2="390" y2="145" stroke="#7a6e6a" stroke-width="1.5" marker-end="url(#ah)"/>
  <text x="375" y="125" text-anchor="middle" fill="#b07070" font-weight="bold" font-size="13">No</text>
  <rect x="50" y="148" width="160" height="44" rx="8" fill="#a8c3a8" stroke="#6b8e6b" stroke-width="1.5"/>
  <text x="130" y="175" text-anchor="middle" fill="#2d4a2d" font-weight="bold" font-size="14">Use Greedy</text>
  <rect x="310" y="148" width="160" height="44" rx="8" fill="#c3a8a8" stroke="#b07070" stroke-width="1.5"/>
  <text x="390" y="175" text-anchor="middle" fill="#4a2d2d" font-weight="bold" font-size="14">Try DP</text>
  <rect x="20" y="210" width="220" height="95" rx="8" fill="#d6ccc4" stroke="#b0a49a" stroke-width="1"/>
  <text x="130" y="232" text-anchor="middle" fill="#5b4f4a" font-size="12" font-weight="bold">Greedy is great when:</text>
  <text x="130" y="252" text-anchor="middle" fill="#5b4f4a" font-size="11">- Optimal substructure exists</text>
  <text x="130" y="269" text-anchor="middle" fill="#5b4f4a" font-size="11">- Greedy choice property holds</text>
  <text x="130" y="286" text-anchor="middle" fill="#5b4f4a" font-size="11">- O(n log n) or O(n) typical</text>
  <rect x="280" y="210" width="220" height="95" rx="8" fill="#d6ccc4" stroke="#b0a49a" stroke-width="1"/>
  <text x="390" y="232" text-anchor="middle" fill="#5b4f4a" font-size="12" font-weight="bold">DP is needed when:</text>
  <text x="390" y="252" text-anchor="middle" fill="#5b4f4a" font-size="11">- Overlapping subproblems</text>
  <text x="390" y="269" text-anchor="middle" fill="#5b4f4a" font-size="11">- Must explore all choices</text>
  <text x="390" y="286" text-anchor="middle" fill="#5b4f4a" font-size="11">- O(n²) or O(n·W) typical</text>
</svg>
</div>

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

1. **Greedy Choice Property**: A global optimum can be reached by making locally optimal choices. At every step, you pick what looks best *right now* and trust that this leads to the best overall answer.
2. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems. After making a greedy choice, the remaining problem is a smaller instance of the same type.
3. **No Backtracking**: Once a choice is made, it's never reconsidered. This is what makes greedy algorithms fast — but it also means you need to *prove* the greedy strategy is correct before relying on it.
4. **Exchange Argument**: The standard proof technique — assume an optimal solution differs from the greedy one, then show you can "exchange" a choice to match the greedy solution without making it worse.

## Interval Scheduling

**When to use:** The problem mentions "non-overlapping intervals", "minimum rooms", "merge intervals", or asks you to maximize/minimize a count of intervals that don't conflict.

Greedy approach: Sort by end time, always pick the interval that ends earliest.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 250" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <rect width="700" height="250" rx="12" fill="#FAF8F5"/>
  <text x="350" y="26" text-anchor="middle" font-size="15" font-weight="bold" fill="#3A3530">Merge Intervals</text>
  <text x="42" y="68" text-anchor="middle" font-size="11" fill="#7A7772">Input</text>
  <line x1="70" y1="98" x2="630" y2="98" stroke="#B8B5B0" stroke-width="1"/>
  <g font-size="9" fill="#9A9792" text-anchor="middle">
    <line x1="70" y1="95" x2="70" y2="101" stroke="#B8B5B0"/><text x="70" y="112">0</text>
    <line x1="98" y1="95" x2="98" y2="101" stroke="#B8B5B0"/><text x="98" y="112">1</text>
    <line x1="126" y1="97" x2="126" y2="99" stroke="#B8B5B0"/>
    <line x1="154" y1="95" x2="154" y2="101" stroke="#B8B5B0"/><text x="154" y="112">3</text>
    <line x1="238" y1="95" x2="238" y2="101" stroke="#B8B5B0"/><text x="238" y="112">6</text>
    <line x1="294" y1="95" x2="294" y2="101" stroke="#B8B5B0"/><text x="294" y="112">8</text>
    <line x1="350" y1="95" x2="350" y2="101" stroke="#B8B5B0"/><text x="350" y="112">10</text>
    <line x1="490" y1="95" x2="490" y2="101" stroke="#B8B5B0"/><text x="490" y="112">15</text>
    <line x1="574" y1="95" x2="574" y2="101" stroke="#B8B5B0"/><text x="574" y="112">18</text>
  </g>
  <rect x="98" y="46" width="56" height="20" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="126" y="60" text-anchor="middle" font-size="10" fill="#3A3530">[1,3]</text>
  <rect x="126" y="70" width="112" height="20" rx="4" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1" opacity="0.9"/>
  <text x="182" y="84" text-anchor="middle" font-size="10" fill="#3A3530">[2,6]</text>
  <rect x="294" y="58" width="56" height="20" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="322" y="72" text-anchor="middle" font-size="10" fill="#3A3530">[8,10]</text>
  <rect x="490" y="58" width="84" height="20" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="532" y="72" text-anchor="middle" font-size="10" fill="#3A3530">[15,18]</text>
  <text x="350" y="138" text-anchor="middle" font-size="12" fill="#8B8680">▼ merge overlapping</text>
  <text x="42" y="178" text-anchor="middle" font-size="11" fill="#7A7772">Result</text>
  <line x1="70" y1="198" x2="630" y2="198" stroke="#B8B5B0" stroke-width="1"/>
  <g font-size="9" fill="#9A9792" text-anchor="middle">
    <line x1="70" y1="195" x2="70" y2="201" stroke="#B8B5B0"/><text x="70" y="212">0</text>
    <line x1="98" y1="195" x2="98" y2="201" stroke="#B8B5B0"/><text x="98" y="212">1</text>
    <line x1="238" y1="195" x2="238" y2="201" stroke="#B8B5B0"/><text x="238" y="212">6</text>
    <line x1="294" y1="195" x2="294" y2="201" stroke="#B8B5B0"/><text x="294" y="212">8</text>
    <line x1="350" y1="195" x2="350" y2="201" stroke="#B8B5B0"/><text x="350" y="212">10</text>
    <line x1="490" y1="195" x2="490" y2="201" stroke="#B8B5B0"/><text x="490" y="212">15</text>
    <line x1="574" y1="195" x2="574" y2="201" stroke="#B8B5B0"/><text x="574" y="212">18</text>
  </g>
  <rect x="98" y="168" width="140" height="26" rx="5" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="168" y="185" text-anchor="middle" font-size="11" font-weight="bold" fill="#3A3530">[1,6]</text>
  <rect x="294" y="168" width="56" height="26" rx="5" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="322" y="185" text-anchor="middle" font-size="11" font-weight="bold" fill="#3A3530">[8,10]</text>
  <rect x="490" y="168" width="84" height="26" rx="5" fill="#E8E3D8" stroke="#8B8680" stroke-width="1.5"/>
  <text x="532" y="185" text-anchor="middle" font-size="11" font-weight="bold" fill="#3A3530">[15,18]</text>
  <text x="350" y="242" text-anchor="middle" font-size="11" fill="#7A7772" font-style="italic">[1,3] and [2,6] overlap → merged into [1,6]</text>
</svg>
</div>

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

**When to use:** The problem says "maximum activities", "schedule as many as possible", or "select non-conflicting events" — essentially interval scheduling phrased as a selection problem.

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

**When to use:** You can take *fractions* of items (unlike 0/1 knapsack which needs DP). Look for "maximize value with limited capacity" where partial selections are allowed.

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

**When to use:** Look for "jump game", "maximum subarray", "best time to buy/sell", or any problem where you scan an array and maintain a running best/state — local decisions at each index build up to the global answer.

Greedy choices on array elements, often with two pointers or sliding window.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 260" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <rect width="700" height="260" rx="12" fill="#FAF8F5"/>
  <text x="350" y="24" text-anchor="middle" font-size="14" font-weight="bold" fill="#3A3530">Greedy Activity Selection — Pick Earliest End Time</text>
  <line x1="140" y1="230" x2="620" y2="230" stroke="#B8B5B0" stroke-width="1"/>
  <g font-size="9" fill="#9A9792" text-anchor="middle">
    <line x1="140" y1="227" x2="140" y2="233" stroke="#B8B5B0"/><text x="140" y="244">0</text>
    <line x1="188" y1="227" x2="188" y2="233" stroke="#B8B5B0"/><text x="188" y="244">1</text>
    <line x1="236" y1="227" x2="236" y2="233" stroke="#B8B5B0"/><text x="236" y="244">2</text>
    <line x1="284" y1="227" x2="284" y2="233" stroke="#B8B5B0"/><text x="284" y="244">3</text>
    <line x1="332" y1="227" x2="332" y2="233" stroke="#B8B5B0"/><text x="332" y="244">4</text>
    <line x1="380" y1="229" x2="380" y2="231" stroke="#B8B5B0"/>
    <line x1="428" y1="227" x2="428" y2="233" stroke="#B8B5B0"/><text x="428" y="244">6</text>
    <line x1="476" y1="227" x2="476" y2="233" stroke="#B8B5B0"/><text x="476" y="244">7</text>
    <line x1="524" y1="229" x2="524" y2="231" stroke="#B8B5B0"/>
    <line x1="572" y1="227" x2="572" y2="233" stroke="#B8B5B0"/><text x="572" y="244">9</text>
    <line x1="620" y1="227" x2="620" y2="233" stroke="#B8B5B0"/><text x="620" y="244">10</text>
  </g>
  <text x="118" y="55" text-anchor="end" font-size="11" fill="#3A3530">A [0,2]</text>
  <rect x="140" y="42" width="96" height="20" rx="4" fill="#D4D8D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="188" y="56" text-anchor="middle" font-size="9" fill="#5A5752">1st</text>
  <text x="660" y="55" font-size="12" fill="#3A3530">✓</text>
  <text x="118" y="87" text-anchor="end" font-size="11" fill="#9A9792">B [1,4]</text>
  <rect x="188" y="74" width="144" height="20" rx="4" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="260" y="88" text-anchor="middle" font-size="9" fill="#9A9792">overlaps A</text>
  <text x="660" y="87" font-size="12" fill="#9A9792">✗</text>
  <text x="118" y="119" text-anchor="end" font-size="11" fill="#3A3530">C [3,6]</text>
  <rect x="284" y="106" width="144" height="20" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="356" y="120" text-anchor="middle" font-size="9" fill="#5A5752">2nd</text>
  <text x="660" y="119" font-size="12" fill="#3A3530">✓</text>
  <text x="118" y="151" text-anchor="end" font-size="11" fill="#9A9792">D [4,7]</text>
  <rect x="332" y="138" width="144" height="20" rx="4" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="404" y="152" text-anchor="middle" font-size="9" fill="#9A9792">overlaps C</text>
  <text x="660" y="151" font-size="12" fill="#9A9792">✗</text>
  <text x="118" y="183" text-anchor="end" font-size="11" fill="#3A3530">E [6,9]</text>
  <rect x="428" y="170" width="144" height="20" rx="4" fill="#E8E3D8" stroke="#8B8680" stroke-width="1.5"/>
  <text x="500" y="184" text-anchor="middle" font-size="9" fill="#5A5752">3rd</text>
  <text x="660" y="183" font-size="12" fill="#3A3530">✓</text>
  <text x="118" y="215" text-anchor="end" font-size="11" fill="#9A9792">F [7,10]</text>
  <rect x="476" y="202" width="144" height="20" rx="4" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="548" y="216" text-anchor="middle" font-size="9" fill="#9A9792">overlaps E</text>
  <text x="660" y="215" font-size="12" fill="#9A9792">✗</text>
</svg>
</div>

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

**When to use:** The problem says "smallest subsequence", "remove duplicate letters", "minimum swaps", or involves character frequency / ordering decisions — often solved with a stack-based greedy approach.

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

**When to use:** The problem says "assign cookies", "queue reconstruction", "two city scheduling", or any scenario where sorting by one dimension (size, cost difference, height) unlocks a simple greedy scan.

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
| 274 | H-Index | [Link](https://leetcode.com/problems/h-index/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/17/medium-274-h-index/) |

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

## Pattern Summary

| Pattern | Signal Phrases | Key Idea |
|---|---|---|
| Interval Scheduling | "non-overlapping", "minimum rooms" | Sort by end time, pick earliest |
| Activity Selection | "maximum activities", "schedule" | Sort by end, greedily select |
| Greedy on Arrays | "jump game", "max subarray" | Local decisions, running state |
| Greedy on Strings | "smallest subsequence", "remove duplicates" | Stack-based greedy |
| Greedy + Sorting | "assign cookies", "queue reconstruction" | Sort first, then greedily assign |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **DP (when greedy doesn't apply):** [Dynamic Programming](/posts/2025-10-29-leetcode-templates-dp/)
- **Data structures, Graph, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
