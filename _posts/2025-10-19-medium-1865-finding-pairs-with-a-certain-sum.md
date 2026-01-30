---
layout: post
title: "[Medium] 1865. Finding Pairs With a Certain Sum"
date: 2025-10-19 17:38:17 -0700
categories: leetcode algorithm medium cpp hash-map data-structure problem-solving
---

# [Medium] 1865. Finding Pairs With a Certain Sum

You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a data structure that supports the following operations:

1. **`FindSumPairs(int[] nums1, int[] nums2)`** - Initializes the `FindSumPairs` object with two integer arrays.
2. **`void add(int index, int val)`** - Adds `val` to `nums2[index]`.
3. **`int count(int tot)`** - Returns the number of pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.

## Examples

**Example 1:**
```
Input:
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output: [null, 8, null, 2, 1, null, null, 11]
Explanation:
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8. Pairs (0,4), (1,4), (2,2), (2,4), (3,2), (3,4), (4,2), (4,4)
findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // return 2. Pairs (0,3), (1,3)
findSumPairs.count(4);  // return 1. Pair (0,0)
findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // return 11. Pairs (0,4), (1,4), (2,2), (2,4), (3,2), (3,4), (4,2), (4,4), (5,2), (5,4), (6,2), (6,4)
```

**Example 2:**
```
Input:
["FindSumPairs", "count", "add", "count"]
[[[1], [1]], [2], [0, 1], [2]]
Output: [null, 1, null, 1]
Explanation:
FindSumPairs findSumPairs = new FindSumPairs([1], [1]);
findSumPairs.count(2);  // return 1. Pair (0,0)
findSumPairs.add(0, 1); // now nums2 = [2]
findSumPairs.count(2);  // return 1. Pair (0,0)
```

## Constraints

- `1 <= nums1.length <= 10^5`
- `1 <= nums2.length <= 10^5`
- `1 <= nums1[i] <= 10^9`
- `1 <= nums2[i] <= 10^9`
- `0 <= index < nums2.length`
- `1 <= val <= 10^4`
- `1 <= tot <= 10^9`
- At most `1000` calls will be made to `add` and `count` each.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Pair definition**: What constitutes a valid pair? (Assumption: Pair (i, j) where nums1[i] + nums2[j] == target - one element from each array)

2. **Update operations**: What does add() do? (Assumption: Adds val to nums2[index] - modifies nums2 array)

3. **Count operation**: What should count() return? (Assumption: Number of pairs (i, j) where nums1[i] + nums2[j] == target)

4. **Pair uniqueness**: Can pairs be counted multiple times? (Assumption: Yes - if same pair appears multiple times, count each occurrence)

5. **Return value**: What should count() return? (Assumption: Integer count of valid pairs)

## Solution: Hash Map with Count Tracking

**Time Complexity:** 
- Constructor: O(n) where n is length of nums2
- add: O(1)
- count: O(m) where m is length of nums1

**Space Complexity:** O(n) where n is length of nums2

Use a hash map to track the count of each value in nums2, then for each count operation, iterate through nums1 and check if the complement exists in nums2.

```cpp
class FindSumPairs {
private:
    vector<int> nums1, nums2;
    unordered_map<int, int> cnts;
    
public:
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        this->nums1 = nums1;
        this->nums2 = nums2;
        for(auto& num: nums2) cnts[num]++;
    }
    
    void add(int index, int val) {
        cnts[nums2[index]]--;
        nums2[index] += val;
        cnts[nums2[index]]++;
    }
    
    int count(int tot) {
        int cnt = 0;
        for(int num: nums1) {
            int rest = tot - num;
            if(cnts.contains(rest)) {
                cnt += cnts[rest];
            }
        }
        return cnt;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */
```

## How the Algorithm Works

**Key Insight:** Use a hash map to track the count of each value in nums2, then for each count operation, iterate through nums1 and check if the complement exists in nums2.

**Steps:**
1. **Constructor:** Store nums1 and nums2, build count map for nums2
2. **add operation:** Update count map when nums2 values change
3. **count operation:** For each nums1 value, check if complement exists in nums2
4. **Return total count** of valid pairs

