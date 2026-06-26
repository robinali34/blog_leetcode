---
layout: post
title: "[Medium] 593. Valid Square"
date: 2025-12-02 00:00:00 -0800
categories: leetcode algorithm medium cpp math geometry problem-solving
---
Given the coordinates of four points in 2D space `p1`, `p2`, `p3`, and `p4`, return `true` if the four points construct a square.

## Examples

**Example 1:**
```
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
```

**Example 2:**
```
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
```

**Example 3:**
```
Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
```

## Constraints

- `p1.length == p2.length == p3.length == p4.length == 2`
- `-10^4 <= xi, yi <= 10^4`

## Thinking Process

Given the coordinates of four points in 2D space `p1`, `p2`, `p3`, and `p4`, return `true` if the four points construct a square.

- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute force** *(this problem)* | Often $O(n^2)$ or $O(2^n)$ | $O(n)$ | Baseline; clarifies the optimization target |
| Sort + scan | $O(n \log n)$ | $O(1)$ | Pairs, intervals, greedy ordering |
| Hash map / set | $O(n)$ | $O(n)$ | Frequency, membership, two-sum style |
| Single-pass linear | $O(n)$ | $O(1)$ | Two pointers, sliding window, Kadane |

## Solution

**Time Complexity:** O(1) - Constant time since we only have 4 points  
**Space Complexity:** O(1) - Using a set with at most 2 elements

The key insight is that a valid square has exactly **two unique distances**:
1. **Side length** (appears 4 times - 4 sides)
2. **Diagonal length** (appears 2 times - 2 diagonals)

Additionally, we must check that no two points are the same (distance = 0).

```cpp
#include <vector>
#include <unordered_set>

class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        unordered_set<int> distances;
        
        vector<vector<int>> points = {p1, p2, p3, p4};
        
        for(int i = 0; i < 4; i++) {
            for(int j = i + 1; j < 4; j++) {
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                int distSq = dx * dx + dy * dy;
                
                if(distSq == 0) return false; // Duplicate points
                
                distances.insert(distSq);
            }
        }
        
        return distances.size() == 2;
    }
};
```

### Solution Explanation

**Approach:** Brute force (this problem)

**Key idea:** Given the coordinates of four points in 2D space `p1`, `p2`, `p3`, and `p4`, return `true` if the four points construct a square.

**How the code works:**
- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.

**Walkthrough** — input `p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]`, expected output `true`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Operation | Time | Space |
|-----------|------|-------|
| Calculate distances | O(1) | O(1) |
| Store in set | O(1) | O(1) |
| **Overall** | **O(1)** | **O(1)** |
## Common Mistakes

1. **Duplicate points**: If any two points are the same, return false
2. **Rectangle**: Would have 3 unique distances (2 different sides + 1 diagonal)
3. **Rhombus**: Would have 2 unique distances but diagonal ≠ side × √2 (but our solution still works)
4. **Degenerate cases**: All points collinear or forming other shapes

1. **Not checking for duplicate points**: Must return false if `distSq == 0`
2. **Wrong distance count**: Expecting exactly 2 unique distances, not more or less
3. **Using floating point**: Using squared distances avoids precision issues
4. **Not considering all pairs**: Must check all 6 pairs of points

## Alternative Approach: Verify Diagonal Relationship

A more rigorous approach would also verify that `diagonal² = 2 × side²`:

```cpp
class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        unordered_map<int, int> distCount;
        vector<vector<int>> points = {p1, p2, p3, p4};
        
        for(int i = 0; i < 4; i++) {
            for(int j = i + 1; j < 4; j++) {
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];
                int distSq = dx * dx + dy * dy;
                
                if(distSq == 0) return false;
                distCount[distSq]++;
            }
        }
        
        if(distCount.size() != 2) return false;
        
        int side = 0, diagonal = 0;
        for(auto& [dist, count] : distCount) {
            if(count == 4) side = dist;
            else if(count == 2) diagonal = dist;
            else return false;
        }
        
        return diagonal == 2 * side; // Verify diagonal² = 2 × side²
    }
};
```

However, the simpler solution (checking `distances.size() == 2`) is sufficient because:
- If there are exactly 2 unique distances with 4 points
- And one appears 4 times (sides) and one appears 2 times (diagonals)
- Then it must be a square (the geometric constraints are satisfied)

## Key Takeaways

- **Pattern:** Brute force (this problem)
- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.

## References

- [LC 593: Valid Square on LeetCode](https://www.leetcode.com/problems/valid-square/)
- [LeetCode Discuss — LC 593: Valid Square](https://www.leetcode.com/problems/valid-square/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/valid-square/editorial/) *(may require premium)*

## Related Problems

- [469. Convex Polygon](https://www.leetcode.com/problems/convex-polygon/) - Validate polygon shape
- [335. Self Crossing](https://www.leetcode.com/problems/self-crossing/) - Geometric validation
- [149. Max Points on a Line](https://www.leetcode.com/problems/max-points-on-a-line/) - Point geometry
- [973. K Closest Points to Origin](https://www.leetcode.com/problems/k-closest-points-to-origin/) - Distance calculations
