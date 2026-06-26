---
layout: post
title: "[Medium] 683. K Empty Slots"
date: 2025-12-30 15:30:00 -0700
categories: [leetcode, medium, sliding-window, two-pointers, array]
permalink: /2025/12/30/medium-683-k-empty-slots/
---
You have `n` bulbs in a row numbered from `1` to `n`. Initially, all the bulbs are turned off. On day `i` (for `i` from `0` to `n-1`), we turn on exactly one bulb. The position of this bulb is given by `bulbs[i]`.

Given an integer `k`, return the **minimum day number** such that there exist two turned-on bulbs that have **exactly `k` bulbs between them** that are all turned off. If there isn't such day, return `-1`.

## Thinking Process

You have `n` bulbs in a row numbered from `1` to `n`. Initially, all the bulbs are turned off. On day `i` (for `i` from `0` to `n-1`), we turn on exactly one bulb. The position of this bulb is given by `bulbs[i]`.

Given an integer `k`, return the **minimum day number** such that there exist two turned-on bulbs that have **exactly `k` bulbs between them** that are all turned off. If there isn't such day, return `-1`.

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

## Examples

**Example 1:**
```
Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
On day 1: bulbs[0] = 1, first bulb is turned on: [1, 0, 0]
On day 2: bulbs[1] = 3, third bulb is turned on: [1, 0, 1]
On day 3: bulbs[2] = 2, second bulb is turned on: [1, 1, 1]
We return 2 because on day 2, there were two on bulbs with one off bulb between them.
```

**Example 2:**
```
Input: bulbs = [1,2,3], k = 1
Output: -1
Explanation: No such day exists where two bulbs are on with exactly one bulb off between them.
```

## Constraints

- `n == bulbs.length`
- `1 <= n <= 2 * 10^4`
- `1 <= bulbs[i] <= n`
- All values in `bulbs` are **unique**.
- `0 <= k <= n`

## Algorithm Breakdown

### **Key Insight: Window Validation**

The algorithm checks if a window `[left, right]` is valid by ensuring:
- Both endpoints (`left` and `right`) are blooming bulbs
- All bulbs between them (`left+1` to `right-1`) are **off** (bloom later)

**Validation Condition:**
```cpp
for(int i = left + 1; i < right; i++) {
    if(days[i] < days[left] || days[i] < days[right]) {
        // Invalid: bulb i blooms before one of the endpoints
    }
}
```

**Why this works:**
- If `days[i] < days[left]`: bulb `i` blooms before left endpoint → cannot have k empty slots
- If `days[i] < days[right]`: bulb `i` blooms before right endpoint → cannot have k empty slots
- Only if all `days[i] > max(days[left], days[right])`: all middle bulbs bloom after both endpoints → valid window

### **Optimization: Early Termination**

When an invalid bulb is found, we don't need to check positions before it:
```cpp
if(days[i] < days[left] || days[i] < days[right]) {
    left = i;  // Move left to invalid position
    right = i + k + 1;  // Update right accordingly
    break;  // Stop checking this window
}
```

This optimization ensures we don't check redundant windows.

### Complexity
### **Time Complexity:** O(n)
- **Build days array**: O(n) - single pass through bulbs
- **Sliding window**: O(n) - each position visited at most once
  - When invalid bulb found, we skip to that position
  - Each position is checked at most once
- **Total**: O(n)

### **Space Complexity:** O(n)
- **Days array**: O(n) - stores day for each position
- **Total**: O(n)

## Key Points

1. **Position-to-Day Mapping**: Convert problem from "which position blooms on day i" to "which day does position i bloom"
2. **Window Size**: Use window of size `k + 2` (two endpoints + k empty slots)
3. **Validation Logic**: All middle bulbs must bloom after both endpoints
4. **Early Termination**: Skip invalid windows efficiently
5. **Result Calculation**: Day when both endpoints are on = `max(days[left], days[right])`

## Detailed Example Walkthrough

### **Example: `bulbs = [6,5,8,9,7,1,10,2,3,4], k = 2`**

```
Step 1: Build days array
bulbs = [6, 5, 8, 9, 7, 1, 10, 2, 3, 4]
days  = [6, 8, 9, 10, 2, 3, 4, 5, 7, 1]
        (position 1 blooms on day 6, position 2 on day 8, etc.)

Step 2: Check window [0, 3] (positions 1 and 4, k=2 means positions 2,3 between)
Check positions 1, 2 (between 0 and 3):
- days[1] = 8, days[2] = 9
- days[0] = 6, days[3] = 10
- days[1] = 8 > days[0] = 6 ✓ and days[1] = 8 < days[3] = 10 ✗
- Invalid! Position 2 blooms before position 4

Step 3: Move to window [1, 4]
Check positions 2, 3 (between 1 and 4):
- days[2] = 9, days[3] = 10
- days[1] = 8, days[4] = 2
- days[2] = 9 > days[1] = 8 ✓ but days[2] = 9 > days[4] = 2 ✗
- Invalid! Position 3 blooms before position 5

Step 4: Move to window [4, 7]
Check positions 5, 6 (between 4 and 7):
- days[5] = 3, days[6] = 4
- days[4] = 2, days[7] = 5
- days[5] = 3 > days[4] = 2 ✓ but days[5] = 3 < days[7] = 5 ✗
- Invalid! Position 6 blooms before position 8

Step 5: Move to window [5, 8]
Check positions 6, 7 (between 5 and 8):
- days[6] = 4, days[7] = 5
- days[5] = 3, days[8] = 7
- days[6] = 4 > days[5] = 3 ✓ and days[6] = 4 < days[8] = 7 ✗
- Invalid! Position 7 blooms before position 9

Step 6: Move to window [6, 9]
Check positions 7, 8 (between 6 and 9):
- days[7] = 5, days[8] = 7
- days[6] = 4, days[9] = 1
- days[7] = 5 > days[6] = 4 ✓ but days[7] = 5 > days[9] = 1 ✗
- Invalid! Position 8 blooms before position 10

No valid window found → Return -1
```

## Edge Cases

1. **k = 0**: Two adjacent bulbs must both be on
2. **k = n-2**: First and last bulbs with all middle bulbs off
3. **No solution**: All bulbs bloom in order, no valid window
4. **Single valid window**: Only one pair of positions satisfies condition

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [683. K Empty Slots](https://www.leetcode.com/problems/k-empty-slots/) - Current problem
- [239. Sliding Window Maximum](https://www.leetcode.com/problems/sliding-window-maximum/) - Sliding window technique
- [76. Minimum Window Substring](https://www.leetcode.com/problems/minimum-window-substring/) - Variable sliding window
- [3. Longest Substring Without Repeating Characters](https://www.leetcode.com/problems/longest-substring-without-repeating-characters/) - Sliding window

## Tags

`Sliding Window`, `Two Pointers`, `Array`, `Medium`

## Key Takeaways

- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

## References

- [LC 683: K Empty Slots on LeetCode](https://www.leetcode.com/problems/k-empty-slots/)
- [LeetCode Discuss — LC 683: K Empty Slots](https://www.leetcode.com/problems/k-empty-slots/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/k-empty-slots/editorial/) *(may require premium)*

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
