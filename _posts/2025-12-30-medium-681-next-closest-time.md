---
layout: post
title: "681. Next Closest Time"
date: 2025-12-30 16:30:00 -0700
categories: [leetcode, medium, string, simulation, brute-force]
permalink: /2025/12/30/medium-681-next-closest-time/
---

# 681. Next Closest Time

## Problem Statement

Given a time represented in the format `"HH:MM"`, form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, `"01:34"`, `"12:09"` are all valid. `"1:34"`, `"12:9"` are all invalid.

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Time format**: What is the time format? (Assumption: "HH:MM" - 24-hour format, HH from 00-23, MM from 00-59)

2. **Digit restriction**: What digits can we use? (Assumption: Only digits that appear in the input time - reuse digits from current time)

3. **Next closest**: What does "next closest" mean? (Assumption: Next valid time (including next day) that uses only allowed digits)

4. **Return format**: What should we return? (Assumption: String in "HH:MM" format - next closest time)

5. **Wrapping**: Can time wrap to next day? (Assumption: Yes - if no valid time today, find next day's time)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Generate all possible times using only digits from the input time. Check each time in chronological order starting from the input time, wrapping to the next day if needed. Return the first valid time found. This approach works but requires generating many combinations and checking validity, which is inefficient.

**Step 2: Semi-Optimized Approach (7 minutes)**

Extract all unique digits from the input time. Generate all valid HH:MM combinations using these digits. Sort them chronologically and find the next time after the input. Handle wrapping to the next day. This reduces the search space but still requires generating and validating many combinations.

**Step 3: Optimized Solution (8 minutes)**

Simulate time progression: start from the input time and increment by one minute. For each time, check if all digits are from the allowed set. Continue until we find a valid time or wrap around to the next day. This achieves O(24 × 60) = O(1440) worst-case time, which is efficient. Alternatively, we can generate all valid times first and then find the next one, but simulation is simpler. The key insight is that there are only 1440 minutes in a day, so we can simulate minute by minute efficiently.

## Solution Approach

This problem requires finding the next closest time (including next day) that can be formed using only the digits from the current time. We can solve this by **simulating time progression** minute by minute and checking if each new time uses only allowed digits.

### Key Insights:

1. **Allowed Digits**: Extract all unique digits from the input time
2. **Time Progression**: Increment time minute by minute, wrapping around after 23:59
3. **Validation**: Check if all digits in the new time are in the allowed set
4. **Next Day**: If no valid time found in current day, check next day (wraps to 00:00)

### Algorithm:

1. **Extract digits**: Get all digits from input time
2. **Convert to minutes**: Convert current time to total minutes for easy manipulation
3. **Increment and check**: Add 1 minute at a time, check if valid
4. **Return first valid**: Return the first time that uses only allowed digits

## Solution

### **Solution: Minute-by-Minute Simulation**

```cpp
class Solution {
private:
    int getMin(int h, int m) {
        return h * 60 + m;
    }
public:
    string nextClosestTime(string time) {
        int h, m;
        sscanf(time.c_str(), "%d:%d", &h, &m);
        vector<bool> con(10, false);
        con[time[0] - '0'] = con[time[1] - '0'] = con[time[3] - '0'] = con[time[4] - '0'] = true;

        const int start = getMin(h, m), end = getMin(h + 24, m), day = getMin(24, 0);
        int h1 = 0, m1 = 0;
        for(int i = start + 1; i <= end; i++) {
            if(i >= day) i -= day;
            h1 = i / 60;
            m1 = i - h1 * 60;
            if(con[h1/10] && con[h1%10] && con[m1/10] && con[m1 % 10]) break;
        }
        char rtn[60];
        sprintf(rtn, "%02d:%02d", h1, m1);
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Helper Function (Lines 3-5)**:
   - `getMin(h, m)`: Converts hours and minutes to total minutes since midnight
   - Formula: `h * 60 + m`

2. **Parse Input (Lines 8-9)**:
   - Extract hours and minutes from input string using `sscanf`
   - Format: `"HH:MM"` → `h` and `m`

3. **Build Allowed Digits Set (Lines 10-11)**:
   - Create boolean array `con[10]` to track allowed digits (0-9)
   - Mark digits from input time: `time[0]`, `time[1]`, `time[3]`, `time[4]`
   - Example: `"19:34"` → `con[1]=true, con[9]=true, con[3]=true, con[4]=true`

4. **Time Range Setup (Line 13)**:
   - `start`: Current time in minutes
   - `end`: Current time + 24 hours (to include next day)
   - `day`: 24 hours in minutes (1440 minutes)

5. **Simulate Time Progression (Lines 14-20)**:
   - Start from `start + 1` (next minute)
   - Loop until `end` (covers current day and next day)
   - Handle day wrap: if `i >= day`, subtract `day` to wrap to next day
   - Extract hours and minutes: `h1 = i / 60`, `m1 = i % 60`
   - Check if all digits are allowed:
     - `h1/10` (tens digit of hour)
     - `h1%10` (ones digit of hour)
     - `m1/10` (tens digit of minute)
     - `m1%10` (ones digit of minute)

6. **Format Output (Lines 21-23)**:
   - Format result as `"HH:MM"` with leading zeros
   - Use `sprintf` with `"%02d:%02d"` format

### **Example Walkthrough:**

**For `time = "19:34"`:**

```
Step 1: Parse input
h = 19, m = 34
start = getMin(19, 34) = 19*60 + 34 = 1174 minutes

Step 2: Build allowed digits
con = [false, true, false, true, true, false, false, false, false, true]
      (digits 1, 3, 4, 9 are allowed)

Step 3: Simulate from 19:35 onwards
i = 1175 (19:35): h1=19, m1=35
  - h1/10 = 1 ✓, h1%10 = 9 ✓, m1/10 = 3 ✓, m1%10 = 5 ✗
  - Invalid (digit 5 not allowed)

i = 1176 (19:36): h1=19, m1=36
  - h1/10 = 1 ✓, h1%10 = 9 ✓, m1/10 = 3 ✓, m1%10 = 6 ✗
  - Invalid (digit 6 not allowed)

i = 1177 (19:37): h1=19, m1=37
  - h1/10 = 1 ✓, h1%10 = 9 ✓, m1/10 = 3 ✓, m1%10 = 7 ✗
  - Invalid (digit 7 not allowed)

i = 1178 (19:38): h1=19, m1=38
  - h1/10 = 1 ✓, h1%10 = 9 ✓, m1/10 = 3 ✓, m1%10 = 8 ✗
  - Invalid (digit 8 not allowed)

i = 1179 (19:39): h1=19, m1=39
  - h1/10 = 1 ✓, h1%10 = 9 ✓, m1/10 = 3 ✓, m1%10 = 9 ✓
  - Valid! All digits (1, 9, 3, 9) are allowed

Step 4: Format output
Result: "19:39"
```

**For `time = "23:59"`:**

```
Step 1: Parse input
h = 23, m = 59
start = getMin(23, 59) = 23*60 + 59 = 1439 minutes

Step 2: Build allowed digits
con = [false, false, true, true, false, true, false, false, false, true]
      (digits 2, 3, 5, 9 are allowed)

Step 3: Simulate from 00:00 next day onwards
i = 1440 (00:00): h1=0, m1=0
  - h1/10 = 0 ✗, h1%10 = 0 ✗
  - Invalid (digit 0 not allowed)

... (skip invalid times) ...

i = 1342 (22:22): h1=22, m1=22
  - h1/10 = 2 ✓, h1%10 = 2 ✓, m1/10 = 2 ✓, m1%10 = 2 ✓
  - Valid! All digits (2, 2, 2, 2) are allowed

Step 4: Format output
Result: "22:22"
```

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

## Complexity Analysis

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

## Alternative Approaches

### **Approach 1: Minute-by-Minute (Current Solution)**
- **Time**: O(1) - at most 1440 iterations
- **Space**: O(1)
- **Best for**: Simple and straightforward

### **Approach 2: Generate All Valid Times**
- **Time**: O(1) - generate all valid times, sort, find next
- **Space**: O(1)
- **Generate**: All combinations of allowed digits, filter valid times

### **Approach 3: Greedy Construction**
- **Time**: O(1)
- **Space**: O(1)
- **Build**: Try to increment each component (minute, hour) with allowed digits

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

## Related Problems

- [681. Next Closest Time](https://leetcode.com/problems/next-closest-time/) - Current problem
- [949. Largest Time for Given Digits](https://leetcode.com/problems/largest-time-for-given-digits/) - Similar time manipulation
- [539. Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/) - Time calculation

## Tags

`String`, `Simulation`, `Brute Force`, `Time`, `Medium`

