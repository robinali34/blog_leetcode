---
layout: post
title: "[Medium] 528. Random Pick with Weight"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp design binary-search prefix-sum problem-solving
permalink: /posts/2025-11-18-medium-528-random-pick-with-weight/
tags: [leetcode, medium, design, binary-search, prefix-sum, weighted-random]
---

# [Medium] 528. Random Pick with Weight

You are given a **0-indexed** array of positive integers `w` where `w[i]` describes the **weight** of the `i`th index.

You need to implement the function `pickIndex()`, which **randomly** picks an index in the range `[0, w.length - 1]` (inclusive) and returns it. The **probability** of picking an index `i` is `w[i] / sum(w)`.

For example, if `w = [1, 3]`, the probability of picking index `0` is `1 / (1 + 3) = 0.25` (i.e., 25%), and the probability of picking index `1` is `3 / (1 + 3) = 0.75` (i.e., 75%).

## Examples

**Example 1:**
```
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1]],[],[],[],[],[]]
Output
[null,0,0,0,0,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
```

**Example 2:**
```
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the right index (1), and the probability of returning 1 is 3/4 = 0.75.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. The probability of returning 0 is 1/4 = 0.25.
```

## Constraints

- `1 <= w.length <= 10^4`
- `1 <= w[i] <= 10^5`
- `pickIndex` will be called at most `10^4` times.

## Solution: Prefix Sum + Binary Search

**Time Complexity:** 
- Constructor: O(n) - Build prefix sum array
- pickIndex: O(n) linear search or O(log n) binary search

**Space Complexity:** O(n) - Prefix sum array

The key insight is to use prefix sums to create ranges proportional to weights, then use binary search to find the index corresponding to a random value.

### Solution 1: Linear Search

```cpp
class Solution {
private:
    vector<int> prefixSum;

public:
    Solution(vector<int>& w) {
        for(auto n: w) {
            prefixSum.push_back(n + (prefixSum.empty()? 0: prefixSum.back()));
        }
    }
    
    int pickIndex() {
        float randNum = (float) rand() / RAND_MAX;
        float target = randNum * prefixSum.back();
        
        for(int i = 0; i < prefixSum.size(); i++) {
            if(target < prefixSum[i]) return i;
        }
        
        return prefixSum.size() - 1;
    }
};
```

### Solution 2: Binary Search (Optimized)

```cpp
class Solution {
private:
    vector<int> prefixSum;

public:
    Solution(vector<int>& w) {
        for(auto n: w) {
            prefixSum.push_back(n + (prefixSum.empty()? 0: prefixSum.back()));
        }
    }
    
    int pickIndex() {
        float randNum = (float) rand() / RAND_MAX;
        float target = randNum * prefixSum.back();
        
        return lower_bound(prefixSum.begin(), prefixSum.end(), target) - prefixSum.begin();
    }
};
```

## How the Algorithm Works

### Step-by-Step Example: `w = [1, 3, 2]`

```
Constructor:
  prefixSum = []
  n=1: prefixSum.push_back(1 + 0) = [1]
  n=3: prefixSum.push_back(3 + 1) = [1, 4]
  n=2: prefixSum.push_back(2 + 4) = [1, 4, 6]
  
  Ranges:
    Index 0: [0, 1)     → weight 1
    Index 1: [1, 4)     → weight 3
    Index 2: [4, 6)     → weight 2
    Total: 6

pickIndex() call 1:
  randNum = 0.7 (example)
  target = 0.7 * 6 = 4.2
  
  Linear Search:
    i=0: 4.2 < 1? No
    i=1: 4.2 < 4? No
    i=2: 4.2 < 6? Yes → return 2
    
  Binary Search:
    lower_bound([1,4,6], 4.2) → points to index 2
    return 2

pickIndex() call 2:
  randNum = 0.3 (example)
  target = 0.3 * 6 = 1.8
  
  Linear Search:
    i=0: 1.8 < 1? No
    i=1: 1.8 < 4? Yes → return 1
    
  Binary Search:
    lower_bound([1,4,6], 1.8) → points to index 1
    return 1
```

### Visual Representation

```
Weights:     [1,  3,  2]
Prefix Sums: [1,  4,  6]

Range Mapping:
  0    1    4    6
  |----|----|----|
   [0]  [1]  [2]
   
Random value 0.0-6.0 maps to:
  [0.0, 1.0) → Index 0 (weight 1)
  [1.0, 4.0) → Index 1 (weight 3)
  [4.0, 6.0) → Index 2 (weight 2)
```

