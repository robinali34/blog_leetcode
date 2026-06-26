---
layout: post
title: "[Medium] 46. Permutations"
date: 2025-10-20 14:00:00 -0700
categories: leetcode algorithm medium backtracking recursion
permalink: /2025/10/20/medium-46-permutations/
---
**Difficulty:** Medium  
**Category:** Backtracking, Recursion

Given an array `nums` of distinct integers, return **all the possible permutations**. You can return the answer in **any order**.

## Examples

### Example 1:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:
```
Input: nums = [1]
Output: [[1]]
```

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Thinking Process

This is a classic **backtracking** problem that requires generating all possible permutations of a given array. There are two main approaches:

1. **Backtracking with Swapping:** Generate permutations by swapping elements in-place
2. **STL next_permutation:** Use C++ STL's built-in permutation generator

### Algorithm 1: Backtracking with Swapping
1. **Start from index 0** and try each element at current position
2. **Swap elements** to place them at current position
3. **Recursively generate** permutations for remaining positions
4. **Backtrack** by swapping back to original positions
5. **Base case:** When we've placed all elements, add current permutation

### Algorithm 2: STL next_permutation
1. **Sort the array** to get lexicographically smallest permutation
2. **Use do-while loop** with `next_permutation()` to generate all permutations
3. **Add each permutation** to result vector
4. **Continue until** no more permutations exist

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Backtracking tree</text>

  <circle cx="140" cy="30" r="12" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="34" text-anchor="middle" font-size="9">start</text>
  <line x1="140" y1="42" x2="90" y2="65" stroke="#9A9792"/><line x1="140" y1="42" x2="190" y2="65" stroke="#9A9792"/>
  <circle cx="90" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/><circle cx="190" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/>
  <line x1="90" y1="82" x2="60" y2="100" stroke="#9A9792" stroke-dasharray="3"/><line x1="190" y1="82" x2="220" y2="100" stroke="#9A9792" stroke-dasharray="3"/>
  <text x="140" y="118" text-anchor="middle" font-size="11" fill="#6B6560">choose → explore → undo (prune)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Choose / explore / unchoose** *(this problem)* | O(2^n) | O(n) | Subsets, combinations |
| Constraint pruning | Reduced search | O(n) | Early exit on invalid partial |
| Sort + skip duplicates | O(2^n) | O(n) | Combination sum II style |
| Path recording | O(n!) worst | O(n) | Permutations |

## Solution

### Solution 1: Backtracking with Swapping

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> rtn;
        permute(nums, 0, rtn);
        return rtn;
    }
private:
    void permute(vector<int>& nums, int idx, vector<vector<int>>& rtn) {
        if(idx == nums.size()) {
            rtn.push_back(nums);
            return;
        }
        for(int i = idx; i < (int)nums.size(); i++) {
            swap(nums[idx], nums[i]);
            permute(nums, idx + 1, rtn);
            swap(nums[idx], nums[i]);
        }
    }
};
```

### Solution Explanation

**Approach:** Choose / explore / unchoose (this problem)

**Key idea:** This is a classic **backtracking** problem that requires generating all possible permutations of a given array. There are two main approaches:

**How the code works:**
1. **Backtracking with Swapping:** Generate permutations by swapping elements in-place
2. **STL next_permutation:** Use C++ STL's built-in permutation generator
1. **Start from index 0** and try each element at current position
2. **Swap elements** to place them at current position
3. **Recursively generate** permutations for remaining positions
4. **Backtrack** by swapping back to original positions

### Solution 2: STL next_permutation

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> rtn;
        sort(nums.begin(), nums.end());
        do{
            rtn.push_back(nums);
        } while(next_permutation(nums.begin(), nums.end()));
        return rtn;
    }
};
```
## Explanation

### Solution 1: Backtracking with Swapping

**Step-by-Step Process:**

