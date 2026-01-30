---
layout: post
title: "[Medium] 593. Valid Square"
date: 2025-12-02 00:00:00 -0800
categories: leetcode algorithm medium cpp math geometry problem-solving
---

# [Medium] 593. Valid Square

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Square definition**: What makes a valid square? (Assumption: Four points forming a square - four equal sides, four right angles, two equal diagonals)

2. **Point order**: Are points given in any specific order? (Assumption: No - points can be in any order, need to determine if they form a square)

3. **Degenerate cases**: Can points be collinear or form other shapes? (Assumption: Need to check - points might form rectangle, rhombus, or other shapes)

4. **Return value**: What should we return? (Assumption: Boolean - true if points form a valid square, false otherwise)

5. **Duplicate points**: Can there be duplicate points? (Assumption: Per problem, should check - duplicate points cannot form a square)

## Solution: Distance-Based Validation

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

## How the Algorithm Works

### Key Insight: Square Properties

A square has specific distance properties:
- **4 equal sides**: Each side has the same length
- **2 equal diagonals**: Each diagonal has the same length
- **Diagonal = side × √2**: By Pythagorean theorem

### Algorithm Steps

1. **Calculate all pairwise distances**: For 4 points, there are C(4,2) = 6 pairs
2. **Check for duplicate points**: If any distance is 0, return false
3. **Count unique distances**: A valid square has exactly 2 unique distances
   - One distance appears 4 times (sides)
   - Another distance appears 2 times (diagonals)

### Why This Works

For a valid square with 4 points:
- **6 total distances**: 4 sides + 2 diagonals
- **2 unique distances**: side² and diagonal²
- **No zero distances**: All points are distinct

The condition `distances.size() == 2` ensures:
- All 4 sides are equal (same distance appears 4 times)
- Both diagonals are equal (same distance appears 2 times)
- The shape is a square (not a rectangle, which would have different side lengths)

### Example Walkthrough

**Example 1:** `p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]`

```
Distances:
- p1-p2: (0-1)² + (0-1)² = 1 + 1 = 2 (diagonal)
- p1-p3: (0-1)² + (0-0)² = 1 + 0 = 1 (side)
- p1-p4: (0-0)² + (0-1)² = 0 + 1 = 1 (side)
- p2-p3: (1-1)² + (1-0)² = 0 + 1 = 1 (side)
- p2-p4: (1-0)² + (1-1)² = 1 + 0 = 1 (side)
- p3-p4: (1-0)² + (0-1)² = 1 + 1 = 2 (diagonal)

Unique distances: {1, 2}
Size: 2 ✓ (valid square)
```

**Example 2:** `p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]`

```
Distances:
- p1-p2: 2
- p1-p3: 1
- p1-p4: 144
- p2-p3: 1
- p2-p4: 122
- p3-p4: 145

Unique distances: {1, 2, 122, 144, 145}
Size: 5 ✗ (not a square)
```

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Calculate distances | O(1) | O(1) |
| Store in set | O(1) | O(1) |
| **Overall** | **O(1)** | **O(1)** |

## Edge Cases

1. **Duplicate points**: If any two points are the same, return false
2. **Rectangle**: Would have 3 unique distances (2 different sides + 1 diagonal)
3. **Rhombus**: Would have 2 unique distances but diagonal ≠ side × √2 (but our solution still works)
4. **Degenerate cases**: All points collinear or forming other shapes

## Common Mistakes

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

## Related Problems

- [469. Convex Polygon](https://leetcode.com/problems/convex-polygon/) - Validate polygon shape
- [335. Self Crossing](https://leetcode.com/problems/self-crossing/) - Geometric validation
- [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) - Point geometry
- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) - Distance calculations

