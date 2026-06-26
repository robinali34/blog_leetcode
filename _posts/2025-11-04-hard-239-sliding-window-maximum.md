---
layout: post
title: "[Hard] 239. Sliding Window Maximum"
date: 2025-11-04 21:22:32 -0800
categories: leetcode algorithm hard cpp arrays deque sliding-window monotonic-queue problem-solving
permalink: /posts/2025-11-04-hard-239-sliding-window-maximum/
tags: [leetcode, hard, array, deque, sliding-window, monotonic-queue]
---
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

## Thinking Process

1. **Monotonic Deque**: Maintain indices in decreasing order of values

- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Sliding window</text>

  <rect x="20" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="36" y="63" text-anchor="middle" font-size="11">a</text>
  <rect x="52" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="68" y="63" text-anchor="middle" font-size="11">b</text>
  <rect x="84" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="63" text-anchor="middle" font-size="11">c</text>
  <rect x="116" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="132" y="63" text-anchor="middle" font-size="11">d</text>
  <rect x="148" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="164" y="63" text-anchor="middle" font-size="11">e</text>
  <rect x="52" y="38" width="64" height="42" rx="4" fill="none" stroke="#C4956A" stroke-width="2" stroke-dasharray="4"/>
  <text x="84" y="32" text-anchor="middle" font-size="10" fill="#C4956A" font-weight="600">window</text>
  <text x="110" y="105" text-anchor="middle" font-size="11" fill="#6B6560">expand right, shrink left when invalid</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Fixed-size window** *(this problem)* | $O(n)$ | $O(1)$ | Window size known upfront |
| Variable-size window | $O(n)$ | $O(1)$ | Expand/shrink until valid |
| Window + hash map | $O(n)$ | $O(k)$ | Track character/count frequencies |
| Deque window max | $O(n)$ | $O(k)$ | Monotonic deque for max/min in window |

## Solution

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

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** 1. **Monotonic Deque**: Maintain indices in decreasing order of values

**How the code works:**
1. **Monotonic Deque**: Maintain indices in decreasing order of values
- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

**Walkthrough** — input `nums = [1,3,-1,-3,5,3,6,7], k = 3`, expected output `[3,3,5,5,6,7]`:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Each element is added once and removed at most once |
| **Space** | O(k) - Deque stores at most k indices |
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

### Complexity
| Aspect | Complexity |
|--------|------------|
| **Time** | O(n) - Each element is added once and removed at most once |
| **Space** | O(k) - Deque stores at most k indices |

### Why O(n) Time?

- Each index is added to deque exactly once: O(n)
- Each index is removed from deque at most once: O(n)
- Total: O(n) operations

## Why Monotonic Deque is Optimal

1. **Linear Time**: Each element is processed exactly once
2. **Constant Operations**: Deque operations (push, pop) are O(1) amortized
3. **Efficient Removal**: Removing smaller elements early prevents unnecessary comparisons
4. **Direct Access**: Maximum is always at front, no need to search

## Common Mistakes

1. **k = 1**: Each window has one element → return all elements
2. **k = nums.size()**: Single window → return maximum of entire array
3. **All increasing**: `[1,2,3,4,5]` → deque always has one element
4. **All decreasing**: `[5,4,3,2,1]` → deque contains all indices initially
5. **All same**: `[3,3,3,3]` → all 3s in result

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

- [239. Sliding Window Maximum](https://www.leetcode.com/problems/sliding-window-maximum/) - This problem
- [480. Sliding Window Median](https://www.leetcode.com/problems/sliding-window-median/) - Find median instead of maximum
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://www.leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) - Use two deques for min and max
- [2392. Build a Matrix With Conditions](https://www.leetcode.com/problems/build-a-matrix-with-conditions/) - Different application
- [862. Shortest Subarray with Sum at Least K](https://www.leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) - Monotonic deque for prefix sums

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

## Key Takeaways

1. **Monotonic Deque**: Maintain indices in decreasing order of values
2. **Remove Out-of-Window**: Remove indices `i - k + 1` from the front
3. **Remove Smaller Elements**: Remove indices whose values are smaller than current (they can never be maximum)
4. **Front is Maximum**: `q.front()` always points to the maximum element in current window
5. **Amortized O(1)**: Each element is added and removed at most once

## References

- [LC 239: Sliding Window Maximum on LeetCode](https://www.leetcode.com/problems/sliding-window-maximum/)
- [LeetCode Discuss — LC 239: Sliding Window Maximum](https://www.leetcode.com/problems/sliding-window-maximum/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/sliding-window-maximum/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
