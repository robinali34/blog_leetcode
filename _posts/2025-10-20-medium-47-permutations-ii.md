---
layout: post
title: "47. Permutations II"
date: 2025-10-20 14:05:00 -0700
categories: leetcode algorithm medium backtracking recursion duplicates
permalink: /2025/10/20/medium-47-permutations-ii/
---

# 47. Permutations II

**Difficulty:** Medium  
**Category:** Backtracking, Recursion, Duplicates

## Problem Statement

Given a collection of numbers, `nums`, that might contain **duplicates**, return all the possible **unique permutations** in any order.

## Examples

### Example 1:
```
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]
```

### Example 2:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

## Constraints

- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Permutation definition**: What is a permutation? (Assumption: All possible arrangements of array elements - order matters)

2. **Duplicate handling**: How should we handle duplicate elements? (Assumption: Avoid duplicate permutations - if [1,1,2], don't generate [1,1,2] twice)

3. **Output format**: Should we return all permutations or just count? (Assumption: Return all distinct permutations - list of lists)

4. **Array modification**: Can we modify the input array? (Assumption: Typically yes for backtracking, but should clarify)

5. **Empty array**: What if array is empty? (Assumption: Return [[]] - one permutation with no elements)

## Approach

This is an extension of **LC 46 Permutations** that handles **duplicate elements**. The key challenge is avoiding duplicate permutations when the input contains repeated numbers.

### Key Insight:
When we have duplicates, we need to ensure that identical elements don't create duplicate permutations. The solution is to **skip duplicate elements** at the same level of recursion.

### Algorithm 1: Backtracking with Duplicate Handling
1. **Sort the array** to group identical elements together
2. **Use swapping** like in LC 46, but skip duplicates
3. **Skip condition:** If `nums[i] == nums[i-1]` and `i > start`, skip
4. **Recursively generate** permutations for remaining positions
5. **Backtrack** by swapping back to original positions

### Algorithm 2: STL next_permutation (Unchanged)
The STL approach works the same as LC 46 because `next_permutation()` automatically handles duplicates correctly.

## Solution

### Solution 1: Backtracking with Duplicate Handling

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> rtn;
        sort(nums.begin(), nums.end());  // Sort to group duplicates
        vector<bool> used(nums.size(), false);
        vector<int> current;
        permuteUnique(nums, used, current, rtn);
        return rtn;
    }
private:
    void permuteUnique(vector<int>& nums, vector<bool>& used, 
                       vector<int>& current, vector<vector<int>>& rtn) {
        if(current.size() == nums.size()) {
            rtn.push_back(current);
            return;
        }
        
        for(int i = 0; i < (int)nums.size(); i++) {
            if(used[i]) continue;
            // Skip duplicates: if current element equals previous element
            // and previous element is not used, skip current element
            if(i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue;
            
            used[i] = true;
            current.push_back(nums[i]);
            permuteUnique(nums, used, current, rtn);
            current.pop_back();
            used[i] = false;
        }
    }
};
```

### Solution 2: STL next_permutation (Same as LC 46)

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> rtn;
        sort(nums.begin(), nums.end());
        do{
            rtn.push_back(nums);
        } while(next_permutation(nums.begin(), nums.end()));
        return rtn;
    }
};
```

## Why `current` Array is Essential

### **Problem with In-Place Swapping Approach**

The swapping approach from LC 46 doesn't work well for duplicates because:

```cpp
// PROBLEMATIC: Swapping approach for duplicates
void permuteUnique(vector<int>& nums, int idx, vector<vector<int>>& rtn) {
    if(idx == nums.size()) {
        rtn.push_back(nums);
        return;
    }
    for(int i = idx; i < nums.size(); i++) {
        if(i > idx && nums[i] == nums[idx]) continue;  // Still problematic
        swap(nums[idx], nums[i]);
        permuteUnique(nums, idx + 1, rtn);
        swap(nums[idx], nums[i]);
    }
}
```

**Issues:**
1. **Modifies original array** during recursion
2. **Duplicate detection logic** becomes complex and error-prone
3. **Generates duplicate permutations** even with skip logic

