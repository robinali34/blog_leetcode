---
layout: post
title: "[Medium] 406. Queue Reconstruction by Height"
date: 2025-10-19 11:16:19 -0700
categories: leetcode algorithm medium cpp greedy sorting list problem-solving
---

# [Medium] 406. Queue Reconstruction by Height

You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [hi, ki]` represents the `ith` person of height `hi` with exactly `ki` other people who have a height greater than or equal to `hi` in front of them.

Write an algorithm to reconstruct the queue.

## Examples

**Example 1:**
```
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no one taller or equal in front of them.
Person 1 has height 7 with no one taller or equal in front of them.
Person 2 has height 5 with two people taller or equal in front of them.
Person 3 has height 6 with one person taller or equal in front of them.
Person 4 has height 4 with four people taller or equal in front of them.
Person 5 has height 7 with one person taller or equal in front of them.
```

**Example 2:**
```
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
Explanation:
Person 0 has height 4 with no one taller or equal in front of them.
Person 1 has height 5 with no one taller or equal in front of them.
Person 2 has height 2 with two people taller or equal in front of them.
Person 3 has height 3 with two people taller or equal in front of them.
Person 4 has height 1 with four people taller or equal in front of them.
Person 5 has height 6 with no one taller or equal in front of them.
```

## Constraints

- `1 <= people.length <= 2000`
- `0 <= hi <= 10^6`
- `0 <= ki < people.length`
- It is guaranteed that the queue can be reconstructed.

## Solution: Greedy Sorting with List Insertion

**Time Complexity:** O(n²) where n is the number of people  
**Space Complexity:** O(n) for the result list

Sort people by height (descending) and k-value (ascending), then insert each person at the k-th position using a list for efficient insertion.

```cpp
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        /*
        1. Sort by height (descending), then by k-value (ascending)
        2. Insert each person at the k-th position
        3. Use list for efficient insertion at arbitrary positions
        */

        sort(people.begin(), people.end(), [](const vector<int> & a, const vector<int>& b) {
            if(a[0] == b[0]) return a[1] < b[1];  // Same height: sort by k-value
            return a[0] > b[0];                    // Different height: sort by height
        });

        list<vector<int>> rtn;
        for(auto& person: people) {
            auto it = rtn.begin();
            advance(it, person[1]);  // Move iterator to k-th position
            rtn.insert(it, person);
        }
        
        return vector<vector<int>>(rtn.begin(), rtn.end());
    }
};
```

## How the Algorithm Works

**Key Insight:** Sort people by height (descending) and k-value (ascending), then insert each person at the k-th position.

**Steps:**
1. **Sort people** by height (descending) and k-value (ascending)
2. **Use list** for efficient insertion at arbitrary positions
3. **For each person:**
   - Move iterator to k-th position
   - Insert person at that position
4. **Convert list** to vector and return

## Step-by-Step Example

### Example: `people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`

**Step 1: Sort by height (descending) and k-value (ascending)**
```
Original: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Sorted:   [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
```

**Step 2: Insert each person at k-th position**

| Person | Height | K | List State | Insertion Position |
|--------|--------|---|------------|-------------------|
| [7,0] | 7 | 0 | [] | Position 0 → [[7,0]] |
| [7,1] | 7 | 1 | [[7,0]] | Position 1 → [[7,0],[7,1]] |
| [6,1] | 6 | 1 | [[7,0],[7,1]] | Position 1 → [[7,0],[6,1],[7,1]] |
| [5,0] | 5 | 0 | [[7,0],[6,1],[7,1]] | Position 0 → [[5,0],[7,0],[6,1],[7,1]] |
| [5,2] | 5 | 2 | [[5,0],[7,0],[6,1],[7,1]] | Position 2 → [[5,0],[7,0],[5,2],[6,1],[7,1]] |
| [4,4] | 4 | 4 | [[5,0],[7,0],[5,2],[6,1],[7,1]] | Position 4 → [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] |

**Final result:** `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`

## Algorithm Breakdown

### Sorting Logic:
```cpp
sort(people.begin(), people.end(), [](const vector<int> & a, const vector<int>& b) {
    if(a[0] == b[0]) return a[1] < b[1];  // Same height: sort by k-value
    return a[0] > b[0];                    // Different height: sort by height
});
```

**Process:**
1. **Primary sort:** By height (descending)
2. **Secondary sort:** By k-value (ascending) for same height
3. **Result:** Tallest people first, then by k-value

### Insertion Logic:
```cpp
for(auto& person: people) {
    auto it = rtn.begin();
    advance(it, person[1]);  // Move iterator to k-th position
    rtn.insert(it, person);
}
```

**Process:**
1. **Start iterator** at beginning of list
2. **Advance iterator** to k-th position
3. **Insert person** at that position
4. **Repeat** for all people

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sorting | O(n log n) | O(1) |
| Insertion | O(n²) | O(n) |
| **Total** | **O(n²)** | **O(n)** |

Where n is the number of people.

## Edge Cases

1. **Single person:** `people = [[5,0]]` → `[[5,0]]`
2. **All same height:** `people = [[5,0],[5,1],[5,2]]` → `[[5,0],[5,1],[5,2]]`
3. **All k=0:** `people = [[7,0],[6,0],[5,0]]` → `[[5,0],[6,0],[7,0]]`
4. **Maximum k:** `people = [[1,2]]` → `[[1,2]]`

## Key Insights

### Greedy Strategy:
1. **Tallest first:** Process tallest people first
2. **K-value ordering:** For same height, process by k-value
3. **Insertion order:** Insert at k-th position
4. **Optimal result:** Always produces correct reconstruction

### Why This Works:
1. **Tallest people:** Can be placed anywhere without affecting others
2. **K-value constraint:** Each person needs exactly k taller people in front
3. **Insertion order:** Maintains the constraint for all people
4. **List efficiency:** O(1) insertion at arbitrary positions

## Detailed Example Walkthrough

### Example: `people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]`

**Step 1: Sort by height (descending) and k-value (ascending)**
```
Original: [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Sorted:   [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
```

**Step 2: Insert each person at k-th position**

| Person | Height | K | List State | Insertion Position |
|--------|--------|---|------------|-------------------|
| [6,0] | 6 | 0 | [] | Position 0 → [[6,0]] |
| [5,0] | 5 | 0 | [[6,0]] | Position 0 → [[5,0],[6,0]] |
| [4,0] | 4 | 0 | [[5,0],[6,0]] | Position 0 → [[4,0],[5,0],[6,0]] |
| [3,2] | 3 | 2 | [[4,0],[5,0],[6,0]] | Position 2 → [[4,0],[5,0],[3,2],[6,0]] |
| [2,2] | 2 | 2 | [[4,0],[5,0],[3,2],[6,0]] | Position 2 → [[4,0],[5,0],[2,2],[3,2],[6,0]] |
| [1,4] | 1 | 4 | [[4,0],[5,0],[2,2],[3,2],[6,0]] | Position 4 → [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]] |

**Final result:** `[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]`

## Alternative Approaches

### Approach 1: Vector with Insertion
```cpp
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](const vector<int>& a, const vector<int>& b) {
            if(a[0] == b[0]) return a[1] < b[1];
            return a[0] > b[0];
        });
        
        vector<vector<int>> result;
        for(auto& person: people) {
            result.insert(result.begin() + person[1], person);
        }
        
        return result;
    }
};
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

