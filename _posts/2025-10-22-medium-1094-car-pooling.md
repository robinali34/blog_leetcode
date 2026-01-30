---
layout: post
title: "LC 1094: Car Pooling"
date: 2025-10-22 13:30:00 -0700
categories: leetcode medium array sorting
permalink: /posts/2025-10-22-medium-1094-car-pooling/
tags: [leetcode, medium, array, sorting, simulation, bucket-sort]
---

# LC 1094: Car Pooling

**Difficulty:** Medium  
**Category:** Array, Sorting, Simulation  
**Companies:** Amazon, Google, Microsoft, Uber

## Problem Statement

There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengers, from, to]` indicates that the `i`-th trip has `numPassengers` passengers and the locations to pick them up and drop them off are `from` and `to` respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or `false` otherwise.

### Examples

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

### Constraints

- `1 <= trips.length <= 1000`
- `trips[i].length == 3`
- `1 <= numPassengers <= 100`
- `0 <= from < to <= 1000`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Trip format**: How are trips represented? (Assumption: [numPassengers, from, to] - pick up numPassengers at location from, drop off at location to)

2. **Capacity check**: What are we checking? (Assumption: Whether car can accommodate all passengers at all locations without exceeding capacity)

3. **Return value**: What should we return? (Assumption: Boolean - true if all trips can be completed, false if capacity exceeded)

4. **Location order**: Are locations in order? (Assumption: No - trips can be in any order, need to track passengers at each location)

5. **Pickup/dropoff**: When do passengers get on/off? (Assumption: Pick up at "from" location, drop off at "to" location)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For each location from 0 to the maximum location, calculate how many passengers are in the car at that location. For each location, iterate through all trips: if trip.from <= location < trip.to, add passengers. Check if total exceeds capacity at any location. This approach has O(max_location × trips) complexity, which can be slow if locations span a large range.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a difference array (sweep line technique). For each trip, increment passenger count at "from" location and decrement at "to" location. Then iterate through locations in order, maintaining a running sum of passengers. Check if running sum exceeds capacity at any point. This reduces to O(max_location + trips) time, which is better but still depends on the location range.

**Step 3: Optimized Solution (8 minutes)**

Use a map (ordered map) to store location → delta passenger changes. For each trip, add +passengers at "from" and -passengers at "to". Then iterate through map entries in sorted order, maintaining a running sum. Check if running sum exceeds capacity. This achieves O(trips log trips) time for sorting events plus O(trips) for processing. The map automatically handles coordinate compression and sorting, making it efficient even for sparse location ranges. Alternatively, if location range is small, use an array directly.

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

### Approach 2: Sorting with Events

**Algorithm:**
1. Create events for pickup and drop-off
2. Sort events by location
3. Process events in order and track passengers
4. Return false if capacity exceeded

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        vector<pair<int, int>> events;  // {location, passenger_change}
        
        for(auto& trip: trips) {
            events.push_back({trip[1], trip[0]});   // Pick up
            events.push_back({trip[2], -trip[0]});  // Drop off
        }
        
        sort(events.begin(), events.end());
        
        int usedCapacity = 0;
        for(auto& event: events) {
            usedCapacity += event.second;
            if(usedCapacity > capacity) {
                return false;
            }
        }
        return true;
    }
};
```

### Approach 3: Simulation with Priority Queue

**Algorithm:**
1. Sort trips by pickup location
2. Use priority queue to track active trips
3. Process trips in order and manage drop-offs
4. Check capacity at each pickup

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        sort(trips.begin(), trips.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];  // Sort by pickup location
        });
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        int usedCapacity = 0;
        
        for(auto& trip: trips) {
            int passengers = trip[0];
            int pickup = trip[1];
            int dropoff = trip[2];
            
            // Drop off passengers who have reached their destination
            while(!pq.empty() && pq.top().first <= pickup) {
                usedCapacity -= pq.top().second;
                pq.pop();
            }
            
            // Pick up new passengers
            usedCapacity += passengers;
            if(usedCapacity > capacity) {
                return false;
            }
            
            // Add drop-off event
            pq.push({dropoff, passengers});
        }
        
        return true;
    }
};
```

## Algorithm Analysis

### Approach Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Bucket Sort | O(n) | O(1) | Optimal, simple | Limited to small ranges |
| Sorting Events | O(n log n) | O(n) | General purpose | More complex |
| Priority Queue | O(n log n) | O(n) | Handles complex cases | Overkill for this problem |

### Key Insights

1. **Bucket Sort Advantage**: Most efficient for small, bounded ranges
2. **Event Processing**: Treat pickup and drop-off as separate events
3. **Cumulative Tracking**: Track running total of passengers
4. **Early Termination**: Stop as soon as capacity is exceeded

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

## Related Problems

- [LC 253: Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [LC 218: The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
- [LC 56: Merge Intervals](https://leetcode.com/problems/merge-intervals/)

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

---

*This problem demonstrates the power of bucket sort for small, bounded ranges and shows how event-based processing can simplify complex simulation problems.*