### **Why `current` Array Solves the Problem**

```cpp
// CORRECT: Using current array
vector<int> current;  // Build permutation incrementally
vector<bool> used(nums.size(), false);  // Track used elements
```

**Advantages:**
1. **Preserves original array** - never modify `nums`
2. **Incremental building** - add one element at a time
3. **Clean backtracking** - simple `push_back()` and `pop_back()`
4. **Reliable duplicate detection** - compare with previous unused element

### **Example Comparison**

**Input:** `nums = [1,1,2]`

**Swapping Approach (WRONG):**
```
idx=0: Try nums[0]=1, nums[1]=1, nums[2]=2
├─ Swap(0,0): [1,1,2] → Recurse
│  ├─ Swap(1,1): [1,1,2] → Add [1,1,2]
│  └─ Swap(1,2): [1,2,1] → Add [1,2,1]
├─ Skip nums[1] (duplicate of nums[0]) ❌ WRONG!
└─ Swap(0,2): [2,1,1] → Recurse
   ├─ Swap(1,1): [2,1,1] → Add [2,1,1]
   └─ Swap(1,2): [2,1,1] → Add [2,1,1] ❌ DUPLICATE!
```
**Result:** `[[1,1,2], [1,2,1], [2,1,1], [2,1,1]]` - 4 permutations (WRONG!)

**Current Array Approach (CORRECT):**
```
used=[F,F,F], current=[]
├─ i=0: nums[0]=1, used[0]=T, current=[1]
│  ├─ i=0: Skip (used)
│  ├─ i=1: nums[1]=1, Skip (nums[1]==nums[0] && !used[0]) ❌
│  └─ i=2: nums[2]=2, used[2]=T, current=[1,2]
│     ├─ i=0: Skip (used)
│     ├─ i=1: nums[1]=1, used[1]=T, current=[1,2,1] → Add [1,2,1]
│     └─ i=2: Skip (used)
├─ i=1: nums[1]=1, Skip (nums[1]==nums[0] && !used[0]) ❌
└─ i=2: nums[2]=2, used[2]=T, current=[2]
   ├─ i=0: nums[0]=1, used[0]=T, current=[2,1]
   │  ├─ i=1: nums[1]=1, Skip (nums[1]==nums[0] && !used[0]) ❌
   │  └─ i=2: Skip (used)
   └─ i=1: nums[1]=1, Skip (nums[1]==nums[0] && !used[0]) ❌
```
**Result:** `[[1,1,2], [1,2,1], [2,1,1]]` - 3 unique permutations (CORRECT!)

### **Key Benefits of `current` Array**

1. **Clean State Management:**
   ```cpp
   used[i] = true;           // Mark as used
   current.push_back(nums[i]); // Add to permutation
   // ... recurse ...
   current.pop_back();       // Remove from permutation
   used[i] = false;          // Mark as unused
   ```

2. **Reliable Duplicate Detection:**
   ```cpp
   if(i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue;
   ```
   - **`nums[i] == nums[i-1]`** - Current equals previous
   - **`!used[i-1]`** - Previous is not used
   - **Skip current** - Only use first occurrence of each duplicate group

3. **No Array Modification:**
   - Original `nums` array remains unchanged
   - No complex swap/restore logic
   - Easier to debug and understand

### **When You Can Skip `current`**

**STL Approach (No `current` needed):**
```cpp
vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> rtn;
    sort(nums.begin(), nums.end());
    do{
        rtn.push_back(nums);  // Directly use nums
    } while(next_permutation(nums.begin(), nums.end()));
    return rtn;
}
```

**Why STL works without `current`:**
- **`next_permutation()`** handles duplicates automatically
- **Lexicographic generation** - no duplicate permutations
- **Iterative approach** - no recursion state to manage

### **Hash Set Approach (Alternative)**

**Yes, you can use a hash set to remove duplicates:**

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        permute(nums, 0, result);
        
        // Remove duplicates using set
        set<vector<int>> unique_perms(result.begin(), result.end());
        return vector<vector<int>>(unique_perms.begin(), unique_perms.end());
    }
    
