---
layout: post
title: "[Medium] 45. Jump Game II"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp array greedy problem-solving
permalink: /posts/2025-11-18-medium-45-jump-game-ii/
tags: [leetcode, medium, array, greedy, bfs, optimization]
---

# [Medium] 45. Jump Game II

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

- `0 <= j <= nums[i]` and
- `i + j < n`

Return *the minimum number of jumps to reach `nums[n - 1]`*. The test cases are generated such that you can reach `nums[n - 1]`.

## Examples

**Example 1:**
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```
Input: nums = [2,3,0,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Jump definition**: How do jumps work? (Assumption: From index i, can jump to any index from i+1 to i+nums[i] inclusive)

2. **Minimum jumps**: What are we optimizing for? (Assumption: Minimum number of jumps to reach the last index)

3. **Reachability**: Is it guaranteed we can reach the end? (Assumption: Yes - per constraints, guaranteed to reach nums[n-1])

4. **Starting position**: Where do we start? (Assumption: Start at index 0 - first element)

5. **Jump count**: Does staying at same position count as a jump? (Assumption: No - must move forward, each jump advances position)

## Solution: Greedy BFS Approach

**Time Complexity:** O(n) - Single pass through the array  
**Space Complexity:** O(1) - Only using constant extra space

This solution uses a greedy BFS-like approach, tracking the current end of the current jump level and the farthest reachable position.

### Solution: Greedy with BFS Tracking

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int rtn = 0, n = nums.size();
        int curEnd = 0, curFar = 0;
        
        for(int i = 0; i < n - 1; i++) {
            curFar = max(curFar, i + nums[i]);
            
            if(i == curEnd) {
                rtn++;
                curEnd = curFar;
            }
        }
        
        return rtn;
    }
};
```

## How the Algorithm Works

### Step-by-Step Example: `nums = [2,3,1,1,4]`

```
Initial: rtn = 0, curEnd = 0, curFar = 0

i = 0:
  curFar = max(0, 0 + 2) = 2
  i == curEnd (0), so jump!
    rtn = 1
    curEnd = 2  (can reach up to index 2 with 1 jump)

i = 1:
  curFar = max(2, 1 + 3) = 4
  i != curEnd (1 != 2), continue

i = 2:
  curFar = max(4, 2 + 1) = 4
  i == curEnd (2), so jump!
    rtn = 2
    curEnd = 4  (can reach up to index 4 with 2 jumps)

i = 3:
  curFar = max(4, 3 + 1) = 4
  i != curEnd (3 != 4), continue

Loop ends (i < n - 1, so i stops at 3)

Result: rtn = 2
```

### Visual Representation

```
nums = [2, 3, 1, 1, 4]
index:  0  1  2  3  4

Jump 0: Start at index 0
  Can reach: [0, 1, 2]  (curEnd = 2)
  
Jump 1: From indices [0, 1, 2]
  From 0: can reach [0, 1, 2]
  From 1: can reach [1, 2, 3, 4]  ← farthest!
  From 2: can reach [2, 3]
  curFar = 4, curEnd = 4
  
Jump 2: From indices [3, 4]
  Already at index 4 (last index) ✓

Total jumps: 2
```

### Another Example: `nums = [2,3,0,1,4]`

```
i = 0: curFar = 2, i == curEnd → jump, rtn=1, curEnd=2
i = 1: curFar = max(2, 1+3) = 4, i != curEnd
i = 2: curFar = max(4, 2+0) = 4, i == curEnd → jump, rtn=2, curEnd=4
i = 3: curFar = max(4, 3+1) = 4, i != curEnd

Result: 2 jumps
```

## Key Insights

1. **BFS-like Level Traversal**: Each jump represents a "level" in BFS
2. **Greedy Choice**: Always extend to the farthest reachable position
3. **curEnd Tracking**: Marks the boundary of current jump level
4. **curFar Tracking**: Tracks the farthest position reachable from current level
5. **Early Termination**: Stop at `n - 1` since we don't need to jump from last index

## Algorithm Breakdown

```cpp
int jump(vector<int>& nums) {
    int rtn = 0;           // Number of jumps
    int n = nums.size();
    int curEnd = 0;        // End of current jump level
    int curFar = 0;        // Farthest position reachable
    
    // Don't need to process last index
    for(int i = 0; i < n - 1; i++) {
        // Update farthest reachable position
        curFar = max(curFar, i + nums[i]);
        
        // If we've reached the end of current level
        if(i == curEnd) {
            rtn++;              // Make a jump
            curEnd = curFar;    // Update to next level boundary
        }
    }
    
    return rtn;
}
```

## Why This Works

### BFS Analogy

Think of it as BFS levels:
- **Level 0**: Index 0 (starting position)
- **Level 1**: All indices reachable from level 0
- **Level 2**: All indices reachable from level 1
- And so on...

`curEnd` marks the boundary of the current level, and `curFar` tracks the boundary of the next level.

### Greedy Optimality

At each level, we greedily extend to the farthest position because:
1. If we can reach position `j` in `k` jumps, we can reach any position `≤ j` in `k` jumps
2. Extending farthest gives us the most options for the next jump
3. This minimizes the total number of jumps