## Key Insights

1. **Prefix Sum Creates Ranges**: Each index gets a range proportional to its weight
2. **Random Target**: Generate random number in [0, totalSum) range
3. **Binary Search**: Find first prefix sum >= target (O(log n))
4. **Linear Search**: Simpler but slower (O(n))
5. **Probability Proportional**: Larger weights get larger ranges

## Algorithm Breakdown

### Constructor

```cpp
Solution(vector<int>& w) {
    for(auto n: w) {
        prefixSum.push_back(n + (prefixSum.empty()? 0: prefixSum.back()));
    }
}
```

**How it works:**
- Build cumulative prefix sum array
- `prefixSum[i]` = sum of weights from index 0 to i
- Example: `w = [1,3,2]` → `prefixSum = [1,4,6]`

### pickIndex - Linear Search

```cpp
int pickIndex() {
    float randNum = (float) rand() / RAND_MAX;  // [0.0, 1.0)
    float target = randNum * prefixSum.back();   // [0.0, totalSum)
    
    for(int i = 0; i < prefixSum.size(); i++) {
        if(target < prefixSum[i]) return i;
    }
    
    return prefixSum.size() - 1;  // Fallback (shouldn't happen)
}
```

**How it works:**
1. Generate random float in [0.0, 1.0)
2. Scale to [0.0, totalSum)
3. Find first prefix sum >= target
4. Return corresponding index

### pickIndex - Binary Search

```cpp
int pickIndex() {
    float randNum = (float) rand() / RAND_MAX;
    float target = randNum * prefixSum.back();
    
    return lower_bound(prefixSum.begin(), prefixSum.end(), target) 
           - prefixSum.begin();
}
```

**How it works:**
- `lower_bound` finds first element >= target
- Returns iterator, subtract `begin()` to get index
- O(log n) instead of O(n)

## Edge Cases

1. **Single weight**: `w = [1]` → always return 0
2. **Equal weights**: `w = [1,1,1]` → equal probability for all
3. **Very large weight**: `w = [1, 1000000]` → index 1 almost always picked
4. **Single large weight**: `w = [100]` → always return 0

## Alternative Approaches

### Approach 2: Integer Random (More Precise)

**Time Complexity:** O(log n) per pickIndex  
**Space Complexity:** O(n)

```cpp
class Solution {
private:
    vector<int> prefixSum;

public:
    Solution(vector<int>& w) {
        for(int weight : w) {
            prefixSum.push_back(weight + (prefixSum.empty() ? 0 : prefixSum.back()));
        }
    }
    
    int pickIndex() {
        int target = rand() % prefixSum.back() + 1;  // [1, totalSum]
        return lower_bound(prefixSum.begin(), prefixSum.end(), target) 
               - prefixSum.begin();
    }
};
```

**Pros:**
- Uses integer arithmetic (more precise)
- `+1` ensures range [1, totalSum] for proper distribution

**Cons:**
- Slightly different random distribution

### Approach 3: Custom Binary Search

**Time Complexity:** O(log n) per pickIndex  
**Space Complexity:** O(n)

```cpp
class Solution {
private:
    vector<int> prefixSum;

public:
    Solution(vector<int>& w) {
        for(int weight : w) {
            prefixSum.push_back(weight + (prefixSum.empty() ? 0 : prefixSum.back()));
        }
    }
    
    int pickIndex() {
        int target = rand() % prefixSum.back() + 1;
        int left = 0, right = prefixSum.size() - 1;
        
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(prefixSum[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return left;
    }
};
```

**Pros:**
- Explicit binary search implementation
- No STL dependency

**Cons:**
- More verbose than `lower_bound`

## Complexity Analysis

| Approach | Constructor | pickIndex | Space | Pros | Cons |
|----------|-------------|-----------|-------|------|------|
| **Linear Search** | O(n) | O(n) | O(n) | Simple | Slow for many calls |
| **Binary Search (lower_bound)** | O(n) | O(log n) | O(n) | Fast, clean | Requires STL |
| **Custom Binary Search** | O(n) | O(log n) | O(n) | Fast, explicit | More code |

## Implementation Details

### Prefix Sum Construction

```cpp
prefixSum.push_back(n + (prefixSum.empty()? 0: prefixSum.back()));
```