## Step-by-Step Example

### Example: `nums1 = [1, 1, 2, 2, 2, 3]`, `nums2 = [1, 4, 5, 2, 5, 4]`

**Step 1: Constructor**
```
nums1 = [1, 1, 2, 2, 2, 3]
nums2 = [1, 4, 5, 2, 5, 4]
cnts = {1: 1, 4: 2, 5: 2, 2: 1}
```

**Step 2: count(7)**
```
For each nums1 value:
- num = 1, rest = 7 - 1 = 6, cnts[6] = 0 → cnt += 0
- num = 1, rest = 7 - 1 = 6, cnts[6] = 0 → cnt += 0
- num = 2, rest = 7 - 2 = 5, cnts[5] = 2 → cnt += 2
- num = 2, rest = 7 - 2 = 5, cnts[5] = 2 → cnt += 2
- num = 2, rest = 7 - 2 = 5, cnts[5] = 2 → cnt += 2
- num = 3, rest = 7 - 3 = 4, cnts[4] = 2 → cnt += 2

Total count = 0 + 0 + 2 + 2 + 2 + 2 = 8
```

**Step 3: add(3, 2)**
```
nums2[3] = 2 + 2 = 4
cnts[2]-- → cnts[2] = 0
cnts[4]++ → cnts[4] = 3
cnts = {1: 1, 4: 3, 5: 2, 2: 0}
```

**Step 4: count(8)**
```
For each nums1 value:
- num = 1, rest = 8 - 1 = 7, cnts[7] = 0 → cnt += 0
- num = 1, rest = 8 - 1 = 7, cnts[7] = 0 → cnt += 0
- num = 2, rest = 8 - 2 = 6, cnts[6] = 0 → cnt += 0
- num = 2, rest = 8 - 2 = 6, cnts[6] = 0 → cnt += 0
- num = 2, rest = 8 - 2 = 6, cnts[6] = 0 → cnt += 0
- num = 3, rest = 8 - 3 = 5, cnts[5] = 2 → cnt += 2

Total count = 0 + 0 + 0 + 0 + 0 + 2 = 2
```

## Algorithm Breakdown

### Constructor:
```cpp
FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
    this->nums1 = nums1;
    this->nums2 = nums2;
    for(auto& num: nums2) cnts[num]++;
}
```

**Process:**
1. **Store arrays:** Keep references to nums1 and nums2
2. **Build count map:** Count frequency of each value in nums2
3. **Initialize:** Prepare for add and count operations

### Add Operation:
```cpp
void add(int index, int val) {
    cnts[nums2[index]]--;
    nums2[index] += val;
    cnts[nums2[index]]++;
}
```

**Process:**
1. **Decrement old count:** Remove old value from count map
2. **Update array:** Add val to nums2[index]
3. **Increment new count:** Add new value to count map

### Count Operation:
```cpp
int count(int tot) {
    int cnt = 0;
    for(int num: nums1) {
        int rest = tot - num;
        if(cnts.contains(rest)) {
            cnt += cnts[rest];
        }
    }
    return cnt;
}
```

**Process:**
1. **Iterate nums1:** Check each value in nums1
2. **Calculate complement:** Find required value in nums2
3. **Check existence:** If complement exists, add its count
4. **Return total:** Sum of all valid pairs

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Constructor | O(n) | O(n) |
| add | O(1) | O(1) |
| count | O(m) | O(1) |
| **Total** | **O(n + m)** | **O(n)** |

Where n is the length of nums2 and m is the length of nums1.

## Edge Cases

1. **Single elements:** `nums1 = [1]`, `nums2 = [1]` → `count(2) = 1`
2. **No pairs:** `nums1 = [1]`, `nums2 = [2]` → `count(1) = 0`
3. **Multiple same values:** `nums1 = [1,1]`, `nums2 = [1,1]` → `count(2) = 4`
4. **Large values:** Handle large integers correctly

## Key Insights

### Hash Map Optimization:
1. **Count tracking:** Use hash map to track frequency of nums2 values
2. **Fast lookup:** O(1) lookup for complement checking
3. **Efficient updates:** O(1) update when nums2 values change
4. **Memory trade-off:** Use extra space for faster operations

