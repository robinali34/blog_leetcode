---
layout: post
title: "LeetCode 219. Contains Duplicate II"
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

## Thinking Process

This extends [LC 217 Contains Duplicate](/2026/03/07/easy-217-contains-duplicate/) with a distance constraint: duplicates must be within `k` positions of each other.

Two approaches:
1. **Hash map** -- store the last seen index of each value. On a repeat, check if the distance is $\leq k$.
2. **Sliding window set** -- maintain a set of the last `k` elements. If the current element is already in the window, it's a nearby duplicate.

## Approach 1: Hash Map (Last Index) -- $O(n)$

Track the most recent index of each value. If we see the same value again and the gap is $\leq k$, return `true`. Always update to the latest index.

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
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$

## Approach 2: Sliding Window Set -- $O(n)$

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

**Time**: $O(n)$
**Space**: $O(\min(n, k))$ -- the window never exceeds size `k`

## Comparison

| Approach | Time | Space | Advantage |
|---|---|---|---|
| Hash Map | $O(n)$ | $O(n)$ | Simpler logic, stores all indices |
| Sliding Window Set | $O(n)$ | $O(\min(n, k))$ | Better space when $k \ll n$ |

## Common Mistakes

- Not updating `lastIdx` to the current index (keeping the first occurrence means you miss closer duplicates)
- Off-by-one: the condition is `i - j <= k`, not `< k`
- Forgetting to evict the oldest element from the sliding window

## Key Takeaways

- **Hash map with last index** is the most intuitive approach
- **Sliding window set** is more space-efficient -- the set acts as a fixed-size window of recent elements
- This is a bridge problem: LC 217 (any duplicate) → LC 219 (nearby duplicate) → LC 220 (nearby + value range)

## Related Problems

- [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) -- no distance constraint
- [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) -- distance + value range constraint
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) -- sliding window pattern

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
