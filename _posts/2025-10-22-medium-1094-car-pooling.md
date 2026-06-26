---
layout: post
title: "[Medium] 1094. Car Pooling"
date: 2025-10-22 13:30:00 -0700
categories: leetcode medium array sorting
permalink: /posts/2025-10-22-medium-1094-car-pooling/
tags: [leetcode, medium, array, sorting, simulation, bucket-sort]
---
**Difficulty:** Medium  
**Category:** Array, Sorting, Simulation  
**Companies:** Amazon, Google, Microsoft, Uber


There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengers, from, to]` indicates that the `i`-th trip has `numPassengers` passengers and the locations to pick them up and drop them off are `from` and `to` respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or `false` otherwise.

## Examples
**Example 1:**
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Explanation: 
- Trip 1: Pick up 2 passengers at location 1, drop off at location 5
- Trip 2: Pick up 3 passengers at location 3, drop off at location 5
- At location 3, we have 2 + 3 = 5 passengers, which exceeds capacity (4)
```

**Example 2:**
```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Explanation: 
- Trip 1: Pick up 2 passengers at location 1, drop off at location 5
- Trip 2: Pick up 3 passengers at location 3, drop off at location 5
- At location 3, we have 2 + 3 = 5 passengers, which equals capacity (5)
```

## Constraints
- `1 <= trips.length <= 1000`
- `trips[i].length == 3`
- `1 <= numPassengers <= 100`
- `0 <= from < to <= 1000`

## Solution Approaches

### Approach 1: Bucket Sort with Timestamps (Recommended)

**Key Insight:** Use a bucket array to track passenger changes at each timestamp. Add passengers at pickup locations and subtract at drop-off locations.

**Algorithm:**
1. Create a timestamp array of size 1001 (since locations are 0-1000)
2. For each trip, add passengers at pickup location and subtract at drop-off location
3. Iterate through timestamps and track cumulative passengers
4. Return false if capacity is exceeded at any point

**Time Complexity:** O(n + 1001) = O(n)  
**Space Complexity:** O(1001) = O(1)

```cpp
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<int> timestamp(1001);
        for(auto& trip: trips) {
            timestamp[trip[1]] += trip[0];  // Pick up passengers
            timestamp[trip[2]] -= trip[0];  // Drop off passengers
        }
        int usedCapacity = 0;
        for(int number: timestamp) {
            usedCapacity += number;
            if(usedCapacity > capacity) {
                return false;
            }
        }
        return true;
    }
};
```

### Solution Explanation

**Approach:** Prefix sum (this problem)

**Key idea:** Difficulty:** Medium

**How the code works:**
**Difficulty:** Medium
**Category:** Array, Sorting, Simulation
- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.

**Walkthrough** — input `trips = [[2,1,5],[3,3,7]], capacity = 4`, expected output `false`:

- Trip 1: Pick up 2 passengers at location 1, drop off at location 5
- Trip 2: Pick up 3 passengers at location 3, drop off at location 5
- At location 3, we have 2 + 3 = 5 passengers, which exceeds capacity (4)
## Implementation Details

### Bucket Sort Technique
```cpp
// Add passengers at pickup location
timestamp[trip[1]] += trip[0];
// Remove passengers at drop-off location  
timestamp[trip[2]] -= trip[0];
```

### Event Processing
```cpp
// Process events in chronological order
for(int number: timestamp) {
    usedCapacity += number;
    if(usedCapacity > capacity) return false;
}
```

## Edge Cases

1. **Single Trip**: `[[1,0,1]]` with capacity 1 → true
2. **No Trips**: `[]` with any capacity → true
3. **Exact Capacity**: Passengers exactly equal capacity → true
4. **Overlapping Trips**: Multiple trips at same location → check total

## Follow-up Questions

- What if locations could be very large (up to 10^9)?
- How would you handle multiple cars?
- What if passengers could be picked up and dropped off at the same location?
- How would you optimize for very large numbers of trips?

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [LC 253: Meeting Rooms II](https://www.leetcode.com/problems/meeting-rooms-ii/)
- [LC 218: The Skyline Problem](https://www.leetcode.com/problems/the-skyline-problem/)
- [LC 56: Merge Intervals](https://www.leetcode.com/problems/merge-intervals/)

## Optimization Techniques

1. **Bucket Sort**: Use array indexing for small ranges
2. **Event-Based Processing**: Treat state changes as events
3. **Early Termination**: Stop processing when constraint violated
4. **Space Optimization**: Use fixed-size arrays when possible

## Code Quality Notes

1. **Readability**: Bucket sort approach is most intuitive
2. **Performance**: O(n) time complexity is optimal
3. **Scalability**: Sorting approach works for any range
4. **Robustness**: All approaches handle edge cases correctly

## Key Takeaways

- **Pattern:** Prefix sum (this problem)
- Difficulty:** Medium
- Category:** Array, Sorting, Simulation

## References

- [LC 1094: Car Pooling on LeetCode](https://www.leetcode.com/problems/car-pooling/)
- [LeetCode Discuss — LC 1094: Car Pooling](https://www.leetcode.com/problems/car-pooling/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/car-pooling/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)

## Thinking Process

**Difficulty:** Medium

**Category:** Array, Sorting, Simulation

- Clarify if the array is sorted, has negatives, or allows duplicates.
- Prefix sums answer range queries; hash maps answer pair/count queries.
- In-place tricks use swap/write index instead of extra arrays.



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
| **Prefix sum** *(this problem)* | O(n) | O(n) | Range queries, subarray sum |
| Sort + scan | O(n log n) | O(1) | Intervals, meeting rooms |
| Kadane's algorithm | O(n) | O(1) | Maximum subarray |
| Hash map counting | O(n) | O(n) | Frequency, two-sum variants |