private:
    void permute(vector<int>& nums, int idx, vector<vector<int>>& result) {
        if(idx == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for(int i = idx; i < nums.size(); i++) {
            swap(nums[idx], nums[i]);
            permute(nums, idx + 1, result);
            swap(nums[idx], nums[i]);
        }
    }
};
```

**How it works:**
1. **Generate all permutations** using LC 46 approach (including duplicates)
2. **Store in vector** - may contain duplicates
3. **Convert to set** - automatically removes duplicates
4. **Convert back to vector** - return unique permutations

**Example:**
```cpp
// Input: nums = [1,1,2]
// Step 1: Generate all permutations
result = [[1,1,2], [1,2,1], [1,1,2], [1,2,1], [2,1,1], [2,1,1]]

// Step 2: Remove duplicates with set
set<vector<int>> unique_perms(result.begin(), result.end());
// unique_perms = {[1,1,2], [1,2,1], [2,1,1]}

// Step 3: Convert back to vector
return [[1,1,2], [1,2,1], [2,1,1]]
```

### **Hash Set vs Current Array Comparison**

| Aspect | Hash Set Approach | Current Array Approach |
|--------|------------------|----------------------|
| **Time Complexity** | O(n! × n × log(n!)) | O(unique_perms × n) |
| **Space Complexity** | O(n! × n) | O(n) |
| **Code Simplicity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Efficiency** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Memory Usage** | High | Low |
| **Educational Value** | Low | High |

**Time Complexity Breakdown:**
- **Hash Set:** O(n! × n) to generate + O(n! × log(n!)) to sort + O(n!) to convert
- **Current Array:** O(unique_perms × n) where unique_perms < n!

**Space Complexity Breakdown:**
- **Hash Set:** O(n! × n) to store all permutations + O(n! × n) for set
- **Current Array:** O(n) for recursion stack + O(n) for used array

### **When to Use Each Approach**

**Use Hash Set when:**
- **Quick solution** is needed
- **Memory is abundant**
- **Don't mind** generating all permutations first
- **Code simplicity** is priority

**Use Current Array when:**
- **Memory is limited**
- **Performance** is critical
- **Need to understand** the algorithm deeply
- **Educational purposes**

**Use STL when:**
- **Code conciseness** is priority
- **Performance** is critical
- **Lexicographic order** is desired

### **Hash Set Implementation Details**

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        permute(nums, 0, result);
        
        // Method 1: Using set (automatic sorting)
        set<vector<int>> unique_perms(result.begin(), result.end());
        return vector<vector<int>>(unique_perms.begin(), unique_perms.end());
        
        // Method 2: Using unordered_set (faster insertion)
        // unordered_set<vector<int>> unique_perms(result.begin(), result.end());
        // return vector<vector<int>>(unique_perms.begin(), unique_perms.end());
        
        // Method 3: Manual deduplication
        // sort(result.begin(), result.end());
        // result.erase(unique(result.begin(), result.end()), result.end());
        // return result;
    }
    
private:
    void permute(vector<int>& nums, int idx, vector<vector<int>>& result) {
        if(idx == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for(int i = idx; i < nums.size(); i++) {
            swap(nums[idx], nums[i]);
            permute(nums, idx + 1, result);
            swap(nums[idx], nums[i]);
        }
    }
};
```

**Note:** `unordered_set<vector<int>>` requires a custom hash function for `vector<int>`, so `set<vector<int>>` is simpler to use.

### **Solution 3: Hash Set Deduplication**

#### **Option 3a: Using `set<vector<int>>` (Simpler)**

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        permute(nums, 0, result);
        
        // Remove duplicates using set
        set<vector<int>> unique_perms(result.begin(), result.end());
        return vector<vector<int>>(unique_perms.begin(), unique_perms.end());
    }
    
