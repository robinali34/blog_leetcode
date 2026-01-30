---
layout: post
title: "496. Next Greater Element I"
date: 2025-12-31 18:30:00 -0700
categories: [leetcode, easy, array, stack, monotonic-stack, hash-table]
permalink: /2025/12/31/easy-496-next-greater-element-i/
---

# 496. Next Greater Element I

## Problem Statement

The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the **next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return *an array `ans` of length `nums1.length` such that `ans[i]` is the **next greater element** as described above*.

## Examples

**Example 1:**
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
```

**Example 2:**
```
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
```

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are **unique**.
- All the integers of `nums1` also appear in `nums2`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Next greater definition**: What does "next greater element" mean? (Assumption: First element to the right that is strictly greater than current element)

2. **Array relationship**: How are nums1 and nums2 related? (Assumption: All elements of nums1 appear in nums2 - subset relationship)

3. **Position requirement**: Must the next greater element be immediately next? (Assumption: No - can be anywhere to the right, but must be the first one found)

4. **No greater element**: What should we return if no greater element exists? (Assumption: Return -1 - no next greater element found)

5. **Uniqueness**: Are all integers unique? (Assumption: Yes - per constraints, all integers are unique)

## Interview Deduction Process (10 minutes)

### Step 1: Brute-Force Approach (2 minutes)
**Initial Thought**: "I need to find next greater element. Let me search linearly for each element."

**Naive Solution**: For each element in nums1, find its position in nums2, then scan rightward to find first greater element.

**Complexity**: O(m × n) time, O(1) space

**Issues**:
- O(m × n) time complexity
- Linear search for each element
- Doesn't leverage any preprocessing

### Step 2: Semi-Optimized Approach (3 minutes)
**Insight**: "I can preprocess nums2 to build a map of next greater elements, then query nums1."

**Improved Solution**: Build hash map from nums2: for each element, find its next greater element and store. Then query nums1 elements from the map.

**Complexity**: O(m + n²) time, O(n) space

**Improvements**:
- Preprocessing reduces query time
- Still O(n²) for building map
- Better than brute-force for many queries

### Step 3: Optimized Solution (5 minutes)
**Final Optimization**: "I can use monotonic stack to build the next greater map in O(n) time."

**Best Solution**: Use monotonic decreasing stack to process nums2. For each element, pop smaller elements and record next greater. Build map in O(n), query in O(m).

**Complexity**: O(m + n) time, O(n) space

**Key Realizations**:
1. Monotonic stack is perfect for "next greater" problems
2. O(m + n) time is optimal
3. O(n) space for map is necessary
4. Stack approach processes nums2 in single pass

## Solution Approach

This problem requires finding the next greater element for each element in `nums1` within `nums2`. We can efficiently solve this using a **monotonic stack** to process `nums2` and store results in a hash map.

### Key Insights:

1. **Monotonic Stack**: Use stack to find next greater element efficiently
2. **Right-to-Left Traversal**: Process `nums2` from right to left
3. **Hash Map Storage**: Store next greater element for each value in `nums2`
4. **Lookup**: Query hash map for each element in `nums1`

### Algorithm:

1. **Build next greater map**: Traverse `nums2` from right to left using monotonic stack
2. **Store results**: Map each value to its next greater element
3. **Query results**: Look up each `nums1` element in the map

## Solution

### **Solution: Monotonic Stack with Hash Map**

```cpp
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> hashmap;
        stack<int> stk;
        for(int i = nums2.size() - 1; i >= 0; i--) {
            int num = nums2[i];
            while(!stk.empty() && num >= stk.top()) {
                stk.pop();
            }
            hashmap[num] = stk.empty()? -1 : stk.top();
            stk.push(num);
        }
        vector<int> rtn(nums1.size());
        for(int i = 0; i < (int)nums1.size(); i++) {
            rtn[i] = hashmap[nums1[i]];
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize Data Structures (Lines 4-5)**:
   - `hashmap`: Stores next greater element for each value in `nums2`
   - `stk`: Monotonic stack to track potential next greater elements

2. **Process nums2 from Right to Left (Lines 6-13)**:
   - **Traverse backwards**: Start from end of `nums2`
   - **Maintain monotonic stack**: Pop elements smaller than or equal to current
   - **Store result**: Next greater element is top of stack (or -1 if empty)
   - **Push current**: Add current element to stack

3. **Query Results for nums1 (Lines 14-17)**:
   - For each element in `nums1`, look up its next greater element in hashmap
   - Return results array

### **Example Walkthrough:**

**For `nums1 = [4,1,2], nums2 = [1,3,4,2]`:**

```
Step 1: Process nums2 from right to left

i=3: num = 2
  Stack: []
  Pop: nothing to pop
  hashmap[2] = -1 (stack empty)
  Push 2: Stack = [2]

i=2: num = 4
  Stack: [2]
  Pop: 2 <= 4? Yes → pop 2, Stack = []
  hashmap[4] = -1 (stack empty)
  Push 4: Stack = [4]

i=1: num = 3
  Stack: [4]
  Pop: 4 <= 3? No → keep 4
  hashmap[3] = 4 (top of stack)
  Push 3: Stack = [3, 4]

i=0: num = 1
  Stack: [3, 4]
  Pop: 3 <= 1? No → keep 3
  hashmap[1] = 3 (top of stack)
  Push 1: Stack = [1, 3, 4]

hashmap = {2: -1, 4: -1, 3: 4, 1: 3}

Step 2: Query nums1
nums1[0] = 4 → hashmap[4] = -1
nums1[1] = 1 → hashmap[1] = 3
nums1[2] = 2 → hashmap[2] = -1

Result: [-1, 3, -1]
```

**Visual Representation:**

```
nums2: [1, 3, 4, 2]
        0  1  2  3

Processing from right to left:

Position 3 (value 2):
  Stack: []
  Next greater: -1
  Stack: [2]

Position 2 (value 4):
  Stack: [2]
  Pop 2 (2 <= 4)
  Next greater: -1
  Stack: [4]

Position 1 (value 3):
  Stack: [4]
  4 > 3, keep 4
  Next greater: 4
  Stack: [3, 4]

Position 0 (value 1):
  Stack: [3, 4]
  3 > 1, keep 3
  Next greater: 3
  Stack: [1, 3, 4]

Results:
  1 → 3
  3 → 4
  4 → -1
  2 → -1
```

## Algorithm Breakdown

### **Key Insight: Monotonic Stack**

The stack maintains elements in **decreasing order** (from bottom to top):
- When we see a new element, pop all smaller or equal elements
- The top of stack is the next greater element
- Push current element to maintain monotonic property

### **Right-to-Left Traversal**

Processing from right to left ensures:
- We've already processed elements to the right
- Stack contains potential next greater elements
- Each element's next greater is already in stack

### **Why This Works**

1. **Stack Property**: Stack stores elements in decreasing order
2. **Popping Logic**: Elements ≤ current can't be next greater for anything left
3. **Top Element**: Top of stack is the first greater element to the right
4. **Hash Map**: Stores results for O(1) lookup later

## Monotonic Stack Template

Here's the general template for next greater element problems:

```cpp
vector<int> nextGreaterElement(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> stk;
    
    // Traverse from right to left
    for(int i = n - 1; i >= 0; i--) {
        // Pop elements that can't be next greater
        while(!stk.empty() && nums[i] >= stk.top()) {
            stk.pop();
        }
        
        // Top of stack is next greater element
        if(!stk.empty()) {
            result[i] = stk.top();
        }
        
        // Push current element
        stk.push(nums[i]);
    }
    
    return result;
}
```

### **Key Template Components:**

1. **Right-to-Left Traversal**: Process array backwards
2. **Monotonic Stack**: Maintain decreasing order
3. **Pop Condition**: Remove elements ≤ current
4. **Result Storage**: Store next greater or -1

## Complexity Analysis

### **Time Complexity:** O(n + m)
- **Process nums2**: O(n) where n = nums2.length
- **Query nums1**: O(m) where m = nums1.length
- **Total**: O(n + m)

### **Space Complexity:** O(n)
- **Hash map**: O(n) - stores next greater for each element in nums2
- **Stack**: O(n) - worst case all elements in stack
- **Total**: O(n)

## Key Points

1. **Monotonic Stack**: Maintains elements in decreasing order
2. **Right-to-Left**: Process from end to find next greater efficiently
3. **Hash Map**: O(1) lookup for results
4. **Single Pass**: Process nums2 once, query nums1 once
5. **Efficient**: O(n + m) time complexity

## Alternative Approaches

### **Approach 1: Monotonic Stack (Current Solution)**
- **Time**: O(n + m)
- **Space**: O(n)
- **Best for**: Optimal solution

### **Approach 2: Brute Force**
- **Time**: O(n × m)
- **Space**: O(1)
- **For each nums1**: Find in nums2, then search right
- **Inefficient**: O(n × m) time

### **Approach 3: Hash Map with Linear Search**
- **Time**: O(n × m)
- **Space**: O(n)
- **Build map**: Map value to index in nums2
- **Search**: For each nums1, find index and search right
- **Better than brute force**: But still O(n × m)

## Detailed Example Walkthrough

### **Example: `nums1 = [2,4], nums2 = [1,2,3,4]`**

```
Step 1: Process nums2 from right to left

i=3: num = 4
  Stack: []
  Pop: nothing
  hashmap[4] = -1
  Stack: [4]

i=2: num = 3
  Stack: [4]
  Pop: 4 <= 3? No → keep 4
  hashmap[3] = 4
  Stack: [3, 4]

i=1: num = 2
  Stack: [3, 4]
  Pop: 3 <= 2? No → keep 3
  hashmap[2] = 3
  Stack: [2, 3, 4]

i=0: num = 1
  Stack: [2, 3, 4]
  Pop: 2 <= 1? No → keep 2
  hashmap[1] = 2
  Stack: [1, 2, 3, 4]

hashmap = {4: -1, 3: 4, 2: 3, 1: 2}

Step 2: Query nums1
nums1[0] = 2 → hashmap[2] = 3
nums1[1] = 4 → hashmap[4] = -1

Result: [3, -1]
```

## Edge Cases

1. **No greater element**: Element is maximum in nums2 → return -1
2. **Single element**: nums2 has one element → return -1
3. **All decreasing**: nums2 in decreasing order → all return -1
4. **All increasing**: nums2 in increasing order → each has next greater
5. **Duplicate handling**: Problem states all integers are unique

## Related Problems

- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) - Current problem
- [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) - Circular array
- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) - Similar next greater pattern
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) - Monotonic stack application

## Tags

`Array`, `Stack`, `Monotonic Stack`, `Hash Table`, `Easy`