**Why this works:**
- First element: `n + 0 = n`
- Subsequent: `n + previous_sum = cumulative_sum`
- Creates ranges: `[0, prefixSum[0]), [prefixSum[0], prefixSum[1]), ...`

### Random Number Generation

```cpp
float randNum = (float) rand() / RAND_MAX;  // [0.0, 1.0)
float target = randNum * prefixSum.back();  // [0.0, totalSum)
```

**Why float?**
- `rand() / RAND_MAX` gives uniform distribution in [0, 1)
- Multiplying by total sum scales to [0, totalSum)
- Float provides fine-grained selection

### lower_bound Usage

```cpp
lower_bound(prefixSum.begin(), prefixSum.end(), target)
```

**What it does:**
- Returns iterator to first element >= target
- If all elements < target, returns `end()`
- Subtract `begin()` to get index

## Common Mistakes

1. **Wrong random range**: Using `rand() % totalSum` instead of scaling properly
2. **Off-by-one errors**: Not handling edge cases correctly
3. **Integer overflow**: Not considering large weights
4. **Wrong comparison**: Using `<=` instead of `<` in linear search
5. **Not seeding random**: Should call `srand(time(nullptr))` in constructor

## Optimization Tips

1. **Use Binary Search**: Always prefer binary search for O(log n) performance
2. **Integer Random**: Use `rand() % totalSum + 1` for integer precision
3. **Precompute Total**: Store `totalSum` instead of calling `prefixSum.back()` repeatedly
4. **Modern Random**: Consider `<random>` header for better randomness

## Related Problems

- [497. Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) - Similar weighted selection
- [710. Random Pick with Blacklist](https://leetcode.com/problems/random-pick-with-blacklist/) - Random with exclusions
- [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) - Random from set
- [398. Random Pick Index](https://leetcode.com/problems/random-pick-index/) - Random index of target value

## Real-World Applications

1. **Load Balancing**: Weighted random selection of servers
2. **Game Development**: Weighted loot drops, random encounters
3. **Sampling**: Proportional sampling from populations
4. **Recommendation Systems**: Weighted content selection
5. **A/B Testing**: Weighted traffic distribution

## Pattern Recognition

This problem demonstrates the **"Weighted Random Selection"** pattern:

```
1. Build prefix sum array (creates proportional ranges)
2. Generate random number in [0, totalSum)
3. Binary search to find corresponding index
4. Return index
```

Similar problems:
- Random Point in Rectangles
- Weighted sampling
- Proportional selection

## Why Prefix Sum Works

1. **Proportional Ranges**: Each index gets range size = its weight
2. **Non-overlapping**: Ranges don't overlap, covering [0, totalSum)
3. **Uniform Random**: Random number uniformly distributed maps to proportional selection
4. **Efficient Lookup**: Binary search finds index in O(log n)

## Mathematical Proof

For weights `w = [w₀, w₁, ..., wₙ₋₁]`:
- Total sum: `S = Σwᵢ`
- Prefix sums: `P = [w₀, w₀+w₁, ..., S]`
- Random value `r ∈ [0, S)` maps to index `i` where `P[i-1] ≤ r < P[i]`
- Probability of `r` falling in range `[P[i-1], P[i])` = `wᵢ/S` ✓

## Random Number Generation Notes

### Using `rand()`

```cpp
srand(time(nullptr));  // Seed once
int target = rand() % prefixSum.back() + 1;
```

**Pros:**
- Simple, built-in
- Fast

**Cons:**
- Lower quality randomness
- Not thread-safe

### Using `<random>` (Modern C++)

```cpp
#include <random>

class Solution {
private:
    vector<int> prefixSum;
    mt19937 gen;
    uniform_real_distribution<double> dis;

public:
    Solution(vector<int>& w) : gen(random_device{}()), dis(0.0, 1.0) {
        for(int weight : w) {
            prefixSum.push_back(weight + (prefixSum.empty() ? 0 : prefixSum.back()));
        }
    }
    
    int pickIndex() {
        double target = dis(gen) * prefixSum.back();
        return lower_bound(prefixSum.begin(), prefixSum.end(), target) 
               - prefixSum.begin();
    }
};
```

**Pros:**
- Better randomness quality
- Thread-safe
- More control

**Cons:**
- Requires C++11+
- More complex

---

*This problem is an excellent example of combining prefix sums with binary search to achieve efficient weighted random selection, a common pattern in system design and algorithms.*