private:
    void permute(vector<int>& nums, int idx, vector<vector<int>>& result) {
        if(idx == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for(int i = idx; i < nums.size(); i++) {
            swap(nums[idx], nums[i]);
            permute(nums, idx + 1, result);
            swap(nums[idx], nums[i]);
        }
    }
};
```

#### **Option 3b: Using `unordered_set<vector<int>>` (Better Performance)**

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        permute(nums, 0, result);
        
        // Remove duplicates using unordered_set with custom hash
        unordered_set<vector<int>, VectorHash> unique_perms(result.begin(), result.end());
        return vector<vector<int>>(unique_perms.begin(), unique_perms.end());
    }
    
private:
    // Custom hash function for vector<int>
    struct VectorHash {
        size_t operator()(const vector<int>& v) const {
            size_t hash = 0;
            for(int x : v) {
                hash ^= hash << 13;
                hash ^= hash >> 17;
                hash ^= hash << 5;
                hash ^= x;
            }
            return hash;
        }
    };
    
    void permute(vector<int>& nums, int idx, vector<vector<int>>& result) {
        if(idx == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for(int i = idx; i < nums.size(); i++) {
            swap(nums[idx], nums[i]);
            permute(nums, idx + 1, result);
            swap(nums[idx], nums[i]);
        }
    }
};
```

### **Solution 4: Alternative Hash Set Implementations**

```cpp
// Method 1: Using unordered_set (requires custom hash)
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        permute(nums, 0, result);
        
        unordered_set<vector<int>, VectorHash> unique_perms(result.begin(), result.end());
        return vector<vector<int>>(unique_perms.begin(), unique_perms.end());
    }
    
private:
    struct VectorHash {
        size_t operator()(const vector<int>& v) const {
            size_t hash = 0;
            for(int x : v) {
                hash ^= hash << 13;
                hash ^= hash >> 17;
                hash ^= hash << 5;
                hash ^= x;
            }
            return hash;
        }
    };
    
    void permute(vector<int>& nums, int idx, vector<vector<int>>& result) {
        if(idx == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for(int i = idx; i < nums.size(); i++) {
            swap(nums[idx], nums[i]);
            permute(nums, idx + 1, result);
            swap(nums[idx], nums[i]);
        }
    }
};

// Method 2: Manual deduplication
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        permute(nums, 0, result);
        
        // Sort and remove consecutive duplicates
        sort(result.begin(), result.end());
        result.erase(unique(result.begin(), result.end()), result.end());
        return result;
    }
    
private:
    void permute(vector<int>& nums, int idx, vector<vector<int>>& result) {
        if(idx == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for(int i = idx; i < nums.size(); i++) {
            swap(nums[idx], nums[i]);
            permute(nums, idx + 1, result);
            swap(nums[idx], nums[i]);
        }
    }
};
```

## Complete Solution Comparison & Trade-offs

### **Comprehensive Comparison Table**

| Solution | Time Complexity | Space Complexity | Code Simplicity | Memory Usage | Educational Value | Best For |
|----------|----------------|------------------|-----------------|--------------|-------------------|----------|
| **Solution 1: Current Array** | O(unique_perms × n) | O(n) | ⭐⭐⭐⭐ | Low | High | Learning, Memory-constrained |
| **Solution 2: STL** | O(unique_perms × n) | O(1) | ⭐⭐⭐⭐⭐ | Low | Medium | Production, Performance |
| **Solution 3a: Hash Set (set)** | O(n! × n) + O(log(n!)) | O(n! × n) | ⭐⭐⭐⭐⭐ | High | Low | Quick solution, Abundant memory |
| **Solution 3b: Hash Set (unordered_set)** | O(n! × n) | O(n! × n) | ⭐⭐⭐ | High | Low | Better performance, Custom hash |
| **Solution 4a: Unordered Set** | O(n! × n) | O(n! × n) | ⭐⭐⭐ | High | Low | Performance with custom hash |
| **Solution 4b: Manual Dedup** | O(n! × n × log(n!)) | O(n! × n) | ⭐⭐⭐⭐ | High | Medium | Control over deduplication |

### **Detailed Trade-offs Analysis**

#### **Solution 1: Current Array Backtracking**
**Pros:**
- **Optimal space complexity** - O(n) only
- **Educational value** - Shows proper backtracking with duplicates
- **Memory efficient** - No extra storage for all permutations
- **Prevents duplicates** during generation

