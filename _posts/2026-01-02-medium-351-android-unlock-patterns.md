---
layout: post
title: "351. Android Unlock Patterns"
date: 2026-01-02 00:00:00 -0700
categories: [leetcode, medium, backtracking, recursion, dynamic-programming]
permalink: /2026/01/02/medium-351-android-unlock-patterns/
---

# 351. Android Unlock Patterns

## Problem Statement

Android devices have a special lock screen with a `3 x 3` grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, which must meet the following conditions:

1. All of the dots must be **distinct**.
2. If the line segment connecting two consecutive dots in the pattern passes through the **center** of any other dot, the other dot must have previously appeared in the pattern. (No jumps through unvisited dots, except the center dot which can be jumped over if already visited.)
3. The dots in the pattern must all be connected.

Given two integers `m` and `n`, return the **number of unlock patterns** of the Android lock screen that consist of **at least `m` keys and at most `n` keys**.

Two unlock patterns are considered **different** if the two sequences of dots are different.

## Examples

**Example 1:**
```
Input: m = 1, n = 1
Output: 9
Explanation: There are 9 patterns of length 1 (each dot individually).
```

**Example 2:**
```
Input: m = 1, n = 2
Output: 65
Explanation: There are 9 patterns of length 1 + 56 patterns of length 2.
```

## Grid Layout

The 3×3 grid is numbered as follows:
```
0  1  2
3  4  5
6  7  8
```

## Constraints

