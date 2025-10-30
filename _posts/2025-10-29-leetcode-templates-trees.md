---
layout: post
title: "LeetCode Templates: Trees"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates trees
permalink: /posts/2025-10-29-leetcode-templates-trees/
tags: [leetcode, templates, trees]
---

## Contents

- [Traversals (iterative)](#traversals-iterative)
- [LCA (Binary Lifting)](#lca-binary-lifting)
- [HLD (Heavy-Light Decomposition)](#hld-heavy-light-decomposition-skeleton)

## Traversals (iterative)

```cpp
vector<int> inorder(TreeNode* root){
    vector<int> ans; stack<TreeNode*> st; auto cur = root;
    while (cur || !st.empty()){
        while (cur){ st.push(cur); cur = cur->left; }
        cur = st.top(); st.pop(); ans.push_back(cur->val); cur = cur->right;
    }
    return ans;
}
```

```cpp
vector<vector<int>> levelOrder(TreeNode* root){
    vector<vector<int>> res; if(!root) return res; queue<TreeNode*> q; q.push(root);
    while(!q.empty()){
        int sz=q.size(); res.emplace_back();
        while(sz--){ auto* u=q.front(); q.pop(); res.back().push_back(u->val);
            if(u->left) q.push(u->left); if(u->right) q.push(u->right);
        }
    }
    return res;
}
```

| ID | Title | Link |
|---|---|---|
| 94 | Binary Tree Inorder Traversal | https://leetcode.com/problems/binary-tree-inorder-traversal/ |
| 102 | Binary Tree Level Order Traversal | https://leetcode.com/problems/binary-tree-level-order-traversal/ |

## LCA (Binary Lifting)

```cpp
const int K = 17; vector<int> depth; vector<array<int,K+1>> up;
void dfsLift(int u,int p,const vector<vector<int>>& g){ up[u][0]=p; for(int k=1;k<=K;++k) up[u][k]= up[u][k-1]<0?-1: up[up[u][k-1]][k-1];
    for(int v:g[u]) if(v!=p){ depth[v]=depth[u]+1; dfsLift(v,u,g);} }
int lift(int u,int k){ for(int i=0;i<=K;++i) if(k&(1<<i)) u = (u<0)?-1: up[u][i]; return u; }
int lca(int a,int b){ if(depth[a]<depth[b]) swap(a,b); a=lift(a, depth[a]-depth[b]); if(a==b) return a; for(int i=K;i>=0;--i) if(up[a][i]!=up[b][i]){ a=up[a][i]; b=up[b][i]; } return up[a][0]; }
```

| ID | Title | Link |
|---|---|---|
| 236 | Lowest Common Ancestor of a Binary Tree | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ |
| 235 | Lowest Common Ancestor of a BST | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ |

## HLD (Heavy-Light Decomposition) skeleton

```cpp
const int N = 200000; vector<int> gH[N]; int szH[N], parH[N], depH[N], heavyH[N], headH[N], inH[N], curT=0;
int dfs1(int u,int p){ parH[u]=p; depH[u]=(p==-1?0:depH[p]+1); szH[u]=1; heavyH[u]=-1; int best=0; for(int v:gH[u]) if(v!=p){ int s=dfs1(v,u); szH[u]+=s; if(s>best){best=s; heavyH[u]=v;} } return szH[u]; }
void dfs2(int u,int h){ headH[u]=h; inH[u]=curT++; if(heavyH[u]!=-1){ dfs2(heavyH[u],h); for(int v:gH[u]) if(v!=parH[u] && v!=heavyH[u]) dfs2(v,v);} }
```

> Note: HLD is rarely required on LeetCode.
