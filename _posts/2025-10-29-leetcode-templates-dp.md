---
layout: post
title: "Algorithm Templates: Dynamic Programming"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates dynamic-programming
permalink: /posts/2025-10-29-leetcode-templates-dp/
tags: [leetcode, templates, dp]
---

Dynamic Programming is the most common pattern in LeetCode Medium/Hard problems. If you only learn one advanced technique, make it DP.

> **New to DP?** The core idea is simple: **break a big problem into smaller overlapping subproblems, solve each once, and reuse the results.** That's it. Everything else is details.

## The DP Recipe (Use This Every Time)

Every DP problem follows the same four steps. Before writing any code, answer these questions on paper:

| Step | Question to Ask | Example (House Robber) |
|---|---|---|
| **1. Define state** | What does `dp[i]` represent? | `dp[i]` = max money robbing houses `0..i` |
| **2. Transition** | How does `dp[i]` relate to smaller subproblems? | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` |
| **3. Base case** | What are the smallest subproblems I know the answer to? | `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])` |
| **4. Answer** | Which cell contains the final answer? | `dp[n-1]` |

### How to Choose Which DP Type to Use

<svg viewBox="0 0 820 520" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="dp-arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#8B8680"/>
    </marker>
  </defs>

  <!-- Start node -->
  <rect x="290" y="10" width="240" height="40" rx="20" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="410" y="35" font-size="13" fill="#3A3530" font-weight="600" text-anchor="middle">What does the problem ask?</text>

  <!-- Level 1 branches -->
  <line x1="330" y1="50" x2="130" y2="90" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#dp-arr)"/>
  <line x1="410" y1="50" x2="410" y2="90" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#dp-arr)"/>
  <line x1="490" y1="50" x2="690" y2="90" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#dp-arr)"/>

  <!-- Branch labels -->
  <text x="215" y="68" font-size="10" fill="#9A9792" font-style="italic" text-anchor="middle">sequence / array</text>
  <text x="410" y="78" font-size="10" fill="#9A9792" font-style="italic" text-anchor="middle">grid / matrix</text>
  <text x="605" y="68" font-size="10" fill="#9A9792" font-style="italic" text-anchor="middle">choices / states</text>

  <!-- 1D DP -->
  <rect x="40" y="95" width="180" height="36" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="130" y="117" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">1D DP (Linear)</text>

  <!-- 2D DP -->
  <rect x="320" y="95" width="180" height="36" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="410" y="117" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">2D DP (Grid)</text>

  <!-- State Machine -->
  <rect x="600" y="95" width="180" height="36" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="690" y="117" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">State Machine DP</text>

  <!-- Sub-branches from 1D -->
  <line x1="90" y1="131" x2="90" y2="170" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#dp-arr)"/>
  <line x1="170" y1="131" x2="260" y2="170" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#dp-arr)"/>

  <text x="70" y="155" font-size="9" fill="#9A9792" font-style="italic">subsequence?</text>
  <text x="210" y="152" font-size="9" fill="#9A9792" font-style="italic">knapsack?</text>

  <rect x="20" y="175" width="140" height="32" rx="7" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="90" y="195" font-size="11" fill="#5A5752" font-weight="500" text-anchor="middle">LIS / Subsequence</text>

  <rect x="195" y="175" width="130" height="32" rx="7" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="260" y="195" font-size="11" fill="#5A5752" font-weight="500" text-anchor="middle">0/1 Knapsack</text>

  <!-- Sub-branches from State Machine -->
  <line x1="650" y1="131" x2="590" y2="170" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#dp-arr)"/>
  <line x1="730" y1="131" x2="780" y2="170" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#dp-arr)"/>

  <text x="600" y="155" font-size="9" fill="#9A9792" font-style="italic">buy/sell</text>
  <text x="770" y="155" font-size="9" fill="#9A9792" font-style="italic">games</text>

  <rect x="510" y="175" width="160" height="32" rx="7" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="590" y="195" font-size="11" fill="#5A5752" font-weight="500" text-anchor="middle">Stock Problems</text>

  <rect x="710" y="175" width="100" height="32" rx="7" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="760" y="195" font-size="11" fill="#5A5752" font-weight="500" text-anchor="middle">Bitmask DP</text>

  <!-- Second row: advanced types -->
  <text x="410" y="250" font-size="12" fill="#7A7772" font-weight="600" text-anchor="middle">Advanced Patterns (learn these after mastering the basics)</text>
  <line x1="100" y1="260" x2="720" y2="260" stroke="#E0DDD8" stroke-width="1"/>

  <!-- Advanced nodes -->
  <rect x="30" y="275" width="140" height="36" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="100" y="297" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">Interval DP</text>
  <text x="100" y="325" font-size="9" fill="#9A9792" text-anchor="middle">"merge / split ranges"</text>

  <rect x="210" y="275" width="120" height="36" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="270" y="297" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">Tree DP</text>
  <text x="270" y="325" font-size="9" fill="#9A9792" text-anchor="middle">"DP on subtrees"</text>

  <rect x="370" y="275" width="120" height="36" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="430" y="297" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">Digit DP</text>
  <text x="430" y="325" font-size="9" fill="#9A9792" text-anchor="middle">"count numbers ≤ N"</text>

  <rect x="530" y="275" width="140" height="36" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="600" y="297" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">DP + Bin Search</text>
  <text x="600" y="325" font-size="9" fill="#9A9792" text-anchor="middle">"optimize O(n²) → O(n log n)"</text>

  <!-- Quick reference box -->
  <rect x="50" y="360" width="720" height="150" rx="10" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.5"/>
  <text x="410" y="385" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Quick Pattern Recognition</text>
  <text x="70" y="410" font-size="11" fill="#5A5752">"Maximum / minimum of something"</text>
  <text x="530" y="410" font-size="11" fill="#8B8680">→ DP (optimization)</text>
  <text x="70" y="432" font-size="11" fill="#5A5752">"How many ways to..."</text>
  <text x="530" y="432" font-size="11" fill="#8B8680">→ DP (counting)</text>
  <text x="70" y="454" font-size="11" fill="#5A5752">"Is it possible to..."</text>
  <text x="530" y="454" font-size="11" fill="#8B8680">→ DP (feasibility) or greedy</text>
  <text x="70" y="476" font-size="11" fill="#5A5752">"Longest / shortest subsequence"</text>
  <text x="530" y="476" font-size="11" fill="#8B8680">→ LIS-style DP</text>
  <text x="70" y="498" font-size="11" fill="#5A5752">"Path in a grid"</text>
  <text x="530" y="498" font-size="11" fill="#8B8680">→ 2D DP</text>
</svg>

## Contents

- [1D DP (Linear)](#1d-dp-linear) -- House Robber, Coin Change, Knapsack
- [2D DP (Grid)](#2d-dp-grid) -- Unique Paths, Maximal Square
- [LIS (Longest Increasing Subsequence)](#lis-longest-increasing-subsequence)
- [State Machine DP](#state-machine-dp) -- Stock Buy/Sell, Cooldown
- [Interval DP](#interval-dp) -- Burst Balloons, Palindrome
- [DP on Trees](#dp-on-trees) -- House Robber III, Max Path Sum
- [DP + Binary Search](#dp-with-binary-search)
- [Digit DP](#digit-dp-count-numbers-with-property) -- Count numbers with property
- [Bitmask DP](#bitmask-dp-tsp--subsets) -- TSP, subsets

---

## 1D DP (Linear)

**When to use:** The problem involves a sequence (array, string) and asks for a maximum/minimum value or count. Each element either contributes to the answer or doesn't.

### The Pattern

{% raw %}
```
dp[i] = best answer considering elements 0..i
dp[i] depends on dp[i-1], dp[i-2], ... (look back at previous states)
```
{% endraw %}

### Example: House Robber (LC 198)

> "Given an array of house values, find the max money you can rob without robbing two adjacent houses."

**Thinking through the recipe:**

1. **State:** `dp[i]` = max money from houses `0..i`
2. **Transition:** For house `i`, either skip it (`dp[i-1]`) or rob it (`dp[i-2] + nums[i]`)
3. **Base:** `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`
4. **Answer:** `dp[n-1]`

<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- Houses -->
  <text x="20" y="20" font-size="12" fill="#7A7772" font-weight="600">Houses:</text>
  <rect x="90" y="5" width="60" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="120" y="25" font-size="13" fill="#5A5752" font-weight="600" text-anchor="middle">2</text>
  <rect x="170" y="5" width="60" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="200" y="25" font-size="13" fill="#5A5752" font-weight="600" text-anchor="middle">7</text>
  <rect x="250" y="5" width="60" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="280" y="25" font-size="13" fill="#5A5752" font-weight="600" text-anchor="middle">9</text>
  <rect x="330" y="5" width="60" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="360" y="25" font-size="13" fill="#5A5752" font-weight="600" text-anchor="middle">3</text>
  <rect x="410" y="5" width="60" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="440" y="25" font-size="13" fill="#5A5752" font-weight="600" text-anchor="middle">1</text>

  <!-- DP array -->
  <text x="20" y="75" font-size="12" fill="#7A7772" font-weight="600">dp[i]:</text>
  <rect x="90" y="58" width="60" height="30" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="120" y="78" font-size="13" fill="#3A6B3A" font-weight="700" text-anchor="middle">2</text>
  <rect x="170" y="58" width="60" height="30" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="200" y="78" font-size="13" fill="#3A6B3A" font-weight="700" text-anchor="middle">7</text>
  <rect x="250" y="58" width="60" height="30" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="280" y="78" font-size="13" fill="#3A6B3A" font-weight="700" text-anchor="middle">11</text>
  <rect x="330" y="58" width="60" height="30" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="360" y="78" font-size="13" fill="#3A6B3A" font-weight="700" text-anchor="middle">11</text>
  <rect x="410" y="58" width="60" height="30" rx="5" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="440" y="78" font-size="13" fill="#3A6B3A" font-weight="700" text-anchor="middle">12</text>

  <!-- Annotations -->
  <text x="120" y="108" font-size="9" fill="#9A9792" text-anchor="middle">base</text>
  <text x="200" y="108" font-size="9" fill="#9A9792" text-anchor="middle">max(2,7)</text>
  <text x="280" y="108" font-size="9" fill="#9A9792" text-anchor="middle">max(7, 2+9)</text>
  <text x="360" y="108" font-size="9" fill="#9A9792" text-anchor="middle">max(11, 7+3)</text>
  <text x="440" y="108" font-size="9" fill="#9A9792" text-anchor="middle">max(11, 11+1)</text>

  <!-- Result -->
  <text x="510" y="78" font-size="12" fill="#3A6B3A" font-weight="700">→ Answer: 12</text>
  <text x="510" y="98" font-size="10" fill="#9A9792">(rob houses 2, 9, 1)</text>

  <!-- Formula -->
  <rect x="90" y="130" width="460" height="50" rx="8" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.2"/>
  <text x="110" y="152" font-size="12" fill="#5A5752" font-weight="600">Transition:</text>
  <text x="200" y="152" font-size="12" fill="#5A5752" font-family="monospace">dp[i] = max(dp[i-1], dp[i-2] + nums[i])</text>
  <text x="200" y="170" font-size="10" fill="#9A9792">          skip i       rob i</text>
</svg>

{% raw %}
```cpp
int rob(vector<int>& nums) {
    int n = nums.size();
    if (n == 1) return nums[0];

    vector<int> dp(n);
    dp[0] = nums[0];
    dp[1] = max(nums[0], nums[1]);

    for (int i = 2; i < n; ++i)
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);

    return dp[n - 1];
}
```
{% endraw %}

### Template: 0/1 Knapsack

> "Given items with weights and values, maximize total value without exceeding capacity W."

The key insight: iterate items in the outer loop, **capacity in reverse** in the inner loop (to avoid using the same item twice).

{% raw %}
```cpp
int knapsack01(vector<int>& wt, vector<int>& val, int W) {
    vector<int> dp(W + 1, 0);
    for (int i = 0; i < (int)wt.size(); ++i)
        for (int w = W; w >= wt[i]; --w)
            dp[w] = max(dp[w], dp[w - wt[i]] + val[i]);
    return dp[W];
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 509 | Fibonacci Number | [Link](https://leetcode.com/problems/fibonacci-number/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-easy-509-fibonacci-number/) |
| 198 | House Robber | [Link](https://leetcode.com/problems/house-robber/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-198-house-robber/) |
| 279 | Perfect Squares | [Link](https://leetcode.com/problems/perfect-squares/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-14-medium-279-perfect-squares/) |
| 322 | Coin Change | [Link](https://leetcode.com/problems/coin-change/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-322-coin-change/) |
| 494 | Target Sum | [Link](https://leetcode.com/problems/target-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/15/medium-494-target-sum/) |
| 139 | Word Break | [Link](https://leetcode.com/problems/word-break/) | - |
| 487 | Max Consecutive Ones II | [Link](https://leetcode.com/problems/max-consecutive-ones-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/30/medium-487-max-consecutive-ones-ii/) |
| 983 | Minimum Cost For Tickets | [Link](https://leetcode.com/problems/minimum-cost-for-tickets/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-983-minimum-cost-for-tickets/) |
| 2466 | Count Ways To Build Good Strings | [Link](https://leetcode.com/problems/count-ways-to-build-good-strings/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/16/medium-2466-count-ways-to-build-good-strings/) |
| 32 | Longest Valid Parentheses | [Link](https://leetcode.com/problems/longest-valid-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-hard-32-longest-valid-parentheses/) |
| 91 | Decode Ways | [Link](https://leetcode.com/problems/decode-ways/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/09/medium-91-decode-ways/) |
| 416 | Partition Equal Subset Sum | [Link](https://leetcode.com/problems/partition-equal-subset-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/11/medium-416-partition-equal-subset-sum/) |
| 918 | Maximum Sum Circular Subarray | [Link](https://leetcode.com/problems/maximum-sum-circular-subarray/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/25/medium-918-maximum-sum-circular-subarray/) |

## 2D DP (Grid)

**When to use:** The problem involves a 2D grid/matrix and asks about paths, areas, or values computed from neighboring cells.

### The Pattern

{% raw %}
```
dp[i][j] = answer for subproblem ending at cell (i, j)
dp[i][j] depends on dp[i-1][j] (above), dp[i][j-1] (left), dp[i-1][j-1] (diagonal)
```
{% endraw %}

### Example: Unique Paths with Obstacles (LC 63)

> "Count paths from top-left to bottom-right in a grid (can only move right or down). Some cells are blocked."

<svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- Title -->
  <text x="10" y="20" font-size="12" fill="#7A7772" font-weight="600">Grid (0 = open, 1 = blocked):</text>
  <text x="350" y="20" font-size="12" fill="#7A7772" font-weight="600">DP table (number of paths):</text>

  <!-- Grid -->
  <rect x="10" y="35" width="60" height="40" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="40" y="60" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">0</text>
  <rect x="70" y="35" width="60" height="40" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="100" y="60" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">0</text>
  <rect x="130" y="35" width="60" height="40" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="160" y="60" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">0</text>

  <rect x="10" y="75" width="60" height="40" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="40" y="100" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">0</text>
  <rect x="70" y="75" width="60" height="40" fill="#E8D5D0" stroke="#C08070" stroke-width="1.8"/>
  <text x="100" y="100" font-size="14" fill="#8B3A2A" font-weight="700" text-anchor="middle">1</text>
  <rect x="130" y="75" width="60" height="40" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="160" y="100" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">0</text>

  <rect x="10" y="115" width="60" height="40" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="40" y="140" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">0</text>
  <rect x="70" y="115" width="60" height="40" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="100" y="140" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">0</text>
  <rect x="130" y="115" width="60" height="40" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="160" y="140" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">0</text>

  <!-- Arrow -->
  <text x="230" y="100" font-size="24" fill="#B8B5B0">→</text>

  <!-- DP table -->
  <rect x="350" y="35" width="60" height="40" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="380" y="60" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <rect x="410" y="35" width="60" height="40" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="440" y="60" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <rect x="470" y="35" width="60" height="40" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="500" y="60" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>

  <rect x="350" y="75" width="60" height="40" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="380" y="100" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <rect x="410" y="75" width="60" height="40" fill="#E8D5D0" stroke="#C08070" stroke-width="1.8"/>
  <text x="440" y="100" font-size="14" fill="#8B3A2A" font-weight="700" text-anchor="middle">0</text>
  <rect x="470" y="75" width="60" height="40" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="500" y="100" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>

  <rect x="350" y="115" width="60" height="40" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="380" y="140" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <rect x="410" y="115" width="60" height="40" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="440" y="140" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <rect x="470" y="115" width="60" height="40" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="500" y="140" font-size="14" fill="#3A6B3A" font-weight="700" text-anchor="middle">2</text>

  <!-- Annotations -->
  <text x="500" y="175" font-size="11" fill="#3A6B3A" font-weight="600" text-anchor="middle">Answer = 2</text>

  <!-- Formula box -->
  <rect x="10" y="190" width="520" height="120" rx="8" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.2"/>
  <text x="30" y="215" font-size="12" fill="#5A5752" font-weight="600">How each cell is computed:</text>
  <text x="30" y="240" font-size="11" fill="#5A5752" font-family="monospace">if grid[i][j] == blocked:  dp[i][j] = 0</text>
  <text x="30" y="260" font-size="11" fill="#5A5752" font-family="monospace">else:  dp[i][j] = dp[i-1][j] + dp[i][j-1]</text>
  <text x="30" y="280" font-size="10" fill="#9A9792">                    ↑ from above   ↑ from left</text>
  <text x="30" y="300" font-size="10" fill="#9A9792">First row and column: dp = 1 (only one path to reach each edge cell)</text>
</svg>

{% raw %}
```cpp
int uniquePathsWithObstacles(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    if (grid[0][0] == 1) return 0;

    vector<vector<int>> dp(m, vector<int>(n, 0));
    dp[0][0] = 1;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 1) { dp[i][j] = 0; continue; }
            if (i > 0) dp[i][j] += dp[i - 1][j];
            if (j > 0) dp[i][j] += dp[i][j - 1];
        }
    }
    return dp[m - 1][n - 1];
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 62 | Unique Paths | [Link](https://leetcode.com/problems/unique-paths/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/medium-62-unique-paths/) |
| 63 | Unique Paths II | [Link](https://leetcode.com/problems/unique-paths-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/21/medium-63-unique-paths-ii/) |
| 64 | Minimum Path Sum | [Link](https://leetcode.com/problems/minimum-path-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/10/medium-64-minimum-path-sum/) |
| 221 | Maximal Square | [Link](https://leetcode.com/problems/maximal-square/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/18/medium-221-maximal-square/) |
| 418 | Sentence Screen Fitting | [Link](https://leetcode.com/problems/sentence-screen-fitting/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/medium-418-sentence-screen-fitting/) |
| 568 | Maximum Vacation Days | [Link](https://leetcode.com/problems/maximum-vacation-days/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/hard-568-maximum-vacation-days/) |
| 96 | Unique Binary Search Trees | [Link](https://leetcode.com/problems/unique-binary-search-trees/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/03/medium-96-unique-binary-search-trees/) |

## LIS (Longest Increasing Subsequence)

**When to use:** Find the longest subsequence where elements are in strictly increasing order. Also applies to problems reducible to LIS (Russian Doll Envelopes, etc.).

### Visual Walkthrough

<svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- Array -->
  <text x="10" y="20" font-size="12" fill="#7A7772" font-weight="600">Array:</text>
  <rect x="80" y="5" width="45" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="102" y="25" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">10</text>
  <rect x="130" y="5" width="45" height="30" rx="5" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.5"/>
  <text x="152" y="25" font-size="12" fill="#3A6B3A" font-weight="700" text-anchor="middle">9</text>
  <rect x="180" y="5" width="45" height="30" rx="5" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.5"/>
  <text x="202" y="25" font-size="12" fill="#3A6B3A" font-weight="700" text-anchor="middle">2</text>
  <rect x="230" y="5" width="45" height="30" rx="5" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.5"/>
  <text x="252" y="25" font-size="12" fill="#3A6B3A" font-weight="700" text-anchor="middle">5</text>
  <rect x="280" y="5" width="45" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="302" y="25" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">3</text>
  <rect x="330" y="5" width="45" height="30" rx="5" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.5"/>
  <text x="352" y="25" font-size="12" fill="#3A6B3A" font-weight="700" text-anchor="middle">7</text>
  <rect x="380" y="5" width="45" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="402" y="25" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">101</text>
  <rect x="430" y="5" width="45" height="30" rx="5" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="452" y="25" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">18</text>

  <!-- LIS highlight -->
  <text x="510" y="25" font-size="11" fill="#3A6B3A" font-weight="600">LIS = [2, 5, 7, 101]</text>
  <text x="510" y="45" font-size="11" fill="#9A9792">Length = 4</text>

  <!-- DP array -->
  <text x="10" y="80" font-size="12" fill="#7A7772" font-weight="600">dp[i]:</text>
  <rect x="80" y="63" width="45" height="30" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="102" y="83" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <rect x="130" y="63" width="45" height="30" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="152" y="83" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <rect x="180" y="63" width="45" height="30" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="202" y="83" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">1</text>
  <rect x="230" y="63" width="45" height="30" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="252" y="83" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">2</text>
  <rect x="280" y="63" width="45" height="30" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="302" y="83" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">2</text>
  <rect x="330" y="63" width="45" height="30" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="352" y="83" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">3</text>
  <rect x="380" y="63" width="45" height="30" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="402" y="83" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">4</text>
  <rect x="430" y="63" width="45" height="30" rx="5" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="452" y="83" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">4</text>

  <text x="80" y="110" font-size="9" fill="#9A9792">dp[i] = length of longest increasing subsequence ending at index i</text>

  <!-- Two approaches comparison -->
  <rect x="10" y="130" width="310" height="120" rx="8" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.2"/>
  <text x="165" y="152" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">O(n²) DP Approach</text>
  <text x="30" y="172" font-size="10" fill="#5A5752">For each i, look back at all j &lt; i</text>
  <text x="30" y="190" font-size="10" fill="#5A5752">If nums[j] &lt; nums[i]: dp[i] = max(dp[i], dp[j]+1)</text>
  <text x="30" y="215" font-size="10" fill="#9A9792">Simple but slow for n &gt; 10⁴</text>
  <text x="30" y="235" font-size="10" fill="#9A9792">Good enough for most LC problems</text>

  <rect x="340" y="130" width="340" height="120" rx="8" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.2"/>
  <text x="510" y="152" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">O(n log n) Patience Sort</text>
  <text x="360" y="172" font-size="10" fill="#5A5752">Maintain a "tails" array of smallest tail elements</text>
  <text x="360" y="190" font-size="10" fill="#5A5752">Use binary search (lower_bound) to find position</text>
  <text x="360" y="215" font-size="10" fill="#9A9792">Fast enough for n up to 10⁵</text>
  <text x="360" y="235" font-size="10" fill="#9A9792">Tails array length = LIS length (but NOT the LIS)</text>
</svg>

### Template: O(n^2) DP

{% raw %}
```cpp
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);

    for (int i = 1; i < n; ++i)
        for (int j = 0; j < i; ++j)
            if (nums[j] < nums[i])
                dp[i] = max(dp[i], dp[j] + 1);

    return *max_element(dp.begin(), dp.end());
}
```
{% endraw %}

### Template: O(n log n) with Binary Search (Patience Sort)

{% raw %}
```cpp
int lengthOfLIS(vector<int>& nums) {
    vector<int> tails;
    for (int num : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), num);
        if (it == tails.end()) tails.push_back(num);
        else *it = num;
    }
    return tails.size();
}
```
{% endraw %}

### Template: Count Number of LIS (LC 673)

{% raw %}
```cpp
int findNumberOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> length(n, 1), count(n, 1);

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[j] < nums[i]) {
                if (length[j] + 1 > length[i]) {
                    length[i] = length[j] + 1;
                    count[i] = count[j];
                } else if (length[j] + 1 == length[i]) {
                    count[i] += count[j];
                }
            }
        }
    }

    int maxLen = *max_element(length.begin(), length.end());
    int result = 0;
    for (int i = 0; i < n; ++i)
        if (length[i] == maxLen) result += count[i];
    return result;
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 300 | Longest Increasing Subsequence | [Link](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-300-longest-increasing-subsequence/) |
| 673 | Number of Longest Increasing Subsequence | [Link](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/09/medium-673-number-of-longest-increasing-subsequence/) |
| 354 | Russian Doll Envelopes | [Link](https://leetcode.com/problems/russian-doll-envelopes/) | - |
| 334 | Increasing Triplet Subsequence | [Link](https://leetcode.com/problems/increasing-triplet-subsequence/) | - |

## Interval DP

**When to use:** The problem asks you to merge, split, or process contiguous ranges, and the optimal solution for a range depends on how you split it.

**The pattern:** Solve small intervals first, then build up to the full range by trying every possible split point.

{% raw %}
```
dp[i][j] = best answer for the subarray from index i to j
For each split point k in [i, j):
    dp[i][j] = best(dp[i][k] + dp[k+1][j] + merge_cost)
```
{% endraw %}

### Template

{% raw %}
```cpp
int intervalDP(vector<int>& arr) {
    int n = arr.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int i = 0; i < n; ++i) dp[i][i] = arr[i]; // base: length 1

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len - 1;
            for (int k = i; k < j; ++k)
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + cost(i, k, j));
        }
    }
    return dp[0][n - 1];
}
```
{% endraw %}

### Example: Burst Balloons (LC 312)

Think of it as: "which balloon do I burst **last** in the range `[i, j]`?"

{% raw %}
```cpp
int maxCoins(vector<int>& nums) {
    int n = nums.size();
    vector<int> arr = {1};
    arr.insert(arr.end(), nums.begin(), nums.end());
    arr.push_back(1);

    vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
    for (int len = 1; len <= n; ++len) {
        for (int i = 1; i <= n - len + 1; ++i) {
            int j = i + len - 1;
            for (int k = i; k <= j; ++k)
                dp[i][j] = max(dp[i][j],
                    dp[i][k - 1] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j + 1]);
        }
    }
    return dp[1][n];
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 312 | Burst Balloons | [Link](https://leetcode.com/problems/burst-balloons/) | - |
| 516 | Longest Palindromic Subsequence | [Link](https://leetcode.com/problems/longest-palindromic-subsequence/) | - |
| 1039 | Minimum Score Triangulation of Polygon | [Link](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) | - |
| 1130 | Minimum Cost Tree From Leaf Values | [Link](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) | - |

## State Machine DP

**When to use:** The problem has distinct "modes" or "phases" where different rules apply. The classic example is the stock buy/sell family: at any moment, you're either holding a stock or not.

### The Key Idea

Instead of one DP array, maintain **multiple arrays** -- one for each state. At each step, decide which state transitions are legal.

### State Diagram: Stock Buy/Sell

<svg viewBox="0 0 680 280" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="sm-arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#8B8680"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="340" y="20" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Basic Buy/Sell (LC 122: unlimited transactions)</text>

  <!-- NOT HOLDING state -->
  <ellipse cx="170" cy="100" rx="90" ry="35" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/>
  <text x="170" y="95" font-size="13" fill="#3A6B3A" font-weight="700" text-anchor="middle">Not Holding</text>
  <text x="170" y="112" font-size="10" fill="#5A6B5A" text-anchor="middle">dp[i][1]</text>

  <!-- HOLDING state -->
  <ellipse cx="510" cy="100" rx="90" ry="35" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/>
  <text x="510" y="95" font-size="13" fill="#8B3A2A" font-weight="700" text-anchor="middle">Holding</text>
  <text x="510" y="112" font-size="10" fill="#8B5A4A" text-anchor="middle">dp[i][0]</text>

  <!-- Buy arrow (not holding → holding) -->
  <path d="M260,85 Q340,50 420,85" fill="none" stroke="#C08070" stroke-width="1.8" marker-end="url(#sm-arr)"/>
  <text x="340" y="55" font-size="11" fill="#8B3A2A" font-weight="600" text-anchor="middle">buy (-price[i])</text>

  <!-- Sell arrow (holding → not holding) -->
  <path d="M420,115 Q340,150 260,115" fill="none" stroke="#6B8B6B" stroke-width="1.8" marker-end="url(#sm-arr)"/>
  <text x="340" y="158" font-size="11" fill="#3A6B3A" font-weight="600" text-anchor="middle">sell (+price[i])</text>

  <!-- Self-loop: wait (not holding) -->
  <path d="M105,75 Q60,40 105,75" fill="none" stroke="#B8B5B0" stroke-width="1.3"/>
  <text x="88" y="58" font-size="10" fill="#9A9792" text-anchor="middle">wait</text>

  <!-- Self-loop: wait (holding) -->
  <path d="M575,75 Q620,40 575,75" fill="none" stroke="#B8B5B0" stroke-width="1.3"/>
  <text x="592" y="58" font-size="10" fill="#9A9792" text-anchor="middle">wait</text>

  <!-- With Cooldown variant -->
  <text x="340" y="200" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">With Cooldown (LC 309: must wait 1 day after selling)</text>

  <!-- Three states -->
  <rect x="30" y="220" width="130" height="40" rx="10" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.5"/>
  <text x="95" y="245" font-size="11" fill="#3A6B3A" font-weight="600" text-anchor="middle">Rest (free)</text>

  <rect x="265" y="220" width="130" height="40" rx="10" fill="#E8D5D0" stroke="#C08070" stroke-width="1.5"/>
  <text x="330" y="245" font-size="11" fill="#8B3A2A" font-weight="600" text-anchor="middle">Holding</text>

  <rect x="500" y="220" width="130" height="40" rx="10" fill="#D4D8E0" stroke="#7080A0" stroke-width="1.5"/>
  <text x="565" y="245" font-size="11" fill="#3A4A6B" font-weight="600" text-anchor="middle">Cooldown</text>

  <!-- Arrows between three states -->
  <line x1="160" y1="235" x2="260" y2="235" stroke="#C08070" stroke-width="1.3" marker-end="url(#sm-arr)"/>
  <text x="210" y="228" font-size="9" fill="#8B3A2A">buy</text>

  <line x1="395" y1="235" x2="495" y2="235" stroke="#7080A0" stroke-width="1.3" marker-end="url(#sm-arr)"/>
  <text x="445" y="228" font-size="9" fill="#3A4A6B">sell</text>

  <path d="M565,220 Q565,190 95,220" fill="none" stroke="#6B8B6B" stroke-width="1.3" marker-end="url(#sm-arr)"/>
  <text x="340" y="190" font-size="9" fill="#3A6B3A">wait 1 day (cooldown → rest)</text>
</svg>

### Template: Basic Buy/Sell (unlimited transactions)

{% raw %}
```cpp
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    vector<vector<int>> dp(n, vector<int>(2, 0));

    dp[0][0] = -prices[0];  // holding: bought on day 0
    dp[0][1] = 0;            // not holding: did nothing

    for (int i = 1; i < n; ++i) {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]); // hold or buy
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i]); // rest or sell
    }
    return dp[n - 1][1];
}
```
{% endraw %}

### Template: With Cooldown (3 states)

{% raw %}
```cpp
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    vector<vector<int>> dp(n, vector<int>(3, 0));

    dp[0][0] = 0;            // rest
    dp[0][1] = -prices[0];   // hold
    dp[0][2] = INT_MIN;      // sold (impossible on day 0)

    for (int i = 1; i < n; ++i) {
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][2]);              // rest or cooldown done
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]);  // hold or buy
        dp[i][2] = dp[i - 1][1] + prices[i];                      // sell
    }
    return max(dp[n - 1][0], dp[n - 1][2]);
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 121 | Best Time to Buy and Sell Stock | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | - |
| 122 | Best Time to Buy and Sell Stock II | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | - |
| 123 | Best Time to Buy and Sell Stock III | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | - |
| 188 | Best Time to Buy and Sell Stock IV | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | - |
| 309 | Best Time to Buy and Sell Stock with Cooldown | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/20/medium-309-best-time-to-buy-and-sell-stock-with-cooldown/) |
| 714 | Best Time to Buy and Sell Stock with Transaction Fee | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | - |

