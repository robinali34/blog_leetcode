---
layout: post
title: "[Medium] 2342. Max Sum of a Pair With Equal Sum of Digits"
date: 2026-04-11
categories: [leetcode, medium, hash-map, array]
tags: [leetcode, medium, hash-map, array, greedy]
permalink: /2026/04/11/medium-2342-max-sum-of-a-pair-with-equal-sum-of-digits/
---

Given an array `nums`, find two indices `i` and `j` (`i != j`) such that the **digit sum** of `nums[i]` equals the digit sum of `nums[j]`, and return the **maximum** value of `nums[i] + nums[j]`. Return `-1` if no such pair exists.

## Examples

**Example 1:**

```
Input: nums = [18,43,36,13,7]
Output: 54
Explanation:
  digitSum(18) = 9, digitSum(36) = 9
  18 + 36 = 54 is the maximum pair with equal digit sums.
```

**Example 2:**

```
Input: nums = [10,12,19,14]
Output: -1
Explanation: No two numbers share the same digit sum.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Thinking Process

To maximize the sum of a pair with equal digit sums, we want the **two largest** numbers in each digit-sum group.

### Key Insight

We don't need to store all numbers per group -- just the **largest so far**. As we scan, for each number:
1. Compute its digit sum
2. If we've seen a number with the same digit sum, try pairing with the best one
3. Update the best for this digit sum

This is the "best seen so far" pattern -- same idea as tracking the min price in Best Time to Buy and Sell Stock.

### Walk-through

```
nums = [18, 43, 36, 13, 7]

x=18: digitSum=9,  best[9]=0  → no pair, best[9]=18
x=43: digitSum=7,  best[7]=0  → no pair, best[7]=43
x=36: digitSum=9,  best[9]=18 → pair: 18+36=54, rtn=54, best[9]=36
x=13: digitSum=4,  best[4]=0  → no pair, best[4]=13
x=7:  digitSum=7,  best[7]=43 → pair: 43+7=50, rtn=max(54,50)=54, best[7]=43

Answer: 54 ✓
```

### Why `best` Array of Size 100?

Max digit sum occurs for `999,999,999` = $9 \times 9 = 81$. An array of size 100 covers all possible digit sums with margin.

## Solution: Greedy (Best Seen So Far) -- $O(n)$

{% raw %}
```cpp
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        vector<int> best(100, 0);
        int rtn = -1;
        for (int x : nums) {
            int s = digitSum(x);
            if (best[s] > 0) {
                rtn = max(rtn, best[s] + x);
            }
            best[s] = max(best[s], x);
        }
        return rtn;
    }

private:
    int digitSum(int x) {
        int s = 0;
        while (x) {
            s += x % 10;
            x /= 10;
        }
        return s;
    }
};
```
{% endraw %}

**Time**: $O(n \cdot d)$ where $d$ = number of digits (at most 10) $\approx O(n)$
**Space**: $O(1)$ -- fixed-size array of 100

## Common Mistakes

- Storing all numbers per group and sorting (works but $O(n \log n)$ instead of $O(n)$)
- Forgetting to return `-1` when no valid pair exists
- Updating `best[s]` before checking the pair (would pair a number with itself)

## Key Takeaways

- **"Best pair in a group"** = track the best seen so far per group, check pair on each new element
- Using a fixed-size array instead of a hash map leverages the bounded digit-sum range for better constants
- The "update after pairing" order is critical -- pair with the old best, then potentially replace it

## Related Problems

- [1. Two Sum](https://leetcode.com/problems/two-sum/) -- pair finding with hash map
- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) -- "best seen so far" pattern
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) -- grouping by canonical key
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) -- digit/character frequency

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
