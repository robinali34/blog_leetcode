---
layout: post
title: "27. Remove Element"
date: 2026-01-26 00:00:00 -0700
categories: [leetcode, easy, array, two-pointers]
permalink: /2026/01/26/easy-27-remove-element/
tags: [leetcode, easy, array, two-pointers, in-place]
---

# 27. Remove Element

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return *the number of elements in* `nums` *which are not equal to* `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The elements beyond the first `k` elements are not important as well as the size of `nums`.
- Return `k`.

## Examples

**Example 1:**

```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**

```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 3, 0, and 4.
Note that the five elements can be returned in any order, and it does not matter what you leave beyond the returned k.
```

## Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **In-place modification**: Should we modify the array in-place or return a new array? (Assumption: Modify in-place - the problem asks to remove elements in-place)

2. **Order preservation**: Do we need to preserve the relative order of remaining elements? (Assumption: The problem doesn't explicitly require order preservation, but it's typically expected)

3. **Return value**: What should we return - the new length or the modified array? (Assumption: Return the new length `k`, and the first `k` elements should be the valid elements)

4. **Empty array**: What should we return if the array is empty? (Assumption: Return `0`)

5. **Value not present**: What if `val` doesn't exist in the array? (Assumption: Return the original length - no elements removed)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Create a new array, iterate through the original array, and copy only elements that are not equal to `val` to the new array. Return the size of the new array. This approach uses O(n) extra space and requires O(n) time. However, the problem requires in-place modification, so this doesn't meet the requirement.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use two pointers from both ends: use `left` pointer starting from the beginning and `right` pointer from the end. When `nums[left] == val`, swap it with `nums[right]` and decrement `right`. Otherwise, increment `left`. This approach modifies the array in-place but doesn't preserve the relative order of remaining elements, which may not be acceptable.

**Step 3: Optimized Solution (5 minutes)**

Use two pointers moving in the same direction: `curr` scans through all elements, and `last` tracks the position where the next valid element should be placed. When `nums[curr] != val`, copy it to `nums[last]` and increment `last`. This achieves O(n) time with O(1) space, maintains relative order, and modifies the array in-place. The key insight is that we can overwrite elements at the `last` position since we've already processed them, allowing in-place modification without extra space.

## Solution Approach

This problem requires removing all occurrences of `val` from the array **in-place** and returning the count of remaining elements. The key is using **two pointers** to efficiently filter elements.

### Key Insights:

1. **Two Pointers**: Use one pointer to iterate (`curr`) and one to track valid position (`last`)
2. **In-Place Modification**: Overwrite elements at `last` position with valid elements
3. **Order Preservation**: The solution maintains relative order of non-removed elements
4. **Simple Logic**: If current element != val, copy it to `last` position and increment `last`

## Solution

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int last = 0;
        for(int curr = 0; curr < (int)nums.size(); curr++) {
            if(nums[curr] != val) {
                nums[last] = nums[curr];
                last += 1;
            }
        }
        return last;
    }
};
```

### Algorithm Explanation:

#### **Two Pointers Technique:**

1. **`curr`**: Iterator through the entire array
   - Scans all elements from start to end
   - Checks if element equals `val`

2. **`last`**: Position where next valid element should be placed
   - Tracks the end of the "valid" region
   - Only increments when we find a valid element

3. **Process**:
   - For each element at `curr`:
     - If `nums[curr] != val`: Copy to `nums[last]` and increment `last`
     - If `nums[curr] == val`: Skip (don't copy, don't increment `last`)

4. **Result**: `last` is the count of valid elements (and the new length)

### Example Walkthrough:

**Input:** `nums = [3,2,2,3]`, `val = 3`

```
Initial: nums = [3,2,2,3], last = 0, curr = 0

curr=0: nums[0]=3 == val → skip
  nums = [3,2,2,3], last = 0

curr=1: nums[1]=2 != val → copy to nums[0], last++
  nums = [2,2,2,3], last = 1

curr=2: nums[2]=2 != val → copy to nums[1], last++
  nums = [2,2,2,3], last = 2

