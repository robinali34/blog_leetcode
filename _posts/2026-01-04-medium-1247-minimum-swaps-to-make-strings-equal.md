---
layout: post
title: "[Medium] 1247. Minimum Swaps to Make Strings Equal"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, medium, string, math, greedy]
permalink: /2026/01/04/medium-1247-minimum-swaps-to-make-strings-equal/
---
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

## Thinking Process

You are given two strings `s1` and `s2` of equal length consisting of only letters `'x'` and `'y'`.

In one move, you can swap two characters belonging to **different strings** at the same position. In other words, swap `s1[i]` and `s2[i]`.

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

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

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** You are given two strings `s1` and `s2` of equal length consisting of only letters `'x'` and `'y'`.

**How the code works:**
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `s1 = "xx", s2 = "yy"`, expected output `1`:

We have 2 (x,y) mismatches at positions 0 and 1.
- xy = 2, yx = 0
- Total = 2 (even, possible)
- Result = 2/2 + 0/2 + 2%2 + 0%2 = 1 + 0 + 0 + 0 = 1
The algorithm indicates 1 swap is needed to make the strings equal.

**Time:** O(n) where n is the length of `s1` and `s2` · **Space:** O(1)

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

## Common Mistakes

1. **Strings already equal**: `s1 = "xx"`, `s2 = "xx"` → return 0 (no swaps needed)
2. **All (x,y) mismatches**: `s1 = "xx"`, `s2 = "yy"` → return 1 (if even number)
3. **All (y,x) mismatches**: `s1 = "yy"`, `s2 = "xx"` → return 1 (if even number)
4. **Mixed mismatches**: `s1 = "xy"`, `s2 = "yx"` → return 2
5. **Odd total**: `s1 = "xx"`, `s2 = "xy"` → return -1 (impossible)

1. **Not checking odd total**: Forgetting to return -1 when total mismatches is odd
2. **Wrong pairing logic**: Not understanding how to pair mismatches
3. **Off-by-one errors**: Incorrect calculation of pairs and leftovers
4. **Not handling leftovers**: Forgetting the `xy%2 + yx%2` term
5. **Complex simulation**: Trying to simulate swaps instead of using the formula

## Related Problems

- [1217. Minimum Cost to Move Chips to The Same Position](https://www.leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) - Similar parity-based greedy
- [1249. Minimum Remove to Make Valid Parentheses](https://www.leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) - String manipulation
- [921. Minimum Add to Make Parentheses Valid](https://www.leetcode.com/problems/minimum-add-to-make-parentheses-valid/) - Similar counting approach

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

## Key Takeaways

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

## References

- [LC 1247: Minimum Swaps to Make Strings Equal on LeetCode](https://www.leetcode.com/problems/minimum-swaps-to-make-strings-equal/)
- [LeetCode Discuss — LC 1247: Minimum Swaps to Make Strings Equal](https://www.leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-swaps-to-make-strings-equal/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
