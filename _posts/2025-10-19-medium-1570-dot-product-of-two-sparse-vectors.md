---
layout: post
title: "[Medium] 1570. Dot Product of Two Sparse Vectors"
date: 2025-10-19 20:05:38 -0700
categories: leetcode algorithm medium cpp hash-map data-structure optimization problem-solving
---

# [Medium] 1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class `SparseVector`:

- `SparseVector(nums)` Initializes the object with the vector `nums`
- `dotProduct(vec)` Compute the dot product between the instance of `SparseVector` and `vec`

A **sparse vector** is a vector that has mostly zero values. You should store the sparse vector efficiently and compute the dot product between two sparse vectors.

## Examples

**Example 1:**
```
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector([1,0,0,2,3]) and v2 = SparseVector([0,3,0,4,0])
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
```

**Example 2:**
```
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector([0,1,0,0,0]) and v2 = SparseVector([0,0,0,0,2])
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
```

**Example 3:**
```
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
Explanation: v1 = SparseVector([0,1,0,0,2,0,0]) and v2 = SparseVector([1,0,0,0,3,0,4])
v1.dotProduct(v2) = 0*1 + 1*0 + 0*0 + 0*0 + 2*3 + 0*0 + 0*4 = 6
```

## Constraints

- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 100`

## Solution: Hash Map with Optimization

**Time Complexity:** 
- Constructor: O(n) where n is the length of the vector
- dotProduct: O(min(k1, k2)) where k1, k2 are number of non-zero elements

**Space Complexity:** O(k) where k is the number of non-zero elements

Use a hash map to store only non-zero elements, then optimize dot product by iterating through the smaller hash map.

```cpp
class SparseVector {
private:
    unordered_map<int, int> cache;
    
public:
    SparseVector(vector<int> &nums) {
        for(int i = 0; i < (int)nums.size(); i++) {
            if(nums[i] != 0) {
                cache[i] = nums[i];
            }
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
        int rtn = 0;
        auto& smaller = (this->cache.size() <= vec.cache.size()) ? this->cache : vec.cache;
        auto& larger = (this->cache.size() <= vec.cache.size()) ? vec.cache : this->cache;
        
        for(auto& [idx, num]: smaller) {
            if(larger.contains(idx)) {
                rtn += num * larger[idx];
            }
        }
        return rtn;
    }
};

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);
```

## How the Algorithm Works

**Key Insight:** Store only non-zero elements in a hash map, then optimize dot product by iterating through the smaller hash map.

**Steps:**
1. **Constructor:** Store only non-zero elements with their indices
2. **Dot product:** Iterate through smaller hash map and check for matching indices
3. **Optimization:** Always iterate through the smaller hash map for efficiency
4. **Return result:** Sum of products of matching non-zero elements

## Step-by-Step Example

### Example: `nums1 = [1,0,0,2,3]`, `nums2 = [0,3,0,4,0]`

**Step 1: Constructor for v1**
```
nums1 = [1,0,0,2,3]
cache1 = {0: 1, 3: 2, 4: 3}
```

**Step 2: Constructor for v2**
```
nums2 = [0,3,0,4,0]
cache2 = {1: 3, 3: 4}
```

**Step 3: Dot Product Calculation**
```
smaller = cache2 = {1: 3, 3: 4}  (size = 2)
larger = cache1 = {0: 1, 3: 2, 4: 3}  (size = 3)

For each element in smaller:
- idx = 1, num = 3: larger[1] = 0 (not found) → skip
- idx = 3, num = 4: larger[3] = 2 → rtn += 4 * 2 = 8