## DP on Trees

**When to use:** The problem asks for an optimal value on a tree structure. Each subtree is a subproblem, and you combine children's results at each node.

**The pattern:** DFS returns DP values from leaves up. Each node returns a pair/tuple: `{answer if we take this node, answer if we skip it}`.

<svg viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- Tree structure -->
  <text x="10" y="20" font-size="12" fill="#7A7772" font-weight="600">House Robber III: Can't rob parent + child</text>

  <!-- Root -->
  <circle cx="200" cy="50" r="18" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/>
  <text x="200" y="55" font-size="12" fill="#3A6B3A" font-weight="700" text-anchor="middle">3</text>

  <!-- Left child -->
  <line x1="186" y1="65" x2="130" y2="100" stroke="#B8B5B0" stroke-width="1.3"/>
  <circle cx="120" cy="110" r="18" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/>
  <text x="120" y="115" font-size="12" fill="#8B3A2A" font-weight="700" text-anchor="middle">2</text>

  <!-- Right child -->
  <line x1="214" y1="65" x2="270" y2="100" stroke="#B8B5B0" stroke-width="1.3"/>
  <circle cx="280" cy="110" r="18" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/>
  <text x="280" y="115" font-size="12" fill="#8B3A2A" font-weight="700" text-anchor="middle">3</text>

  <!-- Grandchildren -->
  <line x1="133" y1="125" x2="160" y2="155" stroke="#B8B5B0" stroke-width="1.3"/>
  <circle cx="165" cy="165" r="18" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/>
  <text x="165" y="170" font-size="12" fill="#3A6B3A" font-weight="700" text-anchor="middle">3</text>

  <line x1="293" y1="125" x2="320" y2="155" stroke="#B8B5B0" stroke-width="1.3"/>
  <circle cx="325" cy="165" r="18" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/>
  <text x="325" y="170" font-size="12" fill="#3A6B3A" font-weight="700" text-anchor="middle">1</text>

  <!-- Explanation -->
  <rect x="390" y="35" width="200" height="155" rx="8" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.2"/>
  <text x="410" y="58" font-size="11" fill="#5A5752" font-weight="600">Option A: Rob root + leaves</text>
  <text x="410" y="78" font-size="11" fill="#3A6B3A">3 + 3 + 1 = 7 (optimal)</text>
  <text x="410" y="108" font-size="11" fill="#5A5752" font-weight="600">Option B: Rob middle level</text>
  <text x="410" y="128" font-size="11" fill="#8B3A2A">2 + 3 = 5</text>
  <circle cx="420" cy="155" r="6" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1"/>
  <text x="432" y="159" font-size="9" fill="#9A9792">= robbed</text>
  <circle cx="420" cy="175" r="6" fill="#E8D5D0" stroke="#C08070" stroke-width="1"/>
  <text x="432" y="179" font-size="9" fill="#9A9792">= skipped</text>
