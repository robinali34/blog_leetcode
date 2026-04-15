---
layout: post
title: "[Easy] 217. Contains Duplicate"
date: 2026-03-07
categories: [leetcode, easy, array, hash]
tags: [leetcode, easy, array, hash, sorting]
permalink: /2026/03/07/easy-217-contains-duplicate/
---

Given an integer array `nums`, return `true` if any value appears **at least twice**, and `false` if every element is distinct.

## Examples

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**

```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Thinking Process

We need to detect if any element appears more than once. Three standard approaches:

1. **Hash set** -- insert elements one by one, return `true` the moment we see a duplicate. Early exit.
2. **Sorting** -- sort the array, then adjacent duplicates are next to each other.
3. **One-liner** -- build a set from the array and compare sizes.

## Approach 1: Hash Set -- $O(n)$

Insert elements and check for duplicates in one pass. Early exit on first duplicate.

{% raw %}
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int n : nums) {
            if (seen.contains(n)) return true;
            seen.insert(n);
        }
        return false;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$

## Approach 2: Hash Map -- $O(n)$

Same idea but tracks counts. Slightly more than needed here, but useful when the problem asks *how many* duplicates.

{% raw %}
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (int num : nums) {
            mp[num]++;
            if (mp[num] > 1) return true;
        }
        return false;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$

## Approach 3: Sorting -- $O(n \log n)$

Sort first, then duplicates become adjacent.

{% raw %}
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i] == nums[i - 1]) return true;
        }
        return false;
    }
};
```
{% endraw %}

**Time**: $O(n \log n)$
**Space**: $O(1)$ (in-place sort, modifies input)

## Approach 4: One-Liner -- $O(n)$

Build a set and compare sizes. Clean but no early exit.

{% raw %}
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return unordered_set<int>(nums.begin(), nums.end()).size() != nums.size();
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$

## Comparison

| Approach | Time | Space | Early Exit? | Modifies Input? |
|---|---|---|---|---|
| Hash Set | $O(n)$ | $O(n)$ | Yes | No |
| Hash Map | $O(n)$ | $O(n)$ | Yes | No |
| Sorting | $O(n \log n)$ | $O(1)$ | Yes | Yes |
| One-Liner | $O(n)$ | $O(n)$ | No | No |

## Key Takeaways

- **Hash set with early exit** is the best general approach -- $O(n)$ time with short-circuit on first duplicate
- Sorting trades time for space ($O(1)$ extra) but modifies the input
- The one-liner is elegant but always processes the entire array

## Related Problems

- [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) -- duplicates within distance `k`
- [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) -- duplicates within value range and distance
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) -- frequency counting variant

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
