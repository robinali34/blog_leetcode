---
layout: post
title: "[Medium] 351. Android Unlock Patterns"
date: 2026-01-02 00:00:00 -0700
categories: [leetcode, medium, backtracking, recursion, dynamic-programming]
permalink: /2026/01/02/medium-351-android-unlock-patterns/
---
Android devices have a special lock screen with a `3 x 3` grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, which must meet the following conditions:

1. All of the dots must be **distinct**.
2. If the line segment connecting two consecutive dots in the pattern passes through the **center** of any other dot, the other dot must have previously appeared in the pattern. (No jumps through unvisited dots, except the center dot which can be jumped over if already visited.)
3. The dots in the pattern must all be connected.

Given two integers `m` and `n`, return the **number of unlock patterns** of the Android lock screen that consist of **at least `m` keys and at most `n` keys**.

Two unlock patterns are considered **different** if the two sequences of dots are different.

## Thinking Process

Android devices have a special lock screen with a `3 x 3` grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, which must meet the following conditions:

1. All of the dots must be **distinct**.

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">1D DP recurrence</text>

  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [52. N-Queens II](https://www.leetcode.com/problems/n-queens-ii/) - Count valid queen placements
- [46. Permutations](https://www.leetcode.com/problems/permutations/) - Generate all permutations
- [79. Word Search](https://www.leetcode.com/problems/word-search/) - Grid path finding
- [212. Word Search II](https://www.leetcode.com/problems/word-search-ii/) - Multiple word search

## Tags

`Backtracking`, `Recursion`, `Dynamic Programming`, `Medium`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 351: Android Unlock Patterns on LeetCode](https://www.leetcode.com/problems/android-unlock-patterns/)
- [LeetCode Discuss — LC 351: Android Unlock Patterns](https://www.leetcode.com/problems/android-unlock-patterns/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/android-unlock-patterns/editorial/) *(may require premium)*

## Template Reference

- [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/)
