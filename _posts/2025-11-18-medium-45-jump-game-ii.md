---
layout: post
title: "[Medium] 45. Jump Game II"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp array greedy problem-solving
permalink: /posts/2025-11-18-medium-45-jump-game-ii/
tags: [leetcode, medium, array, greedy, bfs, optimization]
---
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

## Thinking Process

1. **BFS-like Level Traversal**: Each jump represents a "level" in BFS

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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** 1. **BFS-like Level Traversal**: Each jump represents a "level" in BFS

**How the code works:**
1. **BFS-like Level Traversal**: Each jump represents a "level" in BFS
- BFS visits nodes in non-decreasing distance from the source.
- Queue guarantees shortest path in unweighted graphs.
- Process level by level when counting layers or distances.

**Walkthrough** — input `nums = [2,3,1,1,4]`, expected output `2`:

The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Greedy BFS** | O(n) | O(1) | Optimal, simple | Requires understanding |
| **Dynamic Programming** | O(n²) | O(n) | Intuitive | Slower, more space |
| **Explicit BFS** | O(n) | O(1) | Clear variable names | Slightly verbose |
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

### Complexity
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

1. **Single element**: `[0]` → return `0` (already at last index)
2. **Can jump directly**: `[3,1,1,1]` → return `1` (one jump from start)
3. **Need multiple jumps**: `[2,3,1,1,4]` → return `2`
4. **Zeros in middle**: `[2,0,1,1,4]` → still solvable (guaranteed by constraints)

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

- [55. Jump Game](https://www.leetcode.com/problems/jump-game/) - Check if can reach last index
- [1306. Jump Game III](https://www.leetcode.com/problems/jump-game-iii/) - Can jump backward/forward
- [1345. Jump Game IV](https://www.leetcode.com/problems/jump-game-iv/) - Can jump to same value indices
- [1696. Jump Game VI](https://www.leetcode.com/problems/jump-game-vi/) - Maximum score with sliding window
- [1871. Jump Game VII](https://www.leetcode.com/problems/jump-game-vii/) - Can only jump to '0's

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

## Key Takeaways

1. **BFS-like Level Traversal**: Each jump represents a "level" in BFS
2. **Greedy Choice**: Always extend to the farthest reachable position
3. **curEnd Tracking**: Marks the boundary of current jump level
4. **curFar Tracking**: Tracks the farthest position reachable from current level
5. **Early Termination**: Stop at `n - 1` since we don't need to jump from last index

## References

- [LC 45: Jump Game II on LeetCode](https://www.leetcode.com/problems/jump-game-ii/)
- [LeetCode Discuss — LC 45: Jump Game II](https://www.leetcode.com/problems/jump-game-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/jump-game-ii/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
