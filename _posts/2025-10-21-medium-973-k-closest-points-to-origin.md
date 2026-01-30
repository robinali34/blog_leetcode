---
layout: post
title: "LC 973: K Closest Points to Origin"
date: 2025-10-21 15:30:00 -0700
categories: leetcode medium array sorting
permalink: /posts/2025-10-21-medium-973-k-closest-points-to-origin/
tags: [leetcode, medium, array, sorting, heap, quickselect]
---

# LC 973: K Closest Points to Origin

**Difficulty:** Medium  
**Category:** Array, Sorting, Heap, Quickselect  
**Companies:** Amazon, Google, Facebook, Microsoft

## Problem Statement

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√((x1 - x2)² + (y1 - y2)²)`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

### Examples

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

### Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Distance calculation**: How is distance calculated? (Assumption: Euclidean distance from origin - sqrt(x² + y²), can use squared distance for comparison)

2. **K closest**: What does "k closest" mean? (Assumption: K points with smallest distances to origin)

3. **Return format**: What should we return? (Assumption: Array of k closest points - can be in any order)

4. **Tie-breaking**: What if multiple points have same distance? (Assumption: Return any k points - order doesn't matter)

5. **K value**: What is the range of k? (Assumption: Per constraints, 1 <= k <= points.length)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Calculate the distance from origin for each point, sort all points by distance, and return the first k points. This approach has O(n log n) time complexity due to sorting, which works but is not optimal when k is much smaller than n.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a max-heap of size k: iterate through all points, calculate distances, and maintain a max-heap of the k smallest distances. When the heap size exceeds k, remove the maximum element. After processing all points, return the k points in the heap. This achieves O(n log k) time, which is better than sorting when k << n.

**Step 3: Optimized Solution (8 minutes)**

Use quickselect (partial sorting): use a partition-based algorithm similar to quicksort to find the k-th smallest distance. Partition the array so that the first k elements are the k smallest distances. Then return these k points. This achieves O(n) average time with O(1) space (if we modify the array in-place), which is optimal. Alternatively, the max-heap approach with O(n log k) is simpler to implement and has better worst-case guarantees. The key insight is that we don't need full sorting - we only need the k smallest elements, which can be found more efficiently.

## Solution Approach

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

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Best When |
|----------|-----------------|------------------|-----------|
| Sorting | O(n log n) | O(1) | General purpose, simple |
| Max Heap | O(n log k) | O(k) | k << n, memory constrained |
| Quickselect | O(n) avg | O(1) | Large datasets, k ≈ n |

## Key Insights

1. **Distance Simplification**: Use squared distance `x² + y²` instead of `√(x² + y²)` for comparison
2. **Sorting Trade-offs**: Simple but sorts all elements even when we only need k
3. **Heap Optimization**: Better when k is much smaller than n
4. **Quickselect Advantage**: Optimal average case but more complex implementation

## Follow-up Questions

- What if we need to handle dynamic updates (add/remove points)?
- How would you optimize for very large datasets that don't fit in memory?
- What if we need the k-th closest point in sorted order?

## Related Problems

- [LC 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [LC 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [LC 692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

---

*This problem demonstrates the importance of choosing the right data structure and algorithm based on the constraints and requirements.*