Result = 8
```

## Algorithm Breakdown

### Constructor:
```cpp
SparseVector(vector<int> &nums) {
    for(int i = 0; i < (int)nums.size(); i++) {
        if(nums[i] != 0) {
            cache[i] = nums[i];
        }
    }
}
```

**Process:**
1. **Iterate through vector:** Check each element
2. **Store non-zero elements:** Only store elements that are not zero
3. **Index-value mapping:** Map index to value for efficient lookup
4. **Space optimization:** Save space by not storing zeros

### Dot Product:
```cpp
int dotProduct(SparseVector& vec) {
    int rtn = 0;
    auto& smaller = (this->cache.size() <= vec.cache.size()) ? this->cache : vec.cache;
    auto& larger = (this->cache.size() <= vec.cache.size()) ? vec.cache : this->cache;
    
    for(auto& [idx, num]: smaller) {
        if(larger.contains(idx)) {
            rtn += num * larger[idx];
        }
    }
    return rtn;
}
```

**Process:**
1. **Choose smaller hash map:** Optimize by iterating through smaller map
2. **Check for matches:** For each index in smaller map, check if it exists in larger map
3. **Calculate product:** If match found, multiply values and add to result
4. **Return sum:** Total dot product of matching elements

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Constructor | O(n) | O(k) |
| dotProduct | O(min(k1, k2)) | O(1) |
| **Total** | **O(n + min(k1, k2))** | **O(k1 + k2)** |

Where n is the length of the vector, k1 and k2 are the number of non-zero elements in each vector.

## Edge Cases

1. **All zeros:** `nums1 = [0,0,0]`, `nums2 = [0,0,0]` → `0`
2. **Single non-zero:** `nums1 = [1,0,0]`, `nums2 = [0,0,1]` → `0`
3. **No matches:** `nums1 = [1,0,0]`, `nums2 = [0,1,0]` → `0`
4. **Perfect match:** `nums1 = [1,2,3]`, `nums2 = [1,2,3]` → `14`

## Key Insights

### Hash Map Optimization:
1. **Space efficiency:** Store only non-zero elements
2. **Fast lookup:** O(1) access to non-zero elements
3. **Index preservation:** Maintain original indices for dot product
4. **Memory trade-off:** Use extra space for faster operations

### Dot Product Optimization:
1. **Smaller iteration:** Always iterate through smaller hash map
2. **Match checking:** Check if index exists in larger hash map
3. **Product calculation:** Multiply matching values
4. **Efficient computation:** Avoid unnecessary iterations

## Detailed Example Walkthrough

### Example: `nums1 = [0,1,0,0,2,0,0]`, `nums2 = [1,0,0,0,3,0,4]`

**Step 1: Constructor for v1**
```
nums1 = [0,1,0,0,2,0,0]
cache1 = {1: 1, 4: 2}
```

**Step 2: Constructor for v2**
```
nums2 = [1,0,0,0,3,0,4]
cache2 = {0: 1, 4: 3, 6: 4}
```

**Step 3: Dot Product Calculation**
```
smaller = cache1 = {1: 1, 4: 2}  (size = 2)
larger = cache2 = {0: 1, 4: 3, 6: 4}  (size = 3)

For each element in smaller:
- idx = 1, num = 1: larger[1] = 0 (not found) → skip
- idx = 4, num = 2: larger[4] = 3 → rtn += 2 * 3 = 6

Result = 6
```

## Alternative Approaches

### Approach 1: Brute Force
```cpp
class SparseVector {
private:
    vector<int> nums;
    
public:
    SparseVector(vector<int> &nums) {
        this->nums = nums;
    }
    
    int dotProduct(SparseVector& vec) {
        int result = 0;
        for(int i = 0; i < nums.size(); i++) {
            result += nums[i] * vec.nums[i];
        }
        return result;
    }
};
```

**Time Complexity:** O(n) for dotProduct  
**Space Complexity:** O(n)

### Approach 2: List of Pairs
```cpp
class SparseVector {
private:
    vector<pair<int, int>> nonZeros;
    
public:
    SparseVector(vector<int> &nums) {
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] != 0) {
                nonZeros.push_back({i, nums[i]});
            }
        }
    }
    
    int dotProduct(SparseVector& vec) {
        int result = 0;
        int i = 0, j = 0;
        
        while(i < nonZeros.size() && j < vec.nonZeros.size()) {
            if(nonZeros[i].first == vec.nonZeros[j].first) {
                result += nonZeros[i].second * vec.nonZeros[j].second;
                i++;
                j++;
            } else if(nonZeros[i].first < vec.nonZeros[j].first) {
                i++;
            } else {
                j++;
            }
        }
        
        return result;
    }
};
```

**Time Complexity:** O(k1 + k2) for dotProduct  
**Space Complexity:** O(k1 + k2)

## Common Mistakes

1. **Not optimizing iteration:** Always iterate through smaller hash map
2. **Missing zero check:** Not checking if index exists in larger map
3. **Wrong index mapping:** Confusing index with value
4. **Inefficient storage:** Storing all elements including zeros

## Related Problems

- [311. Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/)
- [1428. Leftmost Column with at Least a One](https://leetcode.com/problems/leftmost-column-with-at-least-a-one/)
- [1588. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)
- [1641. Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/)

## Why This Solution Works

### Hash Map Optimization:
1. **Space efficiency:** Store only non-zero elements
2. **Fast lookup:** O(1) access to non-zero elements
3. **Index preservation:** Maintain original indices for dot product
4. **Memory trade-off:** Use extra space for faster operations

### Dot Product Optimization:
1. **Smaller iteration:** Always iterate through smaller hash map
2. **Match checking:** Check if index exists in larger hash map
3. **Product calculation:** Multiply matching values
4. **Efficient computation:** Avoid unnecessary iterations

### Key Algorithm Properties:
1. **Correctness:** Always produces valid result
2. **Efficiency:** O(min(k1, k2)) dot product complexity
3. **Space optimization:** Only stores non-zero elements
4. **Simplicity:** Easy to understand and implement
