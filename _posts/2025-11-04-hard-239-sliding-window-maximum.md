---
layout: post
title: "[Hard] 239. Sliding Window Maximum"
date: 2025-11-04 21:22:32 -0800
categories: leetcode algorithm hard cpp arrays deque sliding-window monotonic-queue problem-solving
permalink: /posts/2025-11-04-hard-239-sliding-window-maximum/
tags: [leetcode, hard, array, deque, sliding-window, monotonic-queue]
---

# [Hard] 239. Sliding Window Maximum

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

## Examples

**Example 1:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Window definition**: What is a sliding window? (Assumption: Contiguous subarray of size k that moves from left to right)

2. **Maximum calculation**: What should we return for each window? (Assumption: Maximum element in the current window)

3. **Return format**: What should we return? (Assumption: Array of maximums - one for each window position)

4. **Window count**: How many windows are there? (Assumption: nums.length - k + 1 windows - from index 0 to nums.length - k)

5. **Time complexity**: What time complexity is expected? (Assumption: O(n) - linear time using monotonic deque)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

For each window position, scan through all k elements in that window to find the maximum. This straightforward approach has O(n × k) time complexity, which becomes O(n²) when k ≈ n. For n up to 10^5, this is too slow. The challenge is that we're recalculating the maximum for overlapping windows inefficiently.

**Step 2: Semi-Optimized Approach (10 minutes)**

Use a balanced BST or multiset to maintain elements in the current window. When sliding the window, remove the leftmost element and add the rightmost element, then query the maximum. This gives O(n log k) time complexity, which is better but not optimal. Alternatively, use a max-heap, but removing arbitrary elements (the leftmost element leaving the window) is inefficient in a heap, requiring O(k) time to find and remove.

**Step 3: Optimized Solution (12 minutes)**

Use a monotonic deque (double-ended queue) that maintains indices of elements in decreasing order of their values. The front of the deque always contains the index of the maximum element in the current window. When adding a new element, remove all indices from the back whose values are smaller (they can never be the maximum). When the front index is outside the window, remove it. This achieves O(n) time because each element is added and removed at most once. The key insight is that if a new element is larger than previous elements, those previous elements can never be the maximum in any future window containing the new element, so we can safely remove them.

## Solution: Monotonic Deque (Decreasing Order)

**Time Complexity:** O(n) - Each element is added and removed at most once  
**Space Complexity:** O(k) - Deque stores at most k elements

Use a deque (double-ended queue) to maintain indices of elements in decreasing order of their values. This allows O(1) access to the maximum element in the current window.

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> rtn;
        deque<int> q;
        
        for(int i = 0; i < (int)nums.size(); i++) {
            // Remove indices outside the current window
            while(!q.empty() && q.front() < i - k + 1) {
                q.pop_front();
            }
            
            // Remove indices whose values are smaller than current element
            // (they can never be the maximum)
            while(!q.empty() && nums[q.back()] < nums[i]) {
                q.pop_back();
            }
            
            q.push_back(i);
            
            // Add maximum when window is complete
            if(i >= k - 1) {
                rtn.push_back(nums[q.front()]);
            }
        }
        
        return rtn;
    }
};
```

## How the Algorithm Works

### Key Insight: Monotonic Deque

The deque maintains indices of elements in **decreasing order of their values**. This means:
- `q.front()` always points to the index of the maximum element in the current window
- Elements with smaller values that come before larger values are removed (they can never be maximum)
- We remove indices that are outside the current window

### Step-by-Step Example: `nums = [1,3,-1,-3,5,3,6,7], k = 3`

| Step | i | nums[i] | Deque (indices) | Window | Max | Action |
|------|---|---------|------------------|--------|-----|--------|
| 0 | 0 | 1 | [0] | [1] | - | Add index 0 |
| 1 | 1 | 3 | [1] | [1,3] | - | Remove 0 (nums[0]=1 < 3), add 1 |
| 2 | 2 | -1 | [1,2] | [1,3,-1] | 3 | Add 2, window complete → nums[1]=3 |
| 3 | 3 | -3 | [1,2,3] | [3,-1,-3] | 3 | Remove 0 from front (out of window), add 3 → nums[1]=3 |
| 4 | 4 | 5 | [4] | [-1,-3,5] | 5 | Remove 1,2,3 (smaller values), add 4 → nums[4]=5 |
| 5 | 5 | 3 | [4,5] | [-3,5,3] | 5 | Add 5, keep 4 (5 > 3) → nums[4]=5 |
| 6 | 6 | 6 | [6] | [5,3,6] | 6 | Remove 4,5 (smaller values), add 6 → nums[6]=6 |
| 7 | 7 | 7 | [7] | [3,6,7] | 7 | Remove 6 (out of window), add 7 → nums[7]=7 |

**Final Answer:** `[3,3,5,5,6,7]`

### Visual Representation

```
nums = [1, 3, -1, -3, 5, 3, 6, 7]
       0  1   2    3   4  5  6  7

