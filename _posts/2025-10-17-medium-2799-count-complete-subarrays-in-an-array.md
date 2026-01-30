---
layout: post
title: "[Medium] 2799. Count Complete Subarrays in an Array"
date: 2025-10-17 10:09:13 -0700
categories: leetcode algorithm medium cpp sliding-window hash-map problem-solving
---

# [Medium] 2799. Count Complete Subarrays in an Array

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Complete subarray definition**: What is a "complete subarray"? (Assumption: Subarray that contains all distinct elements present in the original array)

2. **Subarray requirement**: Does subarray need to be contiguous? (Assumption: Yes - subarray is contiguous by definition)

3. **Distinct elements**: How do we determine distinct elements? (Assumption: Count unique values in original array - complete subarray must contain all of them)

4. **Return value**: What should we return? (Assumption: Count of complete subarrays - integer)

5. **Empty subarray**: Can an empty subarray be complete? (Assumption: No - need at least one element to contain distinct values)

## Solution: Optimized Sliding Window

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

## How the Algorithm Works

### Key Insight: Optimized Sliding Window

Use two pointers to maintain a window that contains all distinct elements. When the window is complete, count all subarrays that extend from the current position to the end.

**Steps:**
1. **Count total distinct elements** in the array
2. **Expand right pointer** to include new elements
3. **When window is complete**, count all valid subarrays and shrink from left
4. **Continue until** all subarrays are processed

### Step-by-Step Example: `nums = [1,3,1,2,2]`

| Step | Left | Right | Window | Freq Map | Complete? | Action |
|------|------|-------|--------|----------|-----------|--------|
| 1 | 0 | 0 | [1] | {1:1} | No | Expand right |
| 2 | 0 | 1 | [1,3] | {1:1,3:1} | No | Expand right |
| 3 | 0 | 2 | [1,3,1] | {1:2,3:1} | No | Expand right |
| 4 | 0 | 3 | [1,3,1,2] | {1:2,3:1,2:1} | **Yes** | Count: 5-3=2, shrink left |
| 5 | 1 | 3 | [3,1,2] | {3:1,1:1,2:1} | **Yes** | Count: 5-3=2, shrink left |
| 6 | 2 | 3 | [1,2] | {1:1,2:1} | No | Expand right |
| 7 | 2 | 4 | [1,2,2] | {1:1,2:2} | No | End |

**Total distinct elements:** 3 (1, 3, 2)  
**Complete subarrays:** 4 (2 + 2)

### Visual Representation

```
nums = [1, 3, 1, 2, 2]
       0  1  2  3  4

Complete subarrays:
[1,3,1,2]     (indices 0-3) ✓
[1,3,1,2,2]   (indices 0-4) ✓  
[3,1,2]       (indices 1-3) ✓
[3,1,2,2]     (indices 1-4) ✓

Total: 4 complete subarrays
```

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

## Alternative Approaches

### Approach 1: Nested Loops (Original)
```cpp
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int cnt = 0;
        unordered_set<int> distinct(nums.begin(), nums.end());
        int total_unique = distinct.size();

        for (int left = 0; left < nums.size(); ++left) {
            unordered_map<int, int> window_counts;
            for (int right = left; right < nums.size(); ++right) {
                window_counts[nums[right]]++;
                if (window_counts.size() == total_unique) {
                    cnt++;
                }
            }
        }

        return cnt;
    }
};
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

### Approach 2: Brute Force with Set
```cpp
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> distinct(nums.begin(), nums.end());
        int total_unique = distinct.size();
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                unordered_set<int> subarray_elements;
                for (int k = i; k <= j; k++) {
                    subarray_elements.insert(nums[k]);
                }
                if (subarray_elements.size() == total_unique) {
                    cnt++;
                }
            }
        }

        return cnt;
    }
};
```

**Time Complexity:** O(n³)  
**Space Complexity:** O(n)

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Optimized Sliding Window | O(n) | O(n) |
| Nested Loops | O(n²) | O(n) |
| Brute Force | O(n³) | O(n) |

## Edge Cases

1. **Single element:** `nums = [1]` → `1`
2. **All same elements:** `nums = [5,5,5,5]` → `10`
3. **All distinct elements:** `nums = [1,2,3,4]` → `1`
4. **Two distinct elements:** `nums = [1,2,1,2]` → `3`

## Key Insights

1. **Two Pointers:** Use left and right pointers to maintain sliding window
2. **Complete Window:** When window contains all distinct elements, count all valid subarrays
3. **Efficient Counting:** `cnt += nums.size() - right` counts all subarrays from current position to end
4. **Window Shrinking:** Remove elements from left until window is no longer complete
5. **Linear Time:** Each element is processed at most twice (once by each pointer)

## Common Mistakes

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

- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
- [340. Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

## Why This Solution is Optimal

1. **Linear Time Complexity:** O(n) is optimal for this problem
2. **Two Pointers Technique:** Each element visited at most twice
3. **Efficient Counting:** Counts all valid subarrays in one operation
4. **Optimal Space:** O(n) space for frequency tracking
5. **Clear Logic:** Easy to understand and implement
