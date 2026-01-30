---
layout: post
title: "[Hard] 218. The Skyline Problem"
date: 2025-10-05 00:00:00 -0000
categories: leetcode algorithm hard cpp sweep-line priority-queue data-structures union-find problem-solving
---

# [Hard] 218. The Skyline Problem

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Skyline definition**: What is a skyline? (Assumption: Outline formed by buildings - highest point at each x-coordinate)

2. **Building representation**: How are buildings represented? (Assumption: [left, right, height] - building spans from left to right with given height)

3. **Key points**: What are key points? (Assumption: Points where skyline height changes - [x, height] coordinates)

4. **Overlapping buildings**: How should we handle overlapping buildings? (Assumption: Take maximum height at each x-coordinate - skyline is union of building heights)

5. **Return format**: What should we return? (Assumption: List of key points [x, height] where skyline changes, sorted by x)

## Interview Deduction Process (30 minutes)

### Step 1: Brute-Force Approach (8 minutes)
**Initial Thought**: "I need to find skyline. Let me check height at each x-coordinate."

**Naive Solution**: For each x-coordinate, check all buildings that cover it, find maximum height. Add point when height changes.

**Complexity**: O(n × W) time where W is width range, O(n) space

**Issues**:
- Very inefficient for large coordinate ranges
- W can be up to 2^31
- Doesn't leverage building structure
- Timeout for large inputs

### Step 2: Semi-Optimized Approach (10 minutes)
**Insight**: "I can use sweep line algorithm. Process building start/end events, track active buildings."

**Improved Solution**: Create events for building start and end. Sort events by x-coordinate. Use map/priority queue to track active building heights. Update skyline when max height changes.

**Complexity**: O(n log n) time, O(n) space

**Improvements**:
- Sweep line is natural approach
- O(n log n) time is much better
- Handles all cases correctly
- Still can be optimized

### Step 3: Optimized Solution (12 minutes)
**Final Optimization**: "Sweep line with priority queue is optimal. Can optimize with coordinate compression if needed."

**Best Solution**: Sweep line with priority queue (max-heap) for active buildings. Process events sorted by x. When building starts, add to heap. When ends, mark for removal. Track max height changes.

**Complexity**: O(n log n) time, O(n) space

**Key Realizations**:
1. Sweep line is key technique for interval problems
2. Priority queue efficiently tracks max height
3. O(n log n) time is optimal for sorting events
4. Lazy removal from heap is efficient

## Approach

This is a classic sweep line algorithm problem. The key insight is to process all building edges (start and end points) in sorted order and maintain the current maximum height at each position.

There are several approaches to solve this problem:

1. **Coordinate Compression + Brute Force**: Compress coordinates and update heights for each building
2. **Sweep Line with Map**: Use events and maintain height counts
3. **Sweep Line with Priority Queue**: Use priority queue to track active buildings
4. **Sweep Line with Two Priority Queues**: Separate queues for active and past heights
5. **Union Find Optimization**: Use Union Find to optimize the coordinate compression approach

## Solution 1: Coordinate Compression + Brute Force

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

**Time Complexity:** O(n²) - For each building, we update all positions it covers
**Space Complexity:** O(n) - Edge set and height array

### How it works:
1. **Collect all unique x-coordinates** (building edges)
2. **Create mapping** from coordinate to index
3. **For each building**, update heights in the range [left, right)
4. **Generate skyline** by checking height changes

## Solution 2: Sweep Line with Map

```cpp
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> pairs;
        for(auto& b: buildings) {
            int left = b[0], right = b[1], height = b[2];
            pairs.emplace_back(left, -height);
            pairs.emplace_back(right, height);
        }
        sort(pairs.begin(), pairs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            if(a.first != b.first) return a.first < b.first;
            else return a.second < b.second;
        });
        vector<vector<int>> rtn;
        map<int, int> height_map;
        height_map[0] = 1;
        int pre = 0;
        for(auto& [x, h]: pairs) {
            if(h < 0) height_map[-h]++;
            else {
                height_map[h]--;
                if(height_map[h] == 0) height_map.erase(h);
            }
            int cur = height_map.rbegin()->first;
            if(cur != pre) {
                rtn.push_back({x, cur});
                pre = cur;
            }
        }
        return rtn;
    }
};
```

**Time Complexity:** O(n log n) - Sorting + map operations
**Space Complexity:** O(n) - Map and pairs vector

### How it works:
1. **Create events**: Start events with negative height, end events with positive height
2. **Sort events** by x-coordinate, then by height (negative heights first)
3. **Process events**: Add/remove heights from map
4. **Track maximum height** and add skyline points when it changes

## Solution 3: Sweep Line with Priority Queue

```cpp
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> edges;
        for(int i = 0; i < buildings.size(); i++) {
            edges.push_back({buildings[i][0], i});
            edges.push_back({buildings[i][1], i});
        }
        sort(edges.begin(), edges.end());
        priority_queue<pair<int, int>> live;
        vector<vector<int>> rtn;
        int idx = 0;
        while(idx < edges.size()) {
            int cur = edges[idx][0];
            while(idx < edges.size() && edges[idx][0] == cur) {
                int b = edges[idx][1];
                if(buildings[b][0] == cur) {
                    int right = buildings[b][1];
                    int height = buildings[b][2];
                    live.push({height, right});
                }
                idx += 1;
            }
            while(!live.empty() && live.top().second <= cur) live.pop();
            int curHeight = live.empty() ? 0: live.top().first;
            if(rtn.empty() || rtn[rtn.size() - 1][1] != curHeight) {
                rtn.push_back({cur, curHeight});
            }
        }
        return rtn;
    }
};
```