</svg>

### Template: Tree DP (House Robber III, LC 337)

{% raw %}
```cpp
pair<int, int> dfs(TreeNode* root) {
    if (!root) return {0, 0};

    auto left = dfs(root->left);
    auto right = dfs(root->right);

    int skip = max(left.first, left.second) + max(right.first, right.second);
    int take = root->val + left.first + right.first;

    return {skip, take};  // {not take, take}
}

int rob(TreeNode* root) {
    auto [skip, take] = dfs(root);
    return max(skip, take);
}
```
{% endraw %}

### Template: Max Path Sum (LC 124)

Each node contributes its value + best single path from one child. But the answer can also be a path through the node connecting both children.

{% raw %}
```cpp
int maxPathSum(TreeNode* root) {
    int maxSum = INT_MIN;

    function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
        if (!node) return 0;
        int left = max(0, dfs(node->left));
        int right = max(0, dfs(node->right));
        maxSum = max(maxSum, node->val + left + right); // path through node
        return node->val + max(left, right);             // best single path up
    };

    dfs(root);
    return maxSum;
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 337 | House Robber III | [Link](https://leetcode.com/problems/house-robber-iii/) | - |
| 124 | Binary Tree Maximum Path Sum | [Link](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | - |
| 968 | Binary Tree Cameras | [Link](https://leetcode.com/problems/binary-tree-cameras/) | - |

## DP with Binary Search

**When to use:** A pure DP solution is O(n^2) or worse, and binary search can help find the optimal transition in O(log n), bringing total time down.

### Template: Binary Search on Answer (LC 410)

> "Split array into `m` subarrays to minimize the largest subarray sum."

The insight: binary search on the answer (the maximum sum), and use a greedy check.

{% raw %}
```cpp
bool canSplit(vector<int>& nums, int m, int maxSum) {
    int count = 1, sum = 0;
    for (int num : nums) {
        if (sum + num > maxSum) { ++count; sum = num; }
        else sum += num;
    }
    return count <= m;
}

