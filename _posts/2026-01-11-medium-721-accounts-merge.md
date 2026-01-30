---
layout: post
title: "721. Accounts Merge"
date: 2026-01-11 00:00:00 -0700
categories: [leetcode, medium, array, hash-table, string, union-find, dfs]
permalink: /2026/01/11/medium-721-accounts-merge/
tags: [leetcode, medium, array, hash-table, string, union-find, disjoint-set, dfs]
---

# 721. Accounts Merge

## Problem Statement

Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are **emails** representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in **any order**.

## Examples

**Example 1:**
```
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's accounts are merged because they share the email "johnsmith@mail.com".
The third John's account is not merged because it doesn't share any email with the other accounts.
```

**Example 2:**
```
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
```

## Constraints

- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- `1 <= accounts[i][0].length <= 10`
- `accounts[i][j]` for `j > 0` is a valid email.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Merging rule**: When should accounts be merged? (Assumption: Two accounts belong to the same person if they share at least one common email)

2. **Name handling**: What if accounts have different names but share emails? (Assumption: If emails match, they're the same person - use the name from first account or clarify)

3. **Email uniqueness**: Can the same email appear in multiple accounts? (Assumption: Yes - that's how we identify accounts to merge)

4. **Output format**: How should merged accounts be formatted? (Assumption: List with name first, then sorted unique emails)

5. **Transitive merging**: If A shares email with B, and B shares email with C, should A, B, C all be merged? (Assumption: Yes - transitive closure - use Union-Find to handle this)

## Solution Approach

This is a **Union-Find (Disjoint Set Union)** problem. The key insight is that emails belonging to the same account should be grouped together, and if two accounts share any email, they should be merged.

### Key Insights:

1. **Email as Identifier**: Use emails as unique identifiers (not names, since names can be duplicated)
2. **Union-Find**: Group emails that belong to the same account using Union-Find
3. **Email Mapping**: Map each email to a unique index and to its owner's name
4. **Grouping**: After union operations, group emails by their root parent
5. **Sorting**: Sort emails within each merged account

### Algorithm:

1. **Assign IDs**: Map each unique email to a unique index
2. **Union Emails**: For each account, union all emails in that account
3. **Group by Root**: Group emails by their root parent (connected component)
4. **Build Result**: For each group, create an account with name and sorted emails

## Solution

### **Solution: Union-Find (Disjoint Set Union)**

```cpp
class UnionFind {
public:
    UnionFind(int n) {
        parent.resize(n);
        for(int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    void unionSet(int idx1, int idx2) {
        parent[find(idx2)] = find(idx1);
    }

    int find(int idx) {
        if(parent[idx] != idx) {
            parent[idx] = find(parent[idx]);
        }
        return parent[idx];
    }

private:
    vector<int> parent;
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, int> emailToIdx;
        unordered_map<string, string> emailToName;

        // 1: Assign an ID to each unique email
        int id = 0;
        for(auto& account: accounts) {
            string& name = account[0];
            int size = account.size();
            for(int i = 1; i < size; i++) {
                string& email = account[i];
                if(!emailToIdx.contains(email)) {
                    emailToIdx[email] = id++;
                    emailToName[email] = name;
                }
            }
        }

        // 2: Union emails belonging to the same account
        UnionFind uf(id);
        for(auto& account: accounts) {
            string& firstEmail = account[1];
            int firstIdx = emailToIdx[firstEmail];
            int size = account.size();
            for(int i = 2; i < size; i++) {
                string& nextEmail = account[i];
                int nextIndex = emailToIdx[nextEmail];
                uf.unionSet(firstIdx, nextIndex);
            }
        }

        // 3: Group emails by their root parent        
        unordered_map<int, vector<string>> idxToEmails;
        for(auto& [email, _]: emailToIdx) {
            int idx = uf.find(emailToIdx[email]);
            vector<string>& account = idxToEmails[idx];;
            account.emplace_back(email);
            idxToEmails[idx] = account;
        }

        // 4: Build the merged account list
        vector<vector<string>> merged;
        for(auto& [_, emails]: idxToEmails) {
            sort(emails.begin(), emails.end());
            string& name = emailToName[emails[0]];
            vector<string> account;
            account.emplace_back(name);
            for(auto& email:emails) {
                account.emplace_back(email);
            }
            merged.emplace_back(account);
        }
        return merged;
    }
};
```

### **Algorithm Explanation:**

1. **Union-Find Class (Lines 1-23)**:
   - **Constructor**: Initialize `parent` array where each element is its own parent
   - **`unionSet`**: Union two sets by making `idx2`'s root point to `idx1`'s root
   - **`find`**: Find root with path compression (flattens the tree for efficiency)

2. **Step 1: Assign IDs (Lines 30-41)**:
   - Iterate through all accounts
   - For each email in an account:
     - If email not seen before, assign a unique `id` and map to name
     - Store mappings: `emailToIdx[email] = id` and `emailToName[email] = name`

3. **Step 2: Union Emails (Lines 43-53)**:
   - For each account, union all emails in that account
   - Strategy: Union all emails to the first email in the account
   - This groups all emails from the same account together

4. **Step 3: Group by Root (Lines 55-61)**:
   - For each email, find its root parent using `uf.find()`
   - Group emails by their root parent in `idxToEmails`
   - Emails with the same root belong to the same merged account

5. **Step 4: Build Result (Lines 63-73)**:
   - For each group of emails:
     - Sort emails alphabetically
     - Get the name from the first email (all emails in group have same name)
     - Create account: `[name, email1, email2, ...]`
     - Add to result

### **Why This Works:**

- **Union-Find Groups**: Emails in the same account are unioned, so they share the same root
- **Transitive Merging**: If account A shares email with B, and B shares with C, then A, B, C are all merged (transitive property)
- **Path Compression**: Makes `find` operations efficient (nearly O(1) amortized)
- **Email as Key**: Using emails (not names) correctly handles duplicate names

### **Example Walkthrough:**

**For `accounts = [["John","a@mail.com","b@mail.com"],["John","a@mail.com","c@mail.com"],["Mary","d@mail.com"]]`:**

```
Step 1: Assign IDs
emailToIdx: {
    "a@mail.com": 0,
    "b@mail.com": 1,
    "c@mail.com": 2,
    "d@mail.com": 3
}
emailToName: {
    "a@mail.com": "John",
    "b@mail.com": "John",
    "c@mail.com": "John",
    "d@mail.com": "Mary"
}

Step 2: Union emails
Account 1: ["John","a@mail.com","b@mail.com"]
  - Union(0, 1): parent[1] = 0
  - parent = [0, 0, 2, 3]

Account 2: ["John","a@mail.com","c@mail.com"]
  - Union(0, 2): parent[2] = 0
  - parent = [0, 0, 0, 3]

Account 3: ["Mary","d@mail.com"]
  - No union needed (only one email)
  - parent = [0, 0, 0, 3]

Step 3: Group by root
idxToEmails: {
    0: ["a@mail.com", "b@mail.com", "c@mail.com"],
    3: ["d@mail.com"]
}

Step 4: Build result
Group 0: 
  - Sort: ["a@mail.com", "b@mail.com", "c@mail.com"]
  - Name: "John"
  - Account: ["John", "a@mail.com", "b@mail.com", "c@mail.com"]

Group 3:
  - Sort: ["d@mail.com"]
  - Name: "Mary"
  - Account: ["Mary", "d@mail.com"]

Result: [
    ["John", "a@mail.com", "b@mail.com", "c@mail.com"],
    ["Mary", "d@mail.com"]
]
```

### **Complexity Analysis:**

- **Time Complexity:** O(n × k × α(n × k) + n × k × log(n × k))
  - `n` = number of accounts, `k` = average emails per account
  - O(n × k) for assigning IDs
  - O(n × k × α(n × k)) for union operations (α is inverse Ackermann, nearly constant)
  - O(n × k × log(n × k)) for sorting emails in each group
  - Total: O(n × k × log(n × k)) dominated by sorting
- **Space Complexity:** O(n × k)
  - `emailToIdx`: O(n × k) for all emails
  - `emailToName`: O(n × k) for all emails
  - `idxToEmails`: O(n × k) for grouped emails
  - `parent` array: O(n × k)

## Key Insights

1. **Email as Unique Identifier**: Names can be duplicated, but emails are unique
2. **Union-Find for Grouping**: Efficiently groups emails that belong together
3. **Transitive Merging**: If A shares email with B, and B shares with C, then A, B, C are merged
4. **Path Compression**: Critical for efficiency in Union-Find operations

## Edge Cases

1. **Single email per account**: `[["John","a@mail.com"]]` → return `[["John","a@mail.com"]]`
2. **No shared emails**: All accounts remain separate
3. **All emails shared**: All accounts merge into one
4. **Duplicate emails in same account**: Handled correctly (only assigned one ID)

## Common Mistakes

1. **Using names as keys**: Names can be duplicated, causing incorrect merging
2. **Not sorting emails**: Result must have sorted emails
3. **Wrong union logic**: Must union all emails in an account, not just pairs
4. **Missing path compression**: Without it, `find` can be O(n) instead of O(α(n))
5. **Name mismatch**: Assuming all emails in merged account have same name (they do, but need to verify)

## Alternative Approaches

### **Approach 2: DFS (Depth-First Search)**

Build a graph where emails are nodes and edges connect emails in the same account. Use DFS to find connected components.

```cpp
class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, vector<string>> graph;
        unordered_map<string, string> emailToName;
        
        // Build graph
        for(auto& account: accounts) {
            string name = account[0];
            for(int i = 1; i < account.size(); i++) {
                graph[account[1]].push_back(account[i]);
                graph[account[i]].push_back(account[1]);
                emailToName[account[i]] = name;
            }
        }
        
        // DFS to find connected components
        vector<vector<string>> result;
        unordered_set<string> visited;
        
        for(auto& [email, _]: graph) {
            if(!visited.count(email)) {
                vector<string> component;
                dfs(graph, email, visited, component);
                sort(component.begin(), component.end());
                component.insert(component.begin(), emailToName[email]);
                result.push_back(component);
            }
        }
        
        return result;
    }
    
private:
    void dfs(unordered_map<string, vector<string>>& graph, 
             string email, unordered_set<string>& visited, 
             vector<string>& component) {
        visited.insert(email);
        component.push_back(email);
        for(string& neighbor: graph[email]) {
            if(!visited.count(neighbor)) {
                dfs(graph, neighbor, visited, component);
            }
        }
    }
};
```

**Time Complexity:** O(n × k × log(n × k))  
**Space Complexity:** O(n × k)

## Related Problems

- [LC 323: Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) - Count connected components
- [LC 547: Number of Provinces](https://leetcode.com/problems/number-of-provinces/) - Similar connected components problem
- [LC 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/) - Union-Find for cycle detection
- [LC 990: Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) - Union-Find for equality constraints

---

*This problem demonstrates Union-Find for grouping related entities. The key insight is using emails (not names) as unique identifiers and leveraging Union-Find's transitive property to merge accounts that share any email.*