### Pair Counting:
1. **Complement approach:** For each nums1 value, find complement in nums2
2. **Count multiplication:** Multiply by frequency of complement
3. **Complete coverage:** Check all possible pairs
4. **Efficient calculation:** Avoid nested loops

## Detailed Example Walkthrough

### Example: `nums1 = [1, 2]`, `nums2 = [1, 2, 3]`

**Step 1: Constructor**
```
nums1 = [1, 2]
nums2 = [1, 2, 3]
cnts = {1: 1, 2: 1, 3: 1}
```

**Step 2: count(3)**
```
For each nums1 value:
- num = 1, rest = 3 - 1 = 2, cnts[2] = 1 → cnt += 1
- num = 2, rest = 3 - 2 = 1, cnts[1] = 1 → cnt += 1

Total count = 1 + 1 = 2
```

**Step 3: add(0, 1)**
```
nums2[0] = 1 + 1 = 2
cnts[1]-- → cnts[1] = 0
cnts[2]++ → cnts[2] = 2
cnts = {1: 0, 2: 2, 3: 1}
```

**Step 4: count(3)**
```
For each nums1 value:
- num = 1, rest = 3 - 1 = 2, cnts[2] = 2 → cnt += 2
- num = 2, rest = 3 - 2 = 1, cnts[1] = 0 → cnt += 0

Total count = 2 + 0 = 2
```

## Alternative Approaches

### Approach 1: Brute Force
```cpp
class FindSumPairs {
private:
    vector<int> nums1, nums2;
    
public:
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        this->nums1 = nums1;
        this->nums2 = nums2;
    }
    
    void add(int index, int val) {
        nums2[index] += val;
    }
    
    int count(int tot) {
        int cnt = 0;
        for(int i = 0; i < nums1.size(); i++) {
            for(int j = 0; j < nums2.size(); j++) {
                if(nums1[i] + nums2[j] == tot) {
                    cnt++;
                }
            }
        }
        return cnt;
    }
};
```

**Time Complexity:** O(m × n) for count operation  
**Space Complexity:** O(1)

### Approach 2: Two Hash Maps
```cpp
class FindSumPairs {
private:
    vector<int> nums1, nums2;
    unordered_map<int, int> cnts1, cnts2;
    
public:
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        this->nums1 = nums1;
        this->nums2 = nums2;
        for(auto& num: nums1) cnts1[num]++;
        for(auto& num: nums2) cnts2[num]++;
    }
    
    void add(int index, int val) {
        cnts2[nums2[index]]--;
        nums2[index] += val;
        cnts2[nums2[index]]++;
    }
    
    int count(int tot) {
        int cnt = 0;
        for(auto& [num, freq]: cnts1) {
            int rest = tot - num;
            if(cnts2.contains(rest)) {
                cnt += freq * cnts2[rest];
            }
        }
        return cnt;
    }
};
```

**Time Complexity:** O(k) for count operation where k is unique values in nums1  
**Space Complexity:** O(m + n)

## Common Mistakes

1. **Wrong count update:** Not properly updating count map in add operation
2. **Missing edge cases:** Not handling empty arrays or single elements
3. **Overflow issues:** Not considering large integer values
4. **Inefficient lookup:** Using linear search instead of hash map

## Related Problems

- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)
- [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

## Why This Solution Works

### Hash Map Optimization:
1. **Count tracking:** Use hash map to track frequency of nums2 values
2. **Fast lookup:** O(1) lookup for complement checking
3. **Efficient updates:** O(1) update when nums2 values change
4. **Memory trade-off:** Use extra space for faster operations

### Pair Counting:
1. **Complement approach:** For each nums1 value, find complement in nums2
2. **Count multiplication:** Multiply by frequency of complement
3. **Complete coverage:** Check all possible pairs
4. **Efficient calculation:** Avoid nested loops

### Key Algorithm Properties:
1. **Correctness:** Always produces valid result
2. **Efficiency:** O(1) add, O(m) count operations
3. **Scalability:** Handles large arrays efficiently
4. **Simplicity:** Easy to understand and implement
