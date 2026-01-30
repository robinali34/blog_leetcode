---
layout: post
title: "[Medium] 281. Zigzag Iterator"
date: 2025-12-10 00:00:00 -0800
categories: leetcode algorithm medium cpp design iterator problem-solving
---

# [Medium] 281. Zigzag Iterator

Given two 1d vectors, implement an iterator to return their elements alternately.

## Examples

**Example 1:**
```
Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,3,2,4,5,6].
```

**Example 2:**
```
Input: v1 = [1], v2 = []
Output: [1]
```

**Example 3:**
```
Input: v1 = [], v2 = [1]
Output: [1]
```

## Constraints

- `0 <= v1.length, v2.length <= 1000`
- `1 <= v1.length + v2.length <= 2000`
- `-2^31 <= v1[i], v2[i] <= 2^31 - 1`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Zigzag pattern**: What is the zigzag iteration pattern? (Assumption: Alternate between v1 and v2 - take one element from v1, then one from v2, repeat)

2. **Unequal lengths**: What happens when vectors have different lengths? (Assumption: Continue with remaining elements from the longer vector after shorter one is exhausted)

3. **Empty vectors**: How should we handle empty vectors? (Assumption: Skip empty vectors and continue with non-empty ones)

4. **Iterator interface**: What methods should the iterator support? (Assumption: next() returns next element, hasNext() checks if more elements exist)

5. **Return value**: What should next() return when no elements? (Assumption: Typically throw exception or return sentinel value - but per problem, vectors are non-empty initially)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Store both vectors and maintain two separate indices. Alternate between vectors by checking which one has more elements remaining. When one vector is exhausted, continue with the other. This approach works but becomes complex when handling edge cases like empty vectors or different lengths. The logic for cycling through vectors and tracking positions can be error-prone.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a single array to store all elements in zigzag order during initialization. Flatten the vectors by interleaving elements: take one from v1, one from v2, repeat until both are exhausted. Then implement a simple iterator over this flattened array. This simplifies next() and hasNext() to O(1) operations, but uses O(n) extra space and requires preprocessing time.

**Step 3: Optimized Solution (8 minutes)**

Use a queue-based approach that stores (vector_index, element_index) pairs. Initialize by adding the first position of each non-empty vector to the queue. For next(), pop from the queue, return the element, and if that vector has more elements, push the next position back into the queue. This naturally maintains zigzag order, handles empty vectors gracefully, and easily extends to k vectors. Time complexity is O(1) per operation, and space is O(k) where k is the number of vectors, making it both efficient and extensible.

## Solution 1: Pointer-Based Approach

**Time Complexity:** O(1) for `next()` and `hasNext()`  
**Space Complexity:** O(n) where n is the total number of elements

This approach uses pointers to track the current vector and element position, cycling through vectors in a zigzag pattern.

```cpp
class ZigzagIterator {
private:
    vector<vector<int>> cache;
    int pVec = 0, pElem = 0;
    int totalNum = 0, outputCount = 0;

public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        cache.push_back(v1);
        cache.push_back(v2);
        for(auto& vec: cache) {
            totalNum += vec.size();
        }
    }

    int next() {
        int iterNum = 0;
        while(iterNum < cache.size()) {
            vector<int>& currVec = cache[pVec];
            if(pElem < currVec.size()) {
                int ret = currVec[pElem];
                outputCount++;
                pVec = (pVec + 1) % cache.size();
                if(pVec == 0) {
                    pElem++;
                }
                return ret;
            }
            iterNum++;
            pVec = (pVec + 1) % cache.size();
            if (pVec == 0) {
                pElem++;
            }
        }
        throw runtime_error("No more elements");
    }

    bool hasNext() {
        return outputCount < totalNum;
    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */
```

### How Solution 1 Works

1. **Initialization**: Store both vectors in `cache` and calculate total number of elements
2. **Pointer Management**:
   - `pVec`: Current vector index (0 or 1)
   - `pElem`: Current element index within the vector
3. **Zigzag Pattern**: 
   - Cycle through vectors: `pVec = (pVec + 1) % cache.size()`
   - When we complete a full cycle (`pVec == 0`), increment `pElem`
4. **Skip Empty Vectors**: If current vector is exhausted, skip to next vector
5. **Termination**: Track `outputCount` to know when all elements are returned

## Solution 2: Queue-Based Approach

**Time Complexity:** O(1) for `next()` and `hasNext()`  
**Space Complexity:** O(k) where k is the number of vectors

This approach uses a queue to store pairs of `(vector_index, element_index)`, making it easier to handle vectors of different lengths and extendable to k vectors.