curr=3: nums[3]=3 == val → skip
  nums = [2,2,2,3], last = 2

Result: return 2, nums = [2,2,_,_] ✓
```

**Input:** `nums = [0,1,2,2,3,0,4,2]`, `val = 2`

```
Initial: nums = [0,1,2,2,3,0,4,2], last = 0

curr=0: nums[0]=0 != 2 → nums[0]=0, last=1
curr=1: nums[1]=1 != 2 → nums[1]=1, last=2
curr=2: nums[2]=2 == 2 → skip
curr=3: nums[3]=2 == 2 → skip
curr=4: nums[4]=3 != 2 → nums[2]=3, last=3
curr=5: nums[5]=0 != 2 → nums[3]=0, last=4
curr=6: nums[6]=4 != 2 → nums[4]=4, last=5
curr=7: nums[7]=2 == 2 → skip

Result: return 5, nums = [0,1,3,0,4,_,_,_] ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Single pass through the array: O(n)
  - Each element visited exactly once
  - Overall: O(n)

- **Space Complexity:** O(1)
  - Only two variables (`last`, `curr`): O(1)
  - In-place modification: no extra array
  - Overall: O(1)

## Key Insights

1. **Two Pointers Pattern**: Classic pattern for in-place array modification
2. **Write Pointer (`last`)**: Tracks where to write next valid element
3. **Read Pointer (`curr`)**: Scans through all elements
4. **In-Place**: No extra space needed, modifies array directly
5. **Order Preservation**: Maintains relative order of non-removed elements

## Edge Cases

1. **Empty array**: `nums = []` → return `0`
2. **All elements removed**: `nums = [3,3,3]`, `val = 3` → return `0`
3. **No elements removed**: `nums = [1,2,3]`, `val = 4` → return `3`
4. **Single element removed**: `nums = [1]`, `val = 1` → return `0`
5. **Single element kept**: `nums = [1]`, `val = 2` → return `1`

## Common Mistakes

1. **Wrong pointer logic**: Incrementing `last` even when element equals `val`
2. **Index out of bounds**: Not checking bounds when accessing `nums[curr]`
3. **Wrong return value**: Returning `nums.size()` instead of `last`
4. **Not modifying array**: Only counting without actually removing elements
5. **Type casting**: Forgetting `(int)` cast for `nums.size()` comparison

## Alternative Approaches

### Approach 2: Two Pointers from Both Ends

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0, right = nums.size();
        while(left < right) {
            if(nums[left] == val) {
                nums[left] = nums[right - 1];
                right--;
            } else {
                left++;
            }
        }
        return right;
    }
};
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Pros**: 
- May skip some elements when swapping from end
- Can be faster if `val` appears frequently

**Cons**: 
- Doesn't preserve order
- More complex logic

### Approach 3: Using STL remove

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        auto it = remove(nums.begin(), nums.end(), val);
        return distance(nums.begin(), it);
    }
};
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Pros**: 
- Very concise
- Uses standard library

**Cons**: 
- Less educational
- May not be allowed in interviews

## Comparison of Approaches

| Approach | Time | Space | Order Preserved | Complexity |
|----------|------|-------|----------------|------------|
| **Two Pointers (Forward)** | O(n) | O(1) | Yes | Simple |
| **Two Pointers (Both Ends)** | O(n) | O(1) | No | Moderate |
| **STL remove** | O(n) | O(1) | Yes | Very Simple |

## Related Problems

- [LC 26: Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) - Similar two pointers pattern
- [LC 283: Move Zeroes](https://leetcode.com/problems/move-zeroes/) - Move zeros to end
- [LC 80: Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) - Allow at most 2 duplicates
- [LC 203: Remove Linked List Elements](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-easy-203-remove-linked-list-elements/) - Similar problem on linked list

---

*This problem demonstrates the **two pointers** technique for in-place array modification. The key insight is using a write pointer (`last`) to track where valid elements should be placed, while scanning with a read pointer (`curr`).*
