---
layout: post
title: "[Medium] 523. Continuous Subarray Sum"
date: 2026-03-04
categories: [leetcode, medium, prefix-sum, hash]
tags: [leetcode, medium, prefix-sum, hash, math]
permalink: /2026/03/04/medium-523-continuous-subarray-sum/
---

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray**, i.e., a contiguous subarray of length **at least 2** whose sum is a multiple of `k`.

## Examples

**Example 1:**

```
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2,4] is a subarray of size 2 whose sum 6 is a multiple of 6.
```

**Example 2:**

```
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23,2,6,4,7] sums to 42, which is a multiple of 6.
```

**Example 3:**

```
Input: nums = [23,2,6,4,7], k = 13
Output: false
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= sum(nums[i]) <= 2^31 - 1`
- `1 <= k <= 2^31 - 1`

## Thinking Process

### Prefix Sum + Modular Arithmetic

If `prefix[i] % k == prefix[j] % k` for some `j < i`, then the subarray sum `prefix[i] - prefix[j]` is divisible by `k`.

We need the subarray to have length **at least 2**, so we need `i - j >= 2`.

### Naive Approach

Check all pairs `(i, j)` -- $O(n^2)$. Too slow.

### Hash Map Approach

Store the **earliest index** where each remainder was seen. When we see the same remainder again, check if the gap is at least 2.

Initialize with `map[0] = -1` to handle the case where a prefix sum itself is divisible by `k` (subarray starting from index 0).

### Hash Set Approach (with 1-Step Delay)

If we only need to know *existence* (not index), we can use a set instead. But to enforce the "length >= 2" constraint, we **delay insertion by one step**: at index `i`, we insert the remainder from index `i-1`. This ensures any match found corresponds to a subarray of size $\geq 2$.

**Why the delay?** Without it, a remainder inserted at index `i` could match at index `i+1`, producing a subarray of size 1.

## Approach 1: Hash Map -- $O(n)$

Store the first occurrence index of each prefix remainder. Only update the map if the remainder hasn't been seen before (we want the earliest index to maximize subarray length).

{% raw %}
```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        mp[0] = -1;
        int sum = 0;

        for (int i = 0; i < (int)nums.size(); i++) {
            sum += nums[i];
            int r = sum % k;
            if (mp.count(r)) {
                if (i - mp[r] >= 2) return true;
            } else {
                mp[r] = i;
            }
        }

        return false;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(\min(n, k))$ for the map

## Approach 2: Hash Set with Delayed Insertion -- $O(n)$

Insert each remainder one step late, so any match guarantees a gap of at least 2.

{% raw %}
```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_set<int> hashSet;
        int sum = 0, prev = 0;

        for (int i = 0; i < (int)nums.size(); i++) {
            sum += nums[i];
            int cur = sum % k;
            if (hashSet.contains(cur)) return true;
            hashSet.insert(prev);
            prev = cur;
        }

        return false;
    }
};
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(\min(n, k))$

**How the delay works:**

| Step | `sum` | `cur` (sum%k) | Check against set | Then insert `prev` | `prev` becomes |
|---|---|---|---|---|---|
| init | 0 | - | - | - | 0 |
| i=0 | nums[0] | nums[0]%k | {} | 0 | nums[0]%k |
| i=1 | nums[0..1] | sum%k | {0} | prefix[1]%k | prefix[2]%k |

At `i=1`, the set contains `{0}` (prefix[0]'s remainder), so any match means the subarray spans indices 0 to 1 -- size 2. The remainder from `i=0` isn't available until `i=2`, enforcing a minimum gap.

## Common Mistakes

- **Missing `map[0] = -1` or initial `prev = 0`** -- fails when the entire prefix sum is divisible by `k` (e.g., `[1, 5]` with `k = 6`)
- **Not enforcing length >= 2** -- inserting the current remainder immediately allows size-1 subarrays to match
- **Updating the map when remainder already exists** -- always keep the *earliest* index to maximize the gap

## Key Takeaways

- **Prefix sum + remainder** is the standard technique for "subarray sum divisible by k"
- The "at least size 2" constraint requires either index tracking (map) or delayed insertion (set)
- Initialize with remainder 0 at a virtual index `-1` to handle subarrays starting from the beginning

## Related Problems

- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) -- prefix sum + hash map (exact sum)
- [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) -- count subarrays with sum divisible by k
- [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/) -- prefix sum with 0/1 transformation

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
