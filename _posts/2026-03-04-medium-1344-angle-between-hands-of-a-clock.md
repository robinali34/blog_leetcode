---
layout: post
title: "LeetCode 1344. Angle Between Hands of a Clock"
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

## Thinking Process

A clock face is a circle of 360 degrees. We need to compute each hand's angle independently, then find the smaller of the two possible angles between them.

### Hour Hand Angle

The hour hand moves based on **both** the hour and the minutes:
- Each hour mark = `360 / 12 = 30` degrees
- The minute component shifts the hour hand by `minutes / 60` of one hour mark

$$\text{hourAngle} = (\text{hour} \bmod 12 + \text{minutes} / 60.0) \times 30.0$$

### Minute Hand Angle

The minute hand moves based only on minutes:
- Each minute mark = `360 / 60 = 6` degrees

$$\text{minuteAngle} = (\text{minutes} \bmod 60) \times 6.0$$

### The Smaller Angle

The raw difference might be the "long way around" the clock. The answer is the smaller of the two arcs:

$$\text{answer} = \min(\text{diff},\ 360 - \text{diff})$$

### Walk-Through: hour=12, minutes=30

```
hourAngle   = (12 % 12 + 30/60.0) * 30.0 = (0 + 0.5) * 30 = 15°
minuteAngle = (30 % 60) * 6.0 = 180°
diff        = |15 - 180| = 165°
answer      = min(165, 360 - 165) = min(165, 195) = 165°
```

## Approach: Direct Calculation -- $O(1)$

{% raw %}
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
{% endraw %}

**Time**: $O(1)$
**Space**: $O(1)$

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

- [2515. Shortest Distance to Target String in a Circular Array](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/) -- circular distance pattern

## Template Reference

- [Math & Geometry](/blog_leetcode/posts/2025-10-29-leetcode-templates-math-geometry/)
