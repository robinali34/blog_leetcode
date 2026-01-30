---
layout: post
title: "269. Alien Dictionary"
date: 2026-01-14 00:00:00 -0700
categories: [leetcode, hard, graph, topological-sort, string]
permalink: /2026/01/14/hard-269-alien-dictionary/
tags: [leetcode, hard, graph, topological-sort, string, bfs, kahn]
---

# 269. Alien Dictionary

## Problem Statement

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings are **sorted lexicographically** by the rules of this new language.

Return *a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules*. If there is no solution, return `""`. If there are multiple solutions, return **any of them**.

## Examples

**Example 1:**
```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

**Example 2:**
```
Input: words = ["z","x"]
Output: "zx"
```

**Example 3:**
```
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Ordering inference**: How do we infer character order from words? (Assumption: Compare adjacent words - first differing character gives ordering constraint)

2. **Invalid ordering**: What makes an ordering invalid? (Assumption: If there's a cycle in the ordering constraints - circular dependency)

3. **Missing characters**: What if some characters don't appear in any word? (Assumption: Need to clarify - typically all characters appear, but should confirm)

4. **Prefix handling**: How should we handle words where one is prefix of another? (Assumption: If word1 is prefix of word2, word1 should come first - but this might indicate invalid input)

5. **Return format**: What should we return if ordering is invalid? (Assumption: Return empty string "" - no valid ordering exists)

## Interview Deduction Process (30 minutes)

### Step 1: Brute-Force Approach (8 minutes)
**Initial Thought**: "I need to find character ordering. Let me try all possible orderings and check if they're valid."

**Naive Solution**: Generate all possible character orderings (permutations), check if each satisfies the word order constraints.

**Complexity**: O(26! × n × m) time, O(26) space

**Issues**:
- Factorial time complexity - completely infeasible
- Checks many invalid orderings
- Very inefficient
- Doesn't leverage graph structure

### Step 2: Semi-Optimized Approach (10 minutes)
**Insight**: "This is a topological sort problem. Build a graph from word comparisons, then do topological sort."

**Improved Solution**: Build directed graph: compare adjacent words to find first differing characters, add edge. Then perform topological sort using DFS or Kahn's algorithm.

**Complexity**: O(n × m + V + E) time where V = unique chars, E = edges, O(V + E) space

**Improvements**:
- Graph-based approach is correct
- Topological sort finds valid ordering
- Much more efficient than brute-force
- Handles cycles (invalid ordering) naturally

### Step 3: Optimized Solution (12 minutes)
**Final Optimization**: "Topological sort with cycle detection. Use Kahn's algorithm or DFS with cycle detection."

**Best Solution**: Build graph from word comparisons. Use Kahn's algorithm (BFS-based) or DFS with cycle detection for topological sort. Return empty string if cycle detected or result size < V.

**Complexity**: O(n × m + V + E) time, O(V + E) space

**Key Realizations**:
1. This is a topological sort problem
2. Graph building from word comparisons is key
3. Cycle detection indicates invalid ordering
4. Kahn's algorithm or DFS both work well

## Solution Approach

This problem requires finding the lexicographic order of characters in an alien language. The key insight is that the sorted word list gives us **ordering constraints** between characters, which we can model as a **directed graph** and solve using **topological sort**.

### Key Insights:

1. **Graph Construction**: Compare adjacent words to find character ordering relationships
2. **Edge Creation**: If `words[i][j] != words[i+1][j]`, then `words[i][j]` comes before `words[i+1][j]`
3. **Invalid Order Detection**: If `words[i]` is a prefix of `words[i+1]` and `words[i].size() > words[i+1].size()`, order is invalid
4. **Topological Sort**: Use BFS (Kahn's algorithm) to find valid ordering
5. **Cycle Detection**: If not all nodes are processed, there's a cycle (invalid order)

### Algorithm:

1. **Build Graph**: 
   - Initialize adjacency list for all characters
   - Compare adjacent words to find ordering relationships
   - Create edges: `adj[w1[j]] → w2[j]` when first differing character found
2. **Calculate Indegrees**: Count incoming edges for each character
3. **Topological Sort (BFS)**:
   - Start with characters having `indegree = 0`
   - Process each character, reduce indegrees of neighbors
   - Add to result when indegree becomes 0
4. **Validation**: If result size equals number of unique characters, return result; otherwise return `""`

## Solution

### **Solution: Topological Sort with BFS (Kahn's Algorithm)**

```cpp
class Solution {
public:
    string alienOrder(vector<string>& words) {
        const int N = words.size();
        if(N == 0) return "";
        
        // Build adj list for graph
        unordered_map<char, unordered_set<char>> adj;
        for(const string& word: words) {
            for(char c: word) {
                adj[c];
            }
        }

        vector<int> inDegree(26, 0);
        // Compare adj list to find order
        for(int i = 0; i < N - 1; i++) {
            string& w1 = words[i];
            string& w2 = words[i + 1];
            int minLen = min(w1.size(), w2.size());
            for(int j = 0; j < minLen; j++) {
                if(w1[j] != w2[j]) {
                    if(!adj[w1[j]].contains(w2[j])) {
                        adj[w1[j]].insert(w2[j]);
                        inDegree[w2[j] - 'a']++;
                    }
                    break;
                }
                if(j == minLen - 1 && w1.size() > w2.size()) {
                    return "";
                }
            }
        }

        // BFS Topological Sort
        queue<char> q;
        for(auto& [c, _]: adj) {
            if(inDegree[c - 'a'] == 0) {
                q.push(c);
            }
        }
        string rtn;
        while(!q.empty()) {
            char top = q.front();
            q.pop();
            rtn.push_back(top);
            for(char success: adj[top]) {
                inDegree[success - 'a']--;
                if(inDegree[success - 'a'] == 0) {
                    q.push(success);
                }
            }
        }

        // Check if all nodes were output (DAG check)
        if(rtn.size() == adj.size()) {
            return rtn;
        }
        return "";
    }
};
```

### **Algorithm Explanation:**

1. **Graph Initialization (Lines 7-13)**:
   - Create adjacency list `adj` for all characters
   - Initialize all characters from words (even if no edges)

2. **Build Graph from Word Comparisons (Lines 15-30)**:
   - **Compare adjacent words** `words[i]` and `words[i+1]`
   - **Find first differing character** at position `j`
   - **Create edge**: `adj[w1[j]] → w2[j]` (w1[j] comes before w2[j])
   - **Increment indegree**: `inDegree[w2[j] - 'a']++`
   - **Invalid order check**: If `w1` is prefix of `w2` but `w1.size() > w2.size()`, return `""`
   - **Break after first difference**: Only first differing character gives ordering

3. **Topological Sort (BFS) (Lines 32-45)**:
   - **Find sources**: Characters with `inDegree = 0` (no prerequisites)
   - **Process queue**: 
     - Remove character from queue
     - Add to result
     - Reduce indegrees of all neighbors
     - Add neighbors to queue if indegree becomes 0

4. **Validation (Lines 47-51)**:
   - **Check completeness**: If `rtn.size() == adj.size()`, all characters processed (valid DAG)
   - **Otherwise**: Cycle exists or invalid order → return `""`

### **Why This Works:**

- **Graph Model**: Characters are nodes, ordering relationships are directed edges
- **Topological Sort**: Finds valid ordering that respects all constraints
- **Cycle Detection**: If not all nodes processed, there's a cycle (contradictory orderings)
- **Invalid Prefix**: If longer word comes before shorter word with same prefix, order is invalid

### **Example Walkthrough:**

**Input:** `words = ["wrt","wrf","er","ett","rftt"]`

```
Step 1: Build Graph

Compare "wrt" and "wrf":
  First difference at index 2: 't' != 'f'
  Edge: t → f
  inDegree['f'] = 1

Compare "wrf" and "er":
  First difference at index 0: 'w' != 'e'
  Edge: w → e
  inDegree['e'] = 1

Compare "er" and "ett":
  First difference at index 1: 'r' != 't'
  Edge: r → t
  inDegree['t'] = 1

Compare "ett" and "rftt":
  First difference at index 0: 'e' != 'r'
  Edge: e → r
  inDegree['r'] = 1

Graph:
  w → e → r → t → f
  t → f

Indegrees:
  w: 0, e: 1, r: 1, t: 1, f: 2

Step 2: Topological Sort

Initial queue: [w] (indegree = 0)

Process 'w':
  rtn = "w"
  Neighbors: [e]
  inDegree['e'] = 0 → add 'e' to queue
  Queue: [e]

Process 'e':
  rtn = "we"
  Neighbors: [r]
  inDegree['r'] = 0 → add 'r' to queue
  Queue: [r]

Process 'r':
  rtn = "wer"
  Neighbors: [t]
  inDegree['t'] = 0 → add 't' to queue
  Queue: [t]

Process 't':
  rtn = "wert"
  Neighbors: [f]
  inDegree['f'] = 1 → not ready
  Queue: []

Wait, we need to check all characters. Let me recalculate:

Actually, after processing 't':
  inDegree['f'] = 2 - 1 = 1 (still not 0)
  
But we've processed all nodes with indegree 0. Let me check the graph again.

Actually, the issue is that 'f' has indegree 2 (from 't' and from the first comparison).
After processing 't', inDegree['f'] becomes 1, not 0.

Let me trace more carefully:
- w → e (inDegree['e'] = 1)
- e → r (inDegree['r'] = 1)  
- r → t (inDegree['t'] = 1)
- t → f (inDegree['f'] = 1, but we also have t → f from first comparison)

Wait, the code checks `!adj[w1[j]].contains(w2[j])` to avoid duplicate edges.
So if we already have t → f, we don't add it again.

Let me recalculate:
- "wrt" vs "wrf": t → f, inDegree['f'] = 1
- "wrf" vs "er": w → e, inDegree['e'] = 1
- "er" vs "ett": r → t, inDegree['t'] = 1
- "ett" vs "rftt": e → r, inDegree['r'] = 1

So:
- w: indegree 0
- e: indegree 1 (from w)
- r: indegree 1 (from e)
- t: indegree 1 (from r)
- f: indegree 1 (from t)

Processing:
1. Process w → e indegree becomes 0
2. Process e → r indegree becomes 0
3. Process r → t indegree becomes 0
4. Process t → f indegree becomes 0
5. Process f

Result: "wertf" ✓
```

### **Complexity Analysis:**

- **Time Complexity:** O(C + E) where C is number of unique characters, E is number of edges
  - Building graph: O(N × L) where N is number of words, L is average word length
  - Topological sort: O(C + E)
  - Overall: O(N × L + C + E) = O(N × L) since E ≤ C²
- **Space Complexity:** O(C + E)
  - Adjacency list: O(C + E)
  - Indegree array: O(C)
  - Queue: O(C)

## Key Insights

1. **Graph Construction**: Compare adjacent words to extract ordering constraints
2. **First Difference Rule**: Only the first differing character gives ordering information
3. **Invalid Prefix**: Longer word cannot come before shorter word with same prefix
4. **Topological Sort**: Use BFS (Kahn's algorithm) to find valid ordering
5. **Cycle Detection**: If not all nodes processed, cycle exists (invalid order)

## Edge Cases

1. **Single word**: `words = ["abc"]` → return "abc" (any order)
2. **Invalid prefix**: `words = ["abc", "ab"]` → return "" (invalid)
3. **Cycle**: `words = ["a", "b", "a"]` → return "" (cycle)
4. **No constraints**: `words = ["a", "b"]` → return "ab" or "ba" (both valid)
5. **All same prefix**: `words = ["ab", "ac", "ad"]` → extract ordering from first difference

## Common Mistakes

1. **Not checking invalid prefix**: Forgetting to check if longer word comes before shorter
2. **Duplicate edges**: Not checking if edge already exists before adding
3. **Missing characters**: Not initializing all characters in adjacency list
4. **Wrong indegree calculation**: Incrementing indegree for wrong character
5. **Not validating result**: Not checking if all characters were processed

## Alternative Approaches

### **Approach 2: DFS Topological Sort**

```cpp
class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, unordered_set<char>> adj;
        unordered_map<char, int> state; // 0: unvisited, 1: visiting, 2: visited
        
        // Initialize all characters
        for(const string& word: words) {
            for(char c: word) {
                adj[c];
                state[c] = 0;
            }
        }
        
        // Build graph
        for(int i = 0; i < words.size() - 1; i++) {
            string& w1 = words[i];
            string& w2 = words[i + 1];
            int minLen = min(w1.size(), w2.size());
            bool found = false;
            for(int j = 0; j < minLen; j++) {
                if(w1[j] != w2[j]) {
                    adj[w1[j]].insert(w2[j]);
                    found = true;
                    break;
                }
            }
            if(!found && w1.size() > w2.size()) {
                return "";
            }
        }
        
        string result;
        for(auto& [c, _]: adj) {
            if(state[c] == 0 && hasCycle(c, adj, state, result)) {
                return "";
            }
        }
        
        reverse(result.begin(), result.end());
        return result;
    }
    
private:
    bool hasCycle(char c, unordered_map<char, unordered_set<char>>& adj, 
                  unordered_map<char, int>& state, string& result) {
        if(state[c] == 1) return true; // Cycle detected
        if(state[c] == 2) return false; // Already processed
        
        state[c] = 1; // Mark as visiting
        for(char neighbor: adj[c]) {
            if(hasCycle(neighbor, adj, state, result)) {
                return true;
            }
        }
        state[c] = 2; // Mark as visited
        result.push_back(c);
        return false;
    }
};
```

**Time Complexity:** O(C + E)  
**Space Complexity:** O(C + E)

**Comparison:**
- **BFS (Kahn's)**: More intuitive, easier to understand
- **DFS**: More compact code, but requires reversing result

## Related Problems

- [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) - Topological sort to detect cycles
- [LC 210: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Topological sort to find ordering
- [LC 269: Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) - This problem
- [LC 444: Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/) - Verify unique topological order

---

*This problem demonstrates **Topological Sort** for finding valid ordering that satisfies all constraints. The key is modeling character ordering relationships as a directed graph and using BFS (Kahn's algorithm) to find a valid topological ordering.*

