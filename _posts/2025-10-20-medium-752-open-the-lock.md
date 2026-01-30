---
layout: post
title: "752. Open the Lock"
date: 2025-10-20 15:30:00 -0700
categories: [leetcode, medium, bfs, shortest-path, lock]
permalink: /2025/10/20/medium-752-open-the-lock/
---

# 752. Open the Lock

## Problem Statement

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the 4 wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or `-1` if it is impossible.

## Examples

**Example 1:**
```
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the deadend "0102".
```

**Example 2:**
```
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
```

**Example 3:**
```
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck in a deadend.
```

## Constraints

- `1 <= deadends.length <= 500`
- `deadends[i].length == 4`
- `target.length == 4`
- target and deadends[i] consist of digits only.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Lock state**: What is the lock state? (Assumption: 4-digit combination lock - each wheel can be 0-9, starting at "0000")

2. **Wheel movement**: How can we move wheels? (Assumption: Turn one wheel one position up or down - "0000" can become "1000" or "9000")

3. **Deadends**: What are deadends? (Assumption: States we cannot visit - if we reach a deadend, we're stuck)

4. **Optimization goal**: What are we optimizing for? (Assumption: Minimum number of moves to reach target from "0000")

5. **Return value**: What should we return? (Assumption: Integer - minimum moves, or -1 if target unreachable)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to find minimum moves. Let me try all possible sequences."

**Naive Solution**: Try all possible lock combinations, find shortest path from "0000" to target avoiding deadends.

**Complexity**: Exponential time, O(1) space

**Issues**:
- Exponential time complexity
- Tries many invalid paths
- Very inefficient
- Doesn't leverage BFS

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "This is a shortest path problem. I can use BFS to find minimum moves."

**Improved Solution**: Use BFS starting from "0000". For each state, generate all 8 possible next states (4 wheels × 2 directions). Skip deadends and visited states.

**Complexity**: O(10^4) time worst case (10000 states), O(10^4) space

**Improvements**:
- BFS finds shortest path
- O(10^4) time is much better than exponential
- Handles deadends correctly
- Visited tracking prevents cycles

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "BFS approach is optimal. Use queue and visited set."

**Best Solution**: BFS is optimal. Use queue for BFS, visited set to track explored states. Generate next states by rotating each wheel up/down. Return depth when target found.

**Complexity**: O(10^4) time, O(10^4) space

**Key Realizations**:
1. BFS is perfect for shortest path problems
2. O(10^4) time is optimal - at most 10000 states
3. Visited set prevents revisiting
4. Generate next states systematically

## Solution Approach

This is a **shortest path problem** that can be solved using **BFS**. We need to find the minimum number of moves to reach the target from "0000" while avoiding deadends.

### Key Insights:

1. **State space**: Each lock state is a 4-digit string (0000-9999)
2. **Transitions**: For each position, we can turn up (+1) or down (-1)
3. **Shortest path**: BFS guarantees minimum number of moves
4. **Deadends**: Act as obstacles that block certain states
5. **Wrapping**: 9 → 0 and 0 → 9 (circular nature)

### Algorithm:

1. **BFS from "0000"**: Use queue to explore all possible states
2. **Level-by-level**: Each level represents one move
3. **State transitions**: Generate all 8 possible next states (4 positions × 2 directions)
4. **Avoid deadends**: Skip states that are in deadends set
5. **Visited tracking**: Prevent revisiting states

## Solution

### **Solution: BFS Shortest Path**

```cpp
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> deads (deadends.begin(), deadends.end());
        unordered_set<string> visited;
        if(deads.contains("0000")) return -1;
        queue<string> q;
        q.push("0000");
        visited.insert("0000");
        int steps = 0;
        while(!q.empty()) {
            int size = q.size();
            while(size--) {
                string curr = q.front();
                q.pop();
                if(curr == target) return steps;
                for(int i = 0; i < 4; i++) {
                    for(int dir = -1; dir <=1; dir+=2) {
                        string next = curr;
                        next[i] = (curr[i] - '0' + dir + 10) % 10 + '0';
                        if(!deads.contains(next) && !visited.contains(next)) {
                            q.push(next);
                            visited.insert(next);
                        }
                    }
                }
            }
            steps++;
        }   
        return -1;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize**: Create deadends set and visited set
2. **Check start**: If "0000" is a deadend, return -1 immediately
3. **BFS setup**: Start with "0000" in queue
4. **Level processing**: Process all states at current level
5. **State transitions**: For each position, try both directions (+1 and -1)
6. **Wrapping**: Use modulo arithmetic for circular nature
7. **Validation**: Check if next state is valid (not deadend, not visited)
8. **Target check**: Return steps when target is reached

### **Example Walkthrough:**

**For `deadends = ["0201","0101","0102","1212","2002"], target = "0202"`:**

```
Level 0: ["0000"] → steps = 0
Level 1: ["1000", "9000", "0100", "0900", "0010", "0090", "0001", "0009"] → steps = 1
Level 2: ["2000", "1100", "1900", "0200", "0800", "0110", "0190", "0020", "0080", "0011", "0019", "0002", "0008"] → steps = 2
Level 3: Continue exploring...
...
Level 6: ["0202"] → Found target! Return 6

Path: "0000" → "1000" → "1100" → "1200" → "1201" → "1202" → "0202"
```

### **Key Implementation Details:**

```cpp
// Circular wrapping for digits
next[i] = (curr[i] - '0' + dir + 10) % 10 + '0';

// For dir = -1: (0 - 1 + 10) % 10 = 9 (0 → 9)
// For dir = +1: (9 + 1 + 10) % 10 = 0 (9 → 0)
```

## Complexity Analysis

### **Time Complexity:** O(10^4) = O(1)
- **State space**: At most 10,000 states (0000-9999)
- **BFS traversal**: Each state visited at most once
- **Transitions**: 8 transitions per state
- **Total**: O(10,000 × 8) = O(80,000) = O(1) constant time

### **Space Complexity:** O(10^4) = O(1)
- **Queue**: O(10,000) - maximum states in queue
- **Visited set**: O(10,000) - stores visited states
- **Deadends set**: O(500) - stores deadend states
- **Total**: O(10,000) = O(1) constant space

## Key Points

1. **BFS for shortest path**: Guarantees minimum number of moves
2. **State space**: 4-digit strings represent lock states
3. **Circular wrapping**: Handle 0 ↔ 9 transitions correctly
4. **Deadend avoidance**: Skip invalid states
5. **Visited tracking**: Prevent infinite loops
6. **Level counting**: Each BFS level represents one move

## Alternative Approaches

### **Bidirectional BFS**
```cpp
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> deads(deadends.begin(), deadends.end());
        if(deads.contains("0000") || deads.contains(target)) return -1;
        
        unordered_set<string> begin, end, visited;
        begin.insert("0000");
        end.insert(target);
        int steps = 0;
        
        while(!begin.empty() && !end.empty()) {
            if(begin.size() > end.size()) swap(begin, end);
            
            unordered_set<string> next;
            for(string curr : begin) {
                if(end.contains(curr)) return steps;
                if(deads.contains(curr) || visited.contains(curr)) continue;
                
                visited.insert(curr);
                for(int i = 0; i < 4; i++) {
                    for(int dir = -1; dir <= 1; dir += 2) {
                        string next_state = curr;
                        next_state[i] = (curr[i] - '0' + dir + 10) % 10 + '0';
                        if(!deads.contains(next_state) && !visited.contains(next_state)) {
                            next.insert(next_state);
                        }
                    }
                }
            }
            begin = next;
            steps++;
        }
        return -1;
    }
};
```

## Related Problems

- [127. Word Ladder](https://leetcode.com/problems/word-ladder/) - Similar BFS shortest path
- [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/) - String transformation
- [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) - Find all shortest paths

## Tags

`BFS`, `Shortest Path`, `Lock`, `State Space`, `Medium`
