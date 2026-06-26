---
layout: post
title: "[Medium] 969. Pancake Sorting"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp array sorting problem-solving
permalink: /posts/2025-11-18-medium-969-pancake-sorting/
tags: [leetcode, medium, array, sorting, greedy, pancake-flip]
---
Given an array of integers `arr`, sort the array by performing a series of **pancake flips**.

In one pancake flip we do the following steps:

- Choose an integer `k` where `1 <= k <= arr.length`.
- Reverse the sub-array `arr[0...k-1]` (0-indexed).

For example, if `arr = [3,2,1,4]` and we performed a pancake flip choosing `k = 3`, we reverse the sub-array `[3,2,1]`, so `arr = [1,2,3,4]`.

Return *an array of the `k`-values corresponding to a sequence of pancake flips that sort `arr`*. Any valid answer that sorts the array within `10 * arr.length` flips will be judged as correct.

## Examples

**Example 1:**
```
Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values [4,2,4,3]:
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k=4): arr = [1, 4, 2, 3]
After 2nd flip (k=2): arr = [4, 1, 2, 3]
After 3rd flip (k=4): arr = [3, 2, 1, 4]
After 4th flip (k=3): arr = [1, 2, 3, 4]
```

**Example 2:**
```
Input: arr = [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
```

## Constraints

- `1 <= arr.length <= 100`
- `1 <= arr[i] <= arr.length`
- All integers in `arr` are unique (i.e. `arr` is a permutation of the integers from `1` to `arr.length`).

## Thinking Process

1. **Greedy Strategy**: Place largest elements first, working from right to left
- First flip: Bring target element to front (if not already there)
- Second flip: Move target element to its correct position

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

## Solution

**Time Complexity:** O(n²) - For each of n elements, we may need to search and flip  
**Space Complexity:** O(1) excluding output array

The key insight is to use a greedy strategy: place the largest unsorted element in its correct position, then work on the next largest, and so on.

### Solution: Greedy with Helper Functions

```cpp
class Solution {
private:
    void flip(vector<int>& subarr, int k) {
        int i = 0;
        while(i < k / 2) {
            int tmp = subarr[i];
            subarr[i] = subarr[k - i - 1];
            subarr[k - i - 1] = tmp;
            i++;
        }
    }
    
    int find(vector<int>& arr, int target) {
        for(int i = 0; i < (int)arr.size(); i++) {
            if(arr[i] == target) return i;
        }
        return -1;
    }

public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> rtn;
        
        for(int valueToSort = (int)arr.size(); valueToSort > 0; valueToSort--) {
            int idx = find(arr, valueToSort);
            
            if(idx == valueToSort - 1) continue;
            
            if(idx != 0) {
                rtn.push_back(idx + 1);
                flip(arr, idx + 1);
            }
            
            rtn.push_back(valueToSort);
            flip(arr, valueToSort);
        }
        
        return rtn;
    }
};
```

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** 1. **Greedy Strategy**: Place largest elements first, working from right to left

**How the code works:**
1. **Greedy Strategy**: Place largest elements first, working from right to left
- First flip: Bring target element to front (if not already there)
- Second flip: Move target element to its correct position
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `arr = [3,2,4,1]`, expected output `[4,2,4,3]`:

We perform 4 pancake flips, with k values [4,2,4,3]:
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k=4): arr = [1, 4, 2, 3]
After 2nd flip (k=2): arr = [4, 1, 2, 3]
After 3rd flip (k=4): arr = [3, 2, 1, 4]
After 4th flip (k=3): arr = [1, 2, 3, 4]

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Greedy with Linear Search** | O(n²) | O(1) | Simple, clear | O(n) find per element |
| **STL max_element** | O(n²) | O(1) | Cleaner code | Iterator complexity |
| **Position Map** | O(n²) | O(n) | O(1) find | More complex |
## Algorithm Breakdown

```cpp
vector<int> pancakeSort(vector<int>& arr) {
    vector<int> rtn;
    
    // Process from largest to smallest value
    for(int valueToSort = arr.size(); valueToSort > 0; valueToSort--) {
        // Find current position of valueToSort
        int idx = find(arr, valueToSort);
        
        // If already in correct position, skip
        if(idx == valueToSort - 1) continue;
        
        // Step 1: Bring to front (if not already there)
        if(idx != 0) {
            rtn.push_back(idx + 1);  // k is 1-indexed
            flip(arr, idx + 1);      // Reverse first (idx+1) elements
        }
        
        // Step 2: Move to correct position
        rtn.push_back(valueToSort);  // k = valueToSort
        flip(arr, valueToSort);      // Reverse first valueToSort elements
    }
    
    return rtn;
}
```

### Helper Functions

**Flip Function:**
```cpp
void flip(vector<int>& subarr, int k) {
    int i = 0;
    while(i < k / 2) {
        swap(subarr[i], subarr[k - i - 1]);
        i++;
    }
}
```

