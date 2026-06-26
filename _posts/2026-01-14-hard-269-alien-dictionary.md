---
layout: post
title: "[Hard] 269. Alien Dictionary"
date: 2026-01-14 00:00:00 -0700
categories: [leetcode, hard, graph, topological-sort, string]
permalink: /2026/01/14/hard-269-alien-dictionary/
tags: [leetcode, hard, graph, topological-sort, string, bfs, kahn]
---
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

## Thinking Process

1. **Graph Construction**: Compare adjacent words to extract ordering constraints

- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Queue BFS** *(this problem)* | $O(n)$ | $O(n)$ | Shortest path in unweighted graphs |
| Multi-source BFS | $O(n)$ | $O(n)$ | Start from all sources simultaneously |
| 0-1 BFS / deque | $O(n)$ | $O(n)$ | Weights 0 or 1 |
| Level-order BFS | $O(n)$ | $O(w)$ | Process by depth/layer |

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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** 1. **Graph Construction**: Compare adjacent words to extract ordering constraints

**How the code works:**
1. **Graph Construction**: Compare adjacent words to extract ordering constraints
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `words = ["wrt","wrf","er","ett","rftt"]`, expected output `"wertf"`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

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
## Common Mistakes

1. **Single word**: `words = ["abc"]` → return "abc" (any order)
2. **Invalid prefix**: `words = ["abc", "ab"]` → return "" (invalid)
3. **Cycle**: `words = ["a", "b", "a"]` → return "" (cycle)
4. **No constraints**: `words = ["a", "b"]` → return "ab" or "ba" (both valid)
5. **All same prefix**: `words = ["ab", "ac", "ad"]` → extract ordering from first difference

1. **Not checking invalid prefix**: Forgetting to check if longer word comes before shorter
2. **Duplicate edges**: Not checking if edge already exists before adding
3. **Missing characters**: Not initializing all characters in adjacency list
4. **Wrong indegree calculation**: Incrementing indegree for wrong character
5. **Not validating result**: Not checking if all characters were processed

## Related Problems

- [LC 207: Course Schedule](https://www.leetcode.com/problems/course-schedule/) - Topological sort to detect cycles
- [LC 210: Course Schedule II](https://www.leetcode.com/problems/course-schedule-ii/) - Topological sort to find ordering
- [LC 269: Alien Dictionary](https://www.leetcode.com/problems/alien-dictionary/) - This problem
- [LC 444: Sequence Reconstruction](https://www.leetcode.com/problems/sequence-reconstruction/) - Verify unique topological order

## Key Takeaways

1. **Graph Construction**: Compare adjacent words to extract ordering constraints
2. **First Difference Rule**: Only the first differing character gives ordering information
3. **Invalid Prefix**: Longer word cannot come before shorter word with same prefix
4. **Topological Sort**: Use BFS (Kahn's algorithm) to find valid ordering
5. **Cycle Detection**: If not all nodes processed, cycle exists (invalid order)

## References

- [LC 269: Alien Dictionary on LeetCode](https://www.leetcode.com/problems/alien-dictionary/)
- [LeetCode Discuss — LC 269: Alien Dictionary](https://www.leetcode.com/problems/alien-dictionary/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/alien-dictionary/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
