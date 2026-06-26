---
layout: post
title: "[Medium] 75. Sort Colors"
date: 2025-12-02 00:00:00 -0800
categories: leetcode algorithm medium cpp array two-pointers sorting problem-solving
---
Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

## Examples

**Example 1:**
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Example 2:**
```
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## Thinking Process

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

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
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Solution

**Time Complexity:** O(n) - Single pass through the array  
**Space Complexity:** O(1) - In-place sorting with only constant extra space

The Dutch National Flag algorithm uses two pointers to partition the array into three regions:
- **Left region (0s)**: `[0, p0)`
- **Middle region (1s)**: `[p0, i)`
- **Right region (2s)**: `(p2, n-1]`

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int p0 = 0, p2 = n - 1;
        
        for(int i = 0; i <= p2; i++) {
            while(i <= p2 && nums[i] == 2) {
                swap(nums[i], nums[p2]);
                p2--;
            }
            
            if(nums[i] == 0) {
                swap(nums[i], nums[p0]);
                p0++;
            }
        }
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

**How the code works:**
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `nums = [2,0,2,1,1,0]`, expected output `[0,0,1,1,2,2]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Operation | Time | Space |
|-----------|------|-------|
| Single pass | O(n) | O(1) |
| Swaps | O(n) worst case | - |
| **Overall** | **O(n)** | **O(1)** |
## Key Points

1. **In-place sorting**: No extra space needed (except for variables)
2. **Single pass**: Each element is visited at most twice
3. **Two pointers**: `p0` for 0s, `p2` for 2s
4. **While loop for 2s**: Ensures swapped 2s are handled correctly
5. **Order matters**: Handle 2s first (with while), then 0s

## Common Mistakes

1. **All same color**: `[0,0,0]`, `[1,1,1]`, `[2,2,2]`
2. **Already sorted**: `[0,1,2]`
3. **Reverse sorted**: `[2,1,0]`
4. **Single element**: `[1]`

1. **Not using `while` for 2s**: If you use `if`, swapped 2s might be left in wrong position
2. **Wrong loop condition**: Must use `i <= p2`, not `i < n`
3. **Incrementing `i` after swapping 0**: After swapping with `p0`, we should increment `i` (which happens naturally in the for loop)
4. **Not handling swapped 2s**: The `while` loop is crucial for correctness

## Alternative Approach: Counting Sort

For this specific problem (only 3 values), we could use counting sort:

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0};
        for(int num : nums) count[num]++;
        
        int idx = 0;
        for(int color = 0; color < 3; color++) {
            while(count[color]-- > 0) {
                nums[idx++] = color;
            }
        }
    }
};
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1) - Only 3 counters

However, the two-pointer approach is more general and can be extended to partition problems.

## Key Takeaways

- **Pattern:** Opposite ends (this problem)
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.

## References

