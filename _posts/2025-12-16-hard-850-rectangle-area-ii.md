---
layout: post
title: "[Hard] 850. Rectangle Area II"
date: 2025-12-16 00:00:00 -0800
categories: leetcode algorithm hard cpp geometry sweep-line segment-tree problem-solving
---

{% raw %}
# [Hard] 850. Rectangle Area II

You are given a 2D array of axis-aligned `rectangles`. For each `rectangle[i] = [xi1, yi1, xi2, yi2]`, where `(xi1, yi1)` is the bottom-left corner and `(xi2, yi2)` is the top-right corner of the `ith` rectangle.

Calculate the **total area** covered by all `rectangles` in the plane. Any area covered by two or more rectangles should only be counted **once**.

Return the total area. Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Examples

**Example 1:**
```
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
```

**Example 2:**
```
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is 49.
```

## Constraints

- `1 <= rectangles.length <= 200`
- `rectangles[i].length == 4`
- `0 <= xi1, yi1, xi2, yi2 <= 10^9`
- `xi1 <= xi2`
- `yi1 <= yi2`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Rectangle representation**: How are rectangles represented? (Assumption: [x1, y1, x2, y2] - bottom-left and top-right corners, half-open intervals)

2. **Overlapping areas**: How should we handle overlapping rectangles? (Assumption: Count overlapping area only once - union of rectangles, not sum)

3. **Modulo requirement**: Should the result be modulo 10^9 + 7? (Assumption: Yes - per problem statement, return modulo 10^9 + 7)

4. **Rectangle boundaries**: Are boundaries inclusive or exclusive? (Assumption: Typically half-open [x1, x2) x [y1, y2) - need to clarify)

5. **Return value**: What should we return? (Assumption: Total area covered by union of all rectangles, modulo 10^9 + 7)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

For each rectangle, mark all covered cells in a 2D grid. However, coordinates can be up to 10^9, making this approach infeasible due to memory constraints. Alternatively, iterate through all pairs of rectangles, calculate their intersections, and use inclusion-exclusion principle. This becomes exponentially complex with many rectangles and doesn't scale well.

**Step 2: Semi-Optimized Approach (10 minutes)**

Use a sweep line algorithm: sweep vertically along the y-axis and track horizontal coverage at each y-coordinate. For each y-value, maintain an array tracking which x-segments are covered. When processing events (rectangle start/end), update coverage counts and calculate area incrementally. Use coordinate compression to map large x-coordinates to indices. This reduces the problem to manageable size but still requires O(n) time per event to update coverage, resulting in O(n² log n) overall complexity.

**Step 3: Optimized Solution (12 minutes)**

Enhance the sweep line approach with a Segment Tree for efficient range updates. Instead of updating coverage counts in an array (O(n) per event), use a segment tree that supports range updates in O(log n) time. The segment tree tracks coverage counts and calculates total covered length efficiently. This reduces the time complexity to O(n log n) - optimal for this problem. The key insight is that we need range updates (increment/decrement coverage for x-intervals) and range queries (total covered length), which segment trees handle efficiently.

## Solution 1: Sweep Line with Coordinate Compression

**Time Complexity:** O(n² log n) - Sorting events + O(n) per event for coverage calculation  
**Space Complexity:** O(n) - For events and coordinate arrays

This solution uses a sweep line algorithm with coordinate compression to handle large coordinate values efficiently.

```cpp
class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        const int OPEN = 1, CLOSE = -1, MOD = 1E9 + 7;

        vector<int> xCoords;
        vector<array<int, 4>> events; // {y, type, x1, x2}
        
        for(auto& rec : rectangles) {
            xCoords.push_back(rec[0]);
            xCoords.push_back(rec[2]);
            events.push_back({rec[1], OPEN, rec[0], rec[2]});
            events.push_back({rec[3], CLOSE, rec[0], rec[2]});
        }

        // Coordinate compression
        sort(xCoords.begin(), xCoords.end());
        xCoords.erase(unique(xCoords.begin(), xCoords.end()), xCoords.end());

        unordered_map<int, int> xIdx;
        for(int i = 0; i < xCoords.size(); i++) {
            xIdx[xCoords[i]] = i;
        }
        
        // Sort events by y-coordinate (process OPEN before CLOSE at same y)
        sort(events.begin(), events.end(), [](auto& a, auto& b){
            if(a[0] != b[0]) return a[0] < b[0];
            return a[1] > b[1];
        });
        
        int n = xCoords.size();
        vector<int> count(n, 0);  // Coverage count for each x-segment
        long long rtn = 0;
        int curY = events[0][0];
        
        for(auto& e: events) {
            int y = e[0], type = e[1], x1 = e[2], x2 = e[3];

            // Calculate total covered length
            long long coveredLen = 0;
            for(int i = 0; i < n - 1; i++) {
                if(count[i] > 0) {
                    coveredLen += xCoords[i + 1] - xCoords[i];
                }
            }
            
            rtn = (rtn + coveredLen * (y - curY)) % MOD;

            // Update coverage counts
            int idx1 = xIdx[x1], idx2 = xIdx[x2];
            for(int i = idx1; i < idx2; i++) {
                count[i] += type;
            }
            
            curY = y;
        }
        
        return (int)rtn;
    }
};
```

