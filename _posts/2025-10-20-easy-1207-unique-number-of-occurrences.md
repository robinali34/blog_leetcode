---
layout: post
title: "LC 1207: Unique Number of Occurrences"
date: 2025-10-20 18:00:00 -0700
categories: leetcode easy array hash-table
permalink: /posts/2025-10-20-easy-1207-unique-number-of-occurrences/
tags: [leetcode, easy, array, hash-table, counting]
---

# LC 1207: Unique Number of Occurrences

**Difficulty:** Easy  
**Category:** Array, Hash Table  
**Companies:** Amazon, Google, Microsoft

## Problem Statement

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique**, or `false` otherwise.

### Examples

**Example 1:**
```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 occurrences, and 3 has 1 occurrence. No two values have the same number of occurrences.
```

**Example 2:**
```
Input: arr = [1,2]
Output: false
Explanation: The value 1 has 1 occurrence, and 2 has 1 occurrence. Two values have the same number of occurrences.
```

**Example 3:**
```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
Explanation: The value -3 has 3 occurrences, 0 has 2 occurrences, 1 has 4 occurrences, and 10 has 1 occurrence. No two values have the same number of occurrences.
```

### Constraints

- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Occurrence definition**: What does "occurrence" mean? (Assumption: Number of times each value appears in the array)

2. **Unique occurrences**: What makes occurrences "unique"? (Assumption: Each occurrence count appears only once - no two values have the same count)

3. **Return value**: What should we return? (Assumption: Boolean - true if all occurrence counts are unique, false otherwise)

4. **Empty array**: What if array is empty? (Assumption: Return true - no occurrences means all are unique)

5. **Single element**: What if array has one element? (Assumption: Return true - one occurrence count is unique)

## Interview Deduction Process (10 minutes)

### Step 1: Brute-Force Approach (2 minutes)
**Initial Thought**: "I need to check if occurrence counts are unique. Let me count occurrences manually."

**Naive Solution**: Count occurrences of each value manually, then check if all counts are unique by comparing all pairs.

**Complexity**: O(n²) time, O(n) space

**Issues**:
- O(n²) time - inefficient
- Manual comparison is error-prone
- Doesn't leverage hash set
- Can be optimized

### Step 2: Semi-Optimized Approach (3 minutes)
**Insight**: "I can use hash map to count occurrences, then check uniqueness."

**Improved Solution**: Use hash map to count occurrences. Then check if all counts are unique by comparing counts or using another data structure.

**Complexity**: O(n) time, O(n) space

**Improvements**:
- Hash map enables efficient counting
- O(n) time is much better
- Still need to check uniqueness
- Can optimize uniqueness check

### Step 3: Optimized Solution (5 minutes)
**Final Optimization**: "Use hash set to check uniqueness of counts."

**Best Solution**: Use hash map to count occurrences, then use hash set to check if all counts are unique. If set size equals map size, all counts are unique.

**Complexity**: O(n) time, O(n) space

**Key Realizations**:
1. Hash map for counting is standard
2. Hash set for uniqueness check is elegant
3. O(n) time is optimal - must process each element
4. O(n) space is optimal for both structures

## Solution Approaches

### Approach 1: Hash Map + Hash Set (Recommended)

**Algorithm:**
1. Count frequency of each element using hash map
2. Store all frequencies in a hash set
3. Check if hash set size equals hash map size (no duplicate frequencies)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> freqs;
        unordered_set<int> occurs;
        for(int num: arr) freqs[num]++;

        for(auto& [num, freq]: freqs)
            occurs.insert(freq);
        return occurs.size() == freqs.size();
    }
};
```

### Approach 2: Early Termination Optimization

**Algorithm:**
1. Count frequency of each element using hash map
2. While inserting frequencies into hash set, check for duplicates
3. Return false immediately if duplicate frequency found

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> freqs;
        unordered_set<int> occurs;
        for(int num: arr) freqs[num]++;

        for(auto& [_, freq]: freqs)
            if(!occurs.insert(freq).second) return false;

        return occurs.size() == freqs.size();
    }
};
```

### Approach 3: Array-Based Counting

**Algorithm:**
1. Use array to count frequencies (since values are in range [-1000, 1000])
2. Use another array to count frequency counts
3. Check if any frequency count exceeds 1

**Time Complexity:** O(n)  
**Space Complexity:** O(1) - fixed size arrays

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        int freq[2001] = {0};  // Offset by 1000 for negative numbers
        int count[1001] = {0}; // Max frequency is 1000
        
        // Count frequencies
        for(int num : arr) {
            freq[num + 1000]++;
        }
        
        // Count frequency counts
        for(int i = 0; i < 2001; i++) {
            if(freq[i] > 0) {
                count[freq[i]]++;
                if(count[freq[i]] > 1) return false;
            }
        }
        
        return true;
    }
};
```

## Algorithm Analysis

### Approach Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Hash Map + Set | O(n) | O(n) | Simple, readable | Extra space for set |
| Early Termination | O(n) | O(n) | Early exit optimization | Slightly more complex |
| Array Counting | O(n) | O(1) | Constant space | Limited to small ranges |

### Key Insights

1. **Frequency Counting**: Use hash map to count occurrences of each element
2. **Duplicate Detection**: Use hash set to detect duplicate frequencies
3. **Size Comparison**: If set size equals map size, all frequencies are unique
4. **Early Termination**: Can optimize by checking for duplicates during insertion

## Implementation Details

### Hash Set Insert Behavior
```cpp
// insert() returns pair<iterator, bool>
// second is true if insertion successful (no duplicate)
if(!occurs.insert(freq).second) return false;
```

### Array Offset Technique
```cpp
// Offset by 1000 to handle negative numbers
freq[num + 1000]++;
```

## Edge Cases

1. **Single Element**: `[1]` → true (frequency 1 is unique)
2. **All Same Elements**: `[1,1,1]` → true (frequency 3 is unique)
3. **All Different Elements**: `[1,2,3]` → true (all frequencies are 1)
4. **Duplicate Frequencies**: `[1,2,2,3]` → false (both 1 and 3 have frequency 1)

## Follow-up Questions

- What if the array could contain very large numbers?
- How would you handle floating-point numbers?
- What if you needed to find which frequencies are duplicated?
- How would you optimize for very large arrays?

## Related Problems

- [LC 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [LC 451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
- [LC 692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

## Optimization Techniques

1. **Early Termination**: Stop as soon as duplicate frequency is found
2. **Space Optimization**: Use arrays instead of hash maps for small ranges
3. **Memory Efficiency**: Avoid storing unnecessary data
4. **Cache Performance**: Array-based approach has better cache locality

## Code Quality Notes

1. **Readability**: First approach is most readable and maintainable
2. **Performance**: Array approach is fastest for small ranges
3. **Scalability**: Hash map approach works for any range
4. **Robustness**: All approaches handle edge cases correctly

---

*This problem demonstrates the importance of choosing the right data structure based on constraints and requirements, showing how different approaches can optimize for different aspects.*
