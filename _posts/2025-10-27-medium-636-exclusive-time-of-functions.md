---
layout: post
title: "LC 636: Exclusive Time of Functions"
date: 2025-10-27 21:04:00 -0700
categories: leetcode medium stack parsing
permalink: /posts/2025-10-27-medium-636-exclusive-time-of-functions/
tags: [leetcode, medium, stack, parsing, logs, simulation]
---

# LC 636: Exclusive Time of Functions

**Difficulty:** Medium  
**Category:** Stack, Parsing, Simulation  
**Companies:** Amazon, Facebook, Google, Twitter

## Problem Statement

On a **single-threaded** CPU, we can only execute one function at a time. When a function call starts, it's recorded with a start timestamp. When a call ends, it's recorded with an end timestamp. Functions can call other functions, creating a call stack.

Given an integer `n` representing the number of functions, and an array `logs`, where `logs[i]` represents the `i-th` log message formatted as `"{function_id}:{"start"|"end"}:{timestamp}"`, return an array where each element is the exclusive time of that function.

**Exclusive time** is the sum of execution times for all calls to a function, excluding time spent calling other functions.

### Examples

**Example 1:**
```
Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]
Explanation:
- Function 0 starts at 0 and ends at 6, taking 6 units total
- Function 0 calls function 1, which runs from 2 to 5 (3 units)
- Function 0 exclusive time: 6 - 3 = 3 units
- Function 1 exclusive time: 5 - 2 + 1 = 4 units (inclusive of end timestamp)
```

**Example 2:**
```
Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:end:6"]
Output: [3]
Explanation:
- First call: starts at 0, second call starts at 2
- Second call ends at 5 (duration 4)
- First call ends at 6 (duration 7 total, minus 4 from nested call = 3)
```

**Example 3:**
```
Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
Output: [4,1]
Explanation:
- Function 0: recursive calls from 0-5 (3 units) + 6-7 (1 unit) = 4 total
- Function 1: runs at timestamp 6 (1 unit)
```

### Constraints

- `1 <= n <= 100`
- `1 <= logs.length <= 500`
- `0 <= function_id < n`
- `0 <= timestamp <= 10^9`
- No two start events will happen at the same timestamp
- No two end events will happen at the same timestamp
- Each function call has a matching start and end event

## Solution Approaches

### Approach 1: Stack-Based Time Tracking (Recommended)

**Key Insight:** Use a stack to track the current call stack. When a function starts, push it. When it ends, calculate its duration and subtract that time from its parent.

**Algorithm:**
1. Parse each log entry to extract function ID, action (start/end), and timestamp
2. Maintain a stack of active function calls
3. When a function **starts**: push to stack
4. When a function **ends**: 
   - Pop the top function and calculate its duration
   - Add duration to the function's exclusive time
   - Subtract duration from the parent function (if exists) in the stack

**Time Complexity:** O(m) where m is the number of logs  
**Space Complexity:** O(n) for the stack

```cpp
class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> rtn(n, 0);
        stack<pair<int, int>> st;  // {function_id, start_time}
        
        for(const string& log: logs) {
            int id = 0, time = 0;
            bool isStart = false;

            // Parse function ID
            int i = 0;
            while(log[i] != ':') {
                id = id * 10 + (log[i] - '0');
                i++;
            }
            i++;
            
            // Parse action (start or end)
            if(log[i] == 's') {
                isStart = true;
                i += 6;  // skip "start"
            } else {
                i += 4;  // skip "end"
            }
            
            // Parse timestamp
            while(i < (int) log.size()) {
                time = time * 10 + (log[i] - '0');
                i++;
            }
            
            if(isStart) {
                // Push function to stack
                st.push({id, time});
            } else {
                // Pop and calculate duration
                auto [funcId, startTime] = st.top();
                st.pop();
                int duration = time - startTime + 1;  // +1 to include end timestamp
                rtn[funcId] += duration;

                // Subtract from parent function
                if(!st.empty()) {
                    rtn[st.top().first] -= duration;
                }
            }
        }
        return rtn;
    }
};
```

### Approach 2: Using stringstream for Parsing

**Algorithm:** Same logic but using C++ stringstream for cleaner parsing.