**Cons:**
- **More complex code** - requires used array and current array
- **Slower than STL** - recursive overhead
- **Harder to debug** - more state to track

**When to use:** Learning purposes, memory-constrained environments, interviews

#### **Solution 2: STL next_permutation**
**Pros:**
- **Simplest code** - just 6 lines
- **Highly optimized** - STL is performance-tuned
- **Lexicographic order** - generates permutations in sorted order
- **No recursion** - iterative approach

**Cons:**
- **Less educational** - doesn't show backtracking concepts
- **Requires sorting** - must sort input first
- **Less control** - can't customize generation process

**When to use:** Production code, performance-critical applications, quick implementation

#### **Solution 3a: Hash Set with `set<vector<int>>`**
**Pros:**
- **Simplest logic** - generate all, then deduplicate
- **Easy to understand** - straightforward approach
- **No complex state management** - just generate and filter
- **No custom hash required** - `set` works out of the box

**Cons:**
- **High space complexity** - O(n! × n)
- **High time complexity** - O(n! × n) + O(log(n!))
- **Generates duplicates** - inefficient
- **High memory usage** - stores all permutations

**When to use:** Quick prototyping, abundant memory, simple requirements

**Time Complexity Breakdown:**
- **Generate all permutations:** O(n! × n) - n! permutations, each takes O(n) to copy
- **Insert into set:** O(log(n!)) - n! insertions, each is O(log(n!)) for set
- **Total:** O(n! × n) + O(log(n!)) = O(n! × n) + O(log(n!))

#### **Solution 3b: Hash Set with `unordered_set<vector<int>>`**
**Pros:**
- **Better time complexity** - O(n! × n) vs O(n! × n) + O(log(n!))
- **Faster insertion** - O(1) average vs O(log(n!))
- **Same logic** - generate all, then deduplicate
- **Better performance** - unordered_set is faster

**Cons:**
- **Custom hash function** - more complex implementation
- **Still high space complexity** - O(n! × n)
- **Hash collisions** - potential performance degradation
- **More code** - requires hash function definition

**When to use:** Performance-critical applications, large datasets

**Time Complexity Breakdown:**
- **Generate all permutations:** O(n! × n) - n! permutations, each takes O(n) to copy
- **Insert into unordered_set:** O(n!) - n! insertions, each is O(1) average
- **Total:** O(n! × n) + O(n!) = O(n! × n)

#### **Solution 4a: Unordered Set with Custom Hash**
**Pros:**
- **Better time complexity** - O(n! × n) vs O(n! × n) + O(log(n!))
- **Faster insertion** - O(1) average vs O(log(n!))
- **No sorting required** - unordered storage

**Cons:**
- **Custom hash function** - more complex implementation
- **Still high space complexity** - O(n! × n)
- **Hash collisions** - potential performance degradation

**When to use:** Performance-critical with custom hash, large datasets

**Time Complexity Breakdown:**
- **Generate all permutations:** O(n! × n) - n! permutations, each takes O(n) to copy
- **Insert into unordered_set:** O(n! × 1) - each insertion is O(1) average
- **Total:** O(n! × n) + O(n!) = O(n! × n)

#### **Solution 4b: Manual Deduplication**
**Pros:**
- **Full control** - customize deduplication logic
- **No external dependencies** - uses only STL algorithms
- **Predictable behavior** - deterministic sorting

**Cons:**
- **Sorting overhead** - O(n! × log(n!))
- **High space complexity** - O(n! × n)
- **More code** - additional sorting step

**When to use:** Custom deduplication needs, controlled sorting requirements

### **Performance Analysis**

**For `nums = [1,1,2,2]` (4 elements, 2 duplicates):**
- **Total permutations:** 4! = 24
- **Unique permutations:** 4! / (2! × 2!) = 6

**Solution 1 (Current Array):**
- **Generates:** 6 unique permutations
- **Time:** O(6 × 4) = O(24)
- **Space:** O(4)