**Time Complexity:** O(n log n) - Sorting + priority queue operations
**Space Complexity:** O(n) - Priority queue and edges vector

### How it works:
1. **Create edge events** with building indices
2. **Sort edges** by x-coordinate
3. **Process events**: Add buildings to priority queue when they start
4. **Remove expired buildings** from priority queue
5. **Track maximum height** from active buildings

## Solution 4: Sweep Line with Two Priority Queues

```cpp
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> edges;
        for(auto& b: buildings) {
            edges.push_back({b[0], b[2]});
            edges.push_back({b[1], -b[2]});
        }
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] > b[1];
        });
        priority_queue<int> live;
        priority_queue<int> past;
        vector<vector<int>> rtn;
        int idx = 0;
        while(idx < edges.size()) {
            int cur = edges[idx][0];
            while(idx < edges.size() && edges[idx][0] == cur) {
                int height = edges[idx][1];
                if(height > 0) live.push(height);
                else past.push(-height);
                idx += 1;
            }
            while(!live.empty() && !past.empty() && live.top() == past.top()) {
                live.pop();
                past.pop();
            }
            int curHeight = live.empty() ? 0: live.top();
            if(rtn.empty() || rtn[rtn.size() - 1][1] != curHeight) {
                rtn.push_back({cur, curHeight});
            }
        }
        return rtn;
    }
};
```

**Time Complexity:** O(n log n) - Sorting + priority queue operations
**Space Complexity:** O(n) - Two priority queues

### How it works:
1. **Create events**: Start with positive height, end with negative height
2. **Sort events** by x-coordinate, then by height (descending)
3. **Use two priority queues**: One for active heights, one for past heights
4. **Remove matching heights** from both queues
5. **Track maximum active height**

## Solution 5: Union Find Optimization

```cpp
class UnionFind {
private:
    vector<int> root;
public:
    UnionFind(int n): root(n) {
        iota(root.begin(), root.end(), 0);
    }
    int find(int x) {
        if(root[x] != x) return find(root[x]);
        return root[x];
    }
    void merge(int x, int y) {
        root[find(x)] = find(y);
    }
};

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        sort(buildings.begin(), buildings.end(), [](auto& a, auto& b) {
            return a[2] > b[2];
        });
        set<int> edgeSet;
        for(auto& b: buildings) {
            edgeSet.insert(b[0]);
            edgeSet.insert(b[1]);
        }
        vector<int> edges(edgeSet.begin(), edgeSet.end());
        unordered_map<int, int> edgeIdxMap;
        for(int i = 0; i < edges.size(); i++) {
            edgeIdxMap[edges[i]] = i;
        }
        UnionFind uf(edges.size());
        vector<int> heights(edges.size());
        for(auto& b: buildings) {
            int left = b[0], right = b[1], height = b[2];
            int leftIdx = uf.find(edgeIdxMap[left]);
            int rightIdx = edgeIdxMap[right];
            while(leftIdx < rightIdx) {
                heights[leftIdx] = height;
                uf.merge(leftIdx, rightIdx);
                leftIdx = uf.find(++leftIdx);
            }
        }
        vector<vector<int>> rtn;
        for(int i = 0; i < edges.size(); i++) {
            if(i == 0 || heights[i] != heights[i - 1]) {
                rtn.push_back({edges[i], heights[i]});
            }
        }
        return rtn;
    }
};
```

**Time Complexity:** O(n²) in worst case, but optimized with Union Find
**Space Complexity:** O(n) - Union Find and height arrays

### How it works:
1. **Sort buildings** by height (descending)
2. **Process buildings** in height order
3. **Use Union Find** to skip already processed positions
4. **Update heights** only for unprocessed positions

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

## Edge Cases

1. **Single building**: `[[1,2,3]]` → `[[1,3],[2,0]]`
2. **Overlapping buildings**: Same height buildings
3. **Adjacent buildings**: Buildings touching at edges
4. **Large coordinates**: Integer overflow considerations
5. **Empty input**: Return empty skyline

## Related Problems

- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
- [715. Range Module](https://leetcode.com/problems/range-module/)
- [850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

## Conclusion

The Skyline Problem is a classic sweep line algorithm that tests understanding of:

1. **Event Processing**: Converting 2D problems to 1D events
2. **Data Structures**: Choosing appropriate structures for height tracking
3. **Algorithm Design**: Efficiently processing sorted events
4. **Edge Case Handling**: Managing height changes and duplicates

**Recommended Solution**: Solution 2 (Sweep Line with Map) offers the best balance of efficiency, clarity, and correctness for most scenarios.

The key insight is recognizing that skyline changes only occur at building edges, and we need to efficiently track the maximum height at each position while processing events in order.