Window 1: [1, 3, -1]     → max = 3
Window 2: [3, -1, -3]    → max = 3
Window 3: [-1, -3, 5]    → max = 5
Window 4: [-3, 5, 3]     → max = 5
Window 5: [5, 3, 6]      → max = 6
Window 6: [3, 6, 7]      → max = 7

Deque state at each step (showing indices and values):
Step 0: [0:1]
Step 1: [1:3]           (removed 0 because 1 < 3)
Step 2: [1:3, 2:-1]     (window complete, max = 3)
Step 3: [1:3, 2:-1, 3:-3]  (max = 3)
Step 4: [4:5]           (removed 1,2,3 because all < 5)
Step 5: [4:5, 5:3]      (max = 5)
Step 6: [6:6]           (removed 4,5 because < 6)
Step 7: [7:7]           (removed 6, max = 7)
```

## Key Insights

1. **Monotonic Deque**: Maintain indices in decreasing order of values
2. **Remove Out-of-Window**: Remove indices `i - k + 1` from the front
3. **Remove Smaller Elements**: Remove indices whose values are smaller than current (they can never be maximum)
4. **Front is Maximum**: `q.front()` always points to the maximum element in current window
5. **Amortized O(1)**: Each element is added and removed at most once

## Algorithm Breakdown

### 1. Initialize
```cpp
vector<int> rtn;
deque<int> q;
```
- `rtn`: Result array to store maximums
- `q`: Deque storing indices in decreasing order of values

### 2. Remove Out-of-Window Indices
```cpp
while(!q.empty() && q.front() < i - k + 1) {
    q.pop_front();
}
```
- Window starts at `i - k + 1`
- Remove indices that are before the window start

### 3. Remove Smaller Elements
```cpp
while(!q.empty() && nums[q.back()] < nums[i]) {
    q.pop_back();
}
```
- Remove indices whose values are smaller than `nums[i]`
- These elements can never be the maximum in any future window
- Maintains decreasing order in deque

### 4. Add Current Index
```cpp
q.push_back(i);
```
- Add current index to deque

### 5. Record Maximum
```cpp
if(i >= k - 1) {
    rtn.push_back(nums[q.front()]);
}
```
- When window is complete (i >= k - 1), add maximum to result
- Maximum is always at `q.front()`

## Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Each element is added once and removed at most once |
| **Space** | O(k) - Deque stores at most k indices |

### Why O(n) Time?

- Each index is added to deque exactly once: O(n)
- Each index is removed from deque at most once: O(n)
- Total: O(n) operations

## Alternative Approaches

### Approach 1: Brute Force (TLE for large inputs)

```cpp
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    vector<int> rtn;
    for(int i = 0; i <= (int)nums.size() - k; i++) {
        int maxVal = INT_MIN;
        for(int j = i; j < i + k; j++) {
            maxVal = max(maxVal, nums[j]);
        }
        rtn.push_back(maxVal);
    }
    return rtn;
}
```

**Time Complexity:** O(n×k)  
**Space Complexity:** O(1)

### Approach 2: Using Priority Queue (Max Heap)

```cpp
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    vector<int> rtn;
    priority_queue<pair<int, int>> pq;  // {value, index}
    
    for(int i = 0; i < (int)nums.size(); i++) {
        pq.push({nums[i], i});
        
        // Remove elements outside window
        while(pq.top().second <= i - k) {
            pq.pop();
        }
        
        if(i >= k - 1) {
            rtn.push_back(pq.top().first);
        }
    }
    return rtn;
}
```

**Time Complexity:** O(n log n) - Heap operations  
**Space Complexity:** O(n)

### Approach 3: Using Multiset

```cpp
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    vector<int> rtn;
    multiset<int> window;
    
    for(int i = 0; i < (int)nums.size(); i++) {
        window.insert(nums[i]);
        
        if(i >= k - 1) {
            rtn.push_back(*window.rbegin());  // Maximum element
            window.erase(window.find(nums[i - k + 1]));  // Remove leftmost
        }
    }
    return rtn;
}
```

**Time Complexity:** O(n log k) - Multiset operations  
**Space Complexity:** O(k)

## Comparison of Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n×k) | O(1) | Simple but inefficient |
| Priority Queue | O(n log n) | O(n) | Easy to implement |
| Multiset | O(n log k) | O(k) | Good for small k |
| **Monotonic Deque** | **O(n)** | **O(k)** | **Optimal** |

## Why Monotonic Deque is Optimal

1. **Linear Time**: Each element is processed exactly once
2. **Constant Operations**: Deque operations (push, pop) are O(1) amortized
3. **Efficient Removal**: Removing smaller elements early prevents unnecessary comparisons
4. **Direct Access**: Maximum is always at front, no need to search

## Edge Cases

1. **k = 1**: Each window has one element → return all elements
2. **k = nums.size()**: Single window → return maximum of entire array
3. **All increasing**: `[1,2,3,4,5]` → deque always has one element
4. **All decreasing**: `[5,4,3,2,1]` → deque contains all indices initially
5. **All same**: `[3,3,3,3]` → all 3s in result

## Common Mistakes

1. **Forgetting to remove out-of-window indices**: Must check `q.front() < i - k + 1`
2. **Wrong comparison**: Should be `nums[q.back()] < nums[i]` not `<=` (handles duplicates)
3. **Adding before window complete**: Only add to result when `i >= k - 1`
4. **Using values instead of indices**: Deque should store indices to check window boundaries

## Optimization Tips

### Early Termination Check
```cpp
// Optional: If k == 1, just return the array
if(k == 1) return nums;