Reverses the first `k` elements by swapping elements from both ends.

**Find Function:**
```cpp
int find(vector<int>& arr, int target) {
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] == target) return i;
    }
    return -1;  // Should never happen given constraints
}
```

Linear search to find the index of target value.

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Greedy with Linear Search** | O(n²) | O(1) | Simple, clear | O(n) find per element |
| **STL max_element** | O(n²) | O(1) | Cleaner code | Iterator complexity |
| **Position Map** | O(n²) | O(n) | O(1) find | More complex |

## Implementation Details

### Flip Operation

```cpp
void flip(vector<int>& subarr, int k) {
    int i = 0;
    while(i < k / 2) {
        swap(subarr[i], subarr[k - i - 1]);
        i++;
    }
}
```

**Why `k / 2`?**
- We only need to swap up to the middle
- Swapping `i` with `k-i-1` handles both ends
- When `i >= k/2`, all pairs are swapped

### Index Conversion

```cpp
rtn.push_back(idx + 1);  // Convert 0-indexed to 1-indexed
```

The problem uses 1-indexed `k` (flip first k elements), but arrays are 0-indexed.

### Early Termination

```cpp
if(idx == valueToSort - 1) continue;
```

If element is already in correct position, skip both flips to optimize.

## Common Mistakes

1. **Already sorted**: `[1,2,3]` → return `[]`
2. **Reverse sorted**: `[3,2,1]` → requires flips
3. **Single element**: `[1]` → return `[]`
4. **Element at front**: `[4,1,2,3]` → skip first flip
5. **Element in place**: Skip both flips

1. **Off-by-one errors**: Using `idx` instead of `idx + 1` for k
2. **Wrong flip condition**: Not checking if `idx != 0` before first flip
3. **Incorrect position check**: Using `idx == valueToSort` instead of `idx == valueToSort - 1`
4. **Missing continue**: Not skipping when element is already in place
5. **Wrong loop direction**: Processing smallest to largest instead of largest to smallest

## Optimization Tips

1. **Skip Already Sorted**: Check if element is in place before flipping
2. **Position Map**: Use hash map for O(1) find instead of O(n) linear search
3. **Early Exit**: If array becomes sorted, stop early
4. **STL Functions**: Use `reverse()` and `max_element()` for cleaner code

## Related Problems

- [324. Wiggle Sort II](https://www.leetcode.com/problems/wiggle-sort-ii/) - Different sorting constraint
- [912. Sort an Array](https://www.leetcode.com/problems/sort-an-array/) - General sorting
- [75. Sort Colors](https://www.leetcode.com/problems/sort-colors/) - Three-way partition
- [969. Pancake Sorting](https://www.leetcode.com/problems/pancake-sorting/) - This problem

## Real-World Applications

1. **Network Routing**: Reordering packets with limited operations
2. **Database Operations**: Optimizing query execution order
3. **Game Theory**: Puzzles and optimization problems
4. **Algorithm Design**: Understanding constraint-based sorting

## Pattern Recognition

This problem demonstrates the **"Greedy Sorting with Constraints"** pattern:

```
1. Identify target element (largest unsorted)
2. Bring to front (if needed)
3. Move to correct position
4. Repeat for next target
```

Similar problems:
- Sorting with limited operations
- Constraint-based optimization
- Greedy algorithms

## Why Greedy Works

1. **Optimal Substructure**: Placing largest element correctly doesn't affect smaller elements
2. **Greedy Choice**: Always placing largest unsorted element is optimal
3. **No Future Dependencies**: Decisions don't depend on future placements
4. **Constraint Satisfaction**: Each flip brings us closer to sorted state

## Pancake Sorting Theory

- **Minimum Flips**: Finding minimum flips is NP-hard
- **Upper Bound**: At most `2n - 3` flips needed (proven)
- **Greedy Bound**: This algorithm uses at most `2n` flips
- **Optimal**: For small arrays, can find optimal solution

---

*This problem is a fun introduction to constraint-based sorting, demonstrating how greedy algorithms can solve seemingly complex problems with simple strategies.*

## Key Takeaways

1. **Greedy Strategy**: Place largest elements first, working from right to left
2. **Two-Step Process**: 
   - First flip: Bring target element to front (if not already there)
   - Second flip: Move target element to its correct position
3. **Skip Optimization**: If element is already in correct position, skip it
4. **Index Conversion**: k is 1-indexed (flip first k elements), but arrays are 0-indexed
5. **Unique Values**: Since all values are unique, `find` always returns a valid index

## References

- [LC 969: Pancake Sorting on LeetCode](https://www.leetcode.com/problems/pancake-sorting/)
- [LeetCode Discuss — LC 969: Pancake Sorting](https://www.leetcode.com/problems/pancake-sorting/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/pancake-sorting/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
