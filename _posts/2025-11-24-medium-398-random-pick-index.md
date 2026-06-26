---
layout: post
title: "[Medium] 398. Random Pick Index"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp hash-table reservoir-sampling problem-solving
permalink: /posts/2025-11-24-medium-398-random-pick-index/
tags: [leetcode, medium, hash-table, reservoir-sampling, design, randomization]
---
Given an integer array `nums` with possible duplicates, randomly output the index of a given `target` number. You can assume that the given target number must exist in the array.

Implement the `Solution` class:

- `Solution(vector<int>& nums)` Initializes the object with the array `nums`.
- `int pick(int target)` Picks a random index `i` from `nums` where `nums[i] == target`. If there are multiple valid `i`'s, then each index should have an equal probability of returning.

## Examples

**Example 1:**
```
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [3], [3]]
Output
[null, 4, 4, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
```

**Example 2:**
```
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [1], [3], [3]]
Output
[null, 0, 4, 2]

Explanation
solution.pick(1); // Should return 0. Since there's only one element with value 1 in the array.
solution.pick(3); // Should return either index 2, 3, or 4 randomly.
solution.pick(3); // Should return either index 2, 3, or 4 randomly.
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `target` is an integer from `nums`.
- At most `10^4` calls will be made to `pick`.

## Thinking Process

1. **Preprocessing pays off**: One-time O(n) cost amortized over many `pick()` calls

- Identify required operations and their frequency (get/put/insert).
- Combine data structures: hash map + list, heap + map, trie + DFS.
- Amortized O(1) often needs lazy cleanup or doubly-linked lists.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Design pattern</text>

  <rect x="40" y="45" width="70" height="36" rx="4" fill="#D4D8E0" stroke="#8B8680"/><text x="75" y="67" text-anchor="middle" font-size="10">API</text>
  <rect x="150" y="45" width="90" height="36" rx="4" fill="#E0D8E4" stroke="#A098A8"/><text x="195" y="67" text-anchor="middle" font-size="10">hash + list</text>
  <path d="M110 63h36" stroke="#8B8680" stroke-width="2" marker-end="url(#arr2)"/>
  <defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>
  <text x="140" y="105" text-anchor="middle" font-size="11" fill="#6B6560">compose data structures for operations</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Hash map + list** *(this problem)* | O(1) avg | O(n) | LRU cache pattern |
| Heap + hash map | O(log n) | O(n) | LFU, time-based store |
| Trie (prefix tree) | O(m) | O(nm) | Word search, autocomplete |
| Deque / circular buffer | O(1) | O(n) | Queue with fixed capacity |

## Solution

**Time Complexity:** O(n) preprocessing, O(1) per `pick()` call  
**Space Complexity:** O(n)

The key insight is to preprocess the array once during construction, storing all indices for each value in a hash map. This allows O(1) random selection per `pick()` call.

### Solution: Hash Map Approach (Optimized for Multiple Picks)

```cpp
class Solution {
private:
    unordered_map<int, vector<int>> pos;

public:
    Solution(vector<int>& nums) {
        // Preprocess: store all indices for each value
        for(int i = 0; i < (int)nums.size(); i++) {
            pos[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        auto& indices = pos[target];
        // Randomly select one index from the stored indices
        return indices[rand() % indices.size()];
    }
};
```

### Solution Explanation

**Approach:** Hash map + list (this problem)

**Key idea:** 1. **Preprocessing pays off**: One-time O(n) cost amortized over many `pick()` calls

**How the code works:**
1. **Preprocessing pays off**: One-time O(n) cost amortized over many `pick()` calls
- Identify required operations and their frequency (get/put/insert).
- Combine data structures: hash map + list, heap + map, trie + DFS.
- Amortized O(1) often needs lazy cleanup or doubly-linked lists.
## Algorithm Breakdown

### Constructor: Build Index Map

```cpp
Solution(vector<int>& nums) {
    for(int i = 0; i < (int)nums.size(); i++) {
        pos[nums[i]].push_back(i);
    }
}
```

**Why:**
- Iterate through array once: O(n) time
- For each value, store all its indices
- Hash map provides O(1) average lookup time

### Pick Function: Random Selection

```cpp
int pick(int target) {
    auto& indices = pos[target];
    return indices[rand() % indices.size()];
}
```

**Why:**
- Lookup indices for target: O(1) average case
- Random selection: `rand() % size` gives uniform distribution
- Return selected index: O(1) total time

## Why Reservoir Sampling Times Out

### Solution 1: Reservoir Sampling (O(n) per pick)

```cpp
class Solution {
    vector<int>& nums;

public:
    Solution(vector<int>& nums) : nums(nums) {}
    
    int pick(int target) {
        int rtn = -1;
        for(int i = 0, cnt = 0; i < (int)nums.size(); ++i) {
            if(nums[i] == target) {
                ++cnt;
                if(rand() % cnt == 0) {
                    rtn = i;
                }
            }
        }
        return rtn;
    }
};
```

**Time Complexity:** O(n) per `pick()` call  
**Space Complexity:** O(1)

**Why it times out:**
- Each `pick()` call scans entire array: O(n)
- If `pick()` is called `k` times: O(k × n) total time
- With `k = 10^4` and `n = 2×10^4`: **200 million operations** → TIMEOUT

**When to use:**
- Single or few `pick()` calls
- Memory-constrained environments
- Streaming data (can't preprocess)

## Complexity Comparison

| Approach | Constructor | pick() | Total (k calls) | Space | Best For |
|----------|-------------|--------|----------------|-------|----------|
| **Hash Map** | O(n) | O(1) | O(n + k) | O(n) | Multiple picks |
| **Reservoir Sampling** | O(1) | O(n) | O(k × n) | O(1) | Single pick |

**Key Insight:** 
- Hash map: **Amortized cost** per pick is O(1) after preprocessing
- Reservoir sampling: **Per-call cost** is O(n), expensive for many calls

## Implementation Details

### Why Hash Map is Optimal

**For multiple `pick()` calls:**
- Preprocessing: O(n) one-time cost
- Each pick: O(1) lookup + O(1) random selection
- Total for k picks: O(n + k) vs O(k × n) for reservoir sampling

**Example:**
```
n = 20,000, k = 10,000 picks

Hash Map:
  Constructor: 20,000 operations
  Picks: 10,000 operations
  Total: 30,000 operations ✓

Reservoir Sampling:
  Constructor: 0 operations
  Picks: 10,000 × 20,000 = 200,000,000 operations ✗ TIMEOUT
```

### Random Number Generation

```cpp
rand() % indices.size()
```

**Why this works:**
- `rand()` returns pseudo-random integer
- `% size` maps to range [0, size-1]
- Uniform distribution (assuming good RNG)

**Note:** For better randomness, consider:
```cpp
#include <random>
std::random_device rd;
std::mt19937 gen(rd());
std::uniform_int_distribution<> dis(0, indices.size() - 1);
return indices[dis(gen)];
```

## Common Mistakes

1. **Single occurrence**: `pick()` returns the only index
2. **All same values**: All indices have equal probability
3. **Large array**: Hash map handles efficiently
4. **Many pick calls**: Hash map approach scales better

1. **Using reservoir sampling for many picks**: Times out
2. **Not preprocessing**: Rebuilding indices each time
3. **Wrong random selection**: Not using modulo correctly
4. **Memory concerns**: Hash map uses O(n) space, but worth it for speed
5. **Assuming single occurrence**: Must handle multiple indices

## Optimization Tips

1. **Preprocess in constructor**: Build hash map once
2. **Use reference**: `auto& indices` avoids copying
3. **Hash map over array**: O(1) lookup vs O(n) scan
4. **Consider when to use each**: 
   - Many picks → Hash map
   - Single pick → Reservoir sampling

## Related Problems

- [380. Insert Delete GetRandom O(1)](https://www.leetcode.com/problems/insert-delete-getrandom-o1/) - Similar randomization with hash map
- [381. Insert Delete GetRandom O(1) - Duplicates allowed](https://www.leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) - Extension with duplicates
- [528. Random Pick with Weight](https://www.leetcode.com/problems/random-pick-with-weight/) - Weighted random selection
- [710. Random Pick with Blacklist](https://www.leetcode.com/problems/random-pick-with-blacklist/) - Random selection with exclusions

## Real-World Applications

1. **Load Balancing**: Randomly select server from pool
2. **Sampling**: Randomly sample data points
3. **Game Development**: Random item/spawn selection
4. **Testing**: Random test case generation

## Pattern Recognition

This problem demonstrates the **"Preprocessing for Fast Lookup"** pattern:

```
1. Identify repeated operations (pick() called many times)
2. Preprocess data once (build hash map in constructor)
3. Optimize each operation (O(1) lookup instead of O(n) scan)
4. Trade space for time (O(n) space for O(1) time)
```

Similar problems:
- Design data structures with fast operations
- Caching frequently accessed data
- Precomputation for repeated queries

## Why Hash Map Solution is Optimized

**Time Analysis:**
- **Constructor**: O(n) - one-time cost
- **pick()**: O(1) average case - hash lookup + random selection
- **Total for k picks**: O(n + k) - linear in total operations

**Space Analysis:**
- O(n) - stores all indices (at most n indices total)

**Comparison:**
- Reservoir sampling: O(k × n) time for k picks
- Hash map: O(n + k) time for k picks
- **Improvement**: From O(k × n) to O(n + k) = **k times faster** for k picks

## Step-by-Step Trace: `nums = [1, 2, 3, 3, 3]`, `pick(3)` called 3 times

```
Constructor:
  i=0: nums[0]=1 → pos[1] = [0]
  i=1: nums[1]=2 → pos[2] = [1]
  i=2: nums[2]=3 → pos[3] = [2]
  i=3: nums[3]=3 → pos[3] = [2, 3]
  i=4: nums[4]=3 → pos[3] = [2, 3, 4]

pick(3) call 1:
  indices = pos[3] = [2, 3, 4]
  random = rand() % 3 = 1
  return indices[1] = 3

pick(3) call 2:
  indices = pos[3] = [2, 3, 4]
  random = rand() % 3 = 0
  return indices[0] = 2

pick(3) call 3:
  indices = pos[3] = [2, 3, 4]
  random = rand() % 3 = 2
  return indices[2] = 4
```

## Mathematical Proof: Uniform Distribution

**Hash Map Approach:**
- Each index in `indices` array has equal probability
- `rand() % size` gives uniform distribution over [0, size-1]
- Therefore, each index has probability `1/size` ✓

**Reservoir Sampling:**
- For k occurrences, each index i has probability:
  - Selected at position i: `1/i`
  - Not replaced by later indices: `(i/(i+1)) × ((i+1)/(i+2)) × ... × ((k-1)/k)`
  - Product = `1/k` ✓

Both approaches guarantee uniform distribution!

## Key Takeaways

1. **Preprocessing pays off**: One-time O(n) cost amortized over many `pick()` calls
2. **Hash map lookup**: O(1) average case for finding indices
3. **Random selection**: Use `rand() % size` for uniform distribution
4. **Space-time tradeoff**: Use O(n) space to achieve O(1) time per pick

## References

- [LC 398: Random Pick Index on LeetCode](https://www.leetcode.com/problems/random-pick-index/)
- [LeetCode Discuss — LC 398: Random Pick Index](https://www.leetcode.com/problems/random-pick-index/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/random-pick-index/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
