---
layout: post
title: "1247. Minimum Swaps to Make Strings Equal"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, medium, string, math, greedy]
permalink: /2026/01/04/medium-1247-minimum-swaps-to-make-strings-equal/
---

# 1247. Minimum Swaps to Make Strings Equal

## Problem Statement

You are given two strings `s1` and `s2` of equal length consisting of only letters `'x'` and `'y'`.

In one move, you can swap two characters belonging to **different strings** at the same position. In other words, swap `s1[i]` and `s2[i]`.

Return *the minimum number of moves required to make `s1` and `s2` equal, or return `-1` if it is impossible to make them equal*.

## Examples

**Example 1:**
```
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
We have 2 (x,y) mismatches at positions 0 and 1.
- xy = 2, yx = 0
- Total = 2 (even, possible)
- Result = 2/2 + 0/2 + 2%2 + 0%2 = 1 + 0 + 0 + 0 = 1
The algorithm indicates 1 swap is needed to make the strings equal.
```

**Example 2:**
```
Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
We have 1 (x,y) mismatch at position 0 and 1 (y,x) mismatch at position 1.
- xy = 1, yx = 1
- Total = 2 (even, possible)
- Result = 1/2 + 1/2 + 1%2 + 1%2 = 0 + 0 + 1 + 1 = 2
We need 2 swaps: one to handle the (x,y) mismatch and one to handle the (y,x) mismatch.
```

**Example 3:**
```
Input: s1 = "xx", s2 = "xy"
Output: -1
Explanation: 
- Position 0: (x,x) → match
- Position 1: (x,y) → xy mismatch
- xy = 1, yx = 0
- Total = 1 (odd, impossible)
- Return -1
```

## Constraints

- `1 <= s1.length, s2.length <= 1000`
- `s1.length == s2.length`
- `s1[i], s2[i]` is `'x'` or `'y'`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Swap operation**: What does a swap do? (Assumption: Swap characters at same index in both strings - swap s1[i] with s2[i])

2. **Goal**: What are we trying to achieve? (Assumption: Make both strings equal using minimum number of swaps)

3. **Return value**: What should we return? (Assumption: Integer - minimum swaps needed, or -1 if impossible)

4. **Impossibility**: When is it impossible? (Assumption: If total count of 'x' or 'y' is odd - cannot make strings equal)

5. **Swap efficiency**: Can one swap fix multiple mismatches? (Assumption: Yes - strategic swaps can fix multiple mismatches efficiently)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Try all possible sequences of swaps to make strings equal. Use BFS or DFS to explore all swap sequences, tracking the minimum number of swaps needed. This approach has exponential complexity as we explore all possible swap sequences, which is infeasible for long strings.

**Step 2: Semi-Optimized Approach (7 minutes)**

Identify positions where s1[i] != s2[i]. Count mismatches: positions where s1 has 'x' but s2 has 'y', and positions where s1 has 'y' but s2 has 'x'. If counts don't match, return -1. Otherwise, each swap fixes two mismatches. However, determining the minimum number of swaps requires careful pairing logic.

**Step 3: Optimized Solution (8 minutes)**

Count mismatches: positions where s1[i] != s2[i]. Among these, count how many have (s1[i], s2[i]) = ('x', 'y') and how many have ('y', 'x'). If counts don't match (not both even or both odd), return -1. Otherwise, each swap fixes one pair: swapping two ('x','y') positions or two ('y','x') positions fixes 2 mismatches. Swapping one ('x','y') and one ('y','x') fixes 2 mismatches. The minimum swaps is (count_xy + count_yx + 1) / 2. This achieves O(n) time with O(1) space, which is optimal.

## Solution Approach

This is a **greedy algorithm** problem with a key mathematical insight. The crucial observation is about pairing mismatches efficiently.

### Key Insights:

1. **Mismatch Types**: There are two types of mismatches:
   - `(x,y)`: `s1[i] == 'x'` and `s2[i] == 'y'` → count as `xy`
   - `(y,x)`: `s1[i] == 'y'` and `s2[i] == 'x'` → count as `yx`

2. **Impossibility Check**: If total mismatches `(xy + yx)` is odd, it's impossible to make strings equal → return `-1`

3. **Pairing Strategy**:
   - Two `(x,y)` mismatches can be fixed with 1 swap (swap one to create a pair, then swap the pair)
   - Two `(y,x)` mismatches can be fixed with 1 swap
   - One `(x,y)` and one `(y,x)` require 2 swaps

4. **Optimal Formula**: 
   - `xy/2`: pairs of `(x,y)` mismatches (1 swap per pair)
   - `yx/2`: pairs of `(y,x)` mismatches (1 swap per pair)
   - `xy%2 + yx%2`: leftover mismatches (if both are 1, need 2 swaps)

