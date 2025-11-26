---
layout: post
title: "LeetCode Templates: Union Find"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates union-find
permalink: /posts/2025-11-24-leetcode-templates-union-find/
tags: [leetcode, templates, union-find, dsu, graph]
---

{% raw %}
## Contents

- [Basic Union Find](#basic-union-find)
- [Union Find with Path Compression](#union-find-with-path-compression)
- [Union Find with Union by Rank](#union-find-with-union-by-rank)
- [Applications](#applications)

## Basic Union Find

Union Find (Disjoint Set Union, DSU) tracks connected components efficiently.

```cpp
class UnionFind {
    vector<int> parent;
public:
    UnionFind(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
    }
    
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};
```

## Union Find with Path Compression

Path compression optimizes find operation.

```cpp
class UnionFind {
    vector<int> parent;
public:
    UnionFind(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int x) {
        // Path compression: make parent point directly to root
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
    }
};
```

## Union Find with Union by Rank

Union by rank keeps tree balanced.

```cpp
class UnionFind {
    vector<int> parent, rank;
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px == py) return;
        
        // Union by rank: attach smaller tree to larger tree
        if (rank[px] < rank[py]) {
            parent[px] = py;
        } else if (rank[px] > rank[py]) {
            parent[py] = px;
        } else {
            parent[py] = px;
            rank[px]++;
        }
    }
    
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
    
    int countComponents() {
        unordered_set<int> roots;
        for (int i = 0; i < parent.size(); ++i) {
            roots.insert(find(i));
        }
        return roots.size();
    }
};
```

## Applications

### Number of Connected Components

```cpp
int countComponents(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    for (auto& edge : edges) {
        uf.unite(edge[0], edge[1]);
    }
    return uf.countComponents();
}
```

### Redundant Connection Detection

```cpp
vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    int n = edges.size();
    UnionFind uf(n + 1);
    
    for (auto& edge : edges) {
        if (uf.connected(edge[0], edge[1])) {
            return edge;
        }
        uf.unite(edge[0], edge[1]);
    }
    
    return {};
}
```

### Accounts Merge

```cpp
vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    int n = accounts.size();
    UnionFind uf(n);
    unordered_map<string, int> emailToAccount;
    
    // Union accounts with same email
    for (int i = 0; i < n; ++i) {
        for (int j = 1; j < accounts[i].size(); ++j) {
            string email = accounts[i][j];
            if (emailToAccount.count(email)) {
                uf.unite(i, emailToAccount[email]);
            } else {
                emailToAccount[email] = i;
            }
        }
    }
    
    // Group emails by root account
    unordered_map<int, set<string>> accountToEmails;
    for (int i = 0; i < n; ++i) {
        int root = uf.find(i);
        for (int j = 1; j < accounts[i].size(); ++j) {
            accountToEmails[root].insert(accounts[i][j]);
        }
    }
    
    // Build result
    vector<vector<string>> result;
    for (auto& [root, emails] : accountToEmails) {
        vector<string> account;
        account.push_back(accounts[root][0]);
        account.insert(account.end(), emails.begin(), emails.end());
        result.push_back(account);
    }
    
    return result;
}
```

### Satisfiability of Equality Equations

```cpp
bool equationsPossible(vector<string>& equations) {
    UnionFind uf(26);
    
    // Process == equations first
    for (string& eq : equations) {
        if (eq[1] == '=') {
            uf.unite(eq[0] - 'a', eq[3] - 'a');
        }
    }
    
    // Check != equations
    for (string& eq : equations) {
        if (eq[1] == '!') {
            if (uf.connected(eq[0] - 'a', eq[3] - 'a')) {
                return false;
            }
        }
    }
    
    return true;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 684 | Redundant Connection | [Link](https://leetcode.com/problems/redundant-connection/) | - |
| 721 | Accounts Merge | [Link](https://leetcode.com/problems/accounts-merge/) | - |
| 990 | Satisfiability of Equality Equations | [Link](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/04/medium-990-satisfiability-of-equality-equations/) |
| 1319 | Number of Operations to Make Network Connected | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | - |
| 323 | Number of Connected Components in an Undirected Graph | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | - |
{% endraw %}