int splitArray(vector<int>& nums, int m) {
    int lo = *max_element(nums.begin(), nums.end());
    int hi = accumulate(nums.begin(), nums.end(), 0);

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (canSplit(nums, m, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 300 | Longest Increasing Subsequence | [Link](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-300-longest-increasing-subsequence/) |
| 410 | Split Array Largest Sum | [Link](https://leetcode.com/problems/split-array-largest-sum/) | - |
| 875 | Koko Eating Bananas | [Link](https://leetcode.com/problems/koko-eating-bananas/) | - |
| 1011 | Capacity To Ship Packages | [Link](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | - |

## Digit DP (count numbers with property)

**When to use:** "How many integers in `[1, N]` satisfy some digit-based property?" (e.g., no repeated digits, digit sum = k, etc.)

**The pattern:** Process digits left to right, tracking:
- `tight`: are we still bounded by `N`'s digits?
- `started`: have we placed a non-zero digit yet?
- Any property-specific state (previous digit, digit sum, etc.)

### Template

{% raw %}
```cpp
string sN;
long long dp[20][11][2][2];

long long dfs(int i, int prev, bool tight, bool started) {
    if (i == (int)sN.size()) return started ? 1 : 0;
    auto& res = dp[i][prev + 1][tight][started];
    if (res != -1) return res;
    res = 0;

    int limit = tight ? (sN[i] - '0') : 9;
    for (int d = 0; d <= limit; ++d) {
        bool nt = tight && (d == limit);
        bool ns = started || (d != 0);
        if (!ns || prev == -1 || d != prev) // example: no consecutive same digits
            res += dfs(i + 1, ns ? d : prev, nt, ns);
    }
    return res;
}

long long solve(long long N) {
    sN = to_string(N);
    memset(dp, -1, sizeof dp);
    return dfs(0, -1, true, false);
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 233 | Number of Digit One | [Link](https://leetcode.com/problems/number-of-digit-one/) | - |
| 902 | Numbers At Most N Given Digit Set | [Link](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | - |
| 1012 | Numbers With Repeated Digits | [Link](https://leetcode.com/problems/numbers-with-repeated-digits/) | - |

## Bitmask DP (TSP / subsets)

**When to use:** The problem has a small set of items (n le 20) and you need to track which items have been used. Each bit in a bitmask represents "used" (1) or "not used" (0).

**The key constraint:** n le 20 (otherwise 2^n states explode). If you see n le 15text{-}20 in the constraints, think bitmask.

### Template: Traveling Salesman (TSP)

{% raw %}
```cpp
int tsp(const vector<vector<int>>& w) {
    int n = w.size();
    const int INF = 1e9;
    // dp[mask][u] = min cost to visit all nodes in mask, ending at u
    vector<vector<int>> dp(1 << n, vector<int>(n, INF));
    dp[1][0] = 0; // start at node 0

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (dp[mask][u] >= INF) continue;
            for (int v = 0; v < n; ++v) {
                if (mask & (1 << v)) continue; // already visited
                int next = mask | (1 << v);
                dp[next][v] = min(dp[next][v], dp[mask][u] + w[u][v]);
            }
        }
    }
    return *min_element(dp.back().begin(), dp.back().end());
}
```
{% endraw %}

| ID | Title | Link | Solution |
|---|---|---|---|
| 847 | Shortest Path Visiting All Nodes | [Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | - |
| 698 | Partition to K Equal Sum Subsets | [Link](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | - |
| 1340 | Jump Game V | [Link](https://leetcode.com/problems/jump-game-v/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/10/hard-1340-jump-game-v/) |
| 464 | Can I Win | [Link](https://leetcode.com/problems/can-i-win/) | - |
| 691 | Stickers to Spell Word | [Link](https://leetcode.com/problems/stickers-to-spell-word/) | - |

---

## Summary: When to Use Each DP Type

| Type | Signal in Problem | Time | Space |
|---|---|---|---|
| **1D Linear** | Sequence, "rob/skip", coin change | O(n) or O(n × W) | O(n) or O(W) |
| **2D Grid** | Matrix, paths, grid traversal | O(m × n) | O(m × n) |
| **LIS** | Longest increasing/decreasing subsequence | O(n^2) or O(n log n) | O(n) |
| **State Machine** | Buy/sell, hold/not hold, cooldown | O(n × k) | O(n × k) |
| **Interval** | Merge/split ranges, balloons, palindromes | O(n^3) | O(n^2) |
| **Tree** | DP on subtrees, tree paths | O(n) | O(n) |
| **Digit** | "Count numbers in [1, N] with property" | O(text{digits} × text{states}) | Same |
| **Bitmask** | Small n (le 20), subset selection | O(2^n × n) | O(2^n × n) |

## More Templates

- **Data Structures (segment tree, Fenwick):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search (binary search on answer):** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **DFS + Memoization (grid DP):** [DFS](/posts/2025-11-24-leetcode-templates-dfs/)
- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)