- `1 <= m <= n <= 9`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Pattern definition**: What is an unlock pattern? (Assumption: Sequence of distinct dots connected by lines - valid if line doesn't pass through unvisited dots)

2. **Pattern length**: What length patterns should we count? (Assumption: Patterns with length between m and n inclusive)

3. **Return value**: What should we return? (Assumption: Integer - number of valid unlock patterns)

4. **Line rules**: What makes a line invalid? (Assumption: If line passes through an unvisited dot, pattern is invalid - must visit intermediate dots first)

5. **Starting point**: Can we start from any dot? (Assumption: Yes - can start from any of the 9 dots)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Generate all possible sequences of dots with lengths between m and n. For each sequence, check if it forms a valid pattern by verifying that lines between consecutive dots don't pass through unvisited dots. This requires checking all permutations, which has exponential complexity. The challenge is efficiently checking if a line passes through an unvisited dot.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use backtracking: start from each dot, recursively try all unvisited dots. Before moving to a new dot, check if the line passes through any unvisited dot (if so, skip). Use a visited set to track visited dots. This prunes invalid paths early but still explores many paths. The key is correctly identifying when a line passes through an unvisited dot (e.g., moving from corner to opposite corner passes through center).

**Step 3: Optimized Solution (8 minutes)**

Use backtracking with a jump table. Precompute which dots are "between" other dots (e.g., 1 and 3 have 2 between them). When moving from dot a to dot b, if there's a dot c between them and c is unvisited, the move is invalid. Use DFS with backtracking: for each pattern length from m to n, count valid patterns starting from each dot. Memoization can help if patterns are repeated. This achieves optimal time complexity by exploring only valid paths. The key insight is precomputing the "between" relationships to make validity checks O(1).

## Solution Approach

This problem requires counting all valid unlock patterns of length between `m` and `n`. The key challenge is handling the "jump over" rule: you cannot jump over an unvisited dot unless it's the center (dot 4).

### Key Insights:

1. **Backtracking**: Use DFS to explore all possible patterns
2. **Validation Logic**: Check if a move is valid based on the last position
3. **Jump Over Rule**: 
   - If moving between opposite corners/sides, must pass through center
   - Center (4) can be jumped over if already visited
   - Other dots cannot be jumped over
4. **Pattern Length**: Count patterns of length `m` to `n`

### Algorithm:

1. **For each length** from `m` to `n`:
   - Start from each possible position (or use symmetry)
   - Use backtracking to count valid patterns
2. **Validation**: Check if move from `last` to `idx` is valid
3. **Count**: Sum all valid patterns

## Solution

### **Solution: Backtracking with Validation**

```cpp
class Solution {
public:
    int numberOfPatterns(int m, int n) {
        used.resize(9, false);
        int rtn = 0;
        for(int len = m; len <= n; len++) {
            rtn += claPatterns(-1, len);
            for(int i = 0; i < 9; i++) used[i] = false;
        }
        return rtn;
    }
private:
    vector<bool> used;

    bool isValid(int idx, int last) {
        if(used[idx]) return false;
        if(last == -1) return true;
        if((idx + last) % 2 == 1) return true;
        int mid = (idx + last) / 2;
        if(mid == 4) return used[mid];
        if((idx % 3 != last % 3) && (idx / 3 != last / 3)) return true;
        return used[mid];
    }

    int claPatterns(int last, int len) {
        if(len == 0) return 1;
        int sum = 0;
        for(int i = 0; i < 9; i++) {
            if(isValid(i, last)) {
                used[i] = true;
                sum += claPatterns(i, len - 1);
                used[i] = false;
            }
        }
        return sum;
    }
};
```

### **Algorithm Explanation:**

1. **Main Function (Lines 3-10)**:
   - **Initialize**: Create `used` array to track visited dots
   - **For each length**: Count patterns of length `len` from `m` to `n`
   - **Reset**: Clear `used` array after each length
   - **Return**: Sum of all valid patterns

2. **IsValid Function (Lines 14-23)**:
   - **Already used**: If `idx` is already visited, return false
   - **First move**: If `last == -1`, any dot is valid
   - **Adjacent move**: If `(idx + last) % 2 == 1`, dots are adjacent (valid)
   - **Center jump**: If `mid == 4` (center), check if center is visited
   - **Diagonal jump**: If dots are on different rows and columns, check if middle dot is visited
   - **Same row/column**: Otherwise, check if middle dot is visited

3. **Count Patterns (Lines 25-35)**:
   - **Base case**: If `len == 0`, found a valid pattern (return 1)
   - **Try each dot**: For each unvisited dot `i`
   - **Validate**: Check if move from `last` to `i` is valid
   - **Recurse**: If valid, mark as used and recurse with `len - 1`
   - **Backtrack**: Unmark after recursion

### **Validation Logic Breakdown:**

The `isValid` function handles different cases:

**Case 1: Adjacent moves (no jump)**
```
If (idx + last) % 2 == 1:
    Examples: 0→1, 1→2, 0→3, 3→6
    Always valid (no middle dot)
```

**Case 2: Center (dot 4)**
```
If mid == 4:
    Examples: 0→8, 2→6, 1→7, 3→5
    Valid only if center (4) is already visited
```

**Case 3: Same row or column**
```
If (idx % 3 == last % 3) or (idx / 3 == last / 3):
    Examples: 0→2 (row), 0→6 (column)
    Valid only if middle dot is visited
    Middle: (idx + last) / 2
```

**Case 4: Diagonal (different row and column)**
```
If (idx % 3 != last % 3) && (idx / 3 != last / 3):
    Examples: 1→3, 1→5, 3→1, 5→1
    Always valid (no middle dot to jump over)
```

### **Example Walkthrough:**

**Count patterns of length 2:**

Starting from dot 0:
```
0 → 1: Valid (adjacent)
  1 → 0: Invalid (already used)
  1 → 2: Valid (adjacent)
  1 → 3: Valid (adjacent)
  1 → 4: Valid (adjacent)
  1 → 5: Valid (adjacent)
  1 → 6: Valid (diagonal, no middle)
  1 → 7: Valid (adjacent)
  1 → 8: Valid (diagonal, no middle)
  Total: 8 patterns starting with 0→1

0 → 2: Valid (same row)
  2 → 0: Invalid (already used)
  2 → 1: Valid (adjacent, but 1 not visited yet - wait, need to check middle)
  Actually: 0→2, middle is 1. Need 1 to be visited.
  But if we haven't visited 1, this is invalid.
  
0 → 4: Valid (adjacent)
0 → 6: Valid (same column)
0 → 8: Invalid (diagonal through center 4, need 4 visited first)
```

**Pattern: 0→1→2**
```
Step 1: 0 → 1
  isValid(1, 0): (1+0)%2=1 → true ✓

Step 2: 1 → 2
  isValid(2, 1): (2+1)%2=1 → true ✓
  
Pattern valid: [0, 1, 2]
```

**Pattern: 0→2 (invalid without visiting 1)**
```
Step 1: 0 → 2
  isValid(2, 0): 
    (2+0)%2=0 (not adjacent)
    mid = (2+0)/2 = 1
    mid != 4
    Check: idx%3=2, last%3=0 → different columns
           idx/3=0, last/3=0 → same row
    Same row case: need used[1] = true
    But 1 is not visited → return false ✗
```

**Pattern: 0→4→8 (valid with center)**
```
Step 1: 0 → 4
  isValid(4, 0): (4+0)%2=0, mid=2, mid!=4, same column → need used[2]
  Wait, let's recalculate:
    0→4: (0+4)%2=0, mid=2, but 0 and 4 are in same column
    Actually: 0%3=0, 4%3=1 (different columns)
              0/3=0, 4/3=1 (different rows)
    So it's diagonal? No, 0 and 4 are adjacent vertically.
    
Let me reconsider the grid:
0(0,0)  1(0,1)  2(0,2)
3(1,0)  4(1,1)  5(1,2)
6(2,0)  7(2,1)  8(2,2)

0→4: row 0→1, col 0→1 (diagonal move)
  (0+4)%2=0, mid=2
  But wait, the actual middle between 0 and 4 would be... 
  Actually, the code uses (idx+last)/2 = 2, which is the arithmetic mean.
  But in a 2D grid, the middle between (0,0) and (1,1) is not at index 2.
  
The key insight: The formula (idx+last)/2 works for 1D linear indexing when dots are in a straight line (same row, same column, or through center).

For 0→4: They're diagonal, so (idx%3 != last%3) && (idx/3 != last/3) → returns true directly.

Actually, let me trace through more carefully:
- 0→4: idx=4, last=0
  - used[4]? No, continue
  - last==-1? No
  - (4+0)%2==1? No (4%2=0)
  - mid = (4+0)/2 = 2
  - mid==4? No
  - (4%3 != 0%3)? Yes (1 != 0)
  - (4/3 != 0/3)? Yes (1 != 0)
  - Both true → return true ✓

So 0→4 is valid (diagonal, no middle dot).

Step 2: 4 → 8
  isValid(8, 4):
    - used[8]? No
    - (8+4)%2==1? No (12%2=0)
    - mid = (8+4)/2 = 6
    - mid==4? No
    - (8%3 != 4%3)? Yes (2 != 1)
    - (8/3 != 4/3)? Yes (2 != 1)
    - Both true → return true ✓

Pattern valid: [0, 4, 8]
```

## Algorithm Breakdown

### **Grid Representation**

The 3×3 grid is represented as a 1D array:
```
0  1  2     → indices 0, 1, 2
3  4  5     → indices 3, 4, 5
6  7  8     → indices 6, 7, 8
```

**Coordinates:**
- Row: `idx / 3`
- Column: `idx % 3`

### **Validation Cases**

1. **Adjacent Dots**: `(idx + last) % 2 == 1`
   - Examples: 0→1, 1→2, 0→3, 3→6
   - Always valid (no middle dot)

2. **Through Center**: `mid == 4`
   - Examples: 0→8, 2→6, 1→7, 3→5
   - Valid only if center (4) is visited

3. **Same Row**: `idx / 3 == last / 3` and `idx % 3 != last % 3`
   - Examples: 0→2, 3→5, 6→8
   - Valid only if middle dot is visited

4. **Same Column**: `idx % 3 == last % 3` and `idx / 3 != last / 3`
   - Examples: 0→6, 1→7, 2→8
   - Valid only if middle dot is visited

5. **Diagonal**: Different row and column
   - Examples: 1→3, 1→5, 3→1, 5→1
   - Always valid (no middle dot)

### **Why `(idx + last) % 2 == 1` Works**

This formula identifies adjacent dots in the grid:
- Adjacent horizontally: 0→1 (0+1=1), 1→2 (1+2=3)
- Adjacent vertically: 0→3 (0+3=3), 3→6 (3+6=9)
- Sum is odd → adjacent
- Sum is even → may need to check middle

## Time & Space Complexity

- **Time Complexity**: 
  - **Worst case**: O(9!) for length 9 patterns
  - **For length m to n**: Sum of permutations P(9,k) for k from m to n
  - **Practical**: Much better due to validation pruning
- **Space Complexity**: O(9) for `used` array and recursion stack

## Key Points

1. **Backtracking**: Explore all valid patterns recursively
2. **Validation**: Complex logic to handle jump-over rule
3. **Symmetry**: Could optimize by using symmetry (1,3,7,9 are symmetric; 2,4,6,8 are symmetric)
4. **Pruning**: Validation function prunes invalid paths early
5. **Reset**: Clear `used` array for each length to avoid interference

## Optimization Opportunities

### **Symmetry Optimization**

Since the grid is symmetric, we can count patterns starting from symmetric positions once and multiply:

```cpp
// Corners (0,2,6,8) are symmetric
// Edges (1,3,5,7) are symmetric  
// Center (4) is unique

int count = 0;
count += 4 * countFrom(0, len);  // corners
count += 4 * countFrom(1, len);  // edges
count += 1 * countFrom(4, len);  // center
```

This reduces computation by ~4x for corners and edges.

## Edge Cases

1. **m = n = 1**: Return 9 (each dot individually)
2. **m = n = 9**: Return number of Hamiltonian paths
3. **m = 1, n = 9**: Return all possible patterns
4. **Single length**: Patterns of exactly length m

## Related Problems

- [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/) - Count valid queen placements
- [46. Permutations](https://leetcode.com/problems/permutations/) - Generate all permutations
- [79. Word Search](https://leetcode.com/problems/word-search/) - Grid path finding
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/) - Multiple word search

## Tags

`Backtracking`, `Recursion`, `Dynamic Programming`, `Medium`

