---
layout: post
title: "[Easy] 219. Contains Duplicate II"
date: 2026-03-07
categories: [leetcode, easy, array, hash, sliding-window]
tags: [leetcode, easy, array, hash, sliding-window]
permalink: /2026/03/07/easy-219-contains-duplicate-ii/
---
Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct** indices `i` and `j` such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Examples

**Example 1:**

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Fixed-size window** *(this problem)* | O(n) | O(1) | Window size known upfront |
| Variable-size window | O(n) | O(1) | Expand/shrink until valid |
| Window + hash map | O(n) | O(k) | Track character/count frequencies |
| Deque window max | O(n) | O(k) | Monotonic deque for max/min in window |

## Thinking Process

This extends [LC 217 Contains Duplicate](/2026/03/07/easy-217-contains-duplicate/) with a distance constraint: duplicates must be within `k` positions of each other.

Two approaches:
1. **Hash map** -- store the last seen index of each value. On a repeat, check if the distance is ≤ k.
2. **Sliding window set** -- maintain a set of the last `k` elements. If the current element is already in the window, it's a nearby duplicate.



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

## Approach 1: Hash Map (Last Index) -- O(n)

Track the most recent index of each value. If we see the same value again and the gap is ≤ k, return `true`. Always update to the latest index.

{% raw %}
```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> lastIdx;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (lastIdx.contains(nums[i]) && i - lastIdx[nums[i]] <= k)
                return true;
            lastIdx[nums[i]] = i;
        }
        return false;
    }
};
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** This extends [LC 217 Contains Duplicate](/2026/03/07/easy-217-contains-duplicate/) with a distance constraint: duplicates must be within `k` positions of each other.

**How the code works:**
1. **Hash map** -- store the last seen index of each value. On a repeat, check if the distance is ≤ k.
2. **Sliding window set** -- maintain a set of the last `k` elements. If the current element is already in the window, it's a nearby duplicate.

**Walkthrough** — input `nums = [1,2,3,1], k = 3`, expected output `true`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Approach 2: Sliding Window Set -- O(n)

Maintain a set of size at most `k`. As the window slides forward, remove the element that falls out of range. If the current element is already in the window, it's a duplicate within distance `k`.

{% raw %}
```cpp
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> window;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (window.contains(nums[i])) return true;
            window.insert(nums[i]);
            if ((int)window.size() > k) window.erase(nums[i - k]);
        }
        return false;
    }
};
```
{% endraw %}

**Time**: O(n)
**Space**: O(min(n, k)) -- the window never exceeds size `k`

## Comparison

| Approach | Time | Space | Advantage |
|---|---|---|---|
| Hash Map | O(n) | O(n) | Simpler logic, stores all indices |
| Sliding Window Set | O(n) | O(min(n, k)) | Better space when k ll n |

## Common Mistakes

- Not updating `lastIdx` to the current index (keeping the first occurrence means you miss closer duplicates)
- Off-by-one: the condition is `i - j <= k`, not `< k`
- Forgetting to evict the oldest element from the sliding window

## Key Takeaways

- **Hash map with last index** is the most intuitive approach
- **Sliding window set** is more space-efficient -- the set acts as a fixed-size window of recent elements
- This is a bridge problem: LC 217 (any duplicate) → LC 219 (nearby duplicate) → LC 220 (nearby + value range)

## Related Problems

- [217. Contains Duplicate](https://www.leetcode.com/problems/contains-duplicate/) -- no distance constraint
- [220. Contains Duplicate III](https://www.leetcode.com/problems/contains-duplicate-iii/) -- distance + value range constraint
- [239. Sliding Window Maximum](https://www.leetcode.com/problems/sliding-window-maximum/) -- sliding window pattern

## References

- [LC 219: Contains Duplicate II on LeetCode](https://www.leetcode.com/problems/contains-duplicate-ii/)
- [LeetCode Discuss — LC 219: Contains Duplicate II](https://www.leetcode.com/problems/contains-duplicate-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/contains-duplicate-ii/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
