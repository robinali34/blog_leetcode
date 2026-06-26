---
layout: post
title: "[Hard] 218. The Skyline Problem"
date: 2025-10-05 00:00:00 -0000
categories: leetcode algorithm hard cpp sweep-line priority-queue data-structures union-find problem-solving
---
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array `buildings` where `buildings[i] = [lefti, righti, heighti]`:

- `lefti` is the x coordinate of the left edge of the ith building.
- `righti` is the x coordinate of the right edge of the ith building.
- `heighti` is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form `[[x1,y1],[x2,y2],...]`. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...[2 3],[4 5],[7 5],[11 5],[12 7]...]` is not acceptable; the three lines of height 5 should be merged into one: `[...[2 3],[4 5],[12 7]...]`

## Examples

**Example 1:**
```
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
```

**Example 2:**
```
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
```

## Constraints

- `1 <= buildings.length <= 10^4`
- `0 <= lefti < righti <= 2^31 - 1`
- `1 <= heighti <= 2^31 - 1`
- `buildings` is sorted by `lefti` in non-decreasing order.

## Thinking Process

This is a classic sweep line algorithm problem. The key insight is to process all building edges (start and end points) in sorted order and maintain the current maximum height at each position.

There are several approaches to solve this problem:

1. **Coordinate Compression + Brute Force**: Compress coordinates and update heights for each building
2. **Sweep Line with Map**: Use events and maintain height counts
3. **Sweep Line with Priority Queue**: Use priority queue to track active buildings
4. **Sweep Line with Two Priority Queues**: Separate queues for active and past heights
5. **Union Find Optimization**: Use Union Find to optimize the coordinate compression approach



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

```cpp
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        set<int> edgeSet;
        for(auto& building: buildings) {
            int left = building[0], right = building[1];
            edgeSet.insert(left);
            edgeSet.insert(right);
        }
        vector<int> edges(edgeSet.begin(), edgeSet.end());
        map<int, int> edgeIdxMap;
        for(int i = 0; i < edges.size(); i++) {
            edgeIdxMap[edges[i]] = i;
        }
        vector<int> heights(edges.size());
        for(auto& building :buildings) {
            int left = building[0], right = building[1], height = building[2];
            int leftIdx = edgeIdxMap[left], rightIdx = edgeIdxMap[right];
            for(int idx = leftIdx; idx < rightIdx; idx++) {
                heights[idx] = max(heights[idx], height);
            }
        }
        vector<vector<int>> rtn;
        for(int i = 0; i < heights.size(); i++) {
            int curHeight = heights[i], curPos = edges[i];
            if(i == 0 || curHeight != heights[i - 1]) {
                rtn.push_back({curPos, curHeight});
            }
        }
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Brute force (this problem)

**Key idea:** This is a classic sweep line algorithm problem. The key insight is to process all building edges (start and end points) in sorted order and maintain the current maximum height at each position.

**How the code works:**
1. **Coordinate Compression + Brute Force**: Compress coordinates and update heights for each building
2. **Sweep Line with Map**: Use events and maintain height counts
3. **Sweep Line with Priority Queue**: Use priority queue to track active buildings
4. **Sweep Line with Two Priority Queues**: Separate queues for active and past heights
5. **Union Find Optimization**: Use Union Find to optimize the coordinate compression approach

**Walkthrough** — input `buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]`, expected output `[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]`:

Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
## Step-by-Step Example (Solution 2)

Let's trace through `buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]`:

### Create Events:
```
(2, -10), (9, 10)   // Building 1: height 10
(3, -15), (7, 15)   // Building 2: height 15  
(5, -12), (12, 12)  // Building 3: height 12
(15, -10), (20, 10) // Building 4: height 10
(19, -8), (24, 8)   // Building 5: height 8
```

### Sort Events:
```
(2, -10), (3, -15), (5, -12), (7, 15), (9, 10), (12, 12), (15, -10), (19, -8), (20, 10), (24, 8)
```

### Process Events:
1. **x=2**: Add height 10 → max=10 → add [2,10]
2. **x=3**: Add height 15 → max=15 → add [3,15]
3. **x=5**: Add height 12 → max=15 → no change
4. **x=7**: Remove height 15 → max=12 → add [7,12]
5. **x=9**: Remove height 10 → max=12 → no change
6. **x=12**: Remove height 12 → max=0 → add [12,0]
7. **x=15**: Add height 10 → max=10 → add [15,10]
8. **x=19**: Add height 8 → max=10 → no change
9. **x=20**: Remove height 10 → max=8 → add [20,8]
10. **x=24**: Remove height 8 → max=0 → add [24,0]

### Result: `[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]`

## Algorithm Analysis

### Solution Comparison:

| Solution | Time Complexity | Space Complexity | Approach | Pros | Cons |
|----------|----------------|-----------------|----------|------|------|
| Coordinate Compression | O(n²) | O(n) | Brute Force | Simple logic | Inefficient |
| Sweep Line + Map | O(n log n) | O(n) | Event Processing | Clean, efficient | Map overhead |
| Sweep Line + PQ | O(n log n) | O(n) | Priority Queue | Intuitive | PQ cleanup needed |
| Two Priority Queues | O(n log n) | O(n) | Dual PQ | Handles duplicates | More complex |
| Union Find | O(n²) worst | O(n) | Optimization | Skips processed | Complex implementation |

### Key Insights:

1. **Event Processing**: Convert buildings to start/end events
2. **Height Tracking**: Maintain current maximum height efficiently
3. **Change Detection**: Only add skyline points when height changes
4. **Coordinate Handling**: Process events in sorted order
5. **Data Structure Choice**: Map vs Priority Queue trade-offs

## Common Mistakes

1. **Not handling height changes correctly** - Only add points when height changes
2. **Incorrect event sorting** - Must handle ties properly
3. **Memory management** - Clean up expired buildings from priority queue
4. **Edge cases** - Handle empty buildings, single building scenarios
5. **Coordinate precision** - Handle large coordinate values

1. **Single building**: `[[1,2,3]]` → `[[1,3],[2,0]]`
2. **Overlapping buildings**: Same height buildings
3. **Adjacent buildings**: Buildings touching at edges
4. **Large coordinates**: Integer overflow considerations
5. **Empty input**: Return empty skyline

## Key Takeaways

- **Pattern:** Brute force (this problem)

## References

- [LC 218: The Skyline Problem on LeetCode](https://www.leetcode.com/problems/skyline-problem/)
- [LeetCode Discuss — LC 218: The Skyline Problem](https://www.leetcode.com/problems/skyline-problem/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/skyline-problem/editorial/) *(may require premium)*

## Related Problems

- [253. Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/)
- [56. Merge Intervals](https://www.leetcode.com/problems/merge-intervals/)
- [57. Insert Interval](https://www.leetcode.com/problems/insert-interval/)
- [715. Range Module](https://www.leetcode.com/problems/range-module/)
- [850. Rectangle Area II](https://www.leetcode.com/problems/rectangle-area-ii/)

## Conclusion

The Skyline Problem is a classic sweep line algorithm that tests understanding of:

1. **Event Processing**: Converting 2D problems to 1D events
2. **Data Structures**: Choosing appropriate structures for height tracking
3. **Algorithm Design**: Efficiently processing sorted events
4. **Edge Case Handling**: Managing height changes and duplicates

**Recommended Solution**: Solution 2 (Sweep Line with Map) offers the best balance of efficiency, clarity, and correctness for most scenarios.

The key insight is recognizing that skyline changes only occur at building edges, and we need to efficiently track the maximum height at each position while processing events in order.