**Solution 2 (STL):**
- **Generates:** 6 unique permutations
- **Time:** O(6 × 4) = O(24)
- **Space:** O(1)

**Solution 3a (Hash Set with set):**
- **Generates:** 24 total permutations
- **Time:** O(24 × 4) + O(log(24)) = O(96 + 4.58) = O(100.58)
- **Space:** O(24 × 4) = O(96)

**Solution 3b (Hash Set with unordered_set):**
- **Generates:** 24 total permutations
- **Time:** O(24 × 4) + O(24 × 1) = O(96 + 24) = O(120)
- **Space:** O(24 × 4) = O(96)

**Solution 4a (Unordered Set):**
- **Generates:** 24 total permutations
- **Time:** O(24 × 4) + O(24 × 1) = O(96 + 24) = O(120)
- **Space:** O(24 × 4) = O(96)

### **Memory Usage Comparison**

| Input Size | Solution 1 | Solution 2 | Solution 3 | Solution 4a | Solution 4b |
|------------|------------|-------------|------------|-------------|-------------|
| n=3 | O(3) | O(1) | O(6) | O(6) | O(6) |
| n=4 | O(4) | O(1) | O(24) | O(24) | O(24) |
| n=5 | O(5) | O(1) | O(120) | O(120) | O(120) |
| n=6 | O(6) | O(1) | O(720) | O(720) | O(720) |

### **Recommendation Summary**

**For Interviews:** Use Solution 1 (Current Array) - shows understanding of backtracking and duplicate handling

**For Production:** Use Solution 2 (STL) - optimal performance and simplicity

**For Learning:** Use Solution 1 (Current Array) - best educational value

**For Quick Implementation:** Use Solution 3 (Hash Set) - simplest to code

**For Custom Requirements:** Use Solution 4b (Manual Dedup) - most control

## Explanation

**Key Changes from LC 46:**
1. **Sort the array** before processing to group identical elements
2. **Use visited array** to track which elements are used
3. **Skip duplicates** at the same recursion level
4. **Duplicate detection:** `if(i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue;`

**Step-by-Step Process:**

1. **Sort:** `[1,1,2]` → `[1,1,2]` (already sorted)
2. **Base Case:** When `current.size() == nums.size()`, add current permutation
3. **Recursive Case:** For each position, try every unused element
4. **Skip Logic:** If current element equals previous element and previous is not used, skip
5. **Mark Used:** Mark element as used and add to current permutation
6. **Recurse:** Generate remaining permutations
7. **Backtrack:** Remove from current and mark as unused

**Example Walkthrough for `nums = [1,1,2]`:**

```
Sorted: [1,1,2], used=[F,F,F], current=[]
├─ i=0: nums[0]=1, used[0]=T, current=[1]
│  ├─ i=0: Skip (used)
│  ├─ i=1: nums[1]=1, Skip (nums[1]==nums[0] && !used[0]) ❌
│  └─ i=2: nums[2]=2, used[2]=T, current=[1,2]
│     ├─ i=0: Skip (used)
│     ├─ i=1: nums[1]=1, used[1]=T, current=[1,2,1] → Add [1,2,1]
│     └─ i=2: Skip (used)
├─ i=1: nums[1]=1, Skip (nums[1]==nums[0] && !used[0]) ❌
└─ i=2: nums[2]=2, used[2]=T, current=[2]
   ├─ i=0: nums[0]=1, used[0]=T, current=[2,1]
   │  ├─ i=1: nums[1]=1, Skip (nums[1]==nums[0] && !used[0]) ❌
   │  └─ i=2: Skip (used)
   └─ i=1: nums[1]=1, Skip (nums[1]==nums[0] && !used[0]) ❌
```

