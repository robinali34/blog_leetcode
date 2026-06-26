---
layout: post
title: "[Hard] 480. Sliding Window Median"
date: 2025-11-04 21:55:29 -0800
categories: leetcode algorithm hard cpp arrays multiset sliding-window two-heaps problem-solving
permalink: /posts/2025-11-04-hard-480-sliding-window-median/
tags: [leetcode, hard, array, multiset, sliding-window, two-heaps, median]
---
The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the median array for each window in the original array*.

## Examples

**Example 1:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
```

**Example 2:**
```
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Thinking Process

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.

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

**Time Complexity:** O(n log k) - Each insertion/deletion is O(log k)  
**Space Complexity:** O(k) - Two multisets store window elements

Use two multisets to maintain a balanced structure: `lo` contains the smaller half, `hi` contains the larger half. The median is the maximum of `lo` (odd k) or average of max(lo) and min(hi) (even k).

```cpp
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> res;
        multiset<int> lo, hi;

        auto balance = [&]() {
            while(lo.size() > hi.size() + 1) {
                hi.insert(*prev(lo.end()));
                lo.erase(prev(lo.end()));
            }
            while(lo.size() < hi.size()) {
                lo.insert(*hi.begin());
                hi.erase(hi.begin());
            }
        };

        auto getMedian = [&]() -> double {
            if(k % 2 == 0) return ((double)*prev(lo.end()) + *hi.begin()) / 2.0;
            else return *prev(lo.end());
        };

        for(int i = 0; i < nums.size(); i++) {
            // Insert new element
            if(lo.empty() || nums[i] <= *prev(lo.end())) 
                lo.insert(nums[i]);
            else 
                hi.insert(nums[i]);
            balance();

            // Remove element leaving window
            if(i >= k) {
                int out = nums[i - k];
                if(lo.find(out) != lo.end()) 
                    lo.erase(lo.find(out));
                else 
                    hi.erase(hi.find(out));
                balance();
            }

            // Calculate median when window is complete
            if(i >= k - 1) 
                res.push_back(getMedian());
        }

        return res;
    }
};
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

**How the code works:**
- For example, for `arr = [2,3,4]`, the median is `3`.
- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

**Walkthrough** — input `nums = [1,3,-1,-3,5,3,6,7], k = 3`, expected output `[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]`:

Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| **Solution 1 (Two Multisets)** | O(n log k) | O(k) | Clear separation, easier to understand |
| **Solution 2 (Single Multiset)** | O(n log k) | O(k) | More compact, requires careful iterator management |
## How Solution 1 Works

### Key Insight: Two-Heaps Pattern

- **`lo`**: Multiset containing smaller half, maintained in increasing order
- **`hi`**: Multiset containing larger half, maintained in increasing order
- **Balance**: Keep `lo.size() == hi.size()` (even k) or `lo.size() == hi.size() + 1` (odd k)
- **Median**: 
  - Odd k: `*prev(lo.end())` (maximum of lo)
  - Even k: `(*prev(lo.end()) + *hi.begin()) / 2.0`

### Step-by-Step Example: `nums = [1,3,-1,-3,5,3,6,7], k = 3`

| Step | i | nums[i] | Insert | lo | hi | Remove | lo | hi | Window | Median |
|------|---|---------|--------|----|----|--------|----|----|--------|--------|
| 0 | 0 | 1 | 1→lo | {1} | {} | - | {1} | {} | [1] | - |
| 1 | 1 | 3 | 3→hi | {1} | {3} | - | {1} | {3} | [1,3] | - |
| 2 | 2 | -1 | -1→lo | {-1,1} | {3} | - | {-1,1} | {3} | [-1,1,3] | 1.0 |
| 3 | 3 | -3 | -3→lo | {-3,-1,1} | {3} | 1→out | {-3,-1} | {3} | [-1,-3,3] | -1.0 |
| 4 | 4 | 5 | 5→hi | {-3,-1} | {3,5} | -1→out | {-3} | {3,5} | [-3,3,5] | -1.0 |
| 5 | 5 | 3 | 3→lo | {-3,3} | {5} | -3→out | {3} | {5} | [3,5,3] | 3.0 |
| 6 | 6 | 6 | 6→hi | {3} | {5,6} | 3→out | {5} | {6} | [5,3,6] | 5.0 |
| 7 | 7 | 7 | 7→hi | {5} | {6,7} | 3→out | {6} | {7} | [3,6,7] | 6.0 |

**Final Answer:** `[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]`

### Visual Representation

```
nums = [1, 3, -1, -3, 5, 3, 6, 7]
       0  1   2    3   4  5  6  7

Step 0-2: Window [1, 3, -1]
  lo = {-1, 1}  (smaller half)
  hi = {3}       (larger half)
  Median = max(lo) = 1 (k=3 is odd)

Step 3: Window [3, -1, -3]
  lo = {-3, -1}
  hi = {3}
  Median = (max(lo) + min(hi)) / 2 = (-1 + 3) / 2 = 1
  Wait, k=3 is odd, so median = max(lo) = -1