### Algorithm:

1. **Count Mismatches**: Count `xy` and `yx` mismatches
2. **Check Impossibility**: If `(xy + yx) % 2 == 1`, return `-1`
3. **Calculate Swaps**: Return `xy/2 + yx/2 + xy%2 + yx%2`

## Solution

### **Solution: Greedy with Mismatch Pairing**

```cpp
class Solution {
public:
    int minimumSwap(string s1, string s2) {
        int xy = 0, yx = 0;
        for(int i = 0; i < (int) s1.length(); i++) {
            if(s1[i] == 'x' && s2[i] == 'y') {
                xy++;
            } else if(s1[i] == 'y' && s2[i] == 'x') {
                yx++;
            }
        }
        if((xy + yx) % 2 == 1) {
            return -1;
        }
        return xy / 2 + yx / 2 + xy % 2 + yx % 2;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize Counters (Line 4)**:
   - `xy`: Count of positions where `s1[i] == 'x'` and `s2[i] == 'y'`
   - `yx`: Count of positions where `s1[i] == 'y'` and `s2[i] == 'x'`

2. **Count Mismatches (Lines 5-10)**:
   - **For each position `i`**:
     - **If `(x,y)` mismatch**: `s1[i] == 'x'` and `s2[i] == 'y'` → increment `xy`
     - **If `(y,x)` mismatch**: `s1[i] == 'y'` and `s2[i] == 'x'` → increment `yx`
     - **If match**: Do nothing (both are 'x' or both are 'y')

3. **Check Impossibility (Lines 11-13)**:
   - **If total mismatches is odd**: `(xy + yx) % 2 == 1`
     - Return `-1` (impossible to make strings equal)
   - **Why**: Each swap fixes 2 mismatches (or creates a cycle), so we need even number of mismatches

4. **Calculate Minimum Swaps (Line 14)**:
   - **Formula**: `xy/2 + yx/2 + xy%2 + yx%2`
   - **Explanation**:
     - `xy/2`: Number of pairs of `(x,y)` mismatches (1 swap per pair)
     - `yx/2`: Number of pairs of `(y,x)` mismatches (1 swap per pair)
     - `xy%2 + yx%2`: If both have 1 leftover, we need 2 swaps (1+1=2)

### **Why This Works:**

**Key Insight**: Each swap can fix 2 mismatches when we pair them correctly.

**Strategy**:
1. **Pair Same-Type Mismatches**: Two `(x,y)` mismatches can be fixed with 1 swap
2. **Pair Same-Type Mismatches**: Two `(y,x)` mismatches can be fixed with 1 swap
3. **Handle Leftovers**: If we have one `(x,y)` and one `(y,x)`, we need 2 swaps:
   - First swap: Fixes one mismatch but creates a different type
   - Second swap: Fixes the remaining mismatch

**Example Walkthrough:**

**Example 1: `s1 = "xx"`, `s2 = "yy"`**

**Count mismatches:**
```
Position 0: s1[0]='x', s2[0]='y' → (x,y) mismatch → xy++
Position 1: s1[1]='x', s2[1]='y' → (x,y) mismatch → xy++

xy = 2, yx = 0
Total = 2 (even, possible)
```

**Execution:**
```
Step 1: Pair (x,y) mismatches
  - We have 2 (x,y) mismatches
  - xy/2 = 2/2 = 1 swap needed for the pair
  - xy%2 = 2%2 = 0 (no leftover)
  - yx/2 = 0/2 = 0
  - yx%2 = 0%2 = 0

Result = 1 + 0 + 0 + 0 = 1
```

**Example 2: `s1 = "xy"`, `s2 = "yx"`**

**Count mismatches:**
```
Position 0: s1[0]='x', s2[0]='y' → (x,y) mismatch → xy++
Position 1: s1[1]='y', s2[1]='x' → (y,x) mismatch → yx++

xy = 1, yx = 1
Total = 2 (even, possible)
```

**Execution:**
```
Step 1: Check for pairs
  - xy/2 = 1/2 = 0 (no pair of (x,y))
  - yx/2 = 1/2 = 0 (no pair of (y,x))
  - xy%2 = 1%2 = 1 (one leftover (x,y))
  - yx%2 = 1%2 = 1 (one leftover (y,x))

Step 2: Handle leftovers
  - We have one (x,y) and one (y,x)
  - Need 2 swaps to fix both:
    1. Swap one position to create a pair
    2. Swap again to fix both

Result = 0 + 0 + 1 + 1 = 2
```

**Example 3: `s1 = "xx"`, `s2 = "xy"`**

**Count mismatches:**
```
Position 0: s1[0]='x', s2[0]='x' → match
Position 1: s1[1]='x', s2[1]='y' → (x,y) mismatch → xy++

