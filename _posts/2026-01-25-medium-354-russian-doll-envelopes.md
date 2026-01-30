---
layout: post
title: "354. Russian Doll Envelopes"
date: 2026-01-25 00:00:00 -0700
categories: [leetcode, medium, array, dynamic-programming, binary-search, sorting]
permalink: /2026/01/25/medium-354-russian-doll-envelopes/
tags: [leetcode, medium, array, dynamic-programming, binary-search, sorting, longest-increasing-subsequence]
---

# 354. Russian Doll Envelopes

## Problem Statement

You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi, hi]` represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return *the maximum number of envelopes you can Russian doll* (i.e., put one inside the other).

**Note:** You cannot rotate an envelope.

## Examples

**Example 1:**

```
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

**Example 2:**

```
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
Explanation: No envelope can fit into another envelope.
```

## Constraints

- `1 <= envelopes.length <= 10^5`
- `envelopes[i].length == 2`
- `1 <= wi, hi <= 10^5`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Fitting condition**: For envelope A to fit inside envelope B, do both width and height need to be strictly smaller? (Assumption: Yes - both `w1 < w2` AND `h1 < h2` must be true)

2. **Equal dimensions**: What if two envelopes have the same width or height? (Assumption: They cannot nest - need strictly smaller dimensions)

3. **Rotation**: Can we rotate envelopes (swap width and height)? (Assumption: No - envelopes cannot be rotated)

4. **Multiple nesting**: Can we nest multiple envelopes? (Assumption: Yes - we want the maximum number of envelopes that can be nested)

5. **Empty result**: What should we return if no envelopes can be nested? (Assumption: Return `1` - at least one envelope can be considered as a "nest")

## Solution Approach

This problem is a **2D version of the Longest Increasing Subsequence (LIS)** problem. We need to find the longest chain of envelopes where each envelope can fit inside the next.

### Key Insights:

1. **Sorting Strategy**: Sort by width (ascending), and if widths are equal, sort by height (descending)
   - This ensures we process envelopes in order of increasing width
   - Descending height for equal widths prevents multiple envelopes with same width from being in the chain
2. **LIS on Heights**: After sorting, find LIS on heights using binary search
3. **Binary Search Optimization**: Use `lower_bound` to find insertion position in O(log n) time

### Why Sort Height Descending for Equal Widths?

If we have envelopes `[5,4]` and `[5,5]`, we want to consider `[5,5]` before `[5,4]` so that:
- If `[5,5]` can't fit in the chain, we can still try `[5,4]`
- This prevents both from being in the chain (which would be invalid since they have the same width)

## Solution

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if(envelopes.empty()) return 0;
        const int N = envelopes.size();
        sort(envelopes.begin(), envelopes.end(), [](const auto& e1, const auto& e2) {
            return e1[0] < e2[0] || (e1[0] == e2[0] && e1[1] > e2[1]);
        });

        vector<int> dp = {envelopes[0][1]};
        for(int i = 1; i < N; i++) {
            int num = envelopes[i][1];
            if(num > dp.back()) {
                dp.push_back(num);
            } else {
                auto it = lower_bound(dp.begin(), dp.end(), num);
                *it = num;
            }
        }
        return dp.size();
    }
};
```

### Algorithm Explanation:

#### **Step 1: Sort Envelopes**

```cpp
sort(envelopes.begin(), envelopes.end(), [](const auto& e1, const auto& e2) {
    return e1[0] < e2[0] || (e1[0] == e2[0] && e1[1] > e2[1]);
});
```

- **Primary Sort**: By width (`e1[0]`) in ascending order
- **Secondary Sort**: If widths are equal, by height (`e1[1]`) in descending order
- **Result**: Envelopes are ordered by width, with taller envelopes first when widths match

#### **Step 2: Find LIS on Heights**

After sorting, we only need to find the longest increasing subsequence on heights, since widths are already in order.

```cpp
vector<int> dp = {envelopes[0][1]};
for(int i = 1; i < N; i++) {
    int num = envelopes[i][1];
    if(num > dp.back()) {
        dp.push_back(num);
    } else {
        auto it = lower_bound(dp.begin(), dp.end(), num);
        *it = num;
    }
}
```

- **`dp`**: Maintains smallest tail element for each subsequence length
- **If `num > dp.back()`**: Extend the longest subsequence
- **Otherwise**: Replace the first element >= `num` to maintain smaller tails

### Example Walkthrough:

**Input:** `envelopes = [[5,4],[6,4],[6,7],[2,3]]`

```
Step 1: Sort
  Original: [[5,4], [6,4], [6,7], [2,3]]
  Sorted:   [[2,3], [5,4], [6,7], [6,4]]
            (by width ascending, height descending for equal widths)

