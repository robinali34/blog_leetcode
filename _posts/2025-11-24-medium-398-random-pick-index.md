---
layout: post
title: "[Medium] 398. Random Pick Index"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp hash-table reservoir-sampling problem-solving
permalink: /posts/2025-11-24-medium-398-random-pick-index/
tags: [leetcode, medium, hash-table, reservoir-sampling, design, randomization]
---

# [Medium] 398. Random Pick Index

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Pick operation**: What does pick() do? (Assumption: Randomly selects one index where nums[index] == target, returns that index)

2. **Randomness requirement**: What is the randomness requirement? (Assumption: All indices with target value should have equal probability of being selected)

3. **Return value**: What should pick() return? (Assumption: Integer - randomly selected index where nums[index] == target)

4. **Multiple calls**: Are pick() calls independent? (Assumption: Yes - each call is independent random selection)

5. **Target existence**: Is target guaranteed to exist? (Assumption: Yes - per constraints, target is an integer from nums)

## Solution: Hash Map Preprocessing (Optimized)

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

## How the Algorithm Works

### Key Insight: Preprocessing for Fast Lookup

**Problem:** Need to randomly pick an index where `nums[i] == target` with equal probability.

**Naive Approach:** Scan array each time → O(n) per `pick()` call → **TIMEOUT** if called many times

**Optimized Approach:** 
- Preprocess once: Build hash map of value → list of indices
- Each `pick()` call: O(1) lookup and random selection

### Step-by-Step Example: `nums = [1, 2, 3, 3, 3]`

```
Step 1: Constructor - Build hash map
  pos[1] = [0]
  pos[2] = [1]
  pos[3] = [2, 3, 4]

Step 2: pick(3)
  indices = pos[3] = [2, 3, 4]
  Random index: rand() % 3 could be 0, 1, or 2
  Return indices[random_index] = one of {2, 3, 4}

Step 3: pick(3) again
  Same process, returns a random index from {2, 3, 4}
```

**Visual Representation:**
```
nums = [1, 2, 3, 3, 3]
       0  1  2  3  4

Hash Map:
  1 → [0]
  2 → [1]
  3 → [2, 3, 4]

pick(3): Randomly select from [2, 3, 4]
  - Each index has 1/3 probability
  - Returns 2, 3, or 4 with equal chance
```

## Key Insights

1. **Preprocessing pays off**: One-time O(n) cost amortized over many `pick()` calls
2. **Hash map lookup**: O(1) average case for finding indices
3. **Random selection**: Use `rand() % size` for uniform distribution
4. **Space-time tradeoff**: Use O(n) space to achieve O(1) time per pick

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

## Edge Cases

1. **Single occurrence**: `pick()` returns the only index
2. **All same values**: All indices have equal probability
3. **Large array**: Hash map handles efficiently
4. **Many pick calls**: Hash map approach scales better

## Alternative Approaches

### Approach 2: Reservoir Sampling (For Reference)

**Use when:** Memory is critical or only few picks needed

```cpp
class Solution {
    vector<int>& nums;

public:
    Solution(vector<int>& nums) : nums(nums) {}
    
    int pick(int target) {
        int count = 0;
        int result = -1;
        
        for(int i = 0; i < (int)nums.size(); i++) {
            if(nums[i] == target) {
                count++;
                // With probability 1/count, select current index
                if(rand() % count == 0) {
                    result = i;
                }
            }
        }
        
        return result;
    }
};
```

**How Reservoir Sampling Works:**
- For each occurrence of target, increment count
- With probability `1/count`, replace current selection
- Ensures uniform distribution: each index has `1/k` probability (where k = total occurrences)

**Proof of Uniformity:**
- Index 1 selected with probability: 1/1 = 1
- Index 2 replaces index 1 with probability: 1/2
- Index 3 replaces current with probability: 1/3
- Final probability for index k: (1/k) × (k/(k+1)) × ... × ((n-1)/n) = 1/n

### Approach 3: Two-Pass (Less Efficient)

```cpp
class Solution {
    vector<int> nums;

public:
    Solution(vector<int>& nums) : nums(nums) {}
    
    int pick(int target) {
        // First pass: collect all indices
        vector<int> indices;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == target) {
                indices.push_back(i);
            }
        }
        
        // Second pass: random selection
        return indices[rand() % indices.size()];
    }
};
```

**Why not optimal:**
- Rebuilds indices list on each `pick()` call
- O(n) time per call, same as reservoir sampling
- No preprocessing benefit

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

- [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) - Similar randomization with hash map
- [381. Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) - Extension with duplicates
- [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) - Weighted random selection
- [710. Random Pick with Blacklist](https://leetcode.com/problems/random-pick-with-blacklist/) - Random selection with exclusions

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

---

*This problem demonstrates the importance of choosing the right data structure and algorithm based on usage patterns. For multiple queries, preprocessing with a hash map provides optimal performance.*