### How Solution 1 Works

1. **Event Generation**:
   - For each rectangle, create two events:
     - OPEN event at bottom edge (y1): Start covering x-range [x1, x2]
     - CLOSE event at top edge (y2): Stop covering x-range [x1, x2]

2. **Coordinate Compression**:
   - Collect all unique x-coordinates
   - Map them to indices for efficient segment tracking
   - This handles large coordinate values (up to 10^9)

3. **Sweep Line**:
   - Process events from bottom to top (sorted by y)
   - At each event, calculate the covered area since the last event
   - Area = coveredLength × (currentY - previousY)

4. **Coverage Tracking**:
   - `count[i]` tracks how many rectangles cover the segment [xCoords[i], xCoords[i+1]]
   - OPEN events increment count, CLOSE events decrement

### Key Insight

The sweep line moves vertically (along y-axis), and at each position, we calculate the horizontal coverage. By processing events in order, we can compute the total area incrementally.

## Solution 2: Segment Tree Optimization

**Time Complexity:** O(n log n) - Sorting events + O(log n) per event for segment tree operations  
**Space Complexity:** O(n) - For segment tree and coordinate arrays

This solution uses a segment tree for O(log n) range updates and queries, significantly improving performance.

```cpp
class Solution {
private:
    vector<int> xCoords;
    vector<int> counts;      // Coverage count at each node
    vector<long long> total; // Total covered length in range

    void update(int node, int lo, int hi, int left, int right, int delta) {
        if(right <= lo || hi <= left) return;  // No overlap
        
        if(left <= lo && hi <= right) {
            counts[node] += delta;
        } else {
            int mid = (lo + hi) / 2;
            update(2 * node, lo, mid, left, right, delta);
            update(2 * node + 1, mid, hi, left, right, delta);
        }
        
        // Update total covered length
        if(counts[node] > 0) {
            total[node] = xCoords[hi] - xCoords[lo];
        } else if(hi - lo == 1) {
            total[node] = 0;
        } else {
            total[node] = total[2 * node] + total[2 * node + 1];
        }
    }
    
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        const int OPEN = 1, CLOSE = -1, MOD = 1E9 + 7;
        
        set<int> xSet;
        vector<array<int, 4>> events;
        
        for(auto& rec: rectangles) {
            xSet.insert(rec[0]);
            xSet.insert(rec[2]);
            events.push_back({rec[1], OPEN, rec[0], rec[2]});
            events.push_back({rec[3], CLOSE, rec[0], rec[2]});
        }
        
        xCoords.assign(xSet.begin(), xSet.end());
        
        unordered_map<int, int> xIdx;
        for(int i = 0; i < xCoords.size(); i++) {
            xIdx[xCoords[i]] = i;
        }
        
        sort(events.begin(), events.end(), [](auto& a, auto& b) {
            if(a[0] != b[0]) return a[0] < b[0];
            return a[1] > b[1];
        });

        int n = xCoords.size();
        counts.assign(4 * n, 0);
        total.assign(4 * n, 0);
        
        long long rtn = 0;
        int curY = events[0][0];
        
        for(auto& e: events) {
            auto [y, type, x1, x2] = e;
            
            // Add area since last event
            rtn = (rtn + total[1] * (y - curY)) % MOD;
            
            // Update segment tree
            update(1, 0, n - 1, xIdx[x1], xIdx[x2], type);
            
            curY = y;
        }
        
        return (int)rtn;
    }
};
```

### How Solution 2 Works

1. **Segment Tree Structure**:
   - `counts[node]`: Number of rectangles fully covering this segment
   - `total[node]`: Total covered length in this segment's range

2. **Update Logic**:
   - If a node is fully covered by the update range, increment/decrement its count
   - Otherwise, recursively update children
   - Recalculate `total` based on:
     - If `counts[node] > 0`: Entire segment is covered
     - If leaf node with `counts = 0`: No coverage
     - Otherwise: Sum of children's coverage