### Approach 2: Priority Queue
```cpp
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        priority_queue<pair<int, int>> pq;
        for(auto& person: people) {
            pq.push({person[0], person[1]});
        }
        
        vector<vector<int>> result;
        while(!pq.empty()) {
            auto [h, k] = pq.top();
            pq.pop();
            result.insert(result.begin() + k, {h, k});
        }
        
        return result;
    }
};
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

## Common Mistakes

1. **Wrong sorting order:** Not sorting by height descending first
2. **Incorrect k-value handling:** Not considering k-value for same height
3. **Wrong insertion position:** Inserting at wrong index
4. **Data structure choice:** Using vector instead of list for insertion

## Related Problems

- [135. Candy](https://leetcode.com/problems/candy/)
- [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

## Why This Solution Works

### Greedy Strategy:
1. **Tallest first:** Process tallest people first
2. **K-value ordering:** For same height, process by k-value
3. **Insertion order:** Insert at k-th position
4. **Optimal result:** Always produces correct reconstruction

### List Efficiency:
1. **O(1) insertion:** Insert at arbitrary positions
2. **Iterator advancement:** Efficient position finding
3. **Memory efficient:** No extra space for insertion
4. **Optimal performance:** Better than vector insertion

### Key Algorithm Properties:
1. **Correctness:** Always produces valid reconstruction
2. **Optimality:** Produces correct queue order
3. **Efficiency:** O(n²) time complexity
4. **Simplicity:** Easy to understand and implement
