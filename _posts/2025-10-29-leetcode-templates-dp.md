---
layout: post
title: "Algorithm Templates: Dynamic Programming"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates dynamic-programming
permalink: /posts/2025-10-29-leetcode-templates-dp/
tags: [leetcode, templates, dp]
---

Minimal, copy-paste C++ for 1D/2D DP, LIS, interval DP, state machine, digit DP, and bitmask DP.

## Contents

- [1D DP](#1d-dp-knapsacklinear)
- [2D DP](#2d-dp-gridpath)
- [LIS (Longest Increasing Subsequence)](#lis-longest-increasing-subsequence)
- [Interval DP](#interval-dp)
- [State Machine DP](#state-machine-dp)
- [DP on Trees](#dp-on-trees)
- [DP with Binary Search](#dp-with-binary-search)
- [Digit DP](#digit-dp-count-numbers-with-property)
- [Bitmask DP](#bitmask-dp-tsp--subsets)

## 1D DP (knapsack/linear)

```cpp
int knap01(vector<int>& wt, vector<int>& val, int W){
    vector<int> dp(W+1, 0);
    for (int i=0;i<(int)wt.size();++i)
        for (int w=W; w>=wt[i]; --w)
            dp[w] = max(dp[w], dp[w-wt[i]] + val[i]);
    return dp[W];
}
```

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

## 2D DP (grid/path)

```cpp
int uniquePaths(vector<vector<int>>& g){
    int m=g.size(), n=g[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    if (g[0][0]==1) return 0; dp[0][0]=1;
    for (int i=0;i<m;++i) for(int j=0;j<n;++j){
        if (g[i][j]==1){ dp[i][j]=0; continue; }
        if (i) dp[i][j]+=dp[i-1][j];
        if (j) dp[i][j]+=dp[i][j-1];
    }
    return dp[m-1][n-1];
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 62 | Unique Paths | [Link](https://leetcode.com/problems/unique-paths/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/medium-62-unique-paths/) |
| 63 | Unique Paths II | [Link](https://leetcode.com/problems/unique-paths-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/21/medium-63-unique-paths-ii/) |
| 64 | Minimum Path Sum | [Link](https://leetcode.com/problems/minimum-path-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/10/medium-64-minimum-path-sum/) |
| 221 | Maximal Square | [Link](https://leetcode.com/problems/maximal-square/) | - |
| 418 | Sentence Screen Fitting | [Link](https://leetcode.com/problems/sentence-screen-fitting/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/medium-418-sentence-screen-fitting/) |
| 568 | Maximum Vacation Days | [Link](https://leetcode.com/problems/maximum-vacation-days/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/hard-568-maximum-vacation-days/) |
| 96 | Unique Binary Search Trees | [Link](https://leetcode.com/problems/unique-binary-search-trees/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/03/medium-96-unique-binary-search-trees/) |

## LIS (Longest Increasing Subsequence)

Find the longest subsequence where elements are in strictly increasing order.

### Template: O(n²) DP

```cpp
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    
    return *max_element(dp.begin(), dp.end());
}
```

### Template: O(n log n) with Binary Search

```cpp
int lengthOfLIS(vector<int>& nums) {
    vector<int> tails;
    
    for (int num : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), num);
        if (it == tails.end()) {
            tails.push_back(num);
        } else {
            *it = num;
        }
    }
    
    return tails.size();
}
```

### Count Number of LIS

```cpp
int findNumberOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> length(n, 1), count(n, 1);
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
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
    for (int i = 0; i < n; i++) {
        if (length[i] == maxLen) {
            result += count[i];
        }
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 300 | Longest Increasing Subsequence | [Link](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-300-longest-increasing-subsequence/) |
| 673 | Number of Longest Increasing Subsequence | [Link](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/09/medium-673-number-of-longest-increasing-subsequence/) |
| 354 | Russian Doll Envelopes | [Link](https://leetcode.com/problems/russian-doll-envelopes/) | - |
| 334 | Increasing Triplet Subsequence | [Link](https://leetcode.com/problems/increasing-triplet-subsequence/) | - |

## Interval DP

DP on intervals - solve subproblems for all intervals of length `len`, then combine.

### Template

```cpp
int intervalDP(vector<int>& arr) {
    int n = arr.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    // Base case: length 1
    for (int i = 0; i < n; i++) {
        dp[i][i] = arr[i]; // or base value
    }
    
    // Length 2 to n
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            
            // Try all splits
            for (int k = i; k < j; k++) {
                dp[i][j] = max(dp[i][j], 
                              dp[i][k] + dp[k+1][j] + cost(i, k, j));
            }
        }
    }
    
    return dp[0][n-1];
}
```

### Example: Burst Balloons

```cpp
int maxCoins(vector<int>& nums) {
    int n = nums.size();
    vector<int> arr = {1};
    arr.insert(arr.end(), nums.begin(), nums.end());
    arr.push_back(1);
    
    vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
    
    for (int len = 1; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            for (int k = i; k <= j; k++) {
                dp[i][j] = max(dp[i][j],
                              dp[i][k-1] + dp[k+1][j] + 
                              arr[i-1] * arr[k] * arr[j+1]);
            }
        }
    }
    
    return dp[1][n];
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 312 | Burst Balloons | [Link](https://leetcode.com/problems/burst-balloons/) | - |
| 516 | Longest Palindromic Subsequence | [Link](https://leetcode.com/problems/longest-palindromic-subsequence/) | - |
| 1039 | Minimum Score Triangulation of Polygon | [Link](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) | - |
| 1130 | Minimum Cost Tree From Leaf Values | [Link](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) | - |

## State Machine DP

DP where state transitions follow a state machine pattern.

### Template: Buy/Sell Stock Pattern

```cpp
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    // dp[i][0] = holding stock, dp[i][1] = not holding stock
    vector<vector<int>> dp(n, vector<int>(2, 0));
    
    dp[0][0] = -prices[0]; // Buy on day 0
    dp[0][1] = 0;           // Don't buy on day 0
    
    for (int i = 1; i < n; i++) {
        // Hold: max(keep holding, buy today)
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]);
        // Not hold: max(keep not holding, sell today)
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i]);
    }
    
    return dp[n-1][1];
}
```

### Template: Multiple States

```cpp
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    // States: rest, hold, sold (cooldown)
    vector<vector<int>> dp(n, vector<int>(3, 0));
    
    dp[0][0] = 0;           // rest
    dp[0][1] = -prices[0];  // hold
    dp[0][2] = INT_MIN;     // sold
    
    for (int i = 1; i < n; i++) {
        dp[i][0] = max(dp[i-1][0], dp[i-1][2]); // rest from rest or cooldown
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]); // hold from hold or buy
        dp[i][2] = dp[i-1][1] + prices[i]; // sell
    }
    
    return max(dp[n-1][0], dp[n-1][2]);
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 121 | Best Time to Buy and Sell Stock | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | - |
| 122 | Best Time to Buy and Sell Stock II | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | - |
| 123 | Best Time to Buy and Sell Stock III | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | - |
| 188 | Best Time to Buy and Sell Stock IV | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | - |
| 309 | Best Time to Buy and Sell Stock with Cooldown | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | - |
| 714 | Best Time to Buy and Sell Stock with Transaction Fee | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | - |

## DP on Trees

DP where subproblems are solved on subtrees.

### Template: Tree DP

```cpp
pair<int, int> dfs(TreeNode* root) {
    if (!root) return {0, 0};
    
    auto left = dfs(root->left);
    auto right = dfs(root->right);
    
    // dp[0] = not take current, dp[1] = take current
    int notTake = max(left.first, left.second) + 
                  max(right.first, right.second);
    int take = root->val + left.first + right.first;
    
    return {notTake, take};
}

int rob(TreeNode* root) {
    auto result = dfs(root);
    return max(result.first, result.second);
}
```

### Template: Path Problems

```cpp
int maxPathSum(TreeNode* root) {
    int maxSum = INT_MIN;
    
    function<int(TreeNode*)> dfs = [&](TreeNode* node) {
        if (!node) return 0;
        
        int left = max(0, dfs(node->left));
        int right = max(0, dfs(node->right));
        
        // Path through current node
        maxSum = max(maxSum, node->val + left + right);
        
        // Return max path ending at current node
        return node->val + max(left, right);
    };
    
    dfs(root);
    return maxSum;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 337 | House Robber III | [Link](https://leetcode.com/problems/house-robber-iii/) | - |
| 124 | Binary Tree Maximum Path Sum | [Link](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | - |
| 968 | Binary Tree Cameras | [Link](https://leetcode.com/problems/binary-tree-cameras/) | - |

## DP with Binary Search

Combine DP with binary search for optimization.

### Template: LIS with Binary Search

```cpp
int lengthOfLIS(vector<int>& nums) {
    vector<int> tails;
    
    for (int num : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), num);
        if (it == tails.end()) {
            tails.push_back(num);
        } else {
            *it = num;
        }
    }
    
    return tails.size();
}
```

### Template: DP + Binary Search on Answer

```cpp
int splitArray(vector<int>& nums, int m) {
    int left = *max_element(nums.begin(), nums.end());
    int right = accumulate(nums.begin(), nums.end(), 0);
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (canSplit(nums, m, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    
    return left;
}

bool canSplit(vector<int>& nums, int m, int maxSum) {
    int count = 1, sum = 0;
    
    for (int num : nums) {
        if (sum + num > maxSum) {
            count++;
            sum = num;
        } else {
            sum += num;
        }
    }
    
    return count <= m;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 300 | Longest Increasing Subsequence | [Link](https://leetcode.com/problems/longest-increasing-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-300-longest-increasing-subsequence/) |
| 410 | Split Array Largest Sum | [Link](https://leetcode.com/problems/split-array-largest-sum/) | - |
| 875 | Koko Eating Bananas | [Link](https://leetcode.com/problems/koko-eating-bananas/) | - |
| 1011 | Capacity To Ship Packages | [Link](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | - |

## Digit DP (count numbers with property)

```cpp
long long dp[20][11][2][2]; string sN;
long long dfsDP(int i,int prev,bool tight,bool started){ if(i==(int)sN.size()) return started?1:0; auto &res=dp[i][prev+1][tight][started]; if(res!=-1) return res; res=0; int lim=tight?(sN[i]-'0'):9;
    for(int d=0; d<=lim; ++d){ bool nt=tight && d==lim; bool ns=started||d!=0; if(!ns || prev==-1 || d!=prev) res+=dfsDP(i+1, ns?d:prev, nt, ns); }
    return res; }
long long solveDP(long long N){ sN=to_string(N); memset(dp,-1,sizeof dp); return dfsDP(0,-1,1,0); }
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 233 | Number of Digit One | [Link](https://leetcode.com/problems/number-of-digit-one/) | - |
| 902 | Numbers At Most N Given Digit Set | [Link](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | - |
| 1012 | Numbers With Repeated Digits | [Link](https://leetcode.com/problems/numbers-with-repeated-digits/) | - |

## Bitmask DP (TSP / subsets)

```cpp
int tsp(const vector<vector<int>>& w){
    int n=w.size(); const int INF=1e9; vector<vector<int>> dp(1<<n, vector<int>(n, INF));
    dp[1][0]=0; for(int mask=1; mask<(1<<n); ++mask){ for(int u=0; u<n; ++u) if(dp[mask][u]<INF){ for(int v=0; v<n; ++v) if(!(mask&(1<<v))) dp[mask|1<<v][v] = min(dp[mask|1<<v][v], dp[mask][u]+w[u][v]); } }
    return *min_element(dp.back().begin(), dp.back().end());
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 847 | Shortest Path Visiting All Nodes | [Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | - |
| 698 | Partition to K Equal Sum Subsets | [Link](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | - |
| 1340 | Jump Game V | [Link](https://leetcode.com/problems/jump-game-v/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/10/hard-1340-jump-game-v/) |
| 464 | Can I Win | [Link](https://leetcode.com/problems/can-i-win/) | - |
| 691 | Stickers to Spell Word | [Link](https://leetcode.com/problems/stickers-to-spell-word/) | - |

## More templates

- **Data structures (segment tree, Fenwick):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search (binary search on answer):** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)