xy = 1, yx = 0
Total = 1 (odd, impossible)
```

**Execution:**
```
Check: (xy + yx) % 2 = (1 + 0) % 2 = 1
Return: -1 (impossible)
```

## Algorithm Breakdown

### **Why Pairing Works**

**Two (x,y) mismatches:**
- Position i: (x,y)
- Position j: (x,y)
- Swap at position i: s1[i]='y', s2[i]='x' → now (y,x) at i
- Now we have (y,x) at i and (x,y) at j
- These can be fixed with additional swaps

**Actually, the key insight is simpler:**
- When we have two (x,y) mismatches, we can think of them as needing to swap the 'x' from s1 with the 'y' from s2
- But since we can only swap at the same index, we need a different strategy
- The algorithm counts pairs because pairs can be resolved efficiently

### **Why Odd Total is Impossible**

**Each swap affects 2 positions:**
- When we swap s1[i] and s2[i], we fix the mismatch at position i
- But this might create or fix mismatches in a way that requires even number of total mismatches

**Mathematical proof:**
- Each swap changes the state of 2 characters (one in s1, one in s2)
- To make strings equal, we need to resolve all mismatches
- If total mismatches is odd, we can't pair them all, so it's impossible

### **Formula Explanation**

**`xy/2 + yx/2 + xy%2 + yx%2`:**

1. **`xy/2`**: Integer division gives number of pairs of (x,y) mismatches
   - Each pair can be resolved with 1 swap (in optimal strategy)

2. **`yx/2`**: Integer division gives number of pairs of (y,x) mismatches
   - Each pair can be resolved with 1 swap

3. **`xy%2 + yx%2`**: Remainders give leftover mismatches
   - If `xy%2 == 1` and `yx%2 == 1`: We have one of each type
   - These require 2 swaps to resolve (1+1=2)
   - If only one is 1: This case shouldn't happen (would make total odd, already checked)

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the length of `s1` and `s2`
  - Single pass through both strings to count mismatches
  - Constant time operations for arithmetic
- **Space Complexity**: O(1)
  - Only using two variables (`xy`, `yx`)
  - No additional data structures

## Key Points

1. **Mismatch Types**: Identify two types of mismatches: (x,y) and (y,x)
2. **Parity Check**: Total mismatches must be even (otherwise impossible)
3. **Pairing Strategy**: Pair same-type mismatches (1 swap per pair)
4. **Leftover Handling**: One of each type requires 2 swaps
5. **Simple Formula**: `xy/2 + yx/2 + xy%2 + yx%2`

## Alternative Approaches

### **Approach 1: Mismatch Pairing (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Optimal solution, most efficient

### **Approach 2: Greedy Simulation**
- **Time**: O(n²) or worse
- **Space**: O(n)
- **Not practical**: Try all possible swap sequences

### **Approach 3: Graph Theory**
- **Time**: O(n)
- **Space**: O(n)
- **Overkill**: Can model as graph, but current approach is simpler

## Edge Cases

1. **Strings already equal**: `s1 = "xx"`, `s2 = "xx"` → return 0 (no swaps needed)
2. **All (x,y) mismatches**: `s1 = "xx"`, `s2 = "yy"` → return 1 (if even number)
3. **All (y,x) mismatches**: `s1 = "yy"`, `s2 = "xx"` → return 1 (if even number)
4. **Mixed mismatches**: `s1 = "xy"`, `s2 = "yx"` → return 2
5. **Odd total**: `s1 = "xx"`, `s2 = "xy"` → return -1 (impossible)

## Common Mistakes

1. **Not checking odd total**: Forgetting to return -1 when total mismatches is odd
2. **Wrong pairing logic**: Not understanding how to pair mismatches
3. **Off-by-one errors**: Incorrect calculation of pairs and leftovers
4. **Not handling leftovers**: Forgetting the `xy%2 + yx%2` term
5. **Complex simulation**: Trying to simulate swaps instead of using the formula

## Related Problems

- [1217. Minimum Cost to Move Chips to The Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) - Similar parity-based greedy
- [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) - String manipulation
- [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) - Similar counting approach

## Follow-Up: Why the Formula Works

**Question**: Why does `xy/2 + yx/2 + xy%2 + yx%2` give the correct answer?

**Answer**:
- **Pairs of same type**: Two (x,y) mismatches can be resolved together (1 swap for the pair)
- **Pairs of same type**: Two (y,x) mismatches can be resolved together (1 swap for the pair)
- **Leftovers**: If we have one (x,y) and one (y,x), we need 2 swaps:
  1. First swap fixes one but creates a cycle
  2. Second swap completes the fix
- The formula counts: pairs (1 swap each) + leftovers (2 swaps if both exist)

## Tags

`String`, `Math`, `Greedy`, `Medium`

