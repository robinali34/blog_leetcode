---
layout: post
title: "[Medium] 55. Jump Game"
date: 2026-01-03 04:00:00 -0700
categories: [leetcode, medium, array, greedy, dynamic-programming]
permalink: /2026/01/03/medium-55-jump-game/
---
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

## Thinking Process

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or* `false` *otherwise*.

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">1D DP recurrence</text>

  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | O(n) | O(n) or O(1) | Linear recurrence |
| 2D DP | O(nm) | O(nm) or O(n) | Grid or two-sequence problems |
| State machine DP | O(n) | O(1) | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | O(n) | Recursive + cache |

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

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

**How the code works:**
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `nums = [2,3,1,1,4]`, expected output `true`:

Jump 1 step from index 0 to 1, then 3 steps to the last index.

**Time:** O(n) where n is the length of the array · **Space:** O(1)

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

## Common Mistakes

1. **Single element**: `[0]` → return `true` (already at last index)
2. **All zeros except first**: `[2,0,0,0]` → return `false`
3. **Can reach immediately**: `[5,1,1,1,1]` → return `true` (jump from index 0)
4. **Zero at start**: `[0,1,2]` → return `false` (cannot move from index 0)
5. **Large jump**: `[1,1,1,100]` → return `true`

1. **Not checking reachability**: Updating `rightMost` from unreachable indices
2. **Wrong condition**: Using `i < rightMost` instead of `i <= rightMost`
3. **Missing early termination**: Not checking if we can reach last index early
4. **Wrong update**: Not using `max()` to update `rightMost`
5. **Index confusion**: Off-by-one errors with array indices

## Related Problems

- [45. Jump Game II](https://www.leetcode.com/problems/jump-game-ii/) - Minimum jumps to reach last index
- [1306. Jump Game III](https://www.leetcode.com/problems/jump-game-iii/) - Can reach index with value 0
- [1345. Jump Game IV](https://www.leetcode.com/problems/jump-game-iv/) - Minimum jumps with additional rules
- [1696. Jump Game VI](https://www.leetcode.com/problems/jump-game-vi/) - Maximum score with sliding window

## Tags

`Array`, `Greedy`, `Dynamic Programming`, `Medium`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 55: Jump Game on LeetCode](https://www.leetcode.com/problems/jump-game/)
- [LeetCode Discuss — LC 55: Jump Game](https://www.leetcode.com/problems/jump-game/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/jump-game/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