```cpp
class ZigzagIterator {
private:
    vector<vector<int>> cache;
    queue<pair<int, int>> q;

public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        cache.push_back(v1);
        cache.push_back(v2);
        for(int i = 0; i < (int)cache.size(); i++) {
            if(!cache[i].empty()) {
                q.push({i, 0});
            }
        }
    }

    int next() {
        if (!hasNext()) {
            throw runtime_error("No more elements");
        }
        auto [vec_index, elem_index] = q.front();
        q.pop();
        int next_elem_index = elem_index + 1;
        if(next_elem_index < cache[vec_index].size()) {
            q.push({vec_index, next_elem_index});
        }
        return cache[vec_index][elem_index];
    }

    bool hasNext() {
        return !q.empty();
    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */
```

### How Solution 2 Works

1. **Initialization**: Store vectors in `cache` and add initial positions `(vector_index, 0)` for non-empty vectors to the queue
2. **Queue Management**: 
   - Queue stores `(vector_index, element_index)` pairs
   - Each pair represents the next element to be returned from that vector
3. **Next Element**:
   - Pop front of queue to get next element
   - If vector has more elements, push `(vector_index, element_index + 1)` back to queue
4. **Zigzag Pattern**: Queue naturally maintains zigzag order as we cycle through vectors
5. **Termination**: Queue is empty when all elements are processed

## Comparison of Approaches

| Aspect | Pointer-Based | Queue-Based |
|--------|---------------|-------------|
| **Time Complexity** | O(1) | O(1) |
| **Space Complexity** | O(n) | O(k) where k = number of vectors |
| **Extensibility** | Requires modification for k vectors | Easily extends to k vectors |
| **Code Clarity** | More complex pointer logic | Cleaner, more intuitive |
| **Handling Empty Vectors** | Requires skip logic | Automatically handled |

## Example Walkthrough

**Input:** `v1 = [1,2]`, `v2 = [3,4,5,6]`

### Solution 1 (Pointer-Based):
```
Initial: pVec=0, pElem=0, outputCount=0

next(): pVec=0, pElem=0 → return 1, pVec=1, outputCount=1
next(): pVec=1, pElem=0 → return 3, pVec=0, pElem=1, outputCount=2
next(): pVec=0, pElem=1 → return 2, pVec=1, outputCount=3
next(): pVec=1, pElem=1 → return 4, pVec=0, pElem=2, outputCount=4
next(): pVec=0, pElem=2 → skip (out of bounds), pVec=1, pElem=2
next(): pVec=1, pElem=2 → return 5, pVec=0, pElem=3, outputCount=5
next(): pVec=0, pElem=3 → skip, pVec=1, pElem=3
next(): pVec=1, pElem=3 → return 6, outputCount=6

Result: [1,3,2,4,5,6]
```

### Solution 2 (Queue-Based):
```
Initial: q = [(0,0), (1,0)]

next(): pop (0,0) → return 1, push (0,1) → q = [(1,0), (0,1)]
next(): pop (1,0) → return 3, push (1,1) → q = [(0,1), (1,1)]
next(): pop (0,1) → return 2, push (0,2) → q = [(1,1), (0,2)]
next(): pop (1,1) → return 4, push (1,2) → q = [(0,2), (1,2)]
next(): pop (0,2) → return (skip, out of bounds) → q = [(1,2)]
next(): pop (1,2) → return 5, push (1,3) → q = [(1,3)]
next(): pop (1,3) → return 6 → q = []

Result: [1,3,2,4,5,6]
```

## Edge Cases

1. **Empty vectors**: One or both vectors can be empty
2. **Different lengths**: Vectors can have different lengths
3. **Single element**: One vector has only one element
4. **All elements from one vector**: One vector exhausted before the other

## Extending to K Vectors

The queue-based approach easily extends to handle k vectors:

```cpp
class ZigzagIterator {
private:
    vector<vector<int>> cache;
    queue<pair<int, int>> q;

public:
    ZigzagIterator(vector<vector<int>>& vectors) {
        cache = vectors;
        for(int i = 0; i < (int)cache.size(); i++) {
            if(!cache[i].empty()) {
                q.push({i, 0});
            }
        }
    }

    int next() {
        if (!hasNext()) {
            throw runtime_error("No more elements");
        }
        auto [vec_index, elem_index] = q.front();
        q.pop();
        int next_elem_index = elem_index + 1;
        if(next_elem_index < cache[vec_index].size()) {
            q.push({vec_index, next_elem_index});
        }
        return cache[vec_index][elem_index];
    }

    bool hasNext() {
        return !q.empty();
    }
};
```

## Related Problems

- [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) - Iterator pattern for BST
- [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) - Iterator for nested structures
- [251. Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/) - Flatten 2D vector to 1D
- [1424. Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/) - Diagonal traversal pattern

## Pattern Recognition

This problem demonstrates the **"Iterator Design Pattern"**:

```
1. Encapsulate traversal logic in a class
2. Provide hasNext() to check availability
3. Provide next() to retrieve elements
4. Handle edge cases (empty vectors, different lengths)
5. Support extension to multiple data sources
```

Similar patterns:
- Iterator for complex data structures
- Lazy evaluation
- Stream processing

