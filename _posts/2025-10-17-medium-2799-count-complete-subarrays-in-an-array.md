---
layout: post
title: "[Medium] 2799. Count Complete Subarrays in an Array"
date: 2025-10-17 10:09:13 -0700
categories: leetcode algorithm medium cpp sliding-window hash-map problem-solving
---
You are given an integer array `nums`.

We call a subarray **complete** if:
- The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.

Return the number of **complete subarrays**.

A **subarray** is a contiguous part of an array.

## Examples

**Example 1:**
```
Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following:
- [1,3,1,2,2] at position 0 to 4
- [1,3,1,2] at position 0 to 3  
- [3,1,2,2] at position 1 to 4
- [1,2,2] at position 2 to 4
```

**Example 2:**
```
Input: nums = [5,5,5,5]
Output: 10
Explanation: The complete subarrays are the following:
- [5,5,5,5] at position 0 to 3
- [5,5,5] at position 0 to 2
- [5,5] at position 0 to 1
- [5] at position 0 to 0
- [5,5,5] at position 1 to 3
- [5,5] at position 1 to 2
- [5] at position 1 to 1
- [5,5] at position 2 to 3
- [5] at position 2 to 2
- [5] at position 3 to 3
```

## Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2000`

## Thinking Process

1. **Two Pointers:** Use left and right pointers to maintain sliding window

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

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Use two pointers with sliding window technique to efficiently count complete subarrays.

```cpp
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int cnt = 0;
        unordered_set<int> distinct(nums.begin(), nums.end());
        int distinct_cnt = distinct.size();
        unordered_map<int, int> freq;
        
        for(int left = 0, right = 0; right < (int) nums.size(); right++) {
            freq[nums[right]]++;
            while(freq.size() == distinct_cnt) {
                cnt += nums.size() - right;
                freq[nums[left]]--;
                if(freq[nums[left]] == 0) {
                    freq.erase(nums[left]);
                }
                left++;
            }
        }
        return cnt;
    }
};
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** 1. **Two Pointers:** Use left and right pointers to maintain sliding window

**How the code works:**
1. **Two Pointers:** Use left and right pointers to maintain sliding window
- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

**Walkthrough** — input `nums = [1,3,1,2,2]`, expected output `4`:

The complete subarrays are the following:
- [1,3,1,2,2] at position 0 to 4
- [1,3,1,2] at position 0 to 3  
- [3,1,2,2] at position 1 to 4
- [1,2,2] at position 2 to 4

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Optimized Sliding Window | O(n) | O(n) |
| Nested Loops | O(n²) | O(n) |
| Brute Force | O(n³) | O(n) |
## Algorithm Breakdown

### 1. Initialize Variables
```cpp
unordered_set<int> distinct(nums.begin(), nums.end());
int distinct_cnt = distinct.size();
unordered_map<int, int> freq;
```

**Purpose:** Track total distinct elements and current window frequencies.

### 2. Two Pointers Sliding Window
```cpp
for(int left = 0, right = 0; right < (int) nums.size(); right++) {
    freq[nums[right]]++;
    while(freq.size() == distinct_cnt) {
        cnt += nums.size() - right;
        freq[nums[left]]--;
        if(freq[nums[left]] == 0) {
            freq.erase(nums[left]);
        }
        left++;
    }
}
```

**Process:**
1. **Expand right:** Add new element to window
2. **Check completeness:** When all distinct elements are present
3. **Count subarrays:** All subarrays from current position to end are complete
4. **Shrink left:** Remove elements until window is no longer complete

### Key Insight: `cnt += nums.size() - right;`

This line is the core optimization of the algorithm. When the window `[left, right]` contains all distinct elements, **all subarrays that start at `left` and end at or after `right` are complete**.

**Mathematical Explanation:**
- Current window: `[left, right]` (complete)
- Remaining positions: `right+1, right+2, ..., nums.size()-1`
- Number of complete subarrays: `nums.size() - right`

**Example:** `nums = [1,3,1,2,2]`, `right = 3`
- Current window: `[1,3,1,2]` (indices 0-3) ✓ Complete
- Remaining positions: `4` (index 4)
- Complete subarrays: `[1,3,1,2]` and `[1,3,1,2,2]` = 2 subarrays
- Calculation: `5 - 3 = 2` ✓

**Why this works:**
- If `[left, right]` is complete, then `[left, right+1]`, `[left, right+2]`, ..., `[left, nums.size()-1]` are also complete
- We don't need to check each one individually
- This optimization reduces time complexity from O(n²) to O(n)

### Visual Example: `cnt += nums.size() - right;`

**Scenario:** `nums = [1,3,1,2,2]`, `left = 0`, `right = 3`

```
Array:     [1, 3, 1, 2, 2]
Indices:    0  1  2  3  4
            ↑           ↑
          left        right