Step 4: Window [-1, -3, 5]
  lo = {-3, -1}
  hi = {5}
  Median = max(lo) = -1
```

## How Solution 2 Works

### Key Insight: Median Iterator Tracking

- **`window`**: Multiset containing all elements in current window
- **`mid`**: Iterator pointing to the median element(s)
  - Odd k: `mid` points to middle element
  - Even k: `mid` points to the right median (we average with `next(mid, -1)`)
- **Incremental Updates**: When adding/removing, adjust `mid` by at most 1 position

### Step-by-Step Example: `nums = [1,3,-1,-3,5,3,6,7], k = 3`

| Step | i | nums[i] | Insert | mid points to | Remove | mid points to | Window | Median |
|------|---|---------|--------|---------------|--------|---------------|--------|--------|
| 0 | - | - | - | - | - | - | {1,3,-1} | 1 |
| 1 | 3 | -3 | {-3} | 1→-1 | 1 | -1→-1 | {-3,-1,3} | -1 |
| 2 | 4 | 5 | {5} | -1→-1 | -1 | -1→3 | {-3,3,5} | -1 |
| 3 | 5 | 3 | {3} | 3→3 | -3 | 3→3 | {3,3,5} | 3 |
| 4 | 6 | 6 | {6} | 3→5 | 3 | 5→5 | {3,5,6} | 5 |
| 5 | 7 | 7 | {7} | 5→6 | 3 | 6→6 | {3,6,7} | 6 |

**Note:** After sorting: `{-3,-1,3}` → `mid` points to `-1` (index 1 in sorted array)

### Median Calculation Trick

```cpp
medians.push_back(((double)(*mid) + *next(mid, k % 2 - 1)) * 0.5);
```

- **k is odd**: `k % 2 - 1 = 0` → `*mid` (use same element twice, divide by 2)
  - Actually, for odd k, we should use `*mid` directly, but this formula works
- **k is even**: `k % 2 - 1 = -1` → `(*mid + *prev(mid)) / 2.0`

**Correction for odd k:**
```cpp
if (k % 2 == 1)
    medians.push_back(*mid);
else
    medians.push_back(((double)(*mid) + *prev(mid)) * 0.5);
```

## Algorithm Breakdown

### Solution 1: Two Multisets

#### 1. Insert New Element
```cpp
if(lo.empty() || nums[i] <= *prev(lo.end())) 
    lo.insert(nums[i]);
else 
    hi.insert(nums[i]);
```

- Insert into appropriate multiset based on comparison with max of `lo`

#### 2. Balance the Two Multisets
```cpp
auto balance = [&]() {
    while(lo.size() > hi.size() + 1) {
        hi.insert(*prev(lo.end()));
        lo.erase(prev(lo.end()));
    }
    while(lo.size() < hi.size()) {
        lo.insert(*hi.begin());
        hi.erase(hi.begin());
    }
};
```

- Maintain: `lo.size() == hi.size()` (even k) or `lo.size() == hi.size() + 1` (odd k)

#### 3. Remove Element Leaving Window
```cpp
if(i >= k) {
    int out = nums[i - k];
    if(lo.find(out) != lo.end()) 
        lo.erase(lo.find(out));
    else 
        hi.erase(hi.find(out));
    balance();
}
```

- Find and remove element from appropriate multiset

#### 4. Calculate Median
```cpp
auto getMedian = [&]() -> double {
    if(k % 2 == 0) 
        return ((double)*prev(lo.end()) + *hi.begin()) / 2.0;
    else 
        return *prev(lo.end());
};
```

### Solution 2: Single Multiset with Iterator

#### 1. Initialize
```cpp
multiset<int> window(nums.begin(), nums.begin() + k);
auto mid = next(window.begin(), k / 2);
```

- Create multiset with first k elements
- Set `mid` to point to median position

#### 2. Insert and Adjust
```cpp
window.insert(nums[i]);
if (nums[i] < *mid)
    mid--;  // New element is smaller, median moved left
```

- Insert new element
- Adjust median iterator if needed

#### 3. Remove and Adjust
```cpp
if (nums[i - k] <= *mid)
    mid++;  // Removed element was <= median, median moved right
    
