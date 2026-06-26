---
layout: post
title: "[Hard] 862. Shortest Subarray with Sum at Least K"
date: 2026-01-26 00:00:00 -0700
categories: [leetcode, hard, array, sliding-window, deque, prefix-sum, monotonic-deque]
permalink: /2026/01/26/hard-862-shortest-subarray-with-sum-at-least-k/
tags: [leetcode, hard, array, sliding-window, deque, prefix-sum, monotonic-deque]
---
Given an integer array `nums` and an integer `k`, return *the **length** of the shortest non-empty **subarray** of* `nums` *with a sum of at least* `k`. If there is no such subarray, return `-1`.

A **subarray** is a contiguous part of an array.

## Examples

**Example 1:**

```
Input: nums = [1], k = 1
Output: 1
```

**Example 2:**

```
Input: nums = [1,2], k = 4
Output: -1
```

**Example 3:**

```
Input: nums = [2,-1,2], k = 3
Output: 3
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

## Thinking Process

1. **Negative Numbers Break Simple Sliding Window**: Cannot shrink window from left when sum >= k
- If `preSum[i] <= preSum[j]` and `i < j`, then `i` is always better
- Remove from front: processed starting positions
- Remove from back: maintain monotonic property

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
| **Fixed-size window** *(this problem)* | O(n) | O(1) | Window size known upfront |
| Variable-size window | O(n) | O(1) | Expand/shrink until valid |
| Window + hash map | O(n) | O(k) | Track character/count frequencies |
| Deque window max | O(n) | O(k) | Monotonic deque for max/min in window |

## Solution

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        if(nums.empty()) return -1;
        const int N = nums.size();
        vector<long> preSum(N + 1);
        for(int i = 0; i < N; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        int rtn = INT_MAX;
        deque<int> q;
        for(int i = 0; i <= N; i++) {
            long curSum = preSum[i];
            while(!q.empty() && curSum - preSum[q.front()] >= k) {
                rtn = min(rtn, i - q.front());
                q.pop_front();
            }
            while(!q.empty() && preSum[q.back()] >= curSum) {
                q.pop_back();
            }
            q.push_back(i);
        }
        return rtn == INT_MAX? -1: rtn;
    }
};
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** 1. **Negative Numbers Break Simple Sliding Window**: Cannot shrink window from left when sum >= k

**How the code works:**
1. **Negative Numbers Break Simple Sliding Window**: Cannot shrink window from left when sum >= k
- If `preSum[i] <= preSum[j]` and `i < j`, then `i` is always better
- Remove from front: processed starting positions
- Remove from back: maintain monotonic property
- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.

**Walkthrough** — input `nums = [1], k = 1`, expected output `1`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

1. **Empty array**: `nums = []` → return `-1`
2. **No valid subarray**: `nums = [1,2]`, `k = 4` → return `-1`
3. **Single element**: `nums = [1]`, `k = 1` → return `1`
4. **Negative numbers**: `nums = [2,-1,2]`, `k = 3` → return `3`
5. **All negative**: `nums = [-1,-2,-3]`, `k = 1` → return `-1`
6. **Large k**: `nums = [1,2]`, `k = 10^9` → return `-1`

1. **Using simple sliding window**: Fails with negative numbers
2. **Not maintaining monotonic property**: Leads to incorrect results
3. **Wrong deque operations**: Removing from wrong end
4. **Integer overflow**: Not using `long` for prefix sums
5. **Index confusion**: Mixing 0-indexed and 1-indexed arrays
6. **Not checking empty deque**: Accessing `q.front()` or `q.back()` without checking

## Comparison with LC 209

| Aspect | LC 209 (All Positive) | LC 862 (Can Have Negatives) |
|--------|----------------------|----------------------------|
| **Approach** | Simple sliding window | Monotonic deque |
| **Time** | O(n) | O(n) |
| **Space** | O(1) | O(n) |
| **Complexity** | Simpler | More complex |
| **Key Insight** | Shrink window when sum >= k | Maintain monotonic deque |

## Related Problems

- [LC 209: Minimum Size Subarray Sum](https://robinali34.github.io/blog_leetcode/2026/01/26/medium-209-minimum-size-subarray-sum/) - Similar but all positive numbers
- [LC 3: Longest Substring Without Repeating Characters](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) - Sliding window pattern
- [LC 76: Minimum Window Substring](https://www.leetcode.com/problems/minimum-window-substring/) - Similar sliding window
- [LC 53: Maximum Subarray](https://robinali34.github.io/blog_leetcode/2026/01/04/medium-53-maximum-subarray/) - Maximum sum subarray
- [LC 239: Sliding Window Maximum](https://www.leetcode.com/problems/sliding-window-maximum/) - Monotonic deque pattern

## Key Takeaways

1. **Negative Numbers Break Simple Sliding Window**: Cannot shrink window from left when sum >= k

2. **Prefix Sum Enables Range Queries**: `preSum[j+1] - preSum[i]` = sum from `i` to `j`

3. **Monotonic Deque**: Maintains indices with increasing prefix sums
   - If `preSum[i] <= preSum[j]` and `i < j`, then `i` is always better

4. **Why Deque?**: Need O(1) operations on both ends
   - Remove from front: processed starting positions
   - Remove from back: maintain monotonic property

5. **Two While Loops**:
   - First loop: find valid subarrays ending at current position
   - Second loop: maintain monotonic property for future positions

## References

- [LC 862: Shortest Subarray with Sum at Least K on LeetCode](https://www.leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
- [LeetCode Discuss — LC 862: Shortest Subarray with Sum at Least K](https://www.leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/shortest-subarray-with-sum-at-least-k/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