Step 2: Find LIS on Heights
  Process [2,3]: dp = [3]
  Process [5,4]: 4 > 3 → dp = [3, 4]
  Process [6,7]: 7 > 4 → dp = [3, 4, 7]
  Process [6,4]: 4 <= 7, replace first >= 4 → dp = [3, 4, 7]
                 (lower_bound finds position of 4, replaces it)

Result: dp.size() = 3 ✓

Chain: [2,3] → [5,4] → [6,7]
```

### Why This Works:

1. **Sorting by Width**: Ensures envelopes are processed in order of increasing width
2. **Descending Height for Equal Widths**: Prevents multiple envelopes with same width from being in chain
3. **LIS on Heights**: After sorting, finding LIS on heights gives the longest valid chain
4. **Binary Search**: `lower_bound` finds insertion position in O(log n) time

### Complexity Analysis:

- **Time Complexity:** O(n log n)
  - Sorting: O(n log n)
  - Finding LIS: O(n log n) - each element requires O(log n) binary search
  - Overall: O(n log n)

- **Space Complexity:** O(n)
  - `dp` array: O(n) in worst case
  - Sorting: O(1) extra space (in-place)
  - Overall: O(n)

## Key Insights

1. **2D LIS Problem**: This is essentially finding LIS in 2D space
2. **Sorting Strategy**: Sort by one dimension, then find LIS on the other
3. **Equal Width Handling**: Sort heights descending for equal widths to prevent invalid chains
4. **Binary Search Optimization**: Use `lower_bound` for O(log n) insertion
5. **Greedy Approach**: Maintain smallest tail elements for each subsequence length

## Edge Cases

1. **Empty input**: `envelopes = []` → return `0`
2. **Single envelope**: `envelopes = [[1,1]]` → return `1`
3. **All same size**: `envelopes = [[1,1],[1,1],[1,1]]` → return `1`
4. **No valid chain**: All envelopes have same width → return `1`
5. **Perfect chain**: Envelopes form a perfect chain → return `n`

## Common Mistakes

1. **Wrong sorting order**: Not sorting heights descending for equal widths
2. **Using strict inequality**: Must use `>` not `>=` for fitting condition
3. **Not handling empty input**: Should return `0` for empty array
4. **Wrong LIS implementation**: Not using binary search optimization
5. **Forgetting equal width constraint**: Multiple envelopes with same width can't be in chain

## Alternative Approaches

### Approach 2: O(n²) Dynamic Programming

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if(envelopes.empty()) return 0;
        sort(envelopes.begin(), envelopes.end());
        int n = envelopes.size();
        vector<int> dp(n, 1);
        
        for(int i = 1; i < n; i++) {
            for(int j = 0; j < i; j++) {
                if(envelopes[i][0] > envelopes[j][0] && 
                   envelopes[i][1] > envelopes[j][1]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        
        return *max_element(dp.begin(), dp.end());
    }
};
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

**When to Use:** Simpler code, but slower for large inputs (n > 10⁴)

## Related Problems

- [LC 300: Longest Increasing Subsequence](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-300-longest-increasing-subsequence/) - 1D LIS problem
- [LC 673: Number of Longest Increasing Subsequence](https://robinali34.github.io/blog_leetcode/2026/01/09/medium-673-number-of-longest-increasing-subsequence/) - Count number of LIS
- [LC 646: Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) - Similar interval chaining
- [LC 334: Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) - Check if triplet exists

---

*This problem demonstrates how to extend the **Longest Increasing Subsequence** pattern to 2D. The key insight is sorting by one dimension and finding LIS on the other, with careful handling of equal values.*
