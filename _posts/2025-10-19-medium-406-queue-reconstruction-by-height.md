---
layout: post
title: "[Medium] 406. Queue Reconstruction by Height"
date: 2025-10-19 11:16:19 -0700
categories: leetcode algorithm medium cpp greedy sorting list problem-solving
---
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

## Thinking Process

1. **Tallest first:** Process tallest people first
1. **Tallest people:** Can be placed anywhere without affecting others

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

## Solution

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

### Solution Explanation
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

### Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sorting | O(n log n) | O(1) |
| Insertion | O(n²) | O(n) |
| **Total** | **O(n²)** | **O(n)** |

Where n is the number of people.

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

## Common Mistakes

1. **Single person:** `people = [[5,0]]` → `[[5,0]]`
2. **All same height:** `people = [[5,0],[5,1],[5,2]]` → `[[5,0],[5,1],[5,2]]`
3. **All k=0:** `people = [[7,0],[6,0],[5,0]]` → `[[5,0],[6,0],[7,0]]`
4. **Maximum k:** `people = [[1,2]]` → `[[1,2]]`

1. **Wrong sorting order:** Not sorting by height descending first
2. **Incorrect k-value handling:** Not considering k-value for same height
3. **Wrong insertion position:** Inserting at wrong index
4. **Data structure choice:** Using vector instead of list for insertion

## Related Problems

- [135. Candy](https://www.leetcode.com/problems/candy/)
- [455. Assign Cookies](https://www.leetcode.com/problems/assign-cookies/)
- [621. Task Scheduler](https://www.leetcode.com/problems/task-scheduler/)
- [435. Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/)

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

## References

- [LC 406: Queue Reconstruction by Height on LeetCode](https://www.leetcode.com/problems/queue-reconstruction-by-height/)
- [LeetCode Discuss — LC 406: Queue Reconstruction by Height](https://www.leetcode.com/problems/queue-reconstruction-by-height/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/queue-reconstruction-by-height/editorial/) *(may require premium)*

## Key Takeaways

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
