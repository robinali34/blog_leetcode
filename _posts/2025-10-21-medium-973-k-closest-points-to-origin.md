---
layout: post
title: "[Medium] 973. K Closest Points to Origin"
date: 2025-10-21 15:30:00 -0700
categories: leetcode medium array sorting
permalink: /posts/2025-10-21-medium-973-k-closest-points-to-origin/
tags: [leetcode, medium, array, sorting, heap, quickselect]
---
**Difficulty:** Medium  
**Category:** Array, Sorting, Heap, Quickselect  
**Companies:** Amazon, Google, Facebook, Microsoft


Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√((x1 - x2)² + (y1 - y2)²)`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

## Examples
**Example 1:**
```
Input: points = [[1,1],[2,2],[3,3]], k = 1
Output: [[1,1]]
Explanation:
The distance between (1, 1) and the origin is sqrt(2).
The distance between (2, 2) and the origin is sqrt(8).
The distance between (3, 3) and the origin is sqrt(18).
Since sqrt(2) < sqrt(8) < sqrt(18), we return [[1,1]].
```

**Example 2:**
```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

## Constraints
- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Min/max heap** *(this problem)* | $O(n \log k)$ | $O(k)$ | Top-K, streaming median |
| Two heaps | $O(n \log n)$ | $O(n)$ | Median from data stream |
| Heap + lazy deletion | $O(n \log n)$ | $O(n)$ | Delayed removal |
| Priority-driven search | $O(n \log n)$ | $O(n)$ | Dijkstra, best-first expansion |

## Thinking Process

### Key Insight

Since we're finding the distance to the origin `(0, 0)`, we can simplify the distance calculation:
- **Euclidean distance**: `√(x² + y²)`
- **For comparison**: We can use `x² + y²` instead of `√(x² + y²)` since square root is monotonically increasing
- **Manhattan distance approximation**: `|x| + |y|` (not exact but useful for some optimizations)

### Approach 1: Sorting (Recommended)

**Algorithm:**
1. Sort all points by their squared distance to origin
2. Return the first `k` points

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1) (excluding output)

```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b){
            return (a[0] * a[0] + a[1] * a[1]) < (b[0] * b[0] + b[1] * b[1]);
        });
        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
};
```

### Approach 2: Max Heap

**Algorithm:**
1. Use a max heap to maintain the `k` closest points
2. For each point, if heap size < k, add it
3. If heap size = k and current point is closer than farthest in heap, replace it

**Time Complexity:** O(n log k)  
**Space Complexity:** O(k)

```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> maxHeap;
        
        for(auto& point : points) {
            int dist = point[0] * point[0] + point[1] * point[1];
            if(maxHeap.size() < k) {
                maxHeap.push({dist, point});
            } else if(dist < maxHeap.top().first) {
                maxHeap.pop();
                maxHeap.push({dist, point});
            }
        }
        
        vector<vector<int>> result;
        while(!maxHeap.empty()) {
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return result;
    }
};
```

### Approach 3: Quickselect (Optimal for Large k)

**Algorithm:**
1. Use quickselect to find the k-th smallest distance
2. Partition points around this distance
3. Return first k points

**Time Complexity:** O(n) average, O(n²) worst case  
**Space Complexity:** O(1)

```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        int left = 0, right = points.size() - 1;
        
        while(left <= right) {
            int pivotIndex = partition(points, left, right);
            if(pivotIndex == k) break;
            else if(pivotIndex < k) left = pivotIndex + 1;
            else right = pivotIndex - 1;
        }
        
        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
    
private:
    int partition(vector<vector<int>>& points, int left, int right) {
        int pivotDist = getDistance(points[right]);
        int i = left;
        
        for(int j = left; j < right; j++) {
            if(getDistance(points[j]) <= pivotDist) {
                swap(points[i], points[j]);
                i++;
            }
        }
        swap(points[i], points[right]);
        return i;
    }
    
    int getDistance(const vector<int>& point) {
        return point[0] * point[0] + point[1] * point[1];
    }
};
```

### Complexity
| Approach | Time Complexity | Space Complexity | Best When |
|----------|-----------------|------------------|-----------|
| Sorting | O(n log n) | O(1) | General purpose, simple |
| Max Heap | O(n log k) | O(k) | k << n, memory constrained |
| Quickselect | O(n) avg | O(1) | Large datasets, k ≈ n |



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 120" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Binary heap</text>

  <circle cx="140" cy="35" r="16" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="39" text-anchor="middle" font-size="11">1</text>
  <circle cx="90" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="90" y="79" text-anchor="middle" font-size="10">3</text>
  <circle cx="190" cy="75" r="14" fill="#D4D8E0" stroke="#8B8680"/><text x="190" y="79" text-anchor="middle" font-size="10">2</text>
  <line x1="140" y1="51" x2="90" y2="61" stroke="#9A9792"/><line x1="140" y1="51" x2="190" y2="61" stroke="#9A9792"/>
  <text x="140" y="110" text-anchor="middle" font-size="11" fill="#6B6560">parent ≤ children (min-heap)</text>

</svg>

## Follow-up Questions

- What if we need to handle dynamic updates (add/remove points)?
- How would you optimize for very large datasets that don't fit in memory?
- What if we need the k-th closest point in sorted order?

## Related Problems

- [LC 215: Kth Largest Element in an Array](https://www.leetcode.com/problems/kth-largest-element-in-an-array/)
- [LC 347: Top K Frequent Elements](https://www.leetcode.com/problems/top-k-frequent-elements/)
- [LC 692: Top K Frequent Words](https://www.leetcode.com/problems/top-k-frequent-words/)

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Distance Simplification**: Use squared distance `x² + y²` instead of `√(x² + y²)` for comparison
2. **Sorting Trade-offs**: Simple but sorts all elements even when we only need k
3. **Heap Optimization**: Better when k is much smaller than n
4. **Quickselect Advantage**: Optimal average case but more complex implementation

## References

- [LC 973: K Closest Points to Origin on LeetCode](https://www.leetcode.com/problems/k-closest-points-to-origin/)
- [LeetCode Discuss — LC 973: K Closest Points to Origin](https://www.leetcode.com/problems/k-closest-points-to-origin/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/k-closest-points-to-origin/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
