---
layout: post
title: "46. Permutations"
date: 2025-10-20 14:00:00 -0700
categories: leetcode algorithm medium backtracking recursion
permalink: /2025/10/20/medium-46-permutations/
---

# 46. Permutations

**Difficulty:** Medium  
**Category:** Backtracking, Recursion

## Problem Statement

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Permutation definition**: What is a permutation? (Assumption: All possible arrangements of array elements - order matters)

2. **Element uniqueness**: Are all elements unique? (Assumption: Yes - per constraints, all integers are unique)

3. **Output format**: Should we return all permutations or just count? (Assumption: Return all distinct permutations - list of lists)

4. **Array modification**: Can we modify the input array? (Assumption: Typically yes for backtracking, but should clarify)

5. **Empty array**: What if array is empty? (Assumption: Return [[]] - one permutation with no elements)

## Approach

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

## Complexity Analysis

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

## Key Insights

1. **Backtracking Pattern:** Classic recursive approach with state restoration
2. **In-place Generation:** Swapping allows generating permutations without extra space
3. **STL Efficiency:** `next_permutation()` is highly optimized
4. **Lexicographic Order:** STL approach generates permutations in sorted order
5. **State Management:** Proper backtracking ensures all possibilities are explored

## Comparison of Approaches

| Approach | Time | Space | Advantages | Disadvantages |
|----------|------|-------|------------|---------------|
| **Backtracking** | O(n! × n) | O(n) | Educational, flexible | Recursive overhead |
| **STL** | O(n! × n) | O(1) | Concise, optimized | Less control over order |

## Alternative Approaches

### Approach 3: Backtracking with Visited Array
```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        vector<bool> used(nums.size(), false);
        backtrack(nums, current, used, result);
        return result;
    }
    
private:
    void backtrack(vector<int>& nums, vector<int>& current, 
                   vector<bool>& used, vector<vector<int>>& result) {
        if(current.size() == nums.size()) {
            result.push_back(current);
            return;
        }
        
        for(int i = 0; i < nums.size(); i++) {
            if(used[i]) continue;
            
            used[i] = true;
            current.push_back(nums[i]);
            backtrack(nums, current, used, result);
            current.pop_back();
            used[i] = false;
        }
    }
};
```

### Approach 4: Iterative with Stack
```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        stack<vector<int>> stk;
        stk.push({});
        
        while(!stk.empty()) {
            vector<int> current = stk.top();
            stk.pop();
            
            if(current.size() == nums.size()) {
                result.push_back(current);
                continue;
            }
            
            for(int num : nums) {
                if(find(current.begin(), current.end(), num) == current.end()) {
                    vector<int> next = current;
                    next.push_back(num);
                    stk.push(next);
                }
            }
        }
        
        return result;
    }
};
```

## When to Use Each Approach

### Use Backtracking with Swapping when:
- **Memory is limited** (O(n) space vs O(n!) for visited approach)
- **Need to understand** the algorithm deeply
- **Custom modifications** are required

### Use STL next_permutation when:
- **Code simplicity** is priority
- **Lexicographic order** is desired
- **Performance** is critical (highly optimized)

### Use Visited Array when:
- **Clarity** is more important than space
- **Need to track** which elements are used
- **Modifying** the original array is not allowed

## Key Concepts

1. **Permutations:** All possible arrangements of elements
2. **Backtracking:** Systematic exploration with state restoration
3. **Recursion:** Divide problem into smaller subproblems
4. **State Space:** All possible configurations to explore
5. **Pruning:** Avoiding invalid or duplicate states

This problem is fundamental for understanding backtracking algorithms and is commonly used in interviews to test recursive thinking and state management skills.