// Optional: If k == nums.size(), return max element
if(k == nums.size()) {
    return {*max_element(nums.begin(), nums.end())};
}
```

### Memory Optimization
The deque approach is already optimal. For very large arrays, you could use a fixed-size array, but deque is more flexible and still O(k) space.

## Related Problems

- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - This problem
- [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) - Find median instead of maximum
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) - Use two deques for min and max
- [2392. Build a Matrix With Conditions](https://leetcode.com/problems/build-a-matrix-with-conditions/) - Different application
- [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) - Monotonic deque for prefix sums

## Pattern Recognition

This problem demonstrates the **Monotonic Deque** pattern:
- Maintain a deque with elements in monotonic order (increasing or decreasing)
- Remove elements that violate the monotonic property
- Use deque to efficiently query extreme values (min/max) in a sliding window

**Applications:**
- Sliding window maximum/minimum
- Next greater/smaller element
- Range queries in sliding windows
- Dynamic programming optimizations

## Code Quality Notes

1. **Readability**: Clear variable names (`q` for queue, `rtn` for result)
2. **Efficiency**: Optimal time and space complexity
3. **Correctness**: Handles all edge cases properly
4. **Maintainability**: Well-structured code with clear comments

## Implementation Details

### Why Store Indices Instead of Values?

Storing indices allows us to:
1. Check if an element is outside the window: `q.front() < i - k + 1`
2. Access the value: `nums[q.front()]`
3. Compare values: `nums[q.back()] < nums[i]`

### Why Remove from Back?

We maintain decreasing order, so when we encounter a larger value:
- All smaller values at the back can never be maximum
- Removing from back maintains the monotonic property
- Front always contains the maximum index

### Why Check `i >= k - 1`?

- Window of size `k` starting at index `i` covers `[i, i+k-1]`
- When `i = k - 1`, window is `[0, k-1]` (first complete window)
- Before this, window is incomplete, so we don't record maximum

---

*This problem is a classic example of using a monotonic deque to efficiently solve sliding window problems. The key insight is maintaining a data structure that automatically keeps track of the maximum while efficiently removing outdated elements.*

