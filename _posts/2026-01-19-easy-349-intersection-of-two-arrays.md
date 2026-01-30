---
layout: post
title: "349. Intersection of Two Arrays"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, array, hash-table]
permalink: /2026/01/19/easy-349-intersection-of-two-arrays/
tags: [leetcode, easy, array, hash-table, two-pointers, sorting]
---

# 349. Intersection of Two Arrays

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array of their **intersection**. Each element in the result must be **unique** and you may return the result in **any order**.

## Examples

**Example 1:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Explanation: The intersection contains only the element 2.
```

**Example 2:**
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4] or [4,9]
Explanation: The intersection contains elements 9 and 4. Order does not matter.
```

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Intersection definition**: What exactly is the intersection? (Assumption: Elements that appear in both arrays, each element appears only once in result)

2. **Duplicate handling**: If an element appears multiple times in both arrays, how many times should it appear in result? (Assumption: Only once - intersection contains unique elements)

3. **Order requirement**: Does the order of elements in the result matter? (Assumption: No - order doesn't matter, can return in any order)

4. **Array mutability**: Can we modify the input arrays? (Assumption: No - typically we don't modify input arrays)

5. **Empty arrays**: What if one or both arrays are empty? (Assumption: Return empty array - no intersection)

## Solution Approach

This problem requires finding common elements between two arrays, with each element appearing only once in the result. There are several approaches:

1. **Hash Set**: Use set to track elements from first array, then check second array
2. **Sorting + Two Pointers**: Sort both arrays and use two pointers
3. **Boolean Array**: Use fixed-size array if value range is limited
4. **Built-in Set Operations**: Use set intersection operations

### Key Insights:

1. **Uniqueness**: Result must contain unique elements only
2. **Order Independence**: Result can be in any order
3. **Duplicate Handling**: Need to avoid duplicates in result
4. **Efficiency**: Hash set provides O(1) average lookup time

## Solution: Hash Set Approach

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> seen(nums1.begin(), nums1.end());
        vector<int> rtn;
        for(int num: nums2) {
            if(seen.contains(num)) {
                rtn.emplace_back(num);
                seen.erase(num);
            }
        }
        return rtn;
    }
};
```

### Algorithm Explanation:

1. **Build Hash Set from First Array**:
   - Create `unordered_set<int> seen` from `nums1`
   - This automatically removes duplicates from `nums1`
   - Provides O(1) average lookup time

2. **Iterate Through Second Array**:
   - For each element `num` in `nums2`:
     - Check if `num` exists in `seen` using `seen.contains(num)`
     - If found:
       - Add `num` to result vector `rtn`
       - **Remove `num` from `seen`** to prevent duplicates in result

3. **Return Result**:
   - Return the result vector containing unique intersection elements

### Why Remove from Set?

The key insight is removing elements from `seen` after adding them to the result. This ensures:
- If `nums2` contains duplicates (e.g., `[2,2]`), only the first occurrence is added
- Subsequent occurrences won't match because the element was removed
- Result contains each intersecting element exactly once

### Example Walkthrough:

**Input:** `nums1 = [1,2,2,1]`, `nums2 = [2,2]`

```
Step 1: Build hash set from nums1
  seen = {1, 2}  (duplicates removed)

Step 2: Process nums2
  num = 2:
    seen.contains(2) = true
    rtn.push_back(2) → rtn = [2]
    seen.erase(2) → seen = {1}
  
  num = 2:
    seen.contains(2) = false (was removed)
    Skip

Result: [2] ✓
```

**Input:** `nums1 = [4,9,5]`, `nums2 = [9,4,9,8,4]`

```
Step 1: Build hash set from nums1
  seen = {4, 9, 5}

Step 2: Process nums2
  num = 9:
    seen.contains(9) = true
    rtn.push_back(9) → rtn = [9]
    seen.erase(9) → seen = {4, 5}
  
  num = 4:
    seen.contains(4) = true
    rtn.push_back(4) → rtn = [9, 4]
    seen.erase(4) → seen = {5}
  
  num = 9:
    seen.contains(9) = false (was removed)
    Skip
  
  num = 8:
    seen.contains(8) = false
    Skip
  
  num = 4:
    seen.contains(4) = false (was removed)
    Skip

Result: [9, 4] ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n + m)
  - Building hash set from `nums1`: O(n) where n = `nums1.size()`
  - Iterating through `nums2`: O(m) where m = `nums2.size()`
  - Hash set operations (contains, erase): O(1) average
  - Total: O(n + m)

