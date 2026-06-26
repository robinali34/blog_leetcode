---
layout: post
title: "[Medium] 1344. Angle Between Hands of a Clock"
date: 2026-03-04
categories: [leetcode, medium, math]
tags: [leetcode, medium, math, geometry]
permalink: /2026/03/04/medium-1344-angle-between-hands-of-a-clock/
---
Given two numbers `hour` and `minutes`, return the smaller angle (in degrees) formed between the hour and the minute hand of a clock.

## Examples

**Example 1:**

```
Input: hour = 12, minutes = 30
Output: 165
```

**Example 2:**

```
Input: hour = 3, minutes = 30
Output: 75
```

**Example 3:**

```
Input: hour = 3, minutes = 15
Output: 7.5
```

## Constraints

- `1 <= hour <= 12`
- `0 <= minutes <= 59`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute force** *(this problem)* | Often O(n^2) or O(2^n) | O(n) | Baseline; clarifies the optimization target |
| Sort + scan | O(n log n) | O(1) | Pairs, intervals, greedy ordering |
| Hash map / set | O(n) | O(n) | Frequency, membership, two-sum style |
| Single-pass linear | O(n) | O(1) | Two pointers, sliding window, Kadane |

## Thinking Process

A clock face is a circle of 360 degrees. We need to compute each hand's angle independently, then find the smaller of the two possible angles between them.

### Hour Hand Angle

The hour hand moves based on **both** the hour and the minutes:
- Each hour mark = `360 / 12 = 30` degrees
- The minute component shifts the hour hand by `minutes / 60` of one hour mark

$text{hourAngle} = (text{hour} bmod 12 + text{minutes} / 60.0) × 30.0

### Minute Hand Angle

The minute hand moves based only on minutes:
- Each minute mark = `360 / 60 = 6` degrees

text{minuteAngle} = (text{minutes} bmod 60) × 6.0

### The Smaller Angle

The raw difference might be the "long way around" the clock. The answer is the smaller of the two arcs:

text{answer} = min(text{diff},\ 360 - text{diff})

### Walk-Through: hour=12, minutes=30

```
hourAngle   = (12 % 12 + 30/60.0) * 30.0 = (0 + 0.5) * 30 = 15°
minuteAngle = (30 % 60) * 6.0 = 180°
diff        = |15 - 180| = 165°
answer      = min(165, 360 - 165) = min(165, 195) = 165°
```

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Approach: Direct Calculation -- O(1)$
```cpp
class Solution {
public:
    double angleClock(int hour, int minutes) {
        double hourAngle = (hour % 12 + minutes / 60.0) * 30.0;
        double minuteAngle = (minutes % 60) * 6.0;
        double diff = abs(hourAngle - minuteAngle);
        return min(diff, 360.0 - diff);
    }
};
```

### Solution Explanation

**Approach:** Brute force (this problem)

**Key idea:** A clock face is a circle of 360 degrees. We need to compute each hand's angle independently, then find the smaller of the two possible angles between them.

**How the code works:**
- Each hour mark = `360 / 12 = 30` degrees
- The minute component shifts the hour hand by `minutes / 60` of one hour mark
- Each minute mark = `360 / 60 = 6` degrees

**Walkthrough** — input `hour = 12, minutes = 30`, expected output `165`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- Forgetting that the hour hand **also moves** with minutes (not just snapping to hour marks)
- Not handling `hour = 12` -- must use `hour % 12` to map 12 to 0
- Using integer division for `minutes / 60` instead of `minutes / 60.0` (loses the fractional shift)
- Returning the raw difference without considering the shorter arc (`min(diff, 360 - diff)`)

## Key Takeaways

- Break the problem into independent sub-computations (each hand's angle), then combine
- The `min(diff, 360 - diff)` pattern applies to any "shorter arc on a circle" problem
- Use floating-point division (`60.0`) to preserve the fractional hour-hand movement

## Related Problems

- [2515. Shortest Distance to Target String in a Circular Array](https://www.leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/) -- circular distance pattern

## References

- [LC 1344: Angle Between Hands of a Clock on LeetCode](https://www.leetcode.com/problems/angle-between-hands-of-a-clock/)
- [LeetCode Discuss — LC 1344: Angle Between Hands of a Clock](https://www.leetcode.com/problems/angle-between-hands-of-a-clock/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/angle-between-hands-of-a-clock/editorial/) *(may require premium)*

## Template Reference

- [Math & Geometry](/blog_leetcode/posts/2025-10-29-leetcode-templates-math-geometry/)
