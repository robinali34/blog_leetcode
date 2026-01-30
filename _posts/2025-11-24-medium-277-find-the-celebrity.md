---
layout: post
title: "[Medium] 277. Find the Celebrity"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp graph two-pointers problem-solving
permalink: /posts/2025-11-24-medium-277-find-the-celebrity/
tags: [leetcode, medium, graph, two-pointers, celebrity]
---

# [Medium] 277. Find the Celebrity

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Celebrity definition**: What is a celebrity? (Assumption: Person who knows nobody (except themselves) but is known by everyone)

2. **Knows function**: What does knows(a, b) return? (Assumption: graph[a][b] = 1 means a knows b, 0 means a doesn't know b)

3. **Return value**: What should we return? (Assumption: Integer - celebrity's index if exists, -1 if no celebrity)

4. **Uniqueness**: Can there be multiple celebrities? (Assumption: No - at most one celebrity can exist)

5. **Self-knowledge**: Does everyone know themselves? (Assumption: Yes - graph[i][i] = 1 per constraints)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For each person i, check if they are a celebrity: verify that knows(i, j) is false for all j != i, and knows(j, i) is true for all j != i. This requires O(n²) calls to the knows() function, which is inefficient. The challenge is that we need to check all pairs of relationships.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use the fact that if knows(a, b) is true, then a cannot be a celebrity (they know someone). If knows(a, b) is false, then b cannot be a celebrity (not known by a). Use this to eliminate candidates: start with candidate 0, and for each person i, if knows(candidate, i), then candidate cannot be celebrity, so set candidate = i. After one pass, we have a potential celebrity candidate.

**Step 3: Optimized Solution (8 minutes)**

Use a two-pass algorithm: First pass finds a candidate by elimination. Start with candidate = 0. For each person i from 1 to n-1, if knows(candidate, i), then candidate cannot be celebrity (knows someone), so set candidate = i. Second pass verifies the candidate: check that candidate doesn't know anyone (except themselves) and everyone knows the candidate. This achieves O(n) calls to knows() function, which is optimal. The key insight is that the elimination property allows us to find the only possible candidate in one pass, then verify in a second pass.

## Solution: Two-Pass Algorithm

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

## How the Algorithm Works

### Key Insight: Candidate Elimination

**Celebrity Properties:**
- Celebrity knows **nobody** (except themselves)
- **Everyone** knows the celebrity

**Elimination Logic:**
- If `knows(candidate, i)` is true → candidate cannot be celebrity (knows someone)
- Therefore, `i` becomes the new candidate
- After first pass, candidate is the only person who could be celebrity

### Step-by-Step Example: `n = 3`, Celebrity is person 1

```
Graph:
    0  1  2
0 [ 1  1  0 ]
1 [ 0  1  0 ]
2 [ 1  1  1 ]

First Pass (Find Candidate):
- candidate = 0
- i = 1: knows(0, 1) = true → candidate = 1
- i = 2: knows(1, 2) = false → candidate stays 1
- Candidate found: 1

Second Pass (Verify):
- i = 0: 
  - knows(1, 0) = false ✓ (celebrity doesn't know 0)
  - knows(0, 1) = true ✓ (0 knows celebrity)
- i = 2:
  - knows(1, 2) = false ✓ (celebrity doesn't know 2)
  - knows(2, 1) = true ✓ (2 knows celebrity)
- Verification passed: return 1
```

**Visual Representation:**
```
Party:
  0 ──knows──> 1 <──knows── 2
  │            │             │
  └────────────┴─────────────┘
            (celebrity)

First Pass:
- Start with candidate = 0
- knows(0, 1) = true → eliminate 0, candidate = 1
- knows(1, 2) = false → keep candidate = 1

Second Pass:
- Verify 1 doesn't know anyone: ✓
- Verify everyone knows 1: ✓
- Return 1
```

## Key Insights

1. **Elimination Property**: If candidate knows someone, they can't be celebrity
2. **Single Candidate**: After first pass, at most one candidate remains
3. **Verification Needed**: Must verify candidate meets both celebrity conditions
4. **Efficient**: Only O(n) calls to `knows()` instead of O(n²)

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

## Edge Cases

1. **No celebrity**: Return -1 after verification fails
2. **Celebrity is person 0**: First pass keeps candidate = 0
3. **Celebrity is last person**: First pass updates to last person
4. **Everyone knows everyone**: No celebrity (candidate knows someone)
5. **Nobody knows anyone**: No celebrity (nobody knows candidate)

## Alternative Approaches

### Approach 2: Brute Force (O(n²))

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

```cpp
class Solution {
public:
    int findCelebrity(int n) {
        for (int i = 0; i < n; i++) {
            bool isCelebrity = true;
            
            // Check if i knows anyone
            for (int j = 0; j < n; j++) {
                if (i != j && knows(i, j)) {
                    isCelebrity = false;
                    break;
                }
            }
            
            if (!isCelebrity) continue;
            
            // Check if everyone knows i
            for (int j = 0; j < n; j++) {
                if (i != j && !knows(j, i)) {
                    isCelebrity = false;
                    break;
                }
            }
            
            if (isCelebrity) return i;
        }
        
        return -1;
    }
};
```

**Pros:**
- Simple and straightforward
- Easy to understand

**Cons:**
- O(n²) calls to `knows()` - inefficient
- Doesn't leverage elimination property

## Complexity Analysis

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

- [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) - Similar concept with trust relationships
- [277. Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) - This problem
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

---

*This problem demonstrates how to efficiently find a special node in a graph using candidate elimination and verification, achieving optimal O(n) time complexity.*

