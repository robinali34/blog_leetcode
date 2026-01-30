---
layout: post
title: "55. Jump Game"
date: 2026-01-03 04:00:00 -0700
categories: [leetcode, medium, array, greedy, dynamic-programming]
permalink: /2026/01/03/medium-55-jump-game/
---

# 55. Jump Game

## Problem Statement

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or* `false` *otherwise*.

## Examples

**Example 1:**
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Jump definition**: How do jumps work? (Assumption: From index i, can jump to any index from i+1 to i+nums[i] inclusive)

2. **Reachability**: What are we checking? (Assumption: Whether we can reach the last index starting from index 0)

3. **Return value**: What should we return? (Assumption: Boolean - true if can reach last index, false otherwise)

4. **Starting position**: Where do we start? (Assumption: Start at index 0 - first element)

5. **Zero values**: What if nums[i] is 0? (Assumption: Cannot jump forward from that position - stuck unless already past it)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to check if I can reach the end. Let me try all possible paths."

**Naive Solution**: Use DFS/BFS to explore all possible jump paths from start to end.

**Complexity**: O(2^n) worst case time, O(n) space

**Issues**:
- Exponential time complexity
- Explores many redundant paths
- Very inefficient
- Doesn't leverage greedy property

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use DP to track reachability from each position."

**Improved Solution**: Use DP where dp[i] = true if position i is reachable. For each position, mark all reachable positions as true.

**Complexity**: O(n²) time, O(n) space

**Improvements**:
- O(n²) time instead of exponential
- Correctly finds reachability
- Still can be optimized
- Better than brute-force

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "I can use greedy approach - track rightmost reachable position."

**Best Solution**: Greedy approach. Track rightmost reachable position. For each position, if it's reachable, update rightmost position. If rightmost < current position, cannot reach.

**Complexity**: O(n) time, O(1) space

**Key Realizations**:
1. Greedy approach is optimal
2. O(n) time is optimal - single pass
3. O(1) space is optimal
4. Track rightmost reachable position is key insight

## Solution Approach

This is a **greedy algorithm** problem. The key insight is to track the **rightmost reachable position** as we iterate through the array. If we can reach an index, we can potentially reach further positions from there.

### Key Insights:

1. **Rightmost Reachable**: Track the farthest position we can reach
2. **Greedy Update**: At each index, update the rightmost reachable position
3. **Reachability Check**: Only update if current index is reachable (`i <= rightMost`)
4. **Early Termination**: If rightmost position reaches last index, return `true`

### Algorithm:

1. **Initialize**: `rightMost = 0` (starting position)
2. **Iterate**: For each index `i`:
   - Check if `i` is reachable (`i <= rightMost`)
   - If reachable, update `rightMost = max(rightMost, i + nums[i])`
   - If `rightMost >= N - 1`, return `true`
3. **Return**: `false` if we can't reach the last index

## Solution

### **Solution: Greedy with Rightmost Tracking**

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        const int N = nums.size();
        int rightMost = 0;
        for(int i = 0; i < N; i++) {
            if(i <= rightMost) {
                rightMost = max(rightMost, i + nums[i]);
                if(rightMost >= N - 1) return true;
            }
        }
        return false;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize (Lines 4-5)**:
   - `N`: Length of the array
   - `rightMost`: Farthest position we can reach (starts at 0)

2. **Iterate Through Array (Lines 6-11)**:
   - **For each index `i`**:
     - **Check reachability**: `if(i <= rightMost)`
       - If current index is reachable, we can jump from here
     - **Update rightmost**: `rightMost = max(rightMost, i + nums[i])`
       - From index `i`, we can reach up to `i + nums[i]`
       - Update `rightMost` to the maximum reachable position
     - **Early termination**: `if(rightMost >= N - 1) return true`
       - If we can reach the last index, return `true` immediately

3. **Return (Line 12)**:
   - If we finish the loop without reaching the last index, return `false`

### **Example Walkthrough:**

**Example 1: `nums = [2,3,1,1,4]`**

```
Initial: rightMost = 0, N = 5

i=0: nums[0]=2
  Check: 0 <= 0? Yes (reachable)
  Update: rightMost = max(0, 0+2) = 2
  Check: 2 >= 4? No
  Continue

i=1: nums[1]=3
  Check: 1 <= 2? Yes (reachable)
  Update: rightMost = max(2, 1+3) = 4
  Check: 4 >= 4? Yes ✓
  Return: true
```

**Example 2: `nums = [3,2,1,0,4]`**

