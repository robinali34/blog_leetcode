---
layout: post
title: "[Medium] 969. Pancake Sorting"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp array sorting problem-solving
permalink: /posts/2025-11-18-medium-969-pancake-sorting/
tags: [leetcode, medium, array, sorting, greedy, pancake-flip]
---

# [Medium] 969. Pancake Sorting

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Pancake flip**: What is a pancake flip? (Assumption: Reverse first k elements - flip(arr, k) reverses arr[0:k])

2. **Sorting goal**: What are we trying to achieve? (Assumption: Sort array in ascending order using only pancake flips)

3. **Return format**: What should we return? (Assumption: Array of k values - sequence of flips to sort the array)

4. **Array properties**: What are the array properties? (Assumption: Permutation of [1, 2, ..., n] - unique integers from 1 to n)

5. **Multiple solutions**: Are there multiple valid solutions? (Assumption: Yes - can return any valid sequence of flips)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Try all possible sequences of flips: for each position, try flipping at positions 2, 3, ..., n. Use BFS or DFS to explore all possible flip sequences until we find one that sorts the array. This approach has exponential time complexity and is impractical even for small arrays.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a greedy approach: work from the end of the array. For each position from n-1 down to 0, find the largest unsorted element, flip it to the top, then flip it to its correct position. This reduces the problem size by one each iteration. However, we need to track which elements are already in their correct positions to avoid unnecessary flips.

**Step 3: Optimized Solution (8 minutes)**

Use greedy algorithm with position tracking: for each position `i` from n-1 down to 0, if `arr[i] != i+1` (element not in correct position), find where `i+1` is located, flip it to the top (position 0), then flip it to position `i`. This ensures each element is placed correctly in at most 2 flips. The algorithm runs in O(n²) time: O(n) positions, each requiring O(n) to find the element. The key insight is that we can sort the array by placing elements one by one from the end, and pancake flips allow us to move any element to any position efficiently.

## Solution: Greedy Approach

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

## How the Algorithm Works

### Step-by-Step Example: `arr = [3,2,4,1]`

```
Initial: arr = [3, 2, 4, 1]

valueToSort = 4:
  Find index of 4: idx = 2
  idx != 3 (valueToSort - 1), need to move
  idx != 0, flip first 3 elements: [4, 2, 3, 1]
  Flip first 4 elements: [1, 3, 2, 4]
  rtn = [3, 4]

valueToSort = 3:
  Find index of 3: idx = 1
  idx != 2, need to move
  idx != 0, flip first 2 elements: [3, 1, 2, 4]
  Flip first 3 elements: [2, 1, 3, 4]
  rtn = [3, 4, 2, 3]

valueToSort = 2:
  Find index of 2: idx = 0
  idx != 1, need to move
  idx == 0, skip first flip
  Flip first 2 elements: [1, 2, 3, 4]
  rtn = [3, 4, 2, 3, 2]

valueToSort = 1:
  Find index of 1: idx = 0
  idx == 0 (valueToSort - 1), already in place, continue

Result: rtn = [3, 4, 2, 3, 2]
```

### Visual Representation

```
Step 1: Place 4 in position 4
  [3, 2, 4, 1] → Find 4 at index 2
  Flip k=3: [4, 2, 3, 1]  (bring 4 to front)
  Flip k=4: [1, 3, 2, 4]  (move 4 to end)

Step 2: Place 3 in position 3
  [1, 3, 2, 4] → Find 3 at index 1
  Flip k=2: [3, 1, 2, 4]  (bring 3 to front)
  Flip k=3: [2, 1, 3, 4]  (move 3 to position 3)

Step 3: Place 2 in position 2
  [2, 1, 3, 4] → Find 2 at index 0
  Flip k=2: [1, 2, 3, 4]  (move 2 to position 2)

Final: [1, 2, 3, 4] ✓
```

## Key Insights

1. **Greedy Strategy**: Place largest elements first, working from right to left
2. **Two-Step Process**: 
   - First flip: Bring target element to front (if not already there)
   - Second flip: Move target element to its correct position
3. **Skip Optimization**: If element is already in correct position, skip it
4. **Index Conversion**: k is 1-indexed (flip first k elements), but arrays are 0-indexed
5. **Unique Values**: Since all values are unique, `find` always returns a valid index

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

## Edge Cases

1. **Already sorted**: `[1,2,3]` → return `[]`
2. **Reverse sorted**: `[3,2,1]` → requires flips
3. **Single element**: `[1]` → return `[]`
4. **Element at front**: `[4,1,2,3]` → skip first flip
5. **Element in place**: Skip both flips

## Alternative Approaches

### Approach 2: Using STL reverse

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

```cpp
class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> result;
        
        for(int size = arr.size(); size > 1; size--) {
            // Find index of maximum in unsorted portion
            int maxIdx = max_element(arr.begin(), arr.begin() + size) - arr.begin();
            
            if(maxIdx == size - 1) continue;  // Already in place
            
            // Bring max to front
            if(maxIdx > 0) {
                result.push_back(maxIdx + 1);
                reverse(arr.begin(), arr.begin() + maxIdx + 1);
            }
            
            // Move max to correct position
            result.push_back(size);
            reverse(arr.begin(), arr.begin() + size);
        }
        
        return result;
    }
};
```

**Pros:**
- Uses STL functions (cleaner)
- `max_element` is more efficient than linear search

**Cons:**
- Requires understanding of STL iterators

### Approach 3: Optimized Find

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

Instead of linear search, maintain a position map:

```cpp
class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> result;
        int n = arr.size();
        
        // Create position map: value -> index
        vector<int> pos(n + 1);
        for(int i = 0; i < n; i++) {
            pos[arr[i]] = i;
        }
        
        for(int val = n; val >= 1; val--) {
            int idx = pos[val];
            
            if(idx == val - 1) continue;
            
            if(idx != 0) {
                result.push_back(idx + 1);
                flip(arr, idx + 1, pos);
            }
            
            result.push_back(val);
            flip(arr, val, pos);
        }
        
        return result;
    }
    
private:
    void flip(vector<int>& arr, int k, vector<int>& pos) {
        for(int i = 0; i < k / 2; i++) {
            swap(arr[i], arr[k - 1 - i]);
            pos[arr[i]] = i;
            pos[arr[k - 1 - i]] = k - 1 - i;
        }
    }
};
```

**Pros:**
- O(1) find operation
- More efficient for large arrays

**Cons:**
- More complex implementation
- Need to maintain position map

## Complexity Analysis

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

- [324. Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) - Different sorting constraint
- [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) - General sorting
- [75. Sort Colors](https://leetcode.com/problems/sort-colors/) - Three-way partition
- [969. Pancake Sorting](https://leetcode.com/problems/pancake-sorting/) - This problem

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

