---
layout: post
title: "[Medium] 681. Next Closest Time"
date: 2025-12-30 16:30:00 -0700
categories: [leetcode, medium, string, simulation, brute-force]
permalink: /2025/12/30/medium-681-next-closest-time/
---
Given a time represented in the format `"HH:MM"`, form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, `"01:34"`, `"12:09"` are all valid. `"1:34"`, `"12:9"` are all invalid.

## Thinking Process

Given a time represented in the format `"HH:MM"`, form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, `"01:34"`, `"12:09"` are all valid. `"1:34"`, `"12:9"` are all invalid.

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Examples

**Example 1:**
```
Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later. It is not 19:33, because this occurs 23 hours and 59 minutes later.
```

**Example 2:**
```
Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
```

## Constraints

- `time` is in the format `"HH:MM"`.
- `0 <= HH < 24`
- `0 <= MM < 60`

## Algorithm Breakdown

### **Key Insight: Time Wrapping**

The algorithm handles day wrapping correctly:
```cpp
if(i >= day) i -= day;
```

This ensures that after 23:59, we continue checking from 00:00 of the next day.

### **Digit Validation**

For each candidate time, we check all four digit positions:
- Hour tens: `h1 / 10` (0-2)
- Hour ones: `h1 % 10` (0-9)
- Minute tens: `m1 / 10` (0-5)
- Minute ones: `m1 % 10` (0-9)

All four digits must be in the allowed set.

### **Time Range**

The loop checks from `start + 1` to `end`:
- `start + 1`: Next minute after current time
- `end = getMin(h + 24, m)`: Current time + 24 hours
- This covers the entire next 24-hour period

### Complexity
### **Time Complexity:** O(1)
- **Maximum iterations**: At most 1440 minutes (24 hours)
- **Each iteration**: O(1) - constant time digit checks
- **Total**: O(1) - bounded by constant 1440

### **Space Complexity:** O(1)
- **Allowed digits array**: O(10) = O(1)
- **Variables**: O(1)
- **Total**: O(1)

## Key Points

1. **Digit Reuse**: Any digit can be used multiple times
2. **Next Day**: Solution may wrap to next day if no valid time in current day
3. **Time Format**: Always output in `"HH:MM"` format with leading zeros
4. **Brute Force**: Check all possible times until valid one found
5. **Efficient**: O(1) time complexity since bounded by 24 hours

## Detailed Example Walkthrough

### **Example: `time = "12:09"`**

```
Step 1: Parse input
h = 12, m = 9
start = getMin(12, 9) = 12*60 + 9 = 729 minutes

Step 2: Build allowed digits
con = [true, true, true, false, false, false, false, false, false, true]
      (digits 0, 1, 2, 9 are allowed)

Step 3: Simulate time progression
i = 730 (12:10): h1=12, m1=10
  - h1/10 = 1 ✓, h1%10 = 2 ✓, m1/10 = 1 ✓, m1%10 = 0 ✓
  - Valid! Result: "12:10"
```

### **Example: `time = "01:00"`**

```
Step 1: Parse input
h = 1, m = 0
start = getMin(1, 0) = 60 minutes

Step 2: Build allowed digits
con = [true, true, false, false, false, false, false, false, false, false]
      (digits 0, 1 are allowed)

Step 3: Simulate time progression
i = 61 (01:01): h1=1, m1=1
  - h1/10 = 0 ✓, h1%10 = 1 ✓, m1/10 = 0 ✓, m1%10 = 1 ✓
  - Valid! Result: "01:01"
```

## Edge Cases

1. **Same digits**: `"11:11"` → next valid time using only 1s
2. **All zeros**: `"00:00"` → next time using only 0s (00:00 again if wrapping)
3. **Late in day**: `"23:59"` → may wrap to next day
4. **Single digit set**: `"00:00"` or `"11:11"` → limited options

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [681. Next Closest Time](https://www.leetcode.com/problems/next-closest-time/) - Current problem
- [949. Largest Time for Given Digits](https://www.leetcode.com/problems/largest-time-for-given-digits/) - Similar time manipulation
- [539. Minimum Time Difference](https://www.leetcode.com/problems/minimum-time-difference/) - Time calculation

## Tags

`String`, `Simulation`, `Brute Force`, `Time`, `Medium`

## Key Takeaways

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

## References

- [LC 681: Next Closest Time on LeetCode](https://www.leetcode.com/problems/next-closest-time/)
- [LeetCode Discuss — LC 681: Next Closest Time](https://www.leetcode.com/problems/next-closest-time/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/next-closest-time/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