```

**Current window:** `[1,3,1,2]` (indices 0-3) ✓ **Complete**

**All complete subarrays starting at left=0:**
- `[1,3,1,2]` (indices 0-3) ✓
- `[1,3,1,2,2]` (indices 0-4) ✓

**Calculation:** `nums.size() - right = 5 - 3 = 2` ✓

**Why extending right doesn't break completeness:**
- Adding more elements to a complete subarray keeps it complete
- We already have all distinct elements: {1, 3, 2}
- Adding duplicates (like the second '2') doesn't change distinct count

### Complexity
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Optimized Sliding Window | O(n) | O(n) |
| Nested Loops | O(n²) | O(n) |
| Brute Force | O(n³) | O(n) |

## Common Mistakes

1. **Single element:** `nums = [1]` → `1`
2. **All same elements:** `nums = [5,5,5,5]` → `10`
3. **All distinct elements:** `nums = [1,2,3,4]` → `1`
4. **Two distinct elements:** `nums = [1,2,1,2]` → `3`

1. **Wrong distinct count:** Not counting total distinct elements correctly
2. **Incomplete window check:** Not checking if window has all distinct elements
3. **Index bounds:** Off-by-one errors in loop boundaries
4. **Hash map updates:** Not properly updating element counts

## Detailed Example Walkthrough

### Example: `nums = [1,3,1,2,2]`

**Step 1: Count distinct elements**
```
distinct = {1, 3, 2}
total_unique = 3
```

**Step 2: Check all subarrays**

```
Left = 0:
  Right = 0: [1] → {1} → size = 1 ≠ 3
  Right = 1: [1,3] → {1,3} → size = 2 ≠ 3  
  Right = 2: [1,3,1] → {1,3} → size = 2 ≠ 3
  Right = 3: [1,3,1,2] → {1,3,2} → size = 3 = 3 ✓
  Right = 4: [1,3,1,2,2] → {1,3,2} → size = 3 = 3 ✓

Left = 1:
  Right = 1: [3] → {3} → size = 1 ≠ 3
  Right = 2: [3,1] → {3,1} → size = 2 ≠ 3
  Right = 3: [3,1,2] → {3,1,2} → size = 3 = 3 ✓
  Right = 4: [3,1,2,2] → {3,1,2} → size = 3 = 3 ✓

Left = 2:
  Right = 2: [1] → {1} → size = 1 ≠ 3
  Right = 3: [1,2] → {1,2} → size = 2 ≠ 3
  Right = 4: [1,2,2] → {1,2} → size = 2 ≠ 3

Left = 3:
  Right = 3: [2] → {2} → size = 1 ≠ 3
  Right = 4: [2,2] → {2} → size = 1 ≠ 3

Left = 4:
  Right = 4: [2] → {2} → size = 1 ≠ 3

Total complete subarrays: 4
```

## Optimization Opportunities

### 1. Early Termination
```cpp
if (window_counts.size() == total_unique) {
    cnt += (nums.size() - right);  // All remaining subarrays are complete
    break;
}
```

### 2. Set Instead of Map
```cpp
unordered_set<int> window_elements;
// Only track presence, not frequency
```

### 3. Two Pointers Optimization
```cpp
// Use two pointers to find minimum window with all elements
// Then count all subarrays containing this window
```

## Related Problems

- [76. Minimum Window Substring](https://www.leetcode.com/problems/minimum-window-substring/)
- [3. Longest Substring Without Repeating Characters](https://www.leetcode.com/problems/longest-substring-without-repeating-characters/)
- [159. Longest Substring with At Most Two Distinct Characters](https://www.leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
- [340. Longest Substring with At Most K Distinct Characters](https://www.leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

## Why This Solution is Optimal

1. **Linear Time Complexity:** O(n) is optimal for this problem
2. **Two Pointers Technique:** Each element visited at most twice
3. **Efficient Counting:** Counts all valid subarrays in one operation
4. **Optimal Space:** O(n) space for frequency tracking
5. **Clear Logic:** Easy to understand and implement

## References

- [LC 2799: Count Complete Subarrays in an Array on LeetCode](https://www.leetcode.com/problems/count-complete-subarrays-in-an-array/)
- [LeetCode Discuss — LC 2799: Count Complete Subarrays in an Array](https://www.leetcode.com/problems/count-complete-subarrays-in-an-array/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/count-complete-subarrays-in-an-array/editorial/) *(may require premium)*

## Key Takeaways

1. **Two Pointers:** Use left and right pointers to maintain sliding window
2. **Complete Window:** When window contains all distinct elements, count all valid subarrays
3. **Efficient Counting:** `cnt += nums.size() - right` counts all subarrays from current position to end
4. **Window Shrinking:** Remove elements from left until window is no longer complete
5. **Linear Time:** Each element is processed at most twice (once by each pointer)