- [LC 75: Sort Colors on LeetCode](https://www.leetcode.com/problems/sort-colors/)
- [LeetCode Discuss — LC 75: Sort Colors](https://www.leetcode.com/problems/sort-colors/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/sort-colors/editorial/) *(may require premium)*

## Related Problems

- [324. Wiggle Sort II](https://www.leetcode.com/problems/wiggle-sort-ii/) - Uses 3-way partition
- [215. Kth Largest Element in an Array](https://www.leetcode.com/problems/kth-largest-element-in-an-array/) - Partitioning
- [912. Sort an Array](https://www.leetcode.com/problems/sort-an-array/) - General sorting
- [283. Move Zeroes](https://www.leetcode.com/problems/move-zeroes/) - Two-pointer partitioning

## Pattern Recognition

This problem demonstrates the **"Two-Pointer Partitioning"** pattern:

```
1. Use two pointers to maintain boundaries
2. Process elements in a single pass
3. Swap elements to move them to correct regions
4. Handle edge cases (like swapped values) carefully
```

Similar problems:
- Partition array by value
- Move specific elements to one side
- Three-way partitioning

## Follow-up: Minimize Swaps While Moving 0s to Front and 2s to End

**Problem Variant:** What if we only need to ensure 0s are in front, and during swaps, we want to minimize the number of swaps while moving as many 2s to the end as possible?

### Solution: Two-Pass Approach

The key insight is to process in the optimal order:
1. **First pass**: Move all 2s to the end (maximizes 2s at end)
2. **Second pass**: Move all 0s to the front (ensures 0s in front)

This minimizes swaps because:
- Moving 2s first doesn't interfere with 0s
- Moving 0s after ensures they go to the front without disrupting 2s

```cpp
class Solution {
public:
    void sortColorsMinSwaps(vector<int>& nums) {
        int n = nums.size();
        int p0 = 0, p2 = n - 1;
        
        // First pass: Move all 2s to the end
        while(p0 <= p2) {
            if(nums[p2] == 2) {
                p2--;
            } else if(nums[p0] == 2) {
                swap(nums[p0], nums[p2]);
                p2--;
            } else {
                p0++;
            }
        }
        
        // Second pass: Move all 0s to the front
        p0 = 0;
        for(int i = 0; i <= p2; i++) {
            if(nums[i] == 0) {
                swap(nums[i], nums[p0]);
                p0++;
            }
        }
    }
};
```

### Alternative: Single-Pass Greedy Approach

We can also do this in a single pass by being more strategic about swaps:

```cpp
class Solution {
public:
    void sortColorsMinSwaps(vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = n - 1;
        int i = 0;
        
        while(i <= right) {
            if(nums[i] == 0) {
                // Move 0 to front
                swap(nums[i], nums[left]);
                left++;
                i++;
            } else if(nums[i] == 2) {
                // Move 2 to end, but don't increment i
                // because swapped element needs to be checked
                swap(nums[i], nums[right]);
                right--;
            } else {
                // nums[i] == 1, leave it
                i++;
            }
        }
    }
};
```

### Why This Minimizes Swaps?

1. **Prioritize 2s**: By moving 2s to the end first, we avoid moving them multiple times
2. **Avoid redundant swaps**: Once a 2 is at the end, we don't touch it again
3. **0s naturally go to front**: After 2s are moved, 0s can be placed at the front without interference

### Example: Minimizing Swaps

**Input:** `nums = [2,0,2,1,1,0]`

**Two-pass approach:**
```
Initial: [2, 0, 2, 1, 1, 0]

Pass 1 (Move 2s to end):
[2, 0, 2, 1, 1, 0] -> swap(0,5): [0, 0, 2, 1, 1, 2]
[0, 0, 2, 1, 1, 2] -> swap(2,4): [0, 0, 1, 1, 2, 2]
Total swaps: 2

Pass 2 (Move 0s to front):
[0, 0, 1, 1, 2, 2] -> already in place
Total swaps: 0

Final: [0, 0, 1, 1, 2, 2]
Total swaps: 2
```

**Original approach (for comparison):**
```
[2, 0, 2, 1, 1, 0] -> swap(0,5): [0, 0, 2, 1, 1, 2] (swap 1)
[0, 0, 2, 1, 1, 2] -> swap(2,4): [0, 0, 1, 1, 2, 2] (swap 2)
Total swaps: 2
```

In this case, both approaches have the same number of swaps, but the two-pass approach is more predictable and easier to reason about.

### Example 2: Some 2s Remain in Middle (Swap Minimization)

**Input:** `nums = [1,2,0,2,1,0]`

**Two-pass approach (minimize swaps):**
```
Initial: [1, 2, 0, 2, 1, 0]

Pass 1 (Move 2s to end):
[1, 2, 0, 2, 1, 0] -> p2=5 is 0, p0=0 is 1, move p0
[1, 2, 0, 2, 1, 0] -> p0=1 is 2, swap(1,5): [1, 0, 0, 2, 1, 2]
[1, 0, 0, 2, 1, 2] -> p2=4 is 1, p0=1 is 0, move p0
[1, 0, 0, 2, 1, 2] -> p0=2 is 0, move p0
[1, 0, 0, 2, 1, 2] -> p0=3 is 2, swap(3,4): [1, 0, 0, 1, 2, 2]
Total swaps: 2

Pass 2 (Move 0s to front):
[1, 0, 0, 1, 2, 2] -> swap(0,1): [0, 1, 0, 1, 2, 2]
[0, 1, 0, 1, 2, 2] -> swap(1,2): [0, 0, 1, 1, 2, 2]
Total swaps: 2

Final: [0, 0, 1, 1, 2, 2]
Total swaps: 4
```

**Note:** In this case, we successfully moved all 2s to the end. But consider a variant where we want to minimize swaps even if it means some 2s stay in the middle.

### Example 3: Constrained Scenario - Some 2s Stay in Middle

**Input:** `nums = [1,2,0,2,1,0,2,1]`

**Scenario:** If we want to minimize swaps and 0s are the priority, we might accept some 2s in the middle.

**Approach 1: Prioritize 0s first (minimize swaps)**
```
Initial: [1, 2, 0, 2, 1, 0, 2, 1]

Move 0s to front:
[1, 2, 0, 2, 1, 0, 2, 1] -> swap(0,2): [0, 2, 1, 2, 1, 0, 2, 1]
[0, 2, 1, 2, 1, 0, 2, 1] -> swap(1,5): [0, 0, 1, 2, 1, 2, 2, 1]
Swaps: 2

Result: [0, 0, 1, 2, 1, 2, 2, 1]
- 0s in front: ✓
- Some 2s in middle: positions 3, 5, 6
- Total swaps: 2 (minimized)
```

**Approach 2: Move all 2s to end (more swaps)**
```
Initial: [1, 2, 0, 2, 1, 0, 2, 1]

Pass 1: Move 2s to end
[1, 2, 0, 2, 1, 0, 2, 1] -> swap(1,7): [1, 1, 0, 2, 1, 0, 2, 2]
[1, 1, 0, 2, 1, 0, 2, 2] -> swap(3,6): [1, 1, 0, 2, 1, 0, 2, 2]
Wait, position 6 is already 2. Let me recalculate:
After first swap: [1, 1, 0, 2, 1, 0, 2, 2], p2=6
p0=0 is 1, move p0
p0=1 is 1, move p0  
p0=2 is 0, move p0
p0=3 is 2, swap(3,6): [1, 1, 0, 2, 1, 0, 2, 2] (no change, both 2)
Actually: [1, 1, 0, 2, 1, 0, 2, 2] -> swap(3,5): [1, 1, 0, 0, 1, 2, 2, 2]
Swaps: 2

Pass 2: Move 0s to front
[1, 1, 0, 0, 1, 2, 2, 2] -> swap(0,2): [0, 1, 1, 0, 1, 2, 2, 2]
[0, 1, 1, 0, 1, 2, 2, 2] -> swap(1,3): [0, 0, 1, 1, 1, 2, 2, 2]
Swaps: 2

Final: [0, 0, 1, 1, 1, 2, 2, 2]
Total swaps: 4
```

**Comparison:**
- Approach 1: 2 swaps, but 2s remain scattered → `[0, 0, 1, 2, 1, 2, 2, 1]`
- Approach 2: 4 swaps, all 2s at end → `[0, 0, 1, 1, 1, 2, 2, 2]`

If minimizing swaps is the priority, Approach 1 is better, even though some 2s remain in the middle.

### Example 4: Many 2s, Few 0s - Minimal Swaps

**Input:** `nums = [2,2,2,0,2,2,2]`

**Two-pass approach:**
```
Initial: [2, 2, 2, 0, 2, 2, 2]

Pass 1 (Move 2s to end):
Since most positions are already 2s, we just need to move the 0:
[2, 2, 2, 0, 2, 2, 2] -> swap(0,3): [0, 2, 2, 2, 2, 2, 2]
Swaps: 1

Pass 2 (Move 0s to front):
[0, 2, 2, 2, 2, 2, 2] -> already in place
Swaps: 0

Final: [0, 2, 2, 2, 2, 2, 2]
Total swaps: 1
```

**Key observation:** With only 1 swap, we achieved:
- 0s in front: ✓
- Most 2s at end: ✓ (all except position 1, which is still in the 2s region)
- Minimal swaps: ✓

### Example 5: 2s Scattered, Minimize Swaps

**Input:** `nums = [1,2,1,0,2,1,0,2]`

**Two-pass approach:**
```
Initial: [1, 2, 1, 0, 2, 1, 0, 2]

Pass 1 (Move 2s to end):
[1, 2, 1, 0, 2, 1, 0, 2] -> p2=7 is 2, skip
[1, 2, 1, 0, 2, 1, 0, 2] -> p2=6 is 0, p0=0 is 1, move p0
[1, 2, 1, 0, 2, 1, 0, 2] -> p0=1 is 2, swap(1,6): [1, 0, 1, 0, 2, 1, 2, 2]
[1, 0, 1, 0, 2, 1, 2, 2] -> p2=5 is 1, p0=2 is 1, move p0
[1, 0, 1, 0, 2, 1, 2, 2] -> p0=3 is 0, move p0
[1, 0, 1, 0, 2, 1, 2, 2] -> p0=4 is 2, swap(4,5): [1, 0, 1, 0, 1, 2, 2, 2]
Swaps: 2

Pass 2 (Move 0s to front):
[1, 0, 1, 0, 1, 2, 2, 2] -> swap(0,1): [0, 1, 1, 0, 1, 2, 2, 2]
[0, 1, 1, 0, 1, 2, 2, 2] -> swap(1,3): [0, 0, 1, 1, 1, 2, 2, 2]
Swaps: 2

Final: [0, 0, 1, 1, 1, 2, 2, 2]
Total swaps: 4
```

**If we prioritize 0s first (alternative):**
```
[1, 2, 1, 0, 2, 1, 0, 2] -> swap(0,3): [0, 2, 1, 1, 2, 1, 0, 2]
[0, 2, 1, 1, 2, 1, 0, 2] -> swap(1,6): [0, 0, 1, 1, 2, 1, 2, 2]
Now move 2s: [0, 0, 1, 1, 2, 1, 2, 2] -> swap(4,6): [0, 0, 1, 1, 1, 2, 2, 2]
Total swaps: 3 (better!)
```

This shows that sometimes prioritizing 0s first can result in fewer total swaps, depending on the distribution.

### Complexity Analysis

| Approach | Time | Space | Swaps |
|----------|------|-------|-------|
| Two-pass | O(n) | O(1) | Minimized |
| Single-pass | O(n) | O(1) | Minimized |
| Original | O(n) | O(1) | May be suboptimal |

### Key Differences from Original

1. **Order of operations**: Process 2s first, then 0s
2. **Swap minimization**: Avoids redundant swaps
3. **Goal**: Ensure 0s in front + maximize 2s at end (1s can be anywhere in middle)