## Edge Cases

1. **Single element**: `[0]` → return `0` (already at last index)
2. **Can jump directly**: `[3,1,1,1]` → return `1` (one jump from start)
3. **Need multiple jumps**: `[2,3,1,1,4]` → return `2`
4. **Zeros in middle**: `[2,0,1,1,4]` → still solvable (guaranteed by constraints)

## Alternative Approaches

### Approach 2: Dynamic Programming

**Time Complexity:** O(n²)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, INT_MAX);
        dp[0] = 0;
        
        for(int i = 0; i < n; i++) {
            for(int j = 1; j <= nums[i] && i + j < n; j++) {
                dp[i + j] = min(dp[i + j], dp[i] + 1);
            }
        }
        
        return dp[n - 1];
    }
};
```

**Pros:**
- More intuitive for some developers
- Can track path if needed

**Cons:**
- O(n²) time complexity
- O(n) space complexity
- Slower for large inputs

### Approach 3: Explicit BFS Levels

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

More explicit version of the greedy approach:

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int jumps = 0;
        int currentLevelEnd = 0;
        int nextLevelEnd = 0;
        
        for(int i = 0; i < n - 1; i++) {
            nextLevelEnd = max(nextLevelEnd, i + nums[i]);
            
            if(i == currentLevelEnd) {
                jumps++;
                currentLevelEnd = nextLevelEnd;
            }
        }
        
        return jumps;
    }
};
```

**Pros:**
- More explicit variable names
- Easier to understand BFS analogy

**Cons:**
- Slightly more verbose

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Greedy BFS** | O(n) | O(1) | Optimal, simple | Requires understanding |
| **Dynamic Programming** | O(n²) | O(n) | Intuitive | Slower, more space |
| **Explicit BFS** | O(n) | O(1) | Clear variable names | Slightly verbose |

## Implementation Details

### Why `i < n - 1`?

```cpp
for(int i = 0; i < n - 1; i++)
```

We don't need to process the last index because:
- If we reach `n - 1`, we're done (no need to jump from it)
- The loop processes indices where we might need to make decisions
- This avoids unnecessary computation

### curEnd and curFar Relationship

- **curEnd**: Boundary of current BFS level (where current jump can reach)
- **curFar**: Farthest position reachable from current level (boundary of next level)
- When `i == curEnd`, we've explored all positions in current level, so we jump to next level

### Greedy Choice Property

```cpp
curFar = max(curFar, i + nums[i]);
```

This ensures we always know the farthest position reachable from the current level, allowing us to make the optimal greedy choice.

## Common Mistakes

1. **Processing last index**: Including `i < n` instead of `i < n - 1`
2. **Wrong initialization**: Not initializing `curEnd` and `curFar` to 0
3. **Missing jump increment**: Forgetting to increment `rtn` when `i == curEnd`
4. **Wrong update order**: Updating `curEnd` before checking `i == curEnd`
5. **Off-by-one errors**: Incorrect boundary conditions

## Optimization Tips

1. **Early Exit**: Can add check if `curFar >= n - 1` to exit early
2. **Single Pass**: The greedy approach already achieves optimal O(n) time
3. **Space Optimization**: Already O(1) space, no further optimization needed

## Related Problems

- [55. Jump Game](https://leetcode.com/problems/jump-game/) - Check if can reach last index
- [1306. Jump Game III](https://leetcode.com/problems/jump-game-iii/) - Can jump backward/forward
- [1345. Jump Game IV](https://leetcode.com/problems/jump-game-iv/) - Can jump to same value indices
- [1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/) - Maximum score with sliding window
- [1871. Jump Game VII](https://leetcode.com/problems/jump-game-vii/) - Can only jump to '0's

## Real-World Applications

1. **Network Routing**: Finding minimum hops in network
2. **Game Development**: Pathfinding with jump mechanics
3. **Resource Allocation**: Minimizing steps in resource distribution
4. **Algorithm Design**: Understanding greedy optimization

## Pattern Recognition

This problem demonstrates the **"Greedy BFS"** pattern:

```
1. Track current level boundary
2. Track next level boundary
3. When reaching current boundary, advance to next level
4. Always extend to farthest position
```

Similar problems:
- Minimum steps problems
- Level-order traversal variants
- Greedy optimization with boundaries

## Why Greedy is Optimal

1. **Optimal Substructure**: Minimum jumps to position `i` + optimal jump from `i` = optimal solution
2. **Greedy Choice**: Extending farthest gives maximum future options
3. **No Future Dependencies**: Decision at each level doesn't depend on future levels
4. **Monotonicity**: Once we can reach a position, we can always reach it (no need to reconsider)

## Comparison with Jump Game I

| Aspect | Jump Game I | Jump Game II |
|--------|-------------|--------------|
| **Question** | Can reach last index? | Minimum jumps? |
| **Approach** | Track farthest reachable | Track level boundaries |
| **Complexity** | O(n) time, O(1) space | O(n) time, O(1) space |
| **Return** | Boolean | Integer |

---

*This problem is an excellent example of how greedy algorithms can solve optimization problems efficiently, demonstrating the power of BFS-like level traversal with greedy choices.*