- **Space Complexity:** O(n + k)
  - Hash set `seen`: O(n) to store unique elements from `nums1`
  - Result vector `rtn`: O(k) where k = number of unique intersection elements
  - Total: O(n + k) = O(n + m) in worst case

## Alternative Approaches

### Solution 2: Sorting + Two Pointers

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        
        vector<int> result;
        int i = 0, j = 0;
        
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                // Found intersection
                if (result.empty() || result.back() != nums1[i]) {
                    result.push_back(nums1[i]);
                }
                i++;
                j++;
            }
        }
        
        return result;
    }
};
```

**Complexity:**
- Time: O(n log n + m log m) for sorting + O(n + m) for two pointers = O(n log n + m log m)
- Space: O(1) extra space (excluding output)

**Pros:** No extra space for hash set  
**Cons:** Modifies input arrays, slower for small arrays

### Solution 3: Boolean Array (Fixed Range)

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        bool present[1001] = {false};
        for (int num : nums1) {
            present[num] = true;
        }
        
        vector<int> result;
        for (int num : nums2) {
            if (present[num]) {
                result.push_back(num);
                present[num] = false; // Mark as added
            }
        }
        
        return result;
    }
};
```

**Complexity:**
- Time: O(n + m)
- Space: O(1001) = O(1) fixed space

**Pros:** Very fast, constant space  
**Cons:** Only works when value range is limited (0-1000)

### Solution 4: Using Set Operations

```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        
        vector<int> result;
        for (int num : set1) {
            if (set2.count(num)) {
                result.push_back(num);
            }
        }
        
        return result;
    }
};
```

**Complexity:**
- Time: O(n + m)
- Space: O(n + m)

**Pros:** Clean and readable  
**Cons:** Uses more space (two sets)

## Key Insights

1. **Hash Set for Uniqueness**: Automatically handles duplicates
2. **Erase After Add**: Prevents duplicate results efficiently
3. **Order Independence**: Can return result in any order
4. **Space-Time Trade-off**: Hash set uses more space but provides O(1) lookup

## Edge Cases

1. **No intersection**: `nums1 = [1,2,3]`, `nums2 = [4,5,6]` → `[]`
2. **Complete overlap**: `nums1 = [1,2,3]`, `nums2 = [1,2,3]` → `[1,2,3]`
3. **One array empty**: `nums1 = []`, `nums2 = [1,2]` → `[]`
4. **Duplicates in both**: `nums1 = [1,1,2,2]`, `nums2 = [2,2]` → `[2]`
5. **Single element**: `nums1 = [1]`, `nums2 = [1]` → `[1]`

## Common Mistakes

1. **Not removing from set**: Results in duplicate elements in output
2. **Using vector instead of set**: Doesn't handle duplicates in `nums1`
3. **Wrong comparison**: Comparing entire arrays instead of elements
4. **Forgetting empty check**: Not handling empty arrays
5. **Order dependency**: Trying to maintain order when not needed

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Hash Set** | O(n + m) | O(n + k) | Fast, simple, handles duplicates | Extra space |
| **Sorting + Two Pointers** | O(n log n + m log m) | O(1) | No extra space | Modifies input, slower |
| **Boolean Array** | O(n + m) | O(1) | Very fast, constant space | Limited value range |
| **Set Operations** | O(n + m) | O(n + m) | Clean code | More space |

## When to Use Each Approach

- **Hash Set**: General purpose, most common solution
- **Sorting + Two Pointers**: When space is critical, input can be modified
- **Boolean Array**: When value range is small and known (0-1000)
- **Set Operations**: When code clarity is priority

## Related Problems

- [LC 350: Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) - Allow duplicates in result
- [LC 349: Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) - Unique elements only (this problem)
- [LC 1002: Find Common Characters](https://leetcode.com/problems/find-common-characters/) - Find common characters in strings
- [LC 1213: Intersection of Three Sorted Arrays](https://leetcode.com/problems/intersection-of-three-sorted-arrays/) - Three arrays intersection
- [LC 2248: Intersection of Multiple Arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/) - Multiple arrays intersection

---

*This problem demonstrates efficient **set-based intersection** using hash sets. The key technique is removing elements from the set after adding them to prevent duplicates in the result, ensuring each intersecting element appears exactly once.*

