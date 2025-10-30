---
layout: post
title: "LeetCode Templates: Dynamic Programming"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates dynamic-programming
permalink: /posts/2025-10-29-leetcode-templates-dp/
tags: [leetcode, templates, dp]
---

## Contents

- [1D DP](#1d-dp-knapsacklinear)
- [2D DP](#2d-dp-gridpath)
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

| ID | Title | Link |
|---|---|---|
| 322 | Coin Change | https://leetcode.com/problems/coin-change/ |
| 139 | Word Break | https://leetcode.com/problems/word-break/ |

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

| ID | Title | Link |
|---|---|---|
| 62 | Unique Paths | https://leetcode.com/problems/unique-paths/ |
| 63 | Unique Paths II | https://leetcode.com/problems/unique-paths-ii/ |
| 221 | Maximal Square | https://leetcode.com/problems/maximal-square/ |

## Digit DP (count numbers with property)

```cpp
long long dp[20][11][2][2]; string sN;
long long dfsDP(int i,int prev,bool tight,bool started){ if(i==(int)sN.size()) return started?1:0; auto &res=dp[i][prev+1][tight][started]; if(res!=-1) return res; res=0; int lim=tight?(sN[i]-'0'):9;
    for(int d=0; d<=lim; ++d){ bool nt=tight && d==lim; bool ns=started||d!=0; if(!ns || prev==-1 || d!=prev) res+=dfsDP(i+1, ns?d:prev, nt, ns); }
    return res; }
long long solveDP(long long N){ sN=to_string(N); memset(dp,-1,sizeof dp); return dfsDP(0,-1,1,0); }
```

| ID | Title | Link |
|---|---|---|
| 233 | Number of Digit One | https://leetcode.com/problems/number-of-digit-one/ |
| 902 | Numbers At Most N Given Digit Set | https://leetcode.com/problems/numbers-at-most-n-given-digit-set/ |
| 1012 | Numbers With Repeated Digits | https://leetcode.com/problems/numbers-with-repeated-digits/ |

## Bitmask DP (TSP / subsets)

```cpp
int tsp(const vector<vector<int>>& w){
    int n=w.size(); const int INF=1e9; vector<vector<int>> dp(1<<n, vector<int>(n, INF));
    dp[1][0]=0; for(int mask=1; mask<(1<<n); ++mask){ for(int u=0; u<n; ++u) if(dp[mask][u]<INF){ for(int v=0; v<n; ++v) if(!(mask&(1<<v))) dp[mask|1<<v][v] = min(dp[mask|1<<v][v], dp[mask][u]+w[u][v]); } }
    return *min_element(dp.back().begin(), dp.back().end());
}
```

| ID | Title | Link |
|---|---|---|
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |
| 698 | Partition to K Equal Sum Subsets | https://leetcode.com/problems/partition-to-k-equal-sum-subsets/ |
