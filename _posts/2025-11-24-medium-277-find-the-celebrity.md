---
layout: post
title: "[Medium] 277. Find the Celebrity"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp graph two-pointers problem-solving
permalink: /posts/2025-11-24-medium-277-find-the-celebrity/
tags: [leetcode, medium, graph, two-pointers, celebrity]
---
Suppose you are at a party with `n` people (labeled from `0` to `n - 1`) and among them, there may exist one celebrity. The definition of a celebrity is that all the other `n - 1` people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function `bool knows(a, b)` which tells you whether person `a` knows person `b`. Implement a function `int findCelebrity(n)`. There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return `-1`.

## Examples

**Example 1:**
```
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. 
graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j.
The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
```

**Example 2:**
```
Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.
```

## Constraints

- `n == graph.length == graph[i].length`
- `2 <= n <= 100`
- `graph[i][j]` is `0` or `1`.
- `graph[i][i] == 1` (everyone knows themselves)

## Thinking Process

1. **Elimination Property**: If candidate knows someone, they can't be celebrity

- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| BFS / DFS traversal | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| **Union-Find (DSU)** *(this problem)* | O(α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |

## Solution

**Time Complexity:** O(n) - makes at most 3n calls to `knows()`  
**Space Complexity:** O(1)

The key insight is to use a two-pass approach:
1. **First pass**: Find a candidate celebrity by eliminating people who cannot be the celebrity
2. **Second pass**: Verify that the candidate is indeed a celebrity

### Solution: Two-Pass with Candidate Elimination

```cpp
// Forward declaration of the knows API
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        // First pass: find candidate
        int candidate = 0;
        for (int i = 1; i < n; i++) {
            if (knows(candidate, i)) {
                candidate = i;
            }
        }
        
        // Second pass: verify candidate
        for (int i = 0; i < n; i++) {
            if (i != candidate) {
                // Celebrity should not know anyone
                if (knows(candidate, i)) {
                    return -1;
                }
                // Everyone should know the celebrity
                if (!knows(i, candidate)) {
                    return -1;
                }
            }
        }
        
        return candidate;
    }
};
```

### Solution Explanation

**Approach:** Union-Find (DSU) (this problem)

**Key idea:** 1. **Elimination Property**: If candidate knows someone, they can't be celebrity

**How the code works:**
1. **Elimination Property**: If candidate knows someone, they can't be celebrity
- Model entities as nodes and relationships as edges.
- Pick traversal (BFS/DFS) or shortest-path (Dijkstra) based on weights.
- Union-Find helps when connectivity updates are frequent.

**Walkthrough** — input `graph = [[1,1,0],[0,1,0],[1,1,1]]`, expected output `1`:

There are three persons labeled with 0, 1 and 2. 
graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j.
The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

| Approach | Time | Space | Calls to knows() | Pros | Cons |
|----------|------|-------|------------------|------|------|
| **Two-Pass** | O(n) | O(1) | ~3n | Optimal | Requires two passes |
| **Brute Force** | O(n²) | O(1) | ~n² | Simple | Inefficient |
## Algorithm Breakdown

### First Pass: Find Candidate

```cpp
int candidate = 0;
for (int i = 1; i < n; i++) {
    if (knows(candidate, i)) {
        candidate = i;
    }
}
```

**Why:**
- Start with person 0 as candidate
- If candidate knows person `i`, candidate cannot be celebrity
- Update candidate to `i` (who might be celebrity)
- After loop, candidate is the only possible celebrity

**Invariant:** After processing person `i`, candidate doesn't know anyone from `i+1` to `n-1`.

### Second Pass: Verify Candidate

```cpp
for (int i = 0; i < n; i++) {
    if (i != candidate) {
        if (knows(candidate, i)) return -1;  // Celebrity knows someone
        if (!knows(i, candidate)) return -1;   // Someone doesn't know celebrity
    }
}
```

**Why:**
- Check celebrity doesn't know anyone (except themselves)
- Check everyone knows the celebrity
- If either fails, return -1 (no celebrity)

### Complexity
| Approach | Time | Space | Calls to knows() | Pros | Cons |
|----------|------|-------|------------------|------|------|
| **Two-Pass** | O(n) | O(1) | ~3n | Optimal | Requires two passes |
| **Brute Force** | O(n²) | O(1) | ~n² | Simple | Inefficient |

## Implementation Details

### Why First Pass Works

**Key Observation:**
- If `knows(candidate, i)` is true, candidate cannot be celebrity
- But `i` might be celebrity (we don't know if `i` knows others yet)
- We can safely eliminate candidate and try `i`

**Invariant Maintenance:**
After processing person `i`:
- Candidate doesn't know anyone from `i+1` to `n-1`
- All people before candidate have been eliminated

### Why Verification is Necessary

**Example where first pass finds wrong candidate:**
```
Graph:
    0  1  2
0 [ 1  1  0 ]
1 [ 0  1  0 ]
2 [ 0  0  1 ]

First Pass:
- candidate = 0
- knows(0, 1) = true → candidate = 1
- knows(1, 2) = false → candidate = 1

But person 1 knows person 0! So verification fails.
Actually, there's no celebrity in this graph.
```

### Optimization: Early Termination

The current solution can be slightly optimized:

```cpp
int findCelebrity(int n) {
    int candidate = 0;
    
    // First pass: find candidate
    for (int i = 1; i < n; i++) {
        if (knows(candidate, i)) {
            candidate = i;
        }
    }
    
    // Verify: celebrity doesn't know anyone
    for (int i = 0; i < n; i++) {
        if (i != candidate && knows(candidate, i)) {
            return -1;
        }
    }
    
    // Verify: everyone knows celebrity
    for (int i = 0; i < n; i++) {
        if (i != candidate && !knows(i, candidate)) {
            return -1;
        }
    }
    
    return candidate;
}
```

**Why:** Separating verification into two loops allows early termination.

## Common Mistakes

1. **No celebrity**: Return -1 after verification fails
2. **Celebrity is person 0**: First pass keeps candidate = 0
3. **Celebrity is last person**: First pass updates to last person
4. **Everyone knows everyone**: No celebrity (candidate knows someone)
5. **Nobody knows anyone**: No celebrity (nobody knows candidate)

1. **Skipping verification**: Must verify candidate meets both conditions
2. **Wrong elimination logic**: Must check `knows(candidate, i)`, not `knows(i, candidate)`
3. **Not handling self-loops**: `knows(i, i)` is always true (everyone knows themselves)
4. **Assuming candidate exists**: Must return -1 if verification fails
5. **Incorrect loop bounds**: Must check all `n` people in verification

## Optimization Tips

1. **Two-pass approach**: Optimal O(n) solution
2. **Early termination**: Can return -1 as soon as verification fails
3. **Single candidate**: Only need to verify one person after first pass

## Related Problems

- [997. Find the Town Judge](https://www.leetcode.com/problems/find-the-town-judge/) - Similar concept with trust relationships
- [277. Find the Celebrity](https://www.leetcode.com/problems/find-the-celebrity/) - This problem
- Graph problems with in-degree/out-degree concepts

## Real-World Applications

1. **Social Networks**: Finding influential people
2. **Recommendation Systems**: Identifying key nodes
3. **Graph Analysis**: Finding nodes with specific properties
4. **Network Topology**: Identifying central nodes

## Pattern Recognition

This problem demonstrates the **"Candidate Elimination"** pattern:

```
1. Start with a candidate
2. Use elimination property to narrow down candidates
3. Verify final candidate meets all conditions
4. Return result or indicate no solution
```

Similar problems:
- Finding majority element
- Finding unique elements
- Graph problems with special node properties

## Why Two-Pass Works

**First Pass Guarantee:**
- After first pass, candidate is the only person who could be celebrity
- All others have been eliminated (they know someone after them)

**Why Only One Candidate:**
- If two people could be celebrities:
  - Person A doesn't know person B → A could be celebrity
  - Person B doesn't know person A → B could be celebrity
  - But then A doesn't know B AND B doesn't know A
  - This violates the condition that everyone knows the celebrity
- Therefore, at most one candidate remains

**Verification Necessity:**
- First pass only checks one direction (candidate doesn't know others)
- Must verify other direction (everyone knows candidate)
- Must verify candidate doesn't know anyone before them

## Step-by-Step Trace: `n = 4`, Celebrity is person 2

```
Graph:
    0  1  2  3
0 [ 1  1  1  0 ]
1 [ 0  1  1  0 ]
2 [ 0  0  1  0 ]
3 [ 1  1  1  1 ]

First Pass:
- candidate = 0
- i = 1: knows(0, 1) = true → candidate = 1
- i = 2: knows(1, 2) = true → candidate = 2
- i = 3: knows(2, 3) = false → candidate = 2
- Candidate: 2

Second Pass:
- i = 0: knows(2, 0) = false ✓, knows(0, 2) = true ✓
- i = 1: knows(2, 1) = false ✓, knows(1, 2) = true ✓
- i = 3: knows(2, 3) = false ✓, knows(3, 2) = true ✓
- Verification passed: return 2
```

## Mathematical Insight

**Graph Theory Perspective:**
- Celebrity has **in-degree** = n-1 (everyone knows them)
- Celebrity has **out-degree** = 0 (knows nobody, except self)
- In a directed graph, at most one such node can exist

**Why:**
- If two nodes have out-degree 0, they don't know each other
- But celebrity must be known by everyone
- Contradiction → at most one celebrity

## Key Takeaways

1. **Elimination Property**: If candidate knows someone, they can't be celebrity
2. **Single Candidate**: After first pass, at most one candidate remains
3. **Verification Needed**: Must verify candidate meets both celebrity conditions
4. **Efficient**: Only O(n) calls to `knows()` instead of O(n²)

## References

- [LC 277: Find the Celebrity on LeetCode](https://www.leetcode.com/problems/find-the-celebrity/)
- [LeetCode Discuss — LC 277: Find the Celebrity](https://www.leetcode.com/problems/find-the-celebrity/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/find-the-celebrity/editorial/) *(may require premium)*

## Template Reference

- [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/)