1. **Base Case:** When `idx == nums.size()`, we've generated a complete permutation
2. **Recursive Case:** For each position `idx`, try every element from `idx` to `n-1`
3. **Swap:** Place element at position `i` to position `idx`
4. **Recurse:** Generate permutations for remaining positions (`idx + 1`)
5. **Backtrack:** Swap back to restore original state

**Example Walkthrough for `nums = [1,2,3]`:**

```
Initial: [1,2,3], idx=0
├─ Swap(0,0): [1,2,3] → Recurse with idx=1
│  ├─ Swap(1,1): [1,2,3] → Recurse with idx=2
│  │  └─ Swap(2,2): [1,2,3] → idx=3, add [1,2,3]
│  └─ Swap(1,2): [1,3,2] → Recurse with idx=2
│     └─ Swap(2,2): [1,3,2] → idx=3, add [1,3,2]
├─ Swap(0,1): [2,1,3] → Recurse with idx=1
│  ├─ Swap(1,1): [2,1,3] → Recurse with idx=2
│  │  └─ Swap(2,2): [2,1,3] → idx=3, add [2,1,3]
│  └─ Swap(1,2): [2,3,1] → Recurse with idx=2
│     └─ Swap(2,2): [2,3,1] → idx=3, add [2,3,1]
└─ Swap(0,2): [3,2,1] → Recurse with idx=1
   ├─ Swap(1,1): [3,2,1] → Recurse with idx=2
   │  └─ Swap(2,2): [3,2,1] → idx=3, add [3,2,1]
   └─ Swap(1,2): [3,1,2] → Recurse with idx=2
      └─ Swap(2,2): [3,1,2] → idx=3, add [3,1,2]
```

### Solution 2: STL next_permutation

**Step-by-Step Process:**

1. **Sort array** to get lexicographically smallest permutation
2. **Generate permutations** using `next_permutation()` in do-while loop
3. **Add each permutation** to result vector
4. **Continue until** `next_permutation()` returns false

**Example Walkthrough for `nums = [1,2,3]`:**

```
Sorted: [1,2,3]
1. [1,2,3] → Add to result
2. [1,3,2] → Add to result  
3. [2,1,3] → Add to result
4. [2,3,1] → Add to result
5. [3,1,2] → Add to result
6. [3,2,1] → Add to result
7. next_permutation returns false → Stop
```

### Solution 1: Backtracking with Swapping
**Time Complexity:** O(n! × n)
- **Permutations:** n! permutations generated
- **Each permutation:** O(n) time to copy array
- **Total:** O(n! × n)

**Space Complexity:** O(n)
- **Recursion depth:** O(n) for the call stack
- **No additional space** for storing permutations during generation

### Solution 2: STL next_permutation
**Time Complexity:** O(n! × n)
- **Permutations:** n! permutations generated
- **Each permutation:** O(n) time for `next_permutation()` and copying
- **Total:** O(n! × n)

**Space Complexity:** O(1)
- **No recursion:** Iterative approach
- **No additional space** beyond input and output
## Key Concepts

1. **Permutations:** All possible arrangements of elements
2. **Backtracking:** Systematic exploration with state restoration
3. **Recursion:** Divide problem into smaller subproblems
4. **State Space:** All possible configurations to explore
5. **Pruning:** Avoiding invalid or duplicate states

This problem is fundamental for understanding backtracking algorithms and is commonly used in interviews to test recursive thinking and state management skills.

## References

- [LC 46: Permutations on LeetCode](https://www.leetcode.com/problems/permutations/)
- [LeetCode Discuss — LC 46: Permutations](https://www.leetcode.com/problems/permutations/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/permutations/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Backtracking Pattern:** Classic recursive approach with state restoration
2. **In-place Generation:** Swapping allows generating permutations without extra space
3. **STL Efficiency:** `next_permutation()` is highly optimized
4. **Lexicographic Order:** STL approach generates permutations in sorted order
5. **State Management:** Proper backtracking ensures all possibilities are explored
