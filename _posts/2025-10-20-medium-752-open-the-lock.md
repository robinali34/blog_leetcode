---
layout: post
title: "[Medium] 752. Open the Lock"
date: 2025-10-20 15:30:00 -0700
categories: [leetcode, medium, bfs, shortest-path, lock]
permalink: /2025/10/20/medium-752-open-the-lock/
---
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

## Thinking Process

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the 4 wheels.

- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Queue BFS** *(this problem)* | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| Level-order BFS | O(n) | O(w) | Process by depth/layer |

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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

**How the code works:**
- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.

**Walkthrough** — input `deadends = ["0201","0101","0102","1212","2002"], target = "0202"`, expected output `6`:

A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the deadend "0102".

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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [127. Word Ladder](https://www.leetcode.com/problems/word-ladder/) - Similar BFS shortest path
- [433. Minimum Genetic Mutation](https://www.leetcode.com/problems/minimum-genetic-mutation/) - String transformation
- [126. Word Ladder II](https://www.leetcode.com/problems/word-ladder-ii/) - Find all shortest paths

## Tags

`BFS`, `Shortest Path`, `Lock`, `State Space`, `Medium`

## Key Takeaways

- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.

## References

- [LC 752: Open the Lock on LeetCode](https://www.leetcode.com/problems/open-the-lock/)
- [LeetCode Discuss — LC 752: Open the Lock](https://www.leetcode.com/problems/open-the-lock/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/open-the-lock/editorial/) *(may require premium)*

## Template Reference

- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