window.erase(window.lower_bound(nums[i - k]));
```

- Adjust median iterator before removal
- Remove element using `lower_bound` to handle duplicates

### Complexity
| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| **Solution 1 (Two Multisets)** | O(n log k) | O(k) | Clear separation, easier to understand |
| **Solution 2 (Single Multiset)** | O(n log k) | O(k) | More compact, requires careful iterator management |

### Why O(n log k)?

- **Insertion**: O(log k) - Insert into multiset of size k
- **Deletion**: O(log k) - Erase from multiset of size k
- **Balance/Adjust**: O(log k) - Move elements between sets or adjust iterator
- **Total**: n operations × O(log k) = O(n log k)

## Comparison of Solutions

| Aspect | Solution 1 (Two Multisets) | Solution 2 (Single Multiset) |
|--------|----------------------------|------------------------------|
| **Clarity** | ✅ Clear separation of halves | ⚠️ Requires iterator management |
| **Correctness** | ✅ Easy to verify balance | ⚠️ Iterator adjustments can be tricky |
| **Duplicates** | ✅ Handles naturally | ⚠️ Need `lower_bound` for removal |
| **Median Calc** | ✅ Straightforward | ⚠️ Formula needs careful handling |
| **Maintainability** | ✅ Easier to debug | ⚠️ More complex logic |

## Common Mistakes

1. **k = 1**: Each window has one element → return all elements as doubles
2. **k = nums.size()**: Single window → return single median
3. **All same elements**: `[3,3,3,3], k=3` → `[3.0, 3.0]`
4. **Duplicates**: `[1,2,2,3], k=3` → Need careful handling of duplicate removal
5. **Large numbers**: Use `long long` or handle overflow in median calculation

### Solution 1
1. **Wrong balance condition**: Should be `lo.size() > hi.size() + 1` not `lo.size() > hi.size()`
2. **Wrong median calculation**: For even k, average max(lo) and min(hi)
3. **Duplicate removal**: Must use `lo.find(out)` not `lo.erase(out)` to remove only one occurrence

### Solution 2
1. **Iterator invalidation**: Adjust `mid` before erasing, not after
2. **Wrong median formula**: For odd k, need to handle differently
3. **Duplicate removal**: Must use `lower_bound` to remove correct element
4. **Iterator bounds**: Check `mid != window.begin()` before `prev(mid)`

## Fixed Solution 2 (Correct Median Calculation)

```cpp
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> medians;
        multiset<int> window(nums.begin(), nums.begin() + k);
        auto mid = next(window.begin(), k / 2);
        
        for (int i = k;; i++) {
            // Calculate median
            if (k % 2 == 1) {
                medians.push_back(*mid);
            } else {
                medians.push_back(((double)(*mid) + *prev(mid)) * 0.5);
            }
            
            if (i == nums.size())
                break;
            
            // Insert new element
            window.insert(nums[i]);
            if (nums[i] < *mid)
                mid--;
            
            // Remove element leaving window
            if (nums[i - k] <= *mid)
                mid++;
            
            window.erase(window.lower_bound(nums[i - k]));
        }
        
        return medians;
    }
};
```

## Related Problems

- [295. Find Median from Data Stream](https://www.leetcode.com/problems/find-median-from-data-stream/) - Two heaps pattern
- [239. Sliding Window Maximum](https://www.leetcode.com/problems/sliding-window-maximum/) - Similar sliding window
- [480. Sliding Window Median](https://www.leetcode.com/problems/sliding-window-median/) - This problem
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://www.leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) - Use two deques

## Pattern Recognition

This problem demonstrates the **Two-Heaps/Multisets Pattern**:
- Maintain two balanced collections (heaps or multisets)
- One contains smaller half, other contains larger half
- Median is easily accessible from the boundaries
- Balance maintained after each insertion/deletion

**Key Insight:**
- For median in sliding window, we need to:
  1. Maintain sorted order
  2. Efficiently add/remove elements
  3. Quickly access middle element(s)

**Applications:**
- Finding median in data streams
- Sliding window statistics
- Order statistics in dynamic sets

## Optimization Tips

### Solution 1: Pre-allocate Result
```cpp
vector<double> res;
res.reserve(nums.size() - k + 1);  // Pre-allocate space
```

### Solution 2: Early Exit
```cpp
if (k == 1) {
    return vector<double>(nums.begin(), nums.end());
}
```

### Memory Optimization
Both solutions are already space-optimal. For very large k, consider using two priority queues instead of multisets (but then deletion becomes O(k) instead of O(log k)).

## Why Multiset Instead of Priority Queue?

**Priority Queue (Heap):**
- ✅ Fast insertion: O(log n)
- ❌ Slow deletion: O(n) - need to find and remove specific element
- ❌ Can't iterate - can't access arbitrary elements

**Multiset:**
- ✅ Fast insertion: O(log n)
- ✅ Fast deletion: O(log n) - can find and remove specific element
- ✅ Can iterate - can access any element via iterator
- ✅ Maintains sorted order

For sliding window median, we need to remove specific elements, so multiset is the right choice.

## Code Quality Notes

1. **Solution 1**: More readable and maintainable
2. **Solution 2**: More compact but requires careful iterator handling
3. **Error Handling**: Both handle edge cases properly
4. **Performance**: Both achieve optimal O(n log k) time complexity

---

*This problem extends the sliding window pattern to find median instead of maximum. The two-heaps pattern (implemented with multisets) is essential for efficiently maintaining order statistics in dynamic sets.*

## Key Takeaways

- **Pattern:** Fixed-size window (this problem)
- For example, for `arr = [2,3,4]`, the median is `3`.
- Maintain a window `[left, right]` satisfying a constraint.

## References

- [LC 480: Sliding Window Median on LeetCode](https://www.leetcode.com/problems/sliding-window-median/)
- [LeetCode Discuss — LC 480: Sliding Window Median](https://www.leetcode.com/problems/sliding-window-median/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/sliding-window-median/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