3. **Query**:
   - `total[1]` (root) always contains the total covered length
   - O(1) query time after O(log n) updates

### Why Segment Tree is Better

| Operation | Solution 1 | Solution 2 |
|-----------|-----------|-----------|
| Range update | O(n) | O(log n) |
| Query coverage | O(n) | O(1) |
| **Total per event** | **O(n)** | **O(log n)** |
| **Overall** | **O(n² log n)** | **O(n log n)** |

## Comparison of Approaches

| Aspect | Sweep Line + Array | Sweep Line + Segment Tree |
|--------|-------------------|---------------------------|
| **Time Complexity** | O(n² log n) | O(n log n) |
| **Space Complexity** | O(n) | O(n) |
| **Code Complexity** | Simple | Moderate |
| **Best For** | Small n (≤ 200) | Large n |
| **Update Time** | O(n) | O(log n) |
| **Query Time** | O(n) | O(1) |

## Example Walkthrough

**Input:** `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`

### Coordinate Compression:
```
X-coordinates: [0, 1, 2, 3]
Indices:       [0, 1, 2, 3]
```

### Events (sorted by y):
```
y=0: OPEN  [0,2] (rect 0)
y=0: OPEN  [1,2] (rect 1)
y=0: OPEN  [1,3] (rect 2)
y=1: CLOSE [1,3] (rect 2)
y=2: CLOSE [0,2] (rect 0)
y=3: CLOSE [1,2] (rect 1)
```

### Processing:
```
y=0 to y=1:
  Coverage: [0,1]=1, [1,2]=3, [2,3]=1
  Length: (1-0) + (2-1) + (3-2) = 3
  Area: 3 × (1-0) = 3

y=1 to y=2:
  After CLOSE [1,3]: [0,1]=1, [1,2]=2, [2,3]=0
  Length: (1-0) + (2-1) = 2
  Area: 2 × (2-1) = 2

y=2 to y=3:
  After CLOSE [0,2]: [0,1]=0, [1,2]=1, [2,3]=0
  Length: (2-1) = 1
  Area: 1 × (3-2) = 1

Total: 3 + 2 + 1 = 6
```

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Sweep Line + Array | O(n² log n) | O(n) | Simple, good for n ≤ 200 |
| Sweep Line + Segment Tree | O(n log n) | O(n) | Optimal for large n |

## Edge Cases

1. **Single rectangle**: Just return its area modulo MOD
2. **Large coordinates**: Use coordinate compression
3. **Overlapping rectangles**: Coverage counting handles duplicates
4. **Adjacent rectangles**: Properly counted as separate areas
5. **Large area**: Result can exceed 10^18, must use modulo

## Common Mistakes

1. **Integer overflow**: Use `long long` for intermediate calculations
2. **Modulo operations**: Apply modulo correctly to avoid overflow
3. **Event ordering**: Process OPEN before CLOSE at same y-coordinate
4. **Coordinate compression**: Don't forget to map back to actual lengths
5. **Segment tree indexing**: Be careful with 0-based vs 1-based indexing

## Key Insights

1. **Sweep line**: Convert 2D problem to 1D by sweeping along one axis
2. **Coordinate compression**: Handle large coordinates by mapping to indices
3. **Event-based processing**: Track when rectangles start/end coverage
4. **Coverage counting**: Count overlapping rectangles instead of boolean coverage
5. **Segment tree**: Efficient range updates and queries

## Optimization Tips

1. **Use segment tree**: For O(log n) updates instead of O(n)
2. **Sort events once**: Avoid repeated sorting
3. **Process same-y events together**: Can batch updates
4. **Use `set` for deduplication**: Automatically sorts and removes duplicates

## Related Problems

- [218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) - Similar sweep line approach
- [391. Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/) - Rectangle coverage
- [836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) - Simpler overlap detection
- [223. Rectangle Area](https://leetcode.com/problems/rectangle-area/) - Two rectangles only

## Pattern Recognition

This problem demonstrates the **"Sweep Line with Segment Tree"** pattern:

```
1. Generate events (start/end of ranges)
2. Coordinate compress if needed
3. Sort events by sweep dimension
4. Use segment tree for efficient range updates
5. Calculate answer incrementally
```

Similar problems:
- Skyline Problem
- Interval Coverage
- Range Sum Queries with Updates

## Real-World Applications

1. **Computer Graphics**: Calculating visible areas
2. **GIS Systems**: Computing land coverage
3. **Collision Detection**: Finding overlapping regions
4. **Layout Algorithms**: Determining occupied space
5. **Map Rendering**: Tile coverage calculations

{% endraw %}