```cpp
class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> rtn(n, 0);
        stack<pair<int, int>> st;
        
        for(const string& log: logs) {
            stringstream ss(log);
            string token;
            
            // Parse ID
            getline(ss, token, ':');
            int id = stoi(token);
            
            // Parse action
            getline(ss, token, ':');
            bool isStart = (token == "start");
            
            // Parse timestamp
            getline(ss, token, ':');
            int time = stoi(token);
            
            if(isStart) {
                st.push({id, time});
            } else {
                auto [funcId, startTime] = st.top();
                st.pop();
                int duration = time - startTime + 1;
                rtn[funcId] += duration;
                
                if(!st.empty()) {
                    rtn[st.top().first] -= duration;
                }
            }
        }
        return rtn;
    }
};
```

### Approach 3: Store Only Start Time

**Algorithm:** Store only the start timestamp on the stack.

```cpp
class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> rtn(n, 0);
        stack<int> st;  // Only store function IDs
        
        int prevTime = 0;
        for(const string& log: logs) {
            stringstream ss(log);
            string token;
            
            getline(ss, token, ':');
            int id = stoi(token);
            
            getline(ss, token, ':');
            bool isStart = (token == "start");
            
            getline(ss, token, ':');
            int time = stoi(token);
            
            if(isStart) {
                if(!st.empty()) {
                    rtn[st.top()] += time - prevTime;
                }
                st.push(id);
                prevTime = time;
            } else {
                rtn[st.top()] += time - prevTime + 1;
                st.pop();
                prevTime = time + 1;
            }
        }
        return rtn;
    }
};
```

## Algorithm Analysis

### Key Insights

1. **Nested Function Calls**: The stack naturally models the call stack hierarchy
2. **Exclusive vs Inclusive Time**: When a function calls another, the time spent in the nested call must be subtracted from the parent
3. **End Timestamp Inclusion**: The end timestamp is inclusive in exclusive time calculation (`+1`)
4. **Parent Tracking**: The stack maintains parent-child relationships

### Understanding the Subtraction Logic

```
Function 0: starts at 0
  Function 1: starts at 2
    Function 1: ends at 5 (duration = 4)
  Function 0: ends at 6

Without subtraction:
  Function 0: 0 to 6 = 7 units (WRONG - includes nested call)
  Function 1: 2 to 5 = 4 units (CORRECT)

With subtraction:
  Function 0: 7 - 4 = 3 units (CORRECT)
  Function 1: 4 units (CORRECT)
```

## Implementation Details

### Manual String Parsing

```cpp
// Parse function ID (numeric string to int)
int id = 0;
while(log[i] != ':') {
    id = id * 10 + (log[i] - '0');
    i++;
}

// Check for "start" or "end"
if(log[i + 1] == 's') isStart = true;
```

### Stack Operations

```cpp
// Start event: push function onto stack
if(isStart) {
    st.push({id, time});
}

// End event: pop and calculate
else {
    auto [funcId, startTime] = st.top();
    st.pop();
    int duration = time - startTime + 1;
    rtn[funcId] += duration;
    
    // Subtract from parent
    if(!st.empty()) {
        rtn[st.top().first] -= duration;
    }
}
```

## Edge Cases

1. **Single Function**: Only one function, no nesting → straightforward timing
2. **Recursive Calls**: Same function called recursively → handled by stack
3. **Multiple Separate Calls**: Same function called at different times → duration summed
4. **Immediate Returns**: Start and end at same timestamp → duration = 1
5. **Deep Nesting**: Multiple levels of function calls → stack maintains hierarchy

## Follow-up Questions

- What if logs could be out of order?
- How would you handle multi-threaded execution?
- What if you needed to track inclusive time instead?
- How would you detect mismatched start/end events?

## Related Problems

- [LC 394: Decode String](https://leetcode.com/problems/decode-string/) - Nested structure processing
- [LC 150: Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) - Stack-based evaluation
- [LC 1249: Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) - Stack validation

## Optimization Techniques

1. **Stack for Hierarchy**: Perfect data structure for call stack modeling
2. **Subtraction Trick**: Efficient way to calculate exclusive time
3. **Inclusive Counting**: End timestamp included in duration calculation
4. **Parent Tracking**: Stack automatically maintains parent information

## Code Quality Notes

1. **Readability**: Approach 1 with manual parsing is most educational
2. **Maintainability**: Approach 2 with stringstream is cleaner
3. **Performance**: All approaches are O(n) time and space
4. **Correctness**: Key insight is the subtraction from parent

---

*This problem elegantly demonstrates how to model a call stack using a stack data structure and calculate exclusive time by tracking parent-child relationships in function calls.*