**Correct Logic Explanation:**
The skip condition `if(i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue;` ensures that:
- We only use the **first occurrence** of each duplicate group at each recursion level
- If `nums[i] == nums[i-1]` and `nums[i-1]` is not used, we skip `nums[i]`
- This prevents generating duplicate permutations like `[1,1,2]` and `[1,1,2]` (from different 1's)

### Solution 2: STL next_permutation

**Unchanged from LC 46:**
- **Sort array** to get lexicographically smallest permutation
- **Generate permutations** using `next_permutation()` in do-while loop
- **Add each permutation** to result vector
- **`next_permutation()` automatically handles duplicates** correctly

## Complexity Analysis

### Solution 1: Backtracking with Duplicate Handling
**Time Complexity:** O(n! × n)
- **Unique permutations:** Less than n! due to duplicates
- **Each permutation:** O(n) time to copy array
- **Skip duplicates:** Reduces total permutations generated

**Space Complexity:** O(n)
- **Recursion depth:** O(n) for the call stack
- **Used array:** O(n) to track used elements
- **Current array:** O(n) to build current permutation

### Solution 2: STL next_permutation
**Time Complexity:** O(n! × n)
- **Unique permutations:** Less than n! due to duplicates
- **Each permutation:** O(n) time for `next_permutation()` and copying
- **Automatic duplicate handling:** Built into STL function

**Space Complexity:** O(1)
- **No recursion:** Iterative approach
- **No additional space** beyond input and output

## Key Insights

1. **Duplicate Handling:** Skip identical elements at the same recursion level
2. **Sorting Required:** Must sort array to group duplicates together
3. **Skip Condition:** `nums[i] == nums[i-1] && !used[i-1]`
4. **STL Advantage:** `next_permutation()` handles duplicates automatically
5. **State Tracking:** Need to track which elements are used

## Comparison with LC 46

| Aspect | LC 46 (No Duplicates) | LC 47 (With Duplicates) |
|--------|----------------------|-------------------------|
| **Sorting** | Not required | Required |
| **Skip Logic** | Not needed | Skip duplicates |
| **Space** | O(n) recursion | O(n) recursion + O(n) used array |
| **STL** | Works perfectly | Works perfectly |
| **Complexity** | O(n! × n) | O(unique_perms × n) |

## Alternative Approaches

### Approach 3: Set-based Deduplication
```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        permute(nums, 0, result);
        
        // Remove duplicates using set
        set<vector<int>> unique_perms(result.begin(), result.end());
        return vector<vector<int>>(unique_perms.begin(), unique_perms.end());
    }
    
private:
    void permute(vector<int>& nums, int idx, vector<vector<int>>& result) {
        if(idx == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for(int i = idx; i < nums.size(); i++) {
            swap(nums[idx], nums[i]);
            permute(nums, idx + 1, result);
            swap(nums[idx], nums[i]);
        }
    }
};
```

### Approach 4: Frequency-based Backtracking
```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        unordered_map<int, int> freq;
        
        // Count frequency of each number
        for(int num : nums) {
            freq[num]++;
        }
        
        vector<int> current;
        backtrack(freq, current, result, nums.size());
        return result;
    }
    
private:
    void backtrack(unordered_map<int, int>& freq, vector<int>& current,
                   vector<vector<int>>& result, int target_size) {
        if(current.size() == target_size) {
            result.push_back(current);
            return;
        }
        
        for(auto& pair : freq) {
            if(pair.second > 0) {
                pair.second--;
                current.push_back(pair.first);
                backtrack(freq, current, result, target_size);
                current.pop_back();
                pair.second++;
            }
        }
    }
};
```

## When to Use Each Approach

### Use Backtracking with Used Array when:
- **Need to understand** the algorithm deeply
- **Custom modifications** are required
- **Memory is not a constraint**

### Use STL next_permutation when:
- **Code simplicity** is priority
- **Performance** is critical
- **Lexicographic order** is desired

### Use Set-based Deduplication when:
- **Quick solution** is needed
- **Memory is abundant**
- **Don't mind** generating all permutations first

## Key Concepts

1. **Duplicate Handling:** Preventing duplicate permutations in output
2. **Skip Logic:** Avoiding identical elements at same recursion level
3. **State Tracking:** Keeping track of used elements
4. **Lexicographic Order:** STL generates permutations in sorted order
5. **Frequency Counting:** Alternative approach using element counts

This problem extends the classic permutation generation to handle duplicates, requiring careful state management to avoid duplicate outputs while maintaining efficiency.