```
Initial: rightMost = 0, N = 5

i=0: nums[0]=3
  Check: 0 <= 0? Yes
  Update: rightMost = max(0, 0+3) = 3
  Check: 3 >= 4? No
  Continue

i=1: nums[1]=2
  Check: 1 <= 3? Yes
  Update: rightMost = max(3, 1+2) = 3
  Check: 3 >= 4? No
  Continue

i=2: nums[2]=1
  Check: 2 <= 3? Yes
  Update: rightMost = max(3, 2+1) = 3
  Check: 3 >= 4? No
  Continue

i=3: nums[3]=0
  Check: 3 <= 3? Yes
  Update: rightMost = max(3, 3+0) = 3
  Check: 3 >= 4? No
  Continue

i=4: nums[4]=4
  Check: 4 <= 3? No (not reachable!)
  Cannot update rightMost
  Continue

Loop ends: rightMost = 3 < 4
Return: false
```

**Example 3: `nums = [2,0,0]`**

```
Initial: rightMost = 0, N = 3

i=0: nums[0]=2
  Check: 0 <= 0? Yes
  Update: rightMost = max(0, 0+2) = 2
  Check: 2 >= 2? Yes ✓
  Return: true
```

## Algorithm Breakdown

### **Why Greedy Works**

The greedy strategy is optimal because:
1. **Local Optimal**: At each reachable index, we maximize the rightmost reachable position
2. **No Regret**: If we can reach index `i`, we can always reach any position we could have reached by a different path
3. **Optimal Substructure**: The ability to reach the last index depends only on the rightmost reachable position

### **Key Insight: Rightmost Reachable Position**

Instead of tracking all possible positions, we only need to track:
- **The farthest position we can reach** from any reachable index
- If `rightMost >= N - 1`, we can reach the last index
- If at any point `i > rightMost`, we're stuck (cannot reach index `i`)

### **Reachability Check**

The condition `if(i <= rightMost)` ensures:
- We only update `rightMost` from positions we can actually reach
- If `i > rightMost`, we cannot reach index `i`, so we cannot jump from there
- This prevents invalid updates

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the length of the array
  - Single pass through the array
  - Constant time operations for each element
- **Space Complexity**: O(1)
  - Only using a few variables (`rightMost`, `N`, `i`)
  - No additional data structures

## Key Points

1. **Greedy Strategy**: Track rightmost reachable position
2. **Reachability Check**: Only update from reachable indices
3. **Early Termination**: Return `true` as soon as we can reach the last index
4. **Optimal**: Greedy approach finds the answer in one pass
5. **Simple**: Straightforward implementation

## Alternative Approaches

### **Approach 1: Greedy (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Optimal solution, most efficient

### **Approach 2: Dynamic Programming (Bottom-Up)**
- **Time**: O(n²)
- **Space**: O(n)
- **Use when**: Need to track all reachable positions
- **Idea**: `dp[i]` = true if index `i` is reachable

### **Approach 3: Backtracking**
- **Time**: O(2^n) worst case
- **Space**: O(n) for recursion stack
- **Not practical**: Too slow for large inputs

## Edge Cases

1. **Single element**: `[0]` → return `true` (already at last index)
2. **All zeros except first**: `[2,0,0,0]` → return `false`
3. **Can reach immediately**: `[5,1,1,1,1]` → return `true` (jump from index 0)
4. **Zero at start**: `[0,1,2]` → return `false` (cannot move from index 0)
5. **Large jump**: `[1,1,1,100]` → return `true`

## Common Mistakes

1. **Not checking reachability**: Updating `rightMost` from unreachable indices
2. **Wrong condition**: Using `i < rightMost` instead of `i <= rightMost`
3. **Missing early termination**: Not checking if we can reach last index early
4. **Wrong update**: Not using `max()` to update `rightMost`
5. **Index confusion**: Off-by-one errors with array indices

## Related Problems

- [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) - Minimum jumps to reach last index
- [1306. Jump Game III](https://leetcode.com/problems/jump-game-iii/) - Can reach index with value 0
- [1345. Jump Game IV](https://leetcode.com/problems/jump-game-iv/) - Minimum jumps with additional rules
- [1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/) - Maximum score with sliding window

## Comparison with LC 45 (Jump Game II)

**LC 55 (Jump Game):**
- Goal: Check if we can reach the last index
- Approach: Track rightmost reachable position
- Return: `true` or `false`

**LC 45 (Jump Game II):**
- Goal: Find minimum number of jumps to reach last index
- Approach: Track current jump level and farthest reachable
- Return: Minimum number of jumps

## Tags

`Array`, `Greedy`, `Dynamic Programming`, `Medium